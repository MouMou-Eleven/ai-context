# 自媒体与个人IP经营

> 保存标题、文章、口播、朋友圈、直播和运营经验，不限AI主题。它是独立工作领域，课程产品事实回项目核对；通用表达由system中的表达与成品标准提供。

## 目录结构

```text
self-media/
├── README.md       总入口与激活边界
├── titles/         标题与选题
├── articles/       图文与文章
├── marketing-copy/ 营销文案与推广文章
├── moments-copy/   朋友圈文案
├── community-copy/ 社群文案与话术
├── video-scripts/  口播视频与脚本结构
├── live-sales/     直播销售与内容承接
└── experience/     账号、内容、测试和复盘经验
```

## 写前固定读者与用途

用户直接指定本目录时，实际读取本页和命中的方法正文，不能只列目录或只读索引便开始写。宣传面向潜在购买者，知识文章面向内容读者；讲师、运营者拿去使用不改变成品接收者。按[执行与验收](../../../system/repository/execution-checks.md)留本次约束与成品位置证据。

写产品介绍、报名页、宣传文或回应购买顾虑时，读取[读者问题驱动的宣传方法](./marketing-copy/reader-question-led-promotion.md)：检查问题是否真实关切、答案是否回答、顺序是否衔接、事实是否当前有效。只改成疑问标题不算遵循。纯科普、普通自媒体文章不强制招生问答。

## 读取路由

| 任务 | 首读 |
|---|---|
| 标题、选题、开头 | [`titles/README.md`](./titles/README.md) |
| 图文、文章、公众号内容 | [`articles/README.md`](./articles/README.md) |
| 营销文章、推广文案、产品介绍和跨平台转化文字 | [`marketing-copy/README.md`](./marketing-copy/README.md) |
| 朋友圈文案和连续朋友圈组合 | [`moments-copy/README.md`](./moments-copy/README.md) |
| 社群公告、群内话术和资料承接说明 | [`community-copy/README.md`](./community-copy/README.md) |
| 短视频口播和脚本 | [`video-scripts/README.md`](./video-scripts/README.md) |
| 直播销售、评论关键词、资料与社群承接 | [`live-sales/README.md`](./live-sales/README.md) |
| 账号规划、成果展示、用户动机、内容测试和复盘 | [`experience/README.md`](./experience/README.md) |

## 严格激活规则

- 自媒体、标题、口播、短视频和直播任务生成中文成品时，读取[表达短卡](../../../system/expression/README.md)及本目录对应体裁入口。
- AI 表达负责中文语境、逻辑和质量；本目录负责标题、选题、文章、营销文案、朋友圈、社群话术、口播结构、直播销售、平台承接和内容复盘。
- 通用口语表达、句子节奏和口语化论证统一读取[口语表达](../../../system/expression/oral.md)；本目录只记录自媒体渠道和营销场景的应用，不复制通用口语规则。
- 按实际任务补充必要的[技术解释方法](../training/experience/technical-explanation/README.md)，不因方法来自培训就带入社群事实。
- 内容为某个项目服务时，根据本轮信息和仓库证据确认项目，再读取对应README；身份不明确时保持待确认，不能用课程或直播关键词默认关联会员社群。
- 内容承担获客、产品价值解释、购买顾虑处理或商业承接任务时，组合[商业方法](../other/commercial/experience/content-demand-and-conversion.md)。是否组合由实际目的决定。
- 使用案例演示产品价值、直播展示课程或社群案例、用结果叙事承接购买时，再组合 [`../../other/commercial/experience/case-result-narrative.md`](../other/commercial/experience/case-result-narrative.md)；它负责跨行业案例方法，本目录仍负责自媒体表达与平台动作。
- 内容需要建委的个人经历或判断时，自动读取 `personal/` 或 `brain/` 的相关来源；只引用有证据的经历，不把通用AI表达当作个人口吻。
- 平台算法、流量规律和效果数字必须重新核验；经验不能写成效果保证。

## 语言质量规则

中文搭配、逻辑和语境的问题按需读[跨领域表达](../../../system/expression/corrections.md)。口播和直播按任务读[口语表达](../../../system/expression/oral.md)，文章和正式图文读[书面表达](../../../system/expression/written.md)。本目录不复制跨领域语言规则。

## 写入规则

- 标题、文章、营销文案、朋友圈、社群话术、口播、直播销售和运营复盘分别归类，不混在一个大文件。
- 分类优先按主要发布渠道，其次按内容目的；同一份材料只保留一个主归属，其他目录只引用。
- 跨平台且不属于单一渠道的推广内容进入 `marketing-copy/`，不要因为内容提到社群或朋友圈就重复存放。
- 同一方法只保留一份；项目文件只引用，不复制。
- 没有真实数据时明确写“待验证”，不编造案例和效果。
- 旧平台技巧失效后退出当前文件，必要时用 Git 历史追溯。

*结构确认：2026-09-12*

<!-- generated-related-assets:start -->
## 相关项目与案例

| 类型 | 项目或案例 | 适用领域 |
|---|---|---|
| 长期项目 | [AI 超级个体陪跑社群](../../projects/paid-community-course/README.md) | 会员培训与社群经营 |
<!-- generated-related-assets:end -->

<!-- generated-methods:start -->
## 按实际需要选择方法

由routes.json生成。先判断本次成品和读者，再按下表实际需要读取方法正文；无需点名作者。多种方法可分工，但同一段不拼接相互冲突的结构。没有适用需求时跳过，不能因看到本表就全部加载。

| 需要解决什么 | 方法正文 | 不适用／保留边界 | 成品怎样检查 |
|---|---|---|---|
| 非技术读者需要理解概念、机制或技术差别，不能只背定义时；主题可以来自提示，也可以来自AI读到的材料 | [从问题推导概念](../training/experience/technical-explanation/problem-driven-technical-explanation.md) | 纯查询、术语速查、直接操作、已接受稿逐字保护时不展开推导；出版只借解释逻辑，保留出版书面语与编辑规则 | 读者能说出原问题、关键变化及使用判断；不虚构历史发展、事实或作者经历，不混入讲师指令 |
| 产品介绍、报名页或购买顾虑说明，需要把整体内容、当前内容和真实价值讲清时 | [用读者问题组织宣传](marketing-copy/reader-question-led-promotion.md) | 纯教学、普通科普、内部复盘不套招生问答；具体价格、权益与已发布状态回项目核对 | 每问影响读者理解或决定；答案直接回应，后一问承接前一答；不是只增加问号 |
<!-- generated-methods:end -->
