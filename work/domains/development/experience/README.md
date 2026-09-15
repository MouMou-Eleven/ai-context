# AI 编程经验

> 保存不绑定单一工具、可跨网站和应用项目使用的开发经验。

## 当前内容

| 内容 | 入口 | 用途 |
|---|---|---|
| 创意前端提示词方法 | [`creative-frontend-prompt-patterns.md`](./creative-frontend-prompt-patterns.md) | 视频、3D、滚动叙事和空间画廊的提示词结构 |
| Skill 仓库 | [`skill-repository/`](../../other/skills/README.md) | 保存可直接读取或安装的 Skill 实体，并固定上游地址、版本和更新方式 |
| 原始参考材料 | [`reference-materials/`](./reference-materials/README.md) | 核对原始提示词与交互机制 |
| 前端 UI 质量标准 | [`frontend-ui-quality-standards.md`](./frontend-ui-quality-standards.md) | 层级、间距、多端与状态体验的通用验收方法 |

## 写入规则

- 只有跨两个以上工具或项目仍成立的方法才进入这里。
- 某个工具专属踩坑进入 `tools/<tool>/experience/`。
- 某个项目事实进入 `projects/<project>/`。
- 收录 Skill 时必须保存实际内容，并用条目 README 与 `upstream.json` 记录来源、固定版本、依赖和同步方式；不得只保存外链。
- 原始材料默认不激活，先读提炼后的方法文件。

<!-- generated-methods:start -->
## 按实际需要选择方法

由routes.json生成。先判断本次成品和读者，再按下表实际需要读取方法正文；无需点名作者。多种方法可分工，但同一段不拼接相互冲突的结构。没有适用需求时跳过，不能因看到本表就全部加载。

| 需要解决什么 | 方法正文 | 不适用／保留边界 | 成品怎样检查 |
|---|---|---|---|
| 页面改版、组件选择、响应式适配、编辑器交互或需要判断界面设计质量时 | [前端 UI 质量标准](frontend-ui-quality-standards.md) | 纯后端、数据库迁移、命令行脚本或无界面任务 | 读方法正文与目标项目 README；检查 1920/1024/768/390/360 布局；验证加载、失败、触控和键盘状态 |
<!-- generated-methods:end -->
