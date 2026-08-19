# Design — 设计工作领域

> 设计是建委的核心专业门类。这里按最终交付物分类，不按是否使用 AI 分类。

## 目录结构

| 方向 | 入口 | 保存内容 |
|---|---|---|
| PPT 设计 | [`ppt-design/`](./ppt-design/README.md) | 商务演示、汇报、课程与课件视觉 |
| 海报折页设计 | [`poster-fold-design/`](./poster-fold-design/README.md) | 海报、折页、易拉宝、KV和平面视觉 |
| 书籍设计 | [`book-design/`](./book-design/README.md) | 书籍版式、图文编排、封面与印刷阅读 |
| 微课与 MG 动画设计 | [`microcourse-mg-animation/`](./microcourse-mg-animation/README.md) | 微课、精品课、MG动画、VR和交互课件 |
| AE 宣传视频设计 | [`ae-promo-video/`](./ae-promo-video/README.md) | AE包装、信息动画和宣传视频视觉设计 |
| AI 设计 | [`ai-design/`](./ai-design/README.md) | AI参与的视觉设计流程、生成与人工精修 |

## 分类原则

- AI 设计仍属于设计，因为核心交付是视觉方案，AI 只是生产方式。
- AI 视频制作属于 `../ai/video/`，因为它以生成式视频工作流和视频成片为核心。
- AI 培训课件的教学结构属于 `../ai/training/`；课件视觉方法属于本目录的 PPT 或相关设计方向。
- 同一案例指定一个主归属，其他方向只保留链接，不复制正文。

## 写入规则

- 生成 PPT、海报、书籍、微课或视频中的中文标题、正文、旁白和案例说明时，默认先调用 [`../../brain/ai-expression/`](../../brain/ai-expression/README.md)，再叠加对应设计门类。
- 新资料先判断最终交付物，再进入对应方向。
- 当前没有成熟资料的方向只在 README 中记录边界，不编造经验和项目。
- 形成两个以上重复案例后，再提炼通用方法；单个客户过程留在具体项目。
- 客户隐私、未公开素材和可识别内部信息不得写入仓库。

*分类确认：2026-08-18*
