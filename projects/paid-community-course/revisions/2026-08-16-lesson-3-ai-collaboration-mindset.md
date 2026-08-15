# 2026-08-16：第3课重构为 AI 时代协作心法

> 状态：当前有效
> 飞书正文：<https://hv21wf9uao9.feishu.cn/wiki/VsvFwdyHRiHuDIkxx5gcM6nanmh>
> 飞书写入版本：revision 9
> 受众：第一季度课程学员，以非程序员和 AI 协作初学者为主

## 修订原因

原第3课已经列出 Prompt、Context、Workflow、Skill、MCP 和 CLI，但主要停留在术语定义，学员不容易理解“为什么现在就要学这些，以及它们怎样影响后续 AI 编程”。建委本次明确：这一课的核心不是背名词，而是建立 AI 时代的协作心法，理解这些概念是普通 AI 使用者与能够系统使用 AI 的人的分水岭。

本次重构还补充了 API 接口、现成 Prompt 优化器的使用方法、Skill 的创建/寻找/安装/使用、MCP 的 UI 组件库与数据库场景，以及 Harness 对权限、日志、测试、预算和停止条件的管理。

## 当前正文结构

1. 为什么要单独学这些名词：从“问一次”推进到“长期协作”的分水岭。
2. 能力地图：Prompt、Context、Workflow、Skill、MCP、CLI、API、Harness 的职责边界。
3. Prompt：任务卡、范围与验收，以及 Prompt 优化器的验证流程。
4. Skill：什么值得沉淀，如何创建、寻找、安装和使用。
5. MCP：连接 UI 组件库和数据库时的具体价值与最小权限原则。
6. CLI 与 API：执行命令、系统间请求和 AI 工具连接的区别。
7. Harness：运行环境、确认、日志、测试、预算和停止条件。
8. 完整场景：用组件灵感收藏网站串联全部能力。
9. 学习顺序与学员自检。

## 内容与表达依据

- 当前对话中建委对第三课目标、AI 编程场景、组件库 MCP、数据库 MCP、API 和课程受众的明确要求。
- 仓库 [`projects/paid-community-course/README.md`](../README.md) 与 [`curriculum-design.md`](../curriculum-design.md) 的第一季度 AI 编程系统实战和学员资料边界。
- 仓库 [`projects/ai-training/teaching-and-course-design.md`](../../ai-training/teaching-and-course-design.md) 新增的学员正文与讲师备课边界：默认不写分段授课时长。
- 仓库 [`expression/communication-preferences.md`](../../../expression/communication-preferences.md) 与 [`expression/methods/problem-driven-technical-explanation.md`](../../../expression/methods/problem-driven-technical-explanation.md) 的问题驱动、场景优先和去 AI 味要求。
- 建委提供的 Harness 参考文章：<https://zcnbmtu48lww.feishu.cn/wiki/VuZDwKEC6ik1WckigIpc1GXbnuk>，重点借鉴“模型外部运行系统、权限、反馈、测试和停止条件”的讲解角度；文章中的 Loop Engineering 被压缩为 Harness 的反馈循环，避免在本课继续扩张术语数量。
- 文中链接的官方资料：<https://modelcontextprotocol.io/docs/getting-started/intro>、<https://agentskills.io/specification>、<https://platform.openai.com/docs/guides/prompt-engineering>、<https://openai.com/index/harness-engineering/>、<https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents>。动态工具的具体界面和权限仍需按当前环境复核。

## 验证记录

- 飞书 `docs +update --command overwrite` 写入成功，无服务端 warning。
- 目录回读确认 9 个一级章节和 Prompt 优化器、Skill、MCP、CLI/API、Harness 子章节存在。
- 关键词回读确认“组件库”“数据库”“Prompt 优化器”“API”“Harness”和“分水岭”均落入正文。
- 以“分钟、课时安排、时间分配、讲师提示”扫描正文，无命中。
- 未复制整篇教程到 GitHub；仓库只保存长期索引、规则和修订原因。
