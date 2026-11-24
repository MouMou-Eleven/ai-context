# 视频共用方法

不管做宣传片、微课、故事片、MG 动画还是自媒体短视频都能用的视频方法和工具。整体制作流程（需求 → 素材 → 分工 → 小样 → 交付）见[设计共用流程](../../common/production-workflow.md)，这里不重复。

本目录分两层：**通用层**是所有视频都成立的设计判断和出片检查；**做法层**是 AI 出视频的四种做法，一种做法一个文件夹。片型、比赛自己的要求在片型目录（如[创赛片](../promo/competition/README.md)）。一条经验先按[写入规范 · 视频经验写到哪一层](../../../../../system/repository/ingestion-workflow.md#视频经验写到哪一层默认)定层，落到本目录的，再按下面的“写入与触发”定文件夹和文件。

## 通用层：不管怎么做都要读

| 内容 | 入口 | 什么时候用 |
|---|---|---|
| 视频通用设计与验收：字号、间距、对齐、版面舒展；出场节奏、转场与闪、停留、跟着配音走；出片检查和通用验收表 | [video-craft/](video-craft/README.md) | AI 自己动手出任何视频（生成、代码、Blender、AE、剪辑），开工前读 |

画面本身的排版和审美（层级、留白、对齐、配色）用[设计原则与审美](../../common/design-principles/README.md)，视频画面也是版面。

## 做法层：AI 出视频的四种做法

每种做法一个文件夹，先读它的入口，再按入口里的表读具体文件。

| 做法 | 文件夹 | 里面有什么 | 什么时候用 |
|---|---|---|---|
| AI 生成：扩散模型文生视频、图生视频、参考视频、图加音频 | [ai-generation/](./ai-generation/README.md) | [seedance/](./ai-generation/seedance/README.md)：建委实战、提示词模板与案例、第三方模板库 | 要写实、要人物、要氛围；写视频提示词、让参考图动起来 |
| 代码生成：AI 写代码直接画出画面 | [code-generation/](./code-generation/README.md) | [3d-scene/](./code-generation/3d-scene/README.md) three.js 三维场景与运镜；[footage-overlay/](./code-generation/footage-overlay/README.md) 成片上逐帧叠加包装；通用流程与渲染管线 | 结构、文字、运镜要精确可控，发光、粒子、信息面板这类科技感画面 |
| AI 操作 Blender：AI 写 Python 驱动三维软件建模、动画、渲染 | [blender/](./blender/README.md) | 建模解说视频（照片定模型、交接工程、配音对齐）；白模预演控 AI 视频（先定镜头走位再交给视频模型） | 要真实建模、能推近看、能拆开讲；或 AI 生成的镜头和走位必须可控 |
| AI 接入 AE：AI 通过 MCP 操作 After Effects | [ae/](./ae/README.md) | 改 AE 模板的设计判断、AI 与 AE 协作（两个 AE MCP）、弹窗守护脚本 | 借现成模板的高完成度效果，任何片型 |

可编辑参数化动画（文字、颜色、数据要能改）可以用 [Remotion Skill](../../../other/skills/jianwei-ai-community-remotion-video/README.md)，它属于代码生成。

“AE 风格”的生成视频提示词不证明存在可编辑 AE 工程；这单要求交 AE 工程时，必须实际交付并验收工程。

## 写入与触发（默认）

本目录每个文件夹管什么、什么任务会读到它、什么经验写进来，统一按这张表；各文件夹 README 不另写一套。任务说法会自动读到哪里由[路由表](../../../../../system/repository/navigation/routes.json)执行，表中最后一列是路由编号和例句，例句由回归测试逐句跑，改了这张表要同步改路由和测试。

| 文件夹 | 触发：什么任务读、从哪进 | 写进来：什么经验、写到哪个文件 | 不写进来（去哪） | 路由 · 例句 |
|---|---|---|---|---|
| [video-craft/](video-craft/README.md) | AI 自己动手出任何视频：剪辑、包装、加字幕标题标注、做动画、出成片，不管哪种做法，开工前读入口 | 换成任何做法、任何片型都成立的：尺寸间距进 [layout-and-sizing](video-craft/layout-and-sizing.md)；节奏、转场、停留、跟配音进 [motion-and-verification](video-craft/motion-and-verification.md)；怎么查、验收表进 [verification](video-craft/verification.md) | 放到一页 PPT 上也成立的（进设计原则）；只在某种做法成立的（进那种做法的文件夹） | hands-on-video · “把这段录屏加上字幕和标题”“这个创赛视频帮我做一下片头和转场” |
| [ai-generation/](./ai-generation/README.md) | 要 AI 生成镜头、写视频提示词、让参考图动起来；从入口进，再进对应模型的文件夹 | 跟模型有关的：按模型一个文件夹（目前 [seedance/](./ai-generation/seedance/README.md)，里面实战流程进 practical-workflow、可复用提示词进 prompt-templates、跑过的案例进 prompt-cases）；换哪个模型都成立的输入方式写法，写进入口 | 生图、生视频都成立的（进[设计中用 AI 生成的原则](../../common/ai-generation-principles.md)）；第三方模板库原文不改（awesome-seedance/source） | video-prompt、ai-generation-video · “帮我写一段 Seedance 视频提示词”“把这张参考图动起来”“用AI生成一段工厂视频镜头” |
| [code-generation/](./code-generation/README.md) | AI 写代码出画面：three.js、HTML、Python 逐帧合成、Remotion；从入口进，再进对应门类 | 按效果类型分门类，一个门类一个文件夹（3d-scene、footage-overlay），门类里按片型写用法；跨门类的定调、镜头脚本、确定性、渲染管线、迭代进 [workflow](./code-generation/workflow.md) | 用 Blender 的（进 blender/）；画面排版和验收（进 video-craft） | code-video、code-generation-video · “用 three.js 做一段工厂三维运镜动画”“用Remotion做一段数据动画”“用HyperFrames做个片头” |
| [blender/](./blender/README.md) | 任务里出现 Blender、白模、动态分镜、三维解说；从入口进，再按用法读 | 两种用法共用的开工方式、环境检查写进入口；建模解说片的流程、建模、交接、配音对齐进 [modeled-explainer](./blender/modeled-explainer.md)；白模预演、交给视频模型进 [previs-for-ai-video](./blender/previs-for-ai-video.md)；出现第三种用法时另建一个文件，登记在入口表 | 视频模型提示词本身怎么写（进 ai-generation）；成片验收（进 video-craft） | blender-video · “先搭白模再用 AI 生成视频”“用Blender做一段桥梁建模解说动画” |
| [ae/](./ae/README.md) | AI 要在 After Effects 里读工程、改模板、做动画包装、渲染；不管用户提没提 MCP | 怎么连、两个 MCP 怎么挑、操作和渲染的坑进 [ai-ae-collaboration](./ae/ai-ae-collaboration.md)；拿模板做画面时的设计判断和改模板验收进 [ae-template-design](./ae/ae-template-design.md)；脚本放 tools/ | 某个片型、比赛的模板要求（进片型目录，如创赛 ae-template-layout）；某一单的工程路径、模板名（进项目记录） | ae · “用 AE 模板改一段片头并渲染”“在AE里做个标题动画” |

- **新做法**（比如以后用 C4D、UE、剪映模板）、**做法里的新门类或新模型文件夹**：都先问建委，同意后再建。新做法同时在上表加一行、在路由表加触发、在本表例句列加例句（回归测试会逐句跑），三处一起改；新门类、新模型登记在那种做法的入口表。
- **新文件**：先找上表那一格里已有的文件补充；同一格的文件写到读不下了，按使用时刻拆，并登记在该文件夹的入口表。
- **一条经验同时属于两种做法**（如白模既是 Blender 又服务 AI 生成）：写在“先动手的那一步”所在的文件夹，另一边入口只放一句话加链接。

## 四种做法怎么选（默认）

| | 代码生成 | AI 操作 Blender | AI 生成（Seedance） | AE 模板 |
|---|---|---|---|---|
| 可控性 | 最高：每个元素、每段运镜、每一帧都能指定 | 高：模型、相机、关键帧都在工程里，可推近、可拆开 | 低：靠提示词引导，结果要抽卡 | 中：模板结构固定，可换字换素材、改排版 |
| 改一处的成本 | 改代码后重渲，其他地方前后完全一致 | 改工程后重渲，要算渲染时间 | 重新生成，整段都可能变 | 改图层后重渲；用 MCP 改正在打开的工程，改一处看一帧只要几秒 |
| 擅长 | 结构示意、精确运镜、清晰文字和标注、发光粒子数据感 | 要“像真东西”的结构：桥、设备、产品构造的建模和拆解；白模定镜头 | 写实质感、人物、自然场景、氛围 | 证书墙、粒子、插件光效、三维相机这类现成模板能直接用的效果 |
| 短板 | 写实质感、有机形体、真人 | 真人表情；渲染耗时；目前只有探索作品 | 结构准确、精确文字、指定运镜 | 没有现成模板的内容；第三方插件本机没装就缺效果 |

- **画面上要有清楚的文字、数字、标注时，用代码。** 例：飞机总装实拍上的坐标包装，先用 AI 视频模型生成过一版，文字是糊的，改用代码逐帧绘制才清楚。
- **结构必须讲对、运镜必须指定时，用代码。** 例：“智慧工厂整体解决方案”要讲清产线、仓储、数据中枢的关系，Seedance 生成的工厂结构不可控，改用代码搭三维场景。
- **要真实建模、能推近看、能拆开讲时，用 [Blender](./blender/README.md)。**
- **用 AI 生成、但镜头和走位必须可控时，先用 Blender 搭白模定镜头，再交给视频模型**（[白模预演控 AI 视频](./blender/previs-for-ai-video.md)）。3—5 秒、没有复杂动作的氛围镜头，直接生成可能更划算。
- **要写实、要人物、要情绪时，用 Seedance 或实拍。**
- **用户已经挑好 AE 模板、或要模板级的插件效果时，用 AE。** 平面文字包装用代码往往比改模板快（创赛片的实测对比见[两种分工模式](../promo/competition/ai-code-ae-pipeline.md#两种分工模式默认)）。
- 一条片子可以混用：写实镜头用 Seedance 或实拍，结构和原理镜头用代码或 Blender，模板镜头用 AE，最后统一按配音合成。不管哪种做出来的镜头，都按[出片检查](video-craft/verification.md)验收。

为什么这样分：建委看重可控，代码生成的每个地方都能说清楚、改得动，适合“这一句必须讲清楚”的镜头；Blender 适合要真实三维模型、或要先定死镜头的；AI 生成适合“这一镜要好看、要真”的镜头；AE 模板适合借现成的高完成度效果。

MG 是一种动态图形表达方式，企业、产品、教育都能用。先定信息结构、图形层级、转场和阅读停留时间，再按交付要求选 AE、代码或 Remotion。目前还没有独立验收过的通用 MG 案例。

中文脚本、旁白和字幕，先读[口语样稿](../../../../../system/expression/voice-samples.md)（需要口语时）和[表达短卡](../../../../../system/expression/README.md)。

<!-- generated-methods:start -->
## 按实际需要选择方法

由routes.json生成。先判断本次成品和读者，再按下表实际需要读取方法正文；无需点名作者。多种方法可分工，但同一段不拼接相互冲突的结构。没有适用需求时跳过，不能因看到本表就全部加载。

| 需要解决什么 | 方法正文 | 不适用／保留边界 | 成品怎样检查 |
|---|---|---|---|
| AI要在After Effects里读工程、改模板、做动画或包装、渲染出片时，不管片型（MG、自媒体、特效包装、企业片、创赛片） | [AI与AE协作（两个AE MCP）](ae/ai-ae-collaboration.md) | 只写AE风格的视频提示词，或只用Remotion、Python代码做动画不碰AE时；片型自己的版面和设计规则仍读片型目录 | 交付前检查表填实测值：用了哪个MCP的哪些工具、命令行脚本几次及原因、两个MCP版本、ae_proof结果；成片按出片检查的通用验收表查黑帧频闪接缝 |
| 用现成AE模板做画面时，不管片型（MG、自媒体、企业片、创赛片）：先设计版面再用模板实现、模板文字组件要用上、只用对应一段、模板自带光效倒影年份卡逐个对位、新加层做进模板 | [改AE模板的设计判断](ae/ae-template-design.md) | 从零在AE里做动画不用模板，或只用代码出片时；片型专属要求（如创赛字幕区、主色）读片型目录 | 改模板验收表逐行填实测值：关掉的模板层清单及理由、模板主体位置、排版区距离、灯光强度与色差、光效位置、新加层开关、延长段尾帧 |
| 实际需要AI生成视频素材、参考图动态化或镜头提示词时；可明确调用，也可按制作环节主动识别，再按镜头意图读具体模板 | [Awesome Seedance 视频提示词方法](ai-generation/seedance/awesome-seedance/README.md) | 纯AE／Remotion动效、仅口播文案、模型介绍或查询不自动套用；不覆盖片型设计、已验证经验或用户保护范围 | 实际读对应模板和一个锚点；核对主体／动作／镜头／声音、当前模型限制和复测状态；有生成产物才做成片验收，失败回写原项目 |
<!-- generated-methods:end -->
