# 仓库完整结构与写入规范

> 本文件是仓库目录结构的权威说明。下面按“一级目录 → 二级目录 → 三级目录 → 具体文件”连续展开，并用中文说明每一项用途。

## 一、完整目录树

```text
ai-context/
├── README.md                                      仓库总入口与五个一级目录说明
├── AGENTS.md                                      AI 协作、读取、写入和提交规则
├── llms.txt                                       AI 最小读取与单领域激活路由
├── STRUCTURE.md                                   完整目录树与结构规范（本文件）
│
├── personal/                                      一级目录：个人信息概要
│   ├── README.md                                  个人信息总窗口、索引、写入准则
│   ├── profile.md                                 我是谁：身份、教育和职业基本信息
│   ├── business-overview.md                       业务与项目概要，只做导航不写细节
│   ├── credentials.md                             个人背书：荣誉、成果、聘书和代表经历
│   ├── growth-path.md                             成长路径与阶段变化
│   └── capabilities.md                            能力结构与擅长方向
│
├── brain/                                         一级目录：建委大脑
│   ├── README.md                                  建委大脑入口、边界与激活条件
│   ├── thinking-and-decisions.md                  思维认知、判断习惯与决策方式
│   ├── personal-expression.md                     建委本人的口语、表达逻辑和语言习惯
│   └── business-cognition.md                      建委长期形成的商业与增长认知
│
├── work/                                          一级目录：工作领域与项目
│   ├── README.md                                  工作总入口：设计、AI、其他
│   │
│   ├── design/                                    二级目录：设计领域
│   │   ├── README.md                              设计领域总索引与归类边界
│   │   ├── ppt-design/
│   │   │   └── README.md                          PPT 设计经验与项目入口
│   │   ├── poster-fold-design/
│   │   │   └── README.md                          海报、折页及平面物料设计入口
│   │   ├── book-design/
│   │   │   └── README.md                          书籍装帧与版式设计入口
│   │   ├── microcourse-mg-animation/
│   │   │   └── README.md                          微课、精品课、MG 动画与教育课件
│   │   ├── ae-promo-video/
│   │   │   └── README.md                          AE 宣传视频设计入口
│   │   └── ai-design/
│   │       └── README.md                          AI 辅助视觉设计，归属仍是设计
│   │
│   ├── ai/                                        二级目录：AI 领域
│   │   ├── README.md                              AI 领域总索引
│   │   │
│   │   ├── programming/                           三级目录：AI 编程
│   │   │   ├── README.md                          AI 编程总入口
│   │   │   ├── tools/                             四级目录：编程工具
│   │   │   │   ├── README.md                      工具索引
│   │   │   │   └── miaoda/                        五级目录：百度秒哒
│   │   │   │       ├── README.md                  秒哒总入口与读取边界
│   │   │   │       ├── llms.txt                   秒哒最小读取路由
│   │   │   │       ├── disambiguation.md          百度秒哒与飞书妙搭的同名辨析
│   │   │   │       ├── basics/                    六级目录：基础与发布
│   │   │   │       │   ├── README.md              基础资料索引
│   │   │   │       │   ├── platform-basics.md     平台基础能力
│   │   │   │       │   └── publish-channels.md    发布渠道与限制
│   │   │   │       ├── development/               六级目录：开发能力
│   │   │   │       │   ├── README.md              开发资料索引
│   │   │   │       │   ├── skill-development.md   秒哒 Skill 开发
│   │   │   │       │   └── skill-as-callable.md   秒哒作为可调用 Skill
│   │   │   │       ├── experience/                六级目录：实战经验
│   │   │   │       │   ├── README.md              经验索引
│   │   │   │       │   ├── pitfalls.md            常见坑与规避方式
│   │   │   │       │   ├── prompt-patterns.md     提示词模式
│   │   │   │       │   ├── cases/                 七级目录：案例
│   │   │   │       │   │   ├── README.md          案例索引
│   │   │   │       │   │   └── yungouos-jsapi.md  云购 OS JSAPI 案例
│   │   │   │       │   ├── patterns/              七级目录：可复用工作模式
│   │   │   │       │   │   ├── README.md          模式索引
│   │   │   │       │   │   ├── codex-assisted-workflow.md
│   │   │   │       │   │   │                     Codex 协助秒哒开发流程
│   │   │   │       │   │   ├── codex-source-package-deployment.md
│   │   │   │       │   │   │                     源码分包与秒哒交付
│   │   │   │       │   │   ├── content-rectification-prompts.md
│   │   │   │       │   │   │                     内容整改提示词
│   │   │   │       │   │   ├── large-video-upload.md
│   │   │   │       │   │   │                     大视频上传方案
│   │   │   │       │   │   ├── seo-optimization.md
│   │   │   │       │   │   │                     SEO 优化经验
│   │   │   │       │   │   └── wechat-urlsec-verification.md
│   │   │   │       │   │                         微信 URL 安全验证
│   │   │   │       │   └── reference-materials/  七级目录：原始参考资料
│   │   │   │       │       ├── README.md          参考资料索引
│   │   │   │       │       └── video-chunked-upload/
│   │   │   │       │           ├── README.md      视频分片上传源码说明
│   │   │   │       │           ├── video-serve.ts
│   │   │   │       │           ├── video-upload-chunk.ts
│   │   │   │       │           └── video-upload-complete.ts
│   │   │   │       └── updates/                   六级目录：版本与升级
│   │   │   │           ├── README.md              版本资料索引
│   │   │   │           ├── version-features.md    历史版本能力时间线
│   │   │   │           ├── 2026-08-02-version-governance.md
│   │   │   │           │                         版本知识治理记录
│   │   │   │           └── 2026-08-15-cloud-runtime-diagnostics.md
│   │   │   │                                     云端运行诊断记录
│   │   │   ├── experience/                        四级目录：通用编程经验
│   │   │   │   ├── README.md                      经验索引
│   │   │   │   ├── creative-frontend-prompt-patterns.md
│   │   │   │   │                                 创意前端提示词方法
│   │   │   │   └── reference-materials/           五级目录：编程参考资料
│   │   │   │       ├── README.md                  参考资料索引
│   │   │   │       └── creative-frontend-prompts/
│   │   │   │           ├── README.md              创意前端原始提示词索引
│   │   │   │           └── raw/                   六级目录：未经提炼的原文
│   │   │   │               ├── dark-editorial-portfolio.txt
│   │   │   │               ├── jack-3d-creator-portfolio.txt
│   │   │   │               ├── prmpt-fashion-archive.txt
│   │   │   │               ├── sentinel-spline-3d-hero.txt
│   │   │   │               └── synapsex-video-scrub.txt
│   │   │   └── projects/                          四级目录：AI 编程项目
│   │   │       ├── README.md                      项目索引与源码仓库入口
│   │   │       └── yancut-ai/                     五级目录：言剪 AI
│   │   │           ├── README.md                  当前项目事实与调用规则
│   │   │           ├── architecture-and-upstream.md
│   │   │           │                             架构、上游与能力边界
│   │   │           ├── roadmap.md                 开发路线与上线条件
│   │   │           └── history.md                 已清洗的关键演进摘要
│   │   │
│   │   ├── training/                              三级目录：AI 培训
│   │   │   ├── README.md                          AI 培训总入口
│   │   │   ├── experience/                        四级目录：培训经验
│   │   │   │   ├── README.md                      经验索引
│   │   │   │   ├── teaching-and-course-design.md 备课、课件与课程设计
│   │   │   │   ├── demo-driven-course-design.md  演示驱动课程设计
│   │   │   │   ├── tutorial-writing.md            学员教程写法
│   │   │   │   └── technical-explanation/         五级目录：技术解释方法
│   │   │   │       ├── README.md                  方法索引
│   │   │   │       ├── problem-driven-technical-explanation.md
│   │   │   │       │                             问题驱动的技术解释方法
│   │   │   │       └── source-materials/          六级目录：来源材料
│   │   │   │           ├── README.md              来源材料索引
│   │   │   │           └── feitian-shanke/
│   │   │   │               ├── README.md          飞天闪客材料用途与边界
│   │   │   │               └── raw/
│   │   │   │                   └── feitian-shanke-transcript.txt
│   │   │   ├── outlines/                          四级目录：培训大纲
│   │   │   │   └── README.md                      大纲入口，当前无独立通用大纲
│   │   │   ├── materials/                         四级目录：培训资料
│   │   │   │   └── README.md                      资料入口，避免复制项目资料
│   │   │   └── projects/                          四级目录：培训项目
│   │   │       ├── README.md                      培训项目索引
│   │   │       └── paid-community-course/         五级目录：AI 超级个体陪跑社群
│   │   │           ├── README.md                  当前产品与课程口径
│   │   │           ├── course-development.md      课程研发与内容选择
│   │   │           ├── curriculum-design.md       课程结构与直播节奏
│   │   │           ├── course-materials-index.md  飞书课程资料索引
│   │   │           ├── operations-playbook.md     招生、运营与转化执行
│   │   │           └── history.md                 已清洗的关键演进摘要
│   │   │
│   │   ├── video/                                 三级目录：AI 视频
│   │   │   ├── README.md                          AI 视频总入口
│   │   │   ├── common/
│   │   │   │   └── README.md                      跨片型通用制作经验
│   │   │   ├── types/                             四级目录：视频类型
│   │   │   │   ├── README.md                      类型索引
│   │   │   │   ├── motion-comic/
│   │   │   │   │   └── README.md                  漫剧制作入口
│   │   │   │   ├── enterprise-promo/
│   │   │   │   │   └── README.md                  企业宣传片制作经验
│   │   │   │   └── live-action-story/
│   │   │   │       └── README.md                  真人实拍故事与电影叙事
│   │   │   ├── tools/                             四级目录：AI 视频工具
│   │   │   │   ├── README.md                      工具索引
│   │   │   │   └── seedance/
│   │   │   │       ├── README.md                  Seedance 工具入口
│   │   │   │       ├── practical-workflow.md      实战工作流
│   │   │   │       ├── prompt-templates.md        提示词模板
│   │   │   │       └── prompt-cases.md            提示词案例
│   │   │   └── projects/
│   │   │       └── README.md                      AI 视频项目索引
│   │   │
│   │   ├── publishing/                            三级目录：AI 书籍出版
│   │   │   ├── README.md                          出版领域总入口
│   │   │   └── projects/
│   │   │       ├── README.md                      出版项目索引
│   │   │       └── feishu-efficient-office/       五级目录：《飞书高效办公》
│   │   │           ├── README.md                  项目当前口径、进度和文件索引
│   │   │           ├── writing-style-analysis.md  本书专用写作风格
│   │   │           ├── feishu-doc-style.md        飞书文档视觉规范
│   │   │           ├── feishu-base-form-experience.md
│   │   │           │                             多维表格表单经验
│   │   │           ├── interface-screenshot-guidelines.md
│   │   │           │                             软件截图与图文一致规范
│   │   │           ├── ch1-editor-feedback-lessons.md
│   │   │           ├── ch4-editor-feedback.md
│   │   │           ├── ch4-v3-editor-feedback.md
│   │   │           ├── ch4-v4-revision-log.md
│   │   │           ├── ch5-editor-feedback.md     各章编辑反馈与共性规则
│   │   │           ├── all-docs.md                历史培训素材摘要，默认不读
│   │   │           └── history.md                 已清洗的章节修订摘要
│   │   │
│   │   └── self-media/                            三级目录：AI 自媒体
│   │       ├── README.md                          自媒体总入口与严格边界
│   │       ├── titles/
│   │       │   └── README.md                      标题方法与素材入口
│   │       ├── articles/
│   │       │   └── README.md                      文章内容方法与素材入口
│   │       ├── video-scripts/
│   │       │   ├── README.md                      口播与短视频脚本入口
│   │       │   └── script-patterns.md             脚本结构模式
│   │       ├── live-sales/
│   │       │   ├── README.md                      直播销售与转化入口
│   │       │   └── conversion-path.md             内容到评论、资料和社群的承接
│   │       └── experience/
│   │           ├── README.md                      自媒体经验索引
│   │           └── media-growth.md                账号增长与内容规划
│   │
│   └── other/                                     二级目录：其他领域
│       ├── README.md                              其他项目索引与准入条件
│       └── inshan-popupiano/                      三级目录：海外电商项目
│           ├── README.md                          当前合作模式、事实和待澄清项
│           ├── 90-day-cold-start-plan.md          90 天冷启动执行方案
│           ├── competitive-references.md          竞品与可复刻案例
│           ├── history.md                         已清洗的方向变化摘要
│           └── Inshan海外电商冷启动方案_POPUPIANO智能钢琴键盘.docx
│                                                 修订前原始文档，默认不读
│
├── repository/                                    一级目录：仓库治理
│   ├── README.md                                  治理总入口
│   ├── versioned-knowledge-policy.md              动态产品知识与版本治理
│   ├── environment/                               二级目录：电脑与运行环境
│   │   ├── README.md                              环境入口与安全规则
│   │   └── computers/                             三级目录：按设备管理
│   │       ├── README.md                          设备索引
│   │       ├── windows-junction-migration.md      Windows Junction 迁移经验
│   │       └── desktop-1/                         四级目录：台式电脑 1
│   │           ├── README.md                      当前设备事实与操作禁区
│   │           ├── network-and-codex.md           网络、Clash 与 Codex 排障
│   │           └── history.md                     已清洗的关键修复摘要
│   ├── maintenance/                               二级目录：维护工具
│   │   ├── README.md                              校验工具说明
│   │   └── validate-context.ps1                   结构、索引与链接校验脚本
│   └── revisions/                                 二级目录：仓库级重大修订
│       ├── README.md                              仓库修订索引
│       └── 2026-08-18-information-architecture-rebuild.md
│                                                 本次信息架构重构记录
│
└── history/                                       一级目录：历史与追溯
    ├── README.md                                  历史入口和读取边界
    ├── timeline.md                                跨领域成长与里程碑时间线
    └── archived-projects/                         二级目录：已归档项目
        ├── README.md                              归档项目索引
        ├── openclaw-agent/
        │   └── README.md                          OpenClaw Agent 历史档案
        ├── videoai/
        │   ├── README.md                          VideoAI 历史项目入口
        │   ├── cost-analysis.md                   历史成本测算
        │   └── pricing-plan-association.md        历史协会定价方案
        └── xinghuo-ying-guozhou-vr-courseware/
            ├── README.md                          星火映果州 VR 课件历史入口
            └── interaction-logic.md               Nibiru 场景交互逻辑
```

## 二、归类判断顺序

新增资料前依次判断：

1. 是建委本人的概要事实吗？是则进入 `personal/`。
2. 是建委本人跨场景稳定的思考或个人表达吗？是则进入 `brain/`。
3. 是某个工作领域的经验、工具或项目吗？是则进入 `work/` 对应最具体分支。
4. 是仓库维护、设备或运行环境吗？是则进入 `repository/`。
5. 只剩历史追溯价值、已经退出主线吗？是则进入 `history/`。

无法明确归类时不新建“杂项”目录，先确认长期用途。

## 三、工作目录的固定层级

```text
work/<大领域>/<具体门类>/<经验|工具|项目>/<具体主题>/
```

- 大领域目前只有 `design`、`ai`、`other`。
- 工具不是项目，例如百度秒哒位于 `programming/tools/`。
- 项目不是通用经验，例如言剪 AI 位于 `programming/projects/`。
- 使用 AI 不自动改变业务归属：AI 设计仍在设计，AI 视频微课仍以微课交付归入设计。

## 四、README 与文件索引

- 每个需要独立激活的领域、工具和项目必须有 `README.md`。
- README 说明定位、边界、当前事实、文件索引、激活条件和写入方式。
- 新增文件时必须更新最近一层 README；上层 README 只索引下一层，不重复罗列所有叶子文件。
- 用户要求展示完整仓库时，按本文件这种连续树状层级展示，并附中文说明；禁止按文件类型或搜索结果分散罗列。

## 五、清洗与历史

- 当前 README 只保留当前有效口径，不堆叠相互冲突的旧结论。
- 重大变化写入项目 `history.md`，只保留日期、原因、新旧差异和当前结论。
- 普通编辑、格式修改和过程日志只保留在 Git 提交历史中。
- 原始材料放在 `source-materials/`、`reference-materials/` 或 `raw/`，必须有上层 README 说明用途，默认不激活。
- 已退出主线的完整项目进入 `history/archived-projects/`，只有明确追溯时读取。

## 六、命名、安全与提交

- 目录和普通文件采用小写 kebab-case；固定入口保留 `README.md`、`AGENTS.md`、`STRUCTURE.md`、`llms.txt`。
- Markdown 使用 UTF-8、LF 和相对链接。
- 不保存密码、API Key、Token、Cookie、完整认证文件或可直接利用的隐私信息。
- 结构调整后运行 `repository/maintenance/validate-context.ps1`，确认索引和相对链接有效。

*结构最后确认：2026-08-18*
