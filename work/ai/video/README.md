# AI Video — AI 视频制作

> 本目录按“通用经验、视频类型、生成工具、具体项目”组织，避免把宣传片、漫剧、真人故事和某个模型的经验混在一起。

## 目录结构

```text
video/
├── README.md   AI 视频总入口
├── common/     跨片型通用制作经验
├── types/      按最终视频类型分类
├── tools/      按生成模型或工具分类
└── projects/   具体客户或长期项目
```

## 读取路由

| 任务 | 首读 |
|---|---|
| 通用流程、素材、分镜和验收 | [`common/README.md`](./common/README.md) |
| 漫剧 | [`types/motion-comic/README.md`](./types/motion-comic/README.md) |
| 企业宣传片 | [`types/enterprise-promo/README.md`](./types/enterprise-promo/README.md) |
| 真人实拍故事、电影或电视叙事 | [`types/live-action-story/README.md`](./types/live-action-story/README.md) |
| Seedance | [`tools/seedance/README.md`](./tools/seedance/README.md) |
| 具体 AI 视频项目 | [`projects/README.md`](./projects/README.md) |

## 分类原则

- 先判断片型，再选择工具；不能用某个模型的经验代替片型方法。
- 企业宣传片重信息、品牌和包装；真人故事重角色、场景、动作、情绪和摄影；漫剧有自己的角色连续性、分镜和节奏规则。
- AE 图形包装属于设计门类；当它服务 AI 视频项目时，只组合所需的设计方法。
- 模型版本、参数和平台能力必须重新核验。

## 严格激活

- 只提一种片型时，只读取该片型和必要的通用经验。
- 只有明确使用某个模型时才读取对应工具目录。
- 生成中文脚本、旁白、字幕或项目说明时，默认叠加 [`../../../brain/ai-expression/`](../../../brain/ai-expression/README.md)；不自动加载其他片型、AI 培训或自媒体。

*结构确认：2026-08-18*
