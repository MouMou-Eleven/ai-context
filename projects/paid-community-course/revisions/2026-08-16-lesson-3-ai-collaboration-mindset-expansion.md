# 2026-08-16：第3课第二轮扩写：AI 交叉线、多模态 Prompt 与 Harness

> 状态：已被同日第三轮接口关系与 DeepSeek Harness 修订取代
> 飞书正文：<https://hv21wf9uao9.feishu.cn/wiki/VsvFwdyHRiHuDIkxx5gcM6nanmh>
> 飞书写入版本：revision 18
> 前一版本：[`2026-08-16-lesson-3-ai-collaboration-mindset.md`](./2026-08-16-lesson-3-ai-collaboration-mindset.md)
> 受众：第一季度课程学员，以非程序员和 AI 协作初学者为主

## 本轮反馈

建委确认，第一次重构虽然补齐了名词，但开场定位仍然不准确，内容偏短、层次不足，Harness 没有充分吸收参考文章的观点。新的核心口径不是“AI 会写代码，所以人要继续学习编程”，而是：大家都在使用 AI，差别主要体现在是否理解 AI 能力之外、与真实项目相交的那部分工作。

## 新增与重写内容

1. **AI 能力边界。**明确 AI 擅长在已有输入和可调用工具范围内做内容处理、代码生成、测试和修改；域名、数据库、组件库、账号权限、部署、费用、安全、责任和最终验收仍需要人理解与确认。
2. **AI 延伸线与交叉线。**提醒学员不要把长期学习全部投入到模型暂时不会、但可能被下一次升级覆盖的能力；本课名词主要服务于 AI 与现实项目的交叉位置。
3. **4S 店类比与窗户纸。**用“车可以买到，但牌照、保险、停车和道路规则仍要处理”解释 AI 能力与完整项目之间的外部结构，并把名词放回真实问题中。
4. **Prompt 的历史和新定义。**从早期以文字为主的 Prompt、Prompt Engineering 岗位和角色/目标/格式控制，过渡到当前多模态输入；把文字、截图、音频、视频、文件和结构化数据视为可组合的任务输入。
5. **视频作为代码问题证据。**增加录屏规范：从清楚初始状态开始，边操作边说明预期和实际结果，保留控制台和网络变化，再配文字任务卡，让 AI 先诊断后修改。
6. **Context。**补充 Prompt 与 Context 的边界，以及必须提供、按需提供和通常排除的信息层级。
7. **Skill 生命周期。**扩展 Skill 与 Prompt、Workflow 的区别，加入真实案例、固定步骤、触发条件、输入输出、验收、新任务验证和版本维护。
8. **MCP 深讲。**保留 UI 组件库和数据库两个场景，增加版本、许可证、schema、测试库、迁移、权限和回滚要求；解释 MCP、API 与 Function Calling 的层次关系。
9. **Harness 深讲。**参考建委提供的文章，把 Harness 作为模型外部运行系统展开，覆盖运行环境、工具注册、权限确认、状态进度、错误反馈、验证器、预算停止、恢复回滚；增加按钮改色失控案例、工具失败处理和反馈循环边界。
10. **完整项目串联。**用组件灵感收藏网站把 Prompt、Context、Skill、MCP、API、CLI 和 Harness 放进同一条真实开发链路。

## 表达调整

- 删除“这一课不要求你背一串缩写”“神级提示词”等带有营销或说服口吻的表述。
- 开场从“大家都在使用 AI”进入，不把课程定位成证明 AI 会写代码后人仍需学编程。
- 保留“窗户纸”作为建委确认的认知比喻，但把它落到外部资源、权限、接口、部署和验收等可观察对象。
- 学员正文继续不写分段授课时长、课堂分钟数或讲师提示。

## 依据与来源

- 当前对话中建委对开场、AI 交叉线、Prompt 多模态演变、录屏输入、组件库/数据库 MCP 和 Harness 深度的明确反馈。
- 仓库 [`projects/paid-community-course/README.md`](../README.md)、[`curriculum-design.md`](../curriculum-design.md) 和 [`projects/ai-training/teaching-and-course-design.md`](../../ai-training/teaching-and-course-design.md)。
- 仓库 [`expression/methods/problem-driven-technical-explanation.md`](../../../expression/methods/problem-driven-technical-explanation.md) 的问题驱动、场景推导、具体动作和失败案例要求。
- 建委提供的 Harness 参考文章：<https://zcnbmtu48lww.feishu.cn/wiki/VuZDwKEC6ik1WckigIpc1GXbnuk>；本轮重点吸收其“模型外部运行系统、权限、错误反馈、验证和停止条件”的角度。
- 文中官方资料链接：<https://modelcontextprotocol.io/docs/getting-started/intro>、<https://agentskills.io/specification>、<https://platform.openai.com/docs/guides/prompt-engineering>、<https://openai.com/index/harness-engineering/>、<https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents>。

## 验证记录

- 飞书整体重构写入成功，无服务端 warning；随后将“营销内容”替换为“对外内容”，飞书 revision 为 18。
- 目录回读确认 11 个一级章节，覆盖 AI 能力边界、Prompt 多模态输入、Context、Skill、MCP、CLI/API、Harness 和完整案例。
- 正文回读字符数约 15,583，关键词“窗户纸”“多模态”“录制”“Prompt 优化器”“组件库”“数据库”“Harness”“恢复与回滚”均命中。
- 扫描“这一课不要求”“神级提示词”“多少分钟”“课时安排”“时间分配”“讲师提示”“营销味”均无命中。
- 没有把整篇飞书正文复制到 GitHub；本记录只保存长期口径、变化原因、来源与验证结果。
