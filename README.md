# 杨建委长期 AI 协作上下文仓库

> 这不是普通文件备份，而是建委长期项目、个人档案、工作经验、历史决策和 AI 协作规则的事实中枢。

## 从哪里开始

- 想交互式展开、折叠和搜索完整结构：打开 [`STRUCTURE.html`](./STRUCTURE.html)。
- 想编辑权威上下级目录和中文说明：读 [`STRUCTURE.md`](./STRUCTURE.md)。
- F 盘桌面镜像：`F:\桌面文件\GitHub仓库完整结构.html`，由维护脚本从 `STRUCTURE.md` 自动生成，不单独编辑。
- AI 执行具体任务：先读 [`llms.txt`](./llms.txt)，只进入任务对应领域。
- 新增、移动或清理资料：同时遵守 [`AGENTS.md`](./AGENTS.md) 和 [`STRUCTURE.md`](./STRUCTURE.md)。

## 平台识别硬规则：秒嗒与妙搭

- 建委说“秒嗒”或“秒哒”时，指百度秒哒 MIAODA；回复中沿用“秒嗒”，不得改成“妙搭”。`miaoda.cn`、`*.appmiaoda.com`（包括 `jianwei.appmiaoda.com`）均按百度秒哒处理。
- 飞书妙搭 Spark 是另一个产品。不得因为 `Miaoda` 拼写相同，或网站嵌入了飞书文档，就调用飞书妙搭的 `lark-apps`、`lark-cli apps`、Spark SDK 或套用其平台规则。
- 先确认平台，再选择技能、API 和开发方案。百度秒哒任务从 [`秒哒知识入口`](./work/ai/programming/tools/miaoda/README.md) 读取；只有线索确实不足时才澄清。
- 交付前检查说明、提示词、README、代码注释和工具依赖，清除错误平台名称与接口。完整判定规则见 [`产品辨析`](./work/ai/programming/tools/miaoda/disambiguation.md)。

## 五个一级目录

| 一级目录 | 回答什么问题 | 内容边界 |
|---|---|---|
| [`personal/`](./personal/README.md) | 建委是谁 | 个人资料、业务与项目概要、背书、成长路径、能力；不放项目细节 |
| [`brain/`](./brain/README.md) | 建委怎样思考，以及 AI 怎样输出高质量中文 | 建委认知 + 所有中文内容默认调用的 AI 表达基础层 |
| [`work/`](./work/README.md) | 建委做哪些工作和项目 | 设计、AI、其他工作领域，逐级放经验、工具和项目 |
| [`repository/`](./repository/README.md) | 仓库怎样维护 | 结构、版本治理、电脑环境、校验脚本和仓库级修订 |
| [`history/`](./history/README.md) | 过去发生了什么 | 跨领域时间线与已归档项目；不覆盖当前口径 |

## 工作领域总览

```text
work/
├── design/                  设计
│   ├── ppt-design/         PPT 设计
│   ├── poster-fold-design/ 海报与折页设计
│   ├── book-design/        书籍设计
│   ├── microcourse-mg-animation/ 微课与 MG 动画设计
│   ├── ae-promo-video/     AE 宣传视频设计
│   └── ai-design/          AI 设计（仍归设计）
├── ai/                      AI
│   ├── programming/        AI 编程：工具、经验、项目
│   ├── training/           AI 培训：经验、大纲、资料、项目
│   ├── video/              AI 视频：通用方法、类型、工具、项目
│   ├── publishing/         AI 书籍出版
│   └── self-media/         AI 自媒体
└── other/                   不属于设计或 AI 的其他领域与项目
    ├── commercial/         商业化与对外交付：跨领域规范、经验和注意事项
    ├── ai-sixty-jiazi-music-ip/ AI 六十甲子古音律与 IP 孵化
    └── inshan-popupiano/   海外电商项目
```

## 三条硬规则

1. **AI 表达 + 单一专项**：任何 AI 中文内容默认先调用 `brain/ai-expression/`，再叠加一个最具体的专业领域。用户只提 AI 自媒体，就组合 AI 表达与 AI 自媒体，不得顺带加载 AI 培训或其他领域。
2. **当前口径优先**：当前 README 是事实入口；`history.md`、归档资料和 Git 历史只用于追溯，不得混入当前结论。
3. **清洗后写入**：新增内容先判断是否重复、过时或只是一时记录。长期有效的结论才入库，并更新最近一层 README 索引。

建委要求沉淀到 GitHub 的内容，默认校验后直接提交并推送 `main`，不创建 PR，也不等待第二次提交指令。

对外商业内容另遵守 [`work/other/commercial/`](./work/other/commercial/README.md)：它是跨设计、AI 和其他项目复用的商业规范层。当内容用于给客户看、对外发送或正式交付时，必须区分内部工作稿与对外成品。商业计划书、比赛申报、路演和融资材料还要清除内部研发讨论、自证式声明及外部无法访问的本地证据。

## 快速个人画像

| 项目 | 当前信息 |
|---|---|
| 姓名 | 杨建委（称呼：建委） |
| 身份 | AIGC 实战落地专家、资深跨界设计师、AI 视频创作人 |
| 公司 | 宿州市十一创动画科技有限公司（法人代表） |
| 坐标 / 时区 | 济南 / Asia/Shanghai |
| 核心工作 | 设计、AI 编程、AI 培训、AI 视频、AI 书籍出版、AI 自媒体及其他项目 |
| GitHub | [MouMou-Eleven](https://github.com/MouMou-Eleven) |

个人事实以 [`personal/README.md`](./personal/README.md) 为准。

## 安全与校验

- 不写入密码、API Key、Token、Cookie、完整认证文件或可直接利用的隐私信息。
- 提交前运行：`powershell -ExecutionPolicy Bypass -File repository/maintenance/validate-context.ps1`
- 推送后检查远端文件和分支，不能只看到本地提交就判断完成。

仓库管理方法的对外科普版：<https://www.feishu.cn/wiki/PqSHwL1nniP2pOkML25cZx2bnSb>
