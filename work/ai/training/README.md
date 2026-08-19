# AI Training — AI 培训

> 这里保存建委作为 AI 讲师开展企业培训、公开课和社群课程时的通用经验与具体项目。

## 目录结构

```text
training/
├── README.md     培训总入口
├── experience/   备课、课件、讲解、反馈和复盘经验
├── outlines/     可复用培训大纲
├── materials/    面向讲师或学员的培训资料索引
└── projects/     具体培训产品与长期项目
    └── paid-community-course/
```

## 读取路由

| 任务 | 首读 |
|---|---|
| 备课、课程设计、课件、现场反馈和复盘 | [`experience/README.md`](./experience/README.md) |
| 技术名词解释 | [`experience/technical-explanation/README.md`](./experience/technical-explanation/README.md) |
| 面向学员的实操教程 | [`experience/tutorial-writing.md`](./experience/tutorial-writing.md) |
| 查培训大纲 | [`outlines/README.md`](./outlines/README.md) |
| 查培训资料 | [`materials/README.md`](./materials/README.md) |
| AI 超级个体陪跑社群 | [`projects/paid-community-course/README.md`](./projects/paid-community-course/README.md) |

## 与其他领域的边界

- 生成培训课件、逐字稿、讲解说明或学员资料时，必须先调用 [`../../../brain/ai-expression/`](../../../brain/ai-expression/README.md) 负责中文质量，再调用本目录负责课程逻辑、内容呈现和培训适配。
- 微课、精品课、MG动画和教育交互课件是设计交付，进入 [`../../design/microcourse-mg-animation/`](../../design/microcourse-mg-animation/README.md)。
- 自媒体标题、文章、口播和直播销售进入 [`../self-media/`](../self-media/README.md)。
- AI 编程课程属于培训；只有需要真实开发事实时才按需组合 [`../programming/`](../programming/README.md)。
- AI 表达默认叠加；建委的思维认知只有用户明确要求时才从 [`../../../brain/`](../../../brain/README.md) 读取。

## 严格激活

- “AI 培训、企业培训、公开课、讲师备课、培训课件、培训资料、授课复盘”只进入本目录。
- 不因课程需要宣传就自动加载自媒体。
- 不因课程讲 AI 编程就自动加载全部编程知识库。
- 具体社群价格、权益和进度服从项目 README，不能由通用培训经验覆盖。

## 语言质量规则

中文搭配、逻辑和语境统一服从 [`../../../brain/ai-expression/cross-domain-rules.md`](../../../brain/ai-expression/cross-domain-rules.md)，不在培训目录复制维护。培训目录只补充培训专项：受众、课程逻辑、课件结构、演示方式、讲师与学员资料边界、反馈和复盘。

*结构确认：2026-08-20*
