# GitHub 自动校验说明

> 这里是 GitHub Actions 的维护说明，不是 AI Context 仓库首页。

仓库日常首页请返回[根目录 README](../README.md)；分级浏览请打开[日常知识导航](../system/repository/navigation/STRUCTURE.html)。

- [workflows/context-validation.yml](./workflows/context-validation.yml)：在 Linux 和 Windows 上执行同一套标准库校验与行为测试，检查 `main` 推送及 PR。
- [维护入口](../system/repository/maintenance/README.md)：本地检查、生成、暂存和直接推送规则。

CI 只校验，不生成提交或修改仓库。
