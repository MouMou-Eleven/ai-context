# AI Self-Media — AI 自媒体

> 本目录保存 AI 相关自媒体的标题、文章、口播视频、直播销售和运营经验。它是独立领域，不属于 AI 培训，也不代表建委个人通用表达。

## 目录结构

```text
self-media/
├── README.md       总入口与激活边界
├── titles/         标题与选题
├── articles/       图文与文章
├── video-scripts/  口播视频与脚本结构
├── live-sales/     直播销售与内容承接
└── experience/     账号、内容、测试和复盘经验
```

## 读取路由

| 任务 | 首读 |
|---|---|
| 标题、选题、开头 | [`titles/README.md`](./titles/README.md) |
| 图文、文章、公众号内容 | [`articles/README.md`](./articles/README.md) |
| 短视频口播和脚本 | [`video-scripts/README.md`](./video-scripts/README.md) |
| 直播销售、评论关键词、资料与社群承接 | [`live-sales/README.md`](./live-sales/README.md) |
| 账号规划、内容测试和复盘 | [`experience/README.md`](./experience/README.md) |

## 严格激活规则

- 只提“AI 自媒体、标题、口播、短视频、直播销售”时，只读取本目录。
- 不自动读取 [`../training/`](../training/README.md)、付费社群项目或建委大脑。
- 内容要为某个具体项目服务时，建委需明确项目名称，再组合对应项目 README。
- 需要使用建委个人说话习惯时，建委需明确说“结合我的个人表达”，再读取 `brain/personal-expression.md`。
- 平台算法、流量规律和效果数字必须重新核验；经验不能写成效果保证。

## 语言质量规则

口播和直播销售要像真实交流，但不能为了口语化牺牲中文搭配。引出观点时用“先给大家说一个真实观点”“先说结论”，不要使用“先把话说稳一点”这种语病表达；具体痛点要用“解决掉、判断下一步、处理好”等动作表达，不把“接住”泛化成解决问题。完整修订记录见 [`repository/revisions/2026-08-20-language-precision.md`](../../../repository/revisions/2026-08-20-language-precision.md)。

## 写入规则

- 标题、文章、口播、直播销售和运营复盘分别归类，不混在一个大文件。
- 同一方法只保留一份；项目文件只引用，不复制。
- 没有真实数据时明确写“待验证”，不编造案例和效果。
- 旧平台技巧失效后退出当前文件，必要时用 Git 历史追溯。

*结构确认：2026-08-18*
