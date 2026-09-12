# 登录与手机号身份一致性

> 来源：从原 [prompt-patterns.md](../prompt-patterns.md) 的实战模板按主题整理，原始版本由Git历史保留；2026-09-12仅拆分与明确适用边界，未重新实测秒哒产品能力。
> 模板中的页面名、接口、路径和配置是对应案例条件；执行前替换为当前项目已核验事实。查看模板不代表已授权收费、部署或外部发送。

> 仅在当前项目已经采用Supabase Auth或对应秒哒用户体系、并复现所述故障时使用；“中国手机号”规范化只覆盖本案例业务范围，不据此改全球号码规则或自动合并旧账户。

## 登录：优先使用 Supabase Auth，不要自写 Edge Function

**适用场景**：短信验证码登录报 `Edge Function returned a non-2xx status code`，或登录注册流程被秒哒自己包了一层后端函数。

```text
当前短信验证码登录失败。请不要继续使用自写 Edge Function 实现登录。

红线：
- 登录、注册、验证码、会话管理优先使用 Supabase Auth / 秒哒内置用户体系。
- 不要自己重新实现验证码校验、session 生成、用户身份写入逻辑。
- 不要破坏现有用户表、权限字段和管理员判断逻辑。

任务：
1. 检查当前登录流程是否绕过了 Supabase Auth。
2. 如果存在自写登录 Edge Function，请删除或停用其登录职责。
3. 改为 Supabase Auth / 秒哒内置用户体系支持的登录注册方式。
4. 完成后检查登录后用户身份、管理员权限、历史数据读取是否正常。

完成后请说明：
1. 前端现在调用的 Auth 方法或登录入口。
2. 是否仍有自写登录 Edge Function 残留。
3. 如何测试登录、退出、重新登录和权限识别。
```

## 手机号注册登录：先规范化再查用户

**适用场景**：手机号裸号与 `+86` 写法被注册成两个账户；手机号登录偶发“密码错误”；旧用户兼容登录失败；注册成功但 session 为 `null` 后表单被清空。对应根因和验收清单见 [pitfalls.md #22](../pitfalls.md#22-手机号未做唯一身份规范化--86-与裸号变成两个账户--登录失败)。

**提示词模板**：

```text
请严格修复当前 Login.tsx 的手机号注册与登录一致性问题。本批只允许修改登录/注册相关的前端逻辑和既有的用户查询调用；不要修改订单、支付、权限、业务数据表或无关页面。

红线（必须遵守）：
- 手机号是唯一身份键，不是展示字符串。`+8613xxxxxxxxx` 与 `13xxxxxxxxx` 必须识别为同一个用户。
- 任何注册、登录、RPC 查询、catch 兜底、旧用户兼容、Auth email 拼接都禁止继续使用原始 input；只能使用规范化后的 normalizedInput。
- 不要在不同分支手写 `${input}@miaoda.com`、`phone_${input}@miaoda.com` 或其他 email 拼接；必须集中为一个 helper。
- 修改前先检查当前注册分支和已存在用户实际使用的 Auth email 公式。不要猜是 `phone_<手机号>@miaoda.com` 还是 `<手机号>@miaoda.com`，不要批量改写旧用户 email，也不要自动合并已有账户。
- 保持现有 Supabase Auth / 秒哒内置用户体系，不要新增自写登录 Edge Function。

任务：
1. 新建或复用 normalizeChinaPhone(raw)；清理空格和连接符，输入以 +86 开头时去掉 +86，最终只接受 11 位、1 开头的中国手机号。得到 normalizedInput 后，后续逻辑只传这个值。
2. 新建或复用 toPhoneAuthEmail(normalizedPhone)。它必须使用当前注册流程已生效的 email 公式；注册、正常登录、catch 兜底和旧用户兼容路径都调用它。
3. getUserByPhone 必须传 normalizedInput。RPC 异常进入 catch 时，也必须用 toPhoneAuthEmail(normalizedInput) 登录，绝不能使用原始 input。
4. 旧用户兼容路径的 getUserByUsername 必须传 normalizedInput；成功后的 Auth email 同样调用 toPhoneAuthEmail(normalizedInput)。
5. 注册成功但 session 为 null 时，自动切换到登录 Tab，并把 normalizedInput 预填进当前“用户名/手机号”表单字段；用户只需要补输密码。
6. 注册前先按 normalizedInput 查重，阻止 +86 与裸号再次产生两个新账户。

验收要求：
1. 用 13xxxxxxxxx 注册后，再用 +8613xxxxxxxxx 登录，必须命中同一个用户 ID。
2. 用 +8613xxxxxxxxx 注册后，再用 13xxxxxxxxx 登录，必须命中同一个用户 ID。
3. 模拟 getUserByPhone 抛异常时，catch 兜底仍能用规范化手机号登录，不能误报密码错误。
4. 旧用户兼容分支在两种输入格式下都能命中同一用户。
5. 模拟注册成功但 session 为 null 时，页面自动进入登录 Tab，手机号字段已预填规范化号码。
6. 输出实际确认的 email 公式、修改的文件/函数、未处理的旧账户迁移风险；不要只给 Summary。
```
