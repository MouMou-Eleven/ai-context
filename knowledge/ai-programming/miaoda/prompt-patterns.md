# 秒哒 AI 提示词模板

> 与秒哒 AI 协作时，提示词的写法直接决定它会不会按你的意图执行。这里沉淀经过实战验证的提示词结构和典型片段，可直接复用。

## 核心结构（按这个顺序写）

```
1. @<技能名>（如果涉及技能调用，必须在最前面 @）
2. 一句话场景陈述 + 调动注意力的措辞
3. 红线段（禁止什么、不要动什么）—— 越靠前越好
4. 具体目标
5. 关键算法/函数的代码片段（不让 AI 自己写）
6. 必须使用的 URL / 文件 / 环境变量清单
7. 强制使用的参考实现（防止 AI 自己另写）
```

## 通用模板

```
@<技能名> 我现在需要 <做什么>，请打起十二分的精神专心进行修改和执行任务！！

<现状陈述：哪些已经稳定运行、本次任务的边界>，请保持不变，不要动 X 的任何代码、配置或环境变量。
本次只 <做什么的边界>。

整体目标：<一句话目标>。

<具体的实现指引，包含必要的代码片段>

<禁止清单>：
- ❌ 不要 ...
- ❌ 不要 ...
- ✅ 必须 ...

<URL / 文件 / 环境变量清单>
```

## 经过实战验证的典型片段

### 片段 1：设备识别（让秒哒原样实现，不要自由发挥）

```javascript
function getPayMethod() {
  const ua = navigator.userAgent || "";
  const isWeChat = /MicroMessenger/i.test(ua);
  const isMobile = /Mobile|Android|iPhone|iPad|iPod/i.test(ua);
  if (isWeChat && isMobile) return "jsapi";
  return "native";
}
```

适用场景：要让秒哒在多种条件下做不同分支时，给一段确定函数比口头描述要稳得多。

### 片段 2：强制使用技能而非自己写

```
所有 X 接口调用必须通过 @<技能名> 这个技能内的脚本完成：
- scripts/foo.py 做 A
- scripts/bar.py 做 B
禁止在 Edge Function 或前端代码里自行实现签名 / MD5 / 加密相关逻辑。
之前你这么做过，结果有 bug，已经验证翻车。
```

适用场景：秒哒 AI 有强烈"自己实现一遍"倾向，必须明确禁止+说明原因。

### 片段 3：强制使用参考实现而非另写

```
异步通知接收端请直接使用技能包内的 references/edge_function_notify.ts，
原样部署到 supabase/functions/wxpay-notify/index.ts，**不要重写**。
该文件已经包含 X / Y / Z 功能，并已在测试环境验证。
```

适用场景：技能包里附带了完整可用代码，但秒哒倾向"重新生成一份"。

### 片段 4：保护现有功能不被破坏

```
当前 PC 端用的是 X 接口，已经稳定运行，本次任务保持不变，
不要动 PC 端任何代码、配置或环境变量。
JSAPI 路径与 Native 路径必须能并存互不影响。
```

适用场景：新增功能但不能破坏旧功能。秒哒 AI 容易"顺手重构"。

### 片段 5：禁止 MD5 + Web Crypto 死路

```
禁止调用 crypto.subtle.digest("MD5", ...)，
Deno/浏览器 Web Crypto 拒绝 MD5，必抛 NotSupportedError，
之前你这么做翻车过。
如需 MD5，使用 references/edge_function_notify.ts 里的纯 JS MD5 实现，
或调用技能内的 Python 脚本（用 hashlib.md5）。
```

适用场景：任何涉及微信支付、YunGouOS 等需要 MD5 签名的场景。

### 片段 6：保护密钥

```
<密钥名> 严禁出现在任何源码、配置文件、前端、注释、日志里。
它只通过 <某面板> 的环境变量 X 注入。
如果你的代码里需要密钥，正确做法是调用技能脚本而不是自己读密钥。
```

### 片段 7：手机端调试用「管理员可见的控制台日志按钮」

**背景**：电脑端可以按 F12 看 Console 报错日志，手机端没有这个能力。让秒哒在 UI 里加一个仅管理员可见的"日志按钮"，点击后把报错/日志展示出来供复制，可以让手机端联调效率几倍提升。

**适用场景**：手机端联调（支付、登录、地理定位、相机权限等任何只能在真机上复现的功能），尤其是用户访问真实网站后报错、但你又看不到设备控制台时。

**提示词**：

```
并且因为手机端不能像网页端一样去查看控制台的报错日志，
那我就需要你在手机端给我额外加一个控制台报错日志的按钮。
比如说我点击提交订单之后，他会把对应的报错信息给我打印出来，
然后我可以直接复制。这个按钮只有管理员才能看到，普通用户是看不到的。
可以辅助精准定位错误。
```

**对应实现要点**（写到提示词里更稳）：
- 在前端用一个全局 logger（数组缓冲）拦截 `console.error` / `console.warn` / 关键业务日志
- UI 上增加一个浮窗/抽屉按钮，点击展开日志列表
- 用户身份判断：从应用的用户体系读 `is_admin` 字段（或 email 在白名单内）才显示按钮
- 每条日志展示时间戳 + 级别 + 内容；提供"一键复制全部"按钮（用 `navigator.clipboard.writeText`）
- 调试期开启，上线前确认普通用户看不到

**进阶版**：把日志同时写入数据库一张 `client_logs` 表（按 `user_id` + `session_id` + `created_at` 索引），管理员后台可按用户查询历史，更适合非现场远程支持。

### 片段 8：全站 SEO 优化不漏 keywords

**背景**：一次真实对话里，第一轮让秒哒“做 SEO”后，它完成了 `index.html`、`useSEO`、`robots.txt`、`sitemap.xml` 和 Settings 的部分改动；第二轮继续追问每个页面的 `keywords` 是否都补齐，才改成 `SEOHead` + `react-helmet-async` 的统一管理方式。经验是：SEO 必须按“页面矩阵 × 字段矩阵”验收。

**适用场景**：秒哒生成的 React/Vite 网站需要补全站 SEO，尤其是有 Home / Navigate / About / Feedback 这类多页面路由时。

**提示词**：

```text
我现在需要你对整个网站做一次完整 SEO 优化，请打起十二分的精神专心执行。

红线（必须遵守）：
- 不要只改 index.html，React 页面切换后的 head 也必须正确。
- 不要只处理 title 和 description，keywords 必须每个页面都有。
- 不要在每个页面散落重复 DOM 操作，必须用统一 SEOHead 组件或等价统一入口管理。
- 不要破坏现有路由、数据加载、分类筛选、反馈提交、后台设置保存逻辑。

目标：
1. 安装并使用 react-helmet-async（如果项目已安装则复用）。
2. 在应用根部增加 HelmetProvider。
3. 新建 src/components/SEOHead.tsx，统一输出 title、description、keywords。
4. index.html 中补齐站点级兜底 title、description、keywords。
5. Home、Navigate、About、Feedback 每个页面都必须渲染 SEOHead。
6. Settings 中新增 site_keywords 配置项，和已有 site_description 一起保存、加载、回显。
7. Home 页 SEO 要能结合 site_keywords、当前分类名 selectedCategoryName、站点数据关键词生成。
8. 检查 robots.txt 和 sitemap.xml；没有就创建，有就补全核心路径。

验收要求：
改完后请逐页检查并回报表格，列出每个页面实际生效的 title、description、keywords。
尤其检查 meta[name="keywords"]，不能为空，不能只在首页存在。
```

完整处方见 [patterns/seo-optimization.md](./patterns/seo-optimization.md)。

## 不要做的事

- ❌ 不要写"先告诉我你将怎么做，等我确认再动手"——秒哒是指令式执行，会忽略这段或生成多余说明文档浪费 token
- ❌ 不要分多轮交互——它没记忆和讨论能力，每次都当首次看
- ❌ 不要用"看情况"、"建议"、"考虑"等含糊措辞——它会自己发挥
- ❌ 不要让它"参考某文档自己实现"——它会按理解重新写，必然走样
- ❌ 不要把红线放在文末——它可能"边读边改"，红线放最前才有约束力

## 应该做的事

- ✅ 关键代码段直接贴出来让它原样使用
- ✅ 强约束（禁止 / 必须）写在提示词最前
- ✅ 用具体文件路径指向参考实现，而不是描述"实现一个 X"
- ✅ 在结尾给出可验证的测试场景（用 0.01 元跑一笔、看到 paid 状态等）

## 反面教材：失败的提示词

```
❌ 帮我加上手机端支付，最好兼容微信
❌ 把支付改一下，让它在手机上能用
❌ 接入一个支付插件
```

为什么失败：没有 @ 技能、没有红线、没有约束 AI 行为、没有指明分工。秒哒会自己理解、自己重写，几乎必然踩坑。

## 正面教材：完整接入提示词

见 [case-yungouos-jsapi.md](./case-yungouos-jsapi.md) 的"最终可用提示词"小节。

## 视频上传分片不合并 + HTTP Range 代理

**背景**：秒哒预览域名 `*.miaoda.cn` 下上传 ≥50MB 大视频会同时撞三层墙——CORS（Storage 端点白名单不包括 miaoda.cn）、Edge Function 资源（合并大文件超内存/wall-time 被 supervisor kill）、Storage 全局上限（合并文件写入瞬间 413）。完整复盘见 [pitfalls.md #14](./pitfalls.md)，处方见 [patterns/large-video-upload.md](./patterns/large-video-upload.md)，源码见 [references/video-chunked-upload/](../../../references/video-chunked-upload/)。

**核心：永远不让秒哒重新设计。它会原地另写一份合并版，必然再撞同一面墙。**

**提示词模板**：

```
@<秒哒后端技能> 我现在需要给后台加大视频上传。请打起十二分的精神专心执行！！

红线（必须严格遵守，违反必死）：
- ❌ 禁止前端通过 supabase-js 直接调 Storage 端点（含 createSignedUploadUrl / TUS / upload）——
  秒哒预览域名 *.miaoda.cn 不在 Storage 端点 CORS 白名单内，浏览器会直接拦
- ❌ 禁止把分片在 Edge Function 里合并成完整 mp4 写回 Storage——
  上传合并文件瞬间会被平台 storageFileSizeLimit 在 413 层堵死（已实测，TUS / ReadableStream 流式合并都没用）
- ❌ 禁止重写下述三个函数的逻辑或常量——参考实现已在生产验证
- ✅ 必须用三函数架构：video-upload-chunk（5MB 一片）+ video-upload-complete（验全 + 标完成）+ video-serve（Range 流式代理）
- ✅ 视频 URL 必须指向 video-serve 函数地址，不允许是 Storage 公开 URL
- ✅ video-serve 必须返回 206 + Content-Range + Accept-Ranges: bytes，禁止 200 全文返回

参考实现（必须照抄、不允许另写）：
- references/video-chunked-upload/video-upload-chunk.ts
- references/video-chunked-upload/video-upload-complete.ts
- references/video-chunked-upload/video-serve.ts
直接原样部署到 supabase/functions/video-upload-chunk、video-upload-complete、video-serve。

不可变常量（前后端必须同步）：
- 分片大小 = 5 * 1024 * 1024（前端 + video-serve.ts L21）
- 桶名 = video-chunks（三个函数硬编码）
- 路径格式 = <upload_id>/<chunk_index>（三个函数硬编码）

表 schema 见 references/video-chunked-upload/README.md。
前端切片循环、断点续传 UI、video_uploads 行的创建端点需要你自己实现（这三个函数不管）。

测试场景：上传一个 200MB 的 mp4，complete 返回的 public_url 在 <video> 标签里能正常拖进度条。
```

**为什么必须把"禁止合并"放红线**：秒哒看到"分片不合并"会本能反应"那最后怎么播？"，然后自动加上"合并步骤"。提示词不写禁止 → 它一定加，加完一定撞 413，然后回滚改方案，浪费一晚上。

**为什么必须把 references 路径塞进提示词**：参考 [片段 3](#片段-3强制使用参考实现而非另写)，秒哒会无视已提供实现自己另写一份。把三个 ts 路径作为"必须照抄"的源码喂给它是唯一能让它停下来的方式。

**反面教材**：

```
❌ 帮我加大视频上传功能，最好支持断点续传
❌ 用 Supabase Storage 实现 mp4 上传
❌ 切片上传完后合并成完整视频写回 Storage
```

为什么失败：没有禁止合并、没有指明 video-serve 架构、没有引用已有实现。秒哒会按 Supabase 官方教程做"切片→合并→直传"，三层墙各撞一遍。
