# STRUCTURE.md — 仓库结构与写入规范

> 仅在准备写入、移动文件或调整结构时读取。本文件不属于日常问答的默认上下文。

## 一、仓库定位

本仓库同时承担四类职责：

1. **当前事实层**：建委是谁、现在做什么、偏好什么。
2. **项目决策层**：长期项目的当前口径、文件入口和修订历史。
3. **专业知识层**：可复用的方法、工具经验、案例与源码参考。
4. **历史追溯层**：旧版本、重要事件和方向变化，保留但不冒充当前事实。

设计目标是“入口轻、正文深、历史可追溯”。任何新增内容都必须能从一个 README 或 `llms.txt` 被找到。

## 二、当前目录结构

```text
ai-context/
├── AGENTS.md                 AI 协作规则、事实优先级、特殊项目规则
├── README.md                 人类入口和全局内容地图
├── llms.txt                  AI 最小路由入口
├── STRUCTURE.md              结构与写入规范
├── identity.md               稳定个人身份
├── current.md                当前状态与进行中事项
├── preferences.md            沟通和工作偏好
├── open-questions.md         跨文件事实冲突与待确认事项
├── knowledge/
│   ├── README.md             知识总索引
│   ├── achievements.md       荣誉、案例和影响力数据
│   ├── interests.md          长期关注方向
│   ├── tech-stack.md         能力与技术边界
│   ├── tools.md              工具清单和工具实操经验
│   ├── microcourse.md        微课业务知识
│   ├── windows-junction-migration.md
│   ├── ai-programming/       AI 编程知识包
│   └── ai-video/             AI 视频知识包
├── projects/
│   ├── README.md             长期项目总索引
│   └── <project>/
│       ├── README.md         项目当前口径和文件路由
│       ├── revisions/
│       │   ├── README.md     修订索引与有效性说明
│       │   └── YYYY-MM-DD-<slug>.md
│       └── <topic>.md        具体方案、方法、数据或复盘
├── history/
│   ├── README.md             历史入口和使用边界
│   └── timeline.md           跨项目重要里程碑
├── references/
│   ├── README.md             规范、源码与外部材料索引
│   └── <reference-package>/
└── scripts/
    ├── README.md             维护工具说明
    └── validate-context.ps1  断链、漏索引和目录检查
```

## 三、文件职责与权威顺序

| 文件类型 | 负责什么 | 不负责什么 |
|---|---|---|
| `current.md` | 当前进行中事项、近期业务方向 | 完整履历和历史事件 |
| `identity.md` | 稳定身份、教育背景、核心能力 | 实时项目进度 |
| `open-questions.md` | 跨文件冲突和确认动作 | 项目内部普通待办 |
| 项目 `README.md` | 项目当前口径、状态、边界、入口 | 保存每次变化的全部细节 |
| `revisions/*.md` | 记录为什么变、旧新差异 | 直接充当当前入口 |
| `knowledge/*.md` | 可复用知识和经过验证的经验 | 单个项目的临时进度 |
| `history/timeline.md` | 跨项目重要里程碑 | 每次提交或日常流水账 |
| `references/` | 可直接复用的规范、源码和原始材料 | 当前业务事实 |

冲突处理遵循 [`AGENTS.md`](./AGENTS.md) 的事实优先级。特别注意：修订记录可能包含已失效口径；原始材料可能比 Markdown 当前版更旧。

## 四、渐进式读取

### 日常读取

```text
llms.txt
  → 选择身份 / 当前状态 / 项目 / 知识入口
  → 读取目标 README 或单个专题文件
  → 只有任务需要时才进入修订、历史、长素材或源码
```

### 默认读取预算

- 简单问答：1 个入口文件。
- 对外简介或事实核对：2-3 个文件，并检查 `open-questions.md`。
- 项目任务：项目 README + 1-2 个专题文件。
- 复杂项目修订：项目 README + `revisions/README.md` + 与任务直接相关的修订。

不要为了“完整”自动加载 `all-docs.md`、全部 revisions、整个 history 或源码包。

## 五、项目 README 标准

每个项目 README 至少包含：

```markdown
# 项目名称

> 状态：进行中 / 已上线 / 暂停 / 已完成
> 当前口径确认：YYYY-MM-DD 或“未标注”
> 索引最后整理：YYYY-MM-DD

## 一句话介绍

## 当前确认事实

## 文件索引
| 文件 | 内容 | 何时读取 |

## 待确认事项

## 使用指南
```

规则：

- “当前口径确认”表示业务事实何时被确认；“索引最后整理”只表示文档维护时间，两者不能混写。
- 有方向变化时必须建立 `revisions/`；修订超过 1 个时必须增加 `revisions/README.md`。
- README 保持可快速读取。大量历史说明、完整方案和长清单放到专题文件，通过索引进入。

## 六、写入位置

| 新信息 | 写入位置 | 同步动作 |
|---|---|---|
| 当前正在做的新事项 | `current.md` | 必要时更新项目 README |
| 稳定身份或长期能力 | `identity.md` / `knowledge/` | 对外数据有冲突时更新 `open-questions.md` |
| 新长期项目 | `projects/<name>/README.md` | 更新 `projects/README.md` 和 `llms.txt` |
| 项目方向变化 | `projects/<name>/revisions/YYYY-MM-DD-*.md` | 更新项目 README 和 `revisions/README.md` |
| 可复用方法论 | `knowledge/<topic>/` | 更新最近一层 README |
| 可直接复制的源码/规范 | `references/<package>/` | 更新 `references/README.md` 和调用方索引 |
| 跨项目重要里程碑 | `history/timeline.md` | 最新日期写在前面 |

## 七、状态与历史标记

长材料和旧口径必须在文件开头使用清晰标记：

- `当前有效`：可以作为当前事实使用。
- `历史材料`：仅供追溯，不得覆盖当前 README。
- `已被取代`：必须指出替代文件或最新修订。
- `待确认`：不得对外写成确定事实。
- `参考实现`：可用于执行，但仍需检查适用环境和日期。

## 八、格式与安全

- 文件名和目录名使用 kebab-case；日期化修订使用 `YYYY-MM-DD-slug.md`。
- Markdown 使用 UTF-8、LF、相对链接和单一 H1。
- 技术术语可用英文，正文以中文为主。
- 不写入 API Key、Token、Cookie、密码、私密联系方式或可直接利用的凭证。
- 二进制原稿可以保留，但 README 必须说明它是当前版、历史版还是仅供打印分享。
- 不创建无人索引的文件；不创建空目录；不为了分类而制造只有一个句子的文件。

## 九、提交前检查

1. 运行 `powershell -ExecutionPolicy Bypass -File scripts/validate-context.ps1`。
2. 查看 `git status --short`，确认没有无关文件。
3. 检查新文件是否进入最近一层 README。
4. 检查是否需要新增修订记录或更新时间线。
5. 检查文件整理日期是否被误写成事实确认日期。
6. 推送后再通过远端文件列表或 GitHub 页面确认文件存在。

*最后整理：2026-07-10*
