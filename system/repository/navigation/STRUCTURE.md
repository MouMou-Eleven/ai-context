# 仓库结构与归类规范

日常从[分级知识导航](./STRUCTURE.html)逐层查看；其中“完整文件”视图保留全部技术文件及第三方快照内部层级。README是目录入口，不在日常树重复为平级业务节点；Skill实体只在完整文件视图展开。下方完整文件树自动生成。

## 完整文件树

```text
ai-context/
├── README.md  建委日常使用的四个主入口
├── AGENTS.md  AI启动与必要读取规则
├── llms.txt  兼容调用的极短指针，完整任务指南位于系统导航
├── personal/  个人信息与事实
│   ├── business-overview.md  业务与项目概要
│   ├── credentials.md  背书荣誉和成果
│   ├── profile.md  我是谁
│   ├── README.md  个人信息总窗口、索引、写入准则
│   └── timeline.md  个人经历与阶段里程碑
├── brain/  建委的认知与判断
│   ├── business-cognition.md  商业、增长、内容经营与经营判断
│   ├── README.md  认知入口、读取路由与写入边界
│   └── thinking-and-decisions.md  思维、判断、框架拆解、学习与决策方式
├── work/  领域知识、项目事实与实践案例
│   ├── domains/  领域知识：这类工作怎样做
│   │   ├── design/  按交付物组织设计制作经验
│   │   │   ├── common/  设计共用方法
│   │   │   │   ├── ai-assisted-design.md  AI辅助视觉生产方法
│   │   │   │   ├── production-workflow.md  设计制作与经验复用流程
│   │   │   │   └── README.md  设计共用方法
│   │   │   ├── graphic/  平面与演示
│   │   │   │   ├── book/  书籍封面与版式
│   │   │   │   │   └── README.md  书籍装帧与版式设计入口
│   │   │   │   ├── poster-fold/  海报与折页
│   │   │   │   │   └── README.md  海报、折页及平面物料设计入口
│   │   │   │   ├── ppt/  PPT设计
│   │   │   │   │   └── README.md  PPT 设计经验与项目入口
│   │   │   │   └── README.md  平面与演示
│   │   │   ├── README.md  设计制作入口，项目与案例来自统一登记
│   │   │   └── video/  视频、动画与教育作品
│   │   │       ├── common/  视频共用制作方法与工具
│   │   │       │   ├── ae-production.md  AE包装、合成与工程交付要求
│   │   │       │   ├── README.md  跨片型通用制作经验
│   │   │       │   └── tools/  AI 视频工具
│   │   │       │       ├── README.md  工具索引
│   │   │       │       └── seedance/  Seedance 实战
│   │   │       │           ├── practical-workflow.md  实战工作流
│   │   │       │           ├── prompt-cases.md  提示词案例
│   │   │       │           ├── prompt-templates.md  提示词模板
│   │   │       │           └── README.md  Seedance 工具入口
│   │   │       ├── education/  微课与教育交互
│   │   │       │   ├── README.md  微课、精品课、MG 动画与教育课件
│   │   │       │   └── showcase-guidelines.md  哞哞微课案例展示写作规范
│   │   │       ├── promo/  宣传片
│   │   │       │   ├── prompt-iteration.md  企业片提示词节奏与迭代经验
│   │   │       │   ├── README.md  企业宣传片制作经验
│   │   │       │   ├── visual-recipes.md  科技企业片可选视觉配方
│   │   │       │   └── workflow.md  企业宣传片通用制作与验收流程
│   │   │       ├── README.md  类型索引
│   │   │       └── story/  故事与叙事影片
│   │   │           ├── motion-comic.md  漫剧制作入口
│   │   │           └── README.md  真人实拍故事与电影叙事
│   │   ├── development/  应用开发与自动化
│   │   │   ├── experience/  通用编程经验
│   │   │   │   ├── creative-frontend-prompt-patterns.md  创意前端提示词方法
│   │   │   │   ├── README.md  经验索引
│   │   │   │   └── reference-materials/  编程参考资料
│   │   │   │       ├── creative-frontend-prompts/  创意前端提示词原始样例
│   │   │   │       │   ├── raw/  未经提炼的原文
│   │   │   │       │   │   ├── dark-editorial-portfolio.txt  文本资料
│   │   │   │       │   │   ├── jack-3d-creator-portfolio.txt  文本资料
│   │   │   │       │   │   ├── prmpt-fashion-archive.txt  文本资料
│   │   │   │       │   │   ├── sentinel-spline-3d-hero.txt  文本资料
│   │   │   │       │   │   └── synapsex-video-scrub.txt  文本资料
│   │   │   │       │   └── README.md  创意前端原始提示词索引
│   │   │   │       └── README.md  参考资料索引
│   │   │   ├── README.md  应用开发与自动化入口
│   │   │   └── tools/  编程工具
│   │   │       ├── miaoda/  百度秒哒
│   │   │       │   ├── basics/  基础与发布
│   │   │       │   │   ├── current-capabilities.md  当前能力、权益与限制
│   │   │       │   │   ├── platform-basics.md  平台基础能力
│   │   │       │   │   ├── publish-channels.md  发布渠道与限制
│   │   │       │   │   └── README.md  基础资料索引
│   │   │       │   ├── development/  开发能力
│   │   │       │   │   ├── README.md  开发资料索引
│   │   │       │   │   ├── skill-as-callable.md  秒哒作为可调用 Skill
│   │   │       │   │   └── skill-development.md  秒哒 Skill 开发
│   │   │       │   ├── disambiguation.md  百度秒哒与飞书妙搭的同名辨析
│   │   │       │   ├── experience/  实战经验
│   │   │       │   │   ├── cases/  案例
│   │   │       │   │   │   ├── README.md  案例索引
│   │   │       │   │   │   └── yungouos-jsapi.md  云购 OS JSAPI 案例
│   │   │       │   │   ├── patterns/  可复用工作模式
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
│   │   │       │   │   └── reference-materials/  原始参考资料
│   │   │       │   │       ├── README.md  参考资料索引
│   │   │       │   │       └── video-chunked-upload/  video-chunked-upload — 旧环境兼容源码
│   │   │       │   │           ├── legacy-contract.md  旧环境分片上传合同与专用提示词
│   │   │       │   │           ├── README.md  视频分片上传源码说明
│   │   │       │   │           ├── video-serve.ts  资料与资源
│   │   │       │   │           ├── video-upload-chunk.ts  资料与资源
│   │   │       │   │           └── video-upload-complete.ts  资料与资源
│   │   │       │   ├── llms.txt  秒哒最小读取路由
│   │   │       │   ├── README.md  秒哒总入口与读取边界
│   │   │       │   └── updates/  版本与升级
│   │   │       │       ├── 2026-08-02-version-governance.md  版本知识治理记录
│   │   │       │       ├── 2026-08-15-cloud-runtime-diagnostics.md  云端运行诊断记录
│   │   │       │       ├── 2026-08-29-v3.7-and-upload-limit-governance.md  V3.7 与上传限制口径修订
│   │   │       │       ├── 2026-09-07-codex-miaoda-incremental-loop.md  Codex 协助秒哒增量闭环修订
│   │   │       │       ├── README.md  版本资料索引
│   │   │       │       └── version-features.md  历史版本能力时间线
│   │   │       └── README.md  工具索引
│   │   ├── other/  其他领域
│   │   │   ├── commercial/  商业化与对外交付
│   │   │   │   ├── experience/  商业经验与交付方法
│   │   │   │   │   ├── business-analysis-cards.md  产品信息、渠道与对标执行卡
│   │   │   │   │   ├── case-result-narrative.md  案例选择、结果证明、观点叙事与产品承接
│   │   │   │   │   ├── competition-and-investor-materials.md  赛事、路演与融资材料的对外边界
│   │   │   │   │   ├── content-demand-and-conversion.md  内容驱动的需求识别与商业承接
│   │   │   │   │   ├── external-deliverable-language.md  对外成品与内部工作稿的语言边界
│   │   │   │   │   └── README.md  内容经营与商业交付经验索引
│   │   │   │   └── README.md  跨行业商业方法、触发规则与交付边界
│   │   │   ├── README.md  其他领域与项目索引及准入条件
│   │   │   └── skills/  Skill库
│   │   │       ├── editaplot/  EditaPlot
│   │   │       │   ├── README.md  科研绘图 Skill 的调用、前提与更新方法
│   │   │       │   ├── source/  上游完整快照，共 662 个文件；展开可核查内部层级
│   │   │       │   │   ├── .gitattributes  资料与资源
│   │   │       │   │   ├── .github/  目录入口
│   │   │       │   │   │   ├── CODEOWNERS  资料与资源
│   │   │       │   │   │   ├── dependabot.yml  自动化配置
│   │   │       │   │   │   └── workflows/  目录入口
│   │   │       │   │   │       ├── star-trend.yml  自动化配置
│   │   │       │   │   │       └── tests.yml  自动化配置
│   │   │       │   │   ├── .gitignore  资料与资源
│   │   │       │   │   ├── ASSET_PROVENANCE.md  Asset and data provenance
│   │   │       │   │   ├── assets/  目录入口
│   │   │       │   │   │   ├── gallery/  目录入口
│   │   │       │   │   │   │   ├── bar-error-groups.png  图片素材
│   │   │       │   │   │   │   ├── bubble-indexed-size.png  图片素材
│   │   │       │   │   │   │   ├── circular-network.png  图片素材
│   │   │       │   │   │   │   ├── cv-cycles.png  图片素材
│   │   │       │   │   │   │   ├── density-ridgeline3d.png  图片素材
│   │   │       │   │   │   │   ├── diverging-effects.png  图片素材
│   │   │       │   │   │   │   ├── dsc-multi.png  图片素材
│   │   │       │   │   │   │   ├── eis-nyquist.png  图片素材
│   │   │       │   │   │   │   ├── forest-intervals.png  图片素材
│   │   │       │   │   │   │   ├── ftir-temperature-series.png  图片素材
│   │   │       │   │   │   │   ├── gallery-manifest.json  结构化配置与索引
│   │   │       │   │   │   │   ├── heatmap-dense-30x30.png  图片素材
│   │   │       │   │   │   │   ├── heatmap-dense-40x40.png  图片素材
│   │   │       │   │   │   │   ├── heatmap-results.png  图片素材
│   │   │       │   │   │   │   ├── histogram-frozen-bins.png  图片素材
│   │   │       │   │   │   │   ├── horizontal-long-labels.png  图片素材
│   │   │       │   │   │   │   ├── line-error.png  图片素材
│   │   │       │   │   │   │   ├── lsv-multi.png  图片素材
│   │   │       │   │   │   │   ├── medical-agreement.png  图片素材
│   │   │       │   │   │   │   ├── medical-calibration.png  图片素材
│   │   │       │   │   │   │   ├── medical-confusion.png  图片素材
│   │   │       │   │   │   │   ├── medical-decision.png  图片素材
│   │   │       │   │   │   │   ├── medical-grouped-box.png  图片素材
│   │   │       │   │   │   │   ├── medical-longitudinal.png  图片素材
│   │   │       │   │   │   │   ├── medical-pr.png  图片素材
│   │   │       │   │   │   │   ├── medical-raincloud.png  图片素材
│   │   │       │   │   │   │   ├── medical-roc.png  图片素材
│   │   │       │   │   │   │   ├── medical-shap.png  图片素材
│   │   │       │   │   │   │   ├── nmr-comparison.png  图片素材
│   │   │       │   │   │   │   ├── percent-composition.png  图片素材
│   │   │       │   │   │   │   ├── pie-five-parts.png  图片素材
│   │   │       │   │   │   │   ├── pl-steady-state.png  图片素材
│   │   │       │   │   │   │   ├── pl-temperature-series.png  图片素材
│   │   │       │   │   │   │   ├── pl-trpl.png  图片素材
│   │   │       │   │   │   │   ├── radar-multimetric.png  图片素材
│   │   │       │   │   │   │   ├── raw-observations.png  图片素材
│   │   │       │   │   │   │   ├── sankey-flow.png  图片素材
│   │   │       │   │   │   │   ├── scatter-dense.png  图片素材
│   │   │       │   │   │   │   ├── stacked-composition.png  图片素材
│   │   │       │   │   │   │   ├── trajectory3d.png  图片素材
│   │   │       │   │   │   │   ├── trend-progression.png  图片素材
│   │   │       │   │   │   │   ├── uv-vis-multi.png  图片素材
│   │   │       │   │   │   │   ├── uv-vis-tauc.png  图片素材
│   │   │       │   │   │   │   ├── violin-distributions.png  图片素材
│   │   │       │   │   │   │   ├── xas-profiles.png  图片素材
│   │   │       │   │   │   │   ├── xps-comparison.png  图片素材
│   │   │       │   │   │   │   ├── xps-fit.png  图片素材
│   │   │       │   │   │   │   └── xrd-multi.png  图片素材
│   │   │       │   │   │   ├── palettes/  目录入口
│   │   │       │   │   │   │   ├── cards/  目录入口
│   │   │       │   │   │   │   │   ├── amber_lavender.png  图片素材
│   │   │       │   │   │   │   │   ├── blue_coral.png  图片素材
│   │   │       │   │   │   │   │   ├── deep_sea_gold.png  图片素材
│   │   │       │   │   │   │   │   ├── forest_amber.png  图片素材
│   │   │       │   │   │   │   │   ├── navy_cyan_gold.png  图片素材
│   │   │       │   │   │   │   │   ├── navy_ember.png  图片素材
│   │   │       │   │   │   │   │   ├── ocean_coral.png  图片素材
│   │   │       │   │   │   │   │   ├── plum_rose.png  图片素材
│   │   │       │   │   │   │   │   ├── sky_terra.png  图片素材
│   │   │       │   │   │   │   │   └── violet_lime.png  图片素材
│   │   │       │   │   │   │   ├── palette-catalog.json  结构化配置与索引
│   │   │       │   │   │   │   ├── palette-selector-all.zh-CN.png  图片素材
│   │   │       │   │   │   │   └── palette-selector-public.zh-CN.png  图片素材
│   │   │       │   │   │   ├── provenance-manifest.json  结构化配置与索引
│   │   │       │   │   │   ├── star-trend/  目录入口
│   │   │       │   │   │   │   ├── stars.json  结构化配置与索引
│   │   │       │   │   │   │   └── stars.svg  资料与资源
│   │   │       │   │   │   └── support/  目录入口
│   │   │       │   │   │       └── wechat-tip.png  图片素材
│   │   │       │   │   ├── AUTHORS.md  Authors and contributors
│   │   │       │   │   ├── CHANGELOG.md  Changelog
│   │   │       │   │   ├── CONTRIBUTING.md  Contributing
│   │   │       │   │   ├── docs/  目录入口
│   │   │       │   │   │   ├── dependency-inventory.md  Verified Python dependency inventory
│   │   │       │   │   │   ├── gallery.en.md  Origin 2024b figures generated and reviewed on a live installation
│   │   │       │   │   │   ├── gallery.md  Origin 2024b 实机生成并复核的图形示例
│   │   │       │   │   │   ├── installation.md  安装与环境自检 / Installation
│   │   │       │   │   │   ├── origin-2021-2026-compatibility.md  EditaPlot 的 Origin 2021–2026b 兼容说明
│   │   │       │   │   │   ├── palette-guide.md  科研配色指南
│   │   │       │   │   │   ├── quickstart.en.md  English quick start
│   │   │       │   │   │   ├── quickstart.zh-CN.md  中文快速开始
│   │   │       │   │   │   └── release-boundaries.md  发布、隐私与许可边界
│   │   │       │   │   ├── editaplot.cmd  资料与资源
│   │   │       │   │   ├── examples/  目录入口
│   │   │       │   │   │   ├── ambiguous_xy.csv  资料与资源
│   │   │       │   │   │   ├── category_one_series.csv  资料与资源
│   │   │       │   │   │   ├── category_two_series.csv  资料与资源
│   │   │       │   │   │   ├── eis_bode_zh.csv  资料与资源
│   │   │       │   │   │   ├── gallery/  目录入口
│   │   │       │   │   │   │   ├── bar_grouped_error.csv  资料与资源
│   │   │       │   │   │   │   ├── bubble_indexed_size.csv  资料与资源
│   │   │       │   │   │   │   ├── circular_network.csv  资料与资源
│   │   │       │   │   │   │   ├── cv_cycles.csv  资料与资源
│   │   │       │   │   │   │   ├── density_ridgeline3d.csv  资料与资源
│   │   │       │   │   │   │   ├── diverging_effects.csv  资料与资源
│   │   │       │   │   │   │   ├── dsc_multi.csv  资料与资源
│   │   │       │   │   │   │   ├── eis_nyquist.csv  资料与资源
│   │   │       │   │   │   │   ├── forest_intervals.csv  资料与资源
│   │   │       │   │   │   │   ├── ftir_temperature_series.csv  资料与资源
│   │   │       │   │   │   │   ├── grouped_box_medical.csv  资料与资源
│   │   │       │   │   │   │   ├── heatmap_dense_30x30.csv  资料与资源
│   │   │       │   │   │   │   ├── heatmap_dense_40x40.csv  资料与资源
│   │   │       │   │   │   │   ├── heatmap_results.csv  资料与资源
│   │   │       │   │   │   │   ├── histogram_values.csv  资料与资源
│   │   │       │   │   │   │   ├── horizontal_long_labels.csv  资料与资源
│   │   │       │   │   │   │   ├── line_error.csv  资料与资源
│   │   │       │   │   │   │   ├── lsv_multi.csv  资料与资源
│   │   │       │   │   │   │   ├── medical_bland_altman.csv  资料与资源
│   │   │       │   │   │   │   ├── medical_calibration.csv  资料与资源
│   │   │       │   │   │   │   ├── medical_confusion.csv  资料与资源
│   │   │       │   │   │   │   ├── medical_decision.csv  资料与资源
│   │   │       │   │   │   │   ├── medical_paired.csv  资料与资源
│   │   │       │   │   │   │   ├── medical_pr.csv  资料与资源
│   │   │       │   │   │   │   ├── medical_raincloud.csv  资料与资源
│   │   │       │   │   │   │   ├── medical_roc.csv  资料与资源
│   │   │       │   │   │   │   ├── medical_shap_summary.csv  资料与资源
│   │   │       │   │   │   │   ├── nmr_comparison.csv  资料与资源
│   │   │       │   │   │   │   ├── percent_composition.csv  资料与资源
│   │   │       │   │   │   │   ├── pie_five_parts.csv  资料与资源
│   │   │       │   │   │   │   ├── pl_steady_state.csv  资料与资源
│   │   │       │   │   │   │   ├── pl_temperature_series.csv  资料与资源
│   │   │       │   │   │   │   ├── pl_trpl.csv  资料与资源
│   │   │       │   │   │   │   ├── radar_multimetric.csv  资料与资源
│   │   │       │   │   │   │   ├── raw_observations.csv  资料与资源
│   │   │       │   │   │   │   ├── sankey_four_stage.csv  资料与资源
│   │   │       │   │   │   │   ├── scatter_dense.csv  资料与资源
│   │   │       │   │   │   │   ├── stacked_composition.csv  资料与资源
│   │   │       │   │   │   │   ├── trajectory3d.csv  资料与资源
│   │   │       │   │   │   │   ├── trend_progression.csv  资料与资源
│   │   │       │   │   │   │   ├── uv_vis_multi.csv  资料与资源
│   │   │       │   │   │   │   ├── uv_vis_tauc.csv  资料与资源
│   │   │       │   │   │   │   ├── violin_distributions.csv  资料与资源
│   │   │       │   │   │   │   ├── xas_profiles.csv  资料与资源
│   │   │       │   │   │   │   ├── xps_compare.csv  资料与资源
│   │   │       │   │   │   │   ├── xps_fit.csv  资料与资源
│   │   │       │   │   │   │   └── xrd_multi.csv  资料与资源
│   │   │       │   │   │   ├── line_error_zh.csv  资料与资源
│   │   │       │   │   │   ├── sankey_zh.csv  资料与资源
│   │   │       │   │   │   ├── xps_fit.csv  资料与资源
│   │   │       │   │   │   └── xrd_multi.csv  资料与资源
│   │   │       │   │   ├── LICENSE  资料与资源
│   │   │       │   │   ├── NOTICE  资料与资源
│   │   │       │   │   ├── PRIVACY.md  Privacy
│   │   │       │   │   ├── pyproject.toml  资料与资源
│   │   │       │   │   ├── README.en.md  说明与资料
│   │   │       │   │   ├── README.md  说明与资料
│   │   │       │   │   ├── release/  目录入口
│   │   │       │   │   │   └── public-release-policy.json  结构化配置与索引
│   │   │       │   │   ├── requirements-runtime.lock  资料与资源
│   │   │       │   │   ├── requirements-runtime.txt  文本资料
│   │   │       │   │   ├── runtime/  目录入口
│   │   │       │   │   │   ├── LICENSE  资料与资源
│   │   │       │   │   │   ├── NOTICE  资料与资源
│   │   │       │   │   │   ├── pyproject.toml  资料与资源
│   │   │       │   │   │   ├── requirements-runtime.lock  资料与资源
│   │   │       │   │   │   ├── requirements-runtime.txt  文本资料
│   │   │       │   │   │   ├── runtime-manifest.json  结构化配置与索引
│   │   │       │   │   │   ├── src/  目录入口
│   │   │       │   │   │   │   └── origin_sciplot/  目录入口
│   │   │       │   │   │   │       ├── __init__.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       ├── __main__.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       ├── app.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       ├── circular_network_layout.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       ├── data_loader.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       ├── heatmap_layout.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       ├── logging_utils.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       ├── main_window.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       ├── origin_backend/  目录入口
│   │   │       │   │   │   │       │   ├── __init__.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       │   ├── base_style_contract.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       │   ├── capabilities.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       │   ├── categorical_renderer.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       │   ├── density_ridgeline3d_renderer.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       │   ├── evidence_renderer.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       │   ├── execution_context.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       │   ├── export_utils.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       │   ├── job_queue.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       │   ├── network_renderer.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       │   ├── safe_errors.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       │   ├── scientific_renderer.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       │   ├── session.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       │   ├── smoke_test.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       │   ├── template_capabilities.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       │   ├── trajectory3d_renderer.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       │   ├── verify_utils.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       │   └── version_risks.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       ├── output_manager.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       ├── palette_catalog.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       ├── project_paths.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       ├── reference_adaptation.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       ├── reference_figure.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       ├── reference_style.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       ├── resources/  目录入口
│   │   │       │   │   │   │       │   ├── app_icon.png  图片素材
│   │   │       │   │   │   │       │   └── qss/  目录入口
│   │   │       │   │   │   │       │       └── main.qss  资料与资源
│   │   │       │   │   │   │       ├── scientific_preview.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       ├── scientific_visual.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       ├── scientific_workflow.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       ├── semantic_analysis.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       ├── semantic_contract.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       ├── shap_composite.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       ├── shap_layout.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       ├── template_registry.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       ├── template_service.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       ├── validation/  目录入口
│   │   │       │   │   │   │       │   ├── __init__.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       │   ├── csv_validator.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       │   └── schema_models.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       ├── workers/  目录入口
│   │   │       │   │   │   │       │   ├── __init__.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       │   ├── origin_smoke_worker.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       │   ├── process_launcher.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       │   ├── progress_protocol.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       │   └── run_template_worker.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       ├── xps_adaptive.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       ├── xps_preview.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       ├── xps_visual_style.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       ├── xps_workflow.py  跨平台维护或执行脚本
│   │   │       │   │   │   │       └── xrd_semantics.py  跨平台维护或执行脚本
│   │   │       │   │   │   └── templates/  目录入口
│   │   │       │   │   │       ├── bar/  目录入口
│   │   │       │   │   │       │   ├── data_contract.md  柱状图数据合同
│   │   │       │   │   │       │   ├── data_template.csv  资料与资源
│   │   │       │   │   │       │   ├── example_multi_group.csv  资料与资源
│   │   │       │   │   │       │   ├── example_standard.csv  资料与资源
│   │   │       │   │   │       │   ├── manifest.yaml  自动化配置
│   │   │       │   │   │       │   ├── runner.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── schema.json  结构化配置与索引
│   │   │       │   │   │       │   ├── service.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   └── visual_contract.md  柱状图视觉合同
│   │   │       │   │   │       ├── bland_altman/  目录入口
│   │   │       │   │   │       │   ├── data_contract.md  数据合同
│   │   │       │   │   │       │   ├── data_template.csv  资料与资源
│   │   │       │   │   │       │   ├── example_standard.csv  资料与资源
│   │   │       │   │   │       │   ├── manifest.yaml  自动化配置
│   │   │       │   │   │       │   ├── runner.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── schema.json  结构化配置与索引
│   │   │       │   │   │       │   ├── service.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   └── visual_contract.md  视觉合同
│   │   │       │   │   │       ├── bubble/  目录入口
│   │   │       │   │   │       │   ├── data_contract.md  气泡图数据合同
│   │   │       │   │   │       │   ├── data_template.csv  资料与资源
│   │   │       │   │   │       │   ├── example_standard.csv  资料与资源
│   │   │       │   │   │       │   ├── manifest.yaml  自动化配置
│   │   │       │   │   │       │   ├── runner.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── schema.json  结构化配置与索引
│   │   │       │   │   │       │   ├── service.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   └── visual_contract.md  气泡图视觉合同
│   │   │       │   │   │       ├── calibration_curve/  目录入口
│   │   │       │   │   │       │   ├── data_contract.md  数据合同
│   │   │       │   │   │       │   ├── data_template.csv  资料与资源
│   │   │       │   │   │       │   ├── example_standard.csv  资料与资源
│   │   │       │   │   │       │   ├── manifest.yaml  自动化配置
│   │   │       │   │   │       │   ├── runner.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── schema.json  结构化配置与索引
│   │   │       │   │   │       │   ├── service.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   └── visual_contract.md  视觉合同
│   │   │       │   │   │       ├── circular_network/  目录入口
│   │   │       │   │   │       │   ├── data_contract.md  环形有向加权网络图数据合同
│   │   │       │   │   │       │   ├── data_template.csv  资料与资源
│   │   │       │   │   │       │   ├── example_standard.csv  资料与资源
│   │   │       │   │   │       │   ├── manifest.yaml  自动化配置
│   │   │       │   │   │       │   ├── origin_acceptance.md  Origin route acceptance — passed
│   │   │       │   │   │       │   ├── runner.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── schema.json  结构化配置与索引
│   │   │       │   │   │       │   ├── service.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   └── visual_contract.md  环形有向加权网络图视觉合同
│   │   │       │   │   │       ├── confusion_matrix/  目录入口
│   │   │       │   │   │       │   ├── data_contract.md  数据合同
│   │   │       │   │   │       │   ├── data_template.csv  资料与资源
│   │   │       │   │   │       │   ├── example_standard.csv  资料与资源
│   │   │       │   │   │       │   ├── manifest.yaml  自动化配置
│   │   │       │   │   │       │   ├── runner.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── schema.json  结构化配置与索引
│   │   │       │   │   │       │   ├── service.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   └── visual_contract.md  视觉合同
│   │   │       │   │   │       ├── cv/  目录入口
│   │   │       │   │   │       │   ├── data_contract.md  CV 数据合同
│   │   │       │   │   │       │   ├── data_template.csv  资料与资源
│   │   │       │   │   │       │   ├── example_standard.csv  资料与资源
│   │   │       │   │   │       │   ├── manifest.yaml  自动化配置
│   │   │       │   │   │       │   ├── runner.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── schema.json  结构化配置与索引
│   │   │       │   │   │       │   ├── service.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   └── visual_contract.md  CV 视觉合同
│   │   │       │   │   │       ├── decision_curve/  目录入口
│   │   │       │   │   │       │   ├── data_contract.md  数据合同
│   │   │       │   │   │       │   ├── data_template.csv  资料与资源
│   │   │       │   │   │       │   ├── example_standard.csv  资料与资源
│   │   │       │   │   │       │   ├── manifest.yaml  自动化配置
│   │   │       │   │   │       │   ├── runner.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── schema.json  结构化配置与索引
│   │   │       │   │   │       │   ├── service.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   └── visual_contract.md  视觉合同
│   │   │       │   │   │       ├── density_ridgeline3d/  目录入口
│   │   │       │   │   │       │   ├── data_contract.md  三维双轮廓密度曲线与基线焦点 mixed-wide 数据合同
│   │   │       │   │   │       │   ├── data_template.csv  资料与资源
│   │   │       │   │   │       │   ├── example_standard.csv  资料与资源
│   │   │       │   │   │       │   ├── manifest.yaml  自动化配置
│   │   │       │   │   │       │   ├── origin_acceptance.md  Origin route acceptance — verified 2026-08-01
│   │   │       │   │   │       │   ├── runner.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── schema.json  结构化配置与索引
│   │   │       │   │   │       │   ├── service.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   └── visual_contract.md  三维双轮廓密度曲线与基线焦点视觉合同
│   │   │       │   │   │       ├── diagnostic_curve/  目录入口
│   │   │       │   │   │       │   ├── data_contract.md  数据合同
│   │   │       │   │   │       │   ├── data_template.csv  资料与资源
│   │   │       │   │   │       │   ├── example_pr.csv  资料与资源
│   │   │       │   │   │       │   ├── example_standard.csv  资料与资源
│   │   │       │   │   │       │   ├── manifest.yaml  自动化配置
│   │   │       │   │   │       │   ├── runner.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── schema.json  结构化配置与索引
│   │   │       │   │   │       │   ├── service.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   └── visual_contract.md  视觉合同
│   │   │       │   │   │       ├── dsc/  目录入口
│   │   │       │   │   │       │   ├── data_contract.md  DSC 数据合同
│   │   │       │   │   │       │   ├── data_template.csv  资料与资源
│   │   │       │   │   │       │   ├── example_standard.csv  资料与资源
│   │   │       │   │   │       │   ├── manifest.yaml  自动化配置
│   │   │       │   │   │       │   ├── runner.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── schema.json  结构化配置与索引
│   │   │       │   │   │       │   ├── service.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   └── visual_contract.md  DSC 视觉合同
│   │   │       │   │   │       ├── eis/  目录入口
│   │   │       │   │   │       │   ├── data_contract.md  EIS 数据合同
│   │   │       │   │   │       │   ├── data_template.csv  资料与资源
│   │   │       │   │   │       │   ├── example_bode.csv  资料与资源
│   │   │       │   │   │       │   ├── example_standard.csv  资料与资源
│   │   │       │   │   │       │   ├── manifest.yaml  自动化配置
│   │   │       │   │   │       │   ├── runner.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── schema.json  结构化配置与索引
│   │   │       │   │   │       │   ├── service.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   └── visual_contract.md  EIS 视觉合同
│   │   │       │   │   │       ├── forest/  目录入口
│   │   │       │   │   │       │   ├── data_contract.md  森林图数据合同
│   │   │       │   │   │       │   ├── data_template.csv  资料与资源
│   │   │       │   │   │       │   ├── example_standard.csv  资料与资源
│   │   │       │   │   │       │   ├── manifest.yaml  自动化配置
│   │   │       │   │   │       │   ├── runner.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── schema.json  结构化配置与索引
│   │   │       │   │   │       │   ├── service.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   └── visual_contract.md  森林图视觉合同
│   │   │       │   │   │       ├── ftir/  目录入口
│   │   │       │   │   │       │   ├── data_contract.md  FTIR / IR 数据合同
│   │   │       │   │   │       │   ├── data_template.csv  资料与资源
│   │   │       │   │   │       │   ├── example_standard.csv  资料与资源
│   │   │       │   │   │       │   ├── manifest.yaml  自动化配置
│   │   │       │   │   │       │   ├── runner.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── schema.json  结构化配置与索引
│   │   │       │   │   │       │   ├── service.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   └── visual_contract.md  FTIR / IR 视觉合同
│   │   │       │   │   │       ├── grouped_box/  目录入口
│   │   │       │   │   │       │   ├── data_contract.md  数据合同
│   │   │       │   │   │       │   ├── data_template.csv  资料与资源
│   │   │       │   │   │       │   ├── example_standard.csv  资料与资源
│   │   │       │   │   │       │   ├── manifest.yaml  自动化配置
│   │   │       │   │   │       │   ├── runner.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── schema.json  结构化配置与索引
│   │   │       │   │   │       │   ├── service.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   └── visual_contract.md  视觉合同
│   │   │       │   │   │       ├── heatmap/  目录入口
│   │   │       │   │   │       │   ├── data_contract.md  热力图数据合同
│   │   │       │   │   │       │   ├── data_template.csv  资料与资源
│   │   │       │   │   │       │   ├── example_standard.csv  资料与资源
│   │   │       │   │   │       │   ├── manifest.yaml  自动化配置
│   │   │       │   │   │       │   ├── runner.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── schema.json  结构化配置与索引
│   │   │       │   │   │       │   ├── service.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   └── visual_contract.md  热力图视觉合同
│   │   │       │   │   │       ├── histogram/  目录入口
│   │   │       │   │   │       │   ├── data_contract.md  直方图数据合同
│   │   │       │   │   │       │   ├── data_template.csv  资料与资源
│   │   │       │   │   │       │   ├── example_standard.csv  资料与资源
│   │   │       │   │   │       │   ├── manifest.yaml  自动化配置
│   │   │       │   │   │       │   ├── runner.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── schema.json  结构化配置与索引
│   │   │       │   │   │       │   ├── service.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   └── visual_contract.md  直方图视觉合同
│   │   │       │   │   │       ├── horizontal_bar/  目录入口
│   │   │       │   │   │       │   ├── data_contract.md  横向分组条形图数据合同
│   │   │       │   │   │       │   ├── data_template.csv  资料与资源
│   │   │       │   │   │       │   ├── example_standard.csv  资料与资源
│   │   │       │   │   │       │   ├── manifest.yaml  自动化配置
│   │   │       │   │   │       │   ├── runner.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── schema.json  结构化配置与索引
│   │   │       │   │   │       │   ├── service.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   └── visual_contract.md  横向分组条形图视觉合同
│   │   │       │   │   │       ├── line_error/  目录入口
│   │   │       │   │   │       │   ├── data_contract.md  带误差折线图数据合同
│   │   │       │   │   │       │   ├── data_template.csv  资料与资源
│   │   │       │   │   │       │   ├── example_chinese.csv  资料与资源
│   │   │       │   │   │       │   ├── example_standard.csv  资料与资源
│   │   │       │   │   │       │   ├── manifest.yaml  自动化配置
│   │   │       │   │   │       │   ├── runner.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── schema.json  结构化配置与索引
│   │   │       │   │   │       │   ├── service.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   └── visual_contract.md  带误差折线图视觉合同
│   │   │       │   │   │       ├── lsv/  目录入口
│   │   │       │   │   │       │   ├── data_contract.md  LSV 数据合同
│   │   │       │   │   │       │   ├── data_template.csv  资料与资源
│   │   │       │   │   │       │   ├── example_standard.csv  资料与资源
│   │   │       │   │   │       │   ├── manifest.yaml  自动化配置
│   │   │       │   │   │       │   ├── runner.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── schema.json  结构化配置与索引
│   │   │       │   │   │       │   ├── service.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   └── visual_contract.md  LSV 视觉合同
│   │   │       │   │   │       ├── nmr/  目录入口
│   │   │       │   │   │       │   ├── data_contract.md  NMR 数据合同
│   │   │       │   │   │       │   ├── data_template.csv  资料与资源
│   │   │       │   │   │       │   ├── example_standard.csv  资料与资源
│   │   │       │   │   │       │   ├── manifest.yaml  自动化配置
│   │   │       │   │   │       │   ├── runner.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── schema.json  结构化配置与索引
│   │   │       │   │   │       │   ├── service.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   └── visual_contract.md  NMR 视觉合同
│   │   │       │   │   │       ├── paired_trajectory/  目录入口
│   │   │       │   │   │       │   ├── data_contract.md  数据合同
│   │   │       │   │   │       │   ├── data_template.csv  资料与资源
│   │   │       │   │   │       │   ├── example_standard.csv  资料与资源
│   │   │       │   │   │       │   ├── manifest.yaml  自动化配置
│   │   │       │   │   │       │   ├── runner.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── schema.json  结构化配置与索引
│   │   │       │   │   │       │   ├── service.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   └── visual_contract.md  视觉合同
│   │   │       │   │   │       ├── percent_stacked_bar/  目录入口
│   │   │       │   │   │       │   ├── data_contract.md  百分比堆叠柱状图数据合同
│   │   │       │   │   │       │   ├── data_template.csv  资料与资源
│   │   │       │   │   │       │   ├── example_standard.csv  资料与资源
│   │   │       │   │   │       │   ├── manifest.yaml  自动化配置
│   │   │       │   │   │       │   ├── runner.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── schema.json  结构化配置与索引
│   │   │       │   │   │       │   ├── service.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   └── visual_contract.md  百分比堆叠柱状图视觉合同
│   │   │       │   │   │       ├── pie/  目录入口
│   │   │       │   │   │       │   ├── data_contract.md  二维饼图数据合同
│   │   │       │   │   │       │   ├── data_template.csv  资料与资源
│   │   │       │   │   │       │   ├── example_standard.csv  资料与资源
│   │   │       │   │   │       │   ├── manifest.yaml  自动化配置
│   │   │       │   │   │       │   ├── runner.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── schema.json  结构化配置与索引
│   │   │       │   │   │       │   ├── service.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   └── visual_contract.md  二维饼图视觉合同
│   │   │       │   │   │       ├── pl/  目录入口
│   │   │       │   │   │       │   ├── data_contract.md  数据合同
│   │   │       │   │   │       │   ├── data_template.csv  资料与资源
│   │   │       │   │   │       │   ├── example_standard.csv  资料与资源
│   │   │       │   │   │       │   ├── example_temperature_series.csv  资料与资源
│   │   │       │   │   │       │   ├── manifest.yaml  自动化配置
│   │   │       │   │   │       │   ├── runner.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── schema.json  结构化配置与索引
│   │   │       │   │   │       │   ├── service.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   └── visual_contract.md  视觉合同
│   │   │       │   │   │       ├── radar/  目录入口
│   │   │       │   │   │       │   ├── data_contract.md  雷达图数据合同
│   │   │       │   │   │       │   ├── data_template.csv  资料与资源
│   │   │       │   │   │       │   ├── example_standard.csv  资料与资源
│   │   │       │   │   │       │   ├── manifest.yaml  自动化配置
│   │   │       │   │   │       │   ├── runner.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── schema.json  结构化配置与索引
│   │   │       │   │   │       │   ├── service.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   └── visual_contract.md  雷达图视觉合同
│   │   │       │   │   │       ├── raincloud/  目录入口
│   │   │       │   │   │       │   ├── data_contract.md  Raincloud 数据合同
│   │   │       │   │   │       │   ├── data_template.csv  资料与资源
│   │   │       │   │   │       │   ├── example_standard.csv  资料与资源
│   │   │       │   │   │       │   ├── manifest.yaml  自动化配置
│   │   │       │   │   │       │   ├── runner.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── schema.json  结构化配置与索引
│   │   │       │   │   │       │   ├── service.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   └── visual_contract.md  Raincloud 视觉合同
│   │   │       │   │   │       ├── raw_summary/  目录入口
│   │   │       │   │   │       │   ├── data_contract.md  原始点汇总图数据合同
│   │   │       │   │   │       │   ├── data_template.csv  资料与资源
│   │   │       │   │   │       │   ├── example_standard.csv  资料与资源
│   │   │       │   │   │       │   ├── manifest.yaml  自动化配置
│   │   │       │   │   │       │   ├── runner.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── schema.json  结构化配置与索引
│   │   │       │   │   │       │   ├── service.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   └── visual_contract.md  原始点汇总图视觉合同
│   │   │       │   │   │       ├── sankey/  目录入口
│   │   │       │   │   │       │   ├── data_contract.md  桑基图数据合同
│   │   │       │   │   │       │   ├── data_template.csv  资料与资源
│   │   │       │   │   │       │   ├── example_standard.csv  资料与资源
│   │   │       │   │   │       │   ├── manifest.yaml  自动化配置
│   │   │       │   │   │       │   ├── runner.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── schema.json  结构化配置与索引
│   │   │       │   │   │       │   ├── service.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   └── visual_contract.md  桑基图视觉合同
│   │   │       │   │   │       ├── scatter/  目录入口
│   │   │       │   │   │       │   ├── data_contract.md  散点图数据合同
│   │   │       │   │   │       │   ├── data_template.csv  资料与资源
│   │   │       │   │   │       │   ├── example_dense.csv  资料与资源
│   │   │       │   │   │       │   ├── example_standard.csv  资料与资源
│   │   │       │   │   │       │   ├── manifest.yaml  自动化配置
│   │   │       │   │   │       │   ├── runner.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── schema.json  结构化配置与索引
│   │   │       │   │   │       │   ├── service.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   └── visual_contract.md  散点图视觉合同
│   │   │       │   │   │       ├── shap_summary/  目录入口
│   │   │       │   │   │       │   ├── data_contract.md  预计算 SHAP 复合图数据合同
│   │   │       │   │   │       │   ├── data_template.csv  资料与资源
│   │   │       │   │   │       │   ├── example_standard.csv  资料与资源
│   │   │       │   │   │       │   ├── manifest.yaml  自动化配置
│   │   │       │   │   │       │   ├── runner.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── schema.json  结构化配置与索引
│   │   │       │   │   │       │   ├── service.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   └── visual_contract.md  预计算 SHAP 复合图视觉合同
│   │   │       │   │   │       ├── stacked_bar/  目录入口
│   │   │       │   │   │       │   ├── data_contract.md  堆叠柱状图数据合同
│   │   │       │   │   │       │   ├── data_template.csv  资料与资源
│   │   │       │   │   │       │   ├── example_standard.csv  资料与资源
│   │   │       │   │   │       │   ├── manifest.yaml  自动化配置
│   │   │       │   │   │       │   ├── runner.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── schema.json  结构化配置与索引
│   │   │       │   │   │       │   ├── service.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   └── visual_contract.md  堆叠柱状图视觉合同
│   │   │       │   │   │       ├── trajectory3d/  目录入口
│   │   │       │   │   │       │   ├── data_contract.md  三维多条件 Nyquist 轨迹数据合同
│   │   │       │   │   │       │   ├── data_template.csv  资料与资源
│   │   │       │   │   │       │   ├── example_standard.csv  资料与资源
│   │   │       │   │   │       │   ├── manifest.yaml  自动化配置
│   │   │       │   │   │       │   ├── origin_acceptance.md  Origin 10.15 route acceptance
│   │   │       │   │   │       │   ├── runner.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── schema.json  结构化配置与索引
│   │   │       │   │   │       │   ├── service.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   └── visual_contract.md  三维多条件 Nyquist 轨迹视觉合同
│   │   │       │   │   │       ├── trend/  目录入口
│   │   │       │   │   │       │   ├── data_contract.md  趋势折线图数据合同
│   │   │       │   │   │       │   ├── data_template.csv  资料与资源
│   │   │       │   │   │       │   ├── example_standard.csv  资料与资源
│   │   │       │   │   │       │   ├── manifest.yaml  自动化配置
│   │   │       │   │   │       │   ├── runner.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── schema.json  结构化配置与索引
│   │   │       │   │   │       │   ├── service.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   └── visual_contract.md  趋势折线图视觉合同
│   │   │       │   │   │       ├── uv_vis/  目录入口
│   │   │       │   │   │       │   ├── data_contract.md  数据合同
│   │   │       │   │   │       │   ├── data_template.csv  资料与资源
│   │   │       │   │   │       │   ├── example_multi_spectrum.csv  资料与资源
│   │   │       │   │   │       │   ├── example_standard.csv  资料与资源
│   │   │       │   │   │       │   ├── manifest.yaml  自动化配置
│   │   │       │   │   │       │   ├── runner.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── schema.json  结构化配置与索引
│   │   │       │   │   │       │   ├── service.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   └── visual_contract.md  视觉合同
│   │   │       │   │   │       ├── violin/  目录入口
│   │   │       │   │   │       │   ├── data_contract.md  小提琴图数据合同
│   │   │       │   │   │       │   ├── data_template.csv  资料与资源
│   │   │       │   │   │       │   ├── example_standard.csv  资料与资源
│   │   │       │   │   │       │   ├── manifest.yaml  自动化配置
│   │   │       │   │   │       │   ├── runner.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── schema.json  结构化配置与索引
│   │   │       │   │   │       │   ├── service.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   └── visual_contract.md  小提琴图视觉合同
│   │   │       │   │   │       ├── xas/  目录入口
│   │   │       │   │   │       │   ├── data_contract.md  XAS 数据合同
│   │   │       │   │   │       │   ├── data_template.csv  资料与资源
│   │   │       │   │   │       │   ├── example_standard.csv  资料与资源
│   │   │       │   │   │       │   ├── manifest.yaml  自动化配置
│   │   │       │   │   │       │   ├── runner.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── schema.json  结构化配置与索引
│   │   │       │   │   │       │   ├── service.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   └── visual_contract.md  XAS 视觉合同
│   │   │       │   │   │       ├── xps/  目录入口
│   │   │       │   │   │       │   ├── data_template.csv  资料与资源
│   │   │       │   │   │       │   ├── manifest.yaml  自动化配置
│   │   │       │   │   │       │   ├── runner.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── schema.json  结构化配置与索引
│   │   │       │   │   │       │   └── service.py  跨平台维护或执行脚本
│   │   │       │   │   │       ├── xps_adaptive/  目录入口
│   │   │       │   │   │       │   ├── data_contract.md  XPS Adaptive Data Contract
│   │   │       │   │   │       │   ├── example_standard.csv  资料与资源
│   │   │       │   │   │       │   ├── manifest.yaml  自动化配置
│   │   │       │   │   │       │   ├── runner.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── schema.json  结构化配置与索引
│   │   │       │   │   │       │   └── visual_contract.md  XPS Adaptive Visual Contract
│   │   │       │   │   │       ├── xps_c1s_fit/  目录入口
│   │   │       │   │   │       │   ├── data_contract.md  XPS C 1s CSV 数据合同
│   │   │       │   │   │       │   ├── example_noisy.csv  资料与资源
│   │   │       │   │   │       │   ├── example_standard.csv  资料与资源
│   │   │       │   │   │       │   ├── manifest.yaml  自动化配置
│   │   │       │   │   │       │   ├── preview.png  图片素材
│   │   │       │   │   │       │   ├── runner.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── schema.json  结构化配置与索引
│   │   │       │   │   │       │   ├── tests/  目录入口
│   │   │       │   │   │       │   │   ├── invalid_duplicate_columns.csv  资料与资源
│   │   │       │   │   │       │   │   ├── invalid_empty_rows.csv  资料与资源
│   │   │       │   │   │       │   │   ├── invalid_missing_column.csv  资料与资源
│   │   │       │   │   │       │   │   ├── invalid_non_numeric.csv  资料与资源
│   │   │       │   │   │       │   │   ├── invalid_wrong_range.csv  资料与资源
│   │   │       │   │   │       │   │   ├── valid_xps_chinese_filename.csv  资料与资源
│   │   │       │   │   │       │   │   ├── valid_xps_dense_points.csv  资料与资源
│   │   │       │   │   │       │   │   ├── valid_xps_noisy.csv  资料与资源
│   │   │       │   │   │       │   │   └── valid_xps_standard.csv  资料与资源
│   │   │       │   │   │       │   └── visual_contract.md  XPS C 1s 视觉合同
│   │   │       │   │   │       ├── xps_compare/  目录入口
│   │   │       │   │   │       │   ├── data_contract.md  XPS 多谱线对比数据合同
│   │   │       │   │   │       │   ├── data_template.csv  资料与资源
│   │   │       │   │   │       │   ├── example_standard.csv  资料与资源
│   │   │       │   │   │       │   ├── manifest.yaml  自动化配置
│   │   │       │   │   │       │   ├── runner.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── schema.json  结构化配置与索引
│   │   │       │   │   │       │   ├── service.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   └── visual_contract.md  XPS 多谱线对比视觉合同
│   │   │       │   │   │       └── xrd/  目录入口
│   │   │       │   │   │           ├── data_contract.md  XRD 数据合同
│   │   │       │   │   │           ├── data_template.csv  资料与资源
│   │   │       │   │   │           ├── example_gsas_powder.csv  资料与资源
│   │   │       │   │   │           ├── example_gsas_publication.csv  资料与资源
│   │   │       │   │   │           ├── example_standard.csv  资料与资源
│   │   │       │   │   │           ├── manifest.yaml  自动化配置
│   │   │       │   │   │           ├── runner.py  跨平台维护或执行脚本
│   │   │       │   │   │           ├── schema.json  结构化配置与索引
│   │   │       │   │   │           ├── service.py  跨平台维护或执行脚本
│   │   │       │   │   │           └── visual_contract.md  XRD 视觉合同
│   │   │       │   │   ├── SECURITY.md  Security policy
│   │   │       │   │   ├── skill/  目录入口
│   │   │       │   │   │   └── editaplot/  目录入口
│   │   │       │   │   │       ├── agents/  目录入口
│   │   │       │   │   │       │   └── openai.yaml  自动化配置
│   │   │       │   │   │       ├── assets/  目录入口
│   │   │       │   │   │       │   └── palettes/  目录入口
│   │   │       │   │   │       │       ├── cards/  目录入口
│   │   │       │   │   │       │       │   ├── amber_lavender.png  图片素材
│   │   │       │   │   │       │       │   ├── blue_coral.png  图片素材
│   │   │       │   │   │       │       │   ├── deep_sea_gold.png  图片素材
│   │   │       │   │   │       │       │   ├── forest_amber.png  图片素材
│   │   │       │   │   │       │       │   ├── navy_cyan_gold.png  图片素材
│   │   │       │   │   │       │       │   ├── navy_ember.png  图片素材
│   │   │       │   │   │       │       │   ├── ocean_coral.png  图片素材
│   │   │       │   │   │       │       │   ├── plum_rose.png  图片素材
│   │   │       │   │   │       │       │   ├── sky_terra.png  图片素材
│   │   │       │   │   │       │       │   └── violet_lime.png  图片素材
│   │   │       │   │   │       │       ├── palette-catalog.json  结构化配置与索引
│   │   │       │   │   │       │       ├── palette-selector-all.zh-CN.png  图片素材
│   │   │       │   │   │       │       └── palette-selector-public.zh-CN.png  图片素材
│   │   │       │   │   │       ├── LICENSE  资料与资源
│   │   │       │   │   │       ├── NOTICE  资料与资源
│   │   │       │   │   │       ├── references/  目录入口
│   │   │       │   │   │       │   ├── chart-selection.md  Chart selection and support levels
│   │   │       │   │   │       │   ├── data-contracts.md  Data contracts
│   │   │       │   │   │       │   ├── figure-contract.md  Publication-informed Origin figure contract
│   │   │       │   │   │       │   ├── origin-safety.md  Origin Automation safety gate
│   │   │       │   │   │       │   ├── palettes.md  科研配色选择合同
│   │   │       │   │   │       │   ├── reference-figures.md  Reference-figure adaptation
│   │   │       │   │   │       │   ├── runtime.md  Runtime and launcher
│   │   │       │   │   │       │   ├── semantic-understanding.md  Scientific data understanding and element confirmation
│   │   │       │   │   │       │   ├── showcase.md  Showcase policy
│   │   │       │   │   │       │   └── verification.md  Origin delivery verification
│   │   │       │   │   │       ├── scripts/  目录入口
│   │   │       │   │   │       │   ├── bootstrap_editaplot.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── editaplot.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── editaplot_core.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   └── requirements-runtime.lock  资料与资源
│   │   │       │   │   │       └── SKILL.md  EditaPlot
│   │   │       │   │   ├── SUPPORT.md  Support scope
│   │   │       │   │   ├── tests/  目录入口
│   │   │       │   │   │   ├── test_axis_title_attachments.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_circular_network_layout.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_circular_network_preview_core.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_circular_network_workflow.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_density_ridgeline3d_renderer.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_density_ridgeline3d_showcase.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_density_ridgeline3d_template.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_density_ridgeline3d_workflow.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_editaplot.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_gsas_data_loader.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_gui_worker_launch_contract.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_heatmap_density.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_material_spectroscopy.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_network_renderer_plan.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_origin_2021_2026_compatibility_documentation.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_origin_capabilities.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_origin_compatibility_reports.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_origin_doctor.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_origin_execution_context.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_origin_geometry_compatibility.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_origin_job_queue.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_origin_safety_documentation.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_origin_session.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_origin_smoke.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_origin_smoke_cli.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_origin_startup_recovery.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_origin_version_risk_integration.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_origin_version_risks.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_performance_guidance.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_progress_protocol.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_public_release_gate.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_public_template_alignment.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_reference_adaptation.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_reference_figure.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_reference_style.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_reference_workflow_core.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_safe_errors.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_semantic_analysis.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_semantic_contract.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_semantic_contract_parsing.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_semantic_workflow_core.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_shap_summary_preview_renderer.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_shap_summary_semantics.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_shap_summary_workflow.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_star_trend.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_style_choice_documentation.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_sync_public_gallery.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_template_capabilities.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_worker_done_payload.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_xps_fixed_runner_style.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_xps_ignored_columns_runner.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_xps_preview_style.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_xps_visual_style_cli.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_xps_visual_style_contract.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_xrd_rietveld_renderer.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── test_xrd_rietveld_workflow.py  跨平台维护或执行脚本
│   │   │       │   │   │   └── test_xrd_semantics.py  跨平台维护或执行脚本
│   │   │       │   │   ├── THIRD_PARTY_NOTICES.md  Third-party runtime notices
│   │   │       │   │   └── tools/  目录入口
│   │   │       │   │       ├── build_asset_provenance.py  跨平台维护或执行脚本
│   │   │       │   │       ├── build_palette_assets.py  跨平台维护或执行脚本
│   │   │       │   │       ├── build_runtime_manifest.py  跨平台维护或执行脚本
│   │   │       │   │       ├── build_showcase.py  跨平台维护或执行脚本
│   │   │       │   │       ├── build_star_trend.py  跨平台维护或执行脚本
│   │   │       │   │       ├── generate_showcase_data.py  跨平台维护或执行脚本
│   │   │       │   │       ├── sync_public_gallery.py  跨平台维护或执行脚本
│   │   │       │   │       └── verify_public_release.py  跨平台维护或执行脚本
│   │   │       │   └── upstream.json  上游仓库、分支、commit 与许可
│   │   │       ├── jianwei-ai-community-remotion-video/  jianwei-ai-community-remotion-video
│   │   │       │   ├── README.md  建委 AI 社群 Remotion 视频 Skill 说明
│   │   │       │   ├── skill/  可直接安装的完整 Skill
│   │   │       │   │   ├── agents/  目录入口
│   │   │       │   │   │   └── openai.yaml  自动化配置
│   │   │       │   │   ├── references/  目录入口
│   │   │       │   │   │   ├── background-fidelity-contract.md  参考图背景保真契约
│   │   │       │   │   │   ├── deterministic-layout-contract.md  Deterministic layout contract
│   │   │       │   │   │   ├── director-console-contract.md  导演台稳定输出契约
│   │   │       │   │   │   ├── director-strategy.md  动效导演策略
│   │   │       │   │   │   ├── input-and-image-analysis.md  输入与图片分析
│   │   │       │   │   │   ├── internal-production-brief.schema.json  结构化配置与索引
│   │   │       │   │   │   ├── motion-blueprint.schema.json  结构化配置与索引
│   │   │       │   │   │   ├── motion-direction.md  动效导演规则
│   │   │       │   │   │   ├── output-contract.md  Motion Blueprint 输出契约
│   │   │       │   │   │   ├── parameterization-contract.md  参数化与 Studio 编辑契约
│   │   │       │   │   │   ├── prompt-expansion-contract.md  内部导演执行稿与二次加工契约
│   │   │       │   │   │   ├── quality-gates.md  质量门槛
│   │   │       │   │   │   ├── reference-fidelity-contract.md  参考图保真契约
│   │   │       │   │   │   ├── remotion-contract.md  Remotion 实施契约
│   │   │       │   │   │   ├── remotion-only-director-contract.md  Remotion-only director contract
│   │   │       │   │   │   ├── render-performance-contract.md  渲染性能与交付流程契约
│   │   │       │   │   │   └── visibility-and-clipping-contract.md  文字与关键元素完整可见契约
│   │   │       │   │   ├── scripts/  目录入口
│   │   │       │   │   │   ├── audit_reference_render_path.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── check_layout_stability.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── check_settle_continuity.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── check_visibility_report.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── compare_background_regions.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── compare_reference_frame.py  跨平台维护或执行脚本
│   │   │       │   │   │   ├── validate_blueprint.py  跨平台维护或执行脚本
│   │   │       │   │   │   └── validate_production_brief.py  跨平台维护或执行脚本
│   │   │       │   │   └── SKILL.md  建委 AI 社群视频制作 Skill
│   │   │       │   └── upstream.json  规范参考与维护策略
│   │   │       ├── jianwei-ai-learning-community-workbench/  jianwei-ai-learning-community-workbench
│   │   │       │   ├── README.md  通用身份适配型工作台设计 Skill 说明
│   │   │       │   ├── skill/  可直接安装的完整 Skill
│   │   │       │   │   ├── agents/  目录入口
│   │   │       │   │   │   └── openai.yaml  自动化配置
│   │   │       │   │   ├── references/  目录入口
│   │   │       │   │   │   ├── conversation-protocol.md  首轮提问协议
│   │   │       │   │   │   ├── design-system.md  视觉、交互与跨端系统
│   │   │       │   │   │   ├── quality-gate.md  交付前品控门
│   │   │       │   │   │   └── role-adaptation.md  身份适配与工作台骨架
│   │   │       │   │   └── SKILL.md  身份适配工作台设计 Skill
│   │   │       │   └── upstream.json  来源、版本与维护策略
│   │   │       ├── qingyun-ip-poster/  青云 IP Poster 海报视觉 Skill
│   │   │       │   ├── README.md  调用方式、适用范围、事实与许可边界
│   │   │       │   ├── skill/  上游完整快照，共 26 个文件；展开可核查内部层级
│   │   │       │   │   ├── .gitignore  资料与资源
│   │   │       │   │   ├── agents/  目录入口
│   │   │       │   │   │   └── openai.yaml  自动化配置
│   │   │       │   │   ├── assets/  目录入口
│   │   │       │   │   │   ├── case-studies/  目录入口
│   │   │       │   │   │   │   ├── wang-lei-after-account-grid.jpg  图片素材
│   │   │       │   │   │   │   └── wang-lei-before-account-grid.jpg  图片素材
│   │   │       │   │   │   └── style-references/  目录入口
│   │   │       │   │   │       ├── 01-black-neon-green.png  图片素材
│   │   │       │   │   │       ├── 02-ivory-editorial.png  图片素材
│   │   │       │   │   │       ├── 03-graphite-thought-leader.png  图片素材
│   │   │       │   │   │       ├── 04-high-contrast-closeup.png  图片素材
│   │   │       │   │   │       ├── 05-black-gold-authority.png  图片素材
│   │   │       │   │   │       ├── 06-cyber-xianxia-character-dossier-light.png  图片素材
│   │   │       │   │   │       ├── 07-keynote-manifesto-dark.png  图片素材
│   │   │       │   │   │       ├── 08-cyber-xianxia-worldview-keyart-dark.png  图片素材
│   │   │       │   │   │       ├── 09-guest-manifesto-orange-cap.png  图片素材
│   │   │       │   │   │       ├── 10-event-lineup-monumental.png  图片素材
│   │   │       │   │   │       ├── 11-guest-manifesto-orange-suit.png  图片素材
│   │   │       │   │   │       └── 12-guest-manifesto-purple.png  图片素材
│   │   │       │   │   ├── README.en.md  Qingyun IP Poster
│   │   │       │   │   ├── README.md  Qingyun IP Poster
│   │   │       │   │   ├── README.zh-CN.md  Qingyun IP Poster · 中文说明
│   │   │       │   │   ├── references/  目录入口
│   │   │       │   │   │   ├── design-system.md  Qingyun 海报设计系统
│   │   │       │   │   │   ├── failure-modes.md  常见失败模式与修复
│   │   │       │   │   │   ├── intake-guide.md  素材引导与模式选择
│   │   │       │   │   │   ├── prompt-compiler.md  图像层与排版层指令编译
│   │   │       │   │   │   ├── quality-checklist.md  海报交付质量检查
│   │   │       │   │   │   └── version-matrix.md  版本矩阵与系列差异控制
│   │   │       │   │   └── SKILL.md  Qingyun IP Poster · Visual System Edition
│   │   │       │   └── upstream.json  上游仓库、固定 commit、版本与更新规则
│   │   │       └── README.md  Skill 实体索引、来源与更新规则
│   │   ├── README.md  设计、开发、培训、自媒体和其他领域的知识入口
│   │   ├── self-media/  自媒体与个人IP经营
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
│   │   │   ├── README.md  内容传播与个人IP经营入口
│   │   │   ├── titles/  自媒体标题与选题
│   │   │   │   └── README.md  标题方法与素材入口
│   │   │   └── video-scripts/  自媒体口播与视频脚本
│   │   │       ├── README.md  口播与短视频脚本入口
│   │   │       └── script-patterns.md  脚本结构模式
│   │   └── training/  培训与教学
│   │       ├── attribution-and-updates.md  培训资料的归属与更新
│   │       ├── experience/  培训经验
│   │       │   ├── demo-driven-course-design.md  演示驱动课程设计
│   │       │   ├── jianwei-training-style.md  建委默认培训风格与课件形态
│   │       │   ├── README.md  经验索引
│   │       │   ├── sources.md  培训方法来源与课程身份
│   │       │   ├── teaching-and-course-design.md  备课、课件与课程设计
│   │       │   ├── technical-explanation/  技术解释方法
│   │       │   │   ├── problem-driven-technical-explanation.md  问题驱动的技术解释方法
│   │       │   │   └── README.md  方法索引
│   │       │   ├── tutorial-writing.md  学员教程写法
│   │       │   └── visual-and-oral-training-docs.md  飞书培训文档的可视化与口语化
│   │       ├── materials/  培训资料
│   │       │   ├── pending-attribution/  待确认归属的培训资料
│   │       │   │   ├── README.md  待确认归属的培训资料
│   │       │   │   ├── revisions/  待归属培训资料修订
│   │       │   │   │   ├── 2026-08-19-lesson-4-student-material-boundary.md  2026-08-19：第 4 课学员正文边界修订
│   │       │   │   │   ├── 2026-08-23-lesson-4-visualization-and-case-delivery.md  2026-08-23：第 4 课可视化与案例交付修订
│   │       │   │   │   ├── 2026-08-29-student-material-definitive-positioning.md  2026-08-29：学员资料中的确定性学习定位
│   │       │   │   │   ├── 2026-09-02-miaoda-advanced-course-scenario-driven-updates.md  秒哒进阶课：把版本更新改造成使用场景链路
│   │       │   │   │   ├── 2026-09-07-lesson-6-lecture-review-and-visualization-rules.md  第六课直播复盘：学员稿表达与可视化规则
│   │       │   │   │   └── README.md  待归属培训资料修订
│   │       │   │   └── technical-dictionary-scope.md  AI 时代技术词典的资料边界
│   │       │   └── README.md  资料入口，避免复制项目资料
│   │       ├── outlines/  培训大纲
│   │       │   └── README.md  大纲入口，当前无独立通用大纲
│   │       └── README.md  AI 培训总入口
│   ├── projects/  项目与案例：这件事具体怎样了
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
│   │   ├── archive/  已归档项目
│   │   │   ├── openclaw-agent/  OpenClaw AI Agent
│   │   │   │   └── README.md  OpenClaw Agent 历史档案
│   │   │   ├── README.md  归档项目索引
│   │   │   └── videoai/  VideoAI — AI 驱动的营销视频自动化平台
│   │   │       ├── cost-analysis.md  历史成本测算
│   │   │       ├── pricing-plan-association.md  历史协会定价方案
│   │   │       └── README.md  VideoAI 历史项目入口
│   │   ├── cases/  商单与实践案例
│   │   │   ├── 2026-05-enterprise-prompt-record.md  2026 年 5 月企业片提示词实战记录
│   │   │   ├── happy-shopping.md  快乐购物小超市
│   │   │   ├── minchao-football.md  大班健康活动：闽超小将
│   │   │   ├── README.md  商单与实践案例
│   │   │   └── vr-ai-interactive.md  VR + AI + 交互教育案例
│   │   ├── external-training/  外出培训
│   │   │   ├── lessons/  外出培训课程资料
│   │   │   │   ├── bug-repair/  别让 Bug 打败你：秒哒故障定位与修复实战
│   │   │   │   │   ├── README.md  别让 Bug 打败你：秒哒故障定位与修复实战
│   │   │   │   │   └── revisions/  Bug 修复课程修订
│   │   │   │   │       ├── 2026-09-09-lesson-6-bug-repair-evidence-chain.md  第六课优化修订：Bug 修复证据链与一案例多故障演示台
│   │   │   │   │       └── README.md  Bug 修复课程修订
│   │   │   │   └── README.md  外出培训课程资料
│   │   │   └── README.md  外出培训
│   │   ├── feishu-efficient-office/  五级目录：《飞书高效办公》
│   │   │   ├── all-docs.md  历史培训素材摘要，默认不读
│   │   │   ├── ch1-editor-feedback-lessons.md  第1章编辑反馈汇总（引以为鉴）
│   │   │   ├── ch2-editor-feedback-lessons.md  第2章 0822 细颗粒度编辑反馈与复查规则
│   │   │   ├── ch4-editor-feedback.md  历史旧第4章 编辑反馈汇总与修改方案
│   │   │   ├── ch4-v3-editor-feedback.md  历史旧第4章 v3 修订稿编辑反馈汇总
│   │   │   ├── ch4-v4-revision-log.md  历史旧第4章 v4 修订稿创建与执行记录
│   │   │   ├── ch5-editor-feedback.md  各章编辑反馈与共性规则
│   │   │   ├── feishu-base-form-experience.md  多维表格表单经验
│   │   │   ├── feishu-doc-style.md  飞书文档视觉规范
│   │   │   ├── history.md  已清洗的章节修订摘要
│   │   │   ├── interface-screenshot-guidelines.md  软件截图与图文一致规范
│   │   │   ├── legacy-ch4-map.md  旧第4章素材映射
│   │   │   ├── publication-acceptance-checklist.md  出版编辑与交稿验收
│   │   │   ├── README.md  项目当前口径、进度和文件索引
│   │   │   ├── writing-style-analysis.md  本书专用写作风格
│   │   │   └── writing-style-history.md  写作风格历史来源（不自动激活）
│   │   ├── paid-community-course/  五级目录：AI 超级个体陪跑社群
│   │   │   ├── competitive-references.md  外部会员社群案例与可迁移经验
│   │   │   ├── course-development.md  课程研发与内容选择
│   │   │   ├── course-materials-index.md  飞书课程资料索引
│   │   │   ├── curriculum-design.md  课程结构与直播节奏
│   │   │   ├── history.md  已清洗的关键演进摘要
│   │   │   ├── operations-playbook.md  招生、运营与转化执行
│   │   │   ├── positioning-and-vision.md  社群定位、愿景与表达边界
│   │   │   ├── README.md  当前产品与课程口径
│   │   │   └── revisions/  六级目录：课程关键修订
│   │   │       ├── 2026-08-30-community-positioning-and-super-individual-definition.md  社群总定位与超级个体定义修订
│   │   │       ├── 2026-08-30-lesson-5-purchase-language-and-decision-boundary.md  第 5 节购买语言与决策边界修订
│   │   │       ├── 2026-08-31-lesson-5-post-lecture-ai-era-purpose-and-parameter-explanation.md  第 5 节课后 AI 时代目的与参数解释修订
│   │   │       ├── 2026-09-01-training-rule-scope-and-delivery-boundary.md  AI 培训规则适用场景与课堂交付边界修订
│   │   │       ├── 2026-09-01-training-rule-single-source-and-technical-selection.md  AI 培训单一来源与技术内容筛选修订
│   │   │       └── README.md  修订索引与读取边界
│   │   ├── README.md  项目与案例总入口
│   │   └── yancut-ai/  五级目录：言剪 AI
│   │       ├── architecture-and-upstream.md  架构、上游与能力边界
│   │       ├── history.md  已清洗的关键演进摘要
│   │       ├── README.md  当前项目事实与调用规则
│   │       ├── revisions/  项目关键修订记录
│   │       │   ├── 2026-08-22-auto-video-editable-project-loop.md  自动剪辑可编辑工程闭环修订
│   │       │   ├── 2026-08-22-wasm-scene-effect-and-editor-localization.md  WASM 场景效果与编辑器本地化修订
│   │       │   ├── 2026-08-31-effects-remotion-commercial-loop.md  Remotion 特效商业化闭环修订
│   │       │   ├── 2026-08-31-recut-remotion-production-loop.md  Remotion 重剪生产闭环修订
│   │       │   ├── 2026-08-31-shotcut-professional-ai-workflow.md  Shotcut 专业 AI 剪辑工作流
│   │       │   ├── 2026-08-31-source-repo-professional-editing-queue.md  源码仓专业剪辑排期修订
│   │       │   ├── 2026-09-01-concat-template-slots-command-queue.md  Concat 模板槽位与命令队列修订
│   │       │   ├── 2026-09-02-admin-shared-backend.md  管理后台与共享后端闭环修订
│   │       │   ├── 2026-09-02-commercialization-closure.md  商业化闭环与上线边界修订
│   │       │   ├── 2026-09-03-glm53-manual-purchase.md  GLM 模型与手动购买流程修订
│   │       │   ├── 2026-09-03-local-demo-effects-stickers.md  本地演示特效与贴纸效果修订
│   │       │   └── 2026-09-04-ai-progress-remotion-hyperframes-keyframes.md  AI 执行进度可视化、Remotion 本地预检与手动关键帧修订
│   │       └── roadmap.md  开发路线与上线条件
│   └── README.md  领域知识与项目案例的分级入口
├── system/  AI协作与维护
│   ├── environment/  设备与执行环境
│   │   ├── computers/  按设备管理
│   │   │   ├── desktop-1/  台式电脑 1
│   │   │   │   ├── disk-cleanup-and-codex-storage.md  磁盘清理与 Codex 存储基线
│   │   │   │   ├── history.md  已清洗的关键修复摘要
│   │   │   │   ├── network-and-codex.md  网络、Clash 与 Codex 排障
│   │   │   │   └── README.md  当前设备事实与操作禁区
│   │   │   ├── README.md  设备索引
│   │   │   └── windows-junction-migration.md  Windows Junction 迁移经验
│   │   ├── image-generation.md  本机生图调用规则
│   │   └── README.md  环境入口与安全规则
│   ├── expression/  通用表达与体裁验收
│   │   ├── corrections.md  中文纠错与真实反馈提炼
│   │   ├── evaluation.md  表达与成品验收
│   │   ├── genres.md  按成品找表达规则
│   │   ├── oral.md  口语化论证与前后承接方法
│   │   ├── README.md  AI 表达总入口、默认激活与组合规则
│   │   ├── sources.md  来源与适用边界
│   │   └── written.md  书稿、教程、方案和文档表达规则
│   ├── README.md  AI协作与维护
│   └── repository/  读取写入、导航与校验
│       ├── capability-evidence.md  从实践归纳个人能力
│       ├── collaboration-rules.md  协作规则与职责边界
│       ├── information-architecture.md  AI Context信息架构与长期规划
│       ├── ingestion-workflow.md  新内容写入与更新流程
│       ├── maintenance/  维护工具
│       │   ├── .gitignore  资料与资源
│       │   ├── context-route.py  跨平台维护或执行脚本
│       │   ├── context_common.py  跨平台维护或执行脚本
│       │   ├── desktop-sync.py  跨平台维护或执行脚本
│       │   ├── generate-structure-html.ps1  从 Markdown 生成交互式 HTML
│       │   ├── git-hooks/  本机自动同步触发器
│       │   │   ├── post-checkout  检出或切换后自愈桌面结构
│       │   │   ├── post-commit  提交后同步桌面结构
│       │   │   ├── post-merge  拉取或合并后同步桌面结构
│       │   │   ├── post-rewrite  amend 或 rebase 后同步桌面结构
│       │   │   ├── pre-commit  提交前校验暂存快照，不生成或暂存额外文件
│       │   │   └── run-python  资料与资源
│       │   ├── invoke-python.ps1  Windows 兼容入口
│       │   ├── pre-commit.py  跨平台维护或执行脚本
│       │   ├── README.md  校验与桌面同步说明
│       │   ├── structure-descriptions.json  结构化配置与索引
│       │   ├── structure-viewer.template.html  HTML 思维导图界面与交互模板
│       │   ├── sync-desktop-structure.ps1  生成并同步 HTML 到 F 盘桌面
│       │   ├── sync-navigation.py  跨平台维护或执行脚本
│       │   ├── sync-structure.py  跨平台维护或执行脚本
│       │   ├── tests/  维护回归测试
│       │   │   ├── README.md  维护回归测试
│       │   │   └── test_context.py  跨平台维护或执行脚本
│       │   ├── validate-context.ps1  结构、索引与链接校验脚本
│       │   ├── validate-context.py  跨平台维护或执行脚本
│       │   └── validation-policy.json  结构化配置与索引
│       ├── navigation/  任务路由与项目登记
│       │   ├── history.md  历史入口和读取边界
│       │   ├── projects.json  结构化配置与索引
│       │   ├── README.md  任务路由与项目登记
│       │   ├── routes.json  结构化配置与索引
│       │   ├── STRUCTURE.html  日常知识导航与完整文件视图
│       │   ├── STRUCTURE.md  完整物理文件树与结构约定
│       │   └── task-guide.md  完整任务指南，按主任务和条件依赖读取
│       ├── README.md  治理总入口
│       ├── revisions/  仓库级重大修订
│       │   ├── 2026-04-05-context-repository-established.md  2026-04-05：建立长期AI协作上下文仓库
│       │   ├── 2026-08-18-information-architecture-rebuild.md  五个一级入口的信息架构重构记录
│       │   ├── 2026-08-20-ai-expression-default-layer.md  AI 表达默认层和语言规则修订
│       │   ├── 2026-08-21-chinese-quality-and-source-governance.md  中文质量基础层与多来源冲突治理修订
│       │   ├── 2026-08-21-commercial-delivery-domain.md  商业化与对外交付边界层首次建立记录
│       │   ├── 2026-08-21-commercial-delivery-relocation.md  商业化迁移到其他领域的修订
│       │   ├── 2026-08-21-desktop-sync-resilience.md  桌面 HTML 同步稳定性加固
│       │   ├── 2026-08-21-direct-main-and-desktop-sync.md  直推 main、旧分支清理与桌面同步修订
│       │   ├── 2026-08-21-interactive-html-structure-viewer.md  交互式 HTML 结构查看与自动同步修订
│       │   ├── 2026-08-22-cognition-and-content-commercialization.md  建委认知归组与跨行业内容经营修订
│       │   ├── 2026-08-23-feishu-document-routing-boundary.md  飞书文档承载平台与飞书书籍项目的路由边界
│       │   ├── 2026-08-24-sixty-jiazi-project-relocation.md  六十甲子项目迁入 other 与唯一路由规则
│       │   ├── 2026-08-27-commercial-external-material-boundary.md  赛事、路演与融资材料的对外边界修订
│       │   ├── 2026-09-01-ai-programming-skill-repository.md  AI 编程 Skill 仓库与上游快照治理
│       │   ├── 2026-09-01-case-result-narrative.md  案例结果叙事方法入库修订
│       │   ├── 2026-09-01-remotion-skill-confirmation-and-action-contract.md  Remotion Skill 确认门与逐元素动作契约修订
│       │   ├── 2026-09-01-remotion-skill-director-and-parameterization.md  2026-09-01 Remotion Skill 导演层与参数化默认输出修订
│       │   ├── 2026-09-02-jianwei-remotion-parameterization.md  Studio 右侧 Default Props 可编辑性验收修订 Remotion Skill 导演层、重叠节奏与参数化默认输出修订
│       │   ├── 2026-09-04-remotion-reference-fidelity-and-preview-gate.md  Remotion Skill 参考图保真、低清预览与最终渲染确认门修订
│       │   ├── 2026-09-05-remotion-deterministic-layout.md  Remotion Skill 修订：数字与高密度布局确定性
│       │   ├── 2026-09-05-remotion-director-expansion-and-background-fidelity.md  Remotion Skill 内部导演加工、动作自然度与背景保真修订
│       │   ├── 2026-09-05-remotion-layout-locked-continuity.md  Remotion 参考图几何锁定与连续性审计
│       │   ├── 2026-09-05-remotion-text-stability-and-director-console.md  Remotion Skill 文字抗抖、字体锁定、布局稳定校验与导演台固定输出修订
│       │   ├── 2026-09-05-remotion-text-visibility-and-clipping.md  Remotion Skill 文字与关键元素完整可见、裁剪祖先和最长参数压力测试修订
│       │   ├── 2026-09-05-remotion-universal-adaptive-architecture.md  Remotion Skill 几何锁定、禁止片尾整图覆盖与连续性审计修订
│       │   ├── 2026-09-07-structure-sync-and-content-routing.md  结构镜像同步与表达/自媒体分流修订
│       │   ├── 2026-09-07-training-review-generalization-and-reinforcement.md  AI 培训复盘通用化与重复错误强化机制
│       │   ├── 2026-09-12-context-operation-and-attribution.md  2026-09-12：上下文运行规则与资料归属纠正
│       │   ├── 2026-09-12-hierarchical-navigation-and-expression.md  2026-09-12：分级导航、项目集中与表达标准调整
│       │   ├── 2026-09-12-personal-expression-and-skill-refinement.md  个人信息、表达与Skill归属调整
│       │   └── README.md  仓库修订索引
│       ├── roadmap.md  长期维护与演进
│       ├── templates/  项目、案例与方法模板
│       │   ├── case.md  实战案例模板
│       │   ├── method.md  方法卡模板
│       │   ├── project.md  项目入口模板
│       │   └── README.md  项目、案例与方法模板
│       └── versioned-knowledge-policy.md  动态产品知识与版本治理
├── .gitattributes  Git 文本属性与换行规范
├── .github/  GitHub 自动校验
│   ├── README.md  GitHub 自动校验
│   └── workflows/  目录入口
│       └── context-validation.yml  自动化配置
└── .gitignore  Git 忽略规则，排除不应入库的本地文件
```

## 四个主入口

- personal：我是谁、个人经历与阶段里程碑、背书荣誉和成果、业务与项目概要；能力归纳并入概要，表达样稿留原领域／项目。
- brain：个人认知与判断，只有有依据的观点进入，不包含通用AI表达。
- work：domains保存工作方法，projects保存具体项目、商单和归档；AI作为方法、工具或主题。
- system：共用表达、仓库运行和设备环境。治理、校验与维护归为一条分支；Skill在work/domains/other/skills。

根README提供日常首页，AGENTS保留AI启动入口，llms是兼容短指针。GitHub要求的.github/workflows以及Git配置保留其技术位置，日常知识树不把它们当业务门类。

## 工作知识怎样归类

先判断交付物，再确定项目身份与方法依赖。平面、视频、教育作品等在设计中逐层选择；AI、AE、MG不能作为与设计平行的项目归属。自媒体不限AI主题；出版书属于具体项目。

方法按最适用的领域保存；项目与案例在work/projects只存一份，通过项目登记自动生成领域关联入口。一个项目可关联多个领域，状态只在项目权威记录维护，不能由示例、模板或旧目录推断。

## 索引与增量维护

每个独立激活的领域、工具或项目有README。最近README索引新增文件，上层只列下一层；不预建空门类或同一方法的多个副本。新增资料执行[写入流程](../ingestion-workflow.md)，判定来源、归属、适用范围与证据，再同步登记、引用、结构和验收。

重大变化写就近revisions，history只保留摘要与链接；普通变动交给Git历史。保留价值明确的旧项目进入work/projects/archive。用户明确彻底清除时同时去除当前树和历史引用，不另建归档。

动态外部能力按[版本政策](../versioned-knowledge-policy.md)核验。Skill来源、许可和版本独立记录；保留实体不证明本机安装或执行。原始长资料和源码只在核验或执行时读。

## 生成与发布

按[维护步骤](../maintenance/README.md)同步任务导航、关联资产、完整树与交互HTML，再校验和暂存。pre-commit验证暂存快照，不静默生成或暂存额外文件。桌面HTML从同一生成版本同步，Windows桌面暂不可用单独报告。

完整设计理由与后续扩展见[信息架构](../information-architecture.md)。命名使用kebab-case，固定工具文件名除外；文本UTF-8与LF，使用相对链接，凭据不入库。

*结构最后确认：2026-09-12*
