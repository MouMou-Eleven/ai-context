# Personal AI Context

> 杨建委的长期 AI 协作上下文中枢。这里保存当前身份、工作偏好、长期项目、专业知识、关键决策与历史修订，让不同 AI 能快速获得一致、可追溯的上下文。

## AI 最短读取路径

1. 先读 [`llms.txt`](./llms.txt)，根据任务选择最小读取包。
2. 涉及对外身份、荣誉或数据时，检查 [`open-questions.md`](./open-questions.md)。
3. 只有准备写入或调整结构时，才需要继续读 [`STRUCTURE.md`](./STRUCTURE.md)。

不要默认加载整个仓库。`all-docs.md`、全部修订记录、历史时间线、源码和二进制附件都属于按需材料。

## 快速概览

| 项目 | 当前信息 |
|---|---|
| 姓名 | 杨建委（称呼：建委） |
| 身份 | AIGC 实战落地专家、资深跨界设计师、AI 视频创作人 |
| 公司 | 宿州市十一创动画科技有限公司（法人代表） |
| 坐标 / 时区 | 济南 / Asia/Shanghai (UTC+8) |
| 核心能力 | 设计、AI 内容创作、AI 培训咨询、AI 应用落地 |
| 技术特点 | 非科班程序员，主要借助 AI 编程工具完成产品和自动化落地 |
| GitHub | [MouMou-Eleven](https://github.com/MouMou-Eleven) |

详细身份以 [`identity.md`](./identity.md) 为准，当前工作以 [`current.md`](./current.md) 为准，荣誉与案例证据以 [`knowledge/achievements.md`](./knowledge/achievements.md) 为准。

## 内容地图

| 入口 | 作用 | 何时读取 |
|---|---|---|
| [`AGENTS.md`](./AGENTS.md) | AI 协作、事实优先级和特殊项目规则 | 支持 AGENTS 的工具会自动读取；其他 AI 在长期协作前读取 |
| [`llms.txt`](./llms.txt) | 最小路由入口 | 每次进入仓库先读 |
| [`identity.md`](./identity.md) | 稳定身份、经历、能力边界 | 写个人介绍、讲师介绍、合作资料时 |
| [`current.md`](./current.md) | 当前项目和业务方向 | 判断“现在在做什么”时 |
| [`preferences.md`](./preferences.md) | 沟通、写作和工作偏好 | 生成内容或长期协作时 |
| [`open-questions.md`](./open-questions.md) | 跨文件事实冲突 | 使用荣誉、数字或争议口径前 |
| [`projects/README.md`](./projects/README.md) | 长期项目索引 | 进入具体项目时 |
| [`knowledge/README.md`](./knowledge/README.md) | 专业知识与能力索引 | 查技能、工具、案例和方法论时 |
| [`history/README.md`](./history/README.md) | 历史和修订说明 | 追溯旧决策时 |
| [`references/README.md`](./references/README.md) | 可复用规范与源码 | 需要执行级参考材料时 |
| [`STRUCTURE.md`](./STRUCTURE.md) | 结构、写入和维护规范 | 修改仓库前 |

## 长期维护原则

- 当前口径写在入口文件，历史变化写进 `revisions/` 或 `history/`。
- 新资料必须进入对应 README 索引，避免形成 AI 找不到的孤岛文件。
- 文件整理日期不等于事实确认日期；涉及价格、平台能力、项目进度时单独标明时效。
- 不确定的信息进入 `open-questions.md` 或项目待确认清单，不用猜测补齐。
- 提交前运行 `powershell -ExecutionPolicy Bypass -File scripts/validate-context.ps1`。

## 对外科普版

本仓库背后的方法论已整理为飞书文章：<https://www.feishu.cn/wiki/PqSHwL1nniP2pOkML25cZx2bnSb>
