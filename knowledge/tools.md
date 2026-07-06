# Tools — 常用工具

## AI 工具

| 工具 | 用途 | 重要程度 |
|------|------|----------|
| 秒哒（Miaoda） | AI 应用开发 | ⭐⭐⭐ 首批超级开发者 |
| Coze | 智能体开发 | ⭐⭐⭐ 认证创作者 |
| 即梦 | AI 视频/图像生成 | ⭐⭐⭐ |
| OpenClaw | 本地 AI Agent | ⭐⭐ |
| ChatGPT | 对话 & 创作 | ⭐⭐ |
| Claude | 深度分析 & 写作 | ⭐⭐ |
| Cursor | AI 编程 | ⭐⭐ |

## 设计工具

| 工具 | 用途 |
|------|------|
| Figma | UI/UX 设计 |
| Adobe 全家桶 | PS、AI、AE、PR 等 |
| 剪映 / CapCut | 视频剪辑 |

## 教育课件工具

| 工具 | 用途 |
|------|------|
| 希沃白板 | 交互课件 |
| PPT | 演示 & 课件 |
| VR 工具 | VR 课件制作 |

## 协作 & 运维

| 工具 | 用途 |
|------|------|
| 飞书 | 团队协作、文档、多维表格、日历 |
| Git / GitHub | 版本控制 |
| Clash | 网络代理 |
| 微信 | 社交 & 工作沟通 |

## 飞书多维表格表单经验

### 二维码作为选项图片

> 2026-07-06 沉淀。来源：百度秒哒·AI落地大会济南城市线下赛报名表调整，以及参考表单 `https://yunyinghui.feishu.cn/share/base/form/shrcnJt0gbL7dBzy4Wx9TieGaWd` 的实操结构。

- 当表单里需要展示活动群、客服、收款码等二维码时，优先做成“选项图片/图片选项”，让图片直接跟随选项展示，比把二维码链接塞进活动简介更直观。
- 参考表单的公开 HTML 里可以看到图片配置位于 `window.formMetaContent.Snapshot.viewProperty.fieldInfos.<field_id>.extra.optionInfos.<option_id>.fileInfos[]`。
- `fileInfos[]` 的关键字段包括 `mimeType`、`fileName`、`token`、`width`、`height`。示例结构：`extra.optionInfos.opt_xxx.fileInfos[0].token`。
- 当前官方 OpenAPI / `lark-cli base +form-questions-update` 能更新表单问题的 `pre_field_id`、`title`、`description`、`required`、`visible`、`rich_description` 等基础字段，但没有公开“选项图片”写入字段；直接传 `extra.optionInfos` 不会真正写入公开表单 HTML。
- 后续创建类似表单时，先用 API 完成题目、顺序、简介、选项文字；二维码图片绑定要走飞书网页编辑器完成，并在交付前用公开表单 `/share/base/form/{share_token}` 验证 HTML 中是否出现 `optionInfos` / `fileInfos`。
- 交付口径要严格：如果只完成了题目和文字，不要说“二维码已直接展示”；只有公开表单里能看到图片或 HTML 中出现对应 `fileInfos`，才算图片选项绑定完成。

---

<!-- 发现新工具后更新此文件 -->
