# EditaPlot

EditaPlot 是面向科研绘图的 Agent Skill，通过 Origin/OriginPro 创建和编辑可复现图表。本目录保存的不是链接或孤立的 `SKILL.md`，而是上游仓库的完整已跟踪文件快照。

## 能力与适用边界

- 来源：**第三方Skill，非建委自研**。作者与运行行为以 [hang-jin/editaplot](https://github.com/hang-jin/editaplot) 的固定快照为准。
- 输入真实实验表格，解释列用途、推荐图形、按确认的科学目的调用Origin；交付可编辑OPJU和PNG/PDF/TIF，附对象回读与视觉检查。
- 适用于科研图、Origin/OriginPro图表制作和已有图编辑。不替用户确定科学结论，不擅自补数据或拟合；参考图仅提取有数据支撑的图形语法，不承诺任意图片复刻。
- 无受支持Windows实体机或Origin时，只能整理方案与数据需求，不能报告完整Origin成图已完成。

## 查看与执行

查能力只读本页和 [upstream.json](./upstream.json)。制作时再读实体Skill，检查本机安装版本、Python与Origin、数据列义和所需授权，再执行对应流程。本仓快照不证明当前电脑已经安装或本轮运行通过。

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
- 需要 Origin/OriginPro 2021–2026b（兼容目标）；上游完整基准版本为 Origin 2024b。
- 上游标明Python 3.10–3.12；完整运行时和安装依赖由 `source/` 中的setup检查。
- 在 `source/` 根目录按上游说明运行 `./editaplot.cmd setup`，安装完成后调用 `$editaplot`。

具体能力、命令和限制以固定快照内的上游 [`README.md`](./source/README.md) 与 [`SKILL.md`](./source/skill/editaplot/SKILL.md) 为准。

## 更新方法

1. 从 `upstream.json` 读取上游地址和当前 commit，抓取 `main` 最新状态。
2. 审查 commit 差异、许可证、依赖锁文件和 Origin 支持范围。
3. 用新 commit 的全部已跟踪文件替换 `source/`，不得只更新 `skill/editaplot/`。
4. 更新 `upstream.json` 和本页固定版本，再运行仓库校验及上游测试。

`source/` 是上游快照，不直接手改；本地适配应另建补丁并留下修订记录。

能力或版本更新同时维护本页、元数据与 [Skill总索引](../README.md)。说明整理日2026-09-12；实体仍为2026-09-01登记的固定commit，未在本轮安装或运行。
