# 秒哒 AI 提示词入口

> 按主题复用可执行模板；不再默认读取支付、排错、SEO、上传、后端和登录的全部经验。
> 整理日期：2026-09-12。原模板来源和代码块保留在主题文件，平台事实核验日期不变。

## 最小执行结构

写清当前基线与事实 → 本批允许动作和保护范围 → 明确目标 → 已验证代码/资源/接口 → 成功与失败验收 → 实际修改和待测项回报。任务分批时每批自包含；真正涉及的能力依赖可以组合，不把无关主题全部激活。

## 任务索引

| 任务 | 读取 |
|---|---|
| 分批执行、保护功能、完整源码导入 | [执行与源码交接](./prompts/execution-and-handoff.md) |
| 版本化增量包 | [增量工作流](./patterns/codex-miaoda-iterative-increment-workflow.md)，先还原baseVersion全量树再叠加 |
| 支付、签名、回调、密钥 | [支付集成](./prompts/payment-integration.md) |
| 日志、Console/Network/真机排错 | [运行诊断](./prompts/runtime-diagnostics.md) |
| SEO与公开主体文案 | [SEO/内容](./prompts/seo-and-content.md) |
| 原生大文件、小程序上传 | [上传](./prompts/uploads.md) |
| 首轮应用形态与数据库持久化 | [后端存储](./prompts/backend-storage.md) |
| Auth与手机号身份一致性 | [登录](./prompts/authentication.md) |
| 模板收录、来源和维护方法 | [主题索引](./prompts/README.md) |

旧分片机制与兼容模板已进入 [legacy-contract.md](./reference-materials/video-chunked-upload/legacy-contract.md)，只有当前环境仍复现旧限制时读取。生成提示词之前核对平台为百度秒哒、当前环境和本轮授权；不把文档模板当成平台能力已实测的证明。
