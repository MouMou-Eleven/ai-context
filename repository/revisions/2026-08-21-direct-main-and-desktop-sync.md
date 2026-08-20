# 2026-08-21 直推主分支与桌面结构同步

## 触发原因

仓库长期由建委直接维护。过去遗留的草稿 PR 和历史分支没有及时清理，容易让旧架构、未合并资料和当前 `main` 同时存在；桌面上的仓库结构说明也缺少稳定同步机制。

## 当前规则

- 建委明确要求资料沉淀到 GitHub 时，默认完成清洗、归类、校验后直接提交并推送 `main`。
- 默认不创建 PR，也不等待建委再次下达“提交”或“合并”指令；只有建委明确要求 PR 或暂不提交时例外。
- 旧 PR 中仍有价值的内容必须先迁移到当前目录结构，再关闭 PR 和删除分支，不能把旧一级目录直接合并回主线。
- 已合并、已被 `main` 覆盖或不再需要的远端临时分支应删除，只保留 `main` 作为长期分支。
- `STRUCTURE.md` 是仓库结构的唯一权威来源；桌面 `F:\桌面文件\GitHub仓库完整结构.md` 是其只读镜像。
- 每次结构更新后运行 `repository/maintenance/sync-desktop-structure.ps1`；本机通过 Git Hook 在提交和拉取合并后自动执行。

## 本次旧内容处理

- 草稿 PR #8 的会员社群竞品分析迁入 `work/ai/training/projects/paid-community-course/competitive-references.md`。
- 草稿 PR #9 的原始逐字稿迁入 `brain/ai-expression/chinese-datasets/`，通用表达方法迁入 `brain/ai-expression/experience/`，自媒体专项方法迁入 `work/ai/self-media/experience/`。
- 旧 `expression/`、`projects/` 路径不重新进入主分支。

当前执行规则以 [`AGENTS.md`](../../AGENTS.md) 和 [`repository/maintenance/README.md`](../maintenance/README.md) 为准。
