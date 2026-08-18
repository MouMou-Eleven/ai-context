# Repository — 仓库治理与维护

> 本目录说明这个长期 AI 上下文仓库怎样分类、怎样更新、怎样保持安全和可追溯。

## 文件索引

| 入口 | 内容 | 何时读取 |
|---|---|---|
| [`../STRUCTURE.md`](../STRUCTURE.md) | 全仓目录、文件职责、写入位置和状态规范 | 新增、移动或重构文件前 |
| [`../AGENTS.md`](../AGENTS.md) | AI 协作、事实优先级和特殊项目规则 | AI 进入仓库时 |
| [`../llms.txt`](../llms.txt) | AI 最小读取路由 | 每次任务开始时 |
| [`environment/README.md`](./environment/README.md) | 电脑、网络和本地工具环境入口 | 处理本机环境问题时 |
| [`versioned-knowledge-policy.md`](./versioned-knowledge-policy.md) | 秒哒等动态产品知识的新旧版本治理 | 记录产品功能、价格、界面、API 或平台规则时 |
| [`maintenance/README.md`](./maintenance/README.md) | 校验脚本和提交前检查方法 | 修改仓库后 |
| [`revisions/README.md`](./revisions/README.md) | 仓库级信息架构和治理变化索引 | 追溯仓库结构变化时 |

## 根目录例外

根目录只保留 `README.md`、`AGENTS.md`、`llms.txt` 和 `STRUCTURE.md` 四个机器与人类都需要快速发现的入口。它们是路由文件，不承担零碎内容沉淀。
