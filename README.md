# Personal AI Context

> 杨建委的长期 AI 协作上下文中枢。仓库按个人、表达、项目、知识、治理和历史六棵树组织，避免信息平铺和新旧口径混用。

## 进入仓库

1. AI 先读 [`llms.txt`](./llms.txt)，按任务选择最小读取包。
2. 人类先从下面六个一级入口判断信息归属。
3. 只有写入、移动或调整结构时才读 [`STRUCTURE.md`](./STRUCTURE.md)。
4. 动态产品知识遵守 [`repository/versioned-knowledge-policy.md`](./repository/versioned-knowledge-policy.md)。

## 六个一级入口

| 一级入口 | 负责什么 | 典型内容 |
|---|---|---|
| [`personal/`](./personal/README.md) | 建委本人 | 身份、当前状态、荣誉、能力、兴趣、工具、待确认事实 |
| [`expression/`](./expression/README.md) | 怎样表达和传达知识 | 沟通偏好、教程写法、讲解方法、优秀来源材料 |
| [`projects/`](./projects/README.md) | 正在做的工作 | AI设计、AI编程、AI视频、AI培训、微课、付费社群、书稿、电脑环境 |
| [`knowledge/`](./knowledge/README.md) | 跨项目认知 | 第一性原理、思维方法、商业增长和长期见解 |
| [`repository/`](./repository/README.md) | 仓库怎样维护 | 结构、版本治理、校验、安全和写入规范 |
| [`history/`](./history/README.md) | 过去发生了什么 | 时间线、已归档项目和历史修订 |

## 根目录为什么只保留四个入口

| 文件 | 必须留在根目录的原因 |
|---|---|
| [`README.md`](./README.md) | GitHub 的人类默认入口 |
| [`AGENTS.md`](./AGENTS.md) | AI 工具自动发现的协作规则 |
| [`llms.txt`](./llms.txt) | AI 的最小路由入口 |
| [`STRUCTURE.md`](./STRUCTURE.md) | 结构调整时的权威规范 |

身份、偏好、待确认事项和工具信息都进入对应一级目录，不再占用根目录。

## 快速画像

| 项目 | 当前信息 |
|---|---|
| 姓名 | 杨建委（称呼：建委） |
| 身份 | AIGC 实战落地专家、资深跨界设计师、AI 视频创作人 |
| 公司 | 宿州市十一创动画科技有限公司（法人代表） |
| 坐标 / 时区 | 济南 / Asia/Shanghai |
| 核心能力 | 设计、微课与教育课件、AI 内容创作、AI 培训咨询、AI 应用落地 |
| GitHub | [MouMou-Eleven](https://github.com/MouMou-Eleven) |

详细事实以 [`personal/README.md`](./personal/README.md) 为准。

## 长期维护原则

- 当前入口只写当前有效口径，旧口径进入修订或历史。
- 新资料必须被最近一层 README 索引，不能形成孤岛文件。
- 原始资料跟随使用它的领域保存，不建立无上下文资料堆。
- 项目事实和跨项目方法分开；提炼知识时保留来源链接。
- 不写入密钥、Token、Cookie、密码和可直接利用的隐私数据。
- 提交前运行 `powershell -ExecutionPolicy Bypass -File repository/maintenance/validate-context.ps1`。

## 对外科普版

本仓库背后的方法论已整理为飞书文章：<https://www.feishu.cn/wiki/PqSHwL1nniP2pOkML25cZx2bnSb>
