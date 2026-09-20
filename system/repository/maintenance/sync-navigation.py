"""Generate short entry points and related-asset links from the single registries."""
import argparse
import json
import os
from pathlib import Path
import re
from context_common import ROOT, NAVIGATION, read_json, write_text


def link(owner, target):
    return Path(os.path.relpath(target, Path(owner).parent)).as_posix()


def block(original, name, body):
    start, end = f'<!-- generated-{name}:start -->', f'<!-- generated-{name}:end -->'
    replacement = start + '\n' + body.rstrip() + '\n' + end
    if (start in original) != (end in original):
        raise ValueError(f'Incomplete generated-{name} markers')
    if start in original:
        return re.sub(re.escape(start) + r'.*?' + re.escape(end), lambda match: replacement, original, flags=re.S)
    return original.rstrip() + '\n\n' + replacement + '\n'


def asset_table(owner, items, heading):
    rows = [heading, '', '| 类型 | 项目或案例 | 适用领域 |', '|---|---|---|']
    for item in items:
        rows.append(f"| {item.get('kind', '项目')} | [{item['name']}]({link(owner, item['entry'])}) | {item['domain']} |")
    return '\n'.join(rows).lstrip() + '\n'


def outputs(root=ROOT):
    root = Path(root).resolve()
    routes = json.loads(read_json(root / NAVIGATION / 'routes.json'))
    registry = json.loads(read_json(root / NAVIGATION / 'projects.json'))
    projects = registry['projects']
    cases, archived = registry.get('cases', []), registry.get('archivedProjects', [])
    guide_path = NAVIGATION + '/task-guide.md'
    result = {
        'llms.txt': '''# AI Context 读取入口

<!-- generated-from: system/repository/navigation/routes.json; do not edit -->

先读[AGENTS](./AGENTS.md)，再用[任务指南](./system/repository/navigation/task-guide.md)进入领域、项目或能力。中文输出遵守[表达短卡](./system/expression/README.md)；写入仓库同时执行[更新流程](./system/repository/ingestion-workflow.md)。简单查询只读必要事实；关键词不能证明课程归属。

制作成品执行[写前约束与最终版本验收](./system/repository/execution-checks.md)。读到规则不算已遵循，格式解析不算内容合格；分享课件默认学员可见，时长安排不进入正文。

不要求用户报文件名：从当前对话提取任务，进入板块后继续读适用正文。可用检索工具的自然任务计划、板块内候选与正文包；网页宿主按任务指南手动走同一链路。仅说“看仓库”不等于要做仓库维护。
'''
    }
    guide = '''# 按任务读取仓库

<!-- generated-from: routes.json; do not edit -->

主任务决定需要哪种方法，明确项目提供事实；Skill和工具按步骤调用。目录不是读取边界，方法与事实正文都只维护一份。

用户指定文件夹时，先读最近README，再实际读本次方法正文与必要依赖；关键词脚本不是完整阅读器，不以目录列表代替理解。

先核对目标、对象、交付物和项目身份，再选择下面的入口。自然语句匹配仅给候选，不能从同课号、平台或相似主题推定归属。

## 不用用户指定文件的读取步骤

1. 从当前对话提取“要做什么成品、给谁、遇到什么问题、已确认哪个项目”。用户说“参考仓库”时沿用正在做的任务；不能仅将这四个字传给检索器。有多个成品分别处理。
2. 先按下表选择入口。用户指定目录就读该README，再按目的读子目录；指定目录不是禁止跨域补依赖，也不能由工具名称推定项目。
3. 读取适用方法正文后，查看本次材料还有哪些问题未覆盖；用这些问题词检索。搜索结果须核对当前状态、适用/排除条件和来源，再决定采用。不要一次载入整个目录、历史或Skill源码。
4. 制作前完成[执行卡](../execution-checks.md)：实际读过的文件、对应本次动作、最终检查位置。目录标题、命中摘要和路径列表不算已读经验。
5. 已覆盖读者、方法、工具限制、明确项目事实和验收动作就开始做；新问题出现再补读。只在任务目标或关键事实真的缺失时询问，不让用户负责找文件。

本地可运行：`python system/repository/maintenance/context-route.py --task "参考仓库，用秒哒开发大视频上传页面" --pack`。AI可补`--scope work/domains/self-media`限定用户指定的板块；默认推断读/创作/沉淀，也可显式指定`--intent`。此命令只读，不执行其中建议的工具或发布。

输出`read`是必需阅读计划，`discovery`是带片段和行号的待判断候选，`sourcePack`是计划内正文及hash；预算不足的文件明确标为待续读，不截断冒充完整。新正文直接参与检索，无需另建向量库或手动索引。关键词和全文排序不能代替语义判断；不适用方法、历史和原始素材不自动升级成规则。

只有网页访问时，按相同步骤读取根AGENTS、对应README、子目录和方法正文；用仓库文件搜索补查任务词与同义词。无法实际打开的文件列为未读取，不宣称已经参考。没有任何任务描述时，先展示四入口并问要完成什么，不盲读全仓。

| 任务 | 主入口 |
|---|---|
'''
    guide += '\n'.join(f"| {item['label']} | [读取]({link(guide_path, item['entry'])}) |" for item in routes['routes']) + '\n'
    guide += '\n## 常用板块的继续读取条件\n\n下表与脚本使用同一依赖配置；条件命中后读正文，只查事实不套创作方法。其他板块按各自README继续。\n\n| 主入口 | 条件（任一线索，仍需判断语义） | 用途 | 继续读 |\n|---|---|---|---|\n'
    for item in routes['routes']:
        if item['id'] not in {'miaoda', 'programming', 'self-media', 'training'}:
            continue
        for dependency in item.get('dependencies', []):
            condition = '、'.join(dependency.get('whenAny', [])) or '本类任务'
            if dependency.get('excludeAny'):
                condition += '；排除：' + '、'.join(dependency['excludeAny'])
            purpose = '创作/修改/沉淀' if dependency.get('intents') == ['create', 'write'] else '按所查问题'
            guide += f"| {item['label']} | {condition} | {purpose} | [正文]({link(guide_path, dependency['path'])}) |\n"
    guide += '''
## 条件组合

- 实际成品执行[写前约束与最终验收](../execution-checks.md)，记录本次接收者、规则来源、材料覆盖和检查证据；无论最终写入飞书还是本地都适用。
- “产生中文输出”和“写入仓库”分别判断。修改并沉淀课件时，两类规则同时成立；只移动文件不读取整套写作资料。
- 中文输出先用[表达短卡](../../expression/README.md)，按成品选择[体裁标准](../../expression/genres.md)中的一项；简单回答遵守短卡即可。实际专业方法来自对应领域，不能把所有体裁全文一起载入。
- 产品介绍、社群宣传和报名页组合[读者问题方法](../../../work/domains/self-media/marketing-copy/reader-question-led-promotion.md)与明确项目事实；验问题是否值得问、答案是否回应，不把营销问答套进纯教学。
- 培训先分会员社群、外部活动或待归属材料；Bug修复课已确认外训，局部“第6课”不决定系列。教学演示不默认叠加销售。
- 设计统一按交付物进入平面、宣传、教育或故事方向。MG、AE、AI生成是制作方法，单独提MG不等于教师或社群课程。
- 项目位置与来源在[登记表](./projects.json)维护；领域README的相关项目、案例由同一登记生成。状态与结果须回正文核验。
- 书稿按明确项目读取当前章与编辑规则。泛称写书不自动确认就是飞书书；百度秒哒不使用飞书妙搭接口。
- [写入流程](../ingestion-workflow.md)由AI负责更新正文、相关入口、登记、结构及校验；历史、语料和Skill源码只在核验或执行需要时展开。

可用[路由辅助脚本](../maintenance/context-route.py)解释候选与依赖。它不执行工具，也不证明所有AI宿主已读取或遵守规则。
'''
    result[guide_path] = guide

    def update(name, marker, body):
        original = result.get(name)
        if original is None:
            original = (root / name).read_text(encoding='utf-8-sig')
        result[name] = block(original, marker, body)

    update('work/projects/README.md', 'projects', asset_table('work/projects/README.md', projects, '## 当前项目与活动入口'))
    update('work/projects/cases/README.md', 'cases', asset_table('work/projects/cases/README.md', cases, '## 已收录案例'))
    update('work/projects/archive/README.md', 'archived-projects', asset_table('work/projects/archive/README.md', archived, '## 已归档入口'))
    related = {}
    for item in projects + cases:
        for owner in item.get('domainEntries', []):
            related.setdefault(owner, []).append(item)
    # Remove stale rows when an asset loses a domain relationship.
    for path in (root / 'work/domains').rglob('README.md'):
        if '<!-- generated-related-assets:start -->' in path.read_text(encoding='utf-8-sig'):
            related.setdefault(path.relative_to(root).as_posix(), [])
    for owner, items in related.items():
        body = asset_table(owner, items, '## 相关项目与案例') if items else '## 相关项目与案例\n\n暂无已登记关联；不能据此断言没有未登记材料。'
        update(owner, 'related-assets', body)
    # Method discovery is generated from the same conditions used by the CLI.
    # Only short purpose/boundary cards are repeated; the method body stays in one file.
    method_owners = {guide_path: []}
    for method in routes.get('methodRules', []):
        if method.get('status') == 'active':
            method_owners[guide_path].append(method)
            for owner in method.get('entryPoints', []):
                method_owners.setdefault(owner, []).append(method)
    for path in root.rglob('README.md'):
        if '.git' not in path.parts and '<!-- generated-methods:start -->' in path.read_text(encoding='utf-8-sig'):
            method_owners.setdefault(path.relative_to(root).as_posix(), [])
    for owner, methods in method_owners.items():
        rows = ['## 按实际需要选择方法', '',
                '由routes.json生成。先判断本次成品和读者，再按下表实际需要读取方法正文；无需点名作者。多种方法可分工，但同一段不拼接相互冲突的结构。没有适用需求时跳过，不能因看到本表就全部加载。', '',
                '| 需要解决什么 | 方法正文 | 不适用／保留边界 | 成品怎样检查 |', '|---|---|---|---|']
        rows.extend(f"| {m['useWhen']} | [{m['label']}]({link(owner, m['path'])}) | {m['notFor']} | {m['acceptance']} |" for m in methods)
        if not methods:
            rows.append('| 当前无已登记适用方法 | 按实际领域正文判断 | 不根据旧表自动激活 | 核对来源与当前任务 |')
        update(owner, 'methods', '\n'.join(rows))
    return result


def sync(check=False, root=ROOT):
    mismatches = []
    for name, content in outputs(root).items():
        target = root / name
        actual = target.read_text(encoding='utf-8-sig') if target.exists() else ''
        if actual != content:
            mismatches.append(name)
            if not check:
                write_text(target, content)
    return mismatches


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--root', type=Path, default=ROOT)
    args = parser.parse_args()
    changed = sync(args.check, args.root.resolve())
    print(('Stale: ' if args.check else 'Updated: ') + ', '.join(changed) if changed else 'Navigation is synchronized.')
    raise SystemExit(1 if args.check and changed else 0)
