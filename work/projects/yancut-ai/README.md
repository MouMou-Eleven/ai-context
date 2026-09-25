# 言剪 AI（YanCut）

> 状态：用户已上传并执行 R6；短信热修后真实验证码可收到，但注册提交因 R6 Edge 占位哈希为 32+140、SQL 只接受 32+128 而返回 `INVALID_REGISTRATION`。R6.1 收口补丁已本地冻结并通过跨层回归，等待用户上传；在真实注册、首管、密码重登和找回密码全部通过前，R6 仍未完成、不能进入 R7。管理员保存、正式域名和 36 个未迁 API 仍未验收。
> 当前口径确认：2026-09-26；历史通过记录不等同于现行线上验收

个人在线入口：[言剪 AI](https://yancut-ai-personal.vercel.app) · [登录/注册](https://yancut-ai-personal.vercel.app/login) · [在线帮助](https://yancut-ai-personal.vercel.app/studio/help)。真实账号、Neon 数据库、管理员和积分继续使用；原片保留本机，云端保存轻量工程与素材描述，旧云素材和明确上传的识别音频/作品仍使用私有 Blob。最新见[工作台更新](./revisions/2026-09-25-editor-voice-integration.md)及[声音定价更正](./revisions/2026-09-25-voice-pricing-v11.md)，存储方向见[统一入口与本机原片](./revisions/2026-09-25-unified-local-media-workspace.md)。[早先云端上线记录](./revisions/2026-09-25-online-cloud-launch.md) 保留历史，但“所有原片上传云端”不再作为当前口径。旧的免登录/个人 Key 模式也未恢复。

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
- 视频包装：用户只需导入、对话、确认、导出同一条完整 MP4，不另设 Remotion 工作台。AI 将部分预设转成原生文字、标签和关键帧，已验证随原片导出；这不是任意 Remotion/HTML/GSAP 代码渲染。新增 Remotion HTTP Worker 已本机出片，公网服务、AI 自动调用和回填时间线仍待接线与整链验收。
- 默认规划模型配置为智谱 `glm-5.3-flash`，使用 `https://open.bigmodel.cn/api/paas/v4`；统一规划器现支持 Chat Completions、Responses、Anthropic Messages、Gemini generateContent。自动按端点及域名识别，未知中转默认 Chat，特殊中转需手选；新增协议经契约测试，不代表所有厂商已联网实测。独立能力适配器控制图片/视频/JSON/推理参数，协议兼容不保证模型质量一致。素材观察仍为经授权的有限静帧抽样，不等于完整视频或音频理解。
- 当前线上版本：2026-09-25 固定域名指向 READY 生产 `dpl_Gbuh1NLbpg7t3zkcDmS3Ks37txoF`；验收 Preview 为 `dpl_FmjyMVSLiHE4yK8YxtBm12LW9E18`，运行代码 `bdd71f13`。前版 `dpl_H4pCaqFCNEuh9RsLtLM8a1ivRBCK` 保留回退，但其旧声音价格预估前提已作废。真实账号、Neon、管理员、积分继续使用；兼容迁移 0009 已执行，回退不删除任务表或账本。国内直连此前失败，本轮使用代理验收，不能保证裸连可用。最终承载平台仍为百度秒哒。
- 本地开发目录：`F:\桌面文件\言剪AI`（2026-08-13 迁移并完成构建、启动验证）。
- 源码仓库为私有仓库 `https://github.com/MouMou-Eleven/yancut-ai`，`upstream` 跟踪 `https://github.com/OpenCut-app/OpenCut.git`。09-16 已将多轮实现提交，合并历史至 `b0b24335`，后续测试发现范围修正为 `22023132`；核对和修复了本地/远端历史分离及字体预览损坏。后续任务仍需实际查询最新 HEAD。`ai-context` 保存项目上下文，不保存完整源码。
- 持续同步约定（本轮更新）：后续以百度秒哒承载和迭代为目标，维护本地权威源码、GitHub及本项目README/修订记录；不再自动继续Vercel发布。旧Vercel作为历史测试／回退入口，秒哒云端适配改动也须同步回源码，避免分叉。
- 开发与部署分工：采用“本地权威源码 + 百度秒哒云端接管”。前端、业务逻辑、价格权益、数据库 Schema、接口合同、Mock 和自动化测试先在本地完成；验证通过后按编号压缩包交付百度秒哒，由秒哒接入 Auth、Postgres、对象存储、Edge Function、短信能力和部署。
- 秒哒兼容边界：应用`app-enipq7iozwn5`为Vite SPA + Supabase Deno Edge，与原Next16.1.3／47API／25表不能原样兼容。825/835失败后按用户要求串行chat，最终1016完成静态预览；外部浏览器确认原首页和邮箱密码登录页可见，但后端未接、登录禁用、未publish。旧DB/Blob/用户未迁，云端pnpm冒烟不是原锁构建，见[迁移修订](./revisions/2026-09-25-miaoda-source-migration.md)。

## 当前进度

最新补充：R6 已上传并由秒哒应用，后续云端热修复补齐构建时 Supabase 公共环境变量，用户实际收到短信；这证明验证码请求链已经跨过前端配置层，但不证明注册完成。注册提交返回“注册信息无效”，本地按云端文件哈希复查到 R6 `PLACEHOLDER_HASH` 摘要长度为 140，违反数据库 `32:128` 合同；原 Deno 测试把 RPC 模拟为恒成功，隔离 SQL 又使用了单独的正确测试值，两层测试没有连接起来。R6 状态改为“已应用、待 R6.1 修复”，R7 暂不开始。临时 `vitesandbox`、HTTP 200、云端 Chromium 自报和构建成功均不作为真实可用验收；完整原因与门禁见[本次修订](./revisions/2026-09-25-miaoda-source-migration.md#r6-云端执行与真实注册失败2026-09-26)。

R6.1 已生成不可覆盖交付包 `yancut-JW-20260926-R6.1-increment.zip`，18272 字节，SHA-256 `20e89bd5794a0266c89e926047fc818c8eb5a8c13a739dc2ca5c5ba5db180063`。它只替换两个 Edge 运行副本及两个测试副本，并以追加版回执 hash 保护构建脚本、前端认证桥、云端登录页和 database.ts；不执行新迁移、不自动发短信、不启动 R7。Deno 7 项与解压实物复测通过；隔离 PGlite 直接从本批 Edge 源码提取生成规则，确认旧 32+140 失败、新 32+128 成功创建首个用户/首管。当前状态是“本地已交付、等待上传和真实主链验收”，不是云端完成。

用户手动上传 R4 后，事件 1069 于 19:33:15 完成：7 项变更、0 删除，1528 个目标文件哈希全部通过；此前上传受自动安全审查阻止保留为历史。1076→1406 接线轮次结束后，源码复核发现仅检查平台用户有手机号、结合 `phone_autoconfirm=true` 可能绕过短信证明。随后严格串行执行 1408→1519（写入安全门但未部署）、1521→1579（部署与探针回执）。云端报告 OTP 证明与平台 sub 绑定加固、旧 email 接口 410、伪 JWT 401、恶意 Origin 403，首管尚未认领。真实短信、云端 v9/v10 完整代码回收和独立验收仍待完成；36 个 API 返回 503、私有存储和 cron 未做，不能认定认证或整站迁移完成。

R4 源码 `fa3e8625` 已推送迁移分支并应用到秒哒源码树：后台设置、AES 兼容和事务权限门控通过 Deno 19 测试及隔离 SQL 27 断言；应用源码时未执行 SQL、未接通接口、未重建静态前端，不能据此认定后台可用。双配色 Logo、公共品牌配置与管理员上传／恢复入口已打为 R5，源码 `0b0cb006` 及后续文档 `b74e3395` 均已推送迁移分支并远端核实；R5 后由用户手动上传。网站配置 Deno 23 项、隔离 SQL 15 断言通过；R5 独立恢复目录完成 1555 文件哈希、冻结安装、TypeScript 和 Vite 3105 模块构建。管理交互仍是本地模拟 API 验证，云端管理员保存未验收，详见[迁移回执](./revisions/2026-09-25-miaoda-source-migration.md)。

最新见[百度秒哒源码迁移](./revisions/2026-09-25-miaoda-source-migration.md)：R1 `cf9fd133`、R2 `80d49a91`均已推送；修复我的空间对齐、工作台标签滚动、参考上传和画面拒绝优先，补声音配置检查。R2完整叠加树528测试／5670断言和生产构建通过，多宽度真实浏览器通过。R3 `ba81b374`已推送迁移分支，严格类型检查、13项Deno/8项前端/89项SQL及独立Vite构建通过，仍有API与数据待迁，不能称迁移已完成。供应商余额接口已公开但言剪未集成，不构成成本硬封顶。

最新工作台见[工作台与声音接入](./revisions/2026-09-25-editor-voice-integration.md)：19 个原生动效、20 个 CC0 实体音效、6 种转场，编辑器附件与 @、AI 精确插入、预览异常恢复及 MiniMax 报价任务接口；实际导出约 12 秒 H.264＋AAC。源码 `b23b7625`，526 项测试与正式构建通过；生产已执行兼容迁移 0009。随后用户更正[定价卡 v1.1](./revisions/2026-09-25-voice-pricing-v11.md)，移除误引的供应商预估要求，改为管理员校准和实扣超 9 元告警暂停；Key及真实样本仍待补，不能当付费联调已完成。

最新交互与验收见[作品发布与统一成片](./revisions/2026-09-25-gallery-protocols-rendering.md)：导出可主动同步广场，用户可另行上传和撤下；首页/广场共用真实瀑布流。移除重复风格选择器，附件有缩略图，浮层不推移输入区；客服二维码本地上传。497 项测试与三平台 CI 通过，真实模型两轮完成12秒裁为10秒、添加入场标题标签并导出MP4。当前结构剪切和包装仍需分轮确认，无声短片不等于真人口播质量通过。

以下结合 09-10、09-15、09-16 修订及源码检查更新；历次证据见 [history.md](./history.md)。

| 能力 | 当前实现与验证边界 |
|---|---|
| 中文剪辑工作台 | 基于 OpenCut 真实素材、预览、时间线与导出；云端账号保存工程/素材描述，新原片留在本机，浏览器保存读句柄并负责预览、解码和 MP4 导出；缺失素材可重新关联，旧云素材兼容 |
| AI计划与统一工作台 | 首页模式、11 个可选技能、提示词、@ 技能与附件、画幅/时长进入持久化需求；独立风格入口已移除，风格由技能和文字表达。每轮最多组合 4 个技能、检索 6 个配方，经证据/时间/布局校验后转原生命令；计划先报价确认，失败退款 |
| 模板与执行稳定性 | 首页与工具箱共用技能目录，映射现有内部合同；技能可组合且后续对话可调整场景。用户调试后可命名保存时间线模板、删除及换素材应用，当前浏览器最多 30 个。项目指纹、串行命令、严格保存与撤销/重做；不保证整轮原子回滚 |
| 专业剪辑 | 已接入停顿处理、字幕、倍速与音调保持、淡入淡出、转场、ducking、响度估计、代理、高光与速度曲线路径；复杂与长视频场景仍待系统验证 |
| 包装与关键帧 | 19 个原生动效配方可预览/编辑/引用 AI；6 种转场可拖到相邻接缝，20 个真实音效可手动添加或引用。白板为原生图形/文字/关键帧，可进入 MP4。尚无逐笔手绘、自动避脸或任意 AE 效果 |
| 参考与编排 | 根据明确画面／参考分析请求抽取有限6帧，拒绝发送优先，不再用独立勾选；作为风格参考而非成片素材。157镜头配方和214样式元数据用于检索，已有二维推近／拉远／平移；不宣称完整视频理解和任意复刻 |
| 声音与渲染服务 | MiniMax Turbo/HD 报价任务、录音输入、改名删除、固定试听与积分事务已实现。v1.1 改为实测校准与实扣超 9 元后暂停；Key、校准与后台扫描待补，未付费联调。Remotion Worker仅本机出片，公网部署与AI自动回填未完成；HyperFrames独立HTML Worker未实现 |
| 购买与积分 | 在线版本支持管理员生成/停用充值码、用户兑换、AI/ASR 报价与失败退款；客服人工购买和正式价格仍按运营确认 |
| 管理后台 | `/admin` 已接入真实账号、Neon、加密配置、用户管理、审计和充值码；新增客服二维码本地拖拽上传、渲染配置状态。普通用户不能访问管理接口 |
| 作品广场 | 导出默认私有，可主动同步；本地成片可单独上传，作者撤下、管理员审核；首页共用分页瀑布流，点击播放，公开成片占云空间但不连带上传原片 |
| 最近验证证据 | 2026-09-25：526 项测试、5649 断言与正式构建通过；声音任务/校准/告警共22项隔离数据库场景通过，未调用付费供应商；真实浏览器导出约12秒动效/转场/音效H.264＋AAC。之前发布/撤下、二维码及两轮真实模型10秒MP4仍留作历史证据，不等于真人长片质量通过 |
| 豆包 ASR 2.0 标准版 | 已接入服务端异步提交/查询、300 积分/小时报价与确认扣费、失败退分、云端任务归属和刷新恢复；真人长视频、上传速度和供应商等待时长仍待用户实测 |
| 当前录屏验收 | 账号制已有管理员；本轮验证工程/素材恢复与原生图文导出，另做真实模型文字规划补验。ASR未重跑，不能把白板或小型合成片当作真人语义剪辑质量通过 |

最新验收补充（2026-09-23）：本地干净工程已真实跑通口播停顿精剪、中文本地字幕、AI 标题/信息条包装和关键帧开关；工程重开恢复成功。浏览器实际下载成片，ffprobe 确认 14.001633 秒、H.264＋AAC、640×360。小型合成测试片不等于真人识别准确率或长片性能通过，详细证据和最终测试数见本日浏览器验收记录。

当前客服资料、模型参数、套餐试验价格及具体测试细节按相应日期的revision读取，不把开发登记值当成现行商业承诺。已撤销的独立包装中心和旧自动收银台只保留在历史记录中。

尚未完成（不影响本次个人在线测试）：

- 秒嗒生产接线、真实多运营商国内链路和正式备份/对账流程；Vercel 个人测试版的 Auth、Postgres、Blob、管理后台、积分和跨账号边界已经部署并完成黑盒基础验收。
- 声音服务的后台 Key、管理员真实校准、短周期任务扫描和付费联调；已撤销不存在的价格预估前提。网站删除声音不代表上游模型被删除，未知提交需人工对账。
- AI 对真人口播、长视频和复杂多轨的系统验证；当前音频按完整源文件估算内存，超预算会拒绝，不是长视频流式分析。
- Remotion Worker云端部署、AI自动调用、结果回填与合成验收，以及HyperFrames HTML Worker；本机渲染成功不等于这些已完成。Zeabur连接无效且尚未购买主机，用户无需为体验当前原生动效的最小闭环先买服务器。
- 专业剪辑能力仍待补齐：片段 slip/slide、响度标准化与真峰值计量、代理持久化与音画代理、速度曲线编辑器、复杂调色、运动跟踪、多机位和更稳定的语义高光模型。
- 模板仍需真实场景成片质量、音乐/音效编排和反复对话修订验收；批量并发、多机位、完整语义高光与数字人克隆尚未完成。
- 正式商业域名、隐私政策最终审阅和长视频/多轨质量验收。

## 文件索引

| 文件 | 作用 |
|---|---|
| [`revisions/2026-09-25-miaoda-source-migration.md`](./revisions/2026-09-25-miaoda-source-migration.md) | 最新：工作台修复、声音配置检查、R1/R2复建、秒哒实际接收与运行时适配缺口 |
| [`revisions/2026-09-25-voice-pricing-v11.md`](./revisions/2026-09-25-voice-pricing-v11.md) | 最新声音规则：撤销误引预估接口、实测校准、实扣告警与成本/计费边界 |
| [`revisions/2026-09-25-editor-voice-integration.md`](./revisions/2026-09-25-editor-voice-integration.md) | 最新：工作台统一、20音效/19动效/6转场、预览修复、MiniMax任务、真实导出与未开放边界 |
| [`revisions/2026-09-25-gallery-protocols-rendering.md`](./revisions/2026-09-25-gallery-protocols-rendering.md) | 最新：发布与撤下作品、首页交互、模型协议、二维码、统一剪辑成片验收及实际Remotion接线缺口 |
| [`revisions/2026-09-17-local-first-manual-spectrum-ui.md`](./revisions/2026-09-17-local-first-manual-spectrum-ui.md) | 本地优先使用手册、工作台与导航修订、Spectrum UI 按需参考边界 |
| [`revisions/2026-09-25-composable-skills-ui.md`](./revisions/2026-09-25-composable-skills-ui.md) | 前轮：模式与多选技能、统一提示词、响应式UI、注册协议、真实模型组合白板及MP4验收 |
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
