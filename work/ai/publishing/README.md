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

- 生成书稿中文内容时，先调用 [`../../../brain/ai-expression/`](../../../brain/ai-expression/README.md) 的书面化和跨领域规则，再叠加出版项目的写作、编辑与事实核验要求。
- 书稿内容、编辑反馈、章节和产品事实进入本目录。
- 书籍视觉版式进入 [`../../design/book-design/`](../../design/book-design/README.md)。
- 只提“文章、自媒体”时不读取书籍出版。
- 飞书菜单、按钮和功能路径必须重新核验官方资料或实际界面。

## 语言质量规则

跨领域中文质量统一服从 [`../../../brain/ai-expression/cross-domain-rules.md`](../../../brain/ai-expression/cross-domain-rules.md) 和 [`../../../brain/ai-expression/written-expression/README.md`](../../../brain/ai-expression/written-expression/README.md)。本目录只保留出版专项规则，不重复维护通用语言搭配。
