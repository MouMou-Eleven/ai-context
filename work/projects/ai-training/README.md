# AI 培训项目

建委到企业、机关、图书馆、夜校讲 AI 课的长期业务。每家单位或每一场培训是本目录下的一个子目录。

**本目录放什么**：各场次的事实（主办方、受众、需求对接、方案、实际报价、场次安排、授课状态、讲后反馈）。
**不放什么**：可复用的培训接洽、大纲、课件和讲法，统一在[培训与教学](../../domains/training/README.md)维护；给主办方的方案写法见[培训方案与大纲设计](../../domains/training/experience/external-proposal-design.md)。AI 培训和[会员社群](../paid-community-course/README.md)是两回事。

## 各场次

| 场次 | 主办方 / 受众 | 状态 |
|---|---|---|
| [济南市领导干部 AI 专题培训](jinan-cadre-ai/README.md) | 济南市总工会；各区县副处级以上约 200 人 | 方案设计阶段，授课日期未确认 |
| [济南市图书馆培训](jinan-city-library/README.md) | 济南市图书馆 | 2026-09-16 建委确认；AI 编程那期班次和日期未提供；WorkBuddy 训练营 2026-11 开讲，第 1—3 课已讲，第 4 课 11-23 写入飞书待建委看 |
| [山东省图书馆 · WorkBuddy AI 办公实战课](shandong-library/README.md) | 山东省图书馆；馆内工作人员 | 2026-11-13 大纲交付（90／180 分钟两版），授课日期待确认 |
| [山东电力咨询院 · WorkBuddy 智能体办公实战培训](shandong-electric-consulting/README.md) | 山东电力咨询院；全员，现场约 20 人、线上约 200 人 | 2026-11-16 方案交付建委（2 小时，Skill 为重点，含 AI + CAD），授课日期待定 |
| [济南城市建设集团 · WorkBuddy 办公提效实操工作坊](jinan-urban-construction/README.md) | 济南城市建设集团；宣传岗约 60 人 | 2026-11-18 方案交付建委（2 小时含 5 分钟休息，接手江坤的框架）；11-20 已授课，讲后反馈见场次记录 |

**万融委托的场次**（目前是山东电力咨询院、济南城市建设集团）写方案和课件时要软植入 WorkBuddy 企业版推广，口径见[万融委托培训](wanrong-commissioned/README.md)；其他场次不植入。新场次在 README 基本情况里写明委托方。

更多已讲过但还没收进仓库的单位、按课件找资料、归属不明的资料，见[场次索引](sessions-index.md)。常讲课题见[常讲课题](../../domains/training/topics.md)。

## 新的一场怎么沉淀

这一场的事实写在本目录：新建或更新 `<单位英文短名>/README.md`（主办方、委托方、日期、受众、时长、课题、资料链接、授课状态、讲后反馈，不知道的写"待确认"），并在上表和[场次索引](sessions-index.md)各加一行。WorkBuddy 这类工具的按钮、入口、限制写进[WorkBuddy 工具事实](workbuddy-tool-facts.md)，不写在场次里。事实之外的部分（能复用的做法改哪个方法文件、一条反馈怎么下结论）按[讲完课怎样沉淀](../../domains/training/experience/README.md#讲完课怎样沉淀)做。

## 本目录的文件

| 文件 | 内容 |
|---|---|
| [sessions-index.md](sessions-index.md) | 场次索引：按资料身份找课件正文、待归属资料 |
| [workbuddy-tool-facts.md](workbuddy-tool-facts.md) | WorkBuddy 的按钮、入口、限制，标了版本和最后核实日期；各场次实测记下的工具事实都集中在这里 |
| 各场次子目录 | 见上面“各场次”表；万融委托的植入口径在 [wanrong-commissioned](wanrong-commissioned/README.md) |

## 培训业务的方法入口

接洽、选题、大纲确认、课程开发与授课复盘的总流程见[培训与教学](../../domains/training/README.md)。2026-10-03 按建委确认的业务归属调整：本项目维护场次事实，培训领域维护复用方法，商业化维护跨行业标准。

<!-- generated-related-assets:start -->
<!-- generated-related-assets:end -->

<!-- generated-methods:start -->
## 按实际需要选择方法

由routes.json生成。先判断本次成品和读者，再按下表实际需要读取方法正文；无需点名作者。多种方法可分工，但同一段不拼接相互冲突的结构。没有适用需求时跳过，不能因看到本表就全部加载。

| 需要解决什么 | 方法正文 | 不适用／保留边界 | 成品怎样检查 |
|---|---|---|---|
| 当前无已登记适用方法 | 按实际领域正文判断 | 不根据旧表自动激活 | 核对来源与当前任务 |
<!-- generated-methods:end -->
