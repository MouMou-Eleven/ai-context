# 商业化与对外交付

建委的东西只要是**给外部的人看、要对方做决定**（采购、签约、评审、投资、报名、合作），就进这个目录。设计、培训、开发、自媒体负责"内容本身怎么做"，这里负责"给谁看、对方关心什么、哪些话不能出现、用什么格式交"。

商业化不是 AI 或设计的下级门类，所以放在 `other/` 下，任何领域的成品都可以叠加这里的规则。

## 一、先看给谁：按受众选交付方式

| 受众 | 对方关心什么 | 读哪些 | 交付格式 |
|---|---|---|---|
| 政府、机关、事业单位 | 政策契合、内容稳妥、流程规范、能落地 | [对外方案内容设计](experience/external-proposal-design.md) + [内外稿边界](experience/external-deliverable-language.md) | [政企 Word 排版](delivery-formats/gov-enterprise-word.md) |
| 企业（培训采购、项目合作） | 解决什么业务问题、员工学完能做什么、投入产出 | 同上；要拿案例证明效果时加读[案例结果叙事](experience/case-result-narrative.md) | [政企 Word 排版](delivery-formats/gov-enterprise-word.md)；路演场合用 PPT |
| 公益组织、图书馆、社区、夜校 | 受众能不能听懂、公益价值、安全稳妥 | [对外方案内容设计](experience/external-proposal-design.md) + [内外稿边界](experience/external-deliverable-language.md) | 暂无单独验证过的格式，先用政企 Word；第一次实际交付后把差异写进 [delivery-formats/](delivery-formats/README.md) |
| 评委、投资人、孵化机构 | 项目价值、可行性、证据能不能验证 | [赛事、路演与融资材料](experience/competition-and-investor-materials.md) + [案例结果叙事](experience/case-result-narrative.md) | 商业计划书、路演 PPT、申报书，按赛事要求 |
| 个人消费者、学员（报名、购买） | 值不值、适不适合我、有什么顾虑 | [用读者问题组织宣传](../../self-media/marketing-copy/reader-question-led-promotion.md) + [内容需求与承接](experience/content-demand-and-conversion.md) | 文章、海报、报名页，按[自媒体](../../self-media/README.md)对应渠道 |

同一份内容给不同受众，内容结构按受众改，版式按格式文件改，两件事分开。

## 二、再看什么场景：按场景找经验

| 场景 | 读哪些 | 当前沉淀情况 |
|---|---|---|
| 写培训方案、课程大纲给主办方 | [对外方案内容设计](experience/external-proposal-design.md)，课题从[常讲课题](../../training/topics.md)选 | 有真实案例：[济南干部培训](../../../projects/ai-training/jinan-cadre-ai/README.md) |
| 路演、比赛答辩、OPC 等创业赛事、项目申报 | [赛事、路演与融资材料](experience/competition-and-investor-materials.md) + [案例结果叙事](experience/case-result-narrative.md)；视频部分读[创赛宣传片](../../design/video/promo/competition-promo-production.md) | 有方法；建委获得过 OPC 赛道一等奖（见[背书表](../../../../personal/credentials.md)），比赛材料本身尚未作为案例沉淀 |
| 对外宣传、公开分享、讲座后的转化 | [内容需求与承接](experience/content-demand-and-conversion.md) + [案例结果叙事](experience/case-result-narrative.md) | 有方法 |
| 谈单沟通、销售话术、报价解释 | 暂无 | 还没有沉淀。第一次有真实谈单经验时，新建 `experience/sales-conversation.md`（放在已有目录里，不另建文件夹），写清对象、对方顾虑、怎么回应、结果 |
| 判断产品、选渠道、找对标、诊断卖不动的原因 | [商业增长闭环](experience/business-growth-loop.md)（完整方法）→ [分析执行卡](experience/business-analysis-cards.md)（做分析时照着填） | 有方法；总原则在[商业判断原则](../../../../brain/business-judgment.md) |

## 三、对外成品的底线（红线）

对外成品和给建委看的内部稿是两种东西。下面几条每次都要查，完整说明和改写对照表在[内外稿边界](experience/external-deliverable-language.md)：

- 正文、标题、文件名不出现"客户""客户版""待客户确认""建议采用""可再调整"这类内部用语；主语用"本项目""本课程"。
- 已确认的事直接写成确定句；没确认的事先列给建委，不擅自补齐写进对外稿。
- 讲师怎么操作、怎么查证、怎么分工，留在内部，不进方案。
- 给评委、投资人的材料不写内部研发讨论、"本计划书不编造"这类自证句，也不放本地路径、`localhost`、私有仓库（详见[赛事材料](experience/competition-and-investor-materials.md)）。

需要同时交两样时，先给建委内部说明，再单独给一份可以直接转发的干净正文，两者不混排。

**什么时候不用本目录**：只讨论专业知识、给建委看的分析和备忘、纯教学课件、没有对外交付语境的自媒体内容。

## 四、和其他领域怎么组合

对外成品的结构由本目录决定，专业内容由对应领域提供：

- 培训方案 = 本目录（给主办方看）+ [培训](../../training/README.md)（课题和讲法）+ [AI 培训项目](../../../projects/ai-training/README.md)（这一场的受众、时长）
- 产品介绍片脚本 = 本目录 + [视频](../../design/video/README.md)
- 项目策划方案 = 本目录 + 具体项目 README
- 招生宣传 = [自媒体宣传写法](../../self-media/marketing-copy/reader-question-led-promotion.md)主导结构，本目录只提供"不假大空"的约束

## 五、写入

- 一次对外交付做完：这一单的事实写成案例（`case-*.md`），放在它证明的那个方法文件旁边（`experience/` 里）；能用到别的单子上的做法，改对应方法文件的原文。
- 新受众、新场景有了第一次真实经验，就填进上面两张表对应的那一行，不另建目录。
- 新交付格式（比如公益组织版、画册版）有实际需求或建委认可的参考后，写进 [delivery-formats/](delivery-formats/README.md)。
- 项目事实（价格、客户名、合同金额）留在项目目录，不写进这里。
- 其他按[写入规范](../../../../system/repository/ingestion-workflow.md)。旧规则的变化原因见[修订记录](revisions/README.md)。

<!-- generated-methods:start -->
## 按实际需要选择方法

由routes.json生成。先判断本次成品和读者，再按下表实际需要读取方法正文；无需点名作者。多种方法可分工，但同一段不拼接相互冲突的结构。没有适用需求时跳过，不能因看到本表就全部加载。

| 需要解决什么 | 方法正文 | 不适用／保留边界 | 成品怎样检查 |
|---|---|---|---|
| 非技术读者需要理解概念、机制或技术差别，不能只背定义时；主题可以来自提示，也可以来自AI读到的材料 | [从问题推导概念](../../training/experience/technical-explanation/problem-driven-technical-explanation.md) | 纯查询、术语速查、直接操作、已接受稿逐字保护时不展开推导；出版只借解释逻辑，保留出版书面语与编辑规则 | 读者能说出原问题、关键变化及使用判断；不虚构历史发展、事实或作者经历，不混入讲师指令 |
| 向政府、企业或组织方提交培训、课程纲要与项目方案时 | [对外方案内容设计](experience/external-proposal-design.md) | 课堂课件、讲师备课、教程、研究报告和合同不按方案删去其必要信息 | 逐段确认内容、场景和价值；移出提示词、操作路径、内部分工、核验过程与免责话语；检查实际DOCX和来源留存 |
| 政府与企业的培训方案、课程纲要或商业项目方案需要Word排版时 | [政企Word方案排版](delivery-formats/gov-enterprise-word.md) | 法定公文、合同、指定标书模板、画册及其他用户明确视觉要求 | 主副标题居中、深蓝层级、宋体正文、首行缩进；按参考渲染逐页查看，不把参考内容当项目事实 |
<!-- generated-methods:end -->

<!-- generated-related-assets:start -->
## 相关项目与案例

暂无已登记关联；不能据此断言没有未登记材料。
<!-- generated-related-assets:end -->
