# 秒哒 Skill：被外部 Agent 调用的反向能力

> V2.5（2026.04.01）里程碑能力。秒哒打包为 Skill，可被 OpenClaw、Claude Code 等 Agent 调用，从外部触发应用的创建、查看、修改、发布。这是**反向方向**——和我们平时讲的「秒哒应用集成 Skill 来用」相反。
>
> 「秒哒应用内部如何使用 Skill / 自定义 Skill 包结构」见 [skill-development.md](./skill-development.md) 与 [platform-basics.md](./platform-basics.md)。本文件只讲「秒哒自身作为 Skill 暴露给外部 Agent」这一反向能力。

## 官方文档锚点

- **秒哒 Skill 使用指南（如何在 OpenClaw 中调用秒哒 Skill）**：[https://cloud.baidu.com/doc/MIAODA/s/mmmnhtlx9](https://cloud.baidu.com/doc/MIAODA/s/mmmnhtlx9)
- V2.5 发布秒哒 Skill 的更新日志条目：[https://cloud.baidu.com/doc/MIAODA/s/Zmm32qp8x](https://cloud.baidu.com/doc/MIAODA/s/Zmm32qp8x)（搜「发布秒哒 Skill」）

## 一句话定义

| 维度 | 内部 Skill（一直存在） | 秒哒 Skill（V2.5 反向能力） |
|------|----------------------|---------------------------|
| 谁是调用方 | 秒哒应用（自身的 Edge Function / 前端） | 外部 Agent（OpenClaw、Claude Code 等） |
| 谁是被调用方 | 第三方能力（微信支付、MiniMax、千帆 Agent…） | 秒哒平台本身 |
| 触发动作 | 应用运行时调一个外部 API | 在 Agent 对话里命令秒哒「建/改/发」一个应用 |
| 入口配置 | 应用编辑器里 @ 技能 + 配置环境变量 | 在外部 Agent 里登记并调用「秒哒 Skill」 |
| 文件 | [skill-development.md](./skill-development.md) | 本文件 |

> 这两个概念在中文里都叫「秒哒 Skill」，但作用方向相反。本档案为消歧起名：内部 Skill 集成 = 「秒哒调外部」，秒哒 Skill = 「外部调秒哒」。

## V2.5 官方原文（事实存档）

> "秒哒打包为 Skill，支持被 OpenClaw、Claude Code 等 Agent 调用，支持通过 Agent 来应用（网页、微信小程序、游戏、AI 工具等）的创建、查看、修改、发布上线等操作，实现智能化、批量化的应用自动开发。"
>
> — 26 年更新日志 V2.5（[原文链接](https://cloud.baidu.com/doc/MIAODA/s/Zmm32qp8x)）

## 能用来干什么（基于官方描述）

按官方更新日志披露的能力范围：

- **创建应用**：从外部 Agent 触发秒哒生成一个新应用（网页 / 微信小程序 / 游戏 / AI 工具等形态）
- **查看应用**：从 Agent 侧读取已有应用的状态、信息
- **修改应用**：从 Agent 侧下发修改指令，秒哒执行变更
- **发布上线**：从 Agent 侧触发已开发应用的发布动作
- **批量化自动开发**：让外部 Agent 串起多个应用的开发流（这是 V2.5 强调的核心场景——批量、自动化）

> ⚠️ **本文件目前不写「具体怎么调用」**：调用方式、鉴权、Skill 注册、入参出参规范等技术细节，必须以官方[使用指南](https://cloud.baidu.com/doc/MIAODA/s/mmmnhtlx9)为准；本档案目前没有验证过的实战记录，不靠猜补充。

## 与 OpenClaw 的关系

OpenClaw 是百度智能云体系内的轻量应用服务器/Agent 部署底座（参见百度智能云[10 分钟快速部署 OpenClaw](https://cloud.baidu.com/doc/LS/s/6ml9f3cvl)）。秒哒 Skill 在 OpenClaw 内调用是 V2.5 官方主推路径。Claude Code 调用是同时披露的另一条路径，具体差异在官方使用指南内说明。

## 与「Claude Skill」机制的关系

「Skill」一词在 Claude / Claude Code 生态里也有同名概念（Anthropic 推出的可被 Agent 调用的能力封装）。秒哒 Skill 在命名上对齐了这一通用概念，使秒哒能力可以**像任何其他 Skill 一样**被支持 Skill 协议的 Agent 加载。这意味着秒哒 V2.5 不是定义了一套私有协议，而是接入了通用 Agent 生态。

> 这与 V2.5 同期把内部插件体系也改名为 Skill 是同一品牌策略——平台对内对外都统一到「Skill」一词。

## 适用场景判断（建议）

适合用「秒哒 Skill」反向调用的场景：

- 需要批量生产同结构的应用（典型如：100 个客户的官网模板都用秒哒生成 + 自定义内容）
- 需要把秒哒的应用生成能力嵌入到一个更大的 Agent 工作流里（典型如：用户给 Agent 描述需求，Agent 调研 → 生成 PRD → 调秒哒生成应用 → 部署）
- 需要程序化触发应用更新（如运营后台自动改文案后让秒哒重发）

不适合的场景：

- 只是想让人类开发者高效用秒哒——直接打开 [miaoda.cn](https://www.miaoda.cn) 用编辑器即可，不需要走 Skill 通道
- 应用复杂度极高、有大量人类决策点——Agent 自动化在这种场景反而比人类直接操作慢

---

## 如何扩展本文件

### 场景 A：实际跑通了一个秒哒 Skill 调用案例（最有价值）

这是本文件最缺的部分。等到第一次真正用 OpenClaw / Claude Code 跑通调用秒哒生成应用后：

1. 在文件末尾新增 `## 实战案例：<场景名>` 章节
2. 记录：调用方 Agent 是什么、Skill 注册步骤、关键提示词、调用入参/出参、踩到的坑
3. 如果场景足够独立，可以拆成单独的 `case-skill-callable-*.md` 文件，参考 [case-yungouos-jsapi.md](./case-yungouos-jsapi.md) 的结构

### 场景 B：官方更新了能力边界

例如新增了「删除应用」「批量发布」「按模板克隆」等动作：

1. 在「能用来干什么」章节追加新动作
2. 同步在 [version-features.md](./version-features.md) 对应版本节点记一笔
3. 标注变更日期与官方更新日志 URL

### 场景 C：发现新的调用方 Agent

例如除 OpenClaw / Claude Code 之外，有其他 Agent 平台也支持调秒哒 Skill：

1. 在「与 OpenClaw 的关系」章节后追加 `## 与 <Agent 名> 的关系`
2. 必须附官方文档 URL 或可验证来源
3. 不要在没有官方公告或实测验证时仅凭印象添加

### 场景 D：澄清「秒哒 Skill」与「内部 Skill 集成」的混淆

如果未来发现新的混淆点（例如在某场景下同一对话里两种 Skill 同时出现需要区分），在「一句话定义」表格内追加新维度，或新增 `## 区分 X 与 Y` 小节。

---

*最后更新：2026-05-22*