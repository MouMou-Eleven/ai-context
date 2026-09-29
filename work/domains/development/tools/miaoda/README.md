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

## 调用规则：AI 怎么和秒哒打交道

| 情况 | 怎么做 | 不要做 |
|---|---|---|
| 有本地源码（言剪这类） | Codex 在本地改代码、测试，打**增量包**上传给秒哒校验合并，按 [workflow.md](./workflow.md) 路径 B | 不退回让秒哒按长提示词自由重写 |
| 新项目 | 本地开发完整版，一次打全量包上传，按路径 A | 不边聊边让秒哒一点点生成 |
| 只在云端、没有源码 | 写给秒哒的提示词，用 [prompt-templates.md](./prompt-templates.md)，按路径 C | 不猜云端代码现状 |
| 要查云端版本、读回执、下达有限命令 | 用秒哒 Skill / CLI，范围和命令见 [skill-as-callable.md](./development/skill-as-callable.md#当前采用方式)；上一轮结束且建委授权后才下达新命令 | 不把 Skill 当成发布工具，发布仍走线上验收 |
| 任何时候 | 只用百度秒哒自己的入口 | **不调用** `lark-apps`、`lark-cli apps`、Spark（那是飞书妙搭） |

## 写入规则：新内容放哪

| 新内容是什么 | 写到哪 | 怎么写 |
|---|---|---|
| 平台事实变了（限额、价格、会员、新功能） | [facts.md](./facts.md) 对应行 | 改原行，写核验日期和来源；别的文件只链接不抄 |
| 协作流程有改进（打包、上传、验收顺序） | [workflow.md](./workflow.md) 对应阶段 | 改那一阶段的原文，不在末尾追加"最新经验" |
| 某类功能的做法（上传、登录、支付、SEO、后端） | [topics/](./topics/README.md) 对应专题 | 同上；完全没有对应专题才新建一个专题文件 |
| 踩了坑、报错 | [pitfalls.md](./pitfalls.md) | 先查有没有同类，有就补证据改那一条 |
| 好用的提示词 | [prompt-templates.md](./prompt-templates.md) | 写清适用路径和场景 |
| 秒哒 Skill、外部调用的新实测 | [development/skill-as-callable.md](./development/skill-as-callable.md) | 按该文件"如何扩展"一节 |
| 某个项目的进度、批次、bug | 项目自己的目录（如[言剪 AI](../../../../projects/yancut-ai/README.md)） | 不写进本目录 |
| 换了工具也成立的开发经验（测试、UI、后端设计） | [通用开发经验](../../experience/README.md) | 本目录只留链接 |
| 官方版本更新记录 | [updates/](./updates/README.md) | 只用于追溯；现状以 facts.md 为准 |

本目录**不再新建子目录**。放不进上表任何一行时，先按[写入规范](../../../../../system/repository/ingestion-workflow.md)给建委 A/B 两个方案。
