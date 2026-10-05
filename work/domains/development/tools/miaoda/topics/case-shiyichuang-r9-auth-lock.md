# 案例：十一创导航 R9 后的认证锁抢占报错

- 日期：2026-10-05。
- 项目：十一创导航，百度秒哒。
- 状态：建委确认云端自动修复后网站使用正常；本轮仅分析与沉淀，没有修改或发布网站。

## 事实与证据

建委回传秒哒报错截图，原文为 `AbortError: Lock broken by another request with the 'steal' option.`，并说明上传R9后出现、经秒哒修复后正常。截图中的秒哒回执称修改了 `src/db/supabase.ts` 的自定义 auth.lock 和 `src/db/api.ts` 三处 getSession 异常处理，并报告慢刷新、外部抢锁、页面恢复和构建检查通过。这些是云端回执，尚未取得热修全文、哈希或独立线上复测。

Codex对本地R8/R9实物核对：上述两个文件、package.json、pnpm-lock.yaml逐字节相同；R9包11个文件中不含这四项。故没有证据支持“R9新增认证实现或升级依赖造成该异常”，也不是ZIP编码或TS语法报错。不能据此宣称与交付完全无关：完整应用继承了该运行时风险，R9验证也未覆盖此竞争场景。

锁文件解析到 `@supabase/auth-js@2.103.1`。本地源码 `src/lib/locks.ts` 的 AbortError分类受 `acquireTimeout>0` 条件限制；`GoTrueClient.ts` 的自动刷新tick使用0，getSession使用配置超时（默认5000ms）。这修正了截图摘要中“getSession固定走0”的表述；缺少线上完整堆栈，不能确定此次异常必经哪个调用点。

## 独立验证

在真实Chromium的两个同源页面中导入该版本原始 navigatorLock，实现持锁后由另一页调用 `navigator.locks.request(...,{steal:true})`，两边回调均受控，无生产账号或密钥：

| 持锁调用参数 | 实际结果 |
|---|---|
| acquireTimeout=0 | 原始AbortError，消息与截图完全一致，isAcquireTimeout=false |
| acquireTimeout=5000 | SDK分类错误，isAcquireTimeout=true |

这是锁辅助函数的隔离复现，不是完整登录刷新链路或线上热修验证。本地测试脚本 `work/qa/r9-lock-audit.mjs` 和结果 `r9-lock-audit-results.json` 保存在本次十一创导航工作区。

R9现有浏览器测试预置一小时有效session，模拟认证接口立即成功；虽有页面和状态回归，没有真正覆盖临近过期、慢刷新与抢锁。测试通过不能推导此场景可靠，这是此次需要补齐的交付检查。

## 热修保护与结果

R10增量6个文件同样不含上述两个认证文件，按manifest窄范围应用不会直接覆盖其热修。但根index.html也在R10范围内，云端回执还提到发布入口重建，必须保留云端入口适配，发生哈希冲突先回收，不能强行替换。未来全量复建前仍须合回热修文件；当前本地R9/R10完整源码不等于云端修复后的权威快照。

没有从截图猜写一份自定义锁来替换已经正常的云端实现，也没有把秒哒自报测试当作独立验证。可复用方法已写入 [认证专题](./authentication.md#会话刷新与浏览器锁竞争)，增量验收入口已补入 [workflow第6阶段](../workflow.md#第-6-阶段在本地修改和测试路径-b)。
