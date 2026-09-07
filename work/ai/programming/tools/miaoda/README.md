# 百度秒哒 MIAODA

> 百度秒哒是 AI 编程下面的一个工具知识包，不是独立工作领域，也不是飞书妙搭 Spark。

## 必须先识别平台

- 建委使用“秒嗒/秒哒”指百度秒哒；与建委对话时沿用“秒嗒”，不得自动替换成“妙搭”。
- `miaoda.cn`、`*.appmiaoda.com`，以及当前网站 `https://jianwei.appmiaoda.com/`，按百度秒哒路由。
- 飞书妙搭是另一产品。禁止只凭 `Miaoda` 拼写加载 `lark-apps`，禁止使用 `lark-cli apps`、`.spark/meta.json`、Spark SDK 或飞书妙搭发布流程改造百度秒哒应用。
- 飞书文档可以作为网站内容来源，但不意味着该网站使用飞书妙搭。文档读取与宿主网站开发分别选择对应能力。
- 生成补丁、压缩包、README 和执行提示词前，核对平台名称、域名、上传规则和接口来源；发现混用必须先修正。
- 以上为 2026-09-05 建委纠正连续误识别后确认的长期规则。

## 目录结构

```text
miaoda/
├── README.md          当前入口与目录说明
├── llms.txt           AI 最小读取路由
├── disambiguation.md  同名产品辨析
├── basics/            平台基础与发布渠道
├── development/       Skill开发与外部调用
├── experience/        踩坑、提示词、案例、处方和参考源码
└── updates/           版本时间线与重要更新
```

## 读取路由

| 问题 | 首读 |
|---|---|
| 不确定“秒哒/妙搭”指什么 | [`disambiguation.md`](./disambiguation.md) |
| 当前版本、会员权益、上传与容量限制 | [`basics/current-capabilities.md`](./basics/current-capabilities.md) |
| 平台形态、运行时、存储、发布渠道 | [`basics/README.md`](./basics/README.md) |
| 开发自定义 Skill 或被外部 Agent 调用 | [`development/README.md`](./development/README.md) |
| 排错、提示词、完整案例或重复方案 | [`experience/README.md`](./experience/README.md) |
| 追溯功能变化和旧环境方案 | [`updates/README.md`](./updates/README.md) |

## 当前原则

- 秒哒功能、计费、渠道和界面会变化；回答“现在能不能做”前必须重新核验官方资料或实际环境。
- 当前已核验口径先读 `basics/current-capabilities.md`；历史版本变化只从 `updates/` 追溯，不能反向覆盖当前口径。
- 秒哒技能运行时与应用运行时是两个环境，密钥和变量不能默认互通。
- 秒哒收到指令后会直接修改，提示词必须写清红线、顺序和验收。
- 秒哒云端构建不等于真实浏览器或手机验收；运行时问题应由用户复现并提供日志。
- `updates/version-features.md` 只用于历史追溯，不能作为当前能力清单。

动态知识治理遵守 [`../../../../../repository/versioned-knowledge-policy.md`](../../../../../repository/versioned-knowledge-policy.md)。

*结构确认：2026-08-18*
