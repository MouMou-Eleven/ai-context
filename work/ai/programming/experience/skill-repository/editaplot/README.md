# EditaPlot

EditaPlot 是面向科研绘图的 Agent Skill，通过 Origin/OriginPro 创建和编辑可复现图表。本目录保存的不是链接或孤立的 `SKILL.md`，而是上游仓库的完整已跟踪文件快照。

## 固定版本

- 上游仓库：<https://github.com/hang-jin/editaplot>
- 默认分支：`main`
- 当前 commit：`4aa986f3f84da9cb2a2297159a8f20e42b7e527c`
- 许可证：Apache-2.0
- 来源记录：[`upstream.json`](./upstream.json)
- 完整快照：[`source/`](./source/)
- Skill 入口：[`source/skill/editaplot/SKILL.md`](./source/skill/editaplot/SKILL.md)

之所以保存完整快照，是因为 EditaPlot 的 `skill/editaplot/` 还依赖仓库根目录的 `runtime/` 和 `editaplot.cmd`。只复制 Skill 子目录会缺失绘图运行时，无法按上游设计工作。

## 使用前提

- 上游当前声明支持 Windows 10/11 x64 物理机。
- 需要 Origin/OriginPro 2021–2026b；上游完整基准版本为 Origin 2024b。
- 在 `source/` 根目录按上游说明运行 `./editaplot.cmd setup`，安装完成后调用 `$editaplot`。

具体能力、命令和限制以固定快照内的上游 [`README.md`](./source/README.md) 与 [`SKILL.md`](./source/skill/editaplot/SKILL.md) 为准。

## 更新方法

1. 从 `upstream.json` 读取上游地址和当前 commit，抓取 `main` 最新状态。
2. 审查 commit 差异、许可证、依赖锁文件和 Origin 支持范围。
3. 用新 commit 的全部已跟踪文件替换 `source/`，不得只更新 `skill/editaplot/`。
4. 更新 `upstream.json` 和本页固定版本，再运行仓库校验及上游测试。

`source/` 是上游快照，不直接手改；本地适配应另建补丁并留下修订记录。
