# 秒哒（Miaoda）实战经验库

> 本目录沉淀建委在使用百度秒哒（MIAODA）平台过程中积累的实战经验、踩坑记录、提示词模板、接入案例，以及对官方版本/渠道/Skill 反向能力的事实归类。

> 注意：中文「miǎodā」存在多个同名产品，进入正文前先看 [disambiguation.md](./disambiguation.md) 确认上下文。本目录所有文件指**百度秒哒 MIAODA**（miaoda.cn）。
> **不要把飞书妙搭 Spark 的经验写进本目录。** 飞书妙搭属于飞书生态低代码/无代码工具，未来应单独放到 `projects/ai-programming/feishu-spark/`。

> **动态产品规则**：秒哒功能、计费、渠道和界面持续变化。回答“现在能不能做、当前怎么操作”时，先读本 README 和当前专题，并重新核验官方资料或实际环境。`version-features.md` 是历史时间线，不是当前能力清单。维护规则见 [`../../../repository/versioned-knowledge-policy.md`](../../../repository/versioned-knowledge-policy.md)。

> AI Agent 进入本目录请先读 [llms.txt](./llms.txt)，它按"查 / 建 / 抄"三种意图路由到具体文件。

## 文档索引

| 文件 | 内容 | 何时该读 |
|---|---|---|
| [llms.txt](./llms.txt) | AI Agent 入口索引：按"查 / 建 / 抄"路由 | AI 第一次进入本目录时 |
| [disambiguation.md](./disambiguation.md) | 同名产品辨析：百度秒哒 MIAODA vs 飞书妙搭 Spark，含路由判断表 | 用户提到「秒哒/妙搭」但没说清是哪个时（必读） |
| [platform-basics.md](./platform-basics.md) | 秒哒平台的基础认知：四套运行时、自定义技能机制、与应用层的关系、后端服务、首轮形态/存储/环境决策、共享后端、资源套餐、快速/深度计费、定时任务等 | 第一次接触秒哒、或要做技术决策前 |
| [version-features.md](./version-features.md) | 历史版本节点速查表：记录能力何时出现、改变或被取代 | 追溯版本变化时；不得直接当作当前能力清单 |
| [publish-channels.md](./publish-channels.md) | 4 种发布渠道（Web / 秒哒官方小程序 web-view / 用户自有原生小程序 / 原生 APP）的能力边界、限制、选型建议；含 V3.5 iOS 打包/分发与自定义分享网址 | 用户问「我的应用要不要做小程序/做 APP」或「分享链接/域名怎么做」时 |
| [skill-development.md](./skill-development.md) | 自定义技能开发指南：.zip 包结构、SKILL.md frontmatter、脚本约定、环境变量，以及 V3.5 的对话创建、导入和 API 文档创建入口 | 要为秒哒开发自定义技能时 |
| [skill-as-callable.md](./skill-as-callable.md) | 反向能力：秒哒被打包为 Skill，可被 OpenClaw / Claude Code 等外部 Agent 调用（V2.5 上线） | 想把秒哒嵌进更大的 Agent 工作流、或做应用批量化生产时 |
| [pitfalls.md](./pitfalls.md) | 22 个真实踩坑清单：MD5 Web Crypto 死路、密钥泄漏、无 Supabase 控制台、多通道退款误路由、**旧后端大视频上传三层墙**、**SPA SEO 漏 keywords**、**微信恢复访问 txt 校验失败**、**浏览器缓存伪存储**、**应用形态强转**、**登录自写 Edge Function**、**+86 手机号身份重复/登录失败**等 | 遇到怪异报错、或想预防性避雷时 |
| [prompt-patterns.md](./prompt-patterns.md) | 与秒哒 AI 协作的提示词模板：@技能调用、红线前置、**全站 SEO**、**大文件先测试 + 旧分片代理兜底**、**首轮形态 + 真实后端存储**、小程序上传、Supabase Auth、+86 手机号标准化等 | 要写一段让秒哒按计划执行的提示词时 |
| [patterns/codex-assisted-workflow.md](./patterns/codex-assisted-workflow.md) | Codex 辅助秒哒开发工作流：用户把秒哒问题交给 Codex，Codex 拆成低风险提示词，用户逐批粘贴到秒哒执行并反馈结果 | 以后遇到任何秒哒开发/修复/整改需求，想让 Codex 先出方案和提示词时 |
| [patterns/seo-optimization.md](./patterns/seo-optimization.md) | 秒哒站点 SEO 优化处方：V3.5 SEO Agent、`index.html`、`SEOHead`、`react-helmet-async`、每页 `keywords` / `description`、`robots.txt` / `sitemap.xml` 检查 | 要给秒哒生成的网站做全站 SEO 时 |
| [patterns/wechat-urlsec-verification.md](./patterns/wechat-urlsec-verification.md) | 微信内置浏览器安全弹窗恢复访问验证处方：根目录 txt 验证、公网 `curl` 验收、SPA fallback 排查 | 微信访问网站出现“无法确认该网页的安全性”，或恢复访问验证文件校验失败时 |
| [patterns/content-rectification-prompts.md](./patterns/content-rectification-prompts.md) | 秒哒内容整改提示词拆分处方：备案主体一致性、品牌/协会/人物口径、SEO/分享隐藏文案、栏目名称、商品详情经营主体说明 | 要让秒哒分批修改网站公开文案、主体口径或备案整改内容时 |
| [patterns/large-video-upload.md](./patterns/large-video-upload.md) | 大文件上传决策：7月15日后先做 200MB 能力测试；原生上传优先，旧分片 + Range 代理仅作兼容兜底 | 要落地大视频上传或判断旧 50MB 限制是否仍适用时 |
| [case-yungouos-jsapi.md](./case-yungouos-jsapi.md) | 完整接入案例：YunGouOS 微信 JSAPI 支付从需求到上线的全过程，含每轮失败与修复 | 做支付接入、或想看一个端到端样板时 |
| [`reference-materials/video-chunked-upload/`](./reference-materials/video-chunked-upload/README.md) | 旧环境生产验证过的视频分片上传源码 | 当前环境能力测试仍复现旧限制时 |
| [`revisions/README.md`](./revisions/README.md) | 动态功能变化、取代关系和当前有效性索引 | 新旧功能冲突或追溯版本变化时 |

## 重要原则（来自实战）

1. **秒哒文档与实际行为有差异**——例如自定义技能 SKILL.md 必须有 YAML frontmatter，但官方文档没写。永远以实际报错为准。
2. **秒哒的"技能运行时"与"应用运行时"是两个独立环境**——密钥、环境变量、运行的语言都不互通。
3. **秒哒 AI 是"指令式执行"**——不能像 Claude/ChatGPT 那样多轮讨论后再动手，发指令就直接改代码。所以提示词必须一次写到位。
4. **秒哒 AI 容易自由发挥**——如果不在提示词里明确禁止它"自己实现某功能"，它会绕过你提供的技能/参考代码，自己另写一遍，且大概率翻车。

## 维护约定

- 每次完成一次有价值的秒哒实战，把"非官方文档可得"的经验追加到对应文件里
- 新增踩坑记录到 [pitfalls.md](./pitfalls.md)
- 新增提示词模板到 [prompt-patterns.md](./prompt-patterns.md)
- 重复实施 ≥ 2 次的复杂方案，沉淀为 `patterns/<name>.md`（处方）+ 配套的可抄源码到 `reference-materials/<name>/`
- 完整端到端案例新建一个 `case-<name>.md` 并在本 README 索引里加一行
- 已经写进 [skill-development.md](./skill-development.md) 的内容不要重复散落到其他文件
- 新功能出现时先全仓搜索旧口径；旧口径退出当前专题，只进入 `version-features.md` 或日期化修订，并标明取代关系
