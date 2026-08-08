# 2026-08-09：飞书平台与书稿风格误路由修订

## 事件

在一次“写入飞书文档的 AI 使用范式文章”任务中，错误读取并套用了 `projects/feishu-efficient-office/writing-style-analysis.md`。用户要求的是日常知识文章，并没有要求出版社书稿；最终内容因此带入了书稿专属的排版、章节和编辑交付思路。

## 已确认的根因

- 把“飞书文档”误当成“飞书书籍项目”。平台是承载工具，不能直接决定写作体裁。
- 没有先确认“写给谁”和“交付物是什么”，就选择了项目专属风格。
- 没有按 `llms.txt` 的最小路由读取 `expression/`，也没有优先使用已经提炼的通用表达方法。

## 新旧口径

旧的错误做法：看到飞书链接或“写飞书文档”，就读取飞书书稿风格。

当前有效做法：只有用户明确提到飞书书籍、出版社书稿或《飞书高效办公》章节，才进入 `projects/feishu-efficient-office/`。普通文章、技术科普和经验帖统一进入 `expression/`，按任务选择通用表达方法。飞天闪客材料对应的主要可调用方法是 [`problem-driven-technical-explanation.md`](../methods/problem-driven-technical-explanation.md)。

## 防复发检查

1. 先确认受众、用途和交付物，不因平台名称推断体裁。
2. 普通文章默认读取 `expression/README.md`、`trigger-rules.md`、`communication-preferences.md` 和匹配的 `methods/`。
3. “飞天闪客”是来源追溯线索，不是要求逐句模仿；优先调用已提炼的方法，必要时才读原始逐字稿。
4. 书稿专属规则不得外溢到日常文章、自媒体、培训或微课；这些交付物分别服从自己的项目规则。
5. 写入飞书前再次检查：平台要求和内容体裁是否被错误合并。

## 关联入口

- [`../README.md`](../README.md)
- [`../trigger-rules.md`](../trigger-rules.md)
- [`../source-materials/feitian-shanke/README.md`](../source-materials/feitian-shanke/README.md)
- [`../methods/problem-driven-technical-explanation.md`](../methods/problem-driven-technical-explanation.md)
- [`../../llms.txt`](../../llms.txt)
