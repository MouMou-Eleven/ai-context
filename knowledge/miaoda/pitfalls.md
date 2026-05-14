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