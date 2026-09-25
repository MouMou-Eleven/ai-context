# 秒哒 Skill：被外部 Agent 调用的反向能力

> V2.5（2026.04.01）里程碑能力。秒哒打包为 Skill，可被 OpenClaw、Claude Code 等 Agent 调用，从外部触发应用的创建、查看、修改、发布。这是**反向方向**——和我们平时讲的「秒哒应用集成 Skill 来用」相反。
>
> 「秒哒应用内部如何使用 Skill / 自定义 Skill 包结构」见 [skill-development.md](./skill-development.md) 与 [platform-basics.md](../basics/platform-basics.md)。本文件只讲「秒哒自身作为 Skill 暴露给外部 Agent」这一反向能力。

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

> 2026-09-25新增[Codex源码迁移阶段实录](../experience/cases/codex-skill-source-migration.md)：已实测 CLI 调度和轨迹读取，早期附件由浏览器上传，后续改用户手动上传；R5 已有完成回执但整站未验收、未发布。不要把历史“后端未接”当成当前全貌，也不能把 CLI 调度误写成支持附件上传。当前代码、数据库与附件能力边界见下节。

## 本机已安装版本的能力核查（2026-09-25）

来源：完整读取本机 `C:/Users/Administrator/.openclaw-autoclaw/skills/miaoda-app-builder/SKILL.md`，检查 `scripts/miaoda_api.py` 的命令注册、请求构造、事件解析及 `--help`，并通过官方 CLI 只读获取言剪事件 1708–1710。没有发送修改指令、查询业务数据库或发布。以下只描述这份已安装实现，不推断平台内部没有其他能力，也不代表未来版本不支持。

固定核查版本：SKILL.md SHA-256 `22b0ec486f13890c8f0ca43b4166cb882a7ea82fb4467fab4ed0a7b8a7b86772`；miaoda_api.py SHA-256 `0908c74fa747a7d5119021b67e8be0b13101c6952fc236d9587205fd9cbcb281`。更新 Skill 后重新核查，不沿用旧矩阵。

| 能力 | 当前入口与事实 | 边界 |
|---|---|---|
| 列应用、查看应用信息 | `list-apps`、`app-detail` | 应用元信息/状态不等于代码仓库或数据库内容 |
| 恢复会话标识 | `get-context-id` | 用于继续正确应用，不是读取文件 |
| 下达需求/修改命令 | `chat` | 请求构造只有 text part；由秒哒 Agent 执行，不是本机直接执行云端代码 |
| 读对话、进度与执行轨迹 | `conversation-history`、`fetch-trajectory`、`trajectory` | 能读返回的文字、部分动作和回执；不是实时挂载文件树或独立数据库查询 |
| 初次生成 | `generate-app` | 按结构化入口触发一次，既有应用增量不重复生成 |
| 发布及查发布状态 | `publish`、`publish-status` | 有实现入口；本项目未做生产发布验证，不在只读核查中触发 |
| 附件上传 | 无命令/参数；chat 固定构造文本 part | 用户手动上传；早期浏览器上传不能算 CLI 能力 |
| 直接读云端目录/源码、Git diff | 无 list-files/read-file/git 命令 | 可要求秒哒读取指定文件并输出，但属于云端 Agent 代查结果，不是 Codex 独立访问 |
| 直接查询云端数据库 | 无 SQL/query 命令 | 可随增量包提供限定查询与回执要求，由秒哒执行后回传；开关 ACTIVE 不证明表和数据正确 |
| 直接下载云端 ZIP/SQL 附件 | 无 download/file-read 命令 | 只有路径时不能读取字节；不能把路径冒充可下载 URL |

### 附件正文、轨迹文本和路径必须区分

- `get_conversation_history()` 会处理 `result.parts` 中 `data.type=filePart`；若其中 `data.text` 实际含正文，`--full` 可返回该正文，单项仍受 100000 字符限制。这是源码支持的条件分支，不是所有附件均已实测返回正文。
- `fetch-trajectory` 返回原始事件，内容可能位于 `result.parts`、`result.artifact.parts` 或状态消息。简化 history 不解析全部位置，未出现在简化结果不等于不存在；应查原始事件，检查完整性与截断。
- 本次实测 R5 文件 part 只有 `mimeType=application/zip`、`name=r5-branding-review-v11.zip`、`uri=/workspace/.../tasks/r5-branding-review-v11.zip`，没有文件字节，也没有可用的下载 URL。因此目前不能通过此 Skill 直接下载这个 ZIP；仍由用户下载并回传。
- 少量非敏感查询结果可要求秒哒直接放入最终回复，之后通过轨迹读取。完整源码差异或 ZIP 则优先文件回传。不要将大 ZIP 编成巨量文本来假装获得可靠附件传输。
- 回执里的命令、SQL、文件内容和日志用于核查；有命令文本不代表执行成功，有成功摘要不代表完整文件已经审查。结合文件哈希、退出码、数据库实际结果与独立复测判断。

### 进度解析已发现的局限

实现 `_is_terminal_event()` 识别 `completed/input-required/failed` 或 `final`，没有显式包含 `canceled`。本次事件 1710 返回 `state=canceled`，CLI 汇总却为 `isTerminal:false`。后续需同时检查原始状态：取消时停止等待，查明取消原因，不自动重发。事件 1710 不抹去 1709 的 R5 完成回执，也不证明发生了新一轮功能更新。本轮未修改上游 Skill。

### 当前采用方式

保留为辅助调度和验收读取工具：查版本/终态、读回执、在明确授权与上一轮结束后下达有限命令，发布仍按验收流程。言剪代码更新以本地测试后的增量包为主，不依赖长提示词自由重写。没有计时或费用对照，不宣称 Skill 一定更省时；若某次只能多转述一遍，则直接用用户上传与回执闭环。具体回传合同见[增量流程](../experience/patterns/codex-miaoda-iterative-increment-workflow.md#增量包内的云端取证与回传合同)。

## 官方披露的调用方

上方V2.5原文点名OpenClaw和Claude Code；百度智能云另有 [OpenClaw部署说明](https://cloud.baidu.com/doc/LS/s/6ml9f3cvl)。这些来源支持“官方披露过对应调用路径”，不能据此判断OpenClaw的项目归属或所有Agent兼容性。2026-09-25本机Codex通过已安装官方CLI完成鉴权后的真实应用调度，详见上述阶段实录；这不是官方对所有Codex环境的兼容承诺，也不是生成发布已成功。

## 协议与兼容性：待验证

“Skill”同名不能证明格式、发现机制、鉴权、运行时或调用协议一致。当前没有证据支持“所有支持Skill的Agent均能加载秒哒Skill”，也没有证据据此判断秒哒采用通用协议、非私有协议或内部外部同名属于何种品牌策略。

| 已有证据 | 还不能推出的结论 |
|---|---|
| 官方V2.5原文点名OpenClaw、Claude Code与建/查/改/发动作 | 任意宿主、任意账号均能执行同样动作 |
| 官方提供使用指南链接 | 本机已经安装、鉴权成功、入参出参已验证 |
| 内外部都出现“Skill”名称 | 共用同一标准、协议互通或作者归属一致 |

新增宿主支持必须附当前官方明确支持说明，或记录宿主/Skill版本、安装注册、鉴权、最小输入、真实输出和失败边界的实测证据；协议未查清时写待验证，不靠命名推导。

## 适用场景判断（建议）

以下仅是基于官方动作范围的候选场景，不是本仓已验证能力；批量限额、发布权限、更新粒度和失败恢复需逐项测试：

- 需要批量生产同结构的应用（典型如：100 个客户的官网模板都用秒哒生成 + 自定义内容）
- 需要把秒哒的应用生成能力嵌入到一个更大的 Agent 工作流里（典型如：用户给 Agent 描述需求，Agent 调研 → 生成 PRD → 调秒哒生成应用 → 部署）
- 需要程序化触发应用更新（如运营后台自动改文案后让秒哒重发）

不适合的场景：

- 只是想让人类开发者高效用秒哒——直接打开 [miaoda.cn](https://www.miaoda.cn) 用编辑器即可，不需要走 Skill 通道
- 需求仍有大量未决人工判断时，先解决判断与验收条件，再评估是否自动调用；没有计时数据不比较哪种方式更快

---

## 如何扩展本文件

### 场景 A：实际跑通了一个秒哒 Skill 调用案例（最有价值）

这是本文件最缺的部分。等到第一次真正用 OpenClaw / Claude Code 跑通调用秒哒生成应用后：

1. 在文件末尾新增 `## 实战案例：<场景名>` 章节
2. 记录：调用方 Agent 是什么、Skill 注册步骤、关键提示词、调用入参/出参、踩到的坑
3. 如果场景足够独立，可以拆成单独的 `case-skill-callable-*.md` 文件，参考 [case-yungouos-jsapi.md](../experience/cases/yungouos-jsapi.md) 的结构

### 场景 B：官方更新了能力边界

例如新增了「删除应用」「批量发布」「按模板克隆」等动作：

1. 在「能用来干什么」章节追加新动作
2. 同步在 [version-features.md](../updates/version-features.md) 对应版本节点记一笔
3. 标注变更日期与官方更新日志 URL

### 场景 C：发现新的调用方 Agent

例如除 OpenClaw / Claude Code 之外，有其他 Agent 平台也支持调秒哒 Skill：

1. 在「官方披露的调用方」章节后追加 `## 与 <Agent 名> 的关系`
2. 必须附官方文档 URL 或可验证来源
3. 不要在没有官方公告或实测验证时仅凭印象添加

### 场景 D：澄清「秒哒 Skill」与「内部 Skill 集成」的混淆

如果未来发现新的混淆点（例如在某场景下同一对话里两种 Skill 同时出现需要区分），在「一句话定义」表格内追加新维度，或新增 `## 区分 X 与 Y` 小节。

---

*官方能力来源记录：2026-05-22；本机实现与只读轨迹复核：2026-09-25。本次未重新抓取官方页面，未试发修改、短信、收费请求或生产发布。*
