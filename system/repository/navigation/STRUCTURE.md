# 仓库结构与归类规范

日常从[分级知识导航](./STRUCTURE.html)逐层查看；其中“完整文件”视图保留全部技术文件及第三方快照内部层级。README是目录入口，不在日常树重复为平级业务节点；Skill实体只在完整文件视图展开。下方完整文件树自动生成。

两种视图来自同一套真实文件。日常导航保留知识目录父子关系、使用中文标题并隐藏技术细节，是建委默认浏览入口；完整文件视图更接近GitHub实际文件列表，收在页面的“维护查看”中，供检查配置与源码，不是另一套知识分类。

## 完整文件树

```text
ai-context/
├── README.md  建委日常使用的四个主入口
├── AGENTS.md  AI启动与必要读取规则
├── llms.txt  兼容调用的极短指针，完整任务指南位于系统导航
├── personal/  个人信息与事实
│   ├── business-overview.md  快速了解业务方向及有实践证据的能力概要
│   ├── credentials.md  查找已确认的获奖、荣誉及成果依据
│   ├── profile.md  了解建委的身份、背景和长期工作方向
│   ├── README.md  个人信息总窗口、索引、写入准则
│   └── timeline.md  按时间查看成长经历与重要阶段变化
├── brain/  建委的认知与判断
│   ├── business-cognition.md  商业、增长、内容经营与经营判断
│   ├── README.md  认知入口、读取路由与写入边界
│   └── thinking-and-decisions.md  思维、判断、框架拆解、学习与决策方式
├── work/  领域知识、项目事实与实践案例
│   ├── domains/  领域知识：这类工作怎样做
│   │   ├── design/  按交付物组织设计制作经验
│   │   │   ├── common/  组合手工设计与AI辅助，统一制作和沉淀流程
│   │   │   │   ├── ai-assisted-design.md  AI辅助视觉生产方法
│   │   │   │   ├── production-workflow.md  从需求到交付组织设计工作，并把经验接回知识库
│   │   │   │   └── README.md  设计共用方法
│   │   │   ├── graphic/  按PPT、海报折页和书籍版式查设计经验
│   │   │   │   ├── book/  查找书籍封面、装帧与内页版式的方法
│   │   │   │   │   └── README.md  书籍装帧与版式设计入口
│   │   │   │   ├── poster-fold/  制作海报、折页等平面宣传物料的经验入口
│   │   │   │   │   └── README.md  海报、折页及平面物料设计入口
│   │   │   │   ├── ppt/  制作演示文稿时查内容组织与视觉设计要求
│   │   │   │   │   └── README.md  PPT 设计经验与项目入口
│   │   │   │   └── README.md  平面与演示
│   │   │   ├── README.md  设计制作入口，项目与案例来自统一登记
│   │   │   └── video/  按宣传、教育、故事片型组合制作方法
│   │   │       ├── common/  跨片型复用分镜、AI生成、合成与验收方法
│   │   │       │   ├── ae-production.md  AE包装、合成与工程交付要求
│   │   │       │   ├── awesome-seedance/  AI视频提示词、模板与第三方案例
│   │   │       │   │   ├── lookup.py  只读提取模板、案例原文和复测状态
│   │   │       │   │   ├── README.md  能力边界、主动调用、来源与后续沉淀
│   │   │       │   │   ├── source/  上游完整快照，共 153 个文件；展开可核查内部层级
│   │   │       │   │   │   ├── .claude-plugin/  目录入口
│   │   │       │   │   │   │   └── marketplace.json  结构化配置与索引
│   │   │       │   │   │   ├── .github/  目录入口
│   │   │       │   │   │   │   ├── CODEOWNERS  资料与资源
│   │   │       │   │   │   │   ├── pull_request_template.md  说明与资料
│   │   │       │   │   │   │   └── workflows/  目录入口
│   │   │       │   │   │   │       ├── refresh-site-stats.yml  自动化配置
│   │   │       │   │   │   │       ├── update-readme.yml  自动化配置
│   │   │       │   │   │   │       └── validate-submissions.yml  自动化配置
│   │   │       │   │   │   ├── .gitignore  资料与资源
│   │   │       │   │   │   ├── agents/  目录入口
│   │   │       │   │   │   │   └── skills/  目录入口
│   │   │       │   │   │   │       ├── seedance-3d-cartoon/  目录入口
│   │   │       │   │   │   │       │   ├── references/  目录入口
│   │   │       │   │   │   │       │   │   └── cases.md  说明文档：Case evidence · 3D cartoon character short
│   │   │       │   │   │   │       │   └── SKILL.md  3D cartoon character short · 3D 卡通角色短片
│   │   │       │   │   │   │       ├── seedance-car-vehicle/  目录入口
│   │   │       │   │   │   │       │   ├── references/  目录入口
│   │   │       │   │   │   │       │   │   └── cases.md  说明文档：Case evidence · Cars and vehicles at speed
│   │   │       │   │   │   │       │   └── SKILL.md  Cars and vehicles at speed · 汽车与载具速度片
│   │   │       │   │   │   │       ├── seedance-epic-fantasy-scifi/  目录入口
│   │   │       │   │   │   │       │   ├── references/  目录入口
│   │   │       │   │   │   │       │   │   └── cases.md  说明文档：Case evidence · Epic fantasy and sci-fi spectacle
│   │   │       │   │   │   │       │   └── SKILL.md  Epic fantasy and sci-fi spectacle · 奇幻科幻大场面
│   │   │       │   │   │   │       ├── seedance-fashion-lookbook/  目录入口
│   │   │       │   │   │   │       │   ├── references/  目录入口
│   │   │       │   │   │   │       │   │   └── cases.md  说明文档：Case evidence · Fashion lookbook and portrait film
│   │   │       │   │   │   │       │   └── SKILL.md  Fashion lookbook and portrait film · 时尚 lookbook 与人像写真片
│   │   │       │   │   │   │       ├── seedance-horror-suspense/  目录入口
│   │   │       │   │   │   │       │   ├── references/  目录入口
│   │   │       │   │   │   │       │   │   └── cases.md  说明文档：Case evidence · Horror and suspense
│   │   │       │   │   │   │       │   └── SKILL.md  Horror and suspense · 恐怖悬疑短片
│   │   │       │   │   │   │       ├── seedance-meme-comedy/  目录入口
│   │   │       │   │   │   │       │   ├── references/  目录入口
│   │   │       │   │   │   │       │   │   └── cases.md  说明文档：Case evidence · Twist-ending comedy skit
│   │   │       │   │   │   │       │   └── SKILL.md  Twist-ending comedy skit · 反转结尾搞笑短片
│   │   │       │   │   │   │       ├── seedance-pet-animal/  目录入口
│   │   │       │   │   │   │       │   ├── references/  目录入口
│   │   │       │   │   │   │       │   │   └── cases.md  说明文档：Case evidence · Pets and animals as the lead
│   │   │       │   │   │   │       │   └── SKILL.md  Pets and animals as the lead · 宠物动物当主角
│   │   │       │   │   │   │       ├── seedance-prompt-library/  目录入口
│   │   │       │   │   │   │       │   ├── bin/  目录入口
│   │   │       │   │   │   │       │   │   └── install.mjs  资料与资源
│   │   │       │   │   │   │       │   ├── CHANGELOG.md  说明文档：Changelog
│   │   │       │   │   │   │       │   ├── package.json  结构化配置与索引
│   │   │       │   │   │   │       │   ├── references/  目录入口
│   │   │       │   │   │   │       │   │   └── style-library.md  说明文档：Seedance Prompt Style Library
│   │   │       │   │   │   │       │   └── SKILL.md  说明文档：Seedance Prompt Library
│   │   │       │   │   │   │       ├── seedance-retro-dv-home-video/  目录入口
│   │   │       │   │   │   │       │   ├── references/  目录入口
│   │   │       │   │   │   │       │   │   └── cases.md  说明文档：Case evidence · Early-2000s DV home video
│   │   │       │   │   │   │       │   └── SKILL.md  Early-2000s DV home video · 早年 DV 家庭录像
│   │   │       │   │   │   │       ├── seedance-sports-extreme/  目录入口
│   │   │       │   │   │   │       │   ├── references/  目录入口
│   │   │       │   │   │   │       │   │   └── cases.md  说明文档：Case evidence · Sports and extreme stunts
│   │   │       │   │   │   │       │   └── SKILL.md  Sports and extreme stunts · 体育与极限运动
│   │   │       │   │   │   │       ├── seedance-storyboard-grid-to-video/  目录入口
│   │   │       │   │   │   │       │   ├── references/  目录入口
│   │   │       │   │   │   │       │   │   └── cases.md  说明文档：Case evidence · Storyboard grid to video
│   │   │       │   │   │   │       │   └── SKILL.md  Storyboard grid to video · 分镜网格转视频
│   │   │       │   │   │   │       └── seedance-travel-city-walk/  目录入口
│   │   │       │   │   │   │           ├── references/  目录入口
│   │   │       │   │   │   │           │   └── cases.md  说明文档：Case evidence · Cinematic travel vlog montage
│   │   │       │   │   │   │           └── SKILL.md  Cinematic travel vlog montage · 电影感旅行漫游
│   │   │       │   │   │   ├── assets/  目录入口
│   │   │       │   │   │   │   ├── goodcase-retest-evidence.png  图片素材
│   │   │       │   │   │   │   ├── goodcase-seedance-gallery.png  图片素材
│   │   │       │   │   │   │   ├── hero.svg  资料与资源
│   │   │       │   │   │   │   └── retests/  目录入口
│   │   │       │   │   │   │       ├── seedance-25-diner-frozen-time-rewind.jpg  图片素材
│   │   │       │   │   │   │       ├── seedance-25-minidv-coffee-asmr-vlog.jpg  图片素材
│   │   │       │   │   │   │       └── vlog-c8171f712492.jpg  图片素材
│   │   │       │   │   │   ├── code-of-conduct.md  说明文档：Contributor Covenant Code of Conduct
│   │   │       │   │   │   ├── contributing.md  说明文档：Contributing to Awesome Seedance
│   │   │       │   │   │   ├── data/  目录入口
│   │   │       │   │   │   │   ├── case-taxonomy.json  结构化配置与索引
│   │   │       │   │   │   │   ├── cases.json  结构化配置与索引
│   │   │       │   │   │   │   ├── fixtures/  目录入口
│   │   │       │   │   │   │   │   ├── cases.fixture.json  结构化配置与索引
│   │   │       │   │   │   │   │   └── style-library.fixture.json  结构化配置与索引
│   │   │       │   │   │   │   ├── site.json  结构化配置与索引
│   │   │       │   │   │   │   ├── skills.json  结构化配置与索引
│   │   │       │   │   │   │   ├── stats.json  结构化配置与索引
│   │   │       │   │   │   │   ├── style-library.json  结构化配置与索引
│   │   │       │   │   │   │   └── templates-local.json  结构化配置与索引
│   │   │       │   │   │   ├── docs/  目录入口
│   │   │       │   │   │   │   ├── gallery-seedance-2-0-part-1.ja.md  Seedance 2.0 — 全ケース（Part 1/3）
│   │   │       │   │   │   │   ├── gallery-seedance-2-0-part-1.md  说明文档：Seedance 2.0 — Full Gallery (Part 1/3)
│   │   │       │   │   │   │   ├── gallery-seedance-2-0-part-1.zh.md  Seedance 2.0 — 全量案例（第 1/3 页）
│   │   │       │   │   │   │   ├── gallery-seedance-2-0-part-2.ja.md  Seedance 2.0 — 全ケース（Part 2/3）
│   │   │       │   │   │   │   ├── gallery-seedance-2-0-part-2.md  说明文档：Seedance 2.0 — Full Gallery (Part 2/3)
│   │   │       │   │   │   │   ├── gallery-seedance-2-0-part-2.zh.md  Seedance 2.0 — 全量案例（第 2/3 页）
│   │   │       │   │   │   │   ├── gallery-seedance-2-0-part-3.ja.md  Seedance 2.0 — 全ケース（Part 3/3）
│   │   │       │   │   │   │   ├── gallery-seedance-2-0-part-3.md  说明文档：Seedance 2.0 — Full Gallery (Part 3/3)
│   │   │       │   │   │   │   ├── gallery-seedance-2-0-part-3.zh.md  Seedance 2.0 — 全量案例（第 3/3 页）
│   │   │       │   │   │   │   ├── gallery-seedance-2-5-part-1.ja.md  Seedance 2.5 — 全ケース（Part 1/4）
│   │   │       │   │   │   │   ├── gallery-seedance-2-5-part-1.md  说明文档：Seedance 2.5 — Full Gallery (Part 1/4)
│   │   │       │   │   │   │   ├── gallery-seedance-2-5-part-1.zh.md  Seedance 2.5 — 全量案例（第 1/4 页）
│   │   │       │   │   │   │   ├── gallery-seedance-2-5-part-2.ja.md  Seedance 2.5 — 全ケース（Part 2/4）
│   │   │       │   │   │   │   ├── gallery-seedance-2-5-part-2.md  说明文档：Seedance 2.5 — Full Gallery (Part 2/4)
│   │   │       │   │   │   │   ├── gallery-seedance-2-5-part-2.zh.md  Seedance 2.5 — 全量案例（第 2/4 页）
│   │   │       │   │   │   │   ├── gallery-seedance-2-5-part-3.ja.md  Seedance 2.5 — 全ケース（Part 3/4）
│   │   │       │   │   │   │   ├── gallery-seedance-2-5-part-3.md  说明文档：Seedance 2.5 — Full Gallery (Part 3/4)
│   │   │       │   │   │   │   ├── gallery-seedance-2-5-part-3.zh.md  Seedance 2.5 — 全量案例（第 3/4 页）
│   │   │       │   │   │   │   ├── gallery-seedance-2-5-part-4.ja.md  Seedance 2.5 — 全ケース（Part 4/4）
│   │   │       │   │   │   │   ├── gallery-seedance-2-5-part-4.md  说明文档：Seedance 2.5 — Full Gallery (Part 4/4)
│   │   │       │   │   │   │   ├── gallery-seedance-2-5-part-4.zh.md  Seedance 2.5 — 全量案例（第 4/4 页）
│   │   │       │   │   │   │   ├── gallery.ja.md  Awesome Seedance — ギャラリー索引
│   │   │       │   │   │   │   ├── gallery.md  说明文档：Awesome Seedance — Gallery Index
│   │   │       │   │   │   │   ├── gallery.zh.md  Awesome Seedance — 画廊总览
│   │   │       │   │   │   │   └── templates/  目录入口
│   │   │       │   │   │   │       ├── en/  说明文档：Prompt Templates by Category (25)
│   │   │       │   │   │   │       │   ├── 3d-cartoon.md  说明文档：🎨 3D cartoon character short
│   │   │       │   │   │   │       │   ├── anime-style-lock.md  说明文档：🎨 Anime and stylized style lock
│   │   │       │   │   │   │       │   ├── car-vehicle.md  说明文档：💥 Cars and vehicles at speed
│   │   │       │   │   │   │       │   ├── character-reference-lock.md  说明文档：🧱 Reference image identity lock
│   │   │       │   │   │   │       │   ├── cinematic-narrative-short.md  说明文档：🎭 Cinematic narrative short
│   │   │       │   │   │   │       │   ├── combat-choreography.md  说明文档：💥 Combat choreography
│   │   │       │   │   │   │       │   ├── dialogue-performance-beats.md  说明文档：🎭 Dialogue and performance beats
│   │   │       │   │   │   │       │   ├── epic-fantasy-scifi.md  说明文档：💥 Epic fantasy and sci-fi spectacle
│   │   │       │   │   │   │       │   ├── fashion-lookbook.md  说明文档：🛒 Fashion lookbook and portrait film
│   │   │       │   │   │   │       │   ├── handheld-ugc-vlog.md  说明文档：📱 Handheld UGC vlog
│   │   │       │   │   │   │       │   ├── horror-suspense.md  说明文档：🎭 Horror and suspense
│   │   │       │   │   │   │       │   ├── meme-comedy.md  说明文档：🎭 Twist-ending comedy skit
│   │   │       │   │   │   │       │   ├── music-beat-sync-mv.md  说明文档：💥 Beat-synced music video
│   │   │       │   │   │   │       │   ├── pet-animal.md  说明文档：📱 Pets and animals as the lead
│   │   │       │   │   │   │       │   ├── pov-continuous-take.md  说明文档：📱 First-person continuous take
│   │   │       │   │   │   │       │   ├── process-transformation-montage.md  说明文档：🛒 Process and transformation montage
│   │   │       │   │   │   │       │   ├── product-commercial-shotlist.md  说明文档：🛒 Cinematic product commercial shot list
│   │   │       │   │   │   │       │   ├── README.md  说明文档：Prompt Templates by Category (25)
│   │   │       │   │   │   │       │   ├── retro-found-footage.md  说明文档：📱 Early-2000s DV home video
│   │   │       │   │   │   │       │   ├── sports-extreme.md  说明文档：💥 Sports and extreme stunts
│   │   │       │   │   │   │       │   ├── stop-motion-cadence.md  说明文档：🎨 Stop motion and stepped cadence
│   │   │       │   │   │   │       │   ├── storyboard-grid-to-video.md  说明文档：🧱 Storyboard grid to video
│   │   │       │   │   │   │       │   ├── time-freeze-rewind.md  说明文档：💥 Time freeze and rewind set piece
│   │   │       │   │   │   │       │   ├── timeline-shot-script.md  说明文档：🧱 Second-by-second timeline script
│   │   │       │   │   │   │       │   ├── travel-city-walk.md  说明文档：🎭 Cinematic travel vlog montage
│   │   │       │   │   │   │       │   └── ugc-creator-review.md  说明文档：🛒 UGC creator review with spoken lines
│   │   │       │   │   │   │       └── zh/  分类提示语模板（25 个）
│   │   │       │   │   │   │           ├── 3d-cartoon.md  🎨 3D 卡通角色短片
│   │   │       │   │   │   │           ├── anime-style-lock.md  🎨 动漫与风格化画风固定
│   │   │       │   │   │   │           ├── car-vehicle.md  💥 汽车与载具速度片
│   │   │       │   │   │   │           ├── character-reference-lock.md  🧱 参考图身份锁定
│   │   │       │   │   │   │           ├── cinematic-narrative-short.md  🎭 电影级叙事短片
│   │   │       │   │   │   │           ├── combat-choreography.md  💥 打斗编排
│   │   │       │   │   │   │           ├── dialogue-performance-beats.md  🎭 对白与表演节拍
│   │   │       │   │   │   │           ├── epic-fantasy-scifi.md  💥 奇幻科幻大场面
│   │   │       │   │   │   │           ├── fashion-lookbook.md  🛒 时尚 lookbook 与人像写真片
│   │   │       │   │   │   │           ├── handheld-ugc-vlog.md  📱 手持 UGC vlog
│   │   │       │   │   │   │           ├── horror-suspense.md  🎭 恐怖悬疑短片
│   │   │       │   │   │   │           ├── meme-comedy.md  🎭 反转结尾搞笑短片
│   │   │       │   │   │   │           ├── music-beat-sync-mv.md  💥 音乐卡点 MV
│   │   │       │   │   │   │           ├── pet-animal.md  📱 宠物动物当主角
│   │   │       │   │   │   │           ├── pov-continuous-take.md  📱 第一人称一镜到底
│   │   │       │   │   │   │           ├── process-transformation-montage.md  🛒 流程与变换蒙太奇
│   │   │       │   │   │   │           ├── product-commercial-shotlist.md  🛒 电影级产品广告分镜
│   │   │       │   │   │   │           ├── README.md  分类提示语模板（25 个）
│   │   │       │   │   │   │           ├── retro-found-footage.md  📱 早年 DV 家庭录像
│   │   │       │   │   │   │           ├── sports-extreme.md  💥 体育与极限运动
│   │   │       │   │   │   │           ├── stop-motion-cadence.md  🎨 定格动画与步进节奏
│   │   │       │   │   │   │           ├── storyboard-grid-to-video.md  🧱 分镜网格转视频
│   │   │       │   │   │   │           ├── time-freeze-rewind.md  💥 时间冻结与倒放奇观
│   │   │       │   │   │   │           ├── timeline-shot-script.md  🧱 逐秒时间轴分镜脚本
│   │   │       │   │   │   │           ├── travel-city-walk.md  🎭 电影感旅行漫游
│   │   │       │   │   │   │           └── ugc-creator-review.md  🛒 UGC 口播测评带货
│   │   │       │   │   │   ├── LICENSE  资料与资源
│   │   │       │   │   │   ├── package.json  结构化配置与索引
│   │   │       │   │   │   ├── README.md  说明文档：Awesome Seedance [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
│   │   │       │   │   │   ├── README_ja.md  说明文档：Awesome Seedance [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
│   │   │       │   │   │   ├── README_zh.md  说明文档：Awesome Seedance [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
│   │   │       │   │   │   ├── scripts/  目录入口
│   │   │       │   │   │   │   ├── check-links.mjs  资料与资源
│   │   │       │   │   │   │   ├── fetch-retest-posters.mjs  资料与资源
│   │   │       │   │   │   │   ├── fetch-site-stats.mjs  资料与资源
│   │   │       │   │   │   │   ├── generate-readme.mjs  资料与资源
│   │   │       │   │   │   │   ├── generate-skill-reference.mjs  资料与资源
│   │   │       │   │   │   │   ├── generate-standalone-skills.mjs  资料与资源
│   │   │       │   │   │   │   ├── lib/  目录入口
│   │   │       │   │   │   │   │   ├── library.mjs  资料与资源
│   │   │       │   │   │   │   │   ├── render.mjs  资料与资源
│   │   │       │   │   │   │   │   ├── render.test.mjs  资料与资源
│   │   │       │   │   │   │   │   ├── sections.mjs  资料与资源
│   │   │       │   │   │   │   │   ├── sections.test.mjs  资料与资源
│   │   │       │   │   │   │   │   ├── standalone-skill.mjs  资料与资源
│   │   │       │   │   │   │   │   ├── standalone-skill.test.mjs  资料与资源
│   │   │       │   │   │   │   │   ├── submissions.mjs  资料与资源
│   │   │       │   │   │   │   │   ├── submissions.test.mjs  资料与资源
│   │   │       │   │   │   │   │   ├── templates.mjs  资料与资源
│   │   │       │   │   │   │   │   └── templates.test.mjs  资料与资源
│   │   │       │   │   │   │   ├── taxonomy-todo.mjs  资料与资源
│   │   │       │   │   │   │   └── validate-submissions.mjs  资料与资源
│   │   │       │   │   │   └── submissions/  说明文档：Submissions
│   │   │       │   │   │       ├── README.md  说明文档：Submissions
│   │   │       │   │   │       └── TEMPLATE.json  结构化配置与索引
│   │   │       │   │   ├── template-guide.md  按镜头需求选25类模板及处理冲突
│   │   │       │   │   └── upstream.json  第三方来源、固定版本与三类许可
│   │   │       │   ├── README.md  跨片型通用制作经验
│   │   │       │   └── tools/  按已选平台查生成技巧、参数边界与案例
│   │   │       │       ├── README.md  工具索引
│   │   │       │       └── seedance/  复用主体、场景参考及提示词的实战经验
│   │   │       │           ├── practical-workflow.md  实战工作流
│   │   │       │           ├── prompt-cases.md  提示词案例
│   │   │       │           ├── prompt-templates.md  提示词模板
│   │   │       │           └── README.md  Seedance 工具入口
│   │   │       ├── education/  为教师委托的微课与教育交互作品查制作规范
│   │   │       │   ├── ai-generated-microcourse-video-workflow.md  AI教师微课的音频分段、场景关键图、多镜头提示词与验收方法
│   │   │       │   ├── interactive-production-workbench.md  仅微课适用：按教学设计、逐字稿与音频组织分镜、参考图、提示词和验收
│   │   │       │   ├── README.md  微课、精品课、MG 动画与教育课件
│   │   │       │   └── showcase-guidelines.md  展示微课案例时检查受众、措辞和成果表达
│   │   │       ├── promo/  查企业与创赛宣传片的分镜、素材和交付经验
│   │   │       │   ├── competition-promo-production.md  创赛文稿拆镜、AI与AE模板分工、定格叠字、参考图动态化与迭代验收
│   │   │       │   ├── prompt-iteration.md  调整企业片的镜头节奏并记录提示词迭代
│   │   │       │   ├── README.md  企业宣传片制作经验
│   │   │       │   ├── visual-recipes.md  为科技企业片选择可选视觉表现与组合方式
│   │   │       │   └── workflow.md  按流程组织企业片制作并检查交付结果
│   │   │       ├── README.md  类型索引
│   │   │       ├── revisions/  视频制作方法的方向与适用范围修订
│   │   │       │   ├── 2026-09-18-competition-and-microcourse-scope.md  创赛画面反馈沉淀，微课工作台迁移并收窄适用范围
│   │   │       │   ├── 2026-09-18-competition-opening-visual-rollback.md  撤回全景与扫描包装过度修订，保留机械质感并尝试三维图板
│   │   │       │   ├── 2026-09-21-competition-production-retrospective.md  石墨烯创赛片完工复盘：制作分工、Seedance参考图与多轮失败修正
│   │   │       │   ├── 2026-09-24-awesome-seedance-integration.md  第三方视频库收录、按需读取与既有经验保护
│   │   │       │   └── README.md  视频制作修订记录
│   │   │       └── story/  查找真人故事与漫剧的叙事制作入口
│   │   │           ├── motion-comic.md  漫剧制作入口
│   │   │           └── README.md  真人实拍故事与电影叙事
│   │   ├── development/  查网站、应用与自动化开发的方法及工具
│   │   │   ├── experience/  通用编程经验
│   │   │   │   ├── creative-frontend-prompt-patterns.md  创意前端提示词方法
│   │   │   │   ├── frontend-ui-quality-standards.md  按布局、响应式和交互状态检查前端成品
│   │   │   │   ├── README.md  经验索引
│   │   │   │   ├── reference-materials/  编程参考资料
│   │   │   │   │   ├── creative-frontend-prompts/  按需查看创意界面提示词原文，避免直接当通用规则
│   │   │   │   │   │   ├── raw/  未经提炼的原文
│   │   │   │   │   │   │   ├── dark-editorial-portfolio.txt  文本资料
│   │   │   │   │   │   │   ├── jack-3d-creator-portfolio.txt  文本资料
│   │   │   │   │   │   │   ├── prmpt-fashion-archive.txt  文本资料
│   │   │   │   │   │   │   ├── sentinel-spline-3d-hero.txt  文本资料
│   │   │   │   │   │   │   └── synapsex-video-scrub.txt  文本资料
│   │   │   │   │   │   └── README.md  创意前端原始提示词索引
│   │   │   │   │   └── README.md  参考资料索引
│   │   │   │   └── revisions/  追溯开发方法的重要纠正与适用范围变化
│   │   │   │       ├── 2026-09-15-mobile-ui-verification.md  追溯“移动端 UI：纠正“记录了规则但成品仍遗漏””的调整原因与适用范围
│   │   │   │       └── README.md  开发经验修订记录
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
│   │   │       │   │   ├── prompts/  按登录、支付、上传和排错等任务选用提示词
│   │   │       │   │   │   ├── authentication.md  排查短信登录与手机号身份不一致问题
│   │   │       │   │   │   ├── backend-storage.md  在应用创建时明确形态和真实后端持久化
│   │   │       │   │   │   ├── execution-and-handoff.md  约定AI修改边界、分批执行和源码交付方式
│   │   │       │   │   │   ├── payment-integration.md  在匹配的支付环境中复用已验证集成片段
│   │   │       │   │   │   ├── README.md  秒哒提示词：按任务读取
│   │   │       │   │   │   ├── runtime-diagnostics.md  给云端或移动端故障补诊断日志与证据回传
│   │   │       │   │   │   ├── seo-and-content.md  核对公开页面的SEO字段和内容整改覆盖范围
│   │   │       │   │   │   └── uploads.md  优先核验原生上传限制，再处理大文件与小程序上传
│   │   │       │   │   ├── README.md  经验索引
│   │   │       │   │   └── reference-materials/  原始参考资料
│   │   │       │   │       ├── README.md  参考资料索引
│   │   │       │   │       └── video-chunked-upload/  保存旧环境的分片上传兜底实现及使用限制
│   │   │       │   │           ├── legacy-contract.md  核对旧分片代理适用条件，避免覆盖当前原生上传方案
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
│   │   ├── other/  收纳跨行业商业方法及通用Skill能力入口
│   │   │   ├── commercial/  商业化与对外交付
│   │   │   │   ├── delivery-formats/  按场景选择商业文件交付格式
│   │   │   │   │   ├── gov-enterprise-word.md  政府与企业Word方案居中题头及正文排版
│   │   │   │   │   ├── README.md  交付格式索引与新增样式规则
│   │   │   │   │   └── references/  用户选定的版式参考与采用范围
│   │   │   │   │       ├── gov-enterprise-word-reference.png  用户图二政企Word排版参考
│   │   │   │   │       └── README.md  政企Word参考来源与视觉边界
│   │   │   │   ├── experience/  查需求识别、案例表达与对外交付经验
│   │   │   │   │   ├── business-analysis-cards.md  梳理产品信息、渠道选择与竞品对标依据
│   │   │   │   │   ├── case-result-narrative.md  案例选择、结果证明、观点叙事与产品承接
│   │   │   │   │   ├── competition-and-investor-materials.md  为赛事、路演与融资材料核对受众和披露边界
│   │   │   │   │   ├── content-demand-and-conversion.md  从内容反馈识别需求并衔接商业服务
│   │   │   │   │   ├── external-deliverable-language.md  把内部工作说明改为客户或机构可直接使用的成品
│   │   │   │   │   ├── external-proposal-design.md  对外培训及项目方案的内容筛选和验收
│   │   │   │   │   └── README.md  内容经营与商业交付经验索引
│   │   │   │   ├── README.md  跨行业商业方法、触发规则与交付边界
│   │   │   │   └── revisions/  商业交付规则修订与真实反馈
│   │   │   │       ├── 2026-09-17-external-proposal-and-word-format.md  对外方案受众纠错、政企Word格式与反例检查
│   │   │   │       └── README.md  商业交付修订索引
│   │   │   ├── README.md  其他领域与项目索引及准入条件
│   │   │   └── skills/  按任务找Skill，并核对来源、版本与执行条件
│   │   │       ├── editaplot/  用实验数据制作可编辑的Origin科研图
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
│   │   │       │   │   ├── ASSET_PROVENANCE.md  说明文档：Asset and data provenance
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
│   │   │       │   │   ├── AUTHORS.md  说明文档：Authors and contributors
│   │   │       │   │   ├── CHANGELOG.md  说明文档：Changelog
│   │   │       │   │   ├── CONTRIBUTING.md  说明文档：Contributing
│   │   │       │   │   ├── docs/  目录入口
│   │   │       │   │   │   ├── dependency-inventory.md  说明文档：Verified Python dependency inventory
│   │   │       │   │   │   ├── gallery.en.md  说明文档：Origin 2024b figures generated and reviewed on a live installation
│   │   │       │   │   │   ├── gallery.md  Origin 2024b 实机生成并复核的图形示例
│   │   │       │   │   │   ├── installation.md  安装与环境自检 / Installation
│   │   │       │   │   │   ├── origin-2021-2026-compatibility.md  EditaPlot 的 Origin 2021–2026b 兼容说明
│   │   │       │   │   │   ├── palette-guide.md  科研配色指南
│   │   │       │   │   │   ├── quickstart.en.md  说明文档：English quick start
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
│   │   │       │   │   ├── PRIVACY.md  说明文档：Privacy
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
│   │   │       │   │   │       │   ├── origin_acceptance.md  说明文档：Origin route acceptance — passed
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
│   │   │       │   │   │       │   ├── origin_acceptance.md  说明文档：Origin route acceptance — verified 2026-08-01
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
│   │   │       │   │   │       │   ├── origin_acceptance.md  说明文档：Origin 10.15 route acceptance
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
│   │   │       │   │   │       │   ├── data_contract.md  说明文档：XPS Adaptive Data Contract
│   │   │       │   │   │       │   ├── example_standard.csv  资料与资源
│   │   │       │   │   │       │   ├── manifest.yaml  自动化配置
│   │   │       │   │   │       │   ├── runner.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── schema.json  结构化配置与索引
│   │   │       │   │   │       │   └── visual_contract.md  说明文档：XPS Adaptive Visual Contract
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
│   │   │       │   │   ├── SECURITY.md  说明文档：Security policy
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
│   │   │       │   │   │       │   ├── chart-selection.md  说明文档：Chart selection and support levels
│   │   │       │   │   │       │   ├── data-contracts.md  说明文档：Data contracts
│   │   │       │   │   │       │   ├── figure-contract.md  说明文档：Publication-informed Origin figure contract
│   │   │       │   │   │       │   ├── origin-safety.md  说明文档：Origin Automation safety gate
│   │   │       │   │   │       │   ├── palettes.md  科研配色选择合同
│   │   │       │   │   │       │   ├── reference-figures.md  说明文档：Reference-figure adaptation
│   │   │       │   │   │       │   ├── runtime.md  说明文档：Runtime and launcher
│   │   │       │   │   │       │   ├── semantic-understanding.md  说明文档：Scientific data understanding and element confirmation
│   │   │       │   │   │       │   ├── showcase.md  说明文档：Showcase policy
│   │   │       │   │   │       │   └── verification.md  说明文档：Origin delivery verification
│   │   │       │   │   │       ├── scripts/  目录入口
│   │   │       │   │   │       │   ├── bootstrap_editaplot.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── editaplot.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   ├── editaplot_core.py  跨平台维护或执行脚本
│   │   │       │   │   │       │   └── requirements-runtime.lock  资料与资源
│   │   │       │   │   │       └── SKILL.md  说明文档：EditaPlot
│   │   │       │   │   ├── SUPPORT.md  说明文档：Support scope
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
│   │   │       │   │   ├── THIRD_PARTY_NOTICES.md  说明文档：Third-party runtime notices
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
│   │   │       ├── jianwei-ai-community-remotion-video/  用脚本或参考图制作可编辑的Remotion参数化动画
│   │   │       │   ├── README.md  建委 AI 社群 Remotion 视频 Skill 说明
│   │   │       │   ├── skill/  可直接安装的完整 Skill
│   │   │       │   │   ├── agents/  目录入口
│   │   │       │   │   │   └── openai.yaml  自动化配置
│   │   │       │   │   ├── references/  目录入口
│   │   │       │   │   │   ├── background-fidelity-contract.md  参考图背景保真契约
│   │   │       │   │   │   ├── deterministic-layout-contract.md  说明文档：Deterministic layout contract
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
│   │   │       │   │   │   ├── remotion-only-director-contract.md  说明文档：Remotion-only director contract
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
│   │   │       ├── jianwei-ai-learning-community-workbench/  根据职业与实际场景设计AI工作台和产品流程
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
│   │   │       │   │   ├── README.en.md  说明文档：Qingyun IP Poster
│   │   │       │   │   ├── README.md  说明文档：Qingyun IP Poster
│   │   │       │   │   ├── README.zh-CN.md  Qingyun IP Poster · 中文说明
│   │   │       │   │   ├── references/  目录入口
│   │   │       │   │   │   ├── design-system.md  Qingyun 海报设计系统
│   │   │       │   │   │   ├── failure-modes.md  常见失败模式与修复
│   │   │       │   │   │   ├── intake-guide.md  素材引导与模式选择
│   │   │       │   │   │   ├── prompt-compiler.md  图像层与排版层指令编译
│   │   │       │   │   │   ├── quality-checklist.md  海报交付质量检查
│   │   │       │   │   │   └── version-matrix.md  版本矩阵与系列差异控制
│   │   │       │   │   └── SKILL.md  说明文档：Qingyun IP Poster · Visual System Edition
│   │   │       │   └── upstream.json  上游仓库、固定 commit、版本与更新规则
│   │   │       └── README.md  Skill 实体索引、来源与更新规则
│   │   ├── README.md  设计、开发、培训、自媒体和其他领域的知识入口
│   │   ├── self-media/  按文章、口播、宣传和运营任务查创作经验
│   │   │   ├── articles/  组织公众号等文章与图文内容，按读者需要展开
│   │   │   │   └── README.md  文章内容方法与素材入口
│   │   │   ├── community-copy/  撰写群公告、社群沟通和群内话术
│   │   │   │   └── README.md  社群文案与话术入口
│   │   │   ├── experience/  沉淀账号经营、内容复盘与外部可借鉴经验
│   │   │   │   ├── media-growth.md  账号增长与内容规划
│   │   │   │   ├── outcome-and-motivation.md  成果展示、用户动机与知识分层
│   │   │   │   └── README.md  自媒体经验索引
│   │   │   ├── live-sales/  组织直播话术与销售内容，关联真实产品事实
│   │   │   │   ├── conversion-path.md  内容到评论、资料和社群的承接
│   │   │   │   └── README.md  直播销售与转化入口
│   │   │   ├── marketing-copy/  用读者关心的问题组织介绍页和推广内容
│   │   │   │   ├── reader-question-led-promotion.md  从报名者真实问题组织宣传内容，含改稿证据与验收
│   │   │   │   └── README.md  营销文案与推广文章入口
│   │   │   ├── moments-copy/  撰写适合朋友圈阅读和个人IP表达的内容
│   │   │   │   └── README.md  朋友圈文案入口
│   │   │   ├── README.md  内容传播与个人IP经营入口
│   │   │   ├── titles/  为自媒体选题拟标题，并诊断和比较候选
│   │   │   │   ├── README.md  标题方法与素材入口
│   │   │   │   └── title-matrix/  第三方中文标题Skill：生成、诊断、评审与复盘
│   │   │   │       ├── README.md  Title Matrix · 标题矩阵 Skill
│   │   │   │       ├── source/  上游完整快照，共 12 个文件；展开可核查内部层级
│   │   │   │       │   ├── .claude-plugin/  目录入口
│   │   │   │       │   │   └── plugin.json  结构化配置与索引
│   │   │   │       │   ├── .gitignore  资料与资源
│   │   │   │       │   ├── LICENSE  资料与资源
│   │   │   │       │   ├── README.md  Title Matrix 标题矩阵
│   │   │   │       │   └── skills/  目录入口
│   │   │   │       │       └── title-matrix/  Title Matrix 标题矩阵
│   │   │   │       │           ├── agents/  目录入口
│   │   │   │       │           │   └── openai.yaml  自动化配置
│   │   │   │       │           ├── data/  目录入口
│   │   │   │       │           │   └── .gitkeep  资料与资源
│   │   │   │       │           ├── LICENSE  资料与资源
│   │   │   │       │           ├── README.md  Title Matrix 标题矩阵
│   │   │   │       │           ├── references/  目录入口
│   │   │   │       │           │   ├── evidence.md  证据分级与研究出处
│   │   │   │       │           │   ├── platforms.md  落点细则与字数核验
│   │   │   │       │           │   └── review-and-library.md  复盘模式与案例库
│   │   │   │       │           └── SKILL.md  一稿多发标题矩阵
│   │   │   │       └── upstream.json  结构化配置与索引
│   │   │   └── video-scripts/  撰写口播与短视频脚本，按需衔接制作方法
│   │   │       ├── README.md  口播与短视频脚本入口
│   │   │       └── script-patterns.md  脚本结构模式
│   │   └── training/  查备课、学员资料与复盘方法，先区分授课系列
│   │       ├── attribution-and-updates.md  判定课程或文章归属，并同步入口和修订记录
│   │       ├── experience/  培训经验
│   │       │   ├── demo-driven-course-design.md  演示驱动课程设计
│   │       │   ├── jianwei-training-style.md  建委默认培训风格与课件形态
│   │       │   ├── README.md  经验索引
│   │       │   ├── sources.md  核对教学方法的来源、课程身份与验证范围
│   │       │   ├── teaching-and-course-design.md  备课、课件与课程设计
│   │       │   ├── technical-explanation/  技术解释方法
│   │       │   │   ├── problem-driven-technical-explanation.md  问题驱动的技术解释方法
│   │       │   │   └── README.md  方法索引
│   │       │   ├── tutorial-writing.md  学员教程写法
│   │       │   └── visual-and-oral-training-docs.md  飞书培训文档的可视化与口语化
│   │       ├── materials/  培训资料
│   │       │   └── README.md  资料入口，避免复制项目资料
│   │       ├── outlines/  培训大纲
│   │       │   └── README.md  大纲入口，当前无独立通用大纲
│   │       └── README.md  AI 培训总入口
│   ├── projects/  项目与案例：这件事具体怎样了
│   │   ├── ai-sixty-jiazi-music-ip/  三级目录：AI 六十甲子古音律与 IP 孵化
│   │   │   ├── current-operations.md  查当前Web演示的访问和操作方式
│   │   │   ├── data-audit.md  本地资料、工具与数据审计
│   │   │   ├── demo-implementation.md  四模块 Demo、测试与本地交付记录
│   │   │   ├── ip-character-prompts-v2-mature.md  已否决的成熟神将视觉方向
│   │   │   ├── ip-character-prompts-v3-toy.md  当前潮玩卡通视觉口径与提示词摘要
│   │   │   ├── ip-character-prompts.md  初版潮玩角色构想，保留作历史参考
│   │   │   ├── product-demo-plan.md  Web Demo 产品与技术规划
│   │   │   ├── README.md  当前项目事实、边界、唯一位置与文件索引
│   │   │   └── revisions/  追溯音乐IP项目的关键方向与实现变化
│   │   │       ├── 2026-08-24-context-relocation-to-other.md  项目迁入 other 与唯一写入位置修订
│   │   │       ├── 2026-08-24-initial-project-and-web-demo-direction.md  首次入库与 Web Demo 方向
│   │   │       ├── 2026-08-24-overseas-sound-oracle-and-stem-artifact-system.md  海外声音产品与天干法器视觉系统
│   │   │       ├── 2026-08-24-separate-web-and-toy-ip-direction.md  网站与潮玩 IP 分线及启动修复
│   │   │       ├── 2026-08-24-web-demo-implementation-complete.md  初版 Web Demo 实现与测试记录
│   │   │       ├── 2026-08-24-wide-workbench-music-prompt-v4.md  宽屏工作台、素材与音乐提示词改造
│   │   │       ├── 2026-09-02-five-tone-product-flow-and-private-audio-demo.md  五音产品流程与私有音频演示修订
│   │   │       ├── 2026-09-02-harmony-v6-ui-audit-and-interaction-fix.md  V6 界面审计与交互修复
│   │   │       └── 2026-09-02-product-v7-ui-and-profile-center.md  V7 产品界面与个人中心修订
│   │   ├── archive/  查已退出当前主线的项目，避免把旧状态当现状
│   │   │   ├── openclaw-agent/  追溯已归档AI Agent项目的资料和决策
│   │   │   │   └── README.md  OpenClaw Agent 历史档案
│   │   │   ├── README.md  归档项目索引
│   │   │   └── videoai/  追溯已归档营销视频自动化平台的项目资料
│   │   │       ├── cost-analysis.md  历史成本测算
│   │   │       ├── pricing-plan-association.md  历史协会定价方案
│   │   │       └── README.md  VideoAI 历史项目入口
│   │   ├── cases/  按真实商单或实践记录查过程、结果和可复用方法
│   │   │   ├── 2026-05-enterprise-prompt-record.md  查看企业片提示词的真实调整过程与适用限制
│   │   │   ├── little-leaf-ai-microcourse-mv.md  《小树叶》AI教师音乐微课画面制作与修订复盘
│   │   │   └── README.md  商单与实践案例
│   │   ├── external-training/  按机构与场次管理外出授课，和会员社群分开
│   │   │   ├── jinan-cadre-ai/  济南市总工会干部AI培训的方案与设计反馈
│   │   │   │   ├── proposal.md  当前对外培训方案正文
│   │   │   │   ├── README.md  培训事实、当前设计与文件入口
│   │   │   │   └── revisions/  本场培训方案方向与版本修订
│   │   │   │       ├── 2026-09-18-tool-panorama-and-work-scenarios.md  工具全景、提示词与六类工作场景设计反馈
│   │   │   │       └── README.md  方案修订入口
│   │   │   ├── jinan-city-library/  查济南市图书馆课程、资料及课后修订
│   │   │   │   ├── README.md  图书馆资料归属、版本与授课边界
│   │   │   │   └── revisions/  图书馆培训改稿与反馈
│   │   │   │       ├── 2026-08-19-lesson-4-student-material-boundary.md  追溯“第 4 课学员正文边界修订”的调整原因与适用范围
│   │   │   │       ├── 2026-09-02-miaoda-advanced-course-scenario-driven-updates.md  追溯“秒哒进阶课：把版本更新改造成使用场景链路”的调整原因与适用范围
│   │   │   │       └── README.md  图书馆培训修订索引
│   │   │   ├── lessons/  查外部培训的独立课程资料与修订入口
│   │   │   │   ├── bug-repair/  查图书馆Bug修复实战课的学员资料与证据链
│   │   │   │   │   ├── README.md  别让 Bug 打败你：秒哒故障定位与修复实战
│   │   │   │   │   └── revisions/  追溯Bug修复课的演示、学员稿及案例调整
│   │   │   │   │       ├── 2026-09-09-lesson-6-bug-repair-evidence-chain.md  追溯“第六课优化修订：Bug 修复证据链与一案例多故障演示台”的调整原因与适用范围
│   │   │   │   │       └── README.md  Bug 修复课程修订
│   │   │   │   └── README.md  外出培训课程资料
│   │   │   └── README.md  外出培训
│   │   ├── feishu-efficient-office/  五级目录：《飞书高效办公》
│   │   │   ├── all-docs.md  历史培训素材摘要，默认不读
│   │   │   ├── ch1-editor-feedback-lessons.md  查第1章编辑意见及后续改稿需避免的问题
│   │   │   ├── ch2-editor-feedback-lessons.md  按第2章细颗粒度反馈逐项复查书稿
│   │   │   ├── ch4-editor-feedback.md  查历史旧第4章编辑意见，不当作当前第4章要求
│   │   │   ├── ch4-v3-editor-feedback.md  追溯历史旧第4章第三版的编辑反馈
│   │   │   ├── ch4-v4-revision-log.md  追溯历史旧第4章第四版的创建与修改执行
│   │   │   ├── ch5-editor-feedback.md  各章编辑反馈与共性规则
│   │   │   ├── feishu-base-form-experience.md  多维表格表单经验
│   │   │   ├── feishu-doc-style.md  飞书文档视觉规范
│   │   │   ├── history.md  已清洗的章节修订摘要
│   │   │   ├── interface-screenshot-guidelines.md  软件截图与图文一致规范
│   │   │   ├── legacy-ch4-map.md  将旧章素材映射到当前目录，防止同章号混用
│   │   │   ├── publication-acceptance-checklist.md  检查章节基线、编辑反馈、飞书回写与Word交稿
│   │   │   ├── README.md  项目当前口径、进度和文件索引
│   │   │   ├── writing-style-analysis.md  本书专用写作风格
│   │   │   └── writing-style-history.md  核对旧风格规则的来源；默认写作不加载
│   │   ├── paid-community-course/  五级目录：AI 超级个体陪跑社群
│   │   │   ├── competitive-references.md  查外部会员社群案例及适合迁移的经营经验
│   │   │   ├── course-development.md  课程研发与内容选择
│   │   │   ├── course-materials-index.md  会员系统课程、配套文章与直播复盘分开登记
│   │   │   ├── curriculum-design.md  课程结构与直播节奏
│   │   │   ├── history.md  已清洗的关键演进摘要
│   │   │   ├── operations-playbook.md  招生、运营与转化执行
│   │   │   ├── positioning-and-vision.md  社群定位、愿景与表达边界
│   │   │   ├── README.md  当前产品与课程口径
│   │   │   ├── revisions/  六级目录：课程关键修订
│   │   │   │   ├── 2026-08-23-lesson-4-visualization-and-case-delivery.md  追溯“第 4 课可视化与案例交付修订”的调整原因与适用范围
│   │   │   │   ├── 2026-08-29-student-material-definitive-positioning.md  追溯“学员资料中的确定性学习定位”的调整原因与适用范围
│   │   │   │   ├── 2026-08-30-community-positioning-and-super-individual-definition.md  社群总定位与超级个体定义修订
│   │   │   │   ├── 2026-08-30-lesson-5-purchase-language-and-decision-boundary.md  第 5 节购买语言与决策边界修订
│   │   │   │   ├── 2026-08-31-lesson-5-post-lecture-ai-era-purpose-and-parameter-explanation.md  第 5 节课后 AI 时代目的与参数解释修订
│   │   │   │   ├── 2026-09-01-training-rule-scope-and-delivery-boundary.md  AI 培训规则适用场景与课堂交付边界修订
│   │   │   │   ├── 2026-09-01-training-rule-single-source-and-technical-selection.md  AI 培训单一来源与技术内容筛选修订
│   │   │   │   ├── 2026-09-07-lesson-6-lecture-review-and-visualization-rules.md  追溯“第六课直播复盘：学员稿表达与可视化规则”的调整原因与适用范围
│   │   │   │   ├── 2026-09-12-onboarding-expression-and-replay-scope.md  追溯“新人入口表达与回放归属修订”的调整原因与适用范围
│   │   │   │   ├── 2026-09-13-reader-questions-and-introduction.md  宣传问答结构与当前介绍页事实修订
│   │   │   │   ├── 2026-09-15-ai-programming-as-first-perspective.md  追溯“AI 编程作为普通人理解 AI 的第一视角”的调整原因与适用范围
│   │   │   │   ├── 2026-09-15-ai-programming-breadth-rationale-correction.md  追溯“首期 AI 编程论证改为具体工具与连接方式”的调整原因与适用范围
│   │   │   │   ├── 2026-09-15-public-term-and-internal-continuity.md  追溯“区分对外年度口径与内部持续交付设计”的调整原因与适用范围
│   │   │   │   ├── 2026-09-15-reader-address-you-and-everyone.md  追溯“社群介绍页统一使用“你／大家”面对读者”的调整原因与适用范围
│   │   │   │   └── README.md  修订索引与读取边界
│   │   │   └── technical-dictionary-scope.md  会员配套文章的资料范围与词条边界
│   │   ├── README.md  项目与案例总入口
│   │   └── yancut-ai/  五级目录：言剪 AI
│   │       ├── architecture-and-upstream.md  架构、上游与能力边界
│   │       ├── history.md  已清洗的关键演进摘要
│   │       ├── README.md  当前项目事实与调用规则
│   │       ├── revisions/  追溯言剪AI的产品方向、实现调整与验收记录
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
│   │       │   ├── 2026-09-04-ai-progress-remotion-hyperframes-keyframes.md  AI 执行进度可视化、Remotion 本地预检与手动关键帧修订
│   │       │   ├── 2026-09-10-evidence-storyboard-workbench.md  追溯“统一工作台、素材证据与分镜剪辑”的调整原因与适用范围
│   │       │   ├── 2026-09-10-narrato-workflow-hardening.md  追溯“NarratoAI 参考与真实剪辑链路加固”的调整原因与适用范围
│   │       │   ├── 2026-09-15-hypit-montage-overlay-scenario-workflows.md  追溯“素材证据、场景规范与可编辑信息动效”的调整原因与适用范围
│   │       │   ├── 2026-09-15-personal-vercel-testing.md  追溯“个人在线测试与项目记录校正”的调整原因与适用范围
│   │       │   ├── 2026-09-16-workbench-motion-reference-templates.md  言剪动效、关键帧、参考视频与个人模板升级及线上验收
│   │       │   ├── 2026-09-17-local-first-manual-spectrum-ui.md  追溯“本地优先手册与界面整理”的调整原因与适用范围
│   │       │   ├── 2026-09-23-demo-browser-evidence.md  追溯“录屏主线真实浏览器验收”的调整原因与适用范围
│   │       │   ├── 2026-09-23-demo-release-hardening.md  追溯“口播录屏演示闭环加固”的调整原因与适用范围
│   │       │   ├── 2026-09-23-doubao-asr-context-image-preview.md  追溯“豆包标准版上下文与辅助图片接入”的调整原因与适用范围
│   │       │   ├── 2026-09-23-doubao-asr-preview-hardening.md  追溯“豆包标准版个人预览可用性修正”的调整原因与适用范围
│   │       │   └── 2026-09-23-doubao-asr-standard-billing.md  追溯“豆包录音文件识别 2.0 标准版与积分确认”的调整原因与适用范围
│   │       └── roadmap.md  开发路线与上线条件
│   └── README.md  领域知识与项目案例的分级入口
├── system/  查AI表达标准、仓库运行规则与本机执行环境
│   ├── environment/  核对当前设备、工具依赖及执行通道
│   │   ├── computers/  按设备管理
│   │   │   ├── desktop-1/  台式电脑 1
│   │   │   │   ├── disk-cleanup-and-codex-storage.md  磁盘清理与 Codex 存储基线
│   │   │   │   ├── history.md  已清洗的关键修复摘要
│   │   │   │   ├── network-and-codex.md  网络、Clash 与 Codex 排障
│   │   │   │   └── README.md  当前设备事实与操作禁区
│   │   │   ├── README.md  设备索引
│   │   │   └── windows-junction-migration.md  Windows Junction 迁移经验
│   │   ├── image-generation.md  按本机已确认的通道调用生图并排查鉴权问题
│   │   └── README.md  环境入口与安全规则
│   ├── expression/  通用表达与体裁验收
│   │   ├── corrections.md  把真实改稿反馈转为可执行的中文纠错规则
│   │   ├── evaluation.md  对照真实稿件检查表达、事实与交付质量
│   │   ├── genres.md  按课件、书稿、方案等成品类型选择表达要求
│   │   ├── oral.md  口语化论证与前后承接方法
│   │   ├── README.md  AI 表达总入口、默认激活与组合规则
│   │   ├── sources.md  核对规则来源，并按证据提炼、晋级或停用方法
│   │   └── written.md  书稿、教程、方案和文档表达规则
│   ├── README.md  AI协作与维护
│   └── repository/  读取写入、导航与校验
│       ├── capability-evidence.md  依据本人实践与复用证据更新能力，收藏不算掌握
│       ├── collaboration-rules.md  明确事实、方法、项目归属和AI执行职责
│       ├── execution-checks.md  从规则读取到实际交付物验收的执行闭环
│       ├── information-architecture.md  了解四入口分工、知识归类与长期演进方向
│       ├── ingestion-workflow.md  写入资料时同步归属、索引、说明、校验和发布
│       ├── maintenance/  维护工具
│       │   ├── .gitignore  资料与资源
│       │   ├── check-deliverable.py  外部交付物的规则信号检查脚本
│       │   ├── context-route.py  跨平台维护或执行脚本
│       │   ├── context_common.py  跨平台维护或执行脚本
│       │   ├── context_retrieval.py  任务识别、实时正文检索与完整来源包
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
│       │   ├── tests/  验证调用、归属、成品检查及导航维护的行为
│       │   │   ├── README.md  维护回归测试
│       │   │   ├── test_context.py  跨平台维护或执行脚本
│       │   │   ├── test_deliverable.py  跨平台维护或执行脚本
│       │   │   ├── test_methods.py  跨领域方法发现、误触发与登记维护回归
│       │   │   ├── test_retrieval.py  自然任务检索与读取证据回归
│       │   │   ├── test_seedance.py  视频提示词自动调用、误触发和按需读取回归
│       │   │   └── test_title_matrix.py  跨平台维护或执行脚本
│       │   ├── validate-context.ps1  结构、索引与链接校验脚本
│       │   ├── validate-context.py  跨平台维护或执行脚本
│       │   └── validation-policy.json  结构化配置与索引
│       ├── navigation/  按任务定位知识并查项目关系与完整文件结构
│       │   ├── history.md  历史入口和读取边界
│       │   ├── projects.json  结构化配置与索引
│       │   ├── README.md  任务路由与项目登记
│       │   ├── routes.json  结构化配置与索引
│       │   ├── STRUCTURE.html  日常知识导航与完整文件视图
│       │   ├── STRUCTURE.md  完整物理文件树与结构约定
│       │   └── task-guide.md  完整任务指南，按主任务和条件依赖读取
│       ├── README.md  治理总入口
│       ├── revisions/  仓库级重大修订
│       │   ├── 2026-04-05-context-repository-established.md  追溯“建立长期AI协作上下文仓库”的调整原因与适用范围
│       │   ├── 2026-08-18-information-architecture-rebuild.md  五个一级入口的信息架构重构记录
│       │   ├── 2026-08-20-ai-expression-default-layer.md  AI 表达默认层和语言规则修订
│       │   ├── 2026-08-21-chinese-quality-and-source-governance.md  中文质量基础层与多来源冲突治理修订
│       │   ├── 2026-08-21-commercial-delivery-domain.md  商业化与对外交付边界层首次建立记录
│       │   ├── 2026-08-21-commercial-delivery-relocation.md  商业化迁移到其他领域的修订
│       │   ├── 2026-08-21-desktop-sync-resilience.md  追溯“桌面 HTML 同步稳定性加固”的调整原因与适用范围
│       │   ├── 2026-08-21-direct-main-and-desktop-sync.md  直推 main、旧分支清理与桌面同步修订
│       │   ├── 2026-08-21-interactive-html-structure-viewer.md  交互式 HTML 结构查看与自动同步修订
│       │   ├── 2026-08-22-cognition-and-content-commercialization.md  追溯“建委认知归组与跨行业内容经营修订”的调整原因与适用范围
│       │   ├── 2026-08-23-feishu-document-routing-boundary.md  飞书文档承载平台与飞书书籍项目的路由边界
│       │   ├── 2026-08-24-sixty-jiazi-project-relocation.md  六十甲子项目迁入 other 与唯一路由规则
│       │   ├── 2026-08-27-commercial-external-material-boundary.md  赛事、路演与融资材料的对外边界修订
│       │   ├── 2026-09-01-ai-programming-skill-repository.md  AI 编程 Skill 仓库与上游快照治理
│       │   ├── 2026-09-01-case-result-narrative.md  追溯“案例结果叙事方法入库修订”的调整原因与适用范围
│       │   ├── 2026-09-01-remotion-skill-confirmation-and-action-contract.md  Remotion Skill 确认门与逐元素动作契约修订
│       │   ├── 2026-09-01-remotion-skill-director-and-parameterization.md  追溯“Remotion Skill 导演层与参数化默认输出修订”的调整原因与适用范围
│       │   ├── 2026-09-02-jianwei-remotion-parameterization.md  Studio 右侧 Default Props 可编辑性验收修订 Remotion Skill 导演层、重叠节奏与参数化默认输出修订
│       │   ├── 2026-09-04-remotion-reference-fidelity-and-preview-gate.md  Remotion Skill 参考图保真、低清预览与最终渲染确认门修订
│       │   ├── 2026-09-05-remotion-deterministic-layout.md  追溯“Remotion Skill 修订：数字与高密度布局确定性”的调整原因与适用范围
│       │   ├── 2026-09-05-remotion-director-expansion-and-background-fidelity.md  Remotion Skill 内部导演加工、动作自然度与背景保真修订
│       │   ├── 2026-09-05-remotion-layout-locked-continuity.md  追溯“Remotion 参考图几何锁定与连续性审计”的调整原因与适用范围
│       │   ├── 2026-09-05-remotion-text-stability-and-director-console.md  Remotion Skill 文字抗抖、字体锁定、布局稳定校验与导演台固定输出修订
│       │   ├── 2026-09-05-remotion-text-visibility-and-clipping.md  Remotion Skill 文字与关键元素完整可见、裁剪祖先和最长参数压力测试修订
│       │   ├── 2026-09-05-remotion-universal-adaptive-architecture.md  Remotion Skill 几何锁定、禁止片尾整图覆盖与连续性审计修订
│       │   ├── 2026-09-07-structure-sync-and-content-routing.md  结构镜像同步与表达/自媒体分流修订
│       │   ├── 2026-09-07-training-review-generalization-and-reinforcement.md  AI 培训复盘通用化与重复错误强化机制
│       │   ├── 2026-09-12-context-operation-and-attribution.md  追溯“上下文运行规则与资料归属纠正”的调整原因与适用范围
│       │   ├── 2026-09-12-hierarchical-navigation-and-expression.md  追溯“分级导航、项目集中与表达标准调整”的调整原因与适用范围
│       │   ├── 2026-09-12-personal-expression-and-skill-refinement.md  追溯“个人信息、表达与Skill归属调整”的调整原因与适用范围
│       │   ├── 2026-09-13-experience-adherence-audit.md  培训经验遵循性审计与执行闭环修订
│       │   ├── 2026-09-15-writing-dna-review-and-method-routing.md  写作蒸馏器评估、材料提炼与按任务发现方法
│       │   ├── 2026-09-16-training-attribution-and-navigation.md  本人确认培训归属、文章课程区分与日常导航
│       │   ├── 2026-09-21-task-retrieval-and-adherence.md  从自然任务到具体经验和成品验收的调用修复
│       │   ├── 2026-09-24-navigation-descriptions.md  追溯导航中文用途说明补齐、缺项校验和直接发布要求
│       │   ├── 2026-09-24-title-matrix-integration.md  追溯“Title Matrix收录与自媒体标题调用”的调整原因与适用范围
│       │   └── README.md  仓库修订索引
│       ├── roadmap.md  按真实使用问题安排仓库后续改进
│       ├── templates/  新建项目、案例或方法记录时复用基本字段
│       │   ├── case.md  记录真实输入、过程、结果、限制与复用方法
│       │   ├── method.md  写清方法适用条件、执行步骤、来源和验收
│       │   ├── project.md  建立长期项目的事实、资料索引与修订入口
│       │   └── README.md  项目、案例与方法模板
│       └── versioned-knowledge-policy.md  动态产品知识与版本治理
├── .gitattributes  Git 文本属性与换行规范
├── .github/  目录入口
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

*结构最后确认：2026-09-24*
