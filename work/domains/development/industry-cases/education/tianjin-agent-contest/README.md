# 天津智能体比赛

天津市 AI 教育应用场景、智能体设计应用和课程案例大赛**赛道二（教育智能体设计应用）**。这个比赛从头到尾沉淀下来的东西都在这个文件夹里：指定平台、提交材料、文档规范、演示视频、作品案例。目前客户参加的是 2026 年这一届（4 个作品已交付）；以后几届先拿新通知对照[提交材料](./submission-package.md)第一节，变化直接改那一节。

| 内容 | 文件 |
|---|---|
| 比赛指定的智能体平台（近似扣子）：能力体系、搭建流程 | [platform/](platform/README.md) |
| 比赛要求、提交文件夹、复现材料 | [提交材料](./submission-package.md) |
| 申报书、技术说明与验证报告的写法和版式 | [文档规范](./document-format.md) |
| 演示视频：逐字稿、录屏、剪辑与画面标注 | [演示视频](./demo-video.md) |
| 已做的作品 | 下面“已做的作品”表 |

本文件夹里的规定和手法只对这个比赛成立（红线）：别的比赛、别的视频即使看起来相似，也按它们自己的要求做，不套这里的片头、版式、字幕区和标注方式。

## 做一个新的参赛作品，按这个顺序读

| 步骤 | 读 |
|---|---|
| 1. 定课堂场景和学科融合方式 | [学科融合方法](../subject-integration/classroom-agent-design.md) |
| 2. 在指定平台搭建 | [平台能力体系](platform/capabilities.md) + [搭建流程](platform/build-sop.md) |
| 3. 整理提交文件夹和复现材料 | [提交材料与文件夹](./submission-package.md) |
| 4. 写申报书、技术说明与验证报告 | [Word 文档规范](./document-format.md) |
| 5. 写逐字稿、录屏、剪辑 | [演示视频](./demo-video.md) |

只做其中一项（比如"重写数学的技术报告"）时，读这一项对应的文件，再加读[文档规范](./document-format.md)第一至三节，那三节是所有评审材料共用的红线。

## 已做的作品

| 作品 | 学科 | 看什么 |
|---|---|---|
| [文有回声——小学语文阅读学伴](./case-wenyouhuisheng-chinese.md) | 语文 | 全文知识库、引文核验、过程记录表、教师报告子流程、图片卡；技术报告和流程图的正例 |
| [小学数学空间与图形探究助手](./case-geometry-helper-math.md) | 数学 | 代码核验数值单位、三维交互网页、示意图、国内部署、旧资源清理 |
| [幼儿自主游戏观察与支持助手](./case-kindergarten-play-observation.md) | 学前保教 | 图文观察、DeepSeek与GLM视觉分工、连续回访、固定工作台与平台表同步 |
| [慧评善改——小学语文习作评改与讲评智能体](./case-huipingshangai-chinese.md) | 语文习作 | GLM原生图文识别、确认后评改、修改反馈、可扩充量规与教师讲评 |

## 新经验写到哪

| 新经验是关于 | 写进 |
|---|---|
| 比赛要求、提交文件、文件夹、复现材料 | [submission-package.md](./submission-package.md) |
| 申报书、技术报告的版式、字体、措辞、团队表 | [document-format.md](./document-format.md) |
| 逐字稿、录屏、剪辑、画面标注、配音 | [demo-video.md](./demo-video.md) 对应环节；零散反馈先进第六节积累区 |
| 平台功能、节点、导入导出、坑 | [平台能力体系](platform/capabilities.md) 或 [搭建流程](platform/build-sop.md) |
| 学科怎么融合、课堂怎么用 | [学科融合方法](../subject-integration/classroom-agent-design.md) |
| 某个作品的 ID、链接、路径、进度、当次问题 | 该作品的案例文件 |
| 新客户的新作品 | 新建 `case-<作品英文短名>.md`，并在上面"已做的作品"表加一行 |

规则：先在对应文件里找同一件事，有就改那一条（补反例、改具体），没有才加；不为一次视频、一份报告新建方法文件。

<!-- generated-related-assets:start -->
## 相关项目与案例

| 类型 | 项目或案例 | 适用领域 |
|---|---|---|
| 案例 | [文有回声——小学语文阅读学伴（天津大赛）](case-wenyouhuisheng-chinese.md) | 教育行业应用开发 |
| 案例 | [小学数学空间与图形探究助手（天津大赛）](case-geometry-helper-math.md) | 教育行业应用开发 |
<!-- generated-related-assets:end -->
