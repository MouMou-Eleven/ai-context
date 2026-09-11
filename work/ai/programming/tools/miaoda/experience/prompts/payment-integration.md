# 支付集成与既有实现复用

> 来源：从原 [prompt-patterns.md](../prompt-patterns.md) 的实战模板按主题整理，原始版本由Git历史保留；2026-09-12仅拆分与明确适用边界，未重新实测秒哒产品能力。
> 模板中的页面名、接口、路径和配置是对应案例条件；执行前替换为当前项目已核验事实。查看模板不代表已授权收费、部署或外部发送。

> 仅适用于已采用对应支付技能、回调和运行时的项目。`getPayMethod`是该案例设备分支，不是所有支付平台的通用协议。密钥读取、签名与部署方式以当前集成合同为准。

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

适用场景：已有案例出现过重写已验证实现的情况，应明确复用路径和原因。

### 片段 3：强制使用参考实现而非另写

```
异步通知接收端请直接使用技能包内的 references/edge_function_notify.ts，
原样部署到 supabase/functions/wxpay-notify/index.ts，**不要重写**。
该文件已经包含 X / Y / Z 功能，并已在测试环境验证。
```

适用场景：技能包里附带了完整可用代码，但秒哒倾向"重新生成一份"。

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

## 反面教材：失败的提示词

```
❌ 帮我加上手机端支付，最好兼容微信
❌ 把支付改一下，让它在手机上能用
❌ 接入一个支付插件
```

为什么失败：没有 @ 技能、没有红线、没有约束 AI 行为、没有指明分工。这类提示缺少可核验边界，案例中曾导致实现偏差。

## 正面教材：完整接入提示词

见 [case-yungouos-jsapi.md](../cases/yungouos-jsapi.md) 的“最终可用提示词”小节。
