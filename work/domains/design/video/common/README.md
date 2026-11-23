# 视频共用方法

不管做宣传片、微课还是故事片都能用的视频制作方法和工具。整体制作流程（需求 → 素材 → 分工 → 小样 → 交付）见[设计共用流程](../../common/production-workflow.md)，这里不重复。

| 内容 | 入口 | 什么时候用 |
|---|---|---|
| AI 视频提示词（Seedance / 即梦） | [seedance/](./seedance/README.md) | 要 AI 生成镜头、写视频提示词、让参考图动起来 |
| AE 制作与工程交付 | [ae-production.md](./ae-production.md) | 信息包装、合成、字幕、源工程、最终导出 |
| AI 与 AE 协作：本机两个 AE MCP 怎么挑、先用自带工具不自己写脚本、保持最新、操作和渲染的坑、经验写到哪里 | [ai-ae-collaboration.md](./ai-ae-collaboration.md) | AI 要在 AE 里读工程、改模板、做动画、渲染，任何片型（MG、自媒体、特效包装、企业片、创赛片） |
| AE 弹窗守护（命令行后备用） | [tools/ae_dialog_guard.py](./tools/ae_dialog_guard.py) | 两个 AE MCP 都连不上、只能用命令行脚本时 |
| 代码生成动画：按效果类型分门类（三维场景与运镜、成片上叠加包装，MG、手绘待补） | [code-rendered-animation/](./code-rendered-animation/README.md) | 结构、文字、运镜要精确可控的画面和效果；写实人物和质感走 Seedance |
| AI 动手剪辑、包装、加效果、出成片（实际都是代码完成） | [代码式视频设计经验](../../common/code-driven-video/README.md) | 字号、间距、对齐、容器、出场节奏和验收；用 Remotion、HTML、Python 都先读 |
| 可编辑参数化动画（Remotion） | [Remotion Skill](../../../other/skills/jianwei-ai-community-remotion-video/README.md) | 文字、颜色、数据要能改的动画 |

MG 是一种动态图形表达方式，企业、产品、教育都能用。先定信息结构、图形层级、转场和阅读停留时间，再按交付要求选 AE 或 Remotion。目前还没有独立验收过的通用 MG 案例。

中文脚本、旁白和字幕，先读[口语样稿](../../../../../system/expression/voice-samples.md)（需要口语时）和[表达短卡](../../../../../system/expression/README.md)。

<!-- generated-methods:start -->
## 按实际需要选择方法

由routes.json生成。先判断本次成品和读者，再按下表实际需要读取方法正文；无需点名作者。多种方法可分工，但同一段不拼接相互冲突的结构。没有适用需求时跳过，不能因看到本表就全部加载。

| 需要解决什么 | 方法正文 | 不适用／保留边界 | 成品怎样检查 |
|---|---|---|---|
| AI要在After Effects里读工程、改模板、做动画或包装、渲染出片时，不管片型（MG、自媒体、特效包装、企业片、创赛片） | [AI与AE协作（两个AE MCP）](ai-ae-collaboration.md) | 只写AE风格的视频提示词，或只用Remotion、Python代码做动画不碰AE时；片型自己的版面和设计规则仍读片型目录 | 交付前检查表填实测值：用了哪个MCP的哪些工具、命令行脚本几次及原因、两个MCP版本、ae_proof结果、黑帧频闪接缝 |
| 实际需要AI生成视频素材、参考图动态化或镜头提示词时；可明确调用，也可按制作环节主动识别，再按镜头意图读具体模板 | [Awesome Seedance 视频提示词方法](seedance/awesome-seedance/README.md) | 纯AE／Remotion动效、仅口播文案、模型介绍或查询不自动套用；不覆盖片型设计、已验证经验或用户保护范围 | 实际读对应模板和一个锚点；核对主体／动作／镜头／声音、当前模型限制和复测状态；有生成产物才做成片验收，失败回写原项目 |
<!-- generated-methods:end -->
