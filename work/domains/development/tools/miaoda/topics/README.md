# 秒哒专题

按问题找。每个专题讲这类问题在秒哒上怎么做、提示词怎么写、踩过什么坑。整体协作流程见 [workflow.md](../workflow.md)，限额见 [facts.md](../facts.md)。

| 问题 | 专题 |
|---|---|
| 大文件上传、小程序上传 | [uploads.md](./uploads.md)；决策流程见 [large-video-upload.md](./large-video-upload.md) |
| 登录、验证码、手机号身份、会话刷新锁竞争 | [authentication.md](./authentication.md)；[十一创R9锁竞争复盘](./case-shiyichuang-r9-auth-lock.md) |
| 支付、签名、回调、退款 | [payment.md](./payment.md)；完整案例 [YunGouOS JSAPI](payment-case-yungouos-jsapi.md) |
| 云端或真机报错、日志面板、排错 | [runtime-diagnostics.md](./runtime-diagnostics.md) |
| 数据存哪里、首轮形态、localStorage 迁数据库 | [backend-storage.md](./backend-storage.md) |
| SEO | [seo-and-content.md](./seo-and-content.md)（提示词）、[seo-optimization.md](./seo-optimization.md)（全站方法） |
| 网站公开内容和主体口径整改 | [content-rectification.md](./content-rectification.md) |
| 微信网址安全验证 | [wechat-urlsec-verification.md](./wechat-urlsec-verification.md) |

新经验改对应专题的原文。一个问题只放一个专题，其他专题用链接。

**来源与状态**：支付、上传、登录、排错、存储、SEO 几个专题的提示词片段于2026-09-12从原提示词合集按主题拆出，原始版本在 Git 历史里，拆分时没有重新实测秒哒产品能力。片段里的页面名、接口、路径和配置是当时案例的条件，执行前替换为当前项目已核验的事实。
