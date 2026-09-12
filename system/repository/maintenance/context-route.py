"""Explain keyword route candidates without executing capabilities or assigning facts."""
import argparse
import json
from pathlib import Path
import re
from context_common import ROOT

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

def resolve(task, intent='read', repo_root=ROOT, produces_chinese=None, writes_repository=None):
    catalog = json.loads((repo_root/'system/repository/navigation/routes.json').read_text(encoding='utf-8-sig'))
    if produces_chinese is None:
        produces_chinese = catalog.get('outputPolicy', {}).get('defaultProducesChinese', True)
    if writes_repository is None:
        writes_repository = intent == 'write'
    candidates = [r for r in catalog['routes'] if route_matches(task, r)
                  and not (r.get('excludeAny') and matches(task, r['excludeAny']))]
    candidates.sort(key=lambda r: -r['priority'])
    selected = candidates[0] if candidates else None
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
        if teaching or selected in delivery_candidates:
            for capability in candidates:
                if capability['id'] in policy.get('capabilityRouteIds', []):
                    include(capability['entry'], '交付物所涉及的工具/能力说明；不自动执行')
                    for dependency in capability.get('dependencies', []):
                        if dependency['path'].endswith('upstream.json') and permitted(task, dependency, intent, produces_chinese, writes_repository):
                            include(dependency['path'], '能力来源与执行条件')
    else:
        include('work/README.md', '未匹配，人工按目标与证据继续路由')
    for overlay in catalog.get('overlays', []) + catalog.get('genreRules', []):
        if permitted(task, overlay, intent, produces_chinese, writes_repository):
            for p in overlay['paths']:
                include(p, f"附加规则: {overlay['id']}")
    number_pattern = policy.get('courseNumberPattern')
    course_number = re.search(number_pattern, task) if number_pattern else None
    unresolved_series = bool(course_number and (not selected or selected['id'] not in policy.get('exclusiveProjectIds', [])))
    if unresolved_series:
        include('work/domains/training/materials/README.md', '课号须先匹配所属课程系列与资料来源')
        include('work/domains/training/attribution-and-updates.md', '课号不是全仓库唯一身份；所属系列待核对')
    # Training project routes still need the general creative methods when producing content.
    if selected and (teaching or selected['id'] in {'training','external-training','bug-lesson'}) and intent in {'create','write'}:
        include('work/domains/training/experience/README.md', '培训创作/复盘')
        include('work/domains/training/experience/jianwei-training-style.md', '培训创作/复盘')
    return {'task': task, 'intent': intent, 'producesChinese': produces_chinese, 'writesRepository': writes_repository,
            'courseSeriesUnresolved': unresolved_series,
            'selectedCandidate': selected['id'] if selected else None,
            'candidates': [{'id':r['id'], 'entry':r['entry'],
                            'matched':[n for n in r.get('matchAny', []) if n.casefold() in task.casefold()],
                            'matchedPatterns':[p for p in r.get('matchPatterns', []) if re.search(p, task, re.I)]} for r in candidates],
            'read': reads, 'reasons': reasons,
            'note':('课号所属系列尚待核对，不能默认会员社群或从第几课推定资料身份。' if unresolved_series else '')
                   + '按交付物、项目事实与明确工具分别给出读取建议；关键词不能证明归属。复杂或歧义任务仍须核对来源，不执行工具。'}

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--task',required=True)
    parser.add_argument('--intent',choices=['read','create','write'],default='read')
    parser.add_argument('--chinese-output', action=argparse.BooleanOptionalAction, default=None,
                        help='Whether the task produces Chinese output; independent of repository writes.')
    parser.add_argument('--write-repository', action=argparse.BooleanOptionalAction, default=None,
                        help='Whether this task changes repository content; defaults to intent=write.')
    args=parser.parse_args()
    print(json.dumps(resolve(args.task,args.intent,produces_chinese=args.chinese_output,
                             writes_repository=args.write_repository),ensure_ascii=False,indent=2))
