# 教育行业

教育行业的 AI 赋能方式之一是开发教育智能体。这里分两类，互不重复：

| 板块 | 管什么 | 适用范围 |
|---|---|---|
| [学科融合](./subject-integration/README.md) | 智能体怎么跟学科、课堂结合：教学研管评育场景、融合手段、新学科推导、融合案例 | 通用，任何平台、任何比赛都适用 |
| [天津智能体比赛](./tianjin-agent-contest/README.md) | 这个比赛从中沉淀的一切：指定平台的能力与搭建流程、提交材料、Word 规范、演示视频、已做的作品案例 | 只管这个比赛 |

**一个比赛一个文件夹（红线）。** 以后有别的省份、别的智能体比赛，按建委的安排在这里另建一个比赛文件夹，那个比赛的平台、材料规范、视频要求、作品案例都放进去；不往天津的文件夹里塞，也不拿天津的规定套别的比赛。只有学科融合这类跟比赛无关的通用做法，才写进[学科融合](./subject-integration/README.md)。

教师课件、微课、录课合成仍由[微课与教育交互](../../../design/video/education/README.md)负责。

## 按任务读取

| 要做什么 | 读 |
|---|---|
| 设计一个教育智能体（任何平台） | [学科融合方法](./subject-integration/classroom-agent-design.md) |
| 新学科、新场景，想借鉴已有案例 | [学科融合](./subject-integration/README.md)的融合案例对照 |
| 在天津比赛指定平台上搭建或修改 | [平台能力体系](./tianjin-agent-contest/platform/capabilities.md) + [搭建流程](./tianjin-agent-contest/platform/build-sop.md) |
| 准备天津大赛赛道二参赛材料（申报书、技术报告、逐字稿、视频、提交包） | [大赛入口](./tianjin-agent-contest/README.md)，按其中顺序读；所有评审材料都读[文档规范](./tianjin-agent-contest/document-format.md)第一至三节 |
| 接续某个已做作品 | 该作品案例，列表见[天津智能体比赛 · 已做的作品](./tianjin-agent-contest/README.md#已做的作品) |

## 写入规则（红线）

往这里写东西时，先按下表找到唯一位置，在原有条目上改或补；表里找不到才问建委。

| 新内容 | 写进 | 不要 |
|---|---|---|
| 学科融合的新做法、新场景、新手段 | [学科融合方法](./subject-integration/classroom-agent-design.md)对应一节的表或段落 | 不另建"语文融合方法""数学融合方法" |
| 别人的参考课例 | `subject-integration/case-external-<学科>-<短名>.md`，并在[学科融合](./subject-integration/README.md)对照表加一行 | 不把未核验的获奖、效果数字写成事实 |
| 天津平台新功能、新限制、新坑 | [能力体系](./tianjin-agent-contest/platform/capabilities.md)对应表 | 不写进作品案例当规则 |
| 天津平台操作步骤的修正 | [搭建流程](./tianjin-agent-contest/platform/build-sop.md)对应步骤 | 不新建"导出指南""导入指南" |
| 比赛要求、提交包变化 | [提交材料](./tianjin-agent-contest/submission-package.md) | — |
| 申报书、技术报告的版式和措辞纠正 | [文档规范](./tianjin-agent-contest/document-format.md) | 不在案例和 README 各写一遍 |
| 逐字稿、录屏、剪辑、标注的反馈 | [演示视频](./tianjin-agent-contest/demo-video.md)；零散的先进第六节积累区，同类合并 | 不为某个视频新建文件 |
| 某个作品的 ID、链接、路径、进度、当次问题 | 该作品案例 | 不写进方法和平台文件 |

同样的错误又出现时，说明规则没写具体或没被读到：把那条规则改得更具体（补"像这样写，不要那样写"），并检查 [AGENTS](../../../../../AGENTS.md) 任务表能不能从自然说法找到它；不要再加一条意思相同的"必须"。

<!-- generated-related-assets:start -->
## 相关项目与案例

暂无已登记关联；不能据此断言没有未登记材料。
<!-- generated-related-assets:end -->

<!-- generated-methods:start -->
## 按实际需要选择方法

由routes.json生成。先判断本次成品和读者，再按下表实际需要读取方法正文；无需点名作者。多种方法可分工，但同一段不拼接相互冲突的结构。没有适用需求时跳过，不能因看到本表就全部加载。

| 需要解决什么 | 方法正文 | 不适用／保留边界 | 成品怎样检查 |
|---|---|---|---|
| 教师或学校的教育智能体与学科应用需要选场景、融合手段，并把学习任务、执行流程、学生作品和教师反馈连接起来时 | [教育智能体课堂融合](subject-integration/classroom-agent-design.md) | 普通课件美化、微课视频和培训大纲；组件与课堂形式按具体学科和使用条件选择 | 课堂任务具体；组件有输入输出与责任；关键核验可复核；学生产物支持教师行动；运行与教学效果分别留证 |
<!-- generated-methods:end -->
