# 仓库完整结构与写入规范

> 本文件展示实际文件结构与职责，目录树由维护工具生成，不能替代业务事实来源。下方按连续层级展开，完整第三方源码折叠到快照入口；读取与写入执行[AGENTS](./AGENTS.md)及[更新流程](./repository/ingestion-workflow.md)。

## 一、完整目录树

```text
ai-context/
├── README.md  仓库总入口与五个一级目录说明
├── AGENTS.md  AI 协作、读取、写入和提交规则
├── llms.txt  任务路由与必要依赖的最小读取入口
├── STRUCTURE.md  完整目录树与结构规范（本文件）
├── STRUCTURE.html  可展开、折叠和搜索的结构思维导图（自动生成）
├── personal/  一级目录：个人信息概要
│   ├── business-overview.md  业务与项目概要，只做导航不写细节
│   ├── capabilities.md  能力结构与擅长方向
│   ├── credentials.md  个人背书：荣誉、成果、聘书和代表经历
│   ├── growth-path.md  成长路径与阶段变化
│   ├── profile.md  我是谁：身份、教育和职业基本信息
│   └── README.md  个人信息总窗口、索引、写入准则
├── brain/  一级目录：建委大脑
│   ├── ai-expression/  二级目录：AI 中文表达基础层
│   │   ├── chinese-datasets/  三级目录：中文数据、规则来源与质量检查
│   │   │   ├── feitian-shanke/  四级目录：中文技术科普参考材料
│   │   │   │   ├── raw/  五级目录：未经改写的原始逐字稿
│   │   │   │   │   └── feitian-shanke-transcript.txt  文本资料
│   │   │   │   └── README.md  材料用途、来源状态和授权边界
│   │   │   ├── grammar-and-error-checklist.md  按需读取的中文语法与病句详查
│   │   │   ├── README.md  数据来源、授权、提炼、冲突治理和使用规则
│   │   │   └── short-video-outcome-and-motivation/  短视频“成果展示与用户动机”逐字稿参考包
│   │   │       ├── raw/  目录入口
│   │   │       │   └── two-video-transcripts.md  两段原始短视频逐字稿 两套材料均仅供内部分析，不声明可训练
│   │   │       └── README.md  短视频口语材料来源、核验和使用边界
│   │   ├── cross-domain-rules.md  跨领域中文质量、逻辑与搭配规则
│   │   ├── experience/  三级目录：AI 表达经验
│   │   │   └── README.md  跨领域表达经验索引与提炼规则
│   │   ├── oral-expression/  三级目录：口语化表达（唯一通用来源）
│   │   │   ├── README.md  口语化表达总入口与检查清单
│   │   │   └── spoken-argument-and-transition.md  口语化论证与前后承接方法
│   │   ├── README.md  AI 表达总入口、默认激活与组合规则
│   │   └── written-expression/  三级目录：书面化表达
│   │       └── README.md  书稿、教程、方案和文档表达规则
│   ├── cognition/  二级目录：建委认知
│   │   ├── business-cognition.md  商业、增长、内容经营与经营判断
│   │   ├── README.md  认知入口、读取路由与写入边界
│   │   └── thinking-and-decisions.md  思维、判断、框架拆解、学习与决策方式
│   └── README.md  建委大脑入口、边界与激活条件
├── work/  一级目录：工作领域与项目
│   ├── ai/  二级目录：AI 领域
│   │   ├── programming/  三级目录：AI 编程
│   │   │   ├── experience/  四级目录：通用编程经验
│   │   │   │   ├── creative-frontend-prompt-patterns.md  创意前端提示词方法
│   │   │   │   ├── README.md  经验索引
│   │   │   │   ├── reference-materials/  五级目录：编程参考资料
│   │   │   │   │   ├── creative-frontend-prompts/  创意前端提示词原始样例
│   │   │   │   │   │   ├── raw/  六级目录：未经提炼的原文
│   │   │   │   │   │   │   ├── dark-editorial-portfolio.txt  文本资料
│   │   │   │   │   │   │   ├── jack-3d-creator-portfolio.txt  文本资料
│   │   │   │   │   │   │   ├── prmpt-fashion-archive.txt  文本资料
│   │   │   │   │   │   │   ├── sentinel-spline-3d-hero.txt  文本资料
│   │   │   │   │   │   │   └── synapsex-video-scrub.txt  文本资料
│   │   │   │   │   │   └── README.md  创意前端原始提示词索引
│   │   │   │   │   └── README.md  参考资料索引
│   │   │   │   └── skill-repository/  五级目录：Skill 仓库
│   │   │   │       ├── editaplot/  EditaPlot
│   │   │   │       │   ├── README.md  科研绘图 Skill 的调用、前提与更新方法
│   │   │   │       │   ├── source/  完整上游快照，内部供应商文件不逐项展开；上游完整快照，共 662 个文件，内部层级按需查看
│   │   │   │       │   └── upstream.json  上游仓库、分支、commit 与许可
│   │   │   │       ├── jianwei-ai-community-remotion-video/  jianwei-ai-community-remotion-video
│   │   │   │       │   ├── README.md  建委 AI 社群 Remotion 视频 Skill 说明
│   │   │   │       │   ├── skill/  可直接安装的完整 Skill
│   │   │   │       │   │   ├── agents/  目录入口
│   │   │   │       │   │   │   └── openai.yaml  自动化配置
│   │   │   │       │   │   ├── references/  目录入口
│   │   │   │       │   │   │   ├── background-fidelity-contract.md  参考图背景保真契约
│   │   │   │       │   │   │   ├── deterministic-layout-contract.md  Deterministic layout contract
│   │   │   │       │   │   │   ├── director-console-contract.md  导演台稳定输出契约
│   │   │   │       │   │   │   ├── director-strategy.md  动效导演策略
│   │   │   │       │   │   │   ├── input-and-image-analysis.md  输入与图片分析
│   │   │   │       │   │   │   ├── internal-production-brief.schema.json  结构化配置与索引
│   │   │   │       │   │   │   ├── motion-blueprint.schema.json  结构化配置与索引
│   │   │   │       │   │   │   ├── motion-direction.md  动效导演规则
│   │   │   │       │   │   │   ├── output-contract.md  Motion Blueprint 输出契约
│   │   │   │       │   │   │   ├── parameterization-contract.md  参数化与 Studio 编辑契约
│   │   │   │       │   │   │   ├── prompt-expansion-contract.md  内部导演执行稿与二次加工契约
│   │   │   │       │   │   │   ├── quality-gates.md  质量门槛
│   │   │   │       │   │   │   ├── reference-fidelity-contract.md  参考图保真契约
│   │   │   │       │   │   │   ├── remotion-contract.md  Remotion 实施契约
│   │   │   │       │   │   │   ├── remotion-only-director-contract.md  Remotion-only director contract
│   │   │   │       │   │   │   ├── render-performance-contract.md  渲染性能与交付流程契约
│   │   │   │       │   │   │   └── visibility-and-clipping-contract.md  文字与关键元素完整可见契约
│   │   │   │       │   │   ├── scripts/  目录入口
│   │   │   │       │   │   │   ├── audit_reference_render_path.py  跨平台维护或执行脚本
│   │   │   │       │   │   │   ├── check_layout_stability.py  跨平台维护或执行脚本
│   │   │   │       │   │   │   ├── check_settle_continuity.py  跨平台维护或执行脚本
│   │   │   │       │   │   │   ├── check_visibility_report.py  跨平台维护或执行脚本
│   │   │   │       │   │   │   ├── compare_background_regions.py  跨平台维护或执行脚本
│   │   │   │       │   │   │   ├── compare_reference_frame.py  跨平台维护或执行脚本
│   │   │   │       │   │   │   ├── validate_blueprint.py  跨平台维护或执行脚本
│   │   │   │       │   │   │   └── validate_production_brief.py  跨平台维护或执行脚本
│   │   │   │       │   │   └── SKILL.md  建委 AI 社群视频制作 Skill
│   │   │   │       │   └── upstream.json  规范参考与维护策略
│   │   │   │       ├── jianwei-ai-learning-community-workbench/  jianwei-ai-learning-community-workbench
│   │   │   │       │   ├── README.md  通用身份适配型工作台设计 Skill 说明
│   │   │   │       │   ├── skill/  可直接安装的完整 Skill
│   │   │   │       │   │   ├── agents/  目录入口
│   │   │   │       │   │   │   └── openai.yaml  自动化配置
│   │   │   │       │   │   ├── references/  目录入口
│   │   │   │       │   │   │   ├── conversation-protocol.md  首轮提问协议
│   │   │   │       │   │   │   ├── design-system.md  视觉、交互与跨端系统
│   │   │   │       │   │   │   ├── quality-gate.md  交付前品控门
│   │   │   │       │   │   │   └── role-adaptation.md  身份适配与工作台骨架
│   │   │   │       │   │   └── SKILL.md  身份适配工作台设计 Skill
│   │   │   │       │   └── upstream.json  来源、版本与维护策略
│   │   │   │       ├── qingyun-ip-poster/  五级目录：青云 IP Poster 海报视觉 Skill
│   │   │   │       │   ├── README.md  调用方式、适用范围、事实与许可边界
│   │   │   │       │   ├── skill/  完整上游 Skill 快照，内部文件不逐项展开；上游完整快照，共 26 个文件，内部层级按需查看
│   │   │   │       │   └── upstream.json  上游仓库、固定 commit、版本与更新规则
│   │   │   │       └── README.md  Skill 实体索引、来源与更新规则
│   │   │   ├── projects/  四级目录：AI 编程项目
│   │   │   │   ├── README.md  项目索引与源码仓库入口
│   │   │   │   └── yancut-ai/  五级目录：言剪 AI
│   │   │   │       ├── architecture-and-upstream.md  架构、上游与能力边界
│   │   │   │       ├── history.md  已清洗的关键演进摘要
│   │   │   │       ├── README.md  当前项目事实与调用规则
│   │   │   │       ├── revisions/  项目关键修订记录
│   │   │   │       │   ├── 2026-08-22-auto-video-editable-project-loop.md  自动剪辑可编辑工程闭环修订
│   │   │   │       │   ├── 2026-08-22-wasm-scene-effect-and-editor-localization.md  WASM 场景效果与编辑器本地化修订
│   │   │   │       │   ├── 2026-08-31-effects-remotion-commercial-loop.md  Remotion 特效商业化闭环修订
│   │   │   │       │   ├── 2026-08-31-recut-remotion-production-loop.md  Remotion 重剪生产闭环修订
│   │   │   │       │   ├── 2026-08-31-shotcut-professional-ai-workflow.md  Shotcut 专业 AI 剪辑工作流
│   │   │   │       │   ├── 2026-08-31-source-repo-professional-editing-queue.md  源码仓专业剪辑排期修订
│   │   │   │       │   ├── 2026-09-01-concat-template-slots-command-queue.md  Concat 模板槽位与命令队列修订
│   │   │   │       │   ├── 2026-09-02-admin-shared-backend.md  管理后台与共享后端闭环修订
│   │   │   │       │   ├── 2026-09-02-commercialization-closure.md  商业化闭环与上线边界修订
│   │   │   │       │   ├── 2026-09-03-glm53-manual-purchase.md  GLM 模型与手动购买流程修订
│   │   │   │       │   ├── 2026-09-03-local-demo-effects-stickers.md  本地演示特效与贴纸效果修订
│   │   │   │       │   └── 2026-09-04-ai-progress-remotion-hyperframes-keyframes.md  AI 执行进度可视化、Remotion 本地预检与手动关键帧修订
│   │   │   │       └── roadmap.md  开发路线与上线条件
│   │   │   ├── README.md  AI 编程总入口
│   │   │   └── tools/  四级目录：编程工具
│   │   │       ├── miaoda/  五级目录：百度秒哒
│   │   │       │   ├── basics/  六级目录：基础与发布
│   │   │       │   │   ├── current-capabilities.md  当前能力、权益与限制
│   │   │       │   │   ├── platform-basics.md  平台基础能力
│   │   │       │   │   ├── publish-channels.md  发布渠道与限制
│   │   │       │   │   └── README.md  基础资料索引
│   │   │       │   ├── development/  六级目录：开发能力
│   │   │       │   │   ├── README.md  开发资料索引
│   │   │       │   │   ├── skill-as-callable.md  秒哒作为可调用 Skill
│   │   │       │   │   └── skill-development.md  秒哒 Skill 开发
│   │   │       │   ├── disambiguation.md  百度秒哒与飞书妙搭的同名辨析
│   │   │       │   ├── experience/  六级目录：实战经验
│   │   │       │   │   ├── cases/  七级目录：案例
│   │   │       │   │   │   ├── README.md  案例索引
│   │   │       │   │   │   └── yungouos-jsapi.md  云购 OS JSAPI 案例
│   │   │       │   │   ├── patterns/  七级目录：可复用工作模式
│   │   │       │   │   │   ├── codex-assisted-workflow.md  Codex 协助秒哒开发流程
│   │   │       │   │   │   ├── codex-miaoda-iterative-increment-workflow.md  Codex 协助秒哒增量迭代流程
│   │   │       │   │   │   ├── codex-source-package-deployment.md  源码分包与秒哒交付
│   │   │       │   │   │   ├── content-rectification-prompts.md  内容整改提示词
│   │   │       │   │   │   ├── large-video-upload.md  大视频上传方案
│   │   │       │   │   │   ├── README.md  模式索引
│   │   │       │   │   │   ├── seo-optimization.md  SEO 优化经验
│   │   │       │   │   │   └── wechat-urlsec-verification.md  微信 URL 安全验证
│   │   │       │   │   ├── pitfalls.md  常见坑与规避方式
│   │   │       │   │   ├── prompt-patterns.md  提示词模式
│   │   │       │   │   ├── prompts/  秒哒提示词：按任务读取
│   │   │       │   │   │   ├── authentication.md  登录与手机号身份一致性
│   │   │       │   │   │   ├── backend-storage.md  应用形态与后端持久化
│   │   │       │   │   │   ├── execution-and-handoff.md  执行边界、分批协作与源码交接
│   │   │       │   │   │   ├── payment-integration.md  支付集成与既有实现复用
│   │   │       │   │   │   ├── README.md  秒哒提示词：按任务读取
│   │   │       │   │   │   ├── runtime-diagnostics.md  运行诊断与证据回传
│   │   │       │   │   │   ├── seo-and-content.md  SEO与公开内容整改
│   │   │       │   │   │   └── uploads.md  原生大文件与小程序上传
│   │   │       │   │   ├── README.md  经验索引
│   │   │       │   │   └── reference-materials/  七级目录：原始参考资料
│   │   │       │   │       ├── README.md  参考资料索引
│   │   │       │   │       └── video-chunked-upload/  video-chunked-upload — 旧环境兼容源码
│   │   │       │   │           ├── legacy-contract.md  旧环境分片上传合同与专用提示词
│   │   │       │   │           ├── README.md  视频分片上传源码说明
│   │   │       │   │           ├── video-serve.ts  资料与资源
│   │   │       │   │           ├── video-upload-chunk.ts  资料与资源
│   │   │       │   │           └── video-upload-complete.ts  资料与资源
│   │   │       │   ├── llms.txt  秒哒最小读取路由
│   │   │       │   ├── README.md  秒哒总入口与读取边界
│   │   │       │   └── updates/  六级目录：版本与升级
│   │   │       │       ├── 2026-08-02-version-governance.md  版本知识治理记录
│   │   │       │       ├── 2026-08-15-cloud-runtime-diagnostics.md  云端运行诊断记录
│   │   │       │       ├── 2026-08-29-v3.7-and-upload-limit-governance.md  V3.7 与上传限制口径修订
│   │   │       │       ├── 2026-09-07-codex-miaoda-incremental-loop.md  Codex 协助秒哒增量闭环修订
│   │   │       │       ├── README.md  版本资料索引
│   │   │       │       └── version-features.md  历史版本能力时间线
│   │   │       └── README.md  工具索引
│   │   ├── publishing/  三级目录：AI 书籍出版
│   │   │   ├── projects/  AI 书籍出版项目
│   │   │   │   ├── feishu-efficient-office/  五级目录：《飞书高效办公》
│   │   │   │   │   ├── all-docs.md  历史培训素材摘要，默认不读
│   │   │   │   │   ├── ch1-editor-feedback-lessons.md  第1章编辑反馈汇总（引以为鉴）
│   │   │   │   │   ├── ch2-editor-feedback-lessons.md  第2章 0822 细颗粒度编辑反馈与复查规则
│   │   │   │   │   ├── ch4-editor-feedback.md  历史旧第4章 编辑反馈汇总与修改方案
│   │   │   │   │   ├── ch4-v3-editor-feedback.md  历史旧第4章 v3 修订稿编辑反馈汇总
│   │   │   │   │   ├── ch4-v4-revision-log.md  历史旧第4章 v4 修订稿创建与执行记录
│   │   │   │   │   ├── ch5-editor-feedback.md  各章编辑反馈与共性规则
│   │   │   │   │   ├── feishu-base-form-experience.md  多维表格表单经验
│   │   │   │   │   ├── feishu-doc-style.md  飞书文档视觉规范
│   │   │   │   │   ├── history.md  已清洗的章节修订摘要
│   │   │   │   │   ├── interface-screenshot-guidelines.md  软件截图与图文一致规范
│   │   │   │   │   ├── legacy-ch4-map.md  旧第4章素材映射
│   │   │   │   │   ├── publication-acceptance-checklist.md  出版编辑与交稿验收
│   │   │   │   │   ├── README.md  项目当前口径、进度和文件索引
│   │   │   │   │   ├── writing-style-analysis.md  本书专用写作风格
│   │   │   │   │   └── writing-style-history.md  写作风格历史来源（不自动激活）
│   │   │   │   └── README.md  出版项目索引
│   │   │   └── README.md  出版领域总入口
│   │   ├── README.md  AI 领域总索引
│   │   ├── self-media/  三级目录：AI 自媒体
│   │   │   ├── articles/  自媒体文章与图文
│   │   │   │   └── README.md  文章内容方法与素材入口
│   │   │   ├── community-copy/  社群文案与话术
│   │   │   │   └── README.md  社群文案与话术入口
│   │   │   ├── experience/  自媒体运营经验
│   │   │   │   ├── media-growth.md  账号增长与内容规划
│   │   │   │   ├── outcome-and-motivation.md  成果展示、用户动机与知识分层
│   │   │   │   └── README.md  自媒体经验索引
│   │   │   ├── live-sales/  直播销售与内容承接
│   │   │   │   ├── conversion-path.md  内容到评论、资料和社群的承接
│   │   │   │   └── README.md  直播销售与转化入口
│   │   │   ├── marketing-copy/  营销文案与推广文章
│   │   │   │   └── README.md  营销文案与推广文章入口
│   │   │   ├── moments-copy/  朋友圈文案
│   │   │   │   └── README.md  朋友圈文案入口
│   │   │   ├── README.md  自媒体总入口与严格边界
│   │   │   ├── titles/  自媒体标题与选题
│   │   │   │   └── README.md  标题方法与素材入口
│   │   │   └── video-scripts/  自媒体口播与视频脚本
│   │   │       ├── README.md  口播与短视频脚本入口
│   │   │       └── script-patterns.md  脚本结构模式
│   │   ├── training/  三级目录：AI 培训
│   │   │   ├── attribution-and-updates.md  培训资料的归属与更新
│   │   │   ├── experience/  四级目录：培训经验
│   │   │   │   ├── demo-driven-course-design.md  演示驱动课程设计
│   │   │   │   ├── jianwei-training-style.md  建委默认培训风格与课件形态
│   │   │   │   ├── README.md  经验索引
│   │   │   │   ├── sources.md  培训方法来源与课程身份
│   │   │   │   ├── teaching-and-course-design.md  备课、课件与课程设计
│   │   │   │   ├── technical-explanation/  五级目录：技术解释方法
│   │   │   │   │   ├── problem-driven-technical-explanation.md  问题驱动的技术解释方法
│   │   │   │   │   └── README.md  方法索引
│   │   │   │   ├── tutorial-writing.md  学员教程写法
│   │   │   │   └── visual-and-oral-training-docs.md  飞书培训文档的可视化与口语化
│   │   │   ├── materials/  四级目录：培训资料
│   │   │   │   ├── pending-attribution/  待确认归属的培训资料
│   │   │   │   │   ├── README.md  待确认归属的培训资料
│   │   │   │   │   ├── revisions/  待归属培训资料修订
│   │   │   │   │   │   ├── 2026-08-19-lesson-4-student-material-boundary.md  2026-08-19：第 4 课学员正文边界修订
│   │   │   │   │   │   ├── 2026-08-23-lesson-4-visualization-and-case-delivery.md  2026-08-23：第 4 课可视化与案例交付修订
│   │   │   │   │   │   ├── 2026-08-29-student-material-definitive-positioning.md  2026-08-29：学员资料中的确定性学习定位
│   │   │   │   │   │   ├── 2026-09-02-miaoda-advanced-course-scenario-driven-updates.md  秒哒进阶课：把版本更新改造成使用场景链路
│   │   │   │   │   │   ├── 2026-09-07-lesson-6-lecture-review-and-visualization-rules.md  第六课直播复盘：学员稿表达与可视化规则
│   │   │   │   │   │   └── README.md  待归属培训资料修订
│   │   │   │   │   └── technical-dictionary-scope.md  AI 时代技术词典的资料边界
│   │   │   │   └── README.md  资料入口，避免复制项目资料
│   │   │   ├── outlines/  四级目录：培训大纲
│   │   │   │   └── README.md  大纲入口，当前无独立通用大纲
│   │   │   ├── projects/  四级目录：培训项目
│   │   │   │   ├── external-training/  外出培训
│   │   │   │   │   ├── lessons/  外出培训课程资料
│   │   │   │   │   │   ├── bug-repair/  别让 Bug 打败你：秒哒故障定位与修复实战
│   │   │   │   │   │   │   ├── README.md  别让 Bug 打败你：秒哒故障定位与修复实战
│   │   │   │   │   │   │   └── revisions/  Bug 修复课程修订
│   │   │   │   │   │   │       ├── 2026-09-09-lesson-6-bug-repair-evidence-chain.md  第六课优化修订：Bug 修复证据链与一案例多故障演示台
│   │   │   │   │   │   │       └── README.md  Bug 修复课程修订
│   │   │   │   │   │   └── README.md  外出培训课程资料
│   │   │   │   │   └── README.md  外出培训
│   │   │   │   ├── paid-community-course/  五级目录：AI 超级个体陪跑社群
│   │   │   │   │   ├── competitive-references.md  外部会员社群案例与可迁移经验
│   │   │   │   │   ├── course-development.md  课程研发与内容选择
│   │   │   │   │   ├── course-materials-index.md  飞书课程资料索引
│   │   │   │   │   ├── curriculum-design.md  课程结构与直播节奏
│   │   │   │   │   ├── history.md  已清洗的关键演进摘要
│   │   │   │   │   ├── operations-playbook.md  招生、运营与转化执行
│   │   │   │   │   ├── positioning-and-vision.md  社群定位、愿景与表达边界
│   │   │   │   │   ├── README.md  当前产品与课程口径
│   │   │   │   │   └── revisions/  六级目录：课程关键修订
│   │   │   │   │       ├── 2026-08-30-community-positioning-and-super-individual-definition.md  社群总定位与超级个体定义修订
│   │   │   │   │       ├── 2026-08-30-lesson-5-purchase-language-and-decision-boundary.md  第 5 节购买语言与决策边界修订
│   │   │   │   │       ├── 2026-08-31-lesson-5-post-lecture-ai-era-purpose-and-parameter-explanation.md  第 5 节课后 AI 时代目的与参数解释修订
│   │   │   │   │       ├── 2026-09-01-training-rule-scope-and-delivery-boundary.md  AI 培训规则适用场景与课堂交付边界修订
│   │   │   │   │       ├── 2026-09-01-training-rule-single-source-and-technical-selection.md  AI 培训单一来源与技术内容筛选修订
│   │   │   │   │       └── README.md  修订索引与读取边界
│   │   │   │   └── README.md  培训项目索引
│   │   │   └── README.md  AI 培训总入口
│   │   └── video/  三级目录：AI 视频
│   │       ├── common/  AI 视频通用经验
│   │       │   └── README.md  跨片型通用制作经验
│   │       ├── projects/  AI 视频项目与跨领域案例
│   │       │   └── README.md  AI 视频项目索引
│   │       ├── README.md  AI 视频总入口
│   │       ├── tools/  四级目录：AI 视频工具
│   │       │   ├── README.md  工具索引
│   │       │   └── seedance/  Seedance 实战
│   │       │       ├── practical-workflow.md  实战工作流
│   │       │       ├── prompt-cases.md  提示词案例
│   │       │       ├── prompt-templates.md  提示词模板
│   │       │       └── README.md  Seedance 工具入口
│   │       └── types/  四级目录：视频类型
│   │           ├── enterprise-promo/  企业宣传片：入口与适用边界
│   │           │   ├── cases/  目录入口
│   │           │   │   └── 2026-05-enterprise-prompt-record.md  2026 年 5 月企业片提示词实战记录
│   │           │   ├── prompt-iteration.md  企业片提示词节奏与迭代经验
│   │           │   ├── README.md  企业宣传片制作经验
│   │           │   ├── visual-recipes.md  科技企业片可选视觉配方
│   │           │   └── workflow.md  企业宣传片通用制作与验收流程
│   │           ├── live-action-story/  真人实拍故事与电影叙事
│   │           │   └── README.md  真人实拍故事与电影叙事
│   │           ├── motion-comic/  AI 漫剧
│   │           │   └── README.md  漫剧制作入口
│   │           └── README.md  类型索引
│   ├── design/  二级目录：设计领域
│   │   ├── ae-promo-video/  AE 宣传视频设计
│   │   │   └── README.md  AE 宣传视频设计入口
│   │   ├── ai-design/  AI 设计
│   │   │   └── README.md  AI 辅助视觉设计，归属仍是设计
│   │   ├── book-design/  书籍设计
│   │   │   └── README.md  书籍装帧与版式设计入口
│   │   ├── cases/  设计商单与跨领域案例索引
│   │   │   ├── case-template.md  案例模板：用真实结果支持下一次复用
│   │   │   └── README.md  设计商单与跨领域案例索引
│   │   ├── microcourse-mg-animation/  微课与 MG 动画设计
│   │   │   ├── cases/  微课与教育交互案例
│   │   │   │   ├── happy-shopping.md  快乐购物小超市
│   │   │   │   ├── minchao-football.md  大班健康活动：闽超小将
│   │   │   │   ├── README.md  微课与教育交互案例
│   │   │   │   └── vr-ai-interactive.md  VR + AI + 交互教育案例
│   │   │   ├── README.md  微课、精品课、MG 动画与教育课件
│   │   │   └── showcase-guidelines.md  哞哞微课案例展示写作规范
│   │   ├── poster-fold-design/  海报与折页设计
│   │   │   └── README.md  海报、折页及平面物料设计入口
│   │   ├── ppt-design/  PPT 设计
│   │   │   └── README.md  PPT 设计经验与项目入口
│   │   ├── production-workflow.md  设计与 AI 视频联合制作、经验沉淀流程
│   │   └── README.md  设计领域总索引与归类边界
│   ├── other/  二级目录：其他领域与项目
│   │   ├── ai-sixty-jiazi-music-ip/  三级目录：AI 六十甲子古音律与 IP 孵化
│   │   │   ├── current-operations.md  当前Web Demo操作入口
│   │   │   ├── data-audit.md  本地资料、工具与数据审计
│   │   │   ├── demo-implementation.md  四模块 Demo、测试与本地交付记录
│   │   │   ├── ip-character-prompts-v2-mature.md  已否决的成熟神将视觉方向
│   │   │   ├── ip-character-prompts-v3-toy.md  当前潮玩卡通视觉口径与提示词摘要
│   │   │   ├── ip-character-prompts.md  初版潮玩角色构想，保留作历史参考
│   │   │   ├── product-demo-plan.md  Web Demo 产品与技术规划
│   │   │   ├── README.md  当前项目事实、边界、唯一位置与文件索引
│   │   │   └── revisions/  项目关键方向和实现修订
│   │   │       ├── 2026-08-24-context-relocation-to-other.md  项目迁入 other 与唯一写入位置修订
│   │   │       ├── 2026-08-24-initial-project-and-web-demo-direction.md  首次入库与 Web Demo 方向
│   │   │       ├── 2026-08-24-overseas-sound-oracle-and-stem-artifact-system.md  海外声音产品与天干法器视觉系统
│   │   │       ├── 2026-08-24-separate-web-and-toy-ip-direction.md  网站与潮玩 IP 分线及启动修复
│   │   │       ├── 2026-08-24-web-demo-implementation-complete.md  初版 Web Demo 实现与测试记录
│   │   │       ├── 2026-08-24-wide-workbench-music-prompt-v4.md  宽屏工作台、素材与音乐提示词改造
│   │   │       ├── 2026-09-02-five-tone-product-flow-and-private-audio-demo.md  五音产品流程与私有音频演示修订
│   │   │       ├── 2026-09-02-harmony-v6-ui-audit-and-interaction-fix.md  V6 界面审计与交互修复
│   │   │       └── 2026-09-02-product-v7-ui-and-profile-center.md  V7 产品界面与个人中心修订
│   │   ├── commercial/  三级目录：商业化与对外交付
│   │   │   ├── experience/  四级目录：商业经验与交付方法
│   │   │   │   ├── business-analysis-cards.md  产品信息、渠道与对标执行卡
│   │   │   │   ├── case-result-narrative.md  案例选择、结果证明、观点叙事与产品承接
│   │   │   │   ├── competition-and-investor-materials.md  赛事、路演与融资材料的对外边界
│   │   │   │   ├── content-demand-and-conversion.md  内容驱动的需求识别与商业承接
│   │   │   │   ├── external-deliverable-language.md  对外成品与内部工作稿的语言边界
│   │   │   │   └── README.md  内容经营与商业交付经验索引
│   │   │   └── README.md  跨行业商业方法、触发规则与交付边界
│   │   └── README.md  其他领域与项目索引及准入条件
│   └── README.md  工作总入口：设计、AI、其他
├── repository/  一级目录：仓库治理
│   ├── environment/  二级目录：电脑与运行环境
│   │   ├── computers/  三级目录：按设备管理
│   │   │   ├── desktop-1/  四级目录：台式电脑 1
│   │   │   │   ├── disk-cleanup-and-codex-storage.md  磁盘清理与 Codex 存储基线
│   │   │   │   ├── history.md  已清洗的关键修复摘要
│   │   │   │   ├── network-and-codex.md  网络、Clash 与 Codex 排障
│   │   │   │   └── README.md  当前设备事实与操作禁区
│   │   │   ├── README.md  设备索引
│   │   │   └── windows-junction-migration.md  Windows Junction 迁移经验
│   │   ├── image-generation.md  本机生图调用规则
│   │   └── README.md  环境入口与安全规则
│   ├── ingestion-workflow.md  新内容写入与更新流程
│   ├── maintenance/  二级目录：维护工具
│   │   ├── .gitignore  资料与资源
│   │   ├── context-route.py  跨平台维护或执行脚本
│   │   ├── context_common.py  跨平台维护或执行脚本
│   │   ├── desktop-sync.py  跨平台维护或执行脚本
│   │   ├── generate-structure-html.ps1  从 Markdown 生成交互式 HTML
│   │   ├── git-hooks/  本机自动同步触发器
│   │   │   ├── post-checkout  检出或切换后自愈桌面结构
│   │   │   ├── post-commit  提交后同步桌面结构
│   │   │   ├── post-merge  拉取或合并后同步桌面结构
│   │   │   ├── post-rewrite  amend 或 rebase 后同步桌面结构
│   │   │   ├── pre-commit  提交前重建并暂存 STRUCTURE.html
│   │   │   └── run-python  资料与资源
│   │   ├── invoke-python.ps1  Windows 兼容入口
│   │   ├── pre-commit.py  跨平台维护或执行脚本
│   │   ├── README.md  校验与桌面同步说明
│   │   ├── structure-descriptions.json  结构化配置与索引
│   │   ├── structure-viewer.template.html  HTML 思维导图界面与交互模板
│   │   ├── sync-desktop-structure.ps1  生成并同步 HTML 到 F 盘桌面
│   │   ├── sync-navigation.py  跨平台维护或执行脚本
│   │   ├── sync-structure.py  跨平台维护或执行脚本
│   │   ├── tests/  维护回归测试
│   │   │   ├── README.md  维护回归测试
│   │   │   └── test_context.py  跨平台维护或执行脚本
│   │   ├── validate-context.ps1  结构、索引与链接校验脚本
│   │   ├── validate-context.py  跨平台维护或执行脚本
│   │   └── validation-policy.json  结构化配置与索引
│   ├── navigation/  任务路由与项目登记
│   │   ├── projects.json  结构化配置与索引
│   │   ├── README.md  任务路由与项目登记
│   │   └── routes.json  结构化配置与索引
│   ├── README.md  治理总入口
│   ├── revisions/  二级目录：仓库级重大修订
│   │   ├── 2026-08-18-information-architecture-rebuild.md  五个一级入口的信息架构重构记录
│   │   ├── 2026-08-20-ai-expression-default-layer.md  AI 表达默认层和语言规则修订
│   │   ├── 2026-08-21-chinese-quality-and-source-governance.md  中文质量基础层与多来源冲突治理修订
│   │   ├── 2026-08-21-commercial-delivery-domain.md  商业化与对外交付边界层首次建立记录
│   │   ├── 2026-08-21-commercial-delivery-relocation.md  商业化迁移到其他领域的修订
│   │   ├── 2026-08-21-desktop-sync-resilience.md  桌面 HTML 同步稳定性加固
│   │   ├── 2026-08-21-direct-main-and-desktop-sync.md  直推 main、旧分支清理与桌面同步修订
│   │   ├── 2026-08-21-interactive-html-structure-viewer.md  交互式 HTML 结构查看与自动同步修订
│   │   ├── 2026-08-22-cognition-and-content-commercialization.md  建委认知归组与跨行业内容经营修订
│   │   ├── 2026-08-23-feishu-document-routing-boundary.md  飞书文档承载平台与飞书书籍项目的路由边界
│   │   ├── 2026-08-24-sixty-jiazi-project-relocation.md  六十甲子项目迁入 other 与唯一路由规则
│   │   ├── 2026-08-27-commercial-external-material-boundary.md  赛事、路演与融资材料的对外边界修订
│   │   ├── 2026-09-01-ai-programming-skill-repository.md  AI 编程 Skill 仓库与上游快照治理
│   │   ├── 2026-09-01-case-result-narrative.md  案例结果叙事方法入库修订
│   │   ├── 2026-09-01-remotion-skill-confirmation-and-action-contract.md  Remotion Skill 确认门与逐元素动作契约修订
│   │   ├── 2026-09-01-remotion-skill-director-and-parameterization.md  2026-09-01 Remotion Skill 导演层与参数化默认输出修订
│   │   ├── 2026-09-02-jianwei-remotion-parameterization.md  Studio 右侧 Default Props 可编辑性验收修订 Remotion Skill 导演层、重叠节奏与参数化默认输出修订
│   │   ├── 2026-09-04-remotion-reference-fidelity-and-preview-gate.md  Remotion Skill 参考图保真、低清预览与最终渲染确认门修订
│   │   ├── 2026-09-05-remotion-deterministic-layout.md  Remotion Skill 修订：数字与高密度布局确定性
│   │   ├── 2026-09-05-remotion-director-expansion-and-background-fidelity.md  Remotion Skill 内部导演加工、动作自然度与背景保真修订
│   │   ├── 2026-09-05-remotion-layout-locked-continuity.md  Remotion 参考图几何锁定与连续性审计
│   │   ├── 2026-09-05-remotion-text-stability-and-director-console.md  Remotion Skill 文字抗抖、字体锁定、布局稳定校验与导演台固定输出修订
│   │   ├── 2026-09-05-remotion-text-visibility-and-clipping.md  Remotion Skill 文字与关键元素完整可见、裁剪祖先和最长参数压力测试修订
│   │   ├── 2026-09-05-remotion-universal-adaptive-architecture.md  Remotion Skill 几何锁定、禁止片尾整图覆盖与连续性审计修订
│   │   ├── 2026-09-07-structure-sync-and-content-routing.md  结构镜像同步与表达/自媒体分流修订
│   │   ├── 2026-09-07-training-review-generalization-and-reinforcement.md  AI 培训复盘通用化与重复错误强化机制
│   │   ├── 2026-09-12-context-operation-and-attribution.md  2026-09-12：上下文运行规则与资料归属纠正
│   │   └── README.md  仓库修订索引
│   ├── roadmap.md  长期维护与演进
│   ├── templates/  项目、案例与方法模板
│   │   ├── case.md  实战案例模板
│   │   ├── method.md  方法卡模板
│   │   ├── project.md  项目入口模板
│   │   └── README.md  项目、案例与方法模板
│   └── versioned-knowledge-policy.md  动态产品知识与版本治理
├── history/  一级目录：历史与追溯
│   ├── archived-projects/  二级目录：已归档项目
│   │   ├── openclaw-agent/  OpenClaw AI Agent
│   │   │   └── README.md  OpenClaw Agent 历史档案
│   │   ├── README.md  归档项目索引
│   │   ├── videoai/  VideoAI — AI 驱动的营销视频自动化平台
│   │   │   ├── cost-analysis.md  历史成本测算
│   │   │   ├── pricing-plan-association.md  历史协会定价方案
│   │   │   └── README.md  VideoAI 历史项目入口
│   │   └── xinghuo-ying-guozhou-vr-courseware/  星火映果州 VR 交互课件
│   │       ├── interaction-logic.md  Nibiru 场景交互逻辑
│   │       └── README.md  星火映果州 VR 课件历史入口
│   ├── README.md  历史入口和读取边界
│   └── timeline.md  跨领域成长与里程碑时间线
├── .gitattributes  Git 文本属性与换行规范
├── .github/  GitHub 自动校验
│   ├── README.md  GitHub 自动校验
│   └── workflows/  目录入口
│       └── context-validation.yml  自动化配置
└── .gitignore  Git 忽略规则，排除不应入库的本地文件
```

## 二、归类判断顺序

新增资料前依次判断：

1. 是建委本人的概要事实吗？是则进入 `personal/`。
2. 是建委本人跨场景稳定的思维认知，或所有中文内容共用的 AI 表达规则吗？是则进入 `brain/` 对应分支。
3. 是某个工作领域的经验、工具或项目吗？是则进入 `work/` 对应最具体分支。
4. 是仓库维护、设备或运行环境吗？是则进入 `repository/`。
5. 只剩历史追溯价值、已经退出主线吗？是则进入 `history/`。

无法明确归类时不新建“杂项”目录，先确认长期用途。

## 三、工作目录的组织方式

```text
work/<大领域>/<具体门类>/<experience|tools|projects|cases>/<具体主题>/
```

- 大领域目前只有 `design`、`ai`、`other`。
- 上式表示职责关系，不要求空建所有层级；沿用已有最具体目录，短案例与长期项目按实际需要分开。
- 工具不是项目，例如百度秒哒位于 `programming/tools/`。
- 项目不是通用经验，例如言剪 AI 位于 `programming/projects/`。
- 使用 AI 不自动改变业务归属：AI 设计仍在设计，AI 视频微课仍以微课交付归入设计。
- `work/other/commercial/`按招生、销售、提案或正式交付目的引用；一个主任务可自动组合多个必要领域，纯教学不触发购买承接。建委个人商业认知仍在 `brain/cognition/`。

## 四、README 与文件索引

- 每个需要独立激活的领域、工具和项目必须有 `README.md`。
- README 说明定位、边界、当前事实、文件索引、激活条件和写入方式。
- 新增文件时必须更新最近一层 README；上层 README 只索引下一层，不重复罗列所有叶子文件。
- 用户要求展示完整仓库时，按本文件这种连续树状层级展示，并附中文说明；禁止按文件类型或搜索结果分散罗列。

## 五、清洗与历史

- 当前 README 只保留当前有效口径，不堆叠相互冲突的旧结论。
- 新发生的重大变化写入就近 `revisions/YYYY-MM-DD-slug.md`，history只保留摘要与链接；当前状态同步权威入口。已存在的历史来源保留原位置。
- 普通编辑、格式修改和过程日志只保留在 Git 提交历史中。
- 原始材料放在最具体主题下的 `reference-materials/` 或 `raw/`；中文表达语料统一进入 `brain/ai-expression/chinese-datasets/`。必须有上层 README 说明来源、授权和用途，默认不激活。
- 退出主线且仍需保留的项目进入 `history/archived-projects/`；用户明确要求彻底清除时同步去掉当前树和历史引用，不另建归档。

## 六、命名、安全与提交

- 目录和普通文件采用小写 kebab-case；固定入口保留 `README.md`、`AGENTS.md`、`STRUCTURE.md`、`STRUCTURE.html`、`llms.txt`。其中 `STRUCTURE.html` 是自动生成文件。
- Markdown 使用 UTF-8、LF 和相对链接。
- 不保存密码、API Key、Token、Cookie、完整认证文件或可直接利用的隐私信息。
- 按[维护步骤](./repository/maintenance/README.md)先同步导航、结构与HTML，再校验、复核并暂存。pre-commit检查暂存快照，不静默生成或暂存额外文件；桌面镜像仅在Windows按已生成HTML同步，不影响仓库内容校验。

*结构最后确认：2026-09-12*
