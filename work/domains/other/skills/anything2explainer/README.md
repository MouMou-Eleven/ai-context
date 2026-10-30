# anything2explainer：MG 科普讲解片

第三方 Skill，作者 Vincent Wei，上游 [Vincentwei1021/anything2explainer](https://github.com/Vincentwei1021/anything2explainer)。固定版本见 [upstream.json](upstream.json)。

## 许可（红线）

**PolyForm Noncommercial 1.0.0：非商业使用免费，任何商业使用都要事先取得作者授权。** 用它做出来的视频归制作者，但用这个工具接客户的付费单属于商业使用。建委自己的学习、研究、非商业内容可以直接用；客户商单先联系作者授权，没有授权时只借它的方法（分镜、构图与光、QC 判据），不跑它的模板和代码。

## 能做什么

- 给一个知识主题或一篇文章，做成一条黑底 MG 风格的科普讲解片：配音、字幕、章节进度条，每一帧用 Remotion 代码画。时长由用户定，常用 3—5 分钟。
- 自带可编译模板、图元库、配音与时间轴脚本、分镜工具。
- 多 agent 分工协议和量化 QC：主角尺寸、光跟主角、末拍停留、最长静止时间都有脚本检查。
- 完整样片《RAG 与知识库》作为质量标尺。

## 什么时候用（可灵活）

| 用 | 不用 |
|---|---|
| 建委自己的非商业科普内容；已获授权的客户讲解片 | 未获授权的客户商单 |
| 想借它的分镜、构图与光、QC 判据检查自己的讲解片 | 真人口播、实拍为主的片子 |
| 把一篇技术文章改成讲解视频 | 教师微课（走[微课与教育交互](../../../design/video/education/README.md)，教学结构由那边定） |

它会在四个确认点停下来等用户：时长和语言、解说词定稿、配音选择、前 30 秒样片。

**黑底、紫光、超粗黑体是这个 Skill 的固定样式，不是建委的默认风格。** 交付前仍按[代码式视频设计经验](../../../design/common/code-driven-video/README.md)的检查表验收。

## 怎么调用

- 本机已按 upstream.json 的 commit 安装到 Claude Code 和 Codex 的 skills 目录（路径见其中的 installPaths）。在 Claude Code 里说“做一条讲 ×× 的科普视频”即可触发；Codex 同样从它的 skills 目录读取。
- 运行需要 Node.js 18+、ffmpeg、Python 3（edge-tts、numpy、pillow、scipy），每片约 2GB 磁盘。
- 换电脑或本机没有时：`git clone` 上游仓库，`git checkout <upstream.json 里的 commit>`，复制到上面两个 skills 目录。

## 更新

先看上游新 commit 的许可、依赖和行为有没有变，再整体重装并更新 upstream.json。不手改已安装的实体。

## 来源与状态

建委 2026-10-30 指定收录。已安装并确认 Claude Code 能识别；还没有用它出过片。它的构图与光、持续动作和停留规则中与本仓经验一致的部分已并入[动效与验收](../../../design/common/code-driven-video/motion-and-verification.md)和[排版与尺寸](../../../design/common/code-driven-video/layout-and-sizing.md)。
