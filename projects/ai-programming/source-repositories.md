# AI 编程源码仓库索引

> 状态：当前有效
> 最近核验：2026-08-10

本文件只记录源码仓库的入口、职责和读取顺序。项目源码、生产素材和构建产物不进入 `ai-context`；`ai-context` 继续作为长期事实、方法、决策与协作规则中枢。

## 独立源码仓库

| 仓库 | 用途 | 项目目录 |
|---|---|---|
| [MouMou-Eleven/ai-programming-development](https://github.com/MouMou-Eleven/ai-programming-development) | AI 编程项目的可复现源码、运行时生产素材、测试和构建配置 | `projects/hunshi-moniu/`：混世魔牛游戏；`projects/jianwei-portfolio/`：杨建委个人网站 |

该仓库与 [MouMou-Eleven/ai-context](https://github.com/MouMou-Eleven/ai-context) 相互独立：

- 需要继续开发、拉取源码、运行测试或构建项目时，读取 `ai-programming-development` 对应项目目录的 README。
- 需要了解长期口径、百度秒哒交付方法、历史决策或 AI 协作规则时，读取 `ai-context` 对应入口。
- 新项目源码继续放入独立源码仓库的 `projects/`；只在本文件增加索引，不把完整源码重复放入 `ai-context`。
- 原始制作母版、未引用素材、依赖目录、密钥和本机临时文件默认不进入 GitHub；项目 README 必须说明本地归档位置和重新生成方式。

## 当前读取顺序

1. 先在本文件确认目标源码仓库和项目目录。
2. 读取目标项目 README、锁文件、测试与构建命令。
3. 涉及百度秒哒分包、对象存储、数据库或部署时，再读 [miaoda/patterns/codex-source-package-deployment.md](./miaoda/patterns/codex-source-package-deployment.md)。
4. 修改后先完成测试和生产构建，再提交源码仓库；形成可复用方法或长期口径时，再同步更新 `ai-context`。
