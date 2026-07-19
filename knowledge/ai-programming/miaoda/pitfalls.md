# 秒哒踩坑清单

> 每一条都是真实踩过的坑，附"症状 / 根因 / 修复 / 预防"四段式。新坑请追加到末尾，不要替换历史条目。

---

## #1 SKILL.md 缺 YAML frontmatter → 上传被拒

**症状**：
```
❌ ZIP 包中未找到 SKILL.md，请确保文件位于根目录或一级子目录
❌ SKILL.md 格式校验失败：SKILL.md 的内容必须以 "---" 开头
```

**根因**：秒哒官方文档没写 frontmatter 是必须的，但实际校验代码要求 `name` / `description` / `license` 三个字段。

**修复**：在 SKILL.md 最前面加：
```yaml
---
name: your-skill
description: 一句话描述 + 何时触发
license: Proprietary
---
```

**预防**：打包前 `head -1 SKILL.md` 检查首行必须是 `---`。

---

## #2 Web Crypto 不支持 MD5 → 签名永远算不对

**症状**：Edge Function 里调 YunGouOS 接口返回 `{"error":"签名错误，请检查签名"}`。

**根因**：Deno / 浏览器 / 现代 Node 的 Web Crypto API **故意拒绝 MD5 算法**（因为 MD5 不安全）：
```javascript
await crypto.subtle.digest("MD5", data)
// → NotSupportedError: Unrecognized algorithm name
```
但很多老 AI 生成的"MD5 签名"代码用了这个 API，所以一上来就死。

**修复**：用纯 JS 实现 MD5（无依赖），或者在 Python 技能里用 `hashlib.md5`。本仓库 `references/edge_function_notify.ts` 文件里有验证过的纯 JS MD5 实现，可直接复制。

**预防**：写到提示词里——"禁止调用 `crypto.subtle.digest('MD5', ...)`"。

---

## #3 秒哒官方插件生成包密钥明文 → 严重安全事故

**症状**：让秒哒"自动创建技能"得到的 .zip 包里，`SKILL.md` 第 29 行 / 第 104 行 / 第 551 行、`references/*.md` 多处直接写着 partnerKey 字面量。

**根因**：秒哒生成包时不会主动用环境变量替代密钥，会原样写进文档/示例代码。这等于把支付通道控制权写进可分发文件。

**修复**：
1. 删掉所有文件里的密钥字面量，改为 `Deno.env.get("YOUR_KEY")` 或 `os.environ.get(...)`
2. 在秒哒「技能 > 环境变量」面板配置 Value
3. **去 YunGouOS / 对应平台控制台重置一次密钥**，原密钥视为已泄漏

**预防**：永远不要让秒哒"自动生成"涉及密钥的包，自己用工具构建。

---

## #4 zip 包多层嵌套 → 上传找不到 SKILL.md

**症状**：
```
❌ ZIP 包中未找到 SKILL.md，请确保文件位于根目录或一级子目录
```

**根因**：秒哒官方插件生成的包结构是 `.skills/<skill-name>/SKILL.md`——这是**二级子目录**，超出"一级"的限制。

**修复**：解压后把 `.skills/<skill-name>/` 这层去掉，重新打包。最终结构：
```
your-skill.zip
├── SKILL.md
├── scripts/
└── references/
```

**预防**：`unzip -l X.zip | head -5` 看顶层路径，第一条必须直接是 `SKILL.md` 或 `<dir>/`。

---

## #5 秒哒 AI 自己重写签名逻辑 → MD5 翻车

**症状**：你提供了技能脚本（含正确签名实现），但秒哒应用层仍然报"签名错误"。

**根因**：秒哒 AI 没用你提供的技能，而是另写了 3 个独立 Edge Function（`yungouos_get_oauth_url`、`yungouos_get_openid`、`yungouos_jsapi_pay`），每个都自己实现一份 JS MD5。其中：
- 用了有符号右移 `>>` 而非 `>>>`（数据超长时算错）
- padding 位置错位
- 用 `crypto.subtle.digest("MD5", ...)`（见 #2）

**修复**：明确告诉秒哒禁止重写，统一调技能脚本。提示词模板见 [prompt-patterns.md](./prompt-patterns.md)。

**预防**：提示词里把"禁止自己实现签名/MD5"放进红线段，前置在所有其他描述之前。

---

## #6 localeCompare 不等于 ASCII 字典序

**症状**：参数排序在某些字符（下划线、连字符与字母混排）下与 YunGouOS 服务端不一致，签名失败。

**根因**：
```javascript
sortedEntries.sort(([a], [b]) => a.localeCompare(b, "en"));
```
`localeCompare("en")` 与 ASCII 排序在多数字母数字场景一致，但**在边界字符上有差异**。

**修复**：用代码点比较：
```javascript
sortedEntries.sort(([a], [b]) => (a < b ? -1 : a > b ? 1 : 0));
```

**预防**：签名相关排序永远不用 locale，纯字符串比较。

---

## #7 YunGouOS 签名反直觉：可选字段即使有值也不签名

**症状**：把 `notify_url`、`attach`、`type` 等可选字段也加入签名计算后，YunGouOS 报签名错。

**根因**：YunGouOS 文档原话"只有文档中的必传参数才参与签名"。即使你传了可选参数（且 YunGouOS 会读取使用），它们也**不进入签名计算**。这与微信支付官方算法不同，要特别注意。

**修复**：脚本里严格区分 `required` 和 `optional` 两组字段，只把 `required` 喂给 sign 函数。

**预防**：写脚本时为每个接口列出明确的 required / optional 清单（[case-yungouos-jsapi.md](./case-yungouos-jsapi.md) 末尾有 5 个接口的完整字段表）。

---

## #8 支付授权目录前缀匹配 → "当前页面URL未注册"

**症状**：JSAPI 下单成功、jspackage 返回正常，但调起微信键盘时弹窗"当前页面的 URL 未注册: https://..."。

**根因**：微信支付要求支付页 URL 必须以"YunGouOS 商户后台登记的支付授权目录"为前缀。如果实际访问的域名是秒哒预览域名 `app-XXX.appmiaoda.com`，但你只登记了 `dejinzhoujin.com/orders/`，前缀对不上。

**修复**：在 YunGouOS 商户后台「配置支付目录」面板，添加实际访问的域名前缀，**末尾的 `/` 不能漏**：
```
https://app-bd0ygtaa9zwh.appmiaoda.com/payment/
https://dejinzhoujin.com/payment/
```

**预防**：上线前用 0.01 元在每个域名都测一次，目录配置变更后等 1-2 分钟生效。

---

## #9 秒哒 AI 改一边、忘一边 → PC 流程被破坏

**症状**：让秒哒"加手机端 JSAPI 支付"，结果原本好用的 PC 端 Native 扫码也坏了。

**根因**：秒哒 AI 倾向"重构"而非"扩展"。给"新增支付方式"指令时，它会把原有支付代码也一并改掉。

**修复**：把"PC 端 Native 不要动一行"写到提示词最前面。改完后必须两端都测一遍。

**预防**：提示词里红线段第一条就是"不要修改 X 任何代码"，并要求改完汇报"PC 流程涉及哪些文件，如何确保零修改"。

---

## #10 用户没有 Supabase 控制台访问权 → 想"对比"做不到

**症状**：调试时想对比"秒哒新建的字段是否真的加上了"、"两个 Edge Function 实际生效的 Secrets 列表是否一致"、"某条 SQL 跑出来什么结果"，但发现自己根本没有 Supabase 后台的访问权限。

**根因**：秒哒应用底层确实是 Supabase（Postgres + Edge Functions + Auth），但用户**没有**原生 Supabase 控制台账号——拿不到 Project URL、anon key、service_role key、SQL Editor、Logs Explorer 这些标准工具。

**替代手段**：秒哒应用编辑器侧栏内置的「**后端服务**」面板，4 个 Tab：
- **数据表管理**：看表结构、改字段值（一张张点开，无 schema 总览图）
- **用户管理**：看应用用户列表
- **后端函数**：看 Edge Functions 列表（有时只读源码）
- **密钥管理**：增删改全局密钥，但**写入后只显示 `••••`**，不能查看当前值

**做不到的事**（必记，避免反复尝试）：
- ❌ 直接在 SQL Editor 里跑 SELECT/UPDATE
- ❌ 看某个 Edge Function 当前实际生效的 Secrets 名字与值
- ❌ 看 Postgres 索引、约束、触发器的细节
- ❌ 看 Edge Function 集中的运行日志（要靠秒哒应用编辑器的"调试"按钮）

**预防/应对**：
1. 让秒哒做加字段、修脏数据这种操作时，**强制要求它执行后回贴 schema 字段列表 + SELECT 样例数据**，否则你看不到改动效果
2. 涉及环境变量的事故，**别浪费时间猜**——直接让 Edge Function 在入口处 `console.log(Object.keys(Deno.env.toObject()))`，几秒锁定真实变量名（见 #11、#12）

详见 [platform-basics.md](./platform-basics.md) 第七节。

---

## #11 Supabase Functions Secrets 是按 Function 级别隔离的 → 新建函数读不到老函数的密钥

**症状**：在某个老 Edge Function（如 `jsapi-pay`）里 `YUNGOUOS_PARTNER_KEY` 工作正常；秒哒新建一个 Edge Function（如 `yungouos-refund`），同样代码读这个变量却拿到 `undefined`，导致函数报"支付配置不完整"等内部错误。

**根因**：Supabase Functions 的 Secrets 默认是**按 Function 级别**配置的——给 Function A 添加的密钥并不会自动可见于 Function B（除非配在 Project-level secrets，且秒哒「密钥管理」面板里把它标为全局可见）。秒哒新建函数后没有自动复制密钥配置，自然读不到。

**修复**：到秒哒「后端服务 > 密钥管理」面板，把变量名一致的 Secret 也加到新 Function 上；或确认它是 Project-level Secret 且已对所有 Function 可见。

**预防**：
- 任何新建的 Edge Function，**先**在入口处加 `console.log("[fnname] env keys:", Object.keys(Deno.env.toObject()))` 验证读得到再写业务逻辑
- 提示词里强制要求："新建任何 Edge Function 时，必须显式声明它依赖的 Secret 名称清单，并验证读取成功后再写业务逻辑"

---

## #12 秒哒新建 Edge Function 时把环境变量名拼错 → 读出 undefined 当作"配置不完整"

**症状**：明明 Supabase 已经配好了 `YUNGOUOS_PARTNER_KEY`，老 Function 都正常，但新建的 `yungouos-refund` 死活报 `{"success":false,"error":"支付配置不完整"}`。

**根因（真实案例）**：秒哒新建函数时，凭印象把变量名写成了 `DEJIN_YUNGUOUOS_PARTNER_KEY`（多了 `DEJIN_` 前缀，且 `yungouos` 错拼成 `yungUouos` 多一个 u）。Secrets 里只有正确名字 `YUNGOUOS_PARTNER_KEY`，所以 `Deno.env.get(...)` 返回 `undefined`，函数自检失败抛"配置不完整"。

**为什么这种坑很难发现**：
- 错误文案是秒哒**自己写的**（"支付配置不完整"），不是 YunGouOS 或 Supabase 的标准报错，所以表面看不出根因
- Secrets 面板写入后只显示 `••••`，肉眼对比变量名时容易"看上去对"
- 其他老 Function 跑得正常，让你误以为密钥本身没问题

**诊断手法**（5 秒搞定）：在出问题的 Function 入口加：
```typescript
const partnerKey = Deno.env.get("YUNGOUOS_PARTNER_KEY");
console.log("[fnname] env diag:", {
  expected_var_exists: !!partnerKey,
  expected_var_length: partnerKey?.length ?? 0,
  candidate_keys: Object.keys(Deno.env.toObject())
    .filter(k => k.toLowerCase().includes("yungouos") || k.toLowerCase().includes("partner")),
});
```
看输出里 `candidate_keys` 数组里实际存在的变量名，就能立刻发现拼错。

**修复**：让秒哒**在所有需要读密钥的 Edge Function 中，统一变量名常量**（例如 `const ENV_KEY = "YUNGOUOS_PARTNER_KEY"`），并在写入新 Function 时直接复用此常量，而不是凭记忆敲一遍。

**预防**：提示词里写明"读取环境变量必须使用确切的变量名 `YUNGOUOS_PARTNER_KEY`，**禁止**添加任何前缀（如 `DEJIN_`、`PROD_`）或后缀；改完后请打印 `Object.keys(Deno.env.toObject())` 自查"。

---

## #13 多通道并存时退款被错误路由到另一个通道 → "订单不存在"

**症状**：手机端 JSAPI 通道下的订单，管理员后台触发退款时报 `Failed to load resource: 500` + `{"success":false,"error":"微信退款失败: 订单不存在"}`。请求路径形如 `/v1/wechat_refund`。

**根因**：网站同时有两条支付通道：PC 端走秒哒自带的"微信官方支付"插件、手机端走自定义的 YunGouOS JSAPI。秒哒生成退款入口时**无脑调了官方插件的 `/v1/wechat_refund`**，但订单是 YunGouOS 通道下的，微信官方账上自然没有这笔订单的记录，于是报"订单不存在"。

**修复要点**：
1. 在 `orders` 表加字段 `pay_channel` 区分通道（取值如 `wxpay_official` / `yungouos`），下单时按通道写入
2. 退款入口先查 `orders.pay_channel`，按值分流：
   ```typescript
   if (order.pay_channel === "yungouos") {
     return await invoke("yungouos-refund", {...});
   } else {
     return await invoke("wechat_refund", {...});  // 原有官方退款,一行不动
   }
   ```
3. 历史订单回填策略：有 `open_id` 字段非空 → 大概率是 yungouos；其他默认 `wxpay_official`。回填前先 SELECT 看分布

**预防**：
- 多通道并存的项目里，**任何**涉及"按订单查支付状态/退款/对账"的操作，都必须先按 `pay_channel` 分流
- 提示词里写明"现有 PC 端 Native 退款保持不变，新增 YunGouOS 退款分支"，避免秒哒重构原有逻辑
- 上线前必须两条通道各跑一遍退款测试

---

## #14 [历史兼容] 旧后端大视频上传：CORS / Edge Function 资源 / Storage 上限三层叠加

> **状态：已被 2026-07-15 更新部分取代。** 旧环境中这是反复踩坑后已在生产成功的方案；新公告已取消“应用内 50MB 文件上传上限”，但没有公布新的单请求、CORS、413、函数资源限制。本条保留历史发现和旧环境兼容方案，不再作为新项目默认架构。
>
> 新项目先按 [patterns/large-video-upload.md](./patterns/large-video-upload.md) 做 200MB 能力测试；只有当前环境仍复现下列问题时，才启用本条的兼容实现。
>
> 本条只保留发现叙事 + 根因；
> 完整实现规范见 [patterns/large-video-upload.md](./patterns/large-video-upload.md)，
> 可直接抄走的三段源码见 [references/video-chunked-upload/](../../../references/video-chunked-upload/)，
> 新环境测试与旧环境兼容提示词见 [prompt-patterns.md](./prompt-patterns.md#大文件上传先测新环境旧分片代理只兜底)。

**症状（四种死法按出现顺序）**：

1. 前端 supabase-js 直传 Storage → 浏览器 CORS 拦截
   ```
   Access to fetch at 'https://xxxx.supabase.co/storage/v1/object/...'
   from origin 'https://app-XXX.miaoda.cn' has been blocked by CORS policy
   ```
2. 改"切 5MB 分片传到 Edge Function，最后合并成完整 mp4 写回 Storage" → 合并步骤稳定报
   `WorkerRequestCancelled: request has been cancelled by supervisor`（文件越大越早死，>200MB 几乎必中）。
3. 改 TUS / 一次性大上传 → nginx `413 Request Entity Too Large`（实测 178MB 上限）。
4. 改 `ReadableStream` 流式合并写回 Storage → 仍然 413（写"合并文件"瞬间撞平台级 `storageFileSizeLimit`）。

**根因（三层叠加，缺一不可，修一层另两层照样死）**：

| 限制层 | 触发位置 | 为何把"前端直传 / 合并大文件"全堵死 |
|---|---|---|
| CORS 白名单 | 浏览器 → Storage 端点 | 秒哒预览域名 `*.miaoda.cn` 在 **Storage 端点**白名单**没有**，但在 **Edge Function 端点**白名单**有**。协议层拒绝，前端代码改不动。 |
| Edge Function 资源 | 单函数内存 / CPU / wall-time | 几百 MB 文件 concat 或流式拼装超过百兆级内存或数百秒 wall-time，被 supervisor 强制 kill。 |
| Storage 全局上限 | 平台级 `storageFileSizeLimit = Math.min(global, bucket)` | 合并后的整文件在写入瞬间被网关 413，调大桶级 limit 也没用。 |

**旧环境兼容解法**：不把分片合并成完整文件。分片以路径 `<upload_id>/<chunk_index>` 永久留在 Storage 桶 `video-chunks` 里，新增一个 `video-serve` Edge Function 用 HTTP Range / 206 Partial Content 把分片伪装成可拖进度条的完整视频文件。它绕开旧环境的 CORS、函数资源和 Storage 上限，但架构复杂、占用对象数量多，不应在新环境未经测试就直接采用。架构图 / 表结构 / 函数契约 / 源码见 [patterns/large-video-upload.md](./patterns/large-video-upload.md)。

**只有新环境测试仍失败时才使用兼容提示词**（详见 [prompt-patterns.md](./prompt-patterns.md#大文件上传先测新环境旧分片代理只兜底)）：
红线"禁止合并分片"+"禁止前端直接调 Storage 端点（含 createSignedUploadUrl / TUS）"+"video-serve 必须返回 206 + Content-Range，不允许 200 全文" + 把 `references/video-chunked-upload/` 三个 ts 作为"禁止重写、必须照抄"的参考实现塞给它（参考 #5：秒哒会无视已提供实现自己另写一份）。

---

## #15 只改 `index.html` / `useSEO` → SPA 页面级 `keywords` 容易漏

> 完整处方见 [patterns/seo-optimization.md](./patterns/seo-optimization.md)，提示词片段见 [prompt-patterns.md](./prompt-patterns.md#片段-8全站-seo-优化不漏-keywords)。

**症状**：让秒哒“做 SEO”后，它的 Summary 看起来完成了 `index.html`、`title`、`description`、`robots.txt`、`sitemap.xml` 等任务，但继续检查每个页面时发现：部分路由没有 `meta[name="keywords"]`，或页面切换后 `keywords` 没有跟着变。

**根因**：React SPA 的 `<head>` 是运行时状态，不是只看 `index.html`。秒哒第一轮容易用 `useSEO` 或手动 DOM 操作分散修改 `title` / `description`，但漏掉 `keywords`；多页面路由越多，越容易出现“首页有、Navigate / About / Feedback 没有”的不一致。

**修复**：
1. 用 `react-helmet-async` 包住应用根部。
2. 建统一 `SEOHead` 组件，组件参数必须包含 `title`、`description`、`keywords`。
3. Home / Navigate / About / Feedback 等每个路由页面都显式渲染 `<SEOHead />`。
4. Settings 增加 `site_keywords`，与 `site_description` 一起保存、加载、回显。
5. 改完后逐页检查 `document.title`、`meta[name="description"]`、`meta[name="keywords"]`。

**预防**：提示词里不要只写“帮我做 SEO”。要明确要求秒哒按“页面矩阵 × 字段矩阵”验收：每个页面都要有 `title` / `description` / `keywords`，并要求它回报逐页检查表。

---

## #16 首轮没明确后端存储 → 数据实际只存在浏览器缓存

**症状**：应用里录入的数据在当前浏览器能看到，但换浏览器、无痕模式、清缓存或换设备后数据丢失。用户以为“秒哒已经保存数据”，实际只是本地缓存。

**根因**：首轮 Query 没有明确包含“后端存储 / 生成数据库 / 创建数据表 / 云端保存”等关键词，模型会为了快速完成原型用 `localStorage`、浏览器缓存或前端状态模拟数据。

**修复**：让秒哒基于现有应用补充真实后端数据库，并迁移读写逻辑：

```text
请基于当前应用补充真实后端数据库存储功能，不允许继续使用浏览器缓存或 localStorage 作为业务数据来源。
请创建必要的数据表，补充数据的增删改查操作，并基于现有表结构生成管理员可用的数据查看维护页面。
完成后请按表回贴字段列表，并说明如何用无痕窗口验证数据持久化。
```

**预防**：首轮提示词里直接写“真实后端数据库存储 + 增删改查 + 数据查看维护页面”。验证时用无痕窗口或另一台设备复查，不要只看当前浏览器。

---

## #17 Web / 小程序 / APP 首轮形态选错 → 后期强转容易编译空产物或无法发布

**症状**：Web 应用后期想发布成微信小程序，或编辑过程中把网站改成小程序，出现编译产出为空、不能发布到小程序渠道、页面能力异常等问题。

**根因**：秒哒不同应用形态的底层技术栈不同：

| 形态 | 技术栈 |
|---|---|
| Web 应用 | React + Vite |
| 微信小程序 | React + Vite + Taro |
| APP | 原生 |

这不是发布面板里的普通渠道切换，而是生成项目时的架构选择。做好的项目不支持稳定地强转形态。

**修复**：如果已经进入强转导致的编译问题，通常建议重新生成正确形态的项目，再迁移业务逻辑和素材。不要在坏掉的项目里继续硬修发布链路。

**预防**：首轮就写清“做 Web 应用 / 做微信小程序 / 做 APP”，如果目标是微信小程序，最好直接使用秒哒界面的“做小程序”入口，并在提示词里重复“本项目是微信小程序，不是 Web 应用”。

---

## #18 小程序上传沿用 H5 文件选择逻辑 → `invalid filepath`

**症状**：图片或视频上传在 H5/Web 预览里正常，发布到微信小程序后报 `invalid filepath` 或上传失败。

**根因**：微信小程序和 H5 不是同一套运行环境。小程序不能直接照搬浏览器端 `<input type="file">` / File API 的路径逻辑，必须使用微信小程序 API 选择本地资源。

**修复**：

- 图片选择用 `wx.chooseImage`
- 视频选择用 `wx.chooseVideo`
- 上传逻辑按 Taro / 微信小程序运行环境适配，不要复用 H5 文件路径

**预防**：只要目标形态是微信小程序，提示词里要明确“文件上传必须按小程序方式实现，不要复用 H5 文件选择逻辑”。同时在真机小程序环境测试，不要只看 Web 预览。

---

## #19 短信验证码登录让秒哒自写 Edge Function → `Edge Function returned a non-2xx status code`

**症状**：短信验证码登录失败，前端报 `Edge Function returned a non-2xx status code`，但业务侧看不出具体原因。

**根因**：秒哒生成登录时可能自己写 Edge Function 包一层验证码登录逻辑，反而绕开了平台内置的 Supabase Auth 能力。登录这类基础能力越绕，越容易在验证码、会话、用户表同步上出错。

**修复**：让秒哒改回 Supabase Auth 登录：

```text
当前短信验证码登录失败，不要使用自写 Edge Function 实现登录。
请采用 Supabase Auth / 秒哒内置用户体系重新实现登录注册流程，并删除绕过 Auth 的自写登录函数。
完成后请说明前端调用的是哪个 Auth 方法，后端是否仍残留自写登录 Edge Function。
```

**预防**：登录、注册、验证码、账号密码这类基础用户体系，优先要求使用 Supabase Auth / 秒哒内置用户体系，不要让模型自由发挥写一套“看起来能跑”的认证后端。

---

## #20 同时保留微信登录和账号密码登录 → 同一个人会变成两个账户

**症状**：用户之前用微信登录，后来补充账号密码登录后，同一用户以两种方式登录看到的数据、权限或订单不一致。

**根因**：微信登录和账号密码登录在秒哒/Supabase Auth 里可能被当成两个不同身份。除非额外做账号绑定，否则“同一个现实用户”不等于“同一个系统用户”。

**修复**：先决定是否允许双登录方式并存。如果必须并存，需要设计账号绑定/合并规则，而不是只让秒哒“再加一种登录方式”。

**预防**：提示词里写明登录方式的唯一主路径。如果要从微信登录切到账号密码登录，先备份/导出用户和业务数据，再要求秒哒说明旧用户数据如何迁移或绑定。

---

## #21 微信恢复访问 txt 验证文件被 SPA fallback 吃掉 → 校验失败

> 完整处方见 [patterns/wechat-urlsec-verification.md](./patterns/wechat-urlsec-verification.md)。

**症状**：微信内置浏览器访问网站时出现“无法确认该网页的安全性，请谨慎访问”。点击“申请恢复访问”后，微信要求在网站根目录部署 txt 验证文件。秒哒 Summary 显示已在 `public/` 目录创建文件，但微信页面仍提示“校验失败，请按要求部署文件及内容”。

**根因**：文件虽然在源码或项目目录里出现了，但线上公网路径 `https://域名/<file>.txt` 并没有返回验证码纯文本，而是被 React/Vite SPA 的路由回退或平台发布层接管，返回了首页 HTML。对微信校验服务器来说，这等于文件内容不匹配。

**诊断手法**：

```bash
curl -i https://域名/<file>.txt
```

如果结果是 `Content-Type: text/html`，正文是 `<!doctype html>` 或站点首页内容，即使状态码是 `200`，也一定会校验失败。

**修复**：

1. 让验证文件作为根目录静态文件优先返回。
2. 确认 `/<file>.txt` 不经过 React Router、SPA fallback、`index.html` 或业务页面渲染。
3. 如果平台静态发布层做不到，就用 Nginx/CDN/边缘规则单独为 `/<file>.txt` 返回纯文本。
4. 用公网 `curl -i` 确认状态码、Content-Type、响应正文都正确后，再回微信页面点击“已部署，开始验证”。

**当前边界（2026-06-23 复测）**：

- 秒哒构建后的 BOS/CDN 源文件已经正确返回 `text/plain`，内容也匹配微信验证码，说明源码和构建产物不是问题。
- 正式绑定域名 `moumou.shiyichuang.com` 下的同名 txt 路径仍返回首页 HTML，说明问题在秒哒域名服务层/发布层的 SPA fallback。
- 秒哒尝试在 `index.html` 中用前端 JS 判断路径并 `document.write` 验证码，但微信校验服务器不会执行浏览器 JS，所以这种修法无效。
- 在继续使用当前秒哒绑定域名链路的前提下，秒哒应用代码层暂时无法独立解决；需要秒哒官方/平台人员在服务端路由层排除该 txt 路径，或走微信“仅提交证明材料”的人工兜底。

**预防**：任何“站长验证 txt 文件”类任务，都不要以“项目里创建了文件”为验收标准；必须以公网 URL 的实际响应为准。

---

## #22 手机号未做唯一身份规范化 → `+86` 与裸号变成两个账户 / 登录失败

> **风险等级：最高危。** 来源：建委 2026-07-16 提供的真实秒哒应用问题。完整可执行提示词见 [prompt-patterns.md](./prompt-patterns.md#手机号注册登录先规范化再查用户)。

**症状**：

1. 用户用 `13xxxxxxxxx` 注册后，再用 `+8613xxxxxxxxx` 登录，系统把两种写法当成不同身份；重复注册会产生两个账户。
2. 手机号登录时，`getUserByPhone` RPC 因网络抖动等异常进入 catch 块，兜底代码用原始 `input` 拼 Auth email。输入含 `+86` 时，email 与注册时的规范化手机号映射不一致，最终误报“密码错误”。
3. 旧用户兼容分支调用 `getUserByUsername(input)`，并用原始 `input` 拼 email；`+86` 输入同样无法命中原账户。
4. 注册成功但 Supabase 未返回 session 时，只提示“请手动登录”，却清空表单且不切换登录 Tab，用户不知道应输入什么。

**根因**：手机号在注册、主登录、RPC 异常兜底、旧用户兼容和注册后 UI 这五条路径中被重复处理。部分分支使用原始输入，部分分支使用去掉 `+86` 的号码，且 email 映射公式没有收口为一个函数。

**修复**：

1. 在 `Login.tsx` 入口只做一次手机号规范化：当前中国手机号场景中，把前后空格、连接符清理掉；若以 `+86` 开头则去掉此前缀，最终只接受 11 位 `1` 开头的手机号。后续逻辑只使用 `normalizedInput`。
2. 把“规范化手机号 → Auth email”的规则提取为唯一 helper。注册、正常登录、catch 兜底和旧用户兼容路径都调用它，**禁止**各分支手写 `${input}@miaoda.com` 或其他拼接。
3. 主路径的 `getUserByPhone`、旧用户路径的 `getUserByUsername` 都必须传 `normalizedInput`；catch 块和旧用户登录都必须用 `toPhoneAuthEmail(normalizedInput)`。
4. 注册成功但 session 为 `null` 时，自动切换到登录 Tab，并把 `normalizedInput` 预填到现有“用户名/手机号”字段；只让用户补输密码。
5. 注册前按规范化手机号检查既有账户，避免 `+86` 与裸号再次创建两条身份记录。已经存在的重复账户不要在同一修复中自动合并，必须先核验用户身份、业务数据和 Auth 记录后单独迁移。

**投产前必核**：本次问题描述中同时出现 `phone_<手机号>@miaoda.com` 与 `<手机号>@miaoda.com` 两种示例。修改前必须检查当前注册分支和真实已注册用户使用的 email 公式；helper 必须复用已生效的公式，不能为了“统一”而改写旧用户 email。

**预防**：

- 手机号是身份键，不是展示字符串；数据库、RPC、Auth email 和表单预填都以同一份规范化值为准。
- 所有登录分支共用同一组 helper，例如 `normalizeChinaPhone(raw)` 与 `toPhoneAuthEmail(normalizedPhone)`；代码审查时搜索 `input`、`@miaoda.com`、`getUserByPhone`、`getUserByUsername`，逐一确认没有绕过 helper。
- 回归测试至少覆盖：裸号注册后用 `+86` 登录、`+86` 注册后用裸号登录、RPC 抛异常后的 catch 兜底、旧用户兼容路径、session 为 `null` 的注册完成页，以及重复注册拦截。
