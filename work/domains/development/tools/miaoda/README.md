# 百度秒哒 MIAODA

建委的主要 AI 开发平台。这里只放**秒哒特有**的知识；测试、UI、后端、商业化这类所有 AI 编程都通用的经验放在[通用开发经验](../../experience/README.md)。

## 先确认平台（红线）

**百度秒哒 ≠ 飞书妙搭。** 两个产品读音相同，分属百度和飞书，没有任何关系。

| 看到这些 | 是 |
|---|---|
| "秒哒""秒嗒""百度秒哒"、`miaoda.cn`、`*.appmiaoda.com`、`miaoda.online`、"秒点" | **百度秒哒**（本目录） |
| "飞书妙搭"、`miaoda.feishu.cn`、`*.aiforce.cloud`、Spark | 飞书妙搭（不在本仓库） |
| 只有 Miaoda 拼写、飞书文档链接、"Skill" | 不能判断，看应用域名或问建委 |

- 建委说"秒嗒""秒哒"时一律按百度秒哒处理，回复时沿用"秒嗒"，不要改成"妙搭"。
- 做百度秒哒的任务时，**不要**加载 `lark-apps` 技能，不要用 `lark-cli apps`、Spark SDK、`.spark/meta.json` 或飞书妙搭的发布流程。
- 秒哒网站里嵌了飞书文档，只说明内容来自飞书，网站仍然是秒哒做的。
- 已确认的秒哒网站：`https://jianwei.appmiaoda.com/`、`https://app-e6qfpypd02yp.appmiaoda.com/`。
- 百度秒哒官网 [miaoda.cn](https://www.miaoda.cn)，官方文档 [cloud.baidu.com/doc/MIAODA](https://cloud.baidu.com/doc/MIAODA/index.html)。

（2026-09-05 建委纠正连续误识别后确认。本机的 `lark-apps` 技能描述里也已写明"不适用于百度秒哒"。）

## 要做什么，读哪个

| 任务 | 读 |
|---|---|
| 查秒哒现在能不能做某事、限额、会员、价格 | [facts.md](./facts.md)（唯一的当前事实表） |
| 用 Codex 开发秒哒项目（新项目、迭代、修问题） | [workflow.md](./workflow.md)：先按顶部表格选路径 A/B/C |
| 要写给秒哒的提示词 | [prompt-templates.md](./prompt-templates.md) |
| 上传、登录、支付、SEO、排错、后端、微信验证 | [topics/](./topics/README.md) 里对应的专题 |
| 报错了、踩坑了 | [pitfalls.md](./pitfalls.md) |
| 平台运行时、后端底座、首轮三个决定 | [basics/platform-basics.md](./basics/platform-basics.md) |
| 发布到小程序、APP、自定义域名 | [basics/publish-channels.md](./basics/publish-channels.md) |
| 开发秒哒 Skill，或让外部 Agent 调用秒哒 | [development/](./development/README.md) |
| 完整支付接入案例 | [topics/payment-case-yungouos-jsapi.md](./topics/payment-case-yungouos-jsapi.md) |
| 追溯版本变化 | [updates/](./updates/README.md)（只用来追溯，不代表现状） |

具体项目（比如言剪 AI）的进度和执行卡在项目自己的目录里，见[言剪 AI](../../../../projects/yancut-ai/README.md)。

## 目录

```text
miaoda/
├── README.md            本页：平台识别 + 读取路由
├── llms.txt             给只认 llms.txt 的工具用的短路由
├── facts.md             当前事实表：会员、限额、计费、版本
├── workflow.md          Codex × 秒哒协作方法（三条路径、十个阶段）
├── prompt-templates.md  可粘贴的提示词模板
├── pitfalls.md          踩坑清单
├── topics/              专题：上传、登录、支付（含完整支付案例）、SEO、排错、后端、微信验证
├── basics/              平台基础、发布渠道
├── development/         Skill 开发、被外部 Agent 调用
├── reference-materials/ 旧环境兼容源码（默认不读）
└── updates/             版本时间线（只用于追溯）
```

## 写入规则

- 会变的事实（限额、价格、功能）只写在 [facts.md](./facts.md)，其他文件链接过去。
- 协作方法的改进直接改 [workflow.md](./workflow.md) 对应阶段的原文；专题经验改对应专题。不要在文件末尾追加"最新经验"。
- 新坑先查 [pitfalls.md](./pitfalls.md) 有没有同类，有就改那一条；没有才新增。
- 只跟某个项目有关的内容（批次号、具体功能、项目 bug）写在项目目录，不写进本目录。
- 能用到所有 AI 编程工具的经验，写进[通用开发经验](../../experience/README.md)。
- 其他规则见仓库[写入规范](../../../../../system/repository/ingestion-workflow.md)。
