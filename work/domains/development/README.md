# 应用开发与自动化

保存开发方法与平台知识；具体产品的目标、源码位置、状态与版本保存在项目。AI辅助是实现方式，不把工具资料数量等同于建委已具备的传统全栈能力。

| 入口 | 用途 |
|---|---|
| [工具知识包](./tools/README.md) | 百度秒哒等平台的功能、限制与实战操作 |
| [开发经验](./experience/README.md) | 跨工具流程、创意前端与参考材料 |
| [行业应用案例](./industry-cases/README.md) | 按行业查开发方法与实践；当前收录教育智能体和课堂融合 |
| [Skill能力库](../other/skills/README.md) | 可编辑动画、职业工作台、科研图与IP海报等能力及来源 |
| [项目与案例](../../projects/README.md) | 继续具体开发任务；项目事实不存工具目录 |

## 调用边界

- 只说秒哒先读[平台辨析](./tools/miaoda/README.md)及[秒哒导航](./tools/miaoda/llms.txt)，不自动读取言剪AI；百度秒哒不能走飞书妙搭接口。
- 开发某个现有项目先读其README，根据技术需求补工具方法，不把整个开发知识包一次读完。
- 页面开发、手机适配、UI 审查或用户继续反馈视觉问题时，读取[前端 UI 质量标准](./experience/frontend-ui-quality-standards.md)，匹配其中的步骤与验收。后续反馈先过准入门槛再合并，不能把每个临时参数都沉淀成规则。
- AI编程课程以[培训](../training/README.md)为主；真实演示需要开发方法时再组合，不据平台判课程归属。
- 教育智能体、学科应用和教学业务系统主读[教育行业](./industry-cases/education/README.md)；教师课件、微课与录课合成仍主读[教育设计](../design/video/education/README.md)。
- 产品答辩、销售提案或价值证明按目的补[商业案例方法](../other/commercial/experience/case-result-narrative.md)，纯技术说明不自动加销售话术。

单次排错可立即存为有证据的案例与候选方法，注明环境、过程、失败与验证范围。按[更新流程](../../../system/repository/ingestion-workflow.md)补相关项目和领域入口，工具参数只在工具主位置维护。

<!-- generated-related-assets:start -->
## 相关项目与案例

| 类型 | 项目或案例 | 适用领域 |
|---|---|---|
| 项目 | [言剪 AI](../../projects/yancut-ai/README.md) | 应用开发 |
| 项目 | [AI 六十甲子古音律与 IP 孵化](../../projects/ai-sixty-jiazi-music-ip/README.md) | 文化产品与IP |
| 案例 | [文有回声——小学语文阅读学伴（天津大赛）](industry-cases/education/tianjin-agent-contest/case-wenyouhuisheng-chinese.md) | 教育行业应用开发 |
| 案例 | [小学数学空间与图形探究助手（天津大赛）](industry-cases/education/tianjin-agent-contest/case-geometry-helper-math.md) | 教育行业应用开发 |
<!-- generated-related-assets:end -->

<!-- generated-methods:start -->
## 按实际需要选择方法

由routes.json生成。先判断本次成品和读者，再按下表实际需要读取方法正文；无需点名作者。多种方法可分工，但同一段不拼接相互冲突的结构。没有适用需求时跳过，不能因看到本表就全部加载。

| 需要解决什么 | 方法正文 | 不适用／保留边界 | 成品怎样检查 |
|---|---|---|---|
| 页面改版、组件选择、响应式适配、编辑器交互或需要判断界面设计质量时 | [前端 UI 质量标准](experience/frontend-ui-quality-standards.md) | 纯后端、数据库迁移、命令行脚本或无界面任务 | 读方法正文与目标项目 README；检查 1920/1024/768/390/360 布局；验证加载、失败、触控和键盘状态 |
| 教师或学校的教育智能体与学科应用需要选场景、融合手段，并把学习任务、执行流程、学生作品和教师反馈连接起来时 | [教育智能体课堂融合](industry-cases/education/subject-integration/classroom-agent-design.md) | 普通课件美化、微课视频和培训大纲；组件与课堂形式按具体学科和使用条件选择 | 课堂任务具体；组件有输入输出与责任；关键核验可复核；学生产物支持教师行动；运行与教学效果分别留证 |
<!-- generated-methods:end -->
