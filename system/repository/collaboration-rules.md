# 协作规则与职责边界

状态：当前有效；来源：建委2026-09-12确认的结构规划与既有业务规则。根[AGENTS](../../AGENTS.md)保留启动摘要，本文件负责完整协作边界。

## 渐进读取

先确认任务目标、对象、交付物和项目身份，再选一个主入口，自动补完成任务所需的方法、工具和事实。没有固定的文件数量上限，不要求建委另说“结合”；也不因为业务多就加载所有领域。

任务导航提供候选，不代替身份判断。只查位置或状态直接读权威记录；生成、改写或审核中文成品读[表达短卡](../expression/README.md)及适用体裁。产生中文与写入仓库可以同时成立，两项责任都要完成。原始材料、长书稿、历史、Skill源码仅在核验或执行需要时展开。

## 事实、方法、表达与执行能力

- 建委当前明确确认决定个人目标、偏好、业务约定及项目归属；不等于外部产品能力已核验。
- 项目README指出价格、权益、章节、课程、状态等唯一事实来源。较新适用证据与摘要冲突时，说明差异并更新入口，不认定README永远正确。
- 外部功能、菜单、接口、版本、价格按账号/环境、来源和日期核验，执行[动态知识政策](./versioned-knowledge-policy.md)。无法消解时分清已确认、待确认和已替代，继续独立可做部分。
- 方法写适用条件、排除条件、步骤、验收和验证程度；示例、模板、拟定方案不能推成项目事实。单次失败或成功都可记录，未经复用验证不能夸大普适性。
- 表达底线与体裁标准共同决定成品；个人口吻只来自认可样稿或明确偏好，合同等正式文书不强套个人IP腔。
- Skill先看能力、origin、维护者、上游URL和固定版本，再看执行入口与当前环境。收录、安装、执行分别记录；不能将快照中的人物、客户、奖项或示例数字当成建委事实。

## 不得混用的业务边界

| 任务 | 必须区分 |
|---|---|
| 培训 | [培训入口](../../work/domains/training/README.md)区分会员社群、企业、图书馆、夜校及其他活动；课号只在所属系列内有效。资料发布不等于实际授课，未知归属不默认社群 |
| 设计与视频 | [制作流程](../../work/domains/design/common/production-workflow.md)按交付物组合手工制作、AI分镜/生成、AE/MG与后期。MG不限教师业务，项目只存一份 |
| 教学与商业 | 纯教学不因“案例/结果展示”加载销售框架；招生、销售、提案或产品价值证明才读[商业案例方法](../../work/domains/other/commercial/experience/case-result-narrative.md) |
| 正式交付 | 对客户或机构交付读[交付语言](../../work/domains/other/commercial/experience/external-deliverable-language.md)；比赛、融资再读[赛事与投资材料](../../work/domains/other/commercial/experience/competition-and-investor-materials.md) |
| 飞书书籍 | [出版项目](../../work/projects/feishu-efficient-office/README.md)与[当前规则](../../work/projects/feishu-efficient-office/writing-style-analysis.md)是入口；先确认新旧章身份，界面事实与图片实际核验，面向小白写可执行步骤 |
| 平台 | 飞书文档链接不证明是出版项目。百度秒嗒/秒哒、miaoda.cn、appmiaoda.com不属于飞书妙搭；百度任务先读[辨析](../../work/domains/development/tools/miaoda/disambiguation.md)，不能调用lark-apps/Spark接口 |
| 六十甲子 | [项目入口](../../work/projects/ai-sixty-jiazi-music-ip/README.md)是唯一上下文，网站与独立IP工作线继续分开；开发、音乐、海报不各建一份项目 |
| 设备与生图 | 先读[设备索引](../environment/computers/README.md)核对本机；先诊断，不擅自重启工作的Codex、CC Switch、Clash或切代理。生图按[通道](../environment/image-generation.md)，换设备重新核验 |

## 写入与发布

所有资料变动执行[更新流程](./ingestion-workflow.md)。唯一主归属、来源与范围、去重和替代判断、最近README、相关资产登记、必要依赖、当前状态、结构与校验由AI负责。

重大变化写就近`revisions/YYYY-MM-DD-slug.md`，既有history只保留摘要和链接；普通编辑交给Git历史。用户明确彻底清除时同步移除当前树及历史引用，不建立归档或墓碑。保留价值明确的退出项目进入[归档](../../work/projects/archive/README.md)。

使用UTF-8、LF、相对链接和英文kebab-case；工具固定文件名遵守其约定。凭据、Token、Cookie、可利用认证信息不入库。提交前按[维护步骤](./maintenance/README.md)检查范围、派生文件和暂存快照，不夹带无关文件。按根AGENTS的直接main政策发布，回读远端commit与路径；桌面镜像单独报告并在后续Git操作时重试。
