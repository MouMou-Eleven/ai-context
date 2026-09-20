# 仓库运行与维护

GitHub工作流见[自动校验配置](../../.github/workflows/context-validation.yml)，说明归入[维护入口](./maintenance/README.md)；仓库日常首页使用[根目录README](../../README.md)。不在.github另放README，以免GitHub优先展示技术说明而遮住知识库入口。

建委描述目标和要沉淀的领域，AI负责完成检索、归属、依赖选择、更新及发布。

| 文件 | 职责 |
|---|---|
| [AGENTS](../../AGENTS.md) | 协作边界、事实判断、写入责任与发布政策 |
| [collaboration-rules.md](./collaboration-rules.md) | 完整协作规则、事实与业务边界；根AGENTS为启动摘要 |
| [information-architecture.md](./information-architecture.md) | 四个主入口、领域与项目分工、长期扩展和验收原则 |
| [llms](../../llms.txt) | 由任务路由登记生成的短入口 |
| [STRUCTURE](./navigation/STRUCTURE.md) / [交互结构](./navigation/STRUCTURE.html) | 完整文件职责与可展开结构 |
| [navigation/README.md](./navigation/README.md) | 任务路由、项目登记、能力发现与接入 |
| [ingestion-workflow.md](./ingestion-workflow.md) | 任何新增/改动都要执行的更新流程 |
| [execution-checks.md](./execution-checks.md) | 使用经验制作实际成品的写前约束、版本验收与写后回读 |
| [capability-evidence.md](./capability-evidence.md) | 每次沉淀后由AI依据独立实践更新个人能力摘要，防止收藏即掌握 |
| [templates/README.md](./templates/README.md) | 案例、方法与项目入口的最小记录模板 |
| [roadmap.md](./roadmap.md) | 持续维护顺序、真实任务评估与未来检索升级条件 |
| [versioned-knowledge-policy.md](./versioned-knowledge-policy.md) | 动态事实的来源、版本与取代关系 |
| [maintenance/README.md](./maintenance/README.md) | 本地/远端校验、派生文件、结构及桌面同步 |
| [environment/README.md](../environment/README.md) | 电脑、本地工具与网络环境 |
| [revisions/README.md](./revisions/README.md) | 治理变化与修订来源 |

技术入口：[Git忽略规则](../../.gitignore)、[文本属性](../../.gitattributes)、[GitHub自动校验](../../.github/workflows/context-validation.yml)。它们保留工具要求的位置，由本分支解释，不作为日常业务门类。

根README面向人，AGENTS负责启动，完整任务导航与派生入口由单份登记生成；不能在各入口另写相反的路由。桌面HTML仅是查看镜像，不参与知识正确性的判断。
