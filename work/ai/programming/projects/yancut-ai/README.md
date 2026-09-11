# 言剪 AI（YanCut）

> 状态：开发中（比赛原型阶段）
> 当前口径确认：2026-09-04

## 定位与边界

言剪 AI 是面向个体创作者和普通用户的中文优先、支持中英双语的 AI 视频剪辑网页应用。核心体验不是让用户学习复杂时间线，而是让用户用自然语言描述目标，由 AI 先生成可检查的操作计划，用户确认后再执行。

当前选择网页优先，不等待上游项目把所有能力做完，也不先做桌面封装。项目以 OpenCut v0.3.0 为剪辑底座，但名称、界面、中文工作流、AI 规划层、个人声音库和视频包装能力形成独立产品口径；不把简单汉化或换壳当作项目价值。

## 当前确认事实

- 目标用户：不会专业剪辑、希望快速完成口播、知识分享、产品介绍、生活记录等常见视频的个体用户。
- 产品形态：先做网页版；中文为主，提供中英双语切换。
- 上游基线：OpenCut v0.3.0，基线提交 `f4bd689f51cf12a4dd0a32f602f761be314d9686`，MIT License。
- 当前界面：首页、创作台、AI自动成片、素材库、模板中心、我的项目、个人声音库、任务中心、帮助中心、价格中心、剪辑工作台及管理后台。包装能力直接进入剪辑工作台AI计划和时间线。
- AI 工作流：用户输入自然语言 → 生成结构化操作计划 → 缺少必要信息时请求补充 → 用户确认 → 映射到真实剪辑命令。
- 个人声音库：已建立声音登记、选择、克隆与合成的接口边界；用户必须拥有声音授权，不能克隆未获许可的声音。
- 视频包装：Remotion 已作为首选可控包装引擎；AI 会把包装预设映射成当前项目中的可编辑文字轨、标签和关键帧，不再要求用户离开剪辑主链路进入独立页面。HyperFrames 已接入本地动效配方桥接，按可检查的 HTML/GSAP 节奏描述写入时间线；云端 HyperFrames 仍由独立队列配置提供。
- 主规划模型：2026-09-03 切换为智谱 `glm-5.3-flash`，使用官方 OpenAI 兼容接口
  `https://open.bigmodel.cn/api/paas/v4`，推理强度 `max`。模型规划器支持把真实图片、视频 URL
  和字幕/转写文本作为多模态上下文发送；本地实测返回 HTTP 200。API Key 只保存在本地忽略文件
  或部署平台密钥管理中，不写入仓库。
- 本地开发目录：`F:\桌面文件\言剪AI`（2026-08-13 迁移并完成构建、启动验证）。
- 代码现状：独立源码仓库为私有仓库 `https://github.com/MouMou-Eleven/yancut-ai`；截至2026-09-04记录的本地 `main` 提交 `c10df52`，远端源码已同步提交 `300ef650a01a0838f64c0e311671239eb8e7a17e`，`upstream` 继续跟踪 `https://github.com/OpenCut-app/OpenCut.git`。该阶段新增AI执行进度事件与时间线浮层、Remotion 本地能力预检、HyperFrames 动效配方桥接、手动关键帧按钮、结束帧可选中和深层中文化；`ai-context` 只保存项目上下文，不保存完整源码。
- 开发与部署分工：采用“本地权威源码 + 百度秒哒云端接管”。前端、业务逻辑、价格权益、数据库 Schema、接口合同、Mock 和自动化测试先在本地完成；验证通过后按编号压缩包交付百度秒哒，由秒哒接入 Auth、Postgres、对象存储、Edge Function、短信能力和部署。
- 秒哒兼容边界：当前本地基线是 Next.js 16.1.3，而已记录的秒哒稳定 Web 导入形态是 React + Vite。正式交付前必须重新核验平台能力；若仍不支持 Next.js，需提供 React + Vite 兼容构建，不能直接上传当前源码并宣称可部署。

## 当前进度

以下是截至2026-09-04记录的**本地原型能力**，2026-09-12仅整理摘要，没有重新运行源码、远端或生产服务。当前采用的购买方式与包装入口已合并说明；历次细项见 [history.md](./history.md)。

| 能力 | 当前实现与验证边界 |
|---|---|
| 中文剪辑工作台 | 基于OpenCut真实素材、预览、时间线与导出；本浏览器上传、持久化、模板和项目使用真实内容；主要界面支持中英双语 |
| AI计划与自动成片 | 自然语言→结构化计划→确认→真实命令；模型不可用明确标记本地兜底；分镜逐镜头确认真实素材后生成可编辑画面/字幕轨 |
| 模板与执行稳定性 | 已有真实素材槽位、连续时间线、串行命令、项目指纹、版本冲突保护与失败回滚；必填素材未完成不创建空壳 |
| 专业剪辑 | 已接入停顿处理、字幕、倍速与音调保持、淡入淡出、转场、ducking、响度估计、代理、高光与速度曲线路径；复杂与长视频场景仍待系统验证 |
| 包装与关键帧 | Remotion能力并入AI计划和可编辑时间线，支持本地异步队列；HyperFrames接入本地HTML/GSAP配方桥接；手动关键帧和执行步骤反馈已实现 |
| 声音与渲染服务 | 声音登记/克隆/合成接口边界、数据库任务、用户归属与失败退款已实现；正式供应商、远端队列与生产成本未验收 |
| 购买与积分 | 当前为联系客服、二维码/联系方式人工确认后开通积分；兼容旧收银台的接口不再创建订单或扣款。免费本地剪辑与付费AI能力的积分目录已在本地实现，正式价格与运营对账仍待确认 |
| 管理后台 | `/admin`、共享配置、管理员授权、审计与加密密钥本地闭环已完成；生产需要真实Auth、数据库和独立加密密钥 |
| 最近验证证据 | 09-02记录187个单元测试、TypeScript、生产构建与Playwright主流程通过；09-03/04记录本地演示、特效、配方桥接、执行反馈与关键帧验证。旧通过结果不代表当前部署已上线 |

当前客服资料、模型参数、套餐试验价格及具体测试细节按相应日期的revision读取，不把开发登记值当成现行商业承诺。已撤销的独立包装中心和旧自动收银台只保留在历史记录中。

尚未完成：

- 秒嗒生产接线、云端项目同步和跨账号隔离验收；管理后端、积分、订单、订阅与客服人工购买指引已完成本地实现，二维码和联系方式已经确认，仍需部署真实 Auth、Postgres、对象存储，并固化付款核验、积分开通和对账流程。
- 声音克隆供应商的正式生产配置、授权留痕、录音质量检查和完整试听回写。
- AI 自动剪辑对长视频、复杂多轨和失败回滚的系统验证。
- Remotion/HyperFrames 云端渲染服务的生产部署、对象存储回写、并发和成本测试；当前已完成 Remotion 本地队列、远端 provider 合同、HyperFrames 本地配方桥接、数据库任务记录和失败退款，仍需接入稳定的云任务服务。
- 专业剪辑能力仍待补齐：片段 slip/slide、响度标准化与真峰值计量、代理持久化与音画代理、速度曲线编辑器、复杂调色、运动跟踪、多机位和更稳定的语义高光模型。
- 模板创作包仍需补镜头替换预览、可选槽位、字幕样式与配乐规则；真实必填素材槽位和连续时间线实例化已完成。
- 部署域名和正式隐私政策。

## 文件索引

| 文件 | 作用 |
|---|---|
| [`architecture-and-upstream.md`](./architecture-and-upstream.md) | 技术结构、上游兼容策略和能力边界 |
| [`roadmap.md`](./roadmap.md) | 后续开发顺序、比赛演示闭环与上线前条件 |
| [`history.md`](./history.md) | 已清洗的项目关键演进与版本结论摘要 |
| [`revisions/2026-08-22-auto-video-editable-project-loop.md`](./revisions/2026-08-22-auto-video-editable-project-loop.md) | AI 自动成片真实闭环、验证证据和能力边界 |
| [`revisions/2026-08-22-wasm-scene-effect-and-editor-localization.md`](./revisions/2026-08-22-wasm-scene-effect-and-editor-localization.md) | WebAssembly 场景特效字段兼容、编辑器深层中文化与真实项目验证 |
| [`revisions/2026-08-31-recut-remotion-production-loop.md`](./revisions/2026-08-31-recut-remotion-production-loop.md) | Recut 经验吸收、可执行模板、Remotion 本地渲染与任务中心真实闭环 |
| [`revisions/2026-08-31-effects-remotion-commercial-loop.md`](./revisions/2026-08-31-effects-remotion-commercial-loop.md) | 音效容错、贴纸/特效扩容、Remotion 8 类动效、商业产品参考与桌面端回归 |
| [`revisions/2026-08-31-shotcut-professional-ai-workflow.md`](./revisions/2026-08-31-shotcut-professional-ai-workflow.md) | Shotcut/MLT 参考边界、AI 专业剪辑四阶段、Remotion 时间线融合、文字比例修复与实测证据 |
| [`revisions/2026-08-31-source-repo-professional-editing-queue.md`](./revisions/2026-08-31-source-repo-professional-editing-queue.md) | 自有源码仓库、专业剪辑命令、代理/高光/速度曲线和 Remotion 队列落地记录 |
| [`revisions/2026-09-01-concat-template-slots-command-queue.md`](./revisions/2026-09-01-concat-template-slots-command-queue.md) | Concat 成熟度与许可判断、真实模板槽位、AI 串行命令和 ducking 单位修复记录 |
| [`revisions/2026-09-02-commercialization-closure.md`](./revisions/2026-09-02-commercialization-closure.md) | 免费与付费边界、积分套餐、订单/订阅/声音/渲染数据模型、安全策略、验证证据和上线条件 |
| [`revisions/2026-09-02-admin-shared-backend.md`](./revisions/2026-09-02-admin-shared-backend.md) | 管理后台、共享配置、管理员权限、审计记录、动态运行配置和秒哒接线顺序 |
| [`revisions/2026-09-03-glm53-manual-purchase.md`](./revisions/2026-09-03-glm53-manual-purchase.md) | GLM-5.3-Flash 多模态规划、官方接口实测与客服扫码人工购买流程 |
| [`revisions/2026-09-03-local-demo-effects-stickers.md`](./revisions/2026-09-03-local-demo-effects-stickers.md) | 本地免登录演示、GPU 特效、AI 特效/贴纸命令、贴纸扩充与中文状态修复 |
| [`revisions/2026-09-04-ai-progress-remotion-hyperframes-keyframes.md`](./revisions/2026-09-04-ai-progress-remotion-hyperframes-keyframes.md) | AI 执行进度可视化、Remotion 本地预检、HyperFrames 动效配方桥接、手动关键帧、结束帧选择与深层中文化 |
| 源码仓库 `docs/yancut/manual-test-checklist.md` | 网站完整功能清单、人工验收步骤、自动门禁与秒嗒上线前测试边界 |

## AI 调用规则

处理言剪 AI 后续任务时：

1. 先读本 README，再根据问题读取架构或路线图；需要追溯方向变化时再读 `history.md`。
2. 不把当前原型能力描述成已上线或可大规模商用；明确区分“界面已完成”“接口已接通”“生产服务已部署”。
3. 涉及 OpenCut 更新时，先核验上游最新 release、changelog 和冲突文件，再决定兼容方式。
4. 涉及模型、API、价格、声音克隆供应商或 HyperFrames 能力时，必须重新核验当前官方资料，记录来源和核验日期。
5. 不在仓库中写入 API Key、Token、Cookie 或可直接利用的内部地址；只记录环境变量名和公共文档地址。
6. 产品叙事始终围绕大众化自然语言剪辑和个体可完成，避免重新扩成过窄行业工具或过重知识库项目。
7. 涉及百度秒哒交付时，同时读取 [`../../tools/miaoda/experience/patterns/codex-source-package-deployment.md`](../../tools/miaoda/experience/patterns/codex-source-package-deployment.md)；先校验技术栈和附件限制，再生成分包。

## 待确认事项

- 参赛的最终赛道、报名材料口径和演示时长。
- 声音克隆正式供应商、收费策略和用户授权流程。
- 百度秒哒当期对 Next.js/React + Vite、手机号登录插件、短信服务、对象存储和长任务的实际支持情况。
- 正式支付渠道、套餐价格、模型与渲染成本、退款和发票策略。
- 上线版本是否继续保留 OpenCut 上游入口，以及具体的署名展示位置。

*索引最后整理：2026-09-12；运行事实基线仍为2026-09-04*

## 后续写入

每次开发更新先按“本地实现、实测范围、生产部署、待验证”更新本页摘要，再将新增能力与测试证据写进对应revision并补索引。被替代的页面、购买方式或接口实现进入history，不在当前进度里并列为有效能力。源码状态需要实际核对源码仓库，不把本页旧commit称为最新HEAD。
