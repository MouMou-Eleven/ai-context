# 案例：YunGouOS 微信 JSAPI 支付接入

> 真实项目：德锦周锦官网（dejinzhoujin.com）支付接入。从需求提出到测试网站打通的完整复盘，包含每一轮失败的原因和提示词演进。

## 一、项目背景

- 网站搭在秒哒平台
- PC 端原本通过微信官方 Native 扫码支付（稳定运行）
- 需新增手机端能力：用户在微信内打开网页应能调起微信键盘付款
- 支付通道方：YunGouOS（商户号 `1112530699`）

## 二、最终架构

```
┌─────────────────────────────────────────────────────────────┐
│  用户浏览器                                                   │
│  ├─ PC 端 / 手机非微信端 ──▶ Native 扫码（原有，不动）        │
│  └─ 手机微信内 ──────────▶ JSAPI 流程                       │
│                              │                              │
└──────────────────────────────┼──────────────────────────────┘
                               ▼
       ┌─────────────────────────────────────────────┐
       │  秒哒应用层（Deno + Supabase Edge Function）  │
       │  - 用 getPayMethod() 决定走哪条路             │
       │  - JSAPI 路径调用 @dejin-wxpay-jsapi 技能     │
       └────────────────────┬────────────────────────┘
                            ▼
       ┌─────────────────────────────────────────────┐
       │  自定义技能 dejin-wxpay-jsapi (.zip 包)        │
       │  Python 脚本: get_oauth_url / get_oauth_info │
       │             create_jsapi_order               │
       │             refund_order / get_refund_result │
       │  环境变量: YUNGOUOS_PARTNER_KEY 注入          │
       └────────────────────┬────────────────────────┘
                            ▼
       ┌─────────────────────────────────────────────┐
       │  YunGouOS api.pay.yungouos.com / api.wx...   │
       └─────────────────────────────────────────────┘

异步通知（独立路径）:
  YunGouOS ──POST──▶ https://dejinzhoujin.com/api/wxpay/notify
                     由 supabase/functions/wxpay-notify/index.ts 接收
                     验签 → 校验金额 → 幂等更新订单 → 返回 SUCCESS
```

## 三、踩坑历程（按时间顺序）

### 失败 #1：秒哒官方"插件创建"功能生成的包不能用

让秒哒直接基于 YunGouOS 文档自动生成技能包，得到的产物：
- `.skills/yungouos-jsapi-payment/SKILL.md`（嵌套两层）
- `partnerKey` 明文出现在 6 个文件里
- Edge Function 用 `crypto.subtle.digest("MD5", ...)` → 必然抛 NotSupportedError
- 强绑定 Supabase 架构

**教训**：不要让秒哒"自动生成"涉及密钥/签名的复杂技能包，自己构建。

### 失败 #2：我们自己构建的初版包上传被拒

第一版 .zip 严格按官方文档"SKILL.md（必需）+ scripts/ + references/ + assets/"结构。上传报错：
```
ZIP 包中未找到 SKILL.md
SKILL.md 格式校验失败：SKILL.md 的内容必须以 "---" 开头
```

**根因**：官方文档没说 SKILL.md 需要 YAML frontmatter，但实际校验要求 `name` / `description` / `license`。

**修复**：在 SKILL.md 最前面加 YAML frontmatter。

### 失败 #3：技能上传成功，但秒哒 AI 没用它

秒哒 AI 看了 SKILL.md 后没调技能脚本，而是**自己另写了 3 个 Edge Function**（`yungouos_get_oauth_url` / `yungouos_get_openid` / `yungouos_jsapi_pay`），并在每个里面实现一份 JS MD5。结果：
- 报"签名错误，请检查签名"
- 自己实现的 MD5 有 padding bug + 用了 Web Crypto

**修复**：在提示词里明确"禁止重写、必须调技能脚本"。

### 失败 #4：环境变量没配 / 名字不对

签名错误的另一可能根因：技能层环境变量 `YUNGOUOS_PARTNER_KEY` 没填，或填错（多空格、漏字符、大小写不对）。秒哒 AI 自写 Edge Function 时还可能读了另一个变量名（如 `INTEGRATIONS_API_KEY`）。

**修复**：
1. 在「技能 > 环境变量」面板删除后重新粘贴（确保 32 位、全大写、无空格）
2. 同时检查 Supabase Functions Secrets 是否也配了同名变量

### 失败 #5：YunGouOS 支付授权目录未配

签名问题解决后，调起微信键盘时弹"当前页面的 URL 未注册"。

**根因**：YunGouOS 商户后台「支付目录」配的是 `dejinzhoujin.com/orders/`，但测试网站实际访问的是 `app-bd0ygtaa9zwh.appmiaoda.com/payment/...`。

**修复**：在 YunGouOS 商户后台增加 `https://app-bd0ygtaa9zwh.appmiaoda.com/payment/`（末尾 `/` 必填），等 1-2 分钟生效。

## 四、最终可用提示词（在德锦周锦官网使用）

```
@dejin-wxpay-jsapi 我现在需要调整网站的支付方式，请打起十二分的精神专心进行修改和执行任务！！

当前 PC 端用的是微信官方 Native 扫码支付，已经稳定运行了，本次任务保持不变，
不要动 PC 端任何代码、配置或环境变量。本次只新增手机端的 JSAPI 支付能力，
使用我已经 @ 的这个技能 dejin-wxpay-jsapi 完成接入。

整体目标是：用户进入支付页时自动判断设备类型——PC 走原有 Native 扫码不变；
手机微信内走 JSAPI（用这个技能）；手机微信外（普通浏览器）退回 Native 扫码。

设备识别用 User-Agent 检测，请实现一个共享函数 getPayMethod()：
检测 navigator.userAgent，如果同时包含 MicroMessenger 和 Mobile|Android|iPhone|iPad|iPod
就返回 "jsapi"，其他所有情况返回 "native"。两条路径必须能并存互不影响。

手机端 JSAPI 流程必须全部通过 @dejin-wxpay-jsapi 完成，
禁止自己实现 YunGouOS 签名、禁止自己写 MD5、
禁止调用 crypto.subtle.digest("MD5", ...)（Deno 不支持 MD5 会抛 NotSupportedError，
之前你这么做翻车过）。所有 YunGouOS 接口都调技能内的脚本：
拿授权链接调 get_oauth_url、用 code 换 openId 调 get_oauth_info、
JSAPI 下单调 create_jsapi_order、发起退款调 refund_order、查询退款调 get_refund_result。
partnerKey 由秒哒平台从环境变量 YUNGOUOS_PARTNER_KEY 安全注入，
应用层不接触密钥，不要写进任何代码/配置/日志/注释。

JSAPI 异步通知接收端请直接使用技能包内的 references/edge_function_notify.ts
原样部署到 supabase/functions/wxpay-notify/index.ts，不要重写。
该文件已实现不依赖 Web Crypto 的纯 JS MD5、签名验证、商户号校验、
金额一致性校验、幂等更新，文件底部注释里附了 orders 和 refunds 两张表的建表 SQL
请直接执行。Supabase Functions Secrets 配置 YUNGOUOS_PARTNER_KEY、
SUPABASE_URL、SUPABASE_SERVICE_ROLE_KEY 三个变量。
PC 端 Native 的异步通知保持不变，不要合并不要重命名。

JSAPI 流程要用到的 URL：
- 主域名 https://dejinzhoujin.com
- OAuth 授权回跳 https://dejinzhoujin.com/oauth/wx-callback
- JSAPI 异步通知 notify_url https://dejinzhoujin.com/api/wxpay/notify
- JSAPI 同步跳转 return_url https://dejinzhoujin.com/pay/return
- 退款异步通知 https://dejinzhoujin.com/api/wxpay/refund-notify

前端调起微信键盘必须使用 references/frontend_jsapi_invoke.html 里的
WeixinJSBridge.invoke("getBrandWCPayRequest", ...) 模式，监听 WeixinJSBridgeReady 事件。
```

## 五、YunGouOS 5 个接口的字段速查

签名规则：**仅必传参数参与签名**，可选参数即使有值也不进签名。

| 脚本 | 接口 | 方法 | 必传（签名） | 可选（不签名） |
|---|---|---|---|---|
| `get_oauth_url.py` | `api.wx.yungouos.com/api/wx/getOauthUrl` | POST | `mch_id`, `callback_url` | `type`, `params` |
| `get_oauth_info.py` | `api.wx.yungouos.com/api/wx/getOauthInfo` | GET | `mch_id`, `code` | — |
| `create_jsapi_order.py` | `api.pay.yungouos.com/api/pay/wxpay/jsapi` | POST | `out_trade_no`, `total_fee`, `mch_id`, `body`, `openId` | `app_id`, `attach`, `notify_url`, `return_url`, `auto`, `auto_node`, `config_no`, `biz_params` |
| `refund_order.py` | `api.pay.yungouos.com/api/pay/wxpay/refundOrder` | POST | `out_trade_no`, `mch_id`, `money` | `out_trade_refund_no`, `refund_desc`, `notify_url` |
| `get_refund_result.py` | `api.pay.yungouos.com/api/pay/wxpay/getRefundResult` | GET | `refund_no`, `mch_id` | — |

异步通知的签名字段（验签用）：

- **支付通知**：`code`, `orderNo`, `outTradeNo`, `payNo`, `money`, `mchId`
- **退款通知**：`code`, `refundNo`, `orderNo`, `outTradeNo`, `payNo`, `mchId`, `payName`, `refundMoney`, `channel`, `refundTime`, `payRefundNo`, `applyTime`

## 六、上线前 Checklist

- [ ] YunGouOS 商户后台「支付目录」配 `https://dejinzhoujin.com/payment/`
- [ ] dejinzhoujin.com 已 ICP 备案、已配 https
- [ ] 秒哒「应用发布 > 自定义域名」绑到 dejinzhoujin.com
- [ ] 秒哒「技能 > 我的 > dejin-wxpay-jsapi > 环境变量」填 YUNGOUOS_PARTNER_KEY
- [ ] Supabase Functions Secrets 填 3 个变量
- [ ] orders / refunds 两张表已建（建表 SQL 在 edge_function_notify.ts 底部）
- [ ] 0.01 元在手机微信内全流程测试
- [ ] 0.01 元在 PC 浏览器扫码全流程测试（确认 Native 没坏）
- [ ] 退款 0.01 元测试
- [ ] **重置 YunGouOS 支付密钥**（开发过程中密钥曾在多处出现，必须重置）

## 七、关键文件清单

技能包 `dejin-wxpay-jsapi.zip` 内容（25KB，13 个文件）：

```
SKILL.md                                  # 含 YAML frontmatter
assets/icon.png
references/
  edge_function_notify.ts                 # 应用后端接收异步通知（首选）
  frontend_jsapi_invoke.html              # 前端调起键盘片段
  pay_notify_handler.py                   # Flask 后端备用版
  refund_notify_handler.py                # Flask 后端备用版
  yungouos-api-cheatsheet.md              # 5 个接口速查
scripts/
  _sign.py                                # MD5 签名工具（自检通过）
  get_oauth_url.py
  get_oauth_info.py
  create_jsapi_order.py
  refund_order.py
  get_refund_result.py
```