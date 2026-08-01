# STRUCTURE.md — 仓库结构与写入规范

> 仅在准备写入、移动文件或调整结构时读取。本文件不属于日常问答的默认上下文。

## 一、设计目标

仓库按“先大后小”的树形逻辑组织。一级目录只表达稳定的大类，具体资料逐层落到工作领域、项目、专题、来源或修订中。

设计原则：

1. 根目录只保留人类入口、AI 规则、AI 路由和结构规范。
2. 个人、表达、项目、认知、治理、历史六棵树各自负责一种信息。
3. 当前入口只保留当前口径，旧口径进入修订或历史。
4. 原始资料跟随使用它的领域保存，不建立脱离上下文的全局资料堆。
5. 每份资料都能从最近一层 README 找到。

## 二、当前目录结构

```text
ai-context/
├── README.md                         人类总入口
├── AGENTS.md                         AI 协作与事实规则
├── llms.txt                          AI 最小读取路由
├── STRUCTURE.md                      结构与写入规范
├── personal/                         建委本人
│   ├── README.md
│   ├── identity.md                   稳定身份与经历
│   ├── current-focus.md              当前重点与阶段状态
│   ├── achievements.md               荣誉与代表成果
│   ├── capabilities.md               能力边界
│   ├── interests.md                  长期关注方向
│   ├── toolbox.md                    常用工具入口
│   └── open-questions.md             跨文件冲突与待确认事实
├── expression/                       表达、写作与知识讲解
│   ├── README.md
│   ├── trigger-rules.md              自然语言触发与组合调用
│   ├── communication-preferences.md  沟通与去 AI 味偏好
│   ├── methods/                      按作用命名的可调用方法
│   ├── tutorial-writing/             教程与学员资料写法
│   └── source-materials/              外部优秀原始材料与来源
├── projects/                         工作领域与长期项目
│   ├── README.md
│   ├── ai-design/                    AI 设计工作领域
│   ├── ai-programming/               AI 编程工作领域，含秒哒
│   ├── ai-video/                     AI 视频工作领域
│   ├── ai-training/                  AI 培训与讲师工作领域
│   ├── microcourse/                  微课与教育课件工作领域
│   ├── paid-community-course/        付费社群课程项目
│   ├── feishu-efficient-office/      飞书书籍项目与飞书专属规范
│   ├── inshan-popupiano/             Inshan POPUPIANO 项目
│   └── computers/                    电脑与本地环境档案
├── knowledge/                        跨项目认知
│   ├── README.md
│   ├── thinking/                     第一性原理与思维方法
│   └── business-growth.md            商业增长与经营认知
├── repository/                       仓库治理
│   ├── README.md
│   ├── versioned-knowledge-policy.md 动态产品知识治理
│   └── maintenance/                  校验工具与维护说明
└── history/                          历史与追溯
    ├── README.md
    ├── timeline.md                   跨项目重要里程碑
    └── archived-projects/            已退出主线的完整项目
```

## 三、一级目录职责

| 一级目录 | 负责什么 | 不负责什么 |
|---|---|---|
| `personal/` | 建委本人的稳定事实、当前状态、能力和冲突 | 写作方法、项目过程和产品知识 |
| `expression/` | 怎样表达、解释、写教程和学习优秀案例 | 培训课程设计、微课制作或项目事实 |
| `projects/` | 工作领域、长期项目、工具经验、案例和迭代 | 与任何项目无关的长期认知 |
| `knowledge/` | 跨多个项目仍成立的思维与经营认知 | 单个项目的进度、工具版本或客户资料 |
| `repository/` | 仓库维护、版本治理、校验和安全 | 业务知识正文 |
| `history/` | 旧项目、旧口径和跨项目里程碑 | 当前事实入口 |

## 四、工作领域与具体项目

`projects/` 下允许两种同级目录：

- 工作领域：持续积累一种长期工作的经验，例如 AI 设计、AI 编程、AI 视频、AI 培训、微课。
- 具体项目：有明确产品、客户、书稿或经营目标，例如付费社群、飞书书籍、Inshan。

工作领域之间按主要交付物划分，不按“是否使用 AI”或“是否出现课程”划分：

| 场景 | 正确位置 |
|---|---|
| 建委作为讲师开展企业培训、公开课、备课和授课 | `projects/ai-training/` |
| 为教师制作微课、精品课、参赛课和教育交互课件 | `projects/microcourse/` |
| 开发网站、应用、自动化或记录秒哒经验 | `projects/ai-programming/` |
| 制作宣传片、AI 影片或沉淀视频流程 | `projects/ai-video/` |
| 制作商业视觉、PPT、UI 或设计方法 | `projects/ai-design/` |

同一任务跨领域时，指定一个主归属，其他领域用相对链接引用，不复制两份正文。

## 五、项目 README 标准

每个长期工作领域或项目 README 至少说明：

```markdown
# 名称

> 状态：进行中 / 长期沉淀 / 暂停 / 已完成
> 当前口径确认：YYYY-MM-DD 或“未标注”

## 定位与边界
## 当前确认事实
## 文件索引
## AI 调用规则
## 待确认事项
```

“当前口径确认”表示业务事实何时被确认；“索引最后整理”只表示文档维护时间，两者不能混写。README 保持可快速读取，大量历史和长素材放入专题文件。

## 六、修订与动态产品

- 重要方向变化写入 `revisions/YYYY-MM-DD-<slug>.md`，并更新 `revisions/README.md`。
- 当前 README 只保留最新有效口径，修订记录解释为什么变和旧口径是什么。
- 秒哒、飞书、Codex、模型、平台 API、价格和界面路径等动态知识必须遵守 [`repository/versioned-knowledge-policy.md`](./repository/versioned-knowledge-policy.md)。
- 动态事实必须记录适用版本或环境、来源、核验日期和取代关系。
- 历史不能无痕删除，但不能与当前规则并列成同等有效。

## 七、表达来源与方法提炼

- 原始文章、逐字稿和作者材料进入 `expression/source-materials/<source>/`。
- 可长期调用的方法进入 `expression/methods/`，按作用命名，不按作者姓名命名。
- 用户用“参考仓库里的语言表达习惯”等通用语义即可触发方法，不要求记住作者。
- “语言风格、语言表达习惯、语言类案例”等表达词可以与“自媒体、AI 培训、微课”等领域词组合，详细规则以 `expression/trigger-rules.md` 为准。
- 只学习叙事、拆解、逻辑和知识传达方式，不复制标志性措辞，不把来源中的事实写成建委事实。

## 八、写入判断

| 新信息 | 写入位置 | 同步动作 |
|---|---|---|
| 当前重点变化 | `personal/current-focus.md` | 必要时更新项目 README 和时间线 |
| 稳定身份、能力或荣誉 | `personal/` 对应文件 | 冲突时更新 `personal/open-questions.md` |
| 新工作领域或长期项目 | `projects/<name>/README.md` | 更新 `projects/README.md` 和 `llms.txt` |
| 项目方向变化 | 项目 `revisions/` | 更新项目 README 和修订索引 |
| 项目或工具经验 | 对应项目或工作领域 | 更新最近一层 README |
| 跨项目思维与经营认知 | `knowledge/` | 保留验证来源或项目链接 |
| 优秀表达原始材料 | `expression/source-materials/` | 提炼方法时更新 `expression/methods/` |
| 跨项目重要里程碑 | `history/timeline.md` | 最新日期在前 |
| 已退出主线项目 | `history/archived-projects/` | 更新归档索引、时间线和 `llms.txt` |

## 九、渐进式读取

```text
llms.txt
  → 选择 personal / expression / projects / knowledge / repository / history
  → 读取目标 README
  → 读取 1-2 个直接相关专题
  → 只有追溯或核对来源时进入 revisions、history、source-materials
```

- 简单问答：1 个入口。
- 对外简介：2-3 个个人文件，并检查待确认事实。
- 项目任务：项目 README + 1-2 个专题。
- 复杂修订：项目 README + 修订索引 + 直接相关修订。

不要为了完整自动加载全部修订、时间线、原始资料或源码包。

## 十、格式、安全与提交

- 文件和目录使用 kebab-case；日期化修订使用 `YYYY-MM-DD-slug.md`。
- Markdown 使用 UTF-8、LF、相对链接和单一 H1。
- 不写入 API Key、Token、Cookie、密码、私密联系方式、内部地址或可直接利用的凭证。
- 不创建无人索引的文件、空目录或只为分类而存在的一句话文件。
- 提交前运行 `powershell -ExecutionPolicy Bypass -File repository/maintenance/validate-context.ps1`。
- 查看 `git status --short` 和差异范围，确认没有无关文件或敏感信息。
- 推送后验证远端分支和对应文件存在。

*最后整理：2026-08-02*
