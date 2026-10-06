# AI 读取和写入本仓库的规则

这是杨建委（建委）的长期上下文仓库：他是谁、怎么想、会做什么、在做什么。任何 AI（GPT、Claude、GLM、Gemini 等，不论哪个版本）接到建委的任务都按本页执行。本页是唯一入口，读完本页就知道下一步读什么，不需要运行脚本。本页的规则对所有模型一样，不因为换了模型就换一套做法。

## 一、读取：接到任务怎么找经验

### 第 1 步：弄清楚要交付什么

从对话里提取：**交付什么东西、给谁看、用在哪里**。建委说"看我的仓库，帮我……"时，后半句就是任务。建委指定了目录，就从那个目录开始，但仍按下表补齐必要的文件。

### 第 2 步：按下表读文件

表里的文件都要读完正文，只看标题或目录不算读过。一个任务同时属于几行时，每行都读。

表里找不到对应的任务时：打开 [work/domains/README.md](work/domains/README.md) 和 [work/projects/README.md](work/projects/README.md)，按领域和项目名找最接近的目录，读它的 README；再用任务里的关键词搜仓库。实在找不到，照常完成任务，并告诉建委"仓库里没找到相关经验"，不要编造"仓库里说……"。

| 任务 | 必读 |
|---|---|
| 准备演讲 / 对外分享 / 外出分享 / 主题分享 / 分享稿 | [培训入口](work/domains/training/README.md) + [课程组织中的演讲与分享方法](work/domains/training/experience/demo-driven-course-design.md#演讲与对外分享问题含义现实事例可灵活) + [口语样稿](system/expression/voice-samples.md)；主动评估三层结构，不要求点名、不强制采用，商业路演与销售仍由对应领域主导 |
| 写培训**课件** / 分享资料 / 课堂文档 | [培训入口](work/domains/training/README.md) → [培训风格](work/domains/training/experience/jianwei-training-style.md) + [口语样稿](system/expression/voice-samples.md) + [课程组织](work/domains/training/experience/demo-driven-course-design.md)；飞书课件加读[可视化与口语化](work/domains/training/experience/visual-and-oral-training-docs.md) |
| 写培训**方案 / 大纲**（给主办方） | [常讲课题](work/domains/training/topics.md) + [对外方案写法](work/domains/training/experience/external-proposal-design.md) + [内外稿边界](work/domains/other/commercial/experience/external-deliverable-language.md)；要 Word 加读[政企 Word 排版](work/domains/other/commercial/delivery-formats/gov-enterprise-word.md) |
| 写实操教程 | [教程写法](work/domains/training/experience/tutorial-writing.md) |
| 公众号 / 图文文章 | [自媒体入口](work/domains/self-media/README.md) → [文章](work/domains/self-media/articles/README.md) + [标题](work/domains/self-media/titles/README.md) |
| 宣传、招生、产品介绍、报名页 | [宣传写法](work/domains/self-media/marketing-copy/reader-question-led-promotion.md) + [口语样稿](system/expression/voice-samples.md) + 对应项目的事实 |
| 朋友圈 / 社群话术 / 口播 / 直播 | [自媒体入口](work/domains/self-media/README.md) 里对应的那一类 + [口语样稿](system/expression/voice-samples.md) |
| 平面设计：PPT、海报、折页、书籍 | [设计入口](work/domains/design/README.md) → 对应交付物目录 |
| 视频：宣传片、微课、故事片、AI 视频提示词 | [视频入口](work/domains/design/video/README.md) → 对应片型目录；要写视频提示词再读 [Seedance](work/domains/design/video/common/seedance/README.md) |
| 用百度秒哒开发 | [秒哒入口](work/domains/development/tools/miaoda/README.md)（先看顶部平台识别）→ 按其中的流程表选一条 |
| 其他网站 / 应用 / 编程 | [开发入口](work/domains/development/README.md) + [通用开发经验](work/domains/development/experience/README.md) |
| PPT、创赛AE视频、教学交互及修改费用报价 | [报价入口](work/domains/other/commercial/quotations/README.md)：先核对对象、范围和价格状态，再查个人基准 |
| 商业计划、比赛申报、路演、融资；跨行业报价、正式文书和对外表达标准 | [商业化入口](work/domains/other/commercial/README.md)：先判断业务归属，再选需要引用的通用标准；具体培训、设计等流程读对应领域 |
| 某一场培训（济南干部培训、济南市图书馆等） | [AI 培训项目](work/projects/ai-training/README.md) → [场次索引](work/projects/ai-training/sessions-index.md) → 该场次 README |
| 某个具体项目（社群、言剪、飞书书、六十甲子） | [项目列表](work/projects/README.md) → 该项目 README |
| 个人简介、讲师介绍、简历 | [个人信息](personal/README.md)；荣誉和数字只按[背书表](personal/credentials.md)写 |
| 建委的想法、偏好、判断方式 | [建委大脑](brain/README.md)；做任何成品前都值得先看一眼[做事与表达偏好](brain/preferences.md) |
| 用 Skill | [Skill 库](work/domains/other/skills/README.md) |
| 电脑、网络、本机工具 | [设备环境](system/environment/README.md) |
| 往仓库里写东西 | 本页第二部分 + [写入规范](system/repository/ingestion-workflow.md) |

**常见的组合任务**（主导方决定整体结构，其他方只提供内容）：

| 组合 | 谁主导结构 | 其他方提供什么 |
|---|---|---|
| 培训宣传文章（有干货也要招生） | 自媒体宣传写法 | 培训：干货内容和课题；项目：课程事实、权益 |
| 培训方案（给主办方） | 培训：接洽、方案与课程设计 | 商业化只提供通用内外稿和文书标准；场次记录提供受众、时长 |
| 培训课件里需要演示视频或做个小工具 | 培训：课件 | 设计或开发：制作方法（只用在那一段） |
| 自媒体内容讲 AI 技术 | 自媒体 | 培训：[技术概念讲法](work/domains/training/experience/technical-explanation/problem-driven-technical-explanation.md) |
| 秒哒开发项目（如言剪） | 秒哒流程 | 项目：当前进度和要求；通用开发经验：测试、UI、后端 |
| 培训＋自媒体＋商业化一起（比如一场付费公开课的招生文章） | 自媒体宣传写法 | 培训：课程讲什么；商业化：[对外表达不假大空](work/domains/other/commercial/experience/external-deliverable-language.md)；项目：价格与权益 |

组合时的做法：先定"主导方"，用它的结构写；其他方只借具体内容放进对应段落，不要把几套结构拼在一起。先按业务、技能与行业确定主导领域，再按受众选择需要引用的通用标准。培训接洽与大纲由培训主导，精品课拆页与合并由设计主导；不能因出现客户、预算、采购就改由商业化主导。跨行业商业计划、合同、报价和通用对外表达才进入商业化；宣传内容仍按对应渠道的方法组织。

### 第 3 步：读到的经验有冲突时

按这个顺序，前面的优先：

1. 建委这次对话里的明确要求
2. 项目里的当前事实（价格、进度、已定内容）
3. 标了"红线"的规则
4. 领域里的默认做法
5. 外部参考、旧记录

规则分三级：

- **红线**：不能违反，比如给学员的课件不写讲师安排、荣誉数字不能编、百度秒哒不用飞书妙搭的接口。
- **默认**：没有特别理由就照做。
- **可灵活**：看具体场景判断，比如课件里用生图还是现场演示，由知识点决定。

没有标级别的，按"默认"处理。默认和可灵活的规则，只要本次场景有更好的做法就可以变通，但要跟建委说一句为什么这样做。

### 第 4 步：交付前自查，并告诉建委用了什么

把读到的红线逐条对照成品检查一遍（方法见[成品自查](system/repository/execution-checks.md)），再交付。交付时用一两句话告诉建委：这次读了仓库里哪几个文件、用了哪几条经验、有没有哪条没照做以及原因。这一步不能省，建委靠它判断经验有没有被用上。

### 容易混淆的地方（红线）

- **百度秒哒 ≠ 飞书妙搭。** 建委说"秒哒""秒嗒"、网址含 miaoda.cn 或 appmiaoda.com，都是百度秒哒。**不要**调用 lark-apps、lark-cli apps、Spark 这些飞书妙搭的工具和接口。只有明确出现"飞书妙搭"或 miaoda.feishu.cn 时才是飞书的产品。
- **培训 ≠ 会员社群。** 企业、机关、图书馆、夜校的培训属于 [AI 培训项目](work/projects/ai-training/README.md)；课号只在自己的系列里有效。
- **给学员的 ≠ 给讲师的 ≠ 给主办方的。** 同一场培训，课件、备课稿、方案是三种东西，分开写。
- **教师委托做的微课、精品课**属于设计，不属于建委讲课。
- **飞书文档链接**不代表是《飞书高效办公》这本书。

## 二、写入：往仓库里沉淀经验

建委说"沉淀一下""记到仓库""这些是培训的经验，沉淀到培训板块"时执行这部分。**建委只说一句话，拆分和归位由 AI 完成**：把内容拆成事实（写项目或场次）、案例（`case-*.md`，放在它证明的方法旁边）、方法（改领域里的方法原文），写完告诉建委每样放到了哪个文件。详细步骤见[写入规范](system/repository/ingestion-workflow.md)。核心规则：

1. **先找已有位置。** 先搜仓库里有没有讲同一件事的文件。有就改那一处：补充、修正或替换过时内容。不要另起新文件，也不要在末尾追加一条意思相近的新规则。
2. **写清楚，不要压缩成口号。** 每条经验写明：什么场景、怎么做、一个正例或反例、为什么。"注意口语化"这种一句话规则没法执行；要写"像这样说，不要像那样说"。
3. **标级别。** 新规则标上红线、默认或可灵活。
4. **领域归属先于商务环节。** 有明确行业或业务属性的接单、制作、客户确认与交付SOP归对应领域，入口按总类、子类、具体方法组织。商业化集中维护跨领域通用标准，不收拢全部对外业务流程。**事实和方法分开放。** 某个项目的事实（价格、进度、客户）放项目；能用到别处的做法放领域。一件事两样都有，就各写一部分，互相加链接。
5. **新建目录或新分类，先问建委。** 问的时候同时给两个方案：A. 放进已有的哪个位置；B. 新建什么、叫什么。并说明理由。建委同意后再建。**例外**：建委已经点名了位置和名字（如"在微课与教育交互下建一个精品课板块"），直接建，并且板块里必须有方法文件，不能只堆案例。不建"合集""其他""杂项"这类汇总文件夹。
6. **过时的内容直接改掉或删掉。** 不要新旧并列，Git 历史能找回旧版本。不再单独写"修订记录"文件，除非改的是整个仓库的结构。
7. **同步索引。** 新增、移动、删除文件后，更新最近一层 README 的目录。移动文件后运行 `python system/repository/maintenance/relink.py 旧路径=新路径` 修正链接。
8. **校验后再推送。** 运行 `python -B system/repository/maintenance/sync-navigation.py`、`sync-structure.py`、`validate-context.py`，没有错误再提交。

**建委大脑自动提炼（任何对话都适用，不需要建委说"存进大脑"）**：建委在对话里自己说出观点、判断标准、偏好或做事原则时，判断一次要不要写进 [brain/](brain/README.md)：只取建委本人说的或明确认可的；只写抽象原则，不写项目细节；先查重，已有就不写、相近就改进原条目；和已有条目矛盾时先问建委再替换；随口一说、带情绪的不存。存了什么，在回复末尾用一句话告诉建委。细则见[写入规范](system/repository/ingestion-workflow.md#建委大脑自动提炼)。

凭据、Token、密码不入库。文件用 UTF-8、LF 换行、英文小写短横线命名。

## 三、发布

<!-- publish-policy: direct-main-no-pr -->

写入完成后直接提交并推送到 main，不开 PR，不建临时分支让建委合并。远端有新提交时先拉取合并，不覆盖别人的改动。推送后确认远端已包含本次提交，并把 GitHub 链接发给建委。

本地仓库启用 Git hooks（`git config core.hooksPath system/repository/maintenance/git-hooks`）后，每次提交会自动更新桌面上的"GitHub仓库完整结构.html"。建委靠这个页面看仓库，不能关掉。

## 其他入口

- 人看的首页：[README](README.md)
- 完整文件结构：[STRUCTURE](system/repository/navigation/STRUCTURE.md)
- 中文表达的通用要求：[表达短卡](system/expression/README.md)
- 仓库维护工具：[maintenance](system/repository/maintenance/README.md)
