# 秒哒应用的发布渠道

> 同一个秒哒应用可以一键发布到 4 类不同渠道，每类的能力边界差别很大。本文件归类官方文档里散落的渠道差异、限制、适用场景，帮 AI 在用户问"我的应用要不要做小程序 / 要不要做 App"时给出准确建议。
>
> 平台基础概念（生成形态、4 子运行时、Skill 内部调用）见 [platform-basics.md](./platform-basics.md)。版本节点（哪个版本上线了哪种渠道）见 [version-features.md](./version-features.md)。本文件只讲「发布到外部时的差异」。

## 官方文档锚点

| 渠道 | 官方文档 |
|------|---------|
| 网页类型应用发布流程 | [https://cloud.baidu.com/doc/MIAODA/s/Lmcjwrtb2](https://cloud.baidu.com/doc/MIAODA/s/Lmcjwrtb2) |
| 自定义域名发布 | [https://cloud.baidu.com/doc/MIAODA/s/Im8ecuhvk](https://cloud.baidu.com/doc/MIAODA/s/Im8ecuhvk) |
| 秒哒官方微信小程序 | [https://cloud.baidu.com/doc/MIAODA/s/Dmdl4j0oj](https://cloud.baidu.com/doc/MIAODA/s/Dmdl4j0oj) |
| 用户自有微信小程序 | [https://cloud.baidu.com/doc/MIAODA/s/pmfnccc1g](https://cloud.baidu.com/doc/MIAODA/s/pmfnccc1g) |
| 5 分钟上线微信小程序 | [https://cloud.baidu.com/doc/MIAODA/s/rmla9utp7](https://cloud.baidu.com/doc/MIAODA/s/rmla9utp7) |
| 提交代码失败常见错误及修复 | [https://cloud.baidu.com/doc/MIAODA/s/mmknf9ork](https://cloud.baidu.com/doc/MIAODA/s/mmknf9ork) |
| 生成 APP | [https://cloud.baidu.com/doc/MIAODA/s/Amoy50baf](https://cloud.baidu.com/doc/MIAODA/s/Amoy50baf) |
| 应用广场 | [https://cloud.baidu.com/doc/MIAODA/s/Pmck9hefk](https://cloud.baidu.com/doc/MIAODA/s/Pmck9hefk) |
| 应用更新与下线 | [https://cloud.baidu.com/doc/MIAODA/s/tmcjx5q55](https://cloud.baidu.com/doc/MIAODA/s/tmcjx5q55) |

---

## 渠道一览

| 渠道 | 形态 | 上线版本 | 是否可绑定自有域名 | 微信支付 | 朋友圈分享 | 微信生态分享 |
|------|------|---------|------------------|---------|----------|-------------|
| **网页类型应用** | Web 应用 | V1.x（一直都有） | ✅ 自定义域名 | ✅（应用集成微信支付，V1.6 起） | — | — |
| **秒哒官方微信小程序**（web-view 接入） | 嵌在秒哒官方小程序里的 Web 应用 | V1.4 一键发布 / 2025.11.11 起新发应用自动开启 | ❌（域名只能在白名单内） | ❌（web-view 限制） | ❌（web-view 限制） | ✅ 可分享给好友 |
| **用户自有微信小程序**（原生小程序） | 微信原生小程序 | V1.6（2025.10.01）首次生成 / V2.4 起支持体验版调试 | — | ✅（原生小程序生态） | ✅（V2.4 起每页默认） | ✅（V2.4 起每页默认） |
| **原生 APP** | iOS / Android 原生 APP | V3.0（2026.05.13） | — | 看具体集成 | — | — |

> 「✅」「❌」反映的是各渠道的官方能力边界，不是"建议要不要做"。

---

## 渠道一：网页类型应用（Web）

最基础也最自由的发布渠道，无外部平台限制。

- **发布流程**：在编辑器内点「发布」→ 选「网页类型」→ 自动分配 `*.appmiaoda.com` 子域名
- **自定义域名**：可绑定自有已 ICP 备案的域名（V1.5 起全类型应用支持，详见 [platform-basics.md](./platform-basics.md) 的「自定义域名」一节）
- **下架/更新**：详见官方[应用更新与下线](https://cloud.baidu.com/doc/MIAODA/s/tmcjx5q55)
- **何时选这条路**：
  - 需要集成微信支付（如电商、付费内容）
  - 需要绑自有域名（如品牌官网）
  - 需要嵌入第三方服务（脚本、SDK）
  - 不希望被微信平台政策约束

## 渠道二：秒哒官方微信小程序（web-view 接入）

把应用接入到「秒哒」这个官方微信小程序里，不需要用户自己注册微信小程序账号。底层是 web-view 加载应用的 Web 版本。

- **发布流程**：发布弹窗里点「立即发布」即可，不需要微信审核
- **2025.11.11 节点**：之前发布的应用需手动重新发布才会自动开启此渠道；之后发布的默认开启
- **访问方式**：扫小程序码 / 链接复制到浏览器 / 在微信里搜「秒哒」小程序进入
- **能力限制**（来自微信官方对 web-view 的规定）：
  1. **不支持微信支付**——web-view 内不能调起支付
  2. **不支持文件下载**——页面会出现「文件下载成功」假象但实际未下载，需要复制链接到浏览器才能完成
  3. **链接外跳白名单**：应用中嵌入的链接，只有在 `appmiaoda.com`、`cloud.baidu.com`、`console.bce.baidu.com` 子域名下时才能在小程序内直接访问；其他域名不能内跳
  4. **不能转发到朋友圈**——只能分享给好友（点右上角分享图标）
- **何时选这条路**：
  - 想让应用进入微信生态、获得分享传播能力
  - 用户没有自己的小程序主体（不想申请认证）
  - 应用本身不依赖微信支付、文件下载、外站跳转

## 渠道三：用户自有微信小程序（原生小程序）

V1.6 (2025.10.01) 起，秒哒可以**生成原生微信小程序源代码**，并通过授权发布到用户自己的微信小程序账号。这是真正的微信原生小程序，不再受 web-view 限制。

- **发布前置**：用户已有微信小程序账号（个人或企业主体）并完成认证
- **关键能力（V2.4 起）**：
  - 支持一键发布到「体验版」用于审核前调试
  - 摄像头/麦克风/相册/位置等隐私能力自动生成微信规范的权限申请弹窗
  - 每个页面默认支持分享到聊天和朋友圈，对话可加内容分享按钮
- **限制**：
  - 每个微信号每周最多 3 次提审（V1.8 节点起，因微信平台月配额限制）
  - 提交代码可能因规范问题失败，详见官方[「向小程序提交代码失败」常见错误及修复方法](https://cloud.baidu.com/doc/MIAODA/s/mmknf9ork)
- **何时选这条路**：
  - 需要微信支付能力
  - 需要朋友圈分享传播
  - 想要独立的小程序品牌主体
  - 项目预算允许走完整微信认证 + 审核链路

## 渠道四：原生 APP（iOS / Android）

V3.0（2026.05.13）里程碑能力。自然语言生成原生 APP，覆盖 iOS 与 Android。

- **能力**（来自 V3.0 更新日志）：
  - 自然语言描述生成原生 APP
  - 支持 iOS 与 Android
  - Android 应用包打包
  - 在线调试
  - APP 热更新
- **何时选这条路**：
  - 需要原生 APP 的独立分发能力（应用商店）
  - 需要原生 APP 才能用的设备能力（推送、深度系统集成等）
  - Web/小程序无法满足体验需求

---

## 同一应用多渠道并存

一个秒哒应用可以同时发布到多个渠道，**但不同渠道的能力差别很大**，最常见的场景是「PC 走 Web Native 扫码 + 手机微信内走 JSAPI」。这种双路径架构的实战实现见 [case-yungouos-jsapi.md](./case-yungouos-jsapi.md)。

为不同渠道做条件分支时（如设备识别、运行环境识别），原则：
- 用 `User-Agent` 检测能力差异（是否在 MicroMessenger 里、是否移动端）
- 在编辑器对话里明确告知秒哒：「PC 走 X，手机微信内走 Y，普通手机浏览器走 Z」
- 不同路径**不要共享支付/账号代码**——能力边界不同，强行复用会绕坑

---

## 如何扩展本文件

### 场景 A：渠道能力变化（最常见）

例如微信平台调整 web-view 能力、秒哒新增桌面 APP 形态、新增鸿蒙 APP 等：

1. 在「渠道一览」表格的对应行更新单元格
2. 在该渠道详细章节追加变化点，标注变更日期与官方文档来源
3. 同步更新 [version-features.md](./version-features.md) 里对应版本节点

### 场景 B：新增第 5 个发布渠道

例如未来上线鸿蒙 APP、桌面应用、其他第三方平台分发：

1. 在「渠道一览」表格新增一行
2. 在文件末尾「渠道四」之后新增 `## 渠道五：<名称>` 章节
3. 必填字段：形态、上线版本、能力边界、限制、何时选这条路
4. 在「官方文档锚点」表格补充该渠道的官方文档 URL

### 场景 C：补充某个渠道的踩坑细节

如果踩坑足够典型，写到 [pitfalls.md](./pitfalls.md)；本文件只记官方能力边界。如果是某个具体业务（如支付）跨渠道接入的完整复盘，写一个 `case-*.md` 案例文件，参考 [case-yungouos-jsapi.md](./case-yungouos-jsapi.md) 的结构。

---

*最后更新：2026-05-22*