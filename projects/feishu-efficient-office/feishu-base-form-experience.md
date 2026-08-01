# 飞书多维表格表单经验

> 状态：当前有效的飞书项目经验
> 最后核验：2026-07-06

## 文字与选项原则

- 选项使用填写人自然会说的话，不使用“不适用、特殊情况”等后台式词。
- 问题和选项一一对应；是否题使用“是 / 否”或“我会 / 我不会”。
- 二维码、地点和群入口等需要立即识别的信息，优先直接展示，不默认藏在活动简介链接里。

## 二维码作为选项图片

来源：百度秒哒 AI 落地大会济南城市线下赛报名表调整，以及参考表单 `https://yunyinghui.feishu.cn/share/base/form/shrcnJt0gbL7dBzy4Wx9TieGaWd` 的实操结构。

- 飞书多维表格表单需要展示活动群、客服或收款码时，优先使用网页端“选项图片 / 图片选项”，让二维码跟随选项显示。
- 公开表单 HTML 中，图片配置位于 `window.formMetaContent.Snapshot.viewProperty.fieldInfos.<field_id>.extra.optionInfos.<option_id>.fileInfos[]`。
- `fileInfos[]` 的关键字段包括 `mimeType`、`fileName`、`token`、`width` 和 `height`。
- 当前官方 OpenAPI 和 `lark-cli base +form-questions-update` 可以更新问题基础字段，但没有公开选项图片写入字段；直接传 `extra.optionInfos` 不会真正写入公开表单 HTML。
- API 先完成题目、顺序、简介和选项文字；二维码图片绑定使用飞书网页编辑器完成。
- 交付前打开公开表单 `/share/base/form/{share_token}`，确认页面能看到图片，或 HTML 中存在对应 `optionInfos` 和 `fileInfos`。
- 如果只完成题目和文字，不能声称“二维码已直接展示”。

## 使用边界

飞书 API 和界面能力会变化。再次执行前必须核验官方文档或当前界面，并遵守 [`../../repository/versioned-knowledge-policy.md`](../../repository/versioned-knowledge-policy.md)。
