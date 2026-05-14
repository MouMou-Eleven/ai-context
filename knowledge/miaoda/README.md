# 秒哒（Miaoda）实战经验库

> 本目录沉淀建委在使用百度秒哒（MIAODA）平台过程中积累的实战经验、踩坑记录、提示词模板和接入案例。
> 所有内容来自真实项目（非官方文档复述），用于让未来的 AI 协作者快速建立对秒哒的实战认知，避免重复踩坑。

## 文档索引

| 文件 | 内容 | 何时该读 |
|---|---|---|
| [platform-basics.md](./platform-basics.md) | 秒哒平台的基础认知：四套运行时、自定义技能机制、与应用层的关系、文档与实现差异等 | 第一次接触秒哒、或要做技术决策前 |
| [skill-development.md](./skill-development.md) | 自定义技能（.zip 包）开发指南：目录结构、SKILL.md frontmatter、脚本约定、环境变量 | 要为秒哒开发自定义技能时 |
| [pitfalls.md](./pitfalls.md) | 9 个真实踩坑清单：MD5 Web Crypto 死路、密钥泄漏、嵌套目录、AI 自动重写签名 等 | 遇到怪异报错、或想预防性避雷时 |
| [prompt-patterns.md](./prompt-patterns.md) | 与秒哒 AI 协作的提示词模板：@技能调用风格、红线前置、分工边界、设备识别函数注入等 | 要写一段让秒哒按计划执行的提示词时 |
| [case-yungouos-jsapi.md](./case-yungouos-jsapi.md) | 完整接入案例：YunGouOS 微信 JSAPI 支付从需求到上线的全过程，含每轮失败与修复 | 做支付接入、或想看一个端到端样板时 |

## 重要原则（来自实战）

1. **秒哒文档与实际行为有差异**——例如自定义技能 SKILL.md 必须有 YAML frontmatter，但官方文档没写。永远以实际报错为准。
2. **秒哒的"技能运行时"与"应用运行时"是两个独立环境**——密钥、环境变量、运行的语言都不互通。
3. **秒哒 AI 是"指令式执行"**——不能像 Claude/ChatGPT 那样多轮讨论后再动手，发指令就直接改代码。所以提示词必须一次写到位。
4. **秒哒 AI 容易自由发挥**——如果不在提示词里明确禁止它"自己实现某功能"，它会绕过你提供的技能/参考代码，自己另写一遍，且大概率翻车。

## 维护约定

- 每次完成一次有价值的秒哒实战，把"非官方文档可得"的经验追加到对应文件里
- 新增踩坑记录到 [pitfalls.md](./pitfalls.md)
- 新增提示词模板到 [prompt-patterns.md](./prompt-patterns.md)
- 完整端到端案例新建一个 `case-<name>.md` 并在本 README 索引里加一行
- 已经写进 [skill-development.md](./skill-development.md) 的内容不要重复散落到其他文件