# 言剪 AI（YanCut）

> 状态：开发中，转入个人在线实测与持续迭代阶段
> 当前口径确认：2026-09-17；历史通过记录不等同于现行线上验收

个人测试入口：[在线工作台](https://yancut-ai-personal.vercel.app/studio/workbench) · [填写本人 GLM Key](https://yancut-ai-personal.vercel.app/ai-settings)。无需启动本地服务；项目仍存当前浏览器。使用前请读 [本地优先使用手册](./revisions/2026-09-17-local-first-manual-spectrum-ui.md)；最新动效、关键帧、参考视频和模板升级见 [09-16 发布记录](./revisions/2026-09-16-workbench-motion-reference-templates.md)，个人测试环境约定见 [部署说明](./revisions/2026-09-15-personal-vercel-testing.md)。

## 定位与边界

言剪 AI 是面向个体创作者和普通用户的中文优先、支持中英双语的 AI 视频剪辑网页应用。核心体验不是让用户学习复杂时间线，而是让用户用自然语言描述目标，由 AI 先生成可检查的操作计划，用户确认后再执行。

当前选择网页优先，不等待上游项目把所有能力做完，也不先做桌面封装。项目以 OpenCut v0.3.0 为剪辑底座，但名称、界面、中文工作流、AI 规划层、个人声音库和视频包装能力形成独立产品口径；不把简单汉化或换壳当作项目价值。

## 当前确认事实

- 目标用户：不会专业剪辑、希望快速完成口播、知识分享、产品介绍、生活记录等常见视频的个体用户。
- 产品形态：先做网页版；中文为主，提供中英双语切换。
- 上游基线：OpenCut v0.3.0，基线提交 `f4bd689f51cf12a4dd0a32f602f761be314d9686`，MIT License。
- 当前界面：首页、统一工作台、素材库、模板中心、我的项目、个人声音库、任务中心、帮助中心、价格中心、剪辑工作台及管理后台。独立 AI 自动成片已合并，旧地址重定向到工作台；页面存在不表示相应云服务已配置。
- AI 工作流：用户输入自然语言 → 生成结构化操作计划 → 缺少必要信息时请求补充 → 用户确认 → 映射到真实剪辑命令。
- 个人声音库：已建立声音登记、选择、克隆与合成的接口边界；用户必须拥有声音授权，不能克隆未获许可的声音。
- 视频包装：AI 把预设转为原生可编辑文字、标签和位置/缩放等关键帧，支持标题、信息卡、列表与数值排行榜；这条路径不是任意 Remotion/HTML/GSAP 代码渲染。独立渲染接口和本地队列另有实现，云端服务尚待部署验收。
- 主规划模型：智谱 `glm-5.3-flash`，使用 `https://open.bigmodel.cn/api/paas/v4`。实际素材观察入口最多取样 4 个素材、12 张静帧，需用户授权；不等同于完整视频、连续动作和音频理解。已有文字可进入上下文，真人转写准确率仍待实测。
- 个人在线测试：用户于 2026-09-15 选择 Vercel，用于本人访问和反复迭代；最终承载平台仍为百度秒哒。新增“AI 设置”手动填写本人 GLM Key，当前标签页会话保存、服务端转发，不写入项目或共享后台。此模式不依赖登录积分，不启用演示管理员；上线结果以本轮部署修订记录为准。
- 本地开发目录：`F:\桌面文件\言剪AI`（2026-08-13 迁移并完成构建、启动验证）。
- 源码仓库为私有仓库 `https://github.com/MouMou-Eleven/yancut-ai`，`upstream` 跟踪 `https://github.com/OpenCut-app/OpenCut.git`。09-16 已将多轮实现提交，合并历史至 `b0b24335`，后续测试发现范围修正为 `22023132`；核对和修复了本地/远端历史分离及字体预览损坏。后续任务仍需实际查询最新 HEAD。`ai-context` 保存项目上下文，不保存完整源码。
- 持续同步约定：今后言剪每次更新默认同步本地权威源码、验收后的 Vercel 个人测试版本和本项目 README/修订记录，无需建委重复提醒。先验收新预览再切换固定域名，保留上一部署回退。
- 开发与部署分工：采用“本地权威源码 + 百度秒哒云端接管”。前端、业务逻辑、价格权益、数据库 Schema、接口合同、Mock 和自动化测试先在本地完成；验证通过后按编号压缩包交付百度秒哒，由秒哒接入 Auth、Postgres、对象存储、Edge Function、短信能力和部署。
- 秒哒兼容边界：当前本地基线是 Next.js 16.1.3，而已记录的秒哒稳定 Web 导入形态是 React + Vite。正式交付前必须重新核验平台能力；若仍不支持 Next.js，需提供 React + Vite 兼容构建，不能直接上传当前源码并宣称可部署。

## 当前进度

以下结合 09-10、09-15、09-16 修订及源码检查更新；历次证据见 [history.md](./history.md)。

| 能力 | 当前实现与验证边界 |
|---|---|
| 中文剪辑工作台 | 基于OpenCut真实素材、预览、时间线与导出；本浏览器上传、持久化、模板和项目使用真实内容；主要界面支持中英双语 |
| AI计划与统一工作台 | 项目需求、素材、画面证据、可调整分镜进入同一时间线；多轮上下文有限保留。个人 Key 模式失败明确报错，不把本地规则当作模型结果 |
| 模板与执行稳定性 | 6 个场景入口：口播、字幕、混剪、动效、产品宣传、知识讲解；8 个内部技能合同。用户调试后可命名保存时间线模板、删除及换素材应用，当前浏览器最多 30 个。项目指纹、串行命令、严格保存与撤销/重做；不保证整轮原子回滚 |
| 专业剪辑 | 已接入停顿处理、字幕、倍速与音调保持、淡入淡出、转场、ducking、响度估计、代理、高光与速度曲线路径；复杂与长视频场景仍待系统验证 |
| 包装与关键帧 | 12 个原生动效配方可预览、编辑、拖拽与引用 AI；修复画布移动/缩放关键帧及未选中片段边界，播放头可越过片尾。关联包装可随锚点移动、分割及删除；质检检查结构与文字重叠，尚无自动避脸和任意 AE 效果 |
| 参考与编排 | 参考视频独立授权抽取 6 帧，作为风格参考而非成片素材；157 镜头配方和 214 样式元数据用于内部检索。情绪/叙事转成具体动作及缺口判断，已有二维推近、拉远和平移；不宣称完整视频理解和任意参考复刻 |
| 声音与渲染服务 | 声音登记/克隆/合成接口边界、数据库任务、用户归属与失败退款已实现；正式供应商、远端队列与生产成本未验收 |
| 购买与积分 | 当前为联系客服、二维码/联系方式人工确认后开通积分；兼容旧收银台的接口不再创建订单或扣款。免费本地剪辑与付费AI能力的积分目录已在本地实现，正式价格与运营对账仍待确认 |
| 管理后台 | `/admin`、共享配置、管理员授权、审计与加密密钥本地闭环已完成；生产需要真实Auth、数据库和独立加密密钥 |
| 最近验证证据 | 09-16：143 项针对性测试后扩展至 307 项全量单元测试、3166 次断言；TypeScript、本地/Vercel 构建通过。本地关键帧 5 秒 H.264 导出与画面对照、线上素材+动效 12 秒 H.264 导出。真实 GLM 六帧参考分析在本地通过，公网未填 Key 明确拒绝；本人有效 Key 的公网成片质量仍待实测 |
| 豆包 ASR 2.0 标准版 | 已接入服务端异步提交/查询、300 积分/小时报价与确认扣费、失败退分和密钥配置；正式使用仍需对象存储 HTTPS 地址与真实长任务验收 |
| 最近验证证据 | 09-16：143 项针对性测试后扩展至 307 项全量单元测试、3166 次断言；TypeScript、本地/Vercel 构建通过。本地关键帧 5 秒 H.264 导出与线上素材+动效 12 秒 H.264 导出已验证。豆包标准版适配器、字幕时间戳转换和前端报价确认流程新增 9 项测试；真实供应商长任务仍待对象存储与账号验收 |

当前客服资料、模型参数、套餐试验价格及具体测试细节按相应日期的revision读取，不把开发登记值当成现行商业承诺。已撤销的独立包装中心和旧自动收银台只保留在历史记录中。

尚未完成：

- 秒嗒生产接线、云端项目同步和跨账号隔离验收；管理后端、积分、订单、订阅与客服人工购买指引已完成本地实现，二维码和联系方式已经确认，仍需部署真实 Auth、Postgres、对象存储，并固化付款核验、积分开通和对账流程。
- 声音克隆供应商的正式生产配置、授权留痕、录音质量检查和完整试听回写。
- AI 对真人口播、长视频和复杂多轨的系统验证；当前音频按完整源文件估算内存，超预算会拒绝，不是长视频流式分析。
- Remotion/HyperFrames 云端渲染服务的生产部署、对象存储回写、并发和成本测试；当前已完成 Remotion 本地队列、远端 provider 合同、HyperFrames 本地配方桥接、数据库任务记录和失败退款，仍需接入稳定的云任务服务。
- 专业剪辑能力仍待补齐：片段 slip/slide、响度标准化与真峰值计量、代理持久化与音画代理、速度曲线编辑器、复杂调色、运动跟踪、多机位和更稳定的语义高光模型。
- 模板仍需真实场景成片质量、音乐/音效编排和反复对话修订验收；批量并发、多机位、完整语义高光与数字人克隆尚未完成。
- 部署域名和正式隐私政策。

## 文件索引

| 文件 | 作用 |
|---|---|
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

*索引与当前口径更新：2026-09-16；部署状态单独记录，不能从本地测试推断。*

## 后续写入

每次开发更新先按“本地实现、实测范围、生产部署、待验证”更新本页摘要，再将新增能力与测试证据写进对应revision并补索引。被替代的页面、购买方式或接口实现由revision保留取代关系，history只补摘要和链接，不在当前进度里并列为有效能力。源码状态需要实际核对源码仓库，不把本页旧commit称为最新HEAD。
