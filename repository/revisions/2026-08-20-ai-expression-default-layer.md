# 2026-08-20 AI 表达默认层修订

## 触发原因

旧结构把“建委本人的口语、表达逻辑和语言习惯”放在单个 `brain/personal-expression.md` 中，容易把个人口吻、中文基础质量和领域专项表达混在一起。与此同时，培训、自媒体和书籍目录分别维护相同的中文搭配规则，后续容易重复、冲突和过期。

直播逐字稿中出现的“先把话说稳一点”“有人把你卡住的地方接住”等问题，也说明中文质量规则不能只挂在某一个领域下：这些是跨领域的主谓宾、语境和动词搭配问题。

## 本次确认

- 当前路径为 `brain/cognition/thinking-and-decisions.md` 和 `brain/cognition/business-cognition.md`，继续保存建委本人的思维与商业认知；2026-08-22 仅调整了归组位置，没有把 AI 表达重新改回个人口吻。
- 原个人表达入口改为 `brain/ai-expression/`，定位为所有中文 AI 内容的默认基础层，不再声明为建委个人口吻。
- AI 表达下设中文数据集、AI 表达经验、口语化表达和书面化表达；跨领域语言质量规则在该目录统一维护。
- 任何中文生成、改写、润色、翻译或内容组织任务，先调用 AI 表达，再叠加一个最具体的专业领域。
- AI 培训内容调用“AI 表达 + AI 培训”；AI 自媒体内容调用“AI 表达 + AI 自媒体”。除非建委明确要求组合，不激活无关领域。
- 中文数据集默认不读取，来源、授权和用途未确认的外部材料不得声明为可训练数据。

## 新旧差异

| 旧口径 | 当前口径 |
|---|---|
| 建委个人表达是一个单文件 | AI 表达是有独立子目录和治理规则的中文基础层 |
| 个人口语、表达逻辑和语言习惯默认代表建委 | AI 表达改善所有中文内容，不自动模仿建委本人 |
| 培训、自媒体、书籍分别复制通用语言规则 | 通用规则只在 AI 表达维护，各领域只保留专项适配 |
| 来源材料放在培训讲解方法下 | 可跨领域复用的中文材料进入中文数据集，并单独登记授权边界 |

## 当前权威位置

- 默认激活与目录边界：[`brain/ai-expression/README.md`](../../brain/ai-expression/README.md)
- 跨领域中文质量：[`brain/ai-expression/cross-domain-rules.md`](../../brain/ai-expression/cross-domain-rules.md)
- 口语化表达：[`brain/ai-expression/oral-expression/README.md`](../../brain/ai-expression/oral-expression/README.md)
- 书面化表达：[`brain/ai-expression/written-expression/README.md`](../../brain/ai-expression/written-expression/README.md)
- 中文数据集治理：[`brain/ai-expression/chinese-datasets/README.md`](../../brain/ai-expression/chinese-datasets/README.md)

本文件只保留修订原因和新旧差异，具体执行规则以上述当前入口为准。
