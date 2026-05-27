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

## #14 秒哒预览域名 *.miaoda.cn 下大视频上传：CORS 把前端直传堵死、Edge Function 又装不下整文件 → 正解是「分片留在 Storage 不合并 + serve 函数用 HTTP Range 流式代理」

> 本条经验是反复踩坑后**已在生产成功**的方案，三个函数源码已沉淀到 `references/video-chunked-upload/` 三个文件，可直接复用。

**症状（按出现顺序）**：

1. 前端代码用 supabase-js 直传 Storage：浏览器控制台直接 CORS 拦截
   ```
   Access to fetch at 'https://xxxx.supabase.co/storage/v1/object/...'
   from origin 'https://app-XXX.miaoda.cn' has been blocked by CORS policy
   ```

2. 改成"前端切 5MB 分片传到 Edge Function `video-upload-chunk`，最后调 `video-upload-complete` 把分片合并成一个完整 mp4 写回 Storage"：分片传输全成功，但合并步骤稳定报
   ```
   WorkerRequestCancelled: request has been cancelled by supervisor
   ```
   （文件越大越早死，>200MB 几乎必中）

3. 改用 TUS / 一次性大请求绕过分片：到达边缘网关被 nginx 截断 `413 Request Entity Too Large`（实测 178MB 上限）。

4. 即使在 `video-upload-complete` 里改用 `ReadableStream` 流式合并写回 Storage：仍然失败——平台全局 `storageFileSizeLimit = Math.min(global, bucket)` 远小于实际视频体积，写"合并文件"时还是触发 413（这条来自成功代码注释里的明确说明）。

**根因（三层叠加，缺一不可）**：

- **CORS 层**：秒哒预览域名 `*.miaoda.cn` 在底层 Supabase **Storage 端点**的 CORS 白名单里**没有**，但在 **Edge Function 端点**的 CORS 白名单里**有**。所以"前端 → Storage"被浏览器协议层拒绝，"前端 → Edge Function"通行。这是协议层的拒绝，前端代码改不动。
- **Edge Function 资源层**：单个 Edge Function 的内存/CPU 都很有限（百兆级内存、数百秒 wall-time，被 supervisor 强制 kill）。把几百 MB 的分片在函数里 concat / 流式拼一份完整文件再写回 Storage，**几乎必然**触发 `WorkerRequestCancelled`。
- **Storage 全局上限层**：平台层有 `storageFileSizeLimit = Math.min(global, bucket)` 的硬上限，并发桶级 limit 调大也没用——合并后的整文件在写入瞬间被网关 413 拒掉。

> 进一步：上述任意单层即便修掉，剩下两层也会让"前端直传 / 合并大文件" 100% 死。所以从单点优化里逃不出来。

**正解（已在生产成功、用户已验证、三段源码完整保存在 [references/video-chunked-upload/](../../../references/video-chunked-upload/) 目录）**：永远别把分片合并成一个大文件。让分片留在 Storage 里，靠一个 serve 代理函数用 HTTP Range/206 假装它是一个完整视频。

架构上需要 **3 个 Edge Function + 1 个 bucket + 1 张元数据表**：

```
bucket:  video-chunks               # 只放分片,不放合并后的完整文件
                                    # 每个分片以路径 `<upload_id>/<chunk_index>` 存放

table:   video_uploads              # 元数据表,字段(实测验证):
                                    #   id (uuid, PK)         — 即 upload_id
                                    #   user_id (uuid)        — 上传者
                                    #   filename (text)
                                    #   total_size (int8)     — 全文件总字节数
                                    #   mime_type (text)
                                    #   chunk_count (int)     — 总分片数
                                    #   uploaded_chunks (int) — 已上传分片数
                                    #   status (text)         — uploading / completed
                                    #   storage_path (text)
                                    #   created_at, completed_at (timestamptz)

Edge Functions (顶层 CORS 头都带 Access-Control-Allow-Origin: *):

  video-upload-chunk     # POST multipart/form-data: { upload_id, chunk_index, chunk(File) }
                         # 鉴权: Authorization Bearer + 管理员角色校验 (profiles.role === 'admin' || is_super_admin)
                         # 单分片硬上限 5MB + 128KB 容差(常量 CHUNK_MAX_BYTES)
                         # 落盘路径: video-chunks/<upload_id>/<chunk_index>
                         # upsert: true 允许重传同一片
                         # 写完递增 video_uploads.uploaded_chunks
                         #   - 走 Edge Function 端点,CORS 通过
                         #   - 单分片 ≈ 5MB,远低于 nginx 178MB / Edge Function 内存上限
                         #   - 前端可多路并发提速

  video-upload-complete  # POST JSON: { upload_id }
                         # 鉴权同上
                         # 关键:**只校验 + 改状态,不读分片内容、不做任何合并**
                         #   1. storage.list(upload_id) 拿到已落盘分片列表
                         #   2. 校验 0..chunk_count-1 全部到位,缺片返回 missing_chunks 数组
                         #   3. UPDATE video_uploads SET status='completed', completed_at=now()
                         #   4. 返回 { public_url, file_path }, public_url 形如:
                         #      `${SUPABASE_URL}/functions/v1/video-serve?id=${upload_id}`
                         # 幂等: 已 completed 直接返回同一 serve URL

  video-serve            # GET /functions/v1/video-serve?id=<upload_id>
                         # **不鉴权**:upload_id 是 UUID 不可猜,且视频是课程公开内容
                         # 浏览器 <video> 标签发起请求,带 `Range: bytes=START-END` 头
                         # 流程:
                         #   1. 查 video_uploads 拿 total_size / chunk_count / mime_type / status
                         #   2. 解析 Range,算出 firstChunkIdx / lastChunkIdx / 首片要跳过的字节数
                         #         firstChunkIdx    = floor(rangeStart / CHUNK_SIZE)
                         #         lastChunkIdx     = min(floor(rangeEnd / CHUNK_SIZE), chunk_count-1)
                         #         skipBytesInFirst = rangeStart - firstChunkIdx * CHUNK_SIZE
                         #   3. 对覆盖到的每个分片调 storage.from('video-chunks').createSignedUrl(`${id}/${i}`, 3600)
                         #   4. 用 ReadableStream 逐分片 fetch → 切片 → enqueue,边读边推
                         #   5. 命中 Range 时返回 `206 Partial Content` + Content-Range,
                         #      未带 Range 返回 200,响应头始终带 `Accept-Ranges: bytes`
                         # 浏览器看到 206 + Content-Range 就当成一个完整可拖动进度条的视频文件。
```

**为什么这套方案三层都能过**：

| 限制层 | 失败方案为何死 | 本方案为何活 |
|---|---|---|
| Storage CORS 白名单不含 `*.miaoda.cn` | 前端直传被浏览器拦 | 前端**永远不直接打 Storage 端点**,全程只与 Edge Function 通信 |
| Edge Function 内存/CPU/wall-time | 合并大文件被 supervisor kill | 上传时每次只处理一个 ~5MB 分片;播放时 video-serve 一次也只代理 Range 命中的几个分片,且边 fetch 边 enqueue 不积压在内存里 |
| Storage 全局 `storageFileSizeLimit` + nginx 178MB | 一次性大请求 / 合并写回都被 413 | 单次写入 Storage 的对象始终是 5MB 分片,永不接近上限;**永不写入合并后的完整文件** |

**前端配合的关键参数**（必须与 Edge Function 一致，否则 Range 算错）：

- 前端切片大小 `CHUNK_SIZE` **必须 = 5 \* 1024 \* 1024**（5 MB），与 `video-serve` 顶部常量保持一致
- 前端可 3 路并发上传分片以提速（不是必需，但实测能显著缩短大视频上传耗时）
- 上传完调一次 `video-upload-complete` 拿 `public_url`，写入业务表（如 `course_videos.video_url`）
- 业务页面播放：`<video src="{public_url}" controls />` 即可，浏览器自动协商 Range

**反模式（实测都不行，别再走弯路）**：

- ❌ 让秒哒"申请 Storage 签名直传 URL"——签名 URL 仍然指向 Storage 端点，CORS 照样拦。
- ❌ 把分片在 `video-upload-complete` 里 in-memory `concat` 后 `upload`——内存爆，`WorkerRequestCancelled`。
- ❌ 改成 `ReadableStream` 流式合并写回 Storage——单函数 wall-time/CPU 不够，且写"合并文件"还撞 `storageFileSizeLimit` 413。
- ❌ 走 TUS 协议 / multipart 一次性大上传——nginx 178MB 卡死。
- ❌ 在前端用 IndexedDB 暂存再合并——浏览器内存与持久化都顶不住几百 MB 视频，且最后还是要面对 CORS。
- ❌ 把 `video-serve` 写成 200 全文返回——浏览器 `<video>` 拖进度条/移动端会卡死，且 Edge Function wall-time 不够推完整文件。

**预防 / 写提示词时怎么落**（建议复制进 [prompt-patterns.md](./prompt-patterns.md)）：

1. 红线段第一条：**禁止合并分片为完整文件**、**禁止前端代码直接调用 Storage 端点（含 createSignedUploadUrl/直传/TUS）**。
2. 强制要求秒哒落 3 个函数：`video-upload-chunk` / `video-upload-complete` / `video-serve`，并把 `video-serve` 必须实现 `Range` / `206` 这条单独列出来——很多 AI 默认写 200 全文返回，那样浏览器没法拖进度条、移动端也加载不动。
3. 前端 `<video>` 标签的 `src` 必须指向 `video-serve` 这个 Edge Function 路径，**不要**指向 Storage 公网 URL。
4. `video_uploads` 表至少要有：`id` / `user_id` / `total_size` / `mime_type` / `chunk_count` / `uploaded_chunks` / `status` / `storage_path` / `created_at` / `completed_at`，否则 `video-serve` 算不出 Range 该读哪几片的哪几个字节。
5. 直接把 [references/video-chunked-upload/](../../../references/video-chunked-upload/) 三个 ts 文件作为「禁止重写、必须照抄」的参考实现喂给秒哒，杜绝它"按印象自己写一遍"翻车（参考 #5：秒哒会无视已提供实现自己另写一份）。
