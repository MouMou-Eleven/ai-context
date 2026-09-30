# 言剪 AI（YanCut）

> 状态：建委确认官方干预后开发对话已恢复；2026-09-30 截图记录 v71–v75 的 UI 修改、静态重建与动态 chunk 发布修复。截图是云端回执，尚未回收 v75 源码或独立复测；此前开发任务 INTERNAL_ERROR 的根因仍未知。下一轮以恢复后的云端差异校准基线，保护加载、认证、依赖、CORS 及静态发布热修，不用旧 B8/B11 覆盖。
> 当前口径确认：2026-09-30。**当前状态看"当前进度"一节**；下面的批次记录只代表各自当时的状态。云端回执、本地验证与正式站验收分别记录

原 Vercel 测试／回退入口（非秒哒）：[言剪 AI](https://yancut-ai-personal.vercel.app) · [登录/注册](https://yancut-ai-personal.vercel.app/login) · [在线帮助](https://yancut-ai-personal.vercel.app/studio/help)。真实账号、Neon 数据库、管理员和积分继续使用；原片保留本机，云端保存轻量工程与素材描述，旧云素材和明确上传的识别音频/作品仍使用私有 Blob。09-25 的工作台更新见[这里](./revisions/2026-09-25-editor-voice-integration.md)及[声音定价更正](./revisions/2026-09-25-voice-pricing-v11.md)，存储方向见[统一入口与本机原片](./revisions/2026-09-25-unified-local-media-workspace.md)。[早先云端上线记录](./revisions/2026-09-25-online-cloud-launch.md) 保留历史，但“所有原片上传云端”不再作为当前口径。旧的免登录/个人 Key 模式也未恢复。

## 各批次记录（按时间倒序；当前状态以下方"当前进度"为准）

[B8：创作确认、画面批注与服务测试](./revisions/2026-09-28-b8-creation-review-and-service-tests.md)：实现与原始测试范围；最新云端回执及下一轮保护项以本页“当前进度”为准，连接查询不能替代成片功能验收。

[B7：管理员 MCP、辅助会话与 v42 热修保护](./revisions/2026-09-28-b7-admin-mcp.md)：含密码眼睛、最长7天会话和后台自检。最新 v43/v44 回执与线上 MCP 实测见 B8，原记录保留当时交付边界。

[B6：真实运行日志与受控 AI 辅助调试增量包](./revisions/2026-09-27-b6-runtime-logs-and-ai-assistance.md)：保留 v39 依赖碰撞与处置历史；新的执行成功截图已由 B7 记录更新，不再按“等待方案 A 结果”处理。同一修订保留精简知识维护约定。

[当前源码基线与不重复付费导出约定](./revisions/2026-09-27-paid-source-baseline-ep8e1gojj18g.md)：完整ZIP已双路径保存、SHA256及全包CRC验证；源码Git HEAD `fd538fe0`。后续优先同步定点diff，不例行要求重新下载源码。本记录取代下方“等待源码”状态。


[v35–v38回执与B6实施规格](./revisions/2026-09-27-v35-v38-receipts-and-b6-observability.md)：前期问题范围备查；完整源码已经归档，后续状态以本页当前进度为准。


[B5：游客浏览、用户价格表与豆包识别](./revisions/2026-09-27-b5-guest-pricing-and-doubao-asr.md)：已纳入当前后续基线；公开浏览无需登录，使用功能需登录；消费展示采用极速/标准品牌名称，极速默认。当前游客来源修复见 v47。


[B4：Token结算、双语界面与加载热修保护](./revisions/2026-09-27-b4-token-localization-and-loading-lessons.md)。该记录优先于下方历史B3待上传口径；价格中心位于我的空间后，FlashX默认，50积分为Token预留上限。

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
- 视频包装：原生可编辑预设与真实框架渲染分开。B3新增render_motion源码任务、Remotion/HyperFrames独立Worker及可撤销回填同一时间线；两框架可信fixture本机实际出片、HTTP模拟回填通过。Docker生产隔离、公网服务与真实模型整链尚未验收，不能认定上传ZIP即已接通。
- 模型默认方向按 B4/B5：FlashX 为极速默认，Flash 为可选标准；公开界面使用言剪品牌名称，已保存的后台配置须单独核对，不用代码默认覆盖密钥或设置。统一规划器的多协议适配不代表所有厂商已联网实测。素材观察仍为经授权的有限静帧抽样，不等于完整视频或音频理解。
- 原 Vercel 最后记录版本（非秒哒）：2026-09-25 固定域名指向 READY 生产 `dpl_Gbuh1NLbpg7t3zkcDmS3Ks37txoF`；验收 Preview 为 `dpl_FmjyMVSLiHE4yK8YxtBm12LW9E18`，运行代码 `bdd71f13`。前版 `dpl_H4pCaqFCNEuh9RsLtLM8a1ivRBCK` 保留回退，但其旧声音价格预估前提已作废。真实账号、Neon、管理员、积分继续使用；兼容迁移 0009 已执行，回退不删除任务表或账本。国内直连此前失败，本轮使用代理验收，不能保证裸连可用。最终承载平台仍为百度秒哒。
- `F:\桌面文件\言剪AI` 是原源码仓库位置，不直接作为当前秒哒 B8 的修改基线。当前本地目录与热修差异见下方“当前进度”。
- 源码仓库为私有仓库 `https://github.com/MouMou-Eleven/yancut-ai`，`upstream` 跟踪 `https://github.com/OpenCut-app/OpenCut.git`。09-16 已将多轮实现提交，合并历史至 `b0b24335`，后续测试发现范围修正为 `22023132`；核对和修复了本地/远端历史分离及字体预览损坏。后续任务仍需实际查询最新 HEAD。`ai-context` 保存项目上下文，不保存完整源码。
- 持续同步约定（本轮更新）：后续以百度秒哒承载和迭代为目标，维护本地权威源码、GitHub及本项目README/修订记录；不再自动继续Vercel发布。旧Vercel作为历史测试／回退入口，秒哒云端适配改动也须同步回源码，避免分叉。
- 开发与部署分工：采用“本地权威源码 + 百度秒哒云端接管”。前端、业务逻辑、价格权益、数据库 Schema、接口合同、Mock 和自动化测试先在本地完成；验证通过后按编号压缩包交付百度秒哒，由秒哒接入 Auth、Postgres、对象存储、Edge Function、短信能力和部署。
- 秒哒初期兼容记录（事件1016，当时状态，已被后续接线取代）：应用`app-enipq7iozwn5`为Vite SPA + Supabase Deno Edge，与原Next16.1.3／47API／25表不能原样兼容。825/835失败后按用户要求串行chat，最终1016完成静态预览；外部浏览器确认原首页和邮箱密码登录页可见，但后端未接、登录禁用、未publish。旧DB/Blob/用户未迁，云端pnpm冒烟不是原锁构建，见[迁移修订](./revisions/2026-09-25-miaoda-source-migration.md)。

## 当前进度

本轮是官方恢复后的故障复盘与经验回写，不追加应用开发或发布。后续按[秒哒协作方法路径 B](../../domains/development/tools/miaoda/workflow.md)执行。

| 对象 | 当前事实与边界（2026-09-30） |
|---|---|
| 开发执行恢复 | 建委明确表示找官方恢复后已能对话和修改。此前四次不可重试 INTERNAL_ERROR 与恢复后的前端问题分开归因；未取得官方后台根因、恢复操作或资源日志，不能认定某增量包、安全漏洞或备份膨胀导致沙箱失效。 |
| v71–v73 回执 | 截图报告工具栏、我的空间源码修改及 lint 通过，但建委在 v72 后反馈没有变化；v73 才查明页面加载静态产物，需将 preview/apps/web/src 经构建发布到 public/yancut，并切换根 index.html。这是源码到产物未完成更新的证据，不是附件传错应用的证据。 |
| v74–v75 回执 | 截图报告 v74 调整空间布局；随后进入工作台失败。v75 将错误归于发布时移走 public/yancut 旧目录，旧页面请求旧 hash chunk 返回 404；报告改 tasks/build-static-preview.sh 为合并发布、保留旧 chunk，并在 main.tsx 加 vite:preloadError 的会话内一次刷新恢复。截图末显示“已发布”；具体正式域名当前版本、响应头、保留策略及真实浏览器仍待验收。 |
| 9/29 源码保全与我方验证缺口 | 既有快照已归档；本轮只读复核根 tsconfig.check.json 的 include 为 ./src，不能证明 preview/apps/web/src 工作台通过检查；根 build 脚本仅输出提示，嵌套 web/build 是 Next 构建，均不能替代秒哒 Vite 产物验证。快照没有 tasks/build-static-preview.sh；不视为已经回收 v75 脚本。此前 B11 的整包验证口径需撤回。 |
| 备份资源线索 | 已核查快照 .release-backups 有 38 个目录、1,856,067,357 字节，25 份 R7 备份重复保存大素材。资源膨胀确实存在，但没有 OOM、磁盘耗尽或官方因果说明。保全后评估容量及保留策略，不能为减体积直接删恢复点。 |
| B8/v46 回执 | 用户图一报告 16 个目标文件 after hash 匹配、7 个保护文件未变、213 项回归通过、双 Edge Deno 检查/部署及根 lint/静态构建通过，无新迁移。这是秒哒执行回执，不是本轮独立下载云端源码或正式域名验收。 |
| MCP/服务查询回执 | 报告两套 Edge 均发现 8 个工具；LLM 查询 authenticated，声音查询 inconclusive + task_not_exist；游客普通 401 未被当成辅助会话失效，越权/无效令牌拒绝。排查中手工测试令牌不符合 64 位小写十六进制合同，改用合法测试输入后通过；不能据此改弱鉴权。测试管理员会话报告已撤销。 |
| v47 热修 | 用户图二报告公开广场 `/api/yancut/gallery?scope=public` 被 Edge 的 `ORIGIN_DENIED` 拦截，原因是原来源集合遗漏预览别名。秒哒修改两套 `server/handler.ts` 的 `isAllowedOrigin` 并部署，报告预览 Origin 返回 200、第三方 Origin 返回 403、根 lint 通过。未取得函数全文；不擅自重建其实现或放行所有平台域名。 |
| 当前云端差异 | 旧 B8 尚缺 v47 handler 热修；恢复后的 v71–v75 又改了工具栏、guest-space.tsx、main.tsx、静态发布脚本及入口。下一包前定点回收这些文件/精确 diff/哈希、实际构建配置及版本引用，并保护认证桥、v42 api-client.ts、v44 根依赖与锁文件。缺全文时只做不冲突改动，禁止旧整文件覆盖。 |
| 待验收 | 完整浏览器三身份流程、真实授权素材剪辑导出、长视频/高码率/多轨性能、Windows/Safari、收费识别/声音/生成、公网 Remotion/HyperFrames Worker；B8 的画面批注仅支持定点文字与短素材叠加，不能宣称任意局部重绘。 |
| 平台边界 | 秒哒对 FFmpeg 的回复已提炼到[当前事实表](../../domains/development/tools/miaoda/facts.md#应用运行时与工具安装边界)和[平台基础](../../domains/development/tools/miaoda/basics/platform-basics.md#引入-ffmpeg浏览器渲染器或-github-项目前怎么选)。应用 Edge、开发工具和外部 Worker 分开，不默认新增收费服务或上传本机原片。 |

复盘证据与归因边界见[迁移案例的官方恢复后复盘](./case-miaoda-source-migration.md#官方恢复后的静态发布复盘)。可复用诊断已写入[秒哒运行诊断](../../domains/development/tools/miaoda/topics/runtime-diagnostics.md#源码改了但页面没变先核对构建和入口)，执行门禁已改进[增量流程](../../domains/development/tools/miaoda/workflow.md)。

### 本机源码与交接入口

工作目录记作 `W = C:\Users\Administrator\Documents\Codex\2026-09-27\codex-threads-01a0dd1d-ccb1-7c73-9cc3-2`。以下路径于本轮检查存在，换设备或后续移动须重新检查，不把存在当成与云端完全一致。

| 路径 | 用途 |
|---|---|
| `W\work\b8-app` | B8 完整开发树；下一轮从副本开始，不修改此基线，不含 v47 云端热修。 |
| `W\work\b8-clean-final-app` | B7 完整树叠加 B8 实际 ZIP 的独立复建树，用于交叉核对。 |
| `W\work\b8-zip-verify` | B8 实际 ZIP 的解压校验目录，含 manifest、payload、安装器、测试、执行说明与证据；16 个 payload 哈希本轮重新核对。 |
| `W\work\yancut-b8-release` | B8 制包工作目录，参考用途；以 manifest 白名单为准，不能将整目录压缩（含仅本地依赖或残留文件）。 |
| `W\work\b8-rebuild.py`、`W\work\build_b8_release.py` | 完整基线复建与增量生成的既有方法；复制后调整下一轮版本，不原地重跑覆盖旧包。 |
| `C:\Users\Administrator\Documents\Codex\yancut-source-archive\2026-09-27-ep8e1gojj18g` | 用户付费导出的完整归档，含原 ZIP、`BASELINE.json`、清单及 `source` 审阅树。仅归档，禁止直接开发或再次例行收费导出。 |
| `F:\桌面文件\言剪AI-Claude交接\01-发给ClaudeCode.md` | 本轮同机交接提示词，含入口、文件分层、证据位置和下一轮增量要求。 |

原 `F:\桌面文件\言剪AI-B8\言剪AI-B8-增量包.zip` 本轮检查已不在原位置；不能继续给出失效链接或把重新压缩文件冒充原 ZIP。可核验的 B8 payload 和安装合同仍保存在上述解压目录，无需因此要求用户重新下载源码。

## 阶段历史（不是当前状态）

### R6至R8当时执行卡

当时执行入口：[完整迁移批次与有效沉淀](./revisions/2026-09-26-batch-delivery-and-effective-context.md)。内部阶段不强制各占一次上传。下方等待实施等是收到回执前的历史，不再据此重复安排。


当时执行入口：[R8实际AI接线包](./revisions/2026-09-26-r8-ai-implementation.md)。这次包含实现代码、追加迁移和定点安装器；下方云端执行说明为上一轮勘察阶段。

当时执行入口：[R8开始与v24云端适配](./revisions/2026-09-26-r8-cloud-adaptation.md)。采用增量代码与限定范围提示词结合，平台故障必须定位、修复或明确阻塞，不能被阶段声明遗漏。以下账户补充记录是上一交付阶段。

用户已上传 R7，当时独立检查发现该包漏带 studio-shell 的账户确认态修改；本地开发树通过不等于ZIP叠加树通过。现以完整导出＋实际R7 ZIP重建，并交付 R7-PROFILE 账户补充，详见 [本轮修订](./revisions/2026-09-26-r7-profile-feedback.md)。用户验证通过项与未完成的存储/积分/后台整体验收分开记录；当前操作不再要求重新全量导出。

以下表格保留 **R6.1 时点的历史执行卡**，其中“R7未开始”“待恢复管理员”等不是现状，不再作为执行指令。当前状态以上述本轮修订为准。旧证据见[迁移修订](./revisions/2026-09-25-miaoda-source-migration.md#r61-云端回执审查与知识纠错2026-09-26)。

| 项目 | 当前结论与下一步 |
|---|---|
| 环境与版本 | 百度秒哒 `app-enipq7iozwn5`，会话 `conv-enipq7iozwn4`；R6.1/v15，实际 Edge 为 `yancut-api-v2`。未正式 publish |
| 已收到证据 | 用户回传 R6.1 Markdown 和截图；4 个替换 hash 与本地包一致，5 个保护文件报告未变。此为云端回执，不是独立文件下载或真机验收 |
| 认证状态 | 用户此前确认短信收到；R6.1 修复占位哈希，报告 SQL 新值成功/旧值拒绝、Deno 7 项通过。真实注册至退出重登/重置密码仍待用户验证 |
| 首管故障 | 用户已确认唯一注册账号属于本人且须作为管理员。v17只读回执报告身份映射一致、admin_users仍为0；定向恢复尚未执行。不可清空bootstrap重开公开领取，不重复要求用户确认 |
| 新 UI 需求 | 已基于用户回传v17完整前端树实现密码眼睛、统一品牌Logo、账户读取15秒超时及不阻塞登录。原锁安装、完整tsc、Vite3023模块构建、五宽度完整前端UI检查通过；尚未应用云端，不称真实登录已修好 |
| 基线债务 | R6/R6.1包与云端热修差异尚未全部整合入源码迁移分支；下一包须回收对应文件与hash，保留短信构建变量和空响应兼容 |
| 未完成范围 | 管理员品牌保存、正式域名、真实账号完整链路及前轮列出的36个未迁API；旧用户/账本迁移、私有存储、cron和渲染服务不得默认已完成 |
| 下一步 | 上传前再次审查已补强覆盖后必须target及Python优化模式下的校验；仅上传`yancut-R6-closeout-20260926-reviewed.zip`，替代同日旧收口包。前端/SQL未变，完整实物解压校验通过；云端应用和真实账号闭环仍待验收。R7未开始 |



以下保留各轮当时结论。遇到“等待上传”“未接入”或“最新”等表述，按段落所述版本理解；当前执行只以“当前进度”及对应新证据为准。

（R6 时点）R6 已上传并由秒哒应用，后续云端热修复补齐构建时 Supabase 公共环境变量，用户实际收到短信；这证明验证码请求链已经跨过前端配置层，但不证明注册完成。注册提交返回“注册信息无效”，本地按云端文件哈希复查到 R6 `PLACEHOLDER_HASH` 摘要长度为 140，违反数据库 `32:128` 合同；原 Deno 测试把 RPC 模拟为恒成功，隔离 SQL 又使用了单独的正确测试值，两层测试没有连接起来。R6 状态改为“已应用、待 R6.1 修复”，R7 暂不开始。临时 `vitesandbox`、HTTP 200、云端 Chromium 自报和构建成功均不作为真实可用验收；完整原因与门禁见[本次修订](./revisions/2026-09-25-miaoda-source-migration.md#r6-云端执行与真实注册失败2026-09-26)。

R6.1 已生成不可覆盖交付包 `yancut-JW-20260926-R6.1-increment.zip`，18272 字节，SHA-256 `20e89bd5794a0266c89e926047fc818c8eb5a8c13a739dc2ca5c5ba5db180063`。它只替换两个 Edge 运行副本及两个测试副本，并以追加版回执 hash 保护构建脚本、前端认证桥、云端登录页和 database.ts；不执行新迁移、不自动发短信、不启动 R7。Deno 7 项与解压实物复测通过；隔离 PGlite 直接从本批 Edge 源码提取生成规则，确认旧 32+140 失败、新 32+128 成功创建首个用户/首管。当前状态是“本地已交付、等待上传和真实主链验收”，不是云端完成。

用户手动上传 R4 后，事件 1069 于 19:33:15 完成：7 项变更、0 删除，1528 个目标文件哈希全部通过；此前上传受自动安全审查阻止保留为历史。1076→1406 接线轮次结束后，源码复核发现仅检查平台用户有手机号、结合 `phone_autoconfirm=true` 可能绕过短信证明。随后严格串行执行 1408→1519（写入安全门但未部署）、1521→1579（部署与探针回执）。云端报告 OTP 证明与平台 sub 绑定加固、旧 email 接口 410、伪 JWT 401、恶意 Origin 403，首管尚未认领。真实短信、云端 v9/v10 完整代码回收和独立验收仍待完成；36 个 API 返回 503、私有存储和 cron 未做，不能认定认证或整站迁移完成。

R4 源码 `fa3e8625` 已推送迁移分支并应用到秒哒源码树：后台设置、AES 兼容和事务权限门控通过 Deno 19 测试及隔离 SQL 27 断言；应用源码时未执行 SQL、未接通接口、未重建静态前端，不能据此认定后台可用。双配色 Logo、公共品牌配置与管理员上传／恢复入口已打为 R5，源码 `0b0cb006` 及后续文档 `b74e3395` 均已推送迁移分支并远端核实；R5 后由用户手动上传。网站配置 Deno 23 项、隔离 SQL 15 断言通过；R5 独立恢复目录完成 1555 文件哈希、冻结安装、TypeScript 和 Vite 3105 模块构建。管理交互仍是本地模拟 API 验证，云端管理员保存未验收，详见[迁移回执](./revisions/2026-09-25-miaoda-source-migration.md)。

（R1～R3 时点）见[百度秒哒源码迁移](./revisions/2026-09-25-miaoda-source-migration.md)：R1 `cf9fd133`、R2 `80d49a91`均已推送；修复我的空间对齐、工作台标签滚动、参考上传和画面拒绝优先，补声音配置检查。R2完整叠加树528测试／5670断言和生产构建通过，多宽度真实浏览器通过。R3 `ba81b374`已推送迁移分支，严格类型检查、13项Deno/8项前端/89项SQL及独立Vite构建通过，仍有API与数据待迁，不能称迁移已完成。供应商余额接口已公开但言剪未集成，不构成成本硬封顶。

（09-25 时点）工作台见[工作台与声音接入](./revisions/2026-09-25-editor-voice-integration.md)：19 个原生动效、20 个 CC0 实体音效、6 种转场，编辑器附件与 @、AI 精确插入、预览异常恢复及 MiniMax 报价任务接口；实际导出约 12 秒 H.264＋AAC。源码 `b23b7625`，526 项测试与正式构建通过；生产已执行兼容迁移 0009。随后用户更正[定价卡 v1.1](./revisions/2026-09-25-voice-pricing-v11.md)，移除误引的供应商预估要求，改为管理员校准和实扣超 9 元告警暂停；Key及真实样本仍待补，不能当付费联调已完成。

（09-25 时点）交互与验收见[作品发布与统一成片](./revisions/2026-09-25-gallery-protocols-rendering.md)：导出可主动同步广场，用户可另行上传和撤下；首页/广场共用真实瀑布流。移除重复风格选择器，附件有缩略图，浮层不推移输入区；客服二维码本地上传。497 项测试与三平台 CI 通过，真实模型两轮完成12秒裁为10秒、添加入场标题标签并导出MP4。当前结构剪切和包装仍需分轮确认，无声短片不等于真人口播质量通过。

## 原 Vercel／本地能力基线（秒哒迁移对照）

以下结合 09-10、09-15、09-16 及 09-25 修订与源码检查整理；仅描述原 Vercel／本地验证范围，不能直接推断秒哒已实现或上线。历次证据见 [history.md](./history.md)。

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

验收补充（2026-09-23 时点）：本地干净工程已真实跑通口播停顿精剪、中文本地字幕、AI 标题/信息条包装和关键帧开关；工程重开恢复成功。浏览器实际下载成片，ffprobe 确认 14.001633 秒、H.264＋AAC、640×360。小型合成测试片不等于真人识别准确率或长片性能通过，详细证据和最终测试数见本日浏览器验收记录。

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
| [cases/miaoda-source-migration-case.md](./case-miaoda-source-migration.md) | 言剪从 Vercel 迁到秒哒的阶段实录：Skill 调度、浏览器上传源码增量、PRD 核验与生成故障；秒哒通用方法已提炼到[秒哒协作方法](../../domains/development/tools/miaoda/workflow.md) |
| [cases/b3-loading-hotfixes.md](./case-b3-loading-hotfixes.md) | B3 后加载热修：会话刷新阻塞、弹窗串行依赖、云端热修保护与本地/现场验收边界 |
| [revisions/2026-09-27-b3-editor-runtime-and-rendering.md](./revisions/2026-09-27-b3-editor-runtime-and-rendering.md) | B2已应用更正、B3包hash、64目标/314补丁、实际测试、Worker部署及完整未测边界 |
| [revisions/2026-09-26-b2-quality-and-redemption.md](./revisions/2026-09-26-b2-quality-and-redemption.md) | B1 v29回执、B2实物交付、渲染根因、同码多人兑换、安全及接口验收边界 |
| [`revisions/2026-09-26-r7-profile-feedback.md`](./revisions/2026-09-26-r7-profile-feedback.md) | 账户确认态补充、实物ZIP重建与用户回执边界 |
| [`revisions/2026-09-26-r7-source-audit.md`](./revisions/2026-09-26-r7-source-audit.md) | 完整导出与R7实际代码包对照、遗漏修复及源码审计 |
| [`revisions/2026-09-26-r8-ai-implementation.md`](./revisions/2026-09-26-r8-ai-implementation.md) | R8规划器实现、事务迁移、定点安装和本地测试证据 |
| [`revisions/2026-09-26-r8-cloud-adaptation.md`](./revisions/2026-09-26-r8-cloud-adaptation.md) | v24平台适配、保护文件、R8执行前故障定位与边界 |
| [`revisions/2026-09-26-batch-delivery-and-effective-context.md`](./revisions/2026-09-26-batch-delivery-and-effective-context.md) | 批次交付纠偏、云端回执核对与自然语言触发回归 |
| [`revisions/2026-09-25-miaoda-source-migration.md`](./revisions/2026-09-25-miaoda-source-migration.md) | 09-25：工作台修复、声音配置检查、R1/R2复建、秒哒实际接收与运行时适配缺口 |
| [`revisions/2026-09-25-voice-pricing-v11.md`](./revisions/2026-09-25-voice-pricing-v11.md) | 09-25 声音规则：撤销误引预估接口、实测校准、实扣告警与成本/计费边界 |
| [`revisions/2026-09-25-editor-voice-integration.md`](./revisions/2026-09-25-editor-voice-integration.md) | 09-25：工作台统一、20音效/19动效/6转场、预览修复、MiniMax任务、真实导出与未开放边界 |
| [`revisions/2026-09-25-gallery-protocols-rendering.md`](./revisions/2026-09-25-gallery-protocols-rendering.md) | 09-25：发布与撤下作品、首页交互、模型协议、二维码、统一剪辑成片验收及实际Remotion接线缺口 |
| [`revisions/2026-09-17-local-first-manual-spectrum-ui.md`](./revisions/2026-09-17-local-first-manual-spectrum-ui.md) | 本地优先使用手册、工作台与导航修订、Spectrum UI 按需参考边界 |
| [`revisions/2026-09-25-composable-skills-ui.md`](./revisions/2026-09-25-composable-skills-ui.md) | 前轮：模式与多选技能、统一提示词、响应式UI、注册协议、真实模型组合白板及MP4验收 |
| [`revisions/2026-09-25-unified-local-media-workspace.md`](./revisions/2026-09-25-unified-local-media-workspace.md) | 09-25 方向：统一首页、本机原片/云端工程、工具候选编排、模型适配、白板、上游核验、真实浏览器导出与部署 |
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
7. 涉及百度秒哒时先读[工具入口](../../domains/development/tools/miaoda/README.md)分流：初次迁移读全量交接，已有基线的更新/回执审查读增量闭环；涉及 Skill 再读能力矩阵。缺云端差异先取证，不用旧页面覆盖。
8. 开发任务完成后同步本地权威源码、GitHub及本项目记录；目标承载为百度秒哒，不再默认发布 Vercel。发布需按当前授权与验收范围执行，记录源码、环境、实际版本与回退边界；查状态不自动发布。

## 待确认事项

- 参赛的最终赛道、报名材料口径和演示时长。
- 声音供应商及定价方向已在声音定价 v1.1 确认；仍待真实 Key、付费校准及授权流程实测，不把已确认选型重新列为未知。
- 百度秒哒当期对 Next.js/React + Vite、手机号登录插件、短信服务、对象存储和长任务的实际支持情况。
- 正式支付渠道、套餐价格、模型与渲染成本、退款和发票策略。
- 上线版本是否继续保留 OpenCut 上游入口，以及具体的署名展示位置。

*索引与当前口径更新：2026-09-26；部署状态单独记录，不能从本地测试推断。*

## 后续写入

按根目录 AGENTS 与写入规范，普通更新直接修改本页当前事实或已有专题，不再为每轮反馈新建 revision。新增独立内容才补索引；可复用方法写秒哒领域，项目版本与证据留在项目。源码状态需要实际核对，不把旧 commit、本地 B8 或秒哒截图称为已回收的云端最新源码。
