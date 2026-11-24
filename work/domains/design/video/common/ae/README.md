# AI 接入 AE

AI 通过 MCP 操作本机的 After Effects：读工程、改模板、做动画和包装、渲染出片。它是 AI 出视频的四种做法之一，另三种是 [AI 生成](../ai-generation/README.md)、[代码生成](../code-generation/README.md)和 [AI 操作 Blender](../blender/README.md)；四种怎么选见[视频共用方法](../README.md#四种做法怎么选默认)，写入和触发见[视频共用方法 · 写入与触发](../README.md#写入与触发默认)。适合借现成模板的高完成度效果（证书墙、粒子、插件光效、三维相机），MG、自媒体、企业片、创赛片都一样。

| 内容 | 入口 | 什么时候用 |
|---|---|---|
| 用模板时的设计判断：先设计版面再用模板实现、模板文字组件要用上、只用对应一段、光效倒影对位、新加层做进模板，以及改模板验收表 | [改 AE 模板的设计判断](./ae-template-design.md) | 拿现成 AE 模板做画面 |
| 怎么连 AE、本机两个 AE MCP 怎么挑、先用自带工具不自己写脚本、操作和渲染的坑、在 AE 里定位闪的层 | [AI 与 AE 协作](./ai-ae-collaboration.md) | 任何要动 AE 工程的时候 |
| AE 弹窗守护（命令行后备用） | [tools/ae_dialog_guard.py](./tools/ae_dialog_guard.py) | 两个 AE MCP 都连不上、只能用命令行脚本时 |

画面排版、动效节奏、出片检查按[视频通用设计与验收](../video-craft/README.md)；片型、比赛自己的要求在片型目录（如[创赛片](../../promo/competition/README.md)）。
