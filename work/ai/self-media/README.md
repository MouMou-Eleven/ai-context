# AI Self-Media — AI 自媒体

> 本目录保存 AI 相关自媒体的标题、文章、口播视频、直播销售和运营经验。它是独立领域，不属于 AI 培训；中文基础质量由建委大脑中的 AI 表达库统一提供。

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

- 只提“AI 自媒体、标题、口播、短视频、直播销售”并要求生成中文内容时，读取 [`../../../brain/ai-expression/`](../../../brain/ai-expression/README.md) + 本目录。
- AI 表达负责中文语境、逻辑和质量；本目录负责标题、选题、文章、营销文案、朋友圈、社群话术、口播结构、直播销售、平台承接和内容复盘。
- 通用口语表达、句子节奏和口语化论证统一读取 [`../../../brain/ai-expression/oral-expression/README.md`](../../../brain/ai-expression/oral-expression/README.md)；本目录只记录自媒体渠道和营销场景的应用，不复制通用口语规则。
- 按实际任务补充必要的[技术解释方法](../training/experience/technical-explanation/README.md)，不因方法来自培训就带入社群事实。
- 内容为某个项目服务时，根据本轮信息和仓库证据确认项目，再读取对应README；身份不明确时保持待确认，不能用课程或直播关键词默认关联会员社群。
- 内容承担获客、产品价值解释、购买顾虑处理或商业承接任务时，组合 [`../../other/commercial/experience/content-demand-and-conversion.md`](../../other/commercial/experience/content-demand-and-conversion.md)；跨行业商业层不计作第二个专业领域。
- 使用案例演示产品价值、直播展示课程或社群案例、用结果叙事承接购买时，再组合 [`../../other/commercial/experience/case-result-narrative.md`](../../other/commercial/experience/case-result-narrative.md)；它负责跨行业案例方法，本目录仍负责自媒体表达与平台动作。
- 内容需要建委的个人经历或判断时，自动读取 `personal/` 或 `brain/` 的相关来源；只引用有证据的经历，不把通用AI表达当作个人口吻。
- 平台算法、流量规律和效果数字必须重新核验；经验不能写成效果保证。

## 语言质量规则

中文搭配、逻辑和语境统一服从 [`../../../brain/ai-expression/cross-domain-rules.md`](../../../brain/ai-expression/cross-domain-rules.md)。口播和直播任务同时读取 [`../../../brain/ai-expression/oral-expression/README.md`](../../../brain/ai-expression/oral-expression/README.md)；文章和正式图文读取 [`../../../brain/ai-expression/written-expression/README.md`](../../../brain/ai-expression/written-expression/README.md)。本目录不再复制跨领域语言规则。

## 写入规则

- 标题、文章、营销文案、朋友圈、社群话术、口播、直播销售和运营复盘分别归类，不混在一个大文件。
- 分类优先按主要发布渠道，其次按内容目的；同一份材料只保留一个主归属，其他目录只引用。
- 跨平台且不属于单一渠道的推广内容进入 `marketing-copy/`，不要因为内容提到社群或朋友圈就重复存放。
- 同一方法只保留一份；项目文件只引用，不复制。
- 没有真实数据时明确写“待验证”，不编造案例和效果。
- 旧平台技巧失效后退出当前文件，必要时用 Git 历史追溯。

*结构确认：2026-09-07*
