# 建委认知归组与跨行业内容经营修订

> 日期：2026-08-22
>
> 范围：建委大脑认知结构、商业内容方法、读取路由和来源治理

## 一、修订原因

原 `brain/` 根目录同时放置思维认知、商业认知和 AI 表达入口，层级关系不够清楚。建委要求把思维与商业认知归入同一文件夹，同时保留两类认知各自的职责。

建委提供的《内容即销售：PPT 内容创作者新手版》、交流截图和新视频逐字稿包含内容获客、用户需求、客户筛选和商业承接经验，但不应只服务 PPT 行业，也不能把创作者个人话术、夸张数据和绝对结论直接写入长期仓库。

## 二、结构变化

旧结构：

```text
brain/
├── thinking-and-decisions.md
├── business-cognition.md
└── ai-expression/
```

新结构：

```text
brain/
├── cognition/
│   ├── README.md
│   ├── thinking-and-decisions.md
│   └── business-cognition.md
└── ai-expression/
```

`cognition/` 中文名称为“建委认知”。思维、决策与学习进入思维认知；商业、增长与经营判断进入商业认知；AI 中文质量仍由 `ai-expression/` 独立负责。

## 三、内容方法变化

新增 `work/other/commercial/experience/content-demand-and-conversion.md`，把多个行业案例共同提炼为跨行业方法：

```text
业务任务
→ 用户研究
→ 价值翻译
→ 内容组合
→ 真实测试
→ 合适客户
→ 行动承接
→ 交付反馈
```

具体行业、产品和项目提供事实，本方法只提供可复用机制。PPT、AI、培训、咨询或其他行业调用时，必须叠加一个最具体的行业或项目入口。

## 四、来源取舍

- 保留内容服务业务目标、从真实用户语言识别需求、按商业信号测试、选择适配客户、用真实价值自然说明服务等机制。
- 校正“内容就是销售”“纯知识不挣钱”“只与精准客户对话”“创始人必须亲自做全部内容”等绝对判断。
- 不把播放、点赞、咨询和成交混为一个指标，不把个别低播放高成交案例推导为平台规律。
- 不原样复制 PDF、聊天截图和逐字稿。原材料的公开转载授权没有独立核验，聊天截图还可能包含私人交流；仓库只保存独立提炼、去重和校正后的当前方法。

## 五、涉及文件

- `AGENTS.md`
- `llms.txt`
- `brain/README.md`
- `brain/cognition/README.md`
- `brain/cognition/thinking-and-decisions.md`
- `brain/cognition/business-cognition.md`
- `work/other/README.md`
- `work/other/commercial/README.md`
- `work/other/commercial/experience/README.md`
- `work/other/commercial/experience/content-demand-and-conversion.md`
- `work/ai/self-media/README.md`
- `work/ai/self-media/experience/README.md`
- `work/ai/self-media/experience/media-growth.md`
- `repository/maintenance/validate-context.ps1`
- `repository/revisions/2026-08-20-ai-expression-default-layer.md`
- `repository/revisions/2026-08-21-commercial-delivery-relocation.md`
- `repository/revisions/README.md`
- `STRUCTURE.md`
- `STRUCTURE.html`
