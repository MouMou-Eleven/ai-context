# Maintenance — 仓库维护工具

## 文件索引

| 文件 | 作用 | 使用时机 |
|---|---|---|
| [`validate-context.ps1`](./validate-context.ps1) | 检查必需入口、工作层级、旧目录残留、Markdown 相对链接和敏感信息线索 | 每次结构调整或提交前运行 |
| [`sync-desktop-structure.ps1`](./sync-desktop-structure.ps1) | 将权威 `STRUCTURE.md` 原样同步到 `F:\桌面文件\GitHub仓库完整结构.md` 并核对 SHA-256 | 每次结构调整后；本机提交或合并后由 Git Hook 自动运行 |
| [`git-hooks/post-commit`](./git-hooks/post-commit) | 提交完成后触发桌面结构同步 | 本机已通过 `core.hooksPath` 启用 |
| [`git-hooks/post-merge`](./git-hooks/post-merge) | 拉取或合并完成后触发桌面结构同步 | 本机已通过 `core.hooksPath` 启用 |

## 运行方式

```powershell
powershell -ExecutionPolicy Bypass -File repository/maintenance/validate-context.ps1
```

脚本只读取仓库并输出错误，不修改任何文件。退出码为 `0` 表示通过，`1` 表示存在必须处理的问题。

## 桌面结构同步

权威结构始终是仓库根目录的 [`../../STRUCTURE.md`](../../STRUCTURE.md)。桌面文件只是镜像，禁止单独编辑；结构变化必须先更新仓库，再运行：

```powershell
powershell -ExecutionPolicy Bypass -File repository/maintenance/sync-desktop-structure.ps1
```

本机仓库配置使用 `repository/maintenance/git-hooks/` 作为 Git Hook 路径。提交或拉取合并后会自动刷新桌面镜像；脚本使用 SHA-256 验证源文件与桌面文件完全一致。
