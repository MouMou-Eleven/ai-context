# AI 编程通用经验

不绑定某个工具、所有 AI 编程项目都能用的经验。某个工具特有的做法放在 `tools/<工具>/`，比如[秒哒](../tools/miaoda/README.md)；某个项目自己的事实放在 `projects/<项目>/`。

## 内容

| 内容 | 文件 | 什么时候读 |
|---|---|---|
| 交付与测试：证据分级、干净复建、跨层契约、字段矩阵、线上版本确认、性能不降质 | [delivery-and-testing.md](./delivery-and-testing.md) | 任何要交付、要测试、要上线的开发任务 |
| 后端、登录、支付：数据存哪、手机号身份、签名、密钥、多通道支付、兑换码事务 | [backend-auth-payment.md](./backend-auth-payment.md) | 涉及数据库、登录、支付、积分 |
| 前端 UI 质量：层级、间距、多端、状态体验、移动端验收 | [frontend-ui-quality-standards.md](./frontend-ui-quality-standards.md) | 页面改版、组件、响应式、需要判断界面好不好看 |
| 创意前端提示词：视频、3D、滚动叙事、空间画廊 | [creative-frontend-prompt-patterns.md](./creative-frontend-prompt-patterns.md) | 要做有视觉冲击力的前端页面 |
| 原始参考材料 | [reference-materials/](./reference-materials/README.md) | 核对原始提示词时才读 |
| 修订记录 | [revisions/](./revisions/README.md) | 追溯规则为什么这样定 |

商业化落地（怎么定价、怎么对外介绍产品）见[商业化领域](../../other/commercial/README.md)；Skill 见 [Skill 库](../../other/skills/README.md)。

## 写入规则

- 在两个以上工具或项目里都成立的，才写进这里；只在某个工具上成立的，写进该工具目录。
- 秒哒上发现的问题，先判断是秒哒特有的还是通用的。通用的写这里，秒哒目录里只留链接。
- 每条标上级别：红线、默认、可灵活。
- 同类错误补证据，不重复造规则。其他规则见[写入规范](../../../../system/repository/ingestion-workflow.md)。

<!-- generated-methods:start -->
## 按实际需要选择方法

由routes.json生成。先判断本次成品和读者，再按下表实际需要读取方法正文；无需点名作者。多种方法可分工，但同一段不拼接相互冲突的结构。没有适用需求时跳过，不能因看到本表就全部加载。

| 需要解决什么 | 方法正文 | 不适用／保留边界 | 成品怎样检查 |
|---|---|---|---|
| 页面改版、组件选择、响应式适配、编辑器交互或需要判断界面设计质量时 | [前端 UI 质量标准](frontend-ui-quality-standards.md) | 纯后端、数据库迁移、命令行脚本或无界面任务 | 读方法正文与目标项目 README；检查 1920/1024/768/390/360 布局；验证加载、失败、触控和键盘状态 |
<!-- generated-methods:end -->
