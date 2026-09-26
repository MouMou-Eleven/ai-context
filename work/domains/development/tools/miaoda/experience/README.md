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

更新保存报 `PgRestWhitelistError:42703`、或用户已在云端热修复后继续交付增量包时，先读[踩坑 #28：PATCH JSON 路径与网关兼容性](./pitfalls.md#28-patch-的-json-路径过滤触发网关白名单错误被误读为数据库缺列)。它记录本项目证据和检查动作，不代表所有环境的通用限制。

版本化的“Codex审查 → 秒哒执行 → 正式域名验收 → 用户反馈”闭环见 [`patterns/codex-miaoda-iterative-increment-workflow.md`](./patterns/codex-miaoda-iterative-increment-workflow.md)。

新增经验先确定当前问题、平台/版本、执行结果和适用边界；模板只写入一个主题，再从相关处方引用。主题拆分或路径变化同时维护本索引、prompts/README和旧引用，不把历史平台限制重新提升为默认规则。

尽快还原或一次给齐，读[一次交付批次](./patterns/codex-miaoda-iterative-increment-workflow.md#一次交付批次与有效完成)。只查套餐、状态不触发开发。
