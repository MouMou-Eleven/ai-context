# References — 执行级参考资料索引

> 本目录保存可复用规范、源码和原始参考。它们通常比知识说明更具体，但不自动代表当前业务事实。

## 文件索引

| 入口 | 内容 | 何时读取 |
|---|---|---|
| [`feishu-doc-style.md`](./feishu-doc-style.md) | 飞书文档的视觉结构、callout、图表和时间落款规范 | 创建或改写飞书文档时 |
| [`writing-style/feitian-shanke/`](./writing-style/feitian-shanke/) | 飞天闪客技术科普逐字稿、来源说明与去 AI 味写作方法提炼 | 编写课程、文章、视频口播稿或向普通人解释技术概念时 |
| [`video-chunked-upload/`](./video-chunked-upload/) | 旧秒哒后端环境生产验证过的永久分片与 Range 代理兼容源码 | 当前环境 200MB 能力测试仍出现 CORS / 413 / supervisor kill 时再读 |
| [`creative-frontend-prompts/`](./creative-frontend-prompts/) | 五类创意前端完整提示词原文，覆盖视频逐帧、空间画廊、个人作品集与 3D 首屏 | 设计动效密集型展示站并需要查阅执行级样例时 |

## 使用边界

- 先读调用方知识文件，理解适用场景和约束，再使用这里的参考实现。
- 源码标记“必须照抄”的部分不得让 AI 自由重写；环境变量和业务表结构仍需按当前项目核对。
- 新增参考包时必须包含 README，写清来源、验证状态、不可变约束和已知边界。
- 原始附件若已被 Markdown 新版取代，必须在最近一层 README 标成历史材料。

*索引最后整理：2026-07-23*
