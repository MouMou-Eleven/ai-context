"""Generate llms.txt and the project-navigation block from the single registries."""
import argparse
import json
from pathlib import Path
import re
from context_common import ROOT

START='<!-- generated-projects:start -->'
END='<!-- generated-projects:end -->'

def outputs(root=ROOT):
    routes=json.loads((root/'repository/navigation/routes.json').read_text(encoding='utf-8-sig'))
    projects=json.loads((root/'repository/navigation/projects.json').read_text(encoding='utf-8-sig'))
    header='''# AI 最小读取路由

<!-- generated-from: repository/navigation/routes.json; do not edit -->

先读[AGENTS.md](./AGENTS.md)，确认目标、对象、交付物与项目身份，再选下面的主入口。一个主任务可自动组合必要依赖，不需要额外说“结合”。关键词仅提供候选；同平台、同课号不证明同项目。

只查状态/位置直接读权威记录；中文创作加[表达短卡](./brain/ai-expression/README.md)。写入/纠错/沉淀先读[更新流程](./repository/ingestion-workflow.md)，AI负责README、引用、状态、路由、结构与校验。详细依赖和排除条件见[routes.json](./repository/navigation/routes.json)，可用context-route.py解释读取建议。

## 按任务找入口

| 任务 | 首读 |
|---|---|
'''
    llms=header+'\n'.join(f"| {r['label']} | [入口](./{r['entry']}) |" for r in routes['routes'])+'\n'
    llms+='''
## 继续读取的条件

- 培训先分会员社群、外部活动或待归属资料。Bug修复课已明确属于外部培训；不凭“第6课”关联社群。创作/复盘读通用经验与风格，状态查询不读整套教学规范。
- AE/MG与AI视频从[制作协作](./work/design/production-workflow.md)双向调用，事实只维护一处；模型、Skill和源码执行时再读，不默认加载全部。
- 纯教学案例不触发销售。招生/销售/商业提案按目的补商业方法；对客户的正式成品补对外交付规范。
- 飞书文档URL不是书籍触发词；百度秒嗒与飞书妙搭先辨平台。书稿读当前出版规则与新旧章映射。
- 当前事实按来源、日期与适用范围核对；较新证据与入口冲突时更新入口。原始材料、历史、供应商源码与大型附件只在核验或执行需要时读。
'''
    table=START+'\n| 领域 | 项目或活动入口 |\n|---|---|\n'+'\n'.join(f"| {p['domain']} | [{p['name']}](../{p['entry']}) |" for p in projects['projects'])+'\n'+END
    path=root/'personal/business-overview.md'
    original=path.read_text(encoding='utf-8-sig')
    if START in original and END in original:
        overview=re.sub(re.escape(START)+r'.*?'+re.escape(END),lambda m:table,original,flags=re.S)
    else:
        begin=original.find('## 当前仓库中的长期项目')
        end=original.find('## 状态使用规则',begin)
        if begin<0 or end<0:
            raise ValueError('Project overview section markers are missing')
        overview=original[:begin]+'## 当前项目与活动入口\n\n'+table+'\n\n'+original[end:]
    return {'llms.txt':llms,'personal/business-overview.md':overview}

def sync(check=False,root=ROOT):
    mismatches=[]
    for name,content in outputs(root).items():
        target=root/name
        actual=target.read_text(encoding='utf-8-sig') if target.exists() else ''
        if actual!=content:
            mismatches.append(name)
            if not check: target.write_text(content,encoding='utf-8',newline='\n')
    return mismatches

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    changed=sync(args.check)
    print(('Stale: ' if args.check else 'Updated: ')+', '.join(changed) if changed else 'Navigation is synchronized.')
    raise SystemExit(1 if args.check and changed else 0)
