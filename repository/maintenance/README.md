# Maintenance — 仓库维护工具

## 文件索引

| 文件 | 作用 | 使用时机 |
|---|---|---|
| [`validate-context.ps1`](./validate-context.ps1) | 检查必需入口、项目 README、修订索引、目录索引覆盖和 Markdown 相对链接 | 每次结构调整或提交前运行 |

## 运行方式

```powershell
powershell -ExecutionPolicy Bypass -File repository/maintenance/validate-context.ps1
```

脚本只读取仓库并输出错误，不修改任何文件。退出码为 `0` 表示通过，`1` 表示存在必须处理的问题。
