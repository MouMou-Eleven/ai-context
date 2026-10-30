# video-shotcraft：产品宣传片镜头库

第三方 Skill，作者 Vincent Wei，上游 [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)，Apache 2.0，可商用。固定版本见 [upstream.json](upstream.json)。

## 能做什么

- 用网站、软件、App 的**真实页面截图**做电影感的产品宣传片（Remotion 代码渲染）。
- 124 张镜头配方卡，每张有 demo 源码和动态样片：运镜、转场、字体动效、数据展示、开场、收尾等。可以只抽一张卡，做任何片子里的某一个镜头。
- 一支已验收的成片模板 Ink Press，可以直接替换产品截图和文案。
- 音效检索（Freesound）、BGM 备选、卡点，以及一套判例式审美准则自检。

## 什么时候用（可灵活）

| 用 | 不用 |
|---|---|
| 客户要网站、SaaS、App 的产品宣传片或功能介绍片 | 教师微课、科普讲解（走[微课与教育交互](../../../design/video/education/README.md)或 [anything2explainer](../anything2explainer/README.md)） |
| 某一个镜头想要成熟的运镜、转场、数据或字体动效 | 只写 AI 视频提示词（走 [Seedance](../../../design/video/common/seedance/README.md)） |
| 给已经做好的片子找音效、对齐声音 | — |

调用时它会先让你在三种模式里选：直接套 Ink Press 模板、AI 自主创作、共同创作（逐步确认）。建委要掌控方向的商单，选共同创作。

**Ink Press 的外观是这个 Skill 的样式，不是建委的默认风格。** 借它的流程、镜头卡和检查方法，配色、字体、版式按本次内容定（见[代码式视频设计经验 · 复用的是手法](../../../design/common/code-driven-video/README.md#复用的是手法不是样式红线)）。交付前仍按[代码式视频设计经验](../../../design/common/code-driven-video/README.md)的检查表验收。

## 怎么调用

- 本机已按 upstream.json 的 commit 安装到 Claude Code 和 Codex 的 skills 目录（路径见其中的 installPaths）。Claude Code 里说“用 video-shotcraft 做……”或直接描述产品宣传片需求即可触发；Codex 同样从它的 skills 目录读取。
- 运行需要 Node.js 18+、npm、ffmpeg。第一次渲染前在工程目录 `npm install`。
- 换电脑或本机没有时：`git clone` 上游仓库，`git checkout <upstream.json 里的 commit>`，把整个目录复制到上面两个 skills 目录。

## 更新

先看上游新 commit 的许可、依赖和行为有没有变，再整体重装并更新 upstream.json 的 commit 和日期。不手改已安装的实体。

## 来源与状态

建委 2026-10-30 指定收录。已安装并确认 Claude Code 能识别；还没有用它做过建委的订单，第一次实际出片后在这里补一句效果和注意事项。它的审美准则里与本仓经验一致的条目（节奏、特效分寸、字幕字高等）已并入[动效与验收](../../../design/common/code-driven-video/motion-and-verification.md)和[排版与尺寸](../../../design/common/code-driven-video/layout-and-sizing.md)。
