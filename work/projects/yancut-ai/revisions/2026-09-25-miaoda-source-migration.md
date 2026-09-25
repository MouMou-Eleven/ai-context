# 百度秒哒源码迁移、工作台修复与声音配置核验

日期：2026-09-25。来源：建委本轮明确要求先修复截图问题，再新建百度秒哒项目完整迁移；本轮源码、压缩包复建日志及统筹代理在线核验回执。这里记录截至本次回执的阶段事实，不把接收源码当作部署成功。

## 方向变化

此前默认每轮同步 Vercel 测试版；本轮改为以百度秒哒承载和后续迭代为目标。继续维护本地权威源码、GitHub 和本上下文，云端适配结果也须回同步；不再自动把每轮更改发布到 Vercel。旧 Vercel 入口保留历史测试与回退用途，不能将本轮未发布的代码称作现行 Vercel 版本。

用户已完成百度秒哒账号登录。已新建应用`app-enipq7iozwn5`，会话`conv-enipq7iozwn4`。这是百度miaoda.cn平台，不是飞书妙搭Spark。R1全量源码及R2增量已上传并收到哈希通过回执，R3候选已上传。generate-app实际调用一次后在事件825失败；随后同应用chat恢复在事件835再次以平台错误终止，未publish。

### 本轮最后核验：生成失败与认证方向更新

先生成PRD并核验generateApp结构动作后，官方CLI实际发起一次generate-app。事件825最终错误为`ServiceUnavailable / MCPGenerateError GenerateStartHook unexpected error Response is not valid JSON`。不能把调用返回应用标识或附件收齐写成生成成功，不重复触发未知状态的生成任务。恢复时先读取同一应用及会话轨迹，再决定如何继续。

之后仅提交一次同应用chat恢复，没有重复generate-app。事件827为恢复请求、829运行、831文字回复恢复迁移，但这些均不是实际执行成功证据。最终17:58:40事件835为`terminal: true`，错误仍为`MCPGenerateError: GenerateStartHook unexpected error: Response is not valid JSON`并伴ValueError；用户可见“秒哒遇到一点问题／秒点稍后返还”。本轮不再重复请求，没有向客服发消息，也没有发布；下一轮先检查平台状态及同会话，不用重建应用掩盖失败。

本轮云端曾用Bun1.4.2／pnpm重新解析依赖，原锁hash因此不一致。已要求恢复原锁并使用Bun1.2.18复测，但截至最终回执没有足够证据认定云端原锁冻结安装与构建通过；本地干净复建通过与云端验证分开记录。

用户最新授权改用秒哒平台原生手机号Auth，覆盖此前以自建密码／opaque Bearer迁移作为最终认证方向。R3已写代码及其测试保留为历史候选，不等于最终Auth已接通；手机验证码接收、登录会话、旧账号映射、管理员归属及积分归属都还要真实验证。

本实例数据库状态为ACTIVE_HEALTHY，且已有服务端角色插入探针成功，只能证明实例与该写路径可用；不能证明业务表全部就绪、私有对象存储上传／签名／清理或短信认证可用。未执行旧生产DB、Blob和用户迁移，也未调用付费声音。Skill与源码增量实践见[秒哒阶段案例](../../../domains/development/tools/miaoda/experience/cases/codex-skill-source-migration.md)。

## 本轮修复与已验证边界

| 用户问题 | 实施结果 | 验收证据与限制 |
|---|---|---|
| 我的空间标题／标签／内容未对齐 | 统一内容宽度和共同左右边界，进一步去除任务中心窄容器 | 真实浏览器6个我的页面分别在2375、1100、390px通过对齐检查；秒哒正式站尚未验收 |
| 资源标签后部不可发现 | 工作台资源条添加可见左右滚动按钮，保留单行 | 1600、1100px分别滚动214、130px，左移可回0；页面没有整体水平偏移 |
| 参考视频选择像纯文字 | 明确上传按钮、参考预览与交互状态 | 本地浏览器核查；待迁移后同场景复验 |
| 独立勾选抽样画面增加负担 | 根据用户明确画面分析／参考请求判断抽样需求；明确拒绝优先，补齐“不要把视频上传”及英文倒装拒绝 | 拒绝分支21条断言；只涉及有限抽样画面，不代表默认上传原视频或取得无限素材使用授权 |
| 声音填密钥后能否真正使用 | 管理后台新增只读配置检查：密钥、私有存储、扫描密钥；声音页面显示具体缺项；可一次保存Key、Turbo/HD及管理员标定设置 | 凭据存在不等于已联调。服务仍按v1.1至少5次真实成本样本校准再公开开放；无真实声音Key，本轮没有付费克隆 |

MiniMax 声音任务继续使用 `/v1/audio/generations` 提交／查询，固定克隆试听、1600积分克隆和Turbo/HD每100字符10/20积分规则未变。供应商文档已公开 `GET /api/usage/wallet/` 余额查询，言剪尚未集成；不得再将未集成误写为供应商没有余额接口。查询余额不等于预估单次任务成本，也无法据此保证并发和在途任务硬封顶。真实校准、分钟级后台扫描及付费联调仍待完成。

## 源码版本与包

源码仓库：[MouMou-Eleven/yancut-ai](https://github.com/MouMou-Eleven/yancut-ai)。R1 基线提交为 `cf9fd13374a24e7420b9e91f46895a50dba156dd`；R2 目标为 `80d49a913de605a81fea8bf2a5614f4fef7f1c5c`，两者已推送，R2通过远端main读取确认。

| 包 | 大小（字节） | SHA-256 |
|---|---:|---|
| `yancut-JW-20260925-R1-01.zip` | 16518381 | `58efdbf59e02ef8b6adeda44b362c55289cdc58af09785d48e88d95427fb84c1` |
| `yancut-JW-20260925-R1-02.zip` | 2490492 | `f0a6abf25bcf508a1e70a4496974fcae93cdaf5323acf9bf8353e7e6df86202b` |
| `yancut-JW-20260925-R2-increment.zip` | 38840 | `c4aab445aca2044588cc55067f1747cf007ef0f1a8aefb0a5ea5a09d8675b427` |
| `yancut-JW-20260925-R3-increment.zip` | 187288 | `5584e471889038ff3c1b766601a7ff1b1c2c51b3cc513defc7ca866f4659926b` |

本地交付目录分别位于 `C:/Users/Administrator/Documents/Codex/2026-08-10/w1/yancut-miaoda-R1`、`yancut-miaoda-R2`。R2仅4个文件：任务页布局、画面拒绝规则及测试、声音余额接口说明；无数据库迁移、无删除。保留无关 `.agents/`、`skills-lock.json`，未将密钥或真实.env装包。R2另附INSTALL、ACCEPTANCE和包外VERIFICATION清单；R2不能独立构建，必须先还原R1完整基线再应用。

## 干净复建

R1两ZIP及1488文件哈希通过。新目录恢复后，Bun1.2.18冻结锁文件安装成功，528测试／5666断言通过，Next16.1.3生产构建成功。R2先核验全部R1源文件，再验证4项旧hash／新payload hash，应用后验证目标hash；完整叠加树528测试／5670断言通过，TypeScript和56个静态页生产构建成功。

实际目录：`C:/Users/Administrator/AppData/Local/Temp/yancut-miaoda-clean-2fa87d8014bd400396e7032b6b0a98c8`，日志 `clean-install-1.2.18.log`、`clean-tests.log`、`clean-build.log`、`r2-tests.log`、`r2-build.log`。仅使用无效构建占位配置，无生产数据库或收费供应商调用。遗留博客抓取曾返回429／连接超时，未导致构建失败；这不证明全站外部依赖均可达。

## 在线运行时核验与尚未迁移内容

R3迁移候选在源码分支`codex/miaoda-runtime`，提交`ba81b3744a3c38275a2e8bb4756628b5ccc0db7d`已推送并远端核验。37个文件变化：Vite运行壳复用原页面和编辑器，Deno身份/钱包/工程/素材元数据/管理基础接口，以及封闭SQL事务RPC。原Next源码不替换，未实现服务明确503，不得作为完成版发布。

R3独立恢复树全量基线与37个目标hash通过；Bun1.2.18冻结安装954包、Vite3103模块生产构建通过。严格前端TypeScript检查通过；8项前端接口回归48断言、13项Deno测试、89项隔离PGlite断言通过。隔离SQL并非真实多连接并发或秒哒生产数据库验收。测试与构建日志位于`C:/Users/Administrator/AppData/Local/Temp/yancut-miaoda-r3-clean-7fac9239e4284a5280df71eb29c2cf37`；交付包与回执在本轮工作目录`yancut-miaoda-R3`。

R3历史候选的身份兼容须精确区分：保留原text UID、BetterAuth1.4.15密码哈希与session表，跨域新建opaque Bearer并在localStorage持久化，不是原HttpOnly Cookie或Supabase JWT。此路径的最终方向已被用户最新平台原生手机号Auth授权替代；代码测试不能证明新Auth或旧数据迁移完成。私有audio/video仍须正确鉴权或换短期签名URL。

统筹代理在本次新建秒哒项目核验到：当前交付环境为Vite SPA + Supabase Deno Edge，而言剪包是Next服务端应用；不能原样部署，必须适配。此结论针对本账号当前应用环境，不扩写为平台永远不支持Next或容器。

源码盘点有47个Next API路由、25个Postgres表声明，涉及BetterAuth、Cookie／headers、Postgres事务与行锁／advisory lock、积分幂等、私有Vercel Blob签名直传与转存、Node DNS／HTTPS防护以及后台任务扫描。移植时须保持实际权限、事务和错误语义，不用只可展示的Vite首页冒充完整迁移。

当前尚未完成：

- Next前端框架边界和47个后端路由到秒哒环境的适配、云端构建和正式发布。
- 旧数据库、账号、钱包账本、任务和Blob对象迁移。不得建立新的空账号系统后宣称旧数据已继承。
- 换域名后的本地文件句柄重新关联：浏览器IndexedDB与授权按origin隔离，不能靠数据库迁移自动继承。原片仍留本机。
- 声音真实付费校准与分钟级扫描。存储密钥、扫描密钥存在不等于调度已执行。
- 独立Remotion容器部署、AI自动回填及完整合成验收；HyperFrames独立HTML Worker仍未实现。平台有数据库和对象存储不等于有Chromium渲染服务。

后续继续按[全量源码交接](../../../domains/development/tools/miaoda/experience/patterns/codex-source-package-deployment.md)和[版本化增量闭环](../../../domains/development/tools/miaoda/experience/patterns/codex-miaoda-iterative-increment-workflow.md)执行。需要适配包、实际迁移日志、正式域名版本和真实剪辑导出证据，才可将“已上传核验”更新为“已部署验收”。
