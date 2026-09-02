# AI 编程项目

> 保存建委实际开发或长期维护的项目。完整源码通常位于独立代码仓库，本上下文仓库只保存项目事实、边界和决策。

## 当前项目

| 项目 | 上下文入口 | 源码状态 |
|---|---|---|
| 言剪 AI | [`yancut-ai/`](./yancut-ai/README.md) | 本地持续开发；独立私有源码仓库 `MouMou-Eleven/yancut-ai` 已建立并同步 |
| 混世魔牛游戏 | 本目录仅保留索引 | 统一源码仓库中的 `projects/hunshi-moniu/` |
| 杨建委个人网站 | 本目录仅保留索引 | 统一源码仓库中的 `projects/jianwei-portfolio/` |

## 已确认的独立源码仓库

| 仓库 | 项目目录 | 使用边界 |
|---|---|---|
| [`MouMou-Eleven/yancut-ai`](https://github.com/MouMou-Eleven/yancut-ai) | 独立仓库根目录 | 言剪 AI 权威源码；本仓库只保存事实、决策、修订与继续开发规则 |
| [`MouMou-Eleven/ai-programming-development`](https://github.com/MouMou-Eleven/ai-programming-development) | `projects/hunshi-moniu/`、`projects/jianwei-portfolio/` | 继续开发、测试或构建时读取对应项目 README；源码不复制进本仓库 |

## 规则

- `ai-context` 保存“为什么做、当前口径、关键决策和如何继续”，不保存完整源码副本。
- 新项目必须说明源码位置、公开状态、当前基线和待确认事项。
- 只讨论某个项目时，不自动加载其他项目或全部编程工具。
- 涉及百度秒哒分包与部署时，按需读取 [`../tools/miaoda/experience/patterns/codex-source-package-deployment.md`](../tools/miaoda/experience/patterns/codex-source-package-deployment.md)。
- “AI 六十甲子古音律与 IP 孵化”是文化产品与 IP 项目，权威入口在 [`../../../other/ai-sixty-jiazi-music-ip/`](../../../other/ai-sixty-jiazi-music-ip/README.md)；不得因其中包含 Web 开发而在本目录建立重复项目。
