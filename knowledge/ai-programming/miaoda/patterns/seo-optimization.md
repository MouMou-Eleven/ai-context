# 秒哒站点 SEO 优化处方

> 来源：2026-06-09 与秒哒的一次 SEO 优化对话截图。场景是对秒哒生成的 React/Vite 单页站点做全站 SEO，第一次只做了 `index.html`、`useSEO` 与基础 meta，第二次发现 `keywords` 仍可能漏掉，改为用统一 `SEOHead` 组件收口。

## 适用场景

| 场景 | 是否适用 |
|---|---|
| 秒哒生成的网站需要补 `title` / `description` / `keywords` | ✅ 用 |
| React SPA 有多个页面或路由，切换页面后 `<head>` 需要变化 | ✅ 用 |
| 网站有后台设置项，如 `site_description`、`site_keywords` | ✅ 用 |
| 只是一个纯静态 HTML 页面，没有路由 | 可简化，只改 `index.html` |

## 核心结论

秒哒做 SEO 时，**不要只让它改 `index.html` 或写一个散落的 `useSEO` hook**。React SPA 里用户切到不同页面后，真实生效的是运行时 `<head>` 状态；如果没有统一组件管理，最容易漏的是 `meta[name="keywords"]`。

更稳的做法是：

1. `index.html` 写站点级兜底 `title`、`description`、`keywords`。
2. 用 `react-helmet-async` 包住应用。
3. 建一个统一 `SEOHead` 组件，接收 `title`、`description`、`keywords`。
4. 每个路由页面都显式渲染 `SEOHead`，不要靠口头约定。
5. 后台配置里补 `site_keywords`，和 `site_description` 一起进入页面 SEO 计算。
6. 检查 `robots.txt`、`sitemap.xml`，确保核心页面可被抓取。

## V3.5 内置 SEO Agent

> 来源：[秒哒 3.5 官方发布文章](https://mp.weixin.qq.com/s/y2_ip4MYlJQPpTJ2a_O26A?scene=1)，2026-07-16。

V3.5 新增 SEO Agent。它可以预览页面在搜索结果中的标题、摘要和链接展示，逐页检查 `title`、`description`、`keywords` 等要素，把问题转成可理解的建议，并支持单项修复、一键修复和重新检查。

这与本文件的代码级 SEO 处方不冲突：SEO Agent 适合作为第一轮诊断和基础修复；React SPA 的路由级 `<head>`、`keywords` 覆盖、`robots.txt`、`sitemap.xml` 仍应按本文件的验收矩阵复核。官方文章没有说明 Agent 会自动处理这些工程细节，不能仅凭“已一键修复”就跳过验收。

推荐顺序：先用 SEO Agent 诊断并修复，再执行本文件「验收清单」的逐页检查；只要有一页 `keywords`、描述或标题为空，就继续按本文件的统一 `SEOHead` 方案补齐。

## 推荐文件改动清单

| 文件 | 目的 |
|---|---|
| `index.html` | 站点级兜底 SEO：`title`、`meta description`、`meta keywords` |
| `src/main.tsx` / `src/App.tsx` | 增加 `HelmetProvider` |
| `src/components/SEOHead.tsx` | 统一管理页面级 head meta |
| `src/pages/Home.tsx` | 首页根据站点设置、分类名、数据关键词生成 SEO |
| `src/pages/Navigate.tsx` | 导航页设置独立 title / description / keywords |
| `src/pages/About.tsx` | 关于页设置独立 title / description / keywords |
| `src/pages/Feedback.tsx` | 反馈页设置独立 title / description / keywords |
| `src/pages/Settings.tsx` | 增加 `site_keywords` 设置项，并保存/加载 |
| `public/robots.txt` | 确认允许搜索引擎抓取公开页面 |
| `public/sitemap.xml` | 列出核心公开路径，后续新路由要同步更新 |

## SEOHead 组件契约

组件可以很简单，但字段必须完整，尤其不能漏 `keywords`：

```tsx
import { Helmet } from "react-helmet-async";

type SEOHeadProps = {
  title: string;
  description: string;
  keywords: string;
};

export function SEOHead({ title, description, keywords }: SEOHeadProps) {
  return (
    <Helmet>
      <title>{title}</title>
      <meta name="description" content={description} />
      <meta name="keywords" content={keywords} />
    </Helmet>
  );
}
```

如果项目已有 `useSEO` hook，不必强行删除；但最终要确认它不是只改 `title` / `description`。最佳做法是让页面层直接渲染 `SEOHead`，避免 hook 内部逻辑分散导致漏字段。

## 每页关键词策略

| 页面 | keywords 来源 |
|---|---|
| Home | `site_keywords` + 当前分类名 `selectedCategoryName` + 数据中的内容关键词 |
| Navigate | 站点关键词 + 导航页业务词，如资源导航、工具导航、分类导航 |
| About | 站点关键词 + 品牌/个人/项目介绍相关词 |
| Feedback | 站点关键词 + 反馈、建议、用户交流、联系等词 |

关键词不要只堆同义词。优先保留三类：

- 站点品牌词或产品名
- 页面主题词
- 用户真实会搜索的长尾词

## robots 与 sitemap 检查

基础版本：

```txt
User-agent: *
Allow: /

Sitemap: https://your-domain.com/sitemap.xml
```

`sitemap.xml` 至少列出：

```xml
<url><loc>https://your-domain.com/</loc></url>
<url><loc>https://your-domain.com/navigate</loc></url>
<url><loc>https://your-domain.com/about</loc></url>
<url><loc>https://your-domain.com/feedback</loc></url>
```

如果还没绑定正式域名，先让秒哒用占位域名生成，但要在上线后提醒替换为真实域名。

## 验收清单

让秒哒改完后，不要只看它的 Summary，要要求它逐页回报检查结果：

| 检查项 | 验收方式 |
|---|---|
| 首页 title | 打开首页后 `document.title` 正确 |
| 首页 description | `document.querySelector('meta[name="description"]')?.content` 非空 |
| 首页 keywords | `document.querySelector('meta[name="keywords"]')?.content` 非空 |
| Navigate 页面 | 切到页面后 title / description / keywords 都变化 |
| About 页面 | 切到页面后 title / description / keywords 都变化 |
| Feedback 页面 | 切到页面后 title / description / keywords 都变化 |
| Settings 保存 | `site_keywords` 能保存、刷新后仍存在 |
| robots/sitemap | 文件存在，域名与路径正确 |

## 可直接喂秒哒的提示词

```text
我现在需要你对整个网站做一次完整 SEO 优化，请打起十二分的精神专心执行。

红线（必须遵守）：
- 不要只改 index.html，React 页面切换后的 head 也必须正确。
- 不要只处理 title 和 description，keywords 必须每个页面都有。
- 不要在每个页面散落重复 DOM 操作，必须用统一 SEOHead 组件或等价统一入口管理。
- 不要破坏现有路由、数据加载、分类筛选、反馈提交、后台设置保存逻辑。

目标：
1. 安装并使用 react-helmet-async（如果项目已安装则复用）。
2. 在应用根部增加 HelmetProvider。
3. 新建 src/components/SEOHead.tsx，统一输出 title、description、keywords。
4. index.html 中补齐站点级兜底 title、description、keywords。
5. Home、Navigate、About、Feedback 每个页面都必须渲染 SEOHead。
6. Settings 中新增 site_keywords 配置项，和已有 site_description 一起保存、加载、回显。
7. Home 页 SEO 要能结合 site_keywords、当前分类名 selectedCategoryName、站点数据关键词生成。
8. 检查 robots.txt 和 sitemap.xml；没有就创建，有就补全核心路径。

验收要求：
改完后请逐页检查并回报表格，列出每个页面实际生效的 title、description、keywords。
尤其检查 meta[name="keywords"]，不能为空，不能只在首页存在。
```

## 反面提示词

```text
帮我做一下 SEO。
```

为什么不稳：秒哒通常会先改 `index.html` 和一部分 meta，看起来 Summary 很完整，但页面级 `keywords`、路由切换后的 head、后台关键词配置很容易漏。

## 对话复盘

这次截图里，第一轮秒哒做了基础 SEO：

- 优化 `index.html`
- 创建 `useSEO` hook
- 在 Home / Navigate / About / Feedback 等页面接入 SEO
- 检查 `robots.txt` 和 `sitemap.xml`
- 在 Settings 增加 `site_keywords`

第二轮继续追问“每个页面、关键词 keywords 是否全部添加，避免漏掉”后，秒哒才进一步：

- 新建 `SEOHead` 组件，用 Helmet 统一管理
- 将各页面从分散的 `useSEO` 调用收口到 `<SEOHead />`
- 一次性补全缺失的 `keywords` / `description`
- 对 Home、Navigate、About、Feedback 逐页检查

沉淀下来的经验：**SEO 优化要按“页面矩阵 + 字段矩阵”验收，而不是按“我已经做了 SEO”验收。页面矩阵是 Home / Navigate / About / Feedback；字段矩阵是 title / description / keywords。两个矩阵交叉处都非空，才算完成。**
