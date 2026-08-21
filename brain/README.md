# Brain - 建委大脑

> 这里保存建委的跨领域认知，以及 AI 生成中文内容时默认调用的“AI 表达”基础层。AI 表达不是建委个人口吻，而是让任何中文输出符合中文语境、逻辑和质量要求的公共基础规则。

## 目录结构

```text
brain/
├── README.md                   建委大脑总入口、激活关系和写入边界
├── thinking-and-decisions.md   思维认知、判断习惯与决策方式
├── business-cognition.md       商业与增长认知
└── ai-expression/              AI 表达基础层
    ├── README.md               默认激活规则、表达层级和质量门槛
    ├── cross-domain-rules.md   跨领域中文质量、逻辑和搭配规则
    ├── oral-expression/        口语化表达
    │   └── README.md           口语化表达经验与检查清单
    ├── written-expression/     书面化表达
    │   └── README.md           书面化表达经验与检查清单
    ├── chinese-datasets/       中文数据、规则来源与质量检查
    │   ├── README.md           来源、授权、提炼和冲突治理规则
    │   ├── grammar-and-error-checklist.md
    │   │                       默认中文语法与病句检查
    │   ├── feitian-shanke/     中文技术科普表达参考数据集
    │   │   ├── README.md       数据集用途、来源和使用边界
    │   │   └── raw/            原始逐字稿，只在需要时读取
    │   │       └── feitian-shanke-transcript.txt
    │   └── short-video-outcome-and-motivation/
    │       ├── README.md       短视频逐字稿来源、核验和使用边界
    │       └── raw/
    │           └── two-video-transcripts.md
    └── experience/             AI 表达实践经验
        ├── README.md           经验索引和提炼规则
        └── spoken-argument-and-transition.md
                               口语化论证与前后承接方法
```

## 建委大脑的两层结构

| 层级 | 负责什么 | 什么时候调用 |
|---|---|---|
| 思维认知 | 建委怎样判断问题、做决策、看待商业和行动 | 分析建委的长期判断，或用户明确要求调用建委认知时 |
| AI 表达 | 任何中文 AI 内容的语言质量、逻辑、搭配和语境 | 只要 AI 生成、改写、润色、翻译或组织中文内容，默认调用 |

AI 表达不等于“建委本人说话方式”。它是一套用于提升中文输出质量的基础能力；建委个人经历、身份和真实项目事实仍分别以 `personal/`、`work/` 为准。

## 默认激活关系

```text
中文内容任务
└── 必须：brain/ai-expression/
    ├── 默认：跨领域规则 + 中文语法与病句检查 + AI 表达经验
    ├── 选择：口语化表达 或 书面化表达
    ├── 查看：中文数据与来源治理；原始语料按授权和任务需要读取
    └── 再叠加：一个最具体的领域 / 项目规则
```

示例：

- AI 培训课件 = `brain/ai-expression/` + `work/ai/training/`。
- AI 自媒体口播 = `brain/ai-expression/` + `work/ai/self-media/`。
- 飞书书稿章节 = `brain/ai-expression/` + `work/ai/publishing/`。
- 微课案例文案 = `brain/ai-expression/` + `work/design/microcourse-mg-animation/`。

领域规则负责专项适配，AI 表达负责中文基础质量；两者不能互相替代。用户明确要求组合多个领域时，才追加多个专项。

## 不自动激活的情况

- 只查询平台能力、项目状态、文件位置或技术事实时，不因为任务中出现“中文”就加载全部 AI 表达文件。
- 只执行代码、整理文件、运行测试或做结构校验时，不加载内容表达经验。
- 只有用户明确要求“模仿建委本人说话、个人口吻或个人思考”时，才需要把个人事实和思维认知作为额外层；AI 表达本身仍然默认适用生成任务。

## 写入边界

- 跨领域中文表达规则进入 `ai-expression/`。
- 口语化、书面化和数据集治理进入 `ai-expression/` 对应文件。
- 培训、自媒体、书稿、设计和项目专用规则进入 `work/` 对应领域。
- 建委本人的长期思维认知进入本目录根部的认知文件。
- 一次性修改意见只有在多个任务中验证或由建委明确确认后，才提炼为 AI 表达规则。

*边界确认：2026-08-21*
