# 2026-08-17：第3课真实授课后的演示驱动重构

> 状态：当前有效
> 飞书正文：<https://hv21wf9uao9.feishu.cn/wiki/VsvFwdyHRiHuDIkxx5gcM6nanmh>
> 飞书写入版本：revision 151
> 前一版本：[`2026-08-16-lesson-3-interfaces-and-deepseek-harness.md`](./2026-08-16-lesson-3-interfaces-and-deepseek-harness.md)
> 复盘来源：2026-08-16 晚会员社群第3课真实授课

## 为什么再次重构

建委实际讲完第3课后确认，前一版虽然内容丰富、结构完整，但整体更像供学员阅读的技术文章，不像能够自然讲出来的课程。现场出现了明确证据：正文与表格重复时表格被直接跳过；纯文字概念没有可见变化时难以展开；Harness 八件事、按钮改色、工具失败、长任务循环、学习顺序和标准答案式自检都没有进入实际讲解。

这次复盘的核心不是继续补字，而是改变课程的设计单位：从“一个知识点写完整”改成“一个概念怎样通过操作、对比和结果被学员看懂”。

## 当前结构

正文从 11 个一级章节压缩为 7 个：

1. CLI：鼠标创建文件夹、手工命令和 AI 自动执行三次对比。
2. Prompt 与 Context：模糊文字、截图和视频输入对比；上下文窗口、压缩和项目说明文件的稳定性对比。
3. Skill：先定义工作说明书，再讲结构、仓库、安装和调用。
4. MCP：按含义、寻找、接入、验证推进，用 UI 组件库和报名数据库两个可视场景讲解。
5. API：在 MCP 之后首次引入，通过 GitHub 普通网页和 API 地址对比建立直观认识，再解释 CLI、API、MCP 的关系。
6. Harness：通过普通聊天工具与 Codex 执行同一任务的差异推出概念，比较 Codex、OpenClaw 和 DeepSeek Harness。
7. 真实项目串联：用带报名功能的课程页面把七个概念放回一条开发路线。

## 删除与保留

删除旧版中讲师现场已经证明无讲授价值的内容：AI 能力大表格、4S 店长篇类比、名词地图、Prompt 要素表、多模态输入表、Context 信息分类表、Skill 生命周期长列表、MCP 内部组成、API 接入检查表、Harness 八件事、按钮改色、工具失败、长任务循环、学习顺序和标准答案式自检。

保留并重新安置建委此前加入的 Prompt 优化器、Google AI Studio 演示、Skill 社区目录、MCP 目录、UI 组件库、Supabase、飞书 CLI、OfficeCLI、DeepSeek Harness 等链接，同时新增 OpenAI / Anthropic 官方 Skill 仓库、Agent Skills 规范、shadcn MCP、Supabase MCP、OpenAI Glossary、OpenClaw 和 GitHub API 演示地址。

## 事实修正

- 课程没有把鼠标点击讲成“调用 CLI”。最终口径是图形界面与 CLI 是两种不同接口，可以完成同一个操作结果；`mkdir` 创建文件夹，`cd` 切换终端当前目录。
- Context window 是模型一次能够处理的信息上限；Compaction 总结较早上下文以继续任务，但不会取消窗口上限。没有写入“模型固定从 100% 下降到 80%”这类无法统一验证的比例。
- Skill 的调用方式按官方工具区分：ChatGPT 桌面端使用 `@`，Codex CLI / IDE 使用 `$` 或 `/skills`；ZIP 被说明为交付形式，不被写成所有产品统一的安装入口。
- UI 场景使用已经提供官方 MCP Server 的 shadcn/ui，不暗示列出的每个 UI 组件库都支持 MCP。
- Supabase MCP 只用于开发和测试场景，正文保留项目范围、只读和不连接生产数据的安全边界。
- DeepSeek Harness 保留开发者预览定位，不把它写成 Codex 或 OpenClaw 的直接替代品。

## 录播与写入保护

写入前完整扫描飞书文档，只发现一个录播资源：

- block ID：`AM44dgxj3oPT6hxP6B6ckOImnDc`
- 类型：飞书妙记 iframe / readonly block

重构采用 block 级操作，保留标题、录播块和其后的空白锚点，分 9 批删除旧正文后再插入新稿，没有使用 overwrite。最终回读仍只有一个录播块，ID 和链接均未变化。

## 验证结果

- 飞书最终 revision 151，全部写入响应无 warning。
- 目录回读确认 7 个一级章节、20 个二级章节，顺序连续。
- 全文只保留 2 张表格，分别承担数据库字段样例和三类 Harness 产品对比，不再复述正文。
- 旧标题“普通人真正需要关心的八件事”“一个按钮改色”“Harness 怎样处理工具失败”“Harness 怎样处理长任务和循环”“学习顺序”“本节自检”均无命中。
- “现场演示不要”“让大家”“多少分钟”“讲师提示”等讲师内部措辞无命中。
- 原有录播、Prompt 优化器、Skill 社区目录、MCP 目录、UI 组件、Supabase、飞书 CLI、OfficeCLI 和 DeepSeek Harness 链接均存在。

## 官方资料

- OpenAI Skills：<https://learn.chatgpt.com/docs/build-skills>
- OpenAI Glossary：<https://learn.chatgpt.com/docs/glossary>
- shadcn MCP：<https://ui.shadcn.com/docs/mcp>
- Supabase MCP：<https://supabase.com/docs/guides/ai-tools/mcp>
- DeepSeek Harness：<https://www.deepseek.com/harness/en/>
- OpenClaw：<https://openclaw.ai/>

## 通用经验沉淀

这次复盘已经抽离为跨课程方法：[`../../ai-training/demo-driven-course-design.md`](../../ai-training/demo-driven-course-design.md)。后续会员社群课程、企业培训、公开课和活动分享在设计技术概念内容时，优先使用其中的“熟悉任务 → 旧做法 → 新做法 → 结果对比 → 概念 → 收益与边界”链路，并把现场被跳过的内容纳入正式复盘。
