# 2026-06-20 付费社群课程项目首次入库

## 背景

建委正在研发一个付费社群课程项目，当前价格为 399 元 / 3 个月，交付包括直播、课程和教程文档。首期准备往 AI 编程方向研发。

同一时间，建委提供了一篇关于 Codex 插件市场灰色、通过 Codex++ 解锁插件市场的教程素材，要求整理成飞书文档，供付费社群成员查看。

## 本次确认的边界

- GitHub 上下文仓库记录的是“建委正在做付费社群课程研发”这件长期项目。
- 具体的 Codex++ 插件解锁教程正文写入飞书文档，不写入本仓库。
- 仓库需要为后续课程研发、自媒体资料、口播稿方法、账号规划等内容预留稳定入口。
- 自媒体是该付费社群课程的重要流量入口，需要单独沉淀为长期资料。

## 本次新增结构

- `projects/paid-community-course/README.md`
- `projects/paid-community-course/course-development.md`
- `projects/paid-community-course/media-growth.md`
- `projects/paid-community-course/revisions/2026-06-20-initial-project-boundary.md`

## 后续维护原则

- 课程方向、交付体系、教程选题标准：更新 `course-development.md`。
- 自媒体账号规划、选题、口播稿、文案套路：更新 `media-growth.md`，内容变多后再拆分子文件。
- 重要方向变化：新增 `revisions/YYYY-MM-DD-{slug}.md`，不要无痕覆盖历史口径。
