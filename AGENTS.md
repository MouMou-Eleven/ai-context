# AI启动规则

本仓库是杨建委的长期AI协作事实中枢。建委只需描述目标或要沉淀的领域，AI承担检索、归属、必要依赖、更新、验收与发布责任。

**调用时不用建委报路径。** 从当前对话提取正在做的交付物、读者、问题和明确项目，再按[任务指南](./system/repository/navigation/task-guide.md)定位；“参考仓库”只是取用上下文，不是仓库维护任务。只指定板块时继续查它的子目录与方法正文。能运行Python就用[检索工具](./system/repository/maintenance/context-route.py)的自然任务计划与正文包；不能运行时按同一指南沿README和站内文件搜索。未命中先改用材料中的问题词检索，不能要求建委替AI找文件。只有对话本身没有任务目标，才问要完成什么。

1. 开始先实际核对仓库版本、[目录](./system/repository/navigation/STRUCTURE.md)和[任务入口](./system/repository/navigation/task-guide.md)，进入最近README；按需读证据，不默认加载全部原文、源码或历史。用户指定文件夹时，读最近README并沿本次触发继续读规则正文；索引与链接本身不是已读经验，必要的通用规则与项目事实仍须组合。
2. 当前执行[协作规则](./system/repository/collaboration-rules.md)。一个主任务可自动组合必要领域；读取领域方法短表后，按读者困难和实际材料选择已采用方法，不要求用户点名作者，也不把短表内方法全部载入；个人事实在personal，个人认知在brain，方法和Skill在work/domains，项目与案例在work/projects，共享表达与运行规则在system。
3. 所有中文输出遵守清楚、准确、连贯、不编造的底线。生成、修改或审核中文成品时读[表达短卡](./system/expression/README.md)和适用体裁；同时写入仓库时两套责任都成立。简单回答无需重复加载长规则。
   制作实际成品按[执行与验收](./system/repository/execution-checks.md)把适用规则落实为本次约束与检查证据。读到规则不算已遵循，格式解析不算内容验收；长任务恢复后回读执行卡，写外部文档前验草稿，写后回读实际成品。
4. 用户最近明确确认决定个人偏好、业务约定和项目归属；外部产品能力另按来源、版本和环境核验。README指向权威事实，不因它是入口就压过更新的适用证据。
5. 培训先核对系列与场次；会员社群不代表全部培训。《别让 Bug 打败你》属于外部培训，同号课程与待归属资料不能推入社群。教师委托教育作品与建委授课分别处理。
6. 项目身份不能由平台名或工具名推断。百度秒哒与飞书妙搭先读[辨析](./work/domains/development/tools/miaoda/disambiguation.md)；飞书文档链接不等于出版项目。飞书书稿先读[项目](./work/projects/feishu-efficient-office/README.md)与[当前出版规则](./work/projects/feishu-efficient-office/writing-style-analysis.md)。
7. 写入、纠错、迁移、删除、收录Skill和复盘先读[更新流程](./system/repository/ingestion-workflow.md)。AI同步最近索引、相关资产登记、当前事实、引用和派生结构；重大变化写就近revisions，普通变动由Git追溯。
8. Skill先查[能力与来源](work/domains/other/skills/README.md)，选定后才读执行实体。收录不等于安装，安装不等于执行。本机环境按[设备入口](./system/environment/README.md)核对；生图按[本机通道](./system/environment/image-generation.md)执行，凭据不入库。

<!-- publish-policy: direct-main-no-pr -->

建委要求写入GitHub时，按[维护步骤](./system/repository/maintenance/README.md)同步、校验并检查暂存范围，然后直接提交推送main，不创建PR或等待第二次提交指令。远端有新变化先核对合并；推送后回读commit与关键路径，并在回复中提供本次实际推送位置的GitHub链接（必要时附具体文件或commit链接）。桌面HTML是派生镜像，其暂不可用不阻断仓库内容校验。
