# 仓库运行与维护

这里放仓库本身的规则和工具。日常读写的核心规则在根目录 [AGENTS.md](../../AGENTS.md)，本目录是它的展开和配套工具。

## 仓库怎么分

| 入口 | 放什么 | 不放什么 |
|---|---|---|
| [personal/](../../personal/README.md) | 建委是谁：身份、经历、荣誉、业务概要 | 做事方法、项目进度 |
| [brain/](../../brain/README.md) | 建委怎么想：原则、偏好、判断方式（抽象的，起统领作用） | 具体项目、操作步骤 |
| [work/domains/](../../work/domains/README.md) | 建委会做什么：设计、开发、培训、自媒体、商业化等领域的方法 | 某个项目的事实 |
| [work/projects/](../../work/projects/README.md) | 建委在做什么：长期项目的事实、进度、决定 | 能用到别处的通用方法 |
| [system/](../README.md) | 怎么跟 AI 协作：表达标准、仓库规则、设备环境 | 建委的个人观点 |

AI 在各领域里是工具或主题，不单独成为一个大类。比如"用 AI 做 PPT"放在设计的 PPT 目录里，"讲 AI 办公"放在培训里。

## 本目录的文件

| 文件 | 作用 |
|---|---|
| [ingestion-workflow.md](./ingestion-workflow.md) | 往仓库写东西的规范：值不值得写、放哪、怎么改、怎么同步 |
| [execution-checks.md](./execution-checks.md) | 用仓库经验做成品后怎么自查 |
| [versioned-knowledge-policy.md](./versioned-knowledge-policy.md) | 平台功能、价格这类会变的事实怎么管 |
| [capability-evidence.md](./capability-evidence.md) | 什么情况下能说建委"会"某项能力 |
| [templates/](./templates/README.md) | 项目、场次、方法的记录模板 |
| [navigation/](./navigation/README.md) | 项目登记、路由配置、完整文件结构（含桌面 HTML 的来源） |
| [maintenance/](./maintenance/README.md) | 校验、生成、改链接、桌面同步的脚本 |
| [revisions/](./revisions/README.md) | 仓库结构的重大变化记录（普通改动看 Git 历史） |

技术文件：[.gitignore](../../.gitignore)、[.gitattributes](../../.gitattributes)、[GitHub 自动校验](../../.github/workflows/context-validation.yml)、[llms.txt](../../llms.txt) 和 [CLAUDE.md](../../CLAUDE.md)（不同 AI 工具会自动读的入口文件，内容都只是"去读 AGENTS.md"，保证换什么模型都按同一套规则）。

## 桌面结构页

`navigation/STRUCTURE.html` 是可展开、可搜索的仓库结构页。每次提交后，Git hook 会把它复制到桌面上的"GitHub仓库完整结构.html"，建委平时靠它查看仓库。本地仓库需要启用 hooks：

```text
git config core.hooksPath system/repository/maintenance/git-hooks
```

手动同步：`python -B system/repository/maintenance/desktop-sync.py`。

## 以后怎么检验仓库好不好用

用真实任务检验，不看文件数量。每次大改之后，用几句建委平时的说法（比如"看我的仓库，帮我写一份给银行的 AI 办公课件"），在一个全新的对话里测：AI 有没有找到对的文件、有没有用上里面的经验、成品有没有违反红线。发现漏读，就改 AGENTS.md 的任务表或对应 README；发现读了还犯错，就把规则改得更具体。
