# AI Publishing — AI 书籍出版

> 保存 AI 相关书籍的选题、写作、编辑、截图、事实核验、设计交接和出版项目。

## 目录结构

```text
publishing/
├── README.md
└── projects/
    └── feishu-efficient-office/
```

## 当前项目

| 项目 | 入口 | 状态 |
|---|---|---|
| 《飞书高效办公》 | [`projects/feishu-efficient-office/`](./projects/feishu-efficient-office/README.md) | 进行中 |

## 激活边界

- 生成书稿中文内容时，先读 [`../../../brain/ai-expression/README.md`](../../../brain/ai-expression/README.md) 短卡，再读出版项目短规则；详细表达、编辑和交稿规则按任务读取。
- 书稿内容、编辑反馈、章节和产品事实进入本目录。
- 书籍视觉版式进入 [`../../design/book-design/`](../../design/book-design/README.md)。
- 只提“文章、自媒体”时不读取书籍出版。
- 飞书菜单、按钮和功能路径必须重新核验官方资料或实际界面。

## 语言质量规则

中文默认从AI表达README短卡进入；详细质量规则按需引用 [`../../../brain/ai-expression/cross-domain-rules.md`](../../../brain/ai-expression/cross-domain-rules.md) 和 [`../../../brain/ai-expression/written-expression/README.md`](../../../brain/ai-expression/written-expression/README.md)。本目录只保留出版专项规则，不重复维护通用语言搭配。

《飞书高效办公》的唯一上下文在 `projects/feishu-efficient-office/`；正文、章节目录、历史旧章与本地Word的位置由其README区分。新增书籍建立独立项目与README，不把培训课程或设计订单混入书稿。
