# B2：实测问题修复、同码多人兑换与验收边界

日期：2026-09-26。依据：用户的 B1-RESULT.md、十一张界面截图及本轮明确需求。用户要一个实际增量包，不要仅计划；后续在百度秒哒迭代，不自动继续发布 Vercel。

## 当前状态与旧口径纠正

- B1 已由用户上传；v29 回执报告三份迁移、双 Edge、构建、cron 与隔离测试通过。预览已更新，回执未声称正式发布；报告不是独立云源码下载。
- B1 报告中真实登录、供应商、MP4、声音与外部 Worker 仍有未测项。不能把上传总包解释为完美复刻最终 Vercel。
- 新截图直接证明用户流程仍有缺陷：预览冻结、贴纸空白、提示词未衔接、后台布局等。本地 B2 修复已交付，云端尚未应用和验收。
- 基线为完整导出叠加实际 R8/B1；没有 v29 全量新导出。保护 v24 认证/工作台和 v29 云端修正，冲突必须定点合并并记录 diff/hash，不能整文件盲覆盖。

## 实物交付

- 文件：YanCut-B2-20260926.zip；3,625,938 字节；922 个包内文件；102 个目标文件，95 处唯一上下文补丁。
- SHA-256：8d0b0720a4e8fc574962ac78cdc25d863843e7b5d8545c0e328b10adf3a3c99e
- 本机会话输出：C:/Users/Administrator/Documents/Codex/2026-09-26/ch/outputs/YanCut-B2-20260926.zip。独立清单为同目录 YanCut-B2-CHECKLIST.md。此路径用于溯源，不作为其他机器可下载地址。
- 入口 START-HERE.md；含实际 payload、manifest、只读预检/备份安装/幂等/回滚、测试、证据、供应商与安全审查、B2-RESULT 模板。只执行新增 00022，不重放历史迁移；同号冲突须核对并记录映射。

## 根因、修复与验证

| 范围 | 本次实际实现 | 验证与限制 |
|---|---|---|
| 特效冻结 | WASM 不再同时发送 camel/snake 别名；动态 canvas/video 纹理逐帧更新 | Chromium 实际 WASM：动态红绿更新、20 特效像素均变化；用户视频 MP4 待云验 |
| 贴纸空白 | 64 个 Twemoji SVG 同域打包，保留 CC-BY4.0 归属与许可；失败缓存可重试 | 真实爱心像素验证；不是用边框可见代替画面出现 |
| 首页提示词 | 持久化工作要求、工作台同步、首次引导关闭后一次进入原计费确认 | 浏览器完整 UI，身份/工程 API 边界 mock；未同意不调用付费规划 |
| 加载与换号 | 公开首屏不被认证阻塞；白名单 GET 去重/短缓存/超时；写入换号失效、旧身份迟到响应拒收 | 16 项传输/QR 断言；缓存不作权限依据 |
| 界面 | 语言/登录44px，发布表单内边距，克隆入口可查看配置说明，六组服务标签保留草稿，QR 私有签名图 | 浏览器尺寸/弹窗/QR解码通过；声音缺配置仍禁止付费提交 |
| 库与技能 | 动效编辑置顶、20/页、本机收藏；言剪AI名称；9种真实关键帧转场；特效20/页；引用按钮描边；手写@与选择技能统一解析 | 9转场结构与原轨位置通过；预设/自写相同skillIds；画幅文字内置，旧项目兼容 |
| 同码多人 | 1000积分×5人生成一条160bit码；每用户一次、码总限额、行锁、唯一领取、原子钱包/流水/计数、哈希、撤销/过期、数据库限速 | 46项SQL/处理器断言含强制失败回滚；PGlite非真实多连接证据，云端仍需并发验收 |

共享码是持有者凭证，本次未绑定指定领取名单。知道码的账号可以占剩余额度，因此界面要求私发、泄露后撤销；不能承诺绝对防盗。普通用户在“我的→账户与积分→积分充值码兑换”使用。日期提供长期/1/7/30天和自定义。

## 接口与服务器结论

- 豆包大模型录音识别 2.0：现有 B1 使用 volc.seedasr.auc、X-Api-Key、/api/v3/auc/bigmodel/submit 与 query，已对官方文档核对；不臆造 model_version=400。官方：https://docs.volcengine.com/docs/DoubaoVoice/LargemodelrecordingfilerecognitionstandardversionAPI?lang=zh 。
- 大模型保留 Chat Completions / Responses / Anthropic Messages / Gemini generateContent；44项真实处理器和SQL回归以mock网络验证，不代表任意中转已联通。
- 现有声音为 Seedance 中转 MiniMax 协议，不是 MiniMax 官方直连；B2 明示区别并拒绝将官方域名误配到中转端点。官方先 multipart /v1/files/upload，再 /v1/voice_clone，来源：https://platform.minimax.cn/docs/api-reference/voice-cloning-uploadcloneaudio 和 https://platform.minimax.cn/docs/solutions/aipodcast 。没有渠道Key，保留成本校准/暂停，不假称已能克隆。
- 秒哒静态托管/Supabase Edge 不等于长任务 Chromium/FFmpeg Worker。用户服务器若具备 Docker/Node/Chromium/FFmpeg 可运行 Worker 并配置 HTTPS 队列/状态/令牌；未获得主机信息，未部署。

## 本地通过与尚未通过

已通过：另一份完整干净基线安装102目标、逐文件hash、原锁安装、TypeScript、3024模块生产构建；双Edge Deno检查；117安装器检查、46SQL/HTTP、16传输/QR、44 R8回归；实际Chromium/WASM及UI流程。最终ZIP独立解压后重新npm ci，117＋46＋16＋44共223项再次通过，102份payload SHA逐一吻合；交付核验文件为同目录YanCut-B2-VERIFY.md。

未通过不是失败掩盖：本轮云端合并部署、真实账号多连接并发、真实视频剪辑→特效贴纸→MP4完整导出、付费ASR/声音/LLM、公网Worker均待相应条件下验收。必须按独立CHECKLIST逐项回传B2-RESULT，保留未测原因。

## 可复用改进

已有秒哒增量协作处方新增本案例的可执行门禁，并由现有自然语言路由触发；项目README索引和当前状态同步。不能只新增无人读取的复盘文件。构建须遵循应用packageManager的pnpm10（当前10.33.0）；全局pnpm11会忽略旧pnpm.overrides导致原锁不匹配，不能改锁规避。
