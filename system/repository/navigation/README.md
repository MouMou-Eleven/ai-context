# 任务路由与项目登记

| 文件 | 用途 |
|---|---|
| [routes.json](./routes.json) | 任务候选、主入口、体裁与写入条件；任务指南与短llms由此生成 |
| [projects.json](./projects.json) | 项目、案例、归档入口与领域关系；状态仍回正文 |
| [task-guide.md](./task-guide.md) | 自动生成的完整任务指南 |
| [STRUCTURE.md](./STRUCTURE.md) | 完整物理文件树与结构约定 |
| [STRUCTURE.html](./STRUCTURE.html) | 默认日常知识导航；完整文件视图位于“维护查看”内，两者来自同一真实目录 |
| [history.md](./history.md) | 按对象查个人经历、项目历史与仓库修订 |

## 接入

AI访问仓库先核对分支/commit或读取时间，读AGENTS和llms，再进入任务入口。浏览器、连接器和本地clone都遵守同一顺序；仓库文本不保证宿主会自动加载。换机器只安装当前任务所需工具，已收录Skill不等于已安装。

可运行 `python system/repository/maintenance/context-route.py --task "用AI辅助AE视频" --intent create` 查看候选和依赖。它是可解释的词匹配辅助，不是完整语义分类器，不执行工具；AI需按目标、对象与证据核对最终选择。没有命中则回work或相关总入口，不能直接断言没有资料。

一个主任务可读取跨目录的必要依赖；相邻入口补双向链接。多个独立交付分别路由。课程身份不能靠课号、标题或旧路径推定；明确项目与文档归属冲突时先记录冲突。

## 方法条件登记

写作方法使用routes.json中的methodRules；不单独建立作者或风格注册表。path指唯一方法正文；evidence指来源记录；entryPoints列需要自动生成短表的README；selectedAny限定适用任务候选。status为active、candidate或retired，只有active进入日常建议和短表。confirmedAt记录当前采用范围的确认日期。

whenAny表示任一线索命中，whenAll表示各组至少一个线索命中；两者都有时必须同时满足。excludeAny优先排除，intents限定create／write。useWhen、notFor和acceptance为人和AI可读的用途、边界与成品验收。字段由执行AI维护，用户不需要写配置或记术语。

方法需要实际Skill实体或配套参考时，用可选readWith列出仅在该方法采用后需要继续读的路径；校验器检查每条路径，路由把它们加入正文计划。能力卡的适配边界优先于上游示例，不因已经读到Skill就另起安装或发布流程。

脚本输出methods和read是读取建议；`discovery`补充当前范围内按正文、标题排序的候选与原文行号，候选不自动成为必读或采用规则。`--pack`实际载入计划内本地正文并提供hash，预算不足及缺失明确列出；它不训练模型或自动判定语义。仅指定板块或换一种说法没命中时，AI继续按该README短表与任务材料判断；不得把关键词规则当成唯一调用方式。候选方法留在原来源记录中，不要求为每个未成熟想法建路由。

相同方法跨领域只增加entryPoints与适用范围，正文一份。范围变更或停用时，同步生成器清理旧短表，并运行匹配、误触发、状态与生成漂移回归。AI还须同步方法正文的当前状态与人工维护的引用，标清替代项；生成器只维护标记区块，不会替正文判断方法失效。

## 更新

新项目登记projects；新能力或任务入口登记routes，并更新对应领域README及路由用例。方法细节放唯一来源，不塞到根路由。运行维护命令重建llms、项目表和结构；派生结果不可手工另写一套。

`projects`登记长期项目与活动容器，`cases`登记独立实践记录，`archivedProjects`登记已退出主线的项目。每项只维护ID、名称、类型、路径和领域关系，不重复进度、价格与验收结果。`domainEntries`列出应发现该资产的领域README；生成器更新其中的`generated-related-assets`区块，同时刷新项目、案例与归档总表。个人概要不生成完整项目表，只在个人方向或能力证据变化时由AI更新。撤销关联时移除旧行，手写用途与方法放生成标记之外。

中文输出与写库独立判断。例：`python system/repository/maintenance/context-route.py --task "修改并沉淀企业培训课件" --intent create --write-repository`。中文回复默认使用表达短卡，纯工具执行可加`--no-chinese-output`；简单查询不读取所有体裁。`--intent write`兼容旧调用并默认开启写库，不关闭中文规则。

日常树和完整树来自同一真实文件清单与说明登记。README作为目录入口，配置脚本、原始语料和Skill快照内部不作为日常业务节点；完整文件视图可核查实际位置。一个长期项目中的案例仍留在项目，不能为总案例表复制正文。
