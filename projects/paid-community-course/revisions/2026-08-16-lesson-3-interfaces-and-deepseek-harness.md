# 2026-08-16：第3课第三轮调整：接口关系与 DeepSeek Harness

> 状态：已被 2026-08-17 真实授课后的演示驱动重构取代
> 飞书正文：<https://hv21wf9uao9.feishu.cn/wiki/VsvFwdyHRiHuDIkxx5gcM6nanmh>
> 飞书写入版本：revision 125
> 前一版本：[`2026-08-16-lesson-3-ai-collaboration-mindset-expansion.md`](./2026-08-16-lesson-3-ai-collaboration-mindset-expansion.md)
> 受众：第一季度课程学员，以非程序员和 AI 协作初学者为主

## 本轮反馈

建委在第二轮正文上继续做了个人调整，增加了 MCP、UI 组件库、Supabase、飞书 CLI 和 OfficeCLI 等链接，并手动调整了多张表格的宽度。本轮修改必须保留这些内容与布局，只处理指定的概念解释。

现有 MCP 组成和 Harness 组成仍然偏技术实现，不适合只想更好使用 AI 的普通学员。课程还需要重点说清终端、CLI、具体 CLI 工具、API 和 MCP 的关系：CLI 既是 Command Line Interface，也经常代指一个具体命令工具，因此容易和 API 里的 Interface 混淆。Function Calling 对本课受众没有直接使用价值，应从主线删除。

## 当前解释口径

1. **终端不是 CLI 工具。**终端是输入命令和查看结果的窗口或运行环境；电脑终端和云端网页终端都属于终端。
2. **CLI 有两种常见用法。**它既可以指命令行这种交互方式，也可以代指 Git、飞书 CLI、OfficeCLI 等具体命令程序。具体 CLI 是人或 AI 的命令入口，不等于 API；它的底层可能继续调用 API。
3. **API 面向程序间的固定协作。**产品代码需要长期、稳定、精确地实现登录、支付或数据查询等功能时，通常直接调用 API。
4. **MCP 面向 AI 的工具发现与调用。**AI 需要在对话或连续任务中发现资料、选择工具和执行外部动作，并且已有可信、权限清楚的 MCP 时，优先考虑 MCP。MCP Server 的底层仍可能调用 API、CLI 或数据库能力，因此 MCP 不取代 API。
5. **按执行者和场景选择。**本地或云端执行明确动作、工具已有成熟命令入口时用 CLI；产品里的固定功能或服务只提供接口时用 API；AI 需要重复发现和调用多项外部能力时用 MCP。三者可以同时出现在一个项目中。
6. **Function Calling 不进入本课主线。**学员当前不需要掌握该实现层概念，避免为了概念完整而增加无用认知负担。
7. **MCP 内部组成降到了解层。**不再要求学员从 Host、Client、Server、Tools、Resources 等协议名词开始，而是先确认正在使用的 AI、接入的 MCP、可访问的外部能力和权限确认范围。
8. **Harness 从使用者关心的问题解释。**正文改为八件事：AI 在哪工作、能用什么、哪些动作先问人、中断后从哪继续、出错时看什么、怎样证明完成、什么时候停止、出问题怎样撤回。

## DeepSeek Harness 的课程位置

DeepSeek Harness 只作为“模型和 Harness 是不同层”的最新实例，不把它讲成所有学员必须安装的新工具，也不把 Harness 简化成可自定义的终端界面。

当前采用的官方事实包括：DeepSeek Harness 处于开发者预览阶段；官方使用 `Agent = Model + Harness` 解释二者关系；项目以 “Everything is a plugin” 说明模型、工具、Skill、会话、运行环境、存储、任务循环、调度和界面可以作为插件组织；执行轨迹可以记录、继续、分叉和回放。Codex、Claude Code 等现成工具则作为已经组装好的 AI 工作台来理解，两者服务的使用门槛和目的不同。

## 保护的用户内容

本轮使用飞书 block 级局部修改，没有覆盖整篇文档。以下建委新增内容在回读中保持存在：

- MCP 仓库：`https://mcp.so/`、`https://lobehub.com/`
- UI 组件：`https://www.originkit.dev/`、`https://reactbits.dev/`、`https://ui.shadcn.com/`、`https://heroui.com/`、`https://magicui.design/`
- Supabase：`https://supabase.com/`
- 飞书 CLI：`https://github.com/larksuite/cli`
- OfficeCLI：`https://github.com/iOfficeAI/OfficeCLI.git`
- MCP 解释表列宽：169 / 651
- CLI、API、MCP 对比表列宽：90 / 280 / 450
- Harness 八件事表列宽：107 / 315 / 398

## 依据与来源

- 当前对话中建委对 CLI、MCP、API、Function Calling、Harness 深度、目标受众和个人修改保护的明确反馈。
- 建委提供的 DeepSeek 分享页：<https://chat.deepseek.com/share/m3ouuwvf62oeiqqtzm>。该页面只作为理解角度参考，事实口径以官方资料复核。
- DeepSeek Harness 官方介绍：<https://www.deepseek.com/harness/en/>。
- DeepSeek Harness 官方仓库：<https://github.com/deepseek-ai/deepseek-harness>。
- 仓库 [`expression/methods/problem-driven-technical-explanation.md`](../../../expression/methods/problem-driven-technical-explanation.md) 和 [`expression/source-materials/feitian-shanke/README.md`](../../../expression/source-materials/feitian-shanke/README.md)：采用问题、旧办法、实际阻力、新连接方式和使用判断的解释顺序，不照抄外部作者句式。

## 验证记录

- 飞书采用局部 block 更新，最终 revision 125，所有写入响应均无 warning。
- 目录回读确认第6章 MCP、第7章 CLI/API、第8章 Harness 的标题层级和编号连续。
- 关键词回读确认建委新增的 MCP、UI 组件、Supabase、飞书 CLI 和 OfficeCLI 链接仍在原内容块。
- `Function Calling` 在正文回读中无命中。
- 三张受保护表格的列宽分别保持为 169 / 651、90 / 280 / 450、107 / 315 / 398。
- DeepSeek Harness 官方介绍和官方 GitHub 仓库链接已写入正文。
