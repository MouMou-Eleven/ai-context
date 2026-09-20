"""Explain keyword route candidates without executing capabilities or assigning facts."""
import argparse
import json
from pathlib import Path
import re
from context_common import ROOT
from context_retrieval import checked_scope, enrich, infer_intent, source_pack

def matches(task, needles):
    return not needles or any(str(word).casefold() in task.casefold() for word in needles)


def route_matches(task, route):
    return ((bool(route.get('matchAny')) and matches(task, route['matchAny']))
            or any(re.search(pattern, task, re.I) for pattern in route.get('matchPatterns', [])))

def permitted(task, item, intent, produces_chinese=True, writes_repository=False):
    return (matches(task, item.get('whenAny', []))
            and not (item.get('excludeAny') and matches(task, item['excludeAny']))
            and (not item.get('intents') or intent in item['intents'])
            and (not item.get('requiresChinese') or produces_chinese)
            and (not item.get('requiresWrite') or writes_repository))


def method_matches(task, method, selected_id, intent, produces_chinese):
    """Recommend a method only within its declared purpose and approved scope."""
    return (method.get('status') == 'active'
            and selected_id in method.get('selectedAny', [])
            and intent in method.get('intents', [])
            and produces_chinese
            and permitted(task, method, intent, produces_chinese)
            and all(matches(task, group) for group in method.get('whenAll', [])))

def resolve(task, intent='read', repo_root=ROOT, produces_chinese=None, writes_repository=None, scope=None):
    if intent == 'auto':
        intent = infer_intent(task)
    if scope:
        scope = checked_scope(repo_root, scope)
    catalog = json.loads((repo_root/'system/repository/navigation/routes.json').read_text(encoding='utf-8-sig'))
    if produces_chinese is None:
        produces_chinese = catalog.get('outputPolicy', {}).get('defaultProducesChinese', True)
    if writes_repository is None:
        writes_repository = intent == 'write'
    candidates = [r for r in catalog['routes'] if route_matches(task, r)
                  and not (r.get('excludeAny') and matches(task, r['excludeAny']))]
    candidates.sort(key=lambda r: -r['priority'])
    selected = candidates[0] if candidates else None
    scope_entry = None
    if scope:
        scope_path = repo_root / scope
        scope_entry = scope if scope_path.is_file() else scope.rstrip('/') + '/README.md'
        if not (repo_root / scope_entry).is_file():
            raise ValueError('指定目录没有 README.md，请定位最近的领域入口')
        if not selected:
            owners = [r for r in catalog['routes']
                      if scope_entry.startswith(str(Path(r['entry']).parent).replace('\\', '/') + '/')]
            owners.sort(key=lambda r: -len(str(Path(r['entry']).parent)))
            if owners:
                selected = owners[0]
                candidates.append(selected)
    policy = catalog.get('selectionPolicy', {})
    training_ids = set(policy.get('trainingRouteIds', []))
    teaching = (matches(task, policy.get('trainingTaskWhenAny', []))
                and not matches(task, policy.get('trainingTaskExcludeAny', [])))
    # A course can be the subject of a poster or post without being the requested deliverable.
    output_is_channel_content = (bool(policy.get('channelDeliverableWhenAny'))
                                 and matches(task, policy['channelDeliverableWhenAny']))
    explicit_teaching = (bool(policy.get('explicitTeachingWhenAny'))
                        and matches(task, policy['explicitTeachingWhenAny']))
    if output_is_channel_content and not explicit_teaching:
        teaching = False
    teaching_candidates = [r for r in candidates if r['id'] in training_ids]
    delivery_candidates = [r for r in candidates if r['id'] in policy.get('deliveryRouteIds', [])]
    if teaching and teaching_candidates:
        selected = teaching_candidates[0]
    elif delivery_candidates and selected and selected['id'] in policy.get('capabilityRouteIds', []) + policy.get('projectContextRouteIds', []):
        selected = delivery_candidates[0]
    reads = list(catalog['readFirst'])
    reasons = []
    def include(p, reason):
        if p not in reads:
            reads.append(p)
            reasons.append({'path': p, 'reason': reason})
    if scope_entry:
        include(scope_entry, '用户指定阅读范围；不覆盖实际交付物和项目边界')
    if selected:
        include(selected['entry'], f"主候选: {selected['label']}")
        for dependency in selected.get('dependencies', []):
            if permitted(task, dependency, intent, produces_chinese, writes_repository):
                include(dependency['path'], '主任务的条件依赖')
        project_candidates = [r for r in candidates if r['id'] in policy.get('projectContextRouteIds', [])]
        if project_candidates:
            project = project_candidates[0]
            # A positively identified exclusive course cannot inherit an obsolete project label.
            if selected['id'] not in policy.get('exclusiveProjectIds', []) or project['id'] == selected['id']:
                include(project['entry'], '明确命名项目的事实上下文；仍需核对归属证据')
                for dependency in project.get('dependencies', []):
                    if dependency['path'].startswith('work/projects/') and permitted(task, dependency, intent, produces_chinese, writes_repository):
                        include(dependency['path'], '明确项目的具体事实资料；不把项目全部教学方法附加到宣传稿')
        if teaching or selected in delivery_candidates:
            for capability in candidates:
                if capability['id'] in policy.get('capabilityRouteIds', []):
                    include(capability['entry'], '交付物所涉及的工具/能力说明；不自动执行')
                    for dependency in capability.get('dependencies', []):
                        if dependency['path'].endswith('upstream.json') and permitted(task, dependency, intent, produces_chinese, writes_repository):
                            include(dependency['path'], '能力来源与执行条件')
    else:
        include('README.md', '未匹配：先从当前对话提取目标，不将看仓库误当作维护任务')
        include('work/README.md', '按目标继续领域检索；只有任务本身缺失时才问要做什么')
    for overlay in catalog.get('overlays', []) + catalog.get('genreRules', []):
        if permitted(task, overlay, intent, produces_chinese, writes_repository):
            for p in overlay['paths']:
                include(p, f"附加规则: {overlay['id']}")
    applied_methods = []
    for method in catalog.get('methodRules', []):
        if method_matches(task, method, selected['id'] if selected else None, intent, produces_chinese):
            include(method['path'], '方法建议: ' + method['useWhen'])
            applied_methods.append({'id': method['id'], 'path': method['path'],
                                    'useWhen': method['useWhen'], 'notFor': method['notFor'],
                                    'acceptance': method['acceptance']})
    if intent in {'create', 'write'}:
        include('system/repository/execution-checks.md', '实际成品须把规则转为本次约束并验收最终版本；仅查询或纯维护按适用项执行')
    number_pattern = policy.get('courseNumberPattern')
    course_number = re.search(number_pattern, task) if number_pattern else None
    unresolved_series = bool(course_number and (not selected or selected['id'] not in policy.get('exclusiveProjectIds', [])))
    if unresolved_series:
        include('work/domains/training/materials/README.md', '课号须先匹配所属课程系列与资料来源')
        include('work/domains/training/attribution-and-updates.md', '课号不是全仓库唯一身份；所属系列待核对')
    # Training project routes still need the general creative methods when producing content.
    if selected and (teaching or selected['id'] in training_ids - {'community'}) and intent in {'create','write'}:
        include('work/domains/training/experience/README.md', '培训创作/复盘')
        include('work/domains/training/experience/jianwei-training-style.md', '培训创作/复盘')
        training_route = next((r for r in catalog['routes'] if r['id'] == 'training'), {})
        for dependency in training_route.get('dependencies', []):
            if permitted(task, dependency, intent, produces_chinese, writes_repository):
                include(dependency['path'], '培训共用条件依赖；具体课程和外训共用同一份配置')
    return {'task': task, 'intent': intent, 'producesChinese': produces_chinese, 'writesRepository': writes_repository,
            'courseSeriesUnresolved': unresolved_series,
            'selectedCandidate': selected['id'] if selected else None,
            'methods': applied_methods,
            'candidates': [{'id':r['id'], 'entry':r['entry'],
                            'matched':[n for n in r.get('matchAny', []) if n.casefold() in task.casefold()],
                            'matchedPatterns':[p for p in r.get('matchPatterns', []) if re.search(p, task, re.I)]} for r in candidates],
            'read': reads, 'reasons': reasons,
            'note':('课号所属系列尚待核对，不能默认会员社群或从第几课推定资料身份。' if unresolved_series else '')
                   + '按交付物、项目事实与明确工具分别给出读取建议；关键词不能证明归属。复杂或歧义任务仍须核对来源，不执行工具。'}

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--task',required=True)
    parser.add_argument('--intent',choices=['auto','read','create','write'],default='auto')
    parser.add_argument('--scope', help='可选仓库相对目录或文件；由AI从用户指定板块解析')
    parser.add_argument('--pack', action='store_true', help='附上计划内完整正文、SHA256和未装入清单')
    parser.add_argument('--max-chars', type=int, default=60000, help='正文包字符预算；超出文件明确列为待续读')
    parser.add_argument('--chinese-output', action=argparse.BooleanOptionalAction, default=None,
                        help='Whether the task produces Chinese output; independent of repository writes.')
    parser.add_argument('--write-repository', action=argparse.BooleanOptionalAction, default=None,
                        help='Whether this task changes repository content; defaults to intent=write.')
    args=parser.parse_args()
    try:
        scope = checked_scope(ROOT, args.scope) if args.scope else None
        result = enrich(ROOT, resolve(args.task,args.intent,produces_chinese=args.chinese_output,
                                     writes_repository=args.write_repository,scope=scope),scope)
        if args.pack:
            result['sourcePack'] = source_pack(ROOT, result, args.max_chars)
        print(json.dumps(result,ensure_ascii=False,indent=2))
    except ValueError as error:
        parser.error(str(error))
