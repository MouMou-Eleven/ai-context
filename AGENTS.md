# AI 协作规则

本仓库是杨建委的长期 AI 协作事实中枢。建委只需说明任务或要求沉淀的领域，AI负责检索、必要依赖、去重、索引更新和验收，不把维护步骤转嫁给建委。

## 任务开始

1. 实际检查仓库版本和目录；读本文件与 [llms.txt](./llms.txt)，按任务进入最近的README。只查状态或位置时不加载创作规则。
2. 以一个主任务确定事实归属，自动读取完成任务必需的其他领域方法和工具，不需要建委另说“结合”。一个文件只存一处，相关入口用链接双向发现。
3. 先判断目标、对象、交付物、项目/场次，再选方法。关键词是查找线索，不是无条件执行命令；课号、同一平台或相似主题不能证明属于同一项目。
4. 默认先入口和短规则，再按需读取具体方法、证据和执行Skill。无固定文件数量上限；不得为了省读取漏掉必要约束，也不默认读取全部源码、原文或历史。
5. 承载平台不决定业务归属：飞书课程文档不等于飞书书籍；百度“秒嗒/秒哒”、miaoda.cn、*.appmiaoda.com不是飞书妙搭。百度任务禁止使用lark-apps/Spark接口，先读[产品辨析](./work/ai/programming/tools/miaoda/disambiguation.md)。

## 事实、规范、工具分别判断

- 建委当前明确确认决定个人目标、偏好、项目归属和商业约定；不得用旧记录覆盖。本次确认不等于外部产品客观能力已经核验。
- 项目README负责指向当前权威记录。状态、价格、权益、章节和课程各自指定唯一来源；发现更新的适用证据与入口不一致时，报告差异并更新，不机械认定README永远正确。
- 外部功能、菜单、版本、价格和API按适用账号/版本/环境核验来源与日期，遵守[动态知识政策](./repository/versioned-knowledge-policy.md)。
- 方法要注明适用条件与验证程度；项目事实不能从示例或模板推导。工具说明不证明本机已安装，已安装不等于本轮已执行。
- 无法消解时区分已确认、待确认和已被替代；继续独立可做的工作，不编造空白。

## 必须保持的业务边界

- 中文成品默认先读[AI表达短卡](./brain/ai-expression/README.md)，再按口语/书面和任务需要展开；纯事实查询或代码执行不默认加载。
- 培训先读[培训入口](./work/ai/training/README.md)区分会员社群、企业、图书馆、夜校和其他外部活动。没有明确归属证据的资料不得默认放入会员社群。课号只在所属课程系列内有意义；资料发布不等于已经授课。
- 创作/复盘培训资料时读培训经验与风格；查询状态直接读项目状态。复盘同时处理案例证据和可复用方法，重复失误应修复调用或验收，不重复新建同义规则。
- AE设计、MG微课与AI视频按[制作协作流程](./work/design/production-workflow.md)互相引用。脚本、分镜、AI生成、合成和交付按任务需要组合，项目事实仍只放一个主归属。
- 纯教学演示不因“案例/结果展示”触发销售框架。用于招生、销售、提案或产品价值证明时才叠加[商业案例方法](./work/other/commercial/experience/case-result-narrative.md)；正式对外交付再读[交付语言](./work/other/commercial/experience/external-deliverable-language.md)，融资/比赛再读[赛事与投资材料](./work/other/commercial/experience/competition-and-investor-materials.md)。
- 《飞书高效办公》唯一位置是[出版项目](./work/ai/publishing/projects/feishu-efficient-office/README.md)。书稿任务先读项目和[当前出版规则](./work/ai/publishing/projects/feishu-efficient-office/writing-style-analysis.md)，确认新旧章身份；飞书功能与图片须实际核验，面向小白写可执行细步骤。
- 六十甲子项目唯一上下文为[项目入口](./work/other/ai-sixty-jiazi-music-ip/README.md)，网站与独立IP工作线分开，不因开发任务复制到编程项目。
- Skill从[能力索引](./work/ai/programming/experience/skill-repository/README.md)查能力、来源、自研/第三方与固定版本；先条目README与upstream.json，真正执行才读SKILL.md及必要引用，不把案例人物、奖项、数据当事实。
- 电脑环境任务先读[设备索引](./repository/environment/computers/README.md)并核对设备；先诊断，不擅自重启工作中的Codex、CC Switch、Clash或切代理。
- 在建委本机生图先读[生图通道](./repository/environment/image-generation.md)，按已确认启动器调用；换设备重新核对依赖，凭据不入库。

## 写入责任

新增、修改、移动、删除、纠错、复盘、收录Skill和“沉淀到某板块”，都必须先读[写入与更新流程](./repository/ingestion-workflow.md)和[结构说明](./STRUCTURE.md)。AI负责判断全部受影响入口，不要求建委提醒更新README。

一次写入完成必须包含：唯一主归属、来源与范围、去重/替代判断、最近README索引、必要跨领域引用、当前状态同步、结构与派生入口同步、校验。商单按[案例/方法模板](./repository/templates/README.md)保留实际过程和验收，缺证据标缺失，不写成已验证。

重大变化写 revisions/YYYY-MM-DD-slug.md；已有history.md仅保留摘要和修订链接，不能同时维护另一套当前事实。普通小修改交给Git历史。用户明确彻底清除资料时，同时移除当前树及history目录引用，不另建归档或墓碑记录。

## 提交标准

<!-- publish-policy: direct-main-no-pr -->

- UTF-8、LF、相对链接、英文kebab-case；不提交密码、Token、Cookie、API密钥或可利用认证信息。
- 提交前检查工作区，只暂存本次范围；运行维护README中的同步、生成和校验。任何目录/文件变化同步STRUCTURE.md；每次提交从同一版本的Markdown和模板重建STRUCTURE.html。
- 建委要求写入GitHub时，校验后直接提交推送main，不创建PR，不等待第二次“提交”。远端有新改动先核对合并，不覆盖他人内容。
- 推送后核对远端commit与新增/移除路径。完成必须是远端可读取，不是只有本地提交。
- 桌面HTML是仓库结构的派生镜像，Git操作后自动同步并比对SHA-256。桌面暂不可用只延后，不影响仓库内容校验；后续自动重试。
