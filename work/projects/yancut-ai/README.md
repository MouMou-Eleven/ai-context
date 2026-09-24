# 言剪 AI（YanCut）

> 状态：账号制在线测试版；本轮更新为统一首页入口、云端工程＋本机原片
> 当前口径确认：2026-09-25；历史通过记录不等同于现行线上验收

个人在线入口：[言剪 AI](https://yancut-ai-personal.vercel.app) · [登录/注册](https://yancut-ai-personal.vercel.app/login) · [在线帮助](https://yancut-ai-personal.vercel.app/studio/help)。真实账号、Neon 数据库、管理员和积分继续使用；用户最新确认新增原片保留在本机，云端只保存轻量工程与素材描述，旧云素材和明确上传的识别音频/作品仍使用私有 Blob。最新方向和验收见 [统一入口与本机原片](./revisions/2026-09-25-unified-local-media-workspace.md)。[早先云端上线记录](./revisions/2026-09-25-online-cloud-launch.md) 保留历史，但“所有原片上传云端”不再作为当前口径。旧的免登录/个人 Key 模式也未恢复。

## 定位与边界

言剪 AI 是面向个体创作者和普通用户的中文优先、支持中英双语的 AI 视频剪辑网页应用。核心体验不是让用户学习复杂时间线，而是让用户用自然语言描述目标，由 AI 先生成可检查的操作计划，用户确认后再执行。

当前选择网页优先，不等待上游项目把所有能力做完，也不先做桌面封装。项目以 OpenCut v0.3.0 为剪辑底座，但名称、界面、中文工作流、AI 规划层、个人声音库和视频包装能力形成独立产品口径；不把简单汉化或换壳当作项目价值。

## 当前确认事实

- 目标用户：不会专业剪辑、希望快速完成口播、知识分享、产品介绍、生活记录等常见视频的个体用户。
- 产品形态：先做网页版；中文为主，提供中英双语切换。
- 上游基线：OpenCut v0.3.0，基线提交 `f4bd689f51cf12a4dd0a32f602f761be314d9686`，MIT License。
- 当前界面：首页为统一新建入口，导航以首页、工具箱、作品广场、我的为主；项目、素材、声音、任务、账户与积分集中在我的空间。旧创建页重定向并保留需求；时间线剪辑工作台、帮助和管理后台保留。页面存在不表示相应云服务已配置。
- AI 工作流：用户输入自然语言 → 生成结构化操作计划 → 缺少必要信息时请求补充 → 用户确认 → 映射到真实剪辑命令。
- 个人声音库：已建立声音登记、选择、克隆与合成的接口边界；用户必须拥有声音授权，不能克隆未获许可的声音。
- 视频包装：AI 把预设转为原生可编辑文字、标签和位置/缩放等关键帧，支持标题、信息卡、列表与数值排行榜；这条路径不是任意 Remotion/HTML/GSAP 代码渲染。独立渲染接口和本地队列另有实现，云端服务尚待部署验收。
- 默认规划模型配置为智谱 `glm-5.3-flash`，使用 `https://open.bigmodel.cn/api/paas/v4`；现已由独立适配器管理 provider 与图片/视频/JSON/推理能力，支持管理员配置其他 Chat Completions 兼容服务。未知模型默认文字能力，不发送不支持的 GLM 参数；协议兼容不保证模型质量相同。实际素材观察入口为有限静帧抽样，需用户授权，不等同于完整视频、连续动作和音频理解；真人转写准确率仍待实测。
- 当前线上版本：2026-09-25 固定域名 `https://yancut-ai-personal.vercel.app` 指向已READY的生产 `dpl_AruyzfJANm5xs1cXw9jNmCLqZ8BS`；最终验收 Preview 为 `dpl_3qW7MYMpXMT2PBTXwDEkGQWeQKwa`，功能源码提交 `3a6ee1be`，后续构建配置修正 `d9ec1f95` 不改变运行时。真实账号、Neon、管理员、积分继续使用，新原片留在本机；旧云素材和授权上传仍用 Blob。国内直连本轮失败，代理访问通过，不能保证裸连可用。最终承载平台仍为百度秒哒；旧云端原片版本及本轮首版生产Gaek保留历史。
- 本地开发目录：`F:\桌面文件\言剪AI`（2026-08-13 迁移并完成构建、启动验证）。
- 源码仓库为私有仓库 `https://github.com/MouMou-Eleven/yancut-ai`，`upstream` 跟踪 `https://github.com/OpenCut-app/OpenCut.git`。09-16 已将多轮实现提交，合并历史至 `b0b24335`，后续测试发现范围修正为 `22023132`；核对和修复了本地/远端历史分离及字体预览损坏。后续任务仍需实际查询最新 HEAD。`ai-context` 保存项目上下文，不保存完整源码。
- 持续同步约定：今后言剪每次更新默认同步本地权威源码、验收后的 Vercel 测试版本和本项目 README/修订记录，无需建委重复提醒。先验收新预览再切换固定域名，保留上一部署回退；Vercel 若因 Git 提交作者权限阻塞，使用不带 `.git` 元数据的干净源码包部署。
- 开发与部署分工：采用“本地权威源码 + 百度秒哒云端接管”。前端、业务逻辑、价格权益、数据库 Schema、接口合同、Mock 和自动化测试先在本地完成；验证通过后按编号压缩包交付百度秒哒，由秒哒接入 Auth、Postgres、对象存储、Edge Function、短信能力和部署。
- 秒哒兼容边界：当前本地基线是 Next.js 16.1.3，而已记录的秒哒稳定 Web 导入形态是 React + Vite。正式交付前必须重新核验平台能力；若仍不支持 Next.js，需提供 React + Vite 兼容构建，不能直接上传当前源码并宣称可部署。

## 当前进度

以下结合 09-10、09-15、09-16 修订及源码检查更新；历次证据见 [history.md](./history.md)。

| 能力 | 当前实现与验证边界 |
|---|---|
| 中文剪辑工作台 | 基于 OpenCut 真实素材、预览、时间线与导出；云端账号保存工程/素材描述，新原片留在本机，浏览器保存读句柄并负责预览、解码和 MP4 导出；缺失素材可重新关联，旧云素材兼容 |
| AI计划与统一工作台 | 首页附件、@ 引用、画幅/时长/风格进入持久化需求；场景工具每轮最多 4 个技能与 6 个配方，经过证据/时间/布局校验后转原生命令；云端计划先报价、确认扣积分，失败退款，不把测试夹具当实际模型效果 |
| 模板与执行稳定性 | 6 个场景入口：口播、字幕、混剪、动效、产品宣传、知识讲解；8 个内部技能合同。用户调试后可命名保存时间线模板、删除及换素材应用，当前浏览器最多 30 个。项目指纹、串行命令、严格保存与撤销/重做；不保证整轮原子回滚 |
| 专业剪辑 | 已接入停顿处理、字幕、倍速与音调保持、淡入淡出、转场、ducking、响度估计、代理、高光与速度曲线路径；复杂与长视频场景仍待系统验证 |
| 包装与关键帧 | 12 个原生动效配方可预览/编辑/引用 AI；新增白板图文逐项揭示，使用原生图形/文字/关键帧，可进入真实 MP4。中途手动补关键帧保持插值，播放头可越过片尾。尚无逐笔手绘、自动避脸或任意 AE 效果 |
| 参考与编排 | 参考视频独立授权抽取 6 帧，作为风格参考而非成片素材；157 镜头配方和 214 样式元数据用于内部检索。情绪/叙事转成具体动作及缺口判断，已有二维推近、拉远和平移；不宣称完整视频理解和任意参考复刻 |
| 声音与渲染服务 | 声音登记/克隆/合成接口边界和任务归属已实现；正式供应商、远端队列与生产成本仍待验收 |
| 购买与积分 | 在线版本支持管理员生成/停用充值码、用户兑换、AI/ASR 报价与失败退款；客服人工购买和正式价格仍按运营确认 |
| 管理后台 | `/admin` 已接入真实账号、Neon 数据库、加密运行配置、用户管理、审计和充值码；普通用户不能访问管理接口 |
| 最近验证证据 | 2026-09-25：Bun 451 项、4116 次断言通过；TypeScript、正式构建及GitHub三平台CI通过；真实9:16创建、本机素材重新关联、手动关键帧通过；真实GLM补验发现审批回环→修复→原需求重测成功，确认后创建10个可编辑元素并真实导出13秒1080p MP4 |
| 豆包 ASR 2.0 标准版 | 已接入服务端异步提交/查询、300 积分/小时报价与确认扣费、失败退分、云端任务归属和刷新恢复；真人长视频、上传速度和供应商等待时长仍待用户实测 |
| 当前录屏验收 | 账号制已有管理员；本轮验证工程/素材恢复与原生图文导出，另做真实模型文字规划补验。ASR未重跑，不能把白板或小型合成片当作真人语义剪辑质量通过 |

最新验收补充（2026-09-23）：本地干净工程已真实跑通口播停顿精剪、中文本地字幕、AI 标题/信息条包装和关键帧开关；工程重开恢复成功。浏览器实际下载成片，ffprobe 确认 14.001633 秒、H.264＋AAC、640×360。小型合成测试片不等于真人识别准确率或长片性能通过，详细证据和最终测试数见本日浏览器验收记录。

当前客服资料、模型参数、套餐试验价格及具体测试细节按相应日期的revision读取，不把开发登记值当成现行商业承诺。已撤销的独立包装中心和旧自动收银台只保留在历史记录中。

尚未完成（不影响本次个人在线测试）：

- 秒嗒生产接线、真实多运营商国内链路和正式备份/对账流程；Vercel 个人测试版的 Auth、Postgres、Blob、管理后台、积分和跨账号边界已经部署并完成黑盒基础验收。
- 声音克隆供应商的正式生产配置、授权留痕、录音质量检查和完整试听回写。
- AI 对真人口播、长视频和复杂多轨的系统验证；当前音频按完整源文件估算内存，超预算会拒绝，不是长视频流式分析。
- Remotion/HyperFrames 云端渲染服务的生产部署、对象存储回写、并发和成本测试；当前已完成 Remotion 本地队列、远端 provider 合同、HyperFrames 本地配方桥接、数据库任务记录和失败退款，仍需接入稳定的云任务服务。
- 专业剪辑能力仍待补齐：片段 slip/slide、响度标准化与真峰值计量、代理持久化与音画代理、速度曲线编辑器、复杂调色、运动跟踪、多机位和更稳定的语义高光模型。
- 模板仍需真实场景成片质量、音乐/音效编排和反复对话修订验收；批量并发、多机位、完整语义高光与数字人克隆尚未完成。
- 正式商业域名、隐私政策最终审阅和长视频/多轨质量验收。

## 文件索引

| 文件 | 作用 |
|---|---|
| [`revisions/2026-09-25-unified-local-media-workspace.md`](./revisions/2026-09-25-unified-local-media-workspace.md) | 最新方向：统一首页、本机原片/云端工程、工具候选编排、模型适配、白板、上游核验、真实浏览器导出与部署 |
| [`revisions/2026-09-16-workbench-motion-reference-templates.md`](./revisions/2026-09-16-workbench-motion-reference-templates.md) | 六项目核验、工作台修复、动效/参考/个人模板、线上导出与持续同步约定 |
| [`revisions/2026-09-15-personal-vercel-testing.md`](./revisions/2026-09-15-personal-vercel-testing.md) | 旧记录修正、个人 Key、Vercel 测试部署与后续迁移边界 |
| [`revisions/2026-09-15-hypit-montage-overlay-scenario-workflows.md`](./revisions/2026-09-15-hypit-montage-overlay-scenario-workflows.md) | 三个参考项目核验、场景技能、真实动效与文字修订 |
| [`revisions/2026-09-10-evidence-storyboard-workbench.md`](./revisions/2026-09-10-evidence-storyboard-workbench.md) | 统一工作台、抽帧证据、真实源区间分镜及导出验收 |
| [`revisions/2026-09-10-narrato-workflow-hardening.md`](./revisions/2026-09-10-narrato-workflow-hardening.md) | NarratoAI 参考、流程与失败保护修订 |
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
| [`revisions/2026-09-15-hypit-montage-overlay-scenario-workflows.md`](./revisions/2026-09-15-hypit-montage-overlay-scenario-workflows.md) | Hypit、montage-vlog-compiler、overlay-studio 核验；素材证据、场景规范与可编辑信息动效 |
| [`revisions/2026-09-23-doubao-asr-standard-billing.md`](./revisions/2026-09-23-doubao-asr-standard-billing.md) | 豆包录音文件识别 2.0 标准版异步提交/查询、积分确认、服务端密钥与对象存储边界 |
| [`revisions/2026-09-23-doubao-asr-preview-hardening.md`](./revisions/2026-09-23-doubao-asr-preview-hardening.md) | 个人 Vercel Preview 的 ASR 路由、任务恢复、实际时长报价、套餐积分口径与验证结果 |
| [`revisions/2026-09-23-doubao-asr-context-image-preview.md`](./revisions/2026-09-23-doubao-asr-context-image-preview.md) | 豆包标准版上下文/辅助图片入口、结构化上下文修复、最新 Preview 与验证边界 |
| [`revisions/2026-09-23-demo-release-hardening.md`](./revisions/2026-09-23-demo-release-hardening.md) | 口播精剪＋字幕＋画面包装录屏主线、个人 Preview 边界、ASR 会话安全和最终测试证据 |
| [`revisions/2026-09-23-demo-browser-evidence.md`](./revisions/2026-09-23-demo-browser-evidence.md) | 干净项目的真实浏览器验收、包装标签、关键帧开关、Vercel Preview 部署和导出验证边界 |
| [`revisions/2026-09-25-online-cloud-launch.md`](./revisions/2026-09-25-online-cloud-launch.md) | 账号制云端版本、Neon/Blob、管理后台、积分、线上黑盒验收、生产部署和回退边界 |
| 源码仓库 `docs/yancut/manual-test-checklist.md` | 网站完整功能清单、人工验收步骤、自动门禁与秒嗒上线前测试边界 |
| 源码仓库 `docs/yancut/doubao-asr-standard-integration.md` | 豆包录音文件识别 2.0 标准版的开通、异步任务、积分确认和对象存储使用说明 |

## AI 调用规则

处理言剪 AI 后续任务时：

1. 先读本 README，再根据问题读取架构或路线图；需要追溯方向变化时再读 `history.md`。
2. 不把当前原型能力描述成已上线或可大规模商用；明确区分“界面已完成”“接口已接通”“生产服务已部署”。
3. 涉及 OpenCut 更新时，先核验上游最新 release、changelog 和冲突文件，再决定兼容方式。
4. 涉及模型、API、价格、声音克隆供应商或 HyperFrames 能力时，必须重新核验当前官方资料，记录来源和核验日期。
5. 不在仓库中写入 API Key、Token、Cookie 或可直接利用的内部地址；只记录环境变量名和公共文档地址。
6. 产品叙事始终围绕大众化自然语言剪辑和个体可完成，避免重新扩成过窄行业工具或过重知识库项目。
7. 涉及百度秒哒交付时，同时读取 [`../../tools/miaoda/experience/patterns/codex-source-package-deployment.md`](../../domains/development/tools/miaoda/experience/patterns/codex-source-package-deployment.md)；先校验技术栈和附件限制，再生成分包。
8. 开发任务完成后默认更新本地源码、Vercel 测试版本和本项目 README/修订记录。部署先做新预览验收再切换固定域名，记录源码提交、部署标识、实测范围和回退目标；不要要求建委再次提醒同步。

## 待确认事项

- 参赛的最终赛道、报名材料口径和演示时长。
- 声音克隆正式供应商、收费策略和用户授权流程。
- 百度秒哒当期对 Next.js/React + Vite、手机号登录插件、短信服务、对象存储和长任务的实际支持情况。
- 正式支付渠道、套餐价格、模型与渲染成本、退款和发票策略。
- 上线版本是否继续保留 OpenCut 上游入口，以及具体的署名展示位置。

*索引与当前口径更新：2026-09-25；部署状态单独记录，不能从本地测试推断。*

## 后续写入

每次开发更新先按“本地实现、实测范围、生产部署、待验证”更新本页摘要，再将新增能力与测试证据写进对应revision并补索引。被替代的页面、购买方式或接口实现由revision保留取代关系，history只补摘要和链接，不在当前进度里并列为有效能力。源码状态需要实际核对源码仓库，不把本页旧commit称为最新HEAD。
