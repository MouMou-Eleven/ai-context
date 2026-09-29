# 培训与教学

建委作为讲师给别人上课的经验：备课、写课件、讲课、复盘。包括会员社群的课、企业和机关培训、图书馆和夜校的课。

教师委托建委**制作**的微课、MG 动画、精品课 PPT 不算这里，属于[设计：教育作品](../design/video/education/README.md)。

## 先分清你要做的是哪一种

| 你要做的 | 给谁看 | 先读 | 再读 |
|---|---|---|---|
| **培训方案 / 课程大纲**（报给主办方的） | 主办方、领导 | [常讲课题](./topics.md) → [对外方案写法](../other/commercial/experience/external-proposal-design.md) | 需要 Word 时读[政企 Word 排版](../other/commercial/delivery-formats/gov-enterprise-word.md) |
| **课件 / 分享资料 / 课堂文档**（上课用的） | 学员 | [建委的培训风格](./experience/jianwei-training-style.md) + [口语样稿](../../../system/expression/voice-samples.md) | [课程怎么组织](./experience/demo-driven-course-design.md)；飞书课件再读[可视化与口语化](./experience/visual-and-oral-training-docs.md) |
| **实操教程**（学员跟着做的） | 学员 | [教程写法](./experience/tutorial-writing.md) | 当前工具的实际界面 |
| **讲技术概念**（API、CLI、Skill 这类） | 学员 | [从问题推导概念](./experience/technical-explanation/problem-driven-technical-explanation.md) | — |
| **讲师备课稿**（时间安排、演示准备，只给自己看） | 建委本人 | 只有建委明确要才写 | [备课与交付物区别](./experience/teaching-and-course-design.md) |
| **招生宣传 / 课程介绍** | 潜在学员 | [自媒体：宣传写法](../self-media/marketing-copy/reader-question-led-promotion.md) + [口语样稿](../../../system/expression/voice-samples.md) | 本页的课题和课程事实，用来提供干货 |
| **讲后复盘、沉淀经验** | 以后的 AI | 本页"怎样沉淀" | — |

同一个主题可能要出好几样东西，比如一场培训要方案、课件、朋友圈宣传。每样东西分开按上表选，事实只取一处。

## 最容易犯的三个错

1. **把给学员的课件写成给讲师看的**：出现"本节讲 20 分钟""讲师这里演示""课堂要看什么"。学员课件里一律不写。
2. **写成书面文章**：课件要能直接讲出来。拿不准时对照[口语样稿](../../../system/expression/voice-samples.md)，读出来不像建委在说话就改。
3. **把对外方案写成内部稿**：方案给主办方看，只写学什么、有什么用、谁来讲。谈判策略、提示词原文、操作路径、"待核实"之类内部内容不写进方案。

## 目录

| 位置 | 内容 |
|---|---|
| [topics.md](./topics.md) | 建委常讲的课题（AI 全景、提示词工具、Excel/Word、知识库、自动化、AI 编程……）和往期大纲 |
| [experience/](./experience/README.md) | 培训方法：风格、课程组织、可视化与口语化、教程写法、技术概念讲解 |
| [AI 培训项目](../../projects/ai-training/README.md) | 各单位培训场次（济南干部培训、济南市图书馆）、[场次索引](../../projects/ai-training/sessions-index.md)；按课件标题找飞书正文；归属不明的资料 |
| [attribution-and-updates.md](./attribution-and-updates.md) | 一份资料属于哪个系列、哪场培训的判断规则 |

会员社群的课程事实（课序、权益、价格）在[社群项目](../../projects/paid-community-course/README.md)，不在这里。课号只在自己的系列里有效：图书馆的"第 6 课"和社群的"第 6 课"是两回事。

## 怎样沉淀

- 讲完课的反馈：能用到别的课上的，直接改 experience/ 里对应的那一条，不要另起新文件；只跟这一场有关的，写进这一场的记录。
- 新的常讲课题、新的讲法：补进 [topics.md](./topics.md)。
- 同一个错误又犯了：不要再加一条"必须……"，而是在[培训风格](./experience/jianwei-training-style.md)的"高频失误"表里补上这次的来源，并想办法让检查动作更具体。
- 具体规则见[仓库写入规范](../../../system/repository/ingestion-workflow.md)。

<!-- generated-related-assets:start -->
## 相关项目与案例

| 类型 | 项目或案例 | 适用领域 |
|---|---|---|
| 长期项目 | [AI 培训](../../projects/ai-training/README.md) | 培训业务 |
| 长期项目 | [AI 超级个体陪跑社群](../../projects/paid-community-course/README.md) | 会员培训与社群经营 |
<!-- generated-related-assets:end -->

<!-- generated-methods:start -->
## 按实际需要选择方法

由routes.json生成。先判断本次成品和读者，再按下表实际需要读取方法正文；无需点名作者。多种方法可分工，但同一段不拼接相互冲突的结构。没有适用需求时跳过，不能因看到本表就全部加载。

| 需要解决什么 | 方法正文 | 不适用／保留边界 | 成品怎样检查 |
|---|---|---|---|
| 非技术读者需要理解概念、机制或技术差别，不能只背定义时；主题可以来自提示，也可以来自AI读到的材料 | [从问题推导概念](experience/technical-explanation/problem-driven-technical-explanation.md) | 纯查询、术语速查、直接操作、已接受稿逐字保护时不展开推导；出版只借解释逻辑，保留出版书面语与编辑规则 | 读者能说出原问题、关键变化及使用判断；不虚构历史发展、事实或作者经历，不混入讲师指令 |
| 向政府、企业或组织方提交培训、课程纲要与项目方案时 | [对外方案内容设计](../other/commercial/experience/external-proposal-design.md) | 课堂课件、讲师备课、教程、研究报告和合同不按方案删去其必要信息 | 逐段确认内容、场景和价值；移出提示词、操作路径、内部分工、核验过程与免责话语；检查实际DOCX和来源留存 |
| 面向跨岗位学员设计AI工具全景与工作场景实操课程时 | [工具全景到工作场景](experience/demo-driven-course-design.md) | 单工具进阶课不强制全景；事实查询不读课程方法；方案不含讲师脚本 | 类别帮助选择，提示词连接任务，场景说明熟悉工作与可见成果；本地存储与模型处理分别核对 |
<!-- generated-methods:end -->
