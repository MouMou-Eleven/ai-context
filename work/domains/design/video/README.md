# 视频、动画与教育作品

| 方向 | 适用任务 |
|---|---|
| [宣传片](./promo/README.md) | 企业、产品、创赛等宣传交付；按片型读取制作方法与提示词记录 |
| [微课与教育交互](./education/README.md) | 教师或学校委托的微课、教学动画、VR和交互课件 |
| [故事与叙事影片](./story/README.md) | 真人故事、剧情镜头、角色连续性及叙事参考 |
| [共用制作方法与工具](./common/README.md) | 分镜、镜头生产、MG/AE、合成、声音与生成工具 |

AE、MG、AI生成是可组合的制作技术。只说“MG动画”先进入共用方法，不能推定为教师微课；企业MG宣传片按宣传目的进入宣传片。教育交互不一律当作视频文件，编程能力按实际需要调用。

中文脚本、旁白与字幕读[表达标准](../../../../system/expression/README.md)。按[设计流程](../common/production-workflow.md)组织需求与交付，工具已选时再读对应能力。项目、案例与实测证据统一保存在[项目与案例](../../../projects/README.md)，本领域提供发现入口。

微课需要把教学设计、逐字稿、音频、分镜、参考图、提示词和返工状态组织起来时，使用[微课交互式制作工作台](./education/interactive-production-workbench.md)。页面根据实际素材启用模块；没有音频时按教学环节或逐字稿语义拆分，不显示无效播放控件。

<!-- generated-methods:start -->
## 按实际需要选择方法

由routes.json生成。先判断本次成品和读者，再按下表实际需要读取方法正文；无需点名作者。多种方法可分工，但同一段不拼接相互冲突的结构。没有适用需求时跳过，不能因看到本表就全部加载。

| 需要解决什么 | 方法正文 | 不适用／保留边界 | 成品怎样检查 |
|---|---|---|---|
| 实际需要AI生成视频素材、参考图动态化或镜头提示词时；可明确调用，也可按制作环节主动识别，再按镜头意图读具体模板 | [Awesome Seedance 视频提示词方法](common/awesome-seedance/README.md) | 纯AE／Remotion动效、仅口播文案、模型介绍或查询不自动套用；不覆盖片型设计、已验证经验或用户保护范围 | 实际读对应模板和一个锚点；核对主体／动作／镜头／声音、当前模型限制和复测状态；有生成产物才做成片验收，失败回写原项目 |
<!-- generated-methods:end -->

<!-- generated-related-assets:start -->
## 相关项目与案例

| 类型 | 项目或案例 | 适用领域 |
|---|---|---|
| 提示词案例 | [企业片提示词实战记录](../../../projects/cases/2026-05-enterprise-prompt-record.md) | 企业宣传片与信息包装 |
| 案例复盘 | [《小树叶》AI教师音乐微课](../../../projects/cases/little-leaf-ai-microcourse-mv.md) | 教师音乐微课、AI画面与Seedance多镜头 |
<!-- generated-related-assets:end -->

## 方法修订

[视频制作修订记录](./revisions/README.md)保存重要方向与适用范围变化。
