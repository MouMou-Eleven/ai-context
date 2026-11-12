# 2026-11-13 第八轮整改：仓库越用越好用，红线收紧

## 为什么改

前七轮主要解决“该读的没读到”。建委指出更大的问题是：规则越写越多，读过了照样做不到，做到了也不一定好看；仓库要像模型训练一样，从每次真实使用里拿到对错信号，越用越强，而不是越来越长的备忘录。

## 改了什么

| 文件 | 做了什么 |
|---|---|
| [进化机制](../evolution.md)（新） | 三类失败（A 没读到、B 读了没做到、C 照做了仍不好）各自的治法；使用日志；建委纠正或认可时先记观察；观察升成通用规则的五条准则（AI 自己判断）；规则改写、降级、撤掉；少而典型的正反例；按内容量升级 |
| [使用日志](../usage-log.md)、[观察记录](../observations.md)（新） | 两张表。观察里先放进本机记忆中言剪AI宣传片、精尺匠造创赛片的 8 条原始反馈，状态都是待定 |
| [建委审美标尺](../../../work/domains/design/common/design-principles/taste-benchmarks.md)（新） | 建委认可过的成品作同类活儿的下限，加 15 对真实的正反例，原话都来自仓库已有的返修记录 |
| [evolution-status.py](../maintenance/evolution-status.py)、[test_evolution.py](../maintenance/tests/test_evolution.py)（新） | 按日志和观察判断该不该升级；Claude Code 开新对话时自动运行，到期才提醒 |
| [成品自查](../execution-checks.md) | 开工时抄本单检查单；正式交付前请一个全新的审查者，只给成品、要求和检查单 |
| [AGENTS](../../../AGENTS.md)、[写入规范](../ingestion-workflow.md) | 红线重新定义；交付后记日志、跑升级状态；纠正和认可先记观察；新规则只标默认或可灵活 |
| [content-guards.py](../maintenance/content-guards.py)、[validation-policy.json](../maintenance/validation-policy.json) | 记下每个文件整改后的红线数（`redlineBudget`），任何文件的红线变多就拦下提交，包括项目和案例文件 |
| 各领域文件 | 89 处红线降为默认（见下表），标题变化带来的 41 个失效链接已同步修正，另修了 1 个原本就失效的链接 |

## 红线的新范围

只留违反了、改稿也补不回来的事：编造事实；把内部内容交给外部的人；虚报做到了哪一步；用错平台；动线上数据、删改别人亲手改过的成果；泄露凭据；违反许可。**新的红线只有建委能定**，AI 觉得重要的规则标默认，并写进检查单。降为默认不等于不重要：没有特别理由照样要做，能在成品上核对的，仍在各领域的检查表、验收表里逐行查。

## 请建委确认（9 条）

拿不准的都没有擅自定：建委定过或可能定过的，保持红线不动；只是强调过的，降为默认但列在这里。建委说一句“第几条降”或“第几条恢复”就改。

| 位置 | 内容 | 现在 | 为什么请建委定 |
|---|---|---|---|
| work/domains/design/graphic/ppt/premium-course/workflow.md:50 | 封面保护：只改课程标题，其余原样保留 | 仍是红线 | 建委当时亲口定为红线；按新范围属于改稿能补回的事 |
| work/domains/design/graphic/ppt/premium-course/workflow.md:52 | 片头 5 秒静止、无声 | 仍是红线 | 建委当时亲口定为红线；按新范围属于改稿能补回的事 |
| work/projects/README.md:25 | 作品集网站与言剪AI是两个独立项目 | 仍是红线 | 建委当时亲口定为红线；按新范围属于改稿能补回的事 |
| work/domains/design/video/promo/competition/ae-template-layout.md:70 | - 画面里不能有任何闪：发现就修，光效引起的就删光效（红线）。 建委原话：“… | 仍是红线 | 本机记忆里这条标着“红线，2026-11-07”，查不到是建委定的还是 AI 标的；按新范围属于改稿能补回的事 |
| work/domains/design/video/promo/competition/ai-code-ae-pipeline.md:106 | 建委按画面给了模板，就每个画面用它对应的模板做（红线）。 建委常按“第N幕画… | 仍是红线 | 同上，本机记忆里标着“红线，2026-11-07”（第14—15幕被批“完全是错的”） |
| work/domains/development/industry-cases/education/tianjin-agent-contest/platform/build-sop.md:54 | 六、生成评审链接（红线） | 仍是红线 | 不在红线的几类里，但评审链接一旦交出去错了就补不回来；保留还是降，请建委定 |
| work/domains/design/video/promo/competition/ai-code-ae-pipeline.md:104 | 只改、只渲模板里对应的那一段（红线）。 一个 AE 模板通常 40 多秒，是… | 已降为默认 | 建委 2026-11-04 说过“一定要记住，后面不再反复提醒”，但没说是红线；要恢复就说一句 |
| brain/preferences.md:29 | - 讲 AI 培训从自己的长处出发（红线）。 建委的长处是善用 AI，能借 … | 已降为默认 | 建委反复强调的讲课定位；讲偏了能改，所以降了；要恢复就说一句 |
| work/domains/training/experience/jianwei-training-style.md:29 | 先站对位置：从“怎么用 AI 驾驭它”出发，不从软件专家的角度讲（红线） | 已降为默认 | 和上一条是同一条规则的执行细则，跟着上一条定 |

另外请看一眼下面“保留的红线”：有不该算红线的，或者“降为默认”里有该保留的，直接说。

## 保留的红线（35 处）

| 位置 | 内容 | 为什么是红线 |
|---|---|---|
| AGENTS.md:83 | - 红线：违反了，改稿也补不回来的事，不能违反。只有这几类：编造事实（荣誉、… | 红线定义本身 |
| AGENTS.md:99 | - 百度秒哒 ≠ 飞书妙搭（红线）。 建委说"秒哒""秒嗒"、网址含 mia… | 用错平台 |
| system/environment/computers/desktop-1/disk-cleanup-and-codex-storage.md:14 | Codex 任务生成的工作产物  与聊天记录独立。2026-09-29 至 … | 误删聊天记录，删了找不回 |
| system/environment/computers/desktop-1/disk-cleanup-and-codex-storage.md:106 | 红线：下面是已部署的后续方案，不能写成已经迁完。下次先读 F:/CC-Swi… | 虚报迁移进度 |
| system/environment/computers/desktop-1/disk-cleanup-and-codex-storage.md:289 | 红线：清理或同步时，不能按“实时 threads 索引不存在”删除 roll… | 误删聊天记录，删了找不回 |
| work/domains/design/common/ai-generation-principles.md:31 | 5. 分清提示词、风格和成品（红线） | 虚报做到了哪一步 |
| work/domains/design/common/feedback-iteration.md:25 | 5. 只改授权的范围（红线） | 删改别人亲手改过的成果 |
| work/domains/design/graphic/ppt/premium-course/workflow.md:23 | 页数合并的判断（红线与默认） | 靠隐藏凑页数等于虚报（标题“红线与默认”，红线只指第一句） |
| work/domains/design/video/promo/competition/ae-template-layout.md:85 | - 签名、证书、标识用客户给的真实素材，不用字体模拟（红线）。 建委给了签名… | 签名、证书不能伪造（编造事实） |
| work/domains/development/experience/backend-auth-payment.md:26 | 密钥（红线） | 泄露凭据 |
| work/domains/development/experience/delivery-and-testing.md:7 | 证据分三级，不能混（红线） | 把没验证的说成验证过（虚报） |
| work/domains/development/industry-cases/education/subject-integration/classroom-agent-design.md:136 | 十二、知识依据与角色边界（红线） | 知识依据与角色边界：编造知识、越权 |
| work/domains/development/industry-cases/education/tianjin-agent-contest/document-format.md:5 | 一、读者是评委（红线） | 内部内容交给评委 |
| work/domains/development/industry-cases/education/tianjin-agent-contest/document-format.md:97 | 模板里的空要分两类：作品内容的空由我们按项目填好，人员身份的空才留给客户（红… | 替客户编造人员身份 |
| work/domains/development/industry-cases/education/tianjin-agent-contest/submission-package.md:53 | - 工作提示只放第三个文件夹（红线）：填报提醒、"姓名待客户填"、录屏预设问… | 工作提示交给评委（内部内容外发） |
| work/domains/development/tools/miaoda/README.md:5 | 先确认平台（红线） | 用错平台 |
| work/domains/development/tools/miaoda/basics/platform-basics.md:56 | 红线：本地优先项目改用远程渲染前，要明确上传哪些素材、保存多久及删除方式，获… | 未经授权上传原片、花钱（违反授权） |
| work/domains/development/tools/miaoda/topics/backend-storage.md:7 | 一、动数据库之前，先判断应用处在哪种状态（红线） | 动线上数据库 |
| work/domains/development/tools/miaoda/topics/backend-storage.md:25 | 二、哪些改动是破坏性的（红线） | 破坏性改动线上数据 |
| work/domains/development/tools/miaoda/workflow.md:18 | 红线：已经有本地基线的项目，即使暂时拿不到云端最新改动，也不要退回路径 C … | 让秒哒自由重写会覆盖已有成果 |
| work/domains/development/tools/miaoda/workflow.md:143 | 数据库迁移（红线）：迁移只做加法、可以重复执行；删列、改名、改类型单独成包，… | 动线上数据库 |
| work/domains/other/commercial/README.md:26 | 对外成品的底线（红线） | 对外成品不编造、不外泄 |
| work/domains/other/commercial/experience/competition-and-investor-materials.md:29 | 评审成品中的空白字段与填写提示（红线） | 内部填写提示交给评委 |
| work/domains/other/commercial/quotations/method.md:16 | - 红线：标注价格状态。 用户亲述基准、历史个案、AI建议、已确认报价、实际… | 把估价写成成交（编造事实） |
| work/domains/other/skills/anything2explainer/README.md:5 | 许可（红线） | 违反许可 |
| work/domains/self-media/experience/media-growth.md:24 | 把人接到下一步（红线＋默认） | 标题“红线＋默认”，红线只指下一行 |
| work/domains/training/experience/jianwei-training-style.md:108 | 真实软件界面、按钮、路径、价格、操作结果  真实截图（红线 3：不用 AI … | 用 AI 生图仿造软件界面（编造事实） |
| work/domains/training/experience/jianwei-training-style.md:129 | 红线 1：学员视角，不写讲师安排。 正文、标题、表头、提示框里都不出现时长（… | 内部讲师安排交给学员 |
| work/domains/training/experience/jianwei-training-style.md:147 | 红线 2：保护建委的成果。 局部改，不整篇覆盖；必须整篇重写时，先完整备份当… | 删改建委亲手改过的成果 |
| work/projects/README.md:11 | 接手项目先核对身份（红线） | 接手错项目会改坏别人的代码和部署 |
| work/domains/development/tools/miaoda/topics/runtime-diagnostics.md:13 | 红线：源码、检查、产物生成、部署和浏览器验收分别报告。不能把 lint 通过… | 部署进度分开报告，不把部分通过写成全部生效（虚报进度） |
| work/domains/development/industry-cases/education/tianjin-agent-contest/platform/build-sop.md:38 | 四、验收：六个状态分开记（红线） | 把前一个状态当成后一个，就是虚报做到了哪一步 |
| work/domains/self-media/experience/media-growth.md:31 | - 红线：不承诺还没准备好的资料，不做标题党引流；价格、权益、边界只按具体项… | 只留“不承诺没准备好的资料”（对外承诺失实）；“不做标题党”移到默认 |
| work/domains/design/graphic/ppt/ai-assisted-design/workflow.md:7 | 红线：内容正确、文字可编辑、资源来源真实、用户最新改稿受到保护。参考图不能代… | 只留内容正确、资源真实、保护用户最新改稿、不虚报放映；“文字可编辑”移到默认 |
| AGENTS.md:101 | 给学员的 ≠ 给讲师的 ≠ 给主办方的 | 内部内容交给外部的人（原来在“容易混淆的地方（红线）”整节下，这次单独标出） |

## 降为默认（89 处）

行号是整改当时的位置。

| 位置 | 内容 | 为什么能降 |
|---|---|---|
| system/repository/ingestion-workflow.md:7 | 第零步：确认在最新的仓库上写（红线） | 写仓库的做法，写错了能改回；“拉最新”另有提交检查兜底 |
| system/repository/ingestion-workflow.md:80 | 一条规则只有一个家（红线） | 写仓库的做法，写错了能改回；“拉最新”另有提交检查兜底 |
| system/repository/ingestion-workflow.md:104 | 2. 案例（这次怎么做的、出了什么问题、怎么改的）→ 按案例模板，文件名 c… | 写仓库的做法，写错了能改回；“拉最新”另有提交检查兜底 |
| system/repository/ingestion-workflow.md:128 | 板块要有总有分，不留零散的点（红线） | 写仓库的做法，写错了能改回；“拉最新”另有提交检查兜底 |
| system/repository/ingestion-workflow.md:139 | 比赛怎么沉淀（红线） | 写仓库的做法，写错了能改回；“拉最新”另有提交检查兜底 |
| system/repository/ingestion-workflow.md:185 | 从一个项目里提炼：写给下一个不同的项目（红线） | 写仓库的做法，写错了能改回；“拉最新”另有提交检查兜底 |
| system/repository/templates/case.md:5 | 按一类任务写，不按单个对象写（红线）：标题写“这一类任务学到什么”（例：“实… | 写仓库的做法，写错了能改回；“拉最新”另有提交检查兜底 |
| work/domains/design/common/ai-generation-principles.md:7 | 1. 精确信息交给后期（红线） | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/common/ai-generation-principles.md:27 | 4. 只引用真实存在的素材（红线） | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/common/code-driven-video/README.md:7 | 什么时候读（红线） | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/common/code-driven-video/README.md:33 | 复用的是手法，不是样式（红线） | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/common/code-driven-video/layout-and-sizing.md:46 | 容器跟着内容走（红线） | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/common/code-driven-video/motion-and-verification.md:17 | 转场（红线） | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/common/code-driven-video/motion-and-verification.md:53 | 验收流程（红线） | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/common/design-principles/aesthetic-vocabulary.md:33 | 防止生搬硬套（红线） | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/common/feedback-iteration.md:11 | 2. 分清保留什么、改什么（红线） | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/common/production-workflow.md:18 | 交付物判断（红线） | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/graphic/ppt/ai-assisted-design/layout-and-pagination.md:14 | 一之二、教学PPT上屏的是课堂知识点（红线） | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/graphic/ppt/ai-assisted-design/layout-and-pagination.md:109 | 五、先选合适的框，不把素材拉成需要的形状（红线＋默认） | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/graphic/ppt/ai-assisted-design/workflow.md:47 | 5. 交给Codex重建分层素材和原生文字（红线＋默认） | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/graphic/ppt/ai-assisted-design/workflow.md:92 | 模板约束（红线）： 内容只进入模板留出的区域，字体字号、色带和标识沿用模板；… | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/graphic/ppt/premium-course/animation-and-geometry.md:39 | 擦除方向要用视频抽帧核对（红线） | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/graphic/ppt/premium-course/animation-and-geometry.md:59 | 在已有动画的页插视频（红线） | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/graphic/ppt/premium-course/recording-guide.md:40 | 页面只保留这些（红线） | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/graphic/ppt/premium-course/recording-guide.md:63 | 句子归页与点击时机（红线） | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/graphic/ppt/premium-course/recording-guide.md:84 | 不要放进去的东西（红线） | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/graphic/ppt/premium-course/recording-guide.md:97 | 一屏看完，键盘操作（红线） | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/graphic/ppt/premium-course/recording-guide.md:119 | 单文件离线，发给谁都能用（红线） | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/graphic/ppt/premium-course/workflow.md:54 | 正文模板（红线）： 内容只进入指定空白区域，字体字号、上下色带和标识沿用当前… | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/video/README.md:10 | AI 自己动手剪辑、包装、加效果、出成片时（红线），不管用户有没有说用代码，… | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/video/common/code-rendered-animation/workflow.md:21 | - 所有动画只由时间 t 决定（红线）。 任何位置、角度、透明度都写成 t … | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/video/common/seedance/README.md:14 | 几条红线 | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/video/promo/competition/ae-template-layout.md:7 | 怎么用本文件（红线） | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/video/promo/competition/ae-template-layout.md:18 | 先设计版面，再用模板去实现（红线） | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/video/promo/competition/ae-template-layout.md:25 | - 模板自带的文字组件必须用上，改字改色，不自己另画（红线）。 模板的标题框… | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/video/promo/competition/ae-template-layout.md:35 | 模板是拿来用的素材和手法，不是填空题（红线）。 建委给模板、给素材，要的是：… | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/video/promo/competition/ae-template-layout.md:62 | - 底部给字幕留一行，不留一大片（红线）。 建委会在剪映里给每条宣传片加一行… | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/video/promo/competition/ae-template-layout.md:67 | - 新加的图层要和同一段原有图层的开关一致（红线）。 加完图层，先把同一个合… | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/video/promo/competition/ae-template-layout.md:83 | - 人像按原图完整显示头和肩，不裁成大脸（红线）。 换人像时按“铺满模板的窗… | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/video/promo/competition/ae-template-layout.md:102 | - 证书和边框严丝合缝：框按证书比例自动收拢，不留衬底空白（红线）。 证书模… | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/video/promo/competition/ae-template-layout.md:107 | - 调色不能把素材调白：渲染后的证书、照片颜色要和原图一致（红线）。 模板常… | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/video/promo/competition/ae-template-layout.md:110 | - 同一画面里一份素材只出现一次（红线）。 照片墙、多图卡片画面，建委看到同… | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/video/promo/competition/ae-template-layout.md:117 | - 一叠东西作为一叠入场，展开前后要是同一叠（红线）。 协议、证书这种一摞纸… | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/video/promo/competition/ae-template-layout.md:121 | 排版验收（红线） | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/video/promo/competition/ae-template-layout.md:125 | 先用眼睛审，再用数字量（红线）。 下面的表只能抓出“量得出的错”，抓不出“不… | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/video/promo/competition/ai-code-ae-pipeline.md:26 | 3. 改模板是“用模板的元素实现设计好的版面”，不是往模板占位里填字（红线）… | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/video/promo/competition/ai-code-ae-pipeline.md:27 | 4. 交给建委前先自己验收（红线）。 开工时把排版验收整张表复制成本单检查单… | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/video/promo/competition/ai-code-ae-pipeline.md:83 | 6. 模板颜色统一成全片主色（红线）。 建委找模板只看效果，颜色常不统一，有… | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/video/promo/competition/ai-code-ae-pipeline.md:94 | - 改完先存盘，再复制渲染副本；成片要和工程同一帧对照（红线）。 aeren… | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/video/promo/competition/ai-code-ae-pipeline.md:107 | - 模板的运镜和节奏不要擅自改（红线）。 建委选模板就是选它的效果：照片墙“… | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/video/promo/competition/ai-code-ae-pipeline.md:117 | - 首尾都要留出画面余量（红线）。 建委拿到片段后要在剪映里自己分配时长，片… | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/video/promo/competition/ai-code-ae-pipeline.md:169 | - 频闪要逐帧查亮度跳变，不只查黑帧（红线）。 要求（发现就修、光效引起的删… | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/video/promo/competition/ai-code-ae-pipeline.md:173 | - 找真正的闪的层：逐层开关、比每帧 RGB 均值，不凭猜（红线）。 第 1… | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/video/promo/competition/ai-code-ae-pipeline.md:185 | AE 级包装的标准（红线） | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/video/promo/competition/ai-code-ae-pipeline.md:228 | 3. 能检查的新规则，必须同时进验收表（红线）。 规则写进正文只管“知道”，… | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/video/promo/competition/competition-promo-basics.md:17 | 先定这次交付什么（红线） | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/video/promo/enterprise/info-shots.md:5 | 先把一段话拆成一类一镜（红线） | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/design/video/promo/enterprise/prompt-iteration.md:46 | 3. 引用只写当前工具支持的（红线） | 设计与制作做法，违反了返修能改好；能核对的已在检查表或验收表里逐行查 |
| work/domains/development/experience/backend-auth-payment.md:20 | 签名与加密（红线） | 工程做法，违反了能重做；数据库、密钥、平台类仍是红线 |
| work/domains/development/experience/creative-frontend-prompt-patterns.md:81 | 11. 视觉红线 | 工程做法，违反了能重做；数据库、密钥、平台类仍是红线 |
| work/domains/development/experience/delivery-and-testing.md:17 | 干净目录复建（红线） | 工程做法，违反了能重做；数据库、密钥、平台类仍是红线 |
| work/domains/development/industry-cases/education/README.md:10 | 一个比赛一个文件夹（红线）。 以后有别的省份、别的智能体比赛，按建委的安排在… | 仓库写入位置的约定，写错了能挪 |
| work/domains/development/industry-cases/education/README.md:24 | 写入规则（红线） | 仓库写入位置的约定，写错了能挪 |
| work/domains/development/industry-cases/education/tianjin-agent-contest/README.md:13 | 本文件夹里的规定和手法只对这个比赛成立（红线）：别的比赛、别的视频即使看起来… | 比赛材料的写法和自检，交付前能改好；“工作提示外发”“替客户填身份”两条仍是红线 |
| work/domains/development/industry-cases/education/tianjin-agent-contest/demo-video.md:22 | 二、逐字稿（红线） | 比赛材料的写法和自检，交付前能改好；“工作提示外发”“替客户填身份”两条仍是红线 |
| work/domains/development/industry-cases/education/tianjin-agent-contest/demo-video.md:54 | 4.1 复用的是手法，不是样式（红线） | 比赛材料的写法和自检，交付前能改好；“工作提示外发”“替客户填身份”两条仍是红线 |
| work/domains/development/industry-cases/education/tianjin-agent-contest/demo-video.md:68 | - 文字不能被裁（红线）：开场页、报告、全文这类成段文字，取景宽度必须覆盖整… | 比赛材料的写法和自检，交付前能改好；“工作提示外发”“替客户填身份”两条仍是红线 |
| work/domains/development/industry-cases/education/tianjin-agent-contest/demo-video.md:70 | 4.3 标注：框要准，文字不压内容（红线） | 比赛材料的写法和自检，交付前能改好；“工作提示外发”“替客户填身份”两条仍是红线 |
| work/domains/development/industry-cases/education/tianjin-agent-contest/demo-video.md:90 | 4.5 转场（红线） | 比赛材料的写法和自检，交付前能改好；“工作提示外发”“替客户填身份”两条仍是红线 |
| work/domains/development/industry-cases/education/tianjin-agent-contest/demo-video.md:100 | 4.7 出片前自检（红线） | 比赛材料的写法和自检，交付前能改好；“工作提示外发”“替客户填身份”两条仍是红线 |
| work/domains/development/industry-cases/education/tianjin-agent-contest/demo-video.md:127 | 逐字稿  旁白书面化、比喻听不懂、结尾澄清；改法见第二节表格  红线  数学… | 比赛材料的写法和自检，交付前能改好；“工作提示外发”“替客户填身份”两条仍是红线 |
| work/domains/development/industry-cases/education/tianjin-agent-contest/demo-video.md:129 | 画面标注  框按测量时刻的坐标画，滚动后落在空白或别的话上；改为模板匹配跟踪… | 比赛材料的写法和自检，交付前能改好；“工作提示外发”“替客户填身份”两条仍是红线 |
| work/domains/development/industry-cases/education/tianjin-agent-contest/demo-video.md:130 | 画面标注  框上的标签压住文字、骑在面板边上；改为自动选位，放不下就去掉（见… | 比赛材料的写法和自检，交付前能改好；“工作提示外发”“替客户填身份”两条仍是红线 |
| work/domains/development/industry-cases/education/tianjin-agent-contest/demo-video.md:133 | 转场  片头标题压在聊天面板上、前后两组卡片同时出现（见 4.5）  红线 … | 比赛材料的写法和自检，交付前能改好；“工作提示外发”“替客户填身份”两条仍是红线 |
| work/domains/development/industry-cases/education/tianjin-agent-contest/demo-video.md:134 | 运镜  开场取景只取页面 86% 宽，每行文字右侧被裁（见 4.2）  红线… | 比赛材料的写法和自检，交付前能改好；“工作提示外发”“替客户填身份”两条仍是红线 |
| work/domains/development/industry-cases/education/tianjin-agent-contest/demo-video.md:136 | 自检  只抽查静止帧，漏掉转场和滚动中的问题；改为逐帧自动检查（见 4.7）… | 比赛材料的写法和自检，交付前能改好；“工作提示外发”“替客户填身份”两条仍是红线 |
| work/domains/development/industry-cases/education/tianjin-agent-contest/demo-video.md:137 | 风格  经验复用的是手法，配色、字体、版式每个作品按内容重定（见 4.1） … | 比赛材料的写法和自检，交付前能改好；“工作提示外发”“替客户填身份”两条仍是红线 |
| work/domains/development/industry-cases/education/tianjin-agent-contest/document-format.md:18 | 二、扬长避短，不做事无巨细的澄清（红线） | 比赛材料的写法和自检，交付前能改好；“工作提示外发”“替客户填身份”两条仍是红线 |
| work/domains/development/industry-cases/education/tianjin-agent-contest/document-format.md:30 | 三、团队分工与 AI 工具使用（红线） | 比赛材料的写法和自检，交付前能改好；“工作提示外发”“替客户填身份”两条仍是红线 |
| work/domains/development/industry-cases/education/tianjin-agent-contest/document-format.md:40 | 四、统一版式（红线） | 比赛材料的写法和自检，交付前能改好；“工作提示外发”“替客户填身份”两条仍是红线 |
| work/domains/development/industry-cases/education/tianjin-agent-contest/document-format.md:116 | 五、字体设置要写到底层（红线） | 比赛材料的写法和自检，交付前能改好；“工作提示外发”“替客户填身份”两条仍是红线 |
| work/domains/development/tools/miaoda/workflow.md:141 | 交付前的干净复建（红线）：增量包不能单独解压构建。在干净目录先还原 base… | 工程做法，违反了能重做；数据库、密钥、平台类仍是红线 |
| work/domains/development/tools/miaoda/workflow.md:147 | 收件校验与作者复建分开（红线）：供秒哒先运行的校验脚本，只依赖独立解压目录中… | 工程做法，违反了能重做；数据库、密钥、平台类仍是红线 |
| work/domains/development/tools/miaoda/workflow.md:151 | Edge 部署输入闭包（红线）：按当前平台实际使用的部署接口，列出真正发送的… | 工程做法，违反了能重做；数据库、密钥、平台类仍是红线 |
| work/domains/other/commercial/experience/competition-and-investor-materials.md:45 | 5. 比赛材料扬长避短（红线）。模板设有“存在不足”等栏目时，不足只写在那一… | 比赛材料的写法，交付前能改好 |
| AGENTS.md:97 | 容易混淆的地方（默认，第一条是红线） | 整节降为默认，第一条（秒哒≠妙搭）、第三条（给学员≠讲师≠主办方）仍是红线 |
| work/domains/development/tools/miaoda/workflow.md:50 | 红线：秒哒 Web 应用是 React + Vite，产物是 dist/。不… | 技术栈用错可以重做，不是“百度秒哒和飞书妙搭用混”那种用错平台 |
| work/domains/development/experience/backend-auth-payment.md:14 | 登录与身份（红线） | 正文是能修好的 bug；其中“已有的重复账户不在同一次修复里自动合并”一句单独保留为红线（动线上数据） |
| AGENTS.md:48 | 按交付物自动叠加（读规范） | 读取规则，漏读属于 A 类失败，补读后能改好 |

## 带“红线”字样但没改的（34 处）

| 位置 | 内容 | 为什么不改 |
|---|---|---|
| system/repository/execution-checks.md:12 | 4. 把这次要守的规则抄成本单检查单。 从读过的文件里只挑和这一单有关的几条… | 只是提到“红线”这个词或链接到红线小节，不是一条规则；链接已随标题更新 |
| system/repository/ingestion-workflow.md:204 | - 红线放在任务一定会读到的那个文件的前面，不要埋在长文件的中段或积累区。 | 只是提到“红线”这个词或链接到红线小节，不是一条规则；链接已随标题更新 |
| system/repository/revisions/README.md:8 | 2026-09-28  仓库整改：AGENTS.md 改为一页"任务 → 必… | 只是提到“红线”这个词或链接到红线小节，不是一条规则；链接已随标题更新 |
| system/repository/templates/method.md:19 | - 红线：不能违反（例：给学员的课件不写讲师安排）。 | 方法模板里的级别说明，已按新的红线范围改写 |
| work/domains/design/common/code-driven-video/motion-and-verification.md:47 | 容器尺寸写死  内容少时留大块空白，内容多时溢出  按容器跟着内容走计算尺寸 | 只是提到“红线”这个词或链接到红线小节，不是一条规则；链接已随标题更新 |
| work/domains/design/common/design-principles/README.md:66 | 除了审美词库里“防止生搬硬套”一节是红线，其余都是默认：没有特别理由就照做。… | 级别说明，已改成“本目录都是默认” |
| work/domains/design/graphic/ppt/premium-course/case-yamiaozhuzhang-layout-and-stroke-animation.md:34 | 建委用这版工作台实际剪辑后（2026-10-14）指出对位错误：第2页视频应… | 只是提到“红线”这个词或链接到红线小节，不是一条规则；链接已随标题更新 |
| work/domains/design/video/promo/competition/README.md:29 | 每轮反馈后，按经验怎么回流判断要不要写：只收新的判断，写进它所属的那一块；能… | 只是提到“红线”这个词或链接到红线小节，不是一条规则；链接已随标题更新 |
| work/domains/design/video/promo/competition/ae-template-layout.md:13 | 1. 开工时：把文末排版验收整张表复制成这一单的检查单（每个画面一列），先过… | 只是提到“红线”这个词或链接到红线小节，不是一条规则；链接已随标题更新 |
| work/domains/design/video/promo/competition/ae-template-layout.md:123 | 每个镜头交给建委之前，AI 自己先做一遍。不过就改，改完重新出图再查，直到全… | 只是提到“红线”这个词或链接到红线小节，不是一条规则；链接已随标题更新 |
| work/domains/design/video/promo/competition/ae-template-layout.md:145 | 版式对照预览  建委认可的代码预览片或 Demo 版式和成片同一帧并排，结构… | 只是提到“红线”这个词或链接到红线小节，不是一条规则；链接已随标题更新 |
| work/domains/design/video/promo/competition/ae-template-layout.md:153 | 模板样例残留、字只放关键词  模板原来的标题、英文副标、编号、年份、示例人名… | 只是提到“红线”这个词或链接到红线小节，不是一条规则；链接已随标题更新 |
| work/domains/design/video/promo/competition/ae-template-layout.md:155 | 模板主体位置  相框、人像框、地面、倒影还在模板设计的位置；挪过的要说出理由… | 只是提到“红线”这个词或链接到红线小节，不是一条规则；链接已随标题更新 |
| work/domains/design/video/promo/enterprise/workflow.md:27 | 一个镜头服务一个主要信息，复杂段落拆为可执行镜头组，不把成立年份、多个财务数… | 只是提到“红线”这个词或链接到红线小节，不是一条规则；链接已随标题更新 |
| work/domains/development/industry-cases/education/tianjin-agent-contest/case-geometry-helper-math.md:13 | 没有功能流程图；主标题和副标题居左；章节未编号；标题和表格里用空格代替顿号（… | 只是提到“红线”这个词或链接到红线小节，不是一条规则；链接已随标题更新 |
| work/domains/development/industry-cases/education/tianjin-agent-contest/case-geometry-helper-math.md:15 | 旁白书面化（“我问……”）、比喻听不懂、结尾澄清“还需要进一步验证”  演示… | 只是提到“红线”这个词或链接到红线小节，不是一条规则；链接已随标题更新 |
| work/domains/development/industry-cases/education/tianjin-agent-contest/document-format.md:28 | 正例：只留第一句。没测的就去测，测过了直接写结果；通知没要求的空缺不写。旁白… | 只是提到“红线”这个词或链接到红线小节，不是一条规则；链接已随标题更新 |
| work/domains/development/industry-cases/education/tianjin-agent-contest/platform/capabilities.md:23 | 临时会话链接  作品卡片"…"→"临时会话"→"新增链接"，复制结果包含临时… | 只是提到“红线”这个词或链接到红线小节，不是一条规则；链接已随标题更新 |
| work/domains/development/industry-cases/education/tianjin-agent-contest/submission-package.md:65 | 评审入口按搭建流程第六节执行完整地址、登录选项和未登录运行核对。链接写进申报… | 只是提到“红线”这个词或链接到红线小节，不是一条规则；链接已随标题更新 |
| work/domains/development/industry-cases/education/tianjin-agent-contest/submission-package.md:74 | - [ ] 评审入口已完成平台核对，正文、超链接目标、二维码及压缩包内文件均… | 只是提到“红线”这个词或链接到红线小节，不是一条规则；链接已随标题更新 |
| work/domains/development/tools/miaoda/basics/platform-basics.md:71 | 容易丢失上下文  改完一处可能忘了另一处保持不变  强约束写在提示词最前面（… | 提示词模板里写给秒哒等模型的“红线”字样，是提示词内容 |
| work/domains/development/tools/miaoda/prompt-templates.md:11 | 3. 严禁改什么（红线写在前面，秒哒可能边读边改，放在末尾就晚了）。 | 提示词模板里写给秒哒等模型的“红线”字样，是提示词内容 |
| work/domains/development/tools/miaoda/topics/authentication.md:18 | 红线： | 提示词模板里写给秒哒等模型的“红线”字样，是提示词内容 |
| work/domains/development/tools/miaoda/topics/authentication.md:62 | 红线：继续使用 Supabase Auth 原生手机号流程，不自建验证码签发… | 提示词模板里写给秒哒等模型的“红线”字样，是提示词内容 |
| work/domains/development/tools/miaoda/topics/authentication.md:104 | 红线（必须遵守）： | 提示词模板里写给秒哒等模型的“红线”字样，是提示词内容 |
| work/domains/development/tools/miaoda/topics/backend-storage.md:56 | 红线： | 提示词模板里写给秒哒等模型的“红线”字样，是提示词内容 |
| work/domains/development/tools/miaoda/topics/seo-and-content.md:18 | 红线（必须遵守）： | 提示词模板里写给秒哒等模型的“红线”字样，是提示词内容 |
| work/domains/development/tools/miaoda/topics/seo-optimization.md:135 | 红线（必须遵守）： | 提示词模板里写给秒哒等模型的“红线”字样，是提示词内容 |
| work/domains/development/tools/miaoda/topics/uploads.md:46 | 红线： | 提示词模板里写给秒哒等模型的“红线”字样，是提示词内容 |
| work/domains/development/tools/miaoda/topics/wechat-urlsec-verification.md:104 | 红线： | 提示词模板里写给秒哒等模型的“红线”字样，是提示词内容 |
| work/domains/training/experience/jianwei-training-style.md:27 | 规则分级：标了红线的不能违反；其余为默认，有更好的理由可以变通，但要跟建委说… | 只是提到“红线”这个词或链接到红线小节，不是一条规则；链接已随标题更新 |
| work/domains/training/experience/jianwei-training-style.md:84 | - 建委自己已有的标红保留，不改色、不挪位置（见第六部分红线 2）。 | 只是提到“红线”这个词或链接到红线小节，不是一条规则；链接已随标题更新 |
| work/domains/development/tools/miaoda/pitfalls.md:585 等 | “3. 红线：第二个应用不新建表……”及“红线段”字样 | 写给秒哒的提示词里的段落名，不是本仓库规则的级别 |
| work/projects/feishu-efficient-office/writing-style-history.md:204 | 重复图片属于出版红线 | 《飞书高效办公》书稿的出版要求，属于项目事实，原样不动 |

统计口径：上面四张表收的是所有用级别写法标的红线（“（红线）”“**红线**”、标题里带红线），以及当时检索到的提到“红线”的说明和链接。秒哒踩坑记录、提示词模板里写给秒哒的“红线段”字样不是本仓库规则的级别，只列了代表。

## 独立审查

交付前另开一个全新的审查者，只给它建委的要求和检查单，查出并已改正：

- 审美标尺把建委没评价过的自我介绍 PPT 第四版、被评“跟 v1 差不多”的智慧工厂第二版写成了“认可”，观察记录里写了无依据的“建委接受”，几行版本号对错了位：都已按本机记忆和仓库记录改正，转述和原话分开标。
- AGENTS 写入规则第 3 条、建委偏好里“被指出差距就沉淀”还是旧做法，和“先记观察”冲突：已改成指向观察和晋升条件。
- 使用日志一单记几行、升级后没处理完的行还算不算、示例行把“仓库里本来没有”标成 B：已写明一单一行、留着的行继续计数，示例换成格式示意。
- 红线分类：“给学员≠讲师≠主办方”“六个状态分开记”恢复红线；“React + Vite”“登录与身份”降为默认（保留不自动合并账户一句）；可能由建委定过的两条恢复红线，列进上面请建委确认。
- 红线检查原来只比总数、不查项目文件：改成每个文件单独计数，项目和案例也纳入。
- 观察里言剪 v4“整体不如 v3”和精尺匠造“不如测试片段一”是同一类判断，原来类别写法不同，脚本数不到一起：统一成“不如认可旧版”，并按晋升条件升进审美标尺“认可成品当下限”一节。

## 这次没做的

- **长文件没有拆。** 按进化机制，等日志显示某个文件反复出 B 类，再按使用时刻拆。
- **观察里言剪AI的配色、节奏、交互演示、字幕样式几条还是待定。** 仓库里已有相近规则（配色、出场节奏等），下次升级时按晋升条件第 3 条决定并进哪条，不另起。
- **没有做对照实验。** 新机制有没有效，靠以后的使用日志检验；阈值是起步值，按实际情况调。

## 核对

- 改前的文件清单、每个文件的字数、红线清单都留了基线（仓库外的临时目录）；改后逐项对比，没有文件被删除；字数减少的只有一个文件，少的 3 个字是把“（红线＋默认）”换成了“（默认）”。
- 站内带锚点的链接全部有效；导航、结构、校验脚本和全部回归测试通过。
