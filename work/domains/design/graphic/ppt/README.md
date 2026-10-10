# PPT 设计

## 负责范围

商务汇报、企业演示、路演与课件视觉；信息层级、版式、图表、视觉统一和现场可读性。

## 按内容对象联动

- 建委作为讲师的课程结构、备课和授课经验 → [AI 培训](../../../training/README.md)；具体课表按所属培训项目核验，不能混入会员社群。
- 教师委托的 PPT 微课、教育作品 → [微课设计](../../video/education/README.md)；不因出现“课程”就转为建委授课项目。
- 飞书书稿的出版事实 → [出版入口](../../../../projects/feishu-efficient-office/README.md)。
- AI 生成视觉资产或图文动画 → [AI 设计](../../common/ai-generation-principles.md) 或 [Remotion 能力](../../../other/skills/jianwei-ai-community-remotion-video/README.md)。

只读当前任务的必要依赖，具体项目保存一个主记录。

## 先按约束选择流程

| 场景 | 主流程 | 边界 |
|---|---|---|
| 所有PPT的制作与美化（自由设计，或有教学模板、企业模板等指定模板） | [AI全流程协作](ai-assisted-design/README.md) | 先内容图文稿，再定调（有模板时模板代替定调）和逐页设计，最后分层重建 |
| 精品课：要录课合成、教师出镜 | [精品课制作](premium-course/README.md) | 在上一行流程之上，加教师留位、封面保护、逐页录制等精品课要求 |

“有模板”不等于精品课：只有要录课合成、教师出镜时才走精品课。出现“教学设计、语文、参赛课”也不自动等于精品课。所有排版判断都按[设计原则与规范](../design-principles/README.md)。

## 当前状态与维护

[《山居秋暝》](ai-assisted-design/case-shanju-qiuming.md)记录自由视觉与可编辑重建；[《角的再认识》](premium-course/case-angle-revisited.md)记录指定模板精品课。按[联合流程](../../common/production-workflow.md)维护真实事实、方法与验收边界，不根据能力标签补猜结果。

<!-- generated-related-assets:start -->
## 相关项目与案例

暂无已登记关联；不能据此断言没有未登记材料。
<!-- generated-related-assets:end -->

<!-- generated-methods:start -->
## 按实际需要选择方法

由routes.json生成。先判断本次成品和读者，再按下表实际需要读取方法正文；无需点名作者。多种方法可分工，但同一段不拼接相互冲突的结构。没有适用需求时跳过，不能因看到本表就全部加载。

| 需要解决什么 | 方法正文 | 不适用／保留边界 | 成品怎样检查 |
|---|---|---|---|
| 精品课：要录课合成、教师出镜的课件制作与返修；只有模板没有录课合成的不走 | [精品课制作与验收](premium-course/workflow.md) | 普通商务汇报与自由风格路演；不套用个案费用、字号和人物区域 | 保护最新用户改稿，按任务检查图文适配、箭头轴线与旋转、准确点击句及媒体返回；冻结HTML时不自动同步 |
| 所有PPT的制作、美化、拆页、首页定调、双图逐页设计及设计图重建可编辑成品；有指定模板时模板代替首页定调 | [PPT设计：AI全流程协作](ai-assisted-design/workflow.md) | 精品课的录课合成、教师留位与封面保护由精品课主导（页面美化仍用本流程）；已确认稿从当前阶段接续 | 内容图文稿先过关；风格图与内容图分工；完整素材用生图重建不裁碎；原生文字可编辑；静态、动画、播放分别验收 |
<!-- generated-methods:end -->
