# SEO与公开内容整改

> 来源：从原 [prompt-patterns.md](../prompt-patterns.md) 的实战模板按主题整理，原始版本由Git历史保留；2026-09-12仅拆分与明确适用边界，未重新实测秒哒产品能力。
> 模板中的页面名、接口、路径和配置是对应案例条件；执行前替换为当前项目已核验事实。查看模板不代表已授权收费、部署或外部发送。

> SEO模板记录该项目要求的字段完整性，不把keywords填写推断成搜索引擎排名收益；组件依赖与页面名单按当前工程核验。

### 片段 8：全站 SEO 优化不漏 keywords

**背景**：一次真实对话里，第一轮让秒哒“做 SEO”后，它完成了 `index.html`、`useSEO`、`robots.txt`、`sitemap.xml` 和 Settings 的部分改动；第二轮继续追问每个页面的 `keywords` 是否都补齐，才改成 `SEOHead` + `react-helmet-async` 的统一管理方式。经验是：SEO 必须按“页面矩阵 × 字段矩阵”验收。

**适用场景**：秒哒生成的 React/Vite 网站需要补全站 SEO，尤其是有 Home / Navigate / About / Feedback 这类多页面路由时。

**提示词**：

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

完整处方见 [patterns/seo-optimization.md](../patterns/seo-optimization.md)。

### 片段 9：内容整改 / 备案主体一致性提示词要像执行任务

**背景**：一次真实网站备案整改里，第一版提示词写了“第 0 批：整改前检查”、网站链接、“你是百度秒哒 MIAODA 项目内置开发助手”、“不要依赖上一轮对话记忆”等说明。用户反馈这些对秒哒没有意义：秒哒是在当前云端项目里直接执行，提示词应直接告诉它本批改什么、怎么改、哪些不能动。修订后删掉纯检查批，改成从最高风险的 SEO/分享隐藏文案开始分批执行。

**适用场景**：备案主体一致性、品牌主体口径、协会/合作方页面、人物介绍、商品详情经营主体、公开栏目名称等“只改内容不改后端”的整改任务。

**核心写法**：

```text
请严格、严谨、认真、负责地完成本批备案主体一致性整改。不要编造，不要夸大，不要把未确认关系写成确定事实，不要自行扩展任务。

本批只修改站点名称、SEO、分享卡片、结构化数据、秒哒分享配置、站点设置中的公开文字。

严禁修改：
- 数据库结构
- 数据库记录
- API / 接口
- Edge Function
- 支付、登录、订单、购物车、退款、地址管理
- 商品数据、价格、库存、图片
- 页面布局和路由结构

备案主体统一为：
<公司全称>

网站定位统一为：
<公司全称>主办并运营的<业务定位>。

请全项目搜索并替换以下高风险表述：
<风险词清单>

完成后请只输出：
1. 修改了哪些文件或配置。
2. 高风险词是否仍有残留；如有，请列出残留位置。
3. 是否未修改数据库、接口、支付、登录、订单等后端能力。
完成后停止。
```

**不要写**：

- 不要默认加“第 0 批检查”，除非用户当前只想诊断。
- 不要用“你是百度秒哒内置开发助手”开头。
- 不要把网站链接当任务背景塞进去；当前项目上下文里通常不需要。
- 不要写“不要依赖上一轮对话记忆”，要靠每批重复主体口径、边界和红线来实现自包含。
- 不要把整改方案写成给人看的报告；提示词要像可执行工单。

完整处方见 [patterns/content-rectification-prompts.md](../patterns/content-rectification-prompts.md)。
