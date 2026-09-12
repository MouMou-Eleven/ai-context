# 秒哒实战经验

| 分类 | 入口 | 内容 |
|---|---|---|
| 踩坑 | [`pitfalls.md`](./pitfalls.md) | 真实报错、根因和规避方式 |
| 提示词导航 | [`prompt-patterns.md`](./prompt-patterns.md) | 当前任务的短入口 |
| 主题模板 | [`prompts/README.md`](./prompts/README.md) | 执行、支付、诊断、SEO/内容、上传、后端、登录七类模板 |
| 案例 | [`cases/`](./cases/README.md) | 完整端到端案例 |
| 处方 | [`patterns/`](./patterns/README.md) | 重复验证过的解决方案 |
| 参考源码 | [`reference-materials/`](./reference-materials/README.md) | 只有执行方案需要时才读取的源码 |

单次问题先记录在踩坑或案例；重复验证后再提炼为处方。

版本化的“Codex审查 → 秒哒执行 → 正式域名验收 → 用户反馈”闭环见 [`patterns/codex-miaoda-iterative-increment-workflow.md`](./patterns/codex-miaoda-iterative-increment-workflow.md)。

新增经验先确定当前问题、平台/版本、执行结果和适用边界；模板只写入一个主题，再从相关处方引用。主题拆分或路径变化同时维护本索引、prompts/README和旧引用，不把历史平台限制重新提升为默认规则。
