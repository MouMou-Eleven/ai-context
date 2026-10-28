# 教育行业

教育行业的 AI 赋能方式之一是开发教育智能体。这里分三块，互不重复：

| 板块 | 管什么 | 跟平台和比赛的关系 |
|---|---|---|
| [学科融合](./subject-integration/README.md) | 智能体怎么跟学科、课堂结合：教学研管评育场景、融合手段、新学科推导、融合案例 | 通用，任何平台、任何比赛都适用 |
| [天津指定平台](./tianjin-platform/README.md) | 天津智能体平台（结构近似开源扣子）的能力体系与搭建流程 | 只要在这个平台上开发都用，不限比赛 |
| [天津 AI 教育大赛](./tianjin-ai-contest/README.md) | 赛道二提交材料、Word 规范、演示视频，以及已做的作品案例 | 只管这个比赛 |

教师课件、微课、录课合成仍由[微课与教育交互](../../../design/video/education/README.md)负责。

## 按任务读取

| 要做什么 | 读 |
|---|---|
| 设计一个教育智能体（任何平台） | [学科融合方法](./subject-integration/classroom-agent-design.md) |
| 新学科、新场景，想借鉴已有案例 | [学科融合](./subject-integration/README.md)的融合案例对照 |
| 在天津平台上搭建或修改 | [平台能力体系](./tianjin-platform/capabilities.md) + [搭建流程](./tianjin-platform/build-sop.md) |
| 准备天津大赛赛道二参赛材料（申报书、技术报告、逐字稿、视频、提交包） | [大赛入口](./tianjin-ai-contest/README.md)，按其中顺序读；所有评审材料都读[文档规范](./tianjin-ai-contest/document-format.md)第一至三节 |
| 接续某个已做作品 | 该作品案例：[文有回声（语文）](./tianjin-ai-contest/case-wenyouhuisheng-chinese.md)、[空间与图形探究助手（数学）](./tianjin-ai-contest/case-geometry-helper-math.md) |

## 写入规则（红线）

往这三块写东西时，先按下表找到唯一位置，在原有条目上改或补；表里找不到才问建委。

| 新内容 | 写进 | 不要 |
|---|---|---|
| 学科融合的新做法、新场景、新手段 | [学科融合方法](./subject-integration/classroom-agent-design.md)对应一节的表或段落 | 不另建"语文融合方法""数学融合方法" |
| 别人的参考课例 | `subject-integration/case-external-<学科>-<短名>.md`，并在[学科融合](./subject-integration/README.md)对照表加一行 | 不把未核验的获奖、效果数字写成事实 |
| 天津平台新功能、新限制、新坑 | [能力体系](./tianjin-platform/capabilities.md)对应表 | 不写进作品案例当规则 |
| 天津平台操作步骤的修正 | [搭建流程](./tianjin-platform/build-sop.md)对应步骤 | 不新建"导出指南""导入指南" |
| 比赛要求、提交包变化 | [提交材料](./tianjin-ai-contest/submission-package.md) | — |
| 申报书、技术报告的版式和措辞纠正 | [文档规范](./tianjin-ai-contest/document-format.md) | 不在案例和 README 各写一遍 |
| 逐字稿、录屏、剪辑、标注的反馈 | [演示视频](./tianjin-ai-contest/demo-video.md)；零散的先进第六节积累区，同类合并 | 不为某个视频新建文件 |
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
