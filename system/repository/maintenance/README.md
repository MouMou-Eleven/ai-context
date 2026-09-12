# 仓库维护工具

Python 3.10+ 标准库是跨平台校验与生成的唯一实现；Windows PowerShell 保留兼容入口。脚本分为只读检查、显式生成和非阻断桌面镜像，不在检查过程中静默修改或暂存文件。

## 常用流程

```text
python -B system/repository/maintenance/context-route.py --task "做MG动画微课，用AI生成镜头" --intent create
python -B system/repository/maintenance/sync-navigation.py
python -B system/repository/maintenance/sync-structure.py
python -B system/repository/maintenance/validate-context.py
python -B -m unittest discover -s system/repository/maintenance/tests -v
```

`context-route.py` 只解释候选与依赖，不执行工具，不把关键词匹配当成课程或项目归属证据。写入完成后依次生成导航与结构，复核变化，再明确暂存本次文件。检查时使用 `--check` 查看导航或结构漂移；校验器有 `--json` 供机器读取。

结构发生实际变化并完成核对时，AI 同步将 `structure-descriptions.json` 的 `confirmedDate` 更新为本次确认日期；没有结构变化时保持原日期，不因每天运行或 CI 当前时间改变生成结果。新目录用途需要更精确说明时，由 AI 在同一描述表补充，旧路径说明由生成器自动移除。

## 文件索引

| 文件 | 作用 |
|---|---|
| [context-route.py](./context-route.py) | 从路由注册表解释自然任务的入口与条件依赖 |
| [sync-navigation.py](./sync-navigation.py) | 从注册表生成短llms、任务指南、项目案例总表及领域关联区块，支持只读漂移检查 |
| [sync-structure.py](./sync-structure.py) | 从同一真实文件树生成完整结构与日常知识导航，保留有效中文描述 |
| [structure-descriptions.json](./structure-descriptions.json) | 结构树中文说明与确认日期；不存放第二份项目状态 |
| [structure-viewer.template.html](./structure-viewer.template.html) | 沿用的 HTML 展开、折叠、搜索、导航与本地状态界面 |
| [validate-context.py](./validate-context.py) | 校验必需入口、旧路径、Markdown链接、最近README索引、路由路径、Skill来源与能力、敏感线索、重复内容及全部生成漂移 |
| [validation-policy.json](./validation-policy.json) | 四主目录、必需入口、关键发现链接及废弃路径检查 |
| [context_common.py](./context_common.py) | 实际文件清单、Markdown链接、快照边界与脚本加载的共用实现 |
| [pre-commit.py](./pre-commit.py) | 导出 Git 暂存区到临时目录，在同一快照内运行校验与回归，不修改实际索引 |
| [desktop-sync.py](./desktop-sync.py) | Windows桌面镜像，仅复制已存在的仓库HTML并核对hash；其他平台或桌面不可用时不阻断 |
| [validate-context.ps1](./validate-context.ps1) | Windows旧命令的只读兼容入口 |
| [invoke-python.ps1](./invoke-python.ps1) | Windows兼容入口共用的Python版本与可执行性探测，跳过空别名 |
| [generate-structure-html.ps1](./generate-structure-html.ps1) | Windows显式生成兼容入口，内部使用同一个Python生成器 |
| [sync-desktop-structure.ps1](./sync-desktop-structure.ps1) | 手动生成并同步桌面旧命令，含目标路径、重试与严格模式 |
| [tests/](./tests/README.md) | 路由、坏链接、漏索引、元数据、生成漂移与暂存隔离的行为回归 |
| [.gitignore](.gitignore) | 排除本目录Python字节码缓存 |
| [git-hooks/pre-commit](./git-hooks/pre-commit) | 选择可用Python，执行暂存区检查；从不git add |
| [git-hooks/run-python](./git-hooks/run-python) | 实际探测Python 3.10+，跳过Windows Store空别名，供所有Git hooks共用 |
| [git-hooks/post-commit](./git-hooks/post-commit) | 提交后非阻断复制桌面镜像 |
| [git-hooks/post-merge](./git-hooks/post-merge) | 合并后非阻断复制桌面镜像 |
| [git-hooks/post-checkout](./git-hooks/post-checkout) | 检出后非阻断复制桌面镜像 |
| [git-hooks/post-rewrite](./git-hooks/post-rewrite) | 改写后非阻断复制桌面镜像 |

## 检查边界

- 实际目录树以Git跟踪文件及未忽略的新文件为准，排除`.git`、Python字节码及被忽略的临时文件。完整文件视图包含上游快照内部层级，可折叠查看；日常知识树只显示Skill能力入口。
- 每个普通文件必须被最近一层 README 索引；子目录 README 也须被上层入口索引。原有相对链接、反引号文件清单和树状清单均可识别。
- 第三方完整快照只有 `upstream.json` 中已明确登记的 `sourcePath` 内部可豁免本仓库的README索引约定；包装层仍校验，内部相对链接仍检查。自研Skill不使用此豁免。
- 校验四个知识主目录、当前必需入口、旧路径、关键发现链接、Skill元数据、敏感线索与重复内容。独立项目、案例和归档项目必须有登记，领域关系指向真实领域README。路径检查不证明业务事实。
- 生成漂移检查比较完整生成结果，不能只把当前hash写进旧HTML就通过。文件增删、模板变化、注册表变化、描述变化和HTML内容被改都会触发检查。
- 根技术文件由`validation-policy.json`明确指定系统仓库README为索引负责人，日常首页只展示四主入口；普通正文仍遵守最近README索引。
- 校验不能证明平台功能、授课经历或商业事实真实；这类判断仍需来源、日期与明确归属。自动化结果不替代内容审查。

## 暂存区与 CI

本地启用：`git config core.hooksPath system/repository/maintenance/git-hooks`。提交前检查导出**整个暂存区**，包含暂存的规则、脚本与生成物；未暂存修复不能遮住暂存区错误，未暂存新文件也不会被顺手提交。生成内容引用了未暂存的新文件或输入时，暂存快照会缺链接或出现漂移，提交被阻止。

已审查的旧版本可以单独提交，只要它在暂存区自洽。脚本不要求用户把无关工作区改动一并提交。失败后应修复具体问题、重新生成并明确暂存相匹配的输入与输出；不使用自动 `git add`。

[GitHub CI](../../../.github/README.md)在Linux和Windows运行同一校验与回归。本地hook提供即时反馈，CI防止未安装hook的环境漏检；启用分支保护需仓库设置另行配置。

## 桌面镜像

Git hooks中的桌面同步只复制 `system/repository/navigation/STRUCTURE.html`，不重写仓库生成物；Windows桌面不可用时记录延后，后续Git操作再次尝试。手动兼容命令 `powershell -ExecutionPolicy Bypass -File system/repository/maintenance/sync-desktop-structure.ps1` 会显式生成再同步；加 `-Strict` 可将桌面不可用视为错误。
