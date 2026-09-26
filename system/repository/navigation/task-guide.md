# 按任务读取仓库

<!-- generated-from: routes.json; do not edit -->

主任务决定需要哪种方法，明确项目提供事实；Skill和工具按步骤调用。目录不是读取边界，方法与事实正文都只维护一份。

用户指定文件夹时，先读最近README，再实际读本次方法正文与必要依赖；关键词脚本不是完整阅读器，不以目录列表代替理解。

先核对目标、对象、交付物和项目身份，再选择下面的入口。自然语句匹配仅给候选，不能从同课号、平台或相似主题推定归属。

## 不用用户指定文件的读取步骤

1. 从当前对话提取“要做什么成品、给谁、遇到什么问题、已确认哪个项目”。用户说“参考仓库”时沿用正在做的任务；不能仅将这四个字传给检索器。有多个成品分别处理。
2. 先按下表选择入口。用户指定目录就读该README，再按目的读子目录；指定目录不是禁止跨域补依赖，也不能由工具名称推定项目。
3. 读取适用方法正文后，查看本次材料还有哪些问题未覆盖；用这些问题词检索。搜索结果须核对当前状态、适用/排除条件和来源，再决定采用。不要一次载入整个目录、历史或Skill源码。
4. 制作前完成[执行卡](../execution-checks.md)：实际读过的文件、对应本次动作、最终检查位置。目录标题、命中摘要和路径列表不算已读经验。
5. 已覆盖读者、方法、工具限制、明确项目事实和验收动作就开始做；新问题出现再补读。只在任务目标或关键事实真的缺失时询问，不让用户负责找文件。

本地可运行：`python system/repository/maintenance/context-route.py --task "参考仓库，用秒哒开发大视频上传页面" --pack`。AI可补`--scope work/domains/self-media`限定用户指定的板块；默认推断读/创作/沉淀，也可显式指定`--intent`。此命令只读，不执行其中建议的工具或发布。

输出`read`是必需阅读计划，`discovery`是带片段和行号的待判断候选，`sourcePack`是计划内正文及hash；预算不足的文件明确标为待续读，不截断冒充完整。新正文直接参与检索，无需另建向量库或手动索引。关键词和全文排序不能代替语义判断；不适用方法、历史和原始素材不自动升级成规则。

只有网页访问时，按相同步骤读取根AGENTS、对应README、子目录和方法正文；用仓库文件搜索补查任务词与同义词。无法实际打开的文件列为未读取，不宣称已经参考。没有任何任务描述时，先展示四入口并问要完成什么，不盲读全仓。

| 任务 | 主入口 |
|---|---|
| 有哪些项目、近期工作与业务概要 | [读取](../../../work/projects/README.md) |
| 人物、能力与背书 | [读取](../../../personal/README.md) |
| 建委的思考与判断 | [读取](../../../brain/README.md) |
| 仓库治理、纠错与沉淀 | [读取](../README.md) |
| PPT设计 | [读取](../../../work/domains/design/graphic/ppt/README.md) |
| 海报与平面设计 | [读取](../../../work/domains/design/graphic/poster-fold/README.md) |
| 书籍装帧和版式 | [读取](../../../work/domains/design/graphic/book/README.md) |
| 教师微课与教育交互 | [读取](../../../work/domains/design/video/education/README.md) |
| AE包装与后期合成 | [读取](../../../work/domains/design/video/common/ae-production.md) |
| AI辅助视觉生产 | [读取](../../../work/domains/design/common/ai-assisted-design.md) |
| 视频、动画与生成素材 | [读取](../../../work/domains/design/video/README.md) |
| 企业宣传片 | [读取](../../../work/domains/design/video/promo/README.md) |
| 创赛宣传片制作 | [读取](../../../work/domains/design/video/promo/competition-promo-production.md) |
| 漫剧 | [读取](../../../work/domains/design/video/story/motion-comic.md) |
| 真人故事影片 | [读取](../../../work/domains/design/video/story/README.md) |
| Seedance工具 | [读取](../../../work/domains/design/video/common/tools/seedance/README.md) |
| 网站、应用与编程 | [读取](../../../work/domains/development/README.md) |
| 百度秒嗒平台 | [读取](../../../work/domains/development/tools/miaoda/llms.txt) |
| 查阅、使用或收录Skill | [读取](../../../work/domains/other/skills/README.md) |
| 可编辑参数化React动画 | [读取](../../../work/domains/other/skills/jianwei-ai-community-remotion-video/README.md) |
| Origin可编辑科研图 | [读取](../../../work/domains/other/skills/editaplot/README.md) |
| 按职业设计AI工作台 | [读取](../../../work/domains/other/skills/jianwei-ai-learning-community-workbench/README.md) |
| 个人IP与观点海报 | [读取](../../../work/domains/other/skills/qingyun-ip-poster/README.md) |
| 培训备课与复盘（先核对归属） | [读取](../../../work/domains/training/README.md) |
| 会员社群（仅明确属于本项目） | [读取](../../../work/projects/paid-community-course/README.md) |
| 企业、图书馆、夜校与外部培训 | [读取](../../../work/projects/external-training/README.md) |
| 济南市图书馆：别让Bug打败你 | [读取](../../../work/projects/external-training/lessons/bug-repair/README.md) |
| 出版体裁与书稿（先明确项目） | [读取](../../expression/genres.md) |
| 《飞书高效办公》书籍 | [读取](../../../work/projects/feishu-efficient-office/README.md) |
| 自媒体、个人IP与渠道表达 | [读取](../../../work/domains/self-media/README.md) |
| 产品信息、渠道选择与商业对标 | [读取](../../../work/domains/other/commercial/experience/business-analysis-cards.md) |
| 客户交付、提案、招生或销售 | [读取](../../../work/domains/other/commercial/README.md) |
| 六十甲子项目与独立IP | [读取](../../../work/projects/ai-sixty-jiazi-music-ip/README.md) |
| 言剪AI项目 | [读取](../../../work/projects/yancut-ai/README.md) |
| 当前设备与工具环境 | [读取](../../environment/computers/README.md) |
| 历史项目与追溯 | [读取](history.md) |
| 按课号找资料（先核对所属系列） | [读取](../../../work/domains/training/materials/README.md) |
| 济南市图书馆培训 | [读取](../../../work/projects/external-training/jinan-city-library/README.md) |
| 自媒体标题生成、诊断与评审 | [读取](../../../work/domains/self-media/titles/title-matrix/README.md) |
| AI视频提示词、模板与案例 | [读取](../../../work/domains/design/video/common/awesome-seedance/README.md) |

## 常用板块的继续读取条件

下表与脚本使用同一依赖配置；条件命中后读正文，只查事实不套创作方法。其他板块按各自README继续。

| 主入口 | 条件（任一线索，仍需判断语义） | 用途 | 继续读 |
|---|---|---|---|
| 网站、应用与编程 | 本类任务 | 创作/修改/沉淀 | [正文](../../../work/domains/development/experience/README.md) |
| 百度秒嗒平台 | 本类任务 | 按所查问题 | [正文](../../../work/domains/development/tools/miaoda/disambiguation.md) |
| 百度秒嗒平台 | 本类任务 | 按所查问题 | [正文](../../../work/domains/development/tools/miaoda/README.md) |
| 百度秒嗒平台 | 本类任务 | 创作/修改/沉淀 | [正文](../../../work/domains/development/experience/README.md) |
| 百度秒嗒平台 | 本类任务 | 创作/修改/沉淀 | [正文](../../../work/domains/development/tools/miaoda/experience/README.md) |
| 百度秒嗒平台 | 报错、故障、排错、失败、白屏、踩坑 | 创作/修改/沉淀 | [正文](../../../work/domains/development/tools/miaoda/experience/pitfalls.md) |
| 百度秒嗒平台 | 提示词、开发、搭建、实现、修改、迭代 | 创作/修改/沉淀 | [正文](../../../work/domains/development/tools/miaoda/experience/prompt-patterns.md) |
| 百度秒嗒平台 | 上传、文件传输 | 创作/修改/沉淀 | [正文](../../../work/domains/development/tools/miaoda/experience/prompts/uploads.md) |
| 百度秒嗒平台 | 大视频、大文件、视频上传、分片上传 | 创作/修改/沉淀 | [正文](../../../work/domains/development/tools/miaoda/experience/patterns/large-video-upload.md) |
| 百度秒嗒平台 | 当前、功能、限制、容量、权益 | 按所查问题 | [正文](../../../work/domains/development/tools/miaoda/basics/current-capabilities.md) |
| 百度秒嗒平台 | 登录、认证、验证码、鉴权 | 创作/修改/沉淀 | [正文](../../../work/domains/development/tools/miaoda/experience/prompts/authentication.md) |
| 百度秒嗒平台 | 支付、收款、退款 | 创作/修改/沉淀 | [正文](../../../work/domains/development/tools/miaoda/experience/prompts/payment-integration.md) |
| 百度秒嗒平台 | 报错、故障、排错、无法运行、白屏 | 创作/修改/沉淀 | [正文](../../../work/domains/development/tools/miaoda/experience/prompts/runtime-diagnostics.md) |
| 百度秒嗒平台 | 增量、迭代、回传、回执、验收、审查包 | 按所查问题 | [正文](../../../work/domains/development/tools/miaoda/experience/patterns/codex-miaoda-iterative-increment-workflow.md) |
| 百度秒嗒平台 | Skill、CLI、外部调用、附件、回传、回执、代码仓库、直接查看、直接读取 | 按所查问题 | [正文](../../../work/domains/development/tools/miaoda/development/skill-as-callable.md) |
| 百度秒嗒平台 | 全量、分包、迁移、本地源码 | 按所查问题 | [正文](../../../work/domains/development/tools/miaoda/experience/patterns/codex-source-package-deployment.md) |
| 培训备课与复盘（先核对归属） | 本类任务 | 创作/修改/沉淀 | [正文](../../../work/domains/training/experience/README.md) |
| 培训备课与复盘（先核对归属） | 本类任务 | 创作/修改/沉淀 | [正文](../../../work/domains/training/experience/jianwei-training-style.md) |
| 培训备课与复盘（先核对归属） | 实操、教程、跟做、操作步骤；排除：宣传、朋友圈、招生、只查、查询位置 | 创作/修改/沉淀 | [正文](../../../work/domains/training/experience/tutorial-writing.md) |
| 培训备课与复盘（先核对归属） | 飞书、可视化、图示、图片、口语；排除：宣传、朋友圈、招生、只查、查询位置 | 创作/修改/沉淀 | [正文](../../../work/domains/training/experience/visual-and-oral-training-docs.md) |
| 培训备课与复盘（先核对归属） | 课程结构、课程大纲、演示、场景实操；排除：宣传、朋友圈、招生、只查、查询位置 | 创作/修改/沉淀 | [正文](../../../work/domains/training/experience/demo-driven-course-design.md) |
| 自媒体、个人IP与渠道表达 | 朋友圈、个人IP、个人 IP、建委口吻、我的口吻 | 创作/修改/沉淀 | [正文](../../expression/README.md) |
| 自媒体、个人IP与渠道表达 | 公众号、图文、长文、文章 | 创作/修改/沉淀 | [正文](../../../work/domains/self-media/articles/README.md) |
| 自媒体、个人IP与渠道表达 | 朋友圈 | 创作/修改/沉淀 | [正文](../../../work/domains/self-media/moments-copy/README.md) |
| 自媒体、个人IP与渠道表达 | 群公告、社群话术、群内 | 创作/修改/沉淀 | [正文](../../../work/domains/self-media/community-copy/README.md) |
| 自媒体、个人IP与渠道表达 | 口播、短视频脚本 | 创作/修改/沉淀 | [正文](../../../work/domains/self-media/video-scripts/README.md) |
| 自媒体、个人IP与渠道表达 | 直播销售、带货 | 创作/修改/沉淀 | [正文](../../../work/domains/self-media/live-sales/README.md) |
| 自媒体、个人IP与渠道表达 | 推广、营销、报名页、介绍页、产品介绍、宣传、招生 | 创作/修改/沉淀 | [正文](../../../work/domains/self-media/marketing-copy/README.md) |
| 自媒体、个人IP与渠道表达 | 标题、选题 | 创作/修改/沉淀 | [正文](../../../work/domains/self-media/titles/README.md) |
| 自媒体、个人IP与渠道表达 | 运营、复盘、账号规划、涨粉 | 创作/修改/沉淀 | [正文](../../../work/domains/self-media/experience/README.md) |

## 条件组合

- 实际成品执行[写前约束与最终验收](../execution-checks.md)，记录本次接收者、规则来源、材料覆盖和检查证据；无论最终写入飞书还是本地都适用。
- “产生中文输出”和“写入仓库”分别判断。修改并沉淀课件时，两类规则同时成立；只移动文件不读取整套写作资料。
- 中文输出先用[表达短卡](../../expression/README.md)，按成品选择[体裁标准](../../expression/genres.md)中的一项；简单回答遵守短卡即可。实际专业方法来自对应领域，不能把所有体裁全文一起载入。
- 产品介绍、社群宣传和报名页组合[读者问题方法](../../../work/domains/self-media/marketing-copy/reader-question-led-promotion.md)与明确项目事实；验问题是否值得问、答案是否回应，不把营销问答套进纯教学。
- 培训先分会员社群、外部活动或待归属材料；Bug修复课已确认外训，局部“第6课”不决定系列。教学演示不默认叠加销售。
- 设计统一按交付物进入平面、宣传、教育或故事方向。MG、AE、AI生成是制作方法，单独提MG不等于教师或社群课程。
- 项目位置与来源在[登记表](./projects.json)维护；领域README的相关项目、案例由同一登记生成。状态与结果须回正文核验。
- 书稿按明确项目读取当前章与编辑规则。泛称写书不自动确认就是飞书书；百度秒哒不使用飞书妙搭接口。
- [写入流程](../ingestion-workflow.md)由AI负责更新正文、相关入口、登记、结构及校验；历史、语料和Skill源码只在核验或执行需要时展开。

可用[路由辅助脚本](../maintenance/context-route.py)解释候选与依赖。它不执行工具，也不证明所有AI宿主已读取或遵守规则。

<!-- generated-methods:start -->
## 按实际需要选择方法

由routes.json生成。先判断本次成品和读者，再按下表实际需要读取方法正文；无需点名作者。多种方法可分工，但同一段不拼接相互冲突的结构。没有适用需求时跳过，不能因看到本表就全部加载。

| 需要解决什么 | 方法正文 | 不适用／保留边界 | 成品怎样检查 |
|---|---|---|---|
| 微课需要按教学设计、逐字稿、音频或混合素材组织分镜、参考图、提示词、状态与返工时 | [微课交互式制作工作台](../../../work/domains/design/video/education/interactive-production-workbench.md) | 不适用于创赛宣传片、企业宣传片、普通视频或故事影片；简单微课可用短分镜表，最终成片及多人协作另行验收 | 检查输入素材与画面逐项对应、提示词复制、图片路径、单元锚点、状态反馈和窄屏布局；有音频时再测试时间码与播放，网页打开不能替代交互与成片验收 |
| 页面改版、组件选择、响应式适配、编辑器交互或需要判断界面设计质量时 | [前端 UI 质量标准](../../../work/domains/development/experience/frontend-ui-quality-standards.md) | 纯后端、数据库迁移、命令行脚本或无界面任务 | 读方法正文与目标项目 README；检查 1920/1024/768/390/360 布局；验证加载、失败、触控和键盘状态 |
| 非技术读者需要理解概念、机制或技术差别，不能只背定义时；主题可以来自提示，也可以来自AI读到的材料 | [从问题推导概念](../../../work/domains/training/experience/technical-explanation/problem-driven-technical-explanation.md) | 纯查询、术语速查、直接操作、已接受稿逐字保护时不展开推导；出版只借解释逻辑，保留出版书面语与编辑规则 | 读者能说出原问题、关键变化及使用判断；不虚构历史发展、事实或作者经历，不混入讲师指令 |
| 产品介绍、报名页或购买顾虑说明，需要把整体内容、当前内容和真实价值讲清时 | [用读者问题组织宣传](../../../work/domains/self-media/marketing-copy/reader-question-led-promotion.md) | 纯教学、普通科普、内部复盘不套招生问答；具体价格、权益与已发布状态回项目核对 | 每问影响读者理解或决定；答案直接回应，后一问承接前一答；不是只增加问号 |
| 向政府、企业或组织方提交培训、课程纲要与项目方案时 | [对外方案内容设计](../../../work/domains/other/commercial/experience/external-proposal-design.md) | 课堂课件、讲师备课、教程、研究报告和合同不按方案删去其必要信息 | 逐段确认内容、场景和价值；移出提示词、操作路径、内部分工、核验过程与免责话语；检查实际DOCX和来源留存 |
| 政府与企业的培训方案、课程纲要或商业项目方案需要Word排版时 | [政企Word方案排版](../../../work/domains/other/commercial/delivery-formats/gov-enterprise-word.md) | 法定公文、合同、指定标书模板、画册及其他用户明确视觉要求 | 主副标题居中、深蓝层级、宋体正文、首行缩进；按参考渲染逐页查看，不把参考内容当项目事实 |
| 面向跨岗位学员设计AI工具全景与工作场景实操课程时 | [工具全景到工作场景](../../../work/domains/training/experience/demo-driven-course-design.md) | 单工具进阶课不强制全景；事实查询不读课程方法；方案不含讲师脚本 | 类别帮助选择，提示词连接任务，场景说明熟悉工作与可见成果；本地存储与模型处理分别核对 |
| 收到创赛文稿，需要分析叙事、拆分画面、选择AI／真实素材／AE模板，或调整参考图、人物动作与运镜时 | [创赛宣传片制作](../../../work/domains/design/video/promo/competition-promo-production.md) | 不用于教师微课；不固定所有视频的叙事顺序、设备、蓝色背景或镜头数量，按具体场景借鉴 | 核对文稿与画面、素材及制作分工、定格叠字、参考图文字、人物姿态与机位、连续衔接；提示词和用户完工反馈不代替成片逐镜验收 |
| 为自媒体文章、图文或视频拟发布标题；写公众号等完整文章时即使未点名Skill也用于标题环节；亦可明确调用诊断、评审 | [Title Matrix 标题矩阵](../../../work/domains/self-media/titles/title-matrix/README.md) | 只查资料、只改正文或保留原标题不生成新题；合同、出版章节和学员课件不自动套营销标题；不覆盖文章正文方法 | 实际读Skill和平台参考，逐项对正文核对标题承诺、读者与发布形态；不编实测、数据或资源，不保证点击率；整篇创作交付标题加正文，不强塞矩阵 |
| 实际需要AI生成视频素材、参考图动态化或镜头提示词时；可明确调用，也可按制作环节主动识别，再按镜头意图读具体模板 | [Awesome Seedance 视频提示词方法](../../../work/domains/design/video/common/awesome-seedance/README.md) | 纯AE／Remotion动效、仅口播文案、模型介绍或查询不自动套用；不覆盖片型设计、已验证经验或用户保护范围 | 实际读对应模板和一个锚点；核对主体／动作／镜头／声音、当前模型限制和复测状态；有生成产物才做成片验收，失败回写原项目 |
| 教师委托精品课需要比对文稿、按模板制作PPT、配合真人与网页交互或返修排版时 | [精品课制作与验收](../../../work/domains/design/graphic/ppt/premium-course/workflow.md) | 普通商务汇报与自由风格路演；不套用个案费用、字号和人物区域 | 保护用户改页，核对稿件、模板边界、对齐留白、箭头接缝、动画媒体与网页返回；静态检查不替代成片验收 |
<!-- generated-methods:end -->
