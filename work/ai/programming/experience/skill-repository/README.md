# Skill 仓库

> 收录可直接读取或安装的 Skill 实体，不把这里只做成 GitHub 地址清单。

## 当前收录

| Skill | 实体入口 | 来源与更新信息 | 用途 |
|---|---|---|---|
| jianwei-ai-community-remotion-video | [`jianwei-ai-community-remotion-video/skill/SKILL.md`](./jianwei-ai-community-remotion-video/skill/SKILL.md) | [`jianwei-ai-community-remotion-video/upstream.json`](./jianwei-ai-community-remotion-video/upstream.json) | 先导演记忆点、反差、重叠节奏与最终帧，再默认生成可编辑文字、编号和颜色的参数化 Remotion 工程 |
| EditaPlot | [`editaplot/source/skill/editaplot/SKILL.md`](./editaplot/source/skill/editaplot/SKILL.md) | [`editaplot/upstream.json`](./editaplot/upstream.json) | 通过 Origin/OriginPro 制作与编辑科研图表；本仓保存完整运行仓库快照 |
| jianwei-ai-learning-community-workbench | [`jianwei-ai-learning-community-workbench/skill/SKILL.md`](./jianwei-ai-learning-community-workbench/skill/SKILL.md) | [`jianwei-ai-learning-community-workbench/upstream.json`](./jianwei-ai-learning-community-workbench/upstream.json) | 根据任意身份通过少轮对话生成完整、跨端、可落地的 AI 学习社群工作台 |

## 存放约定

- 每个 Skill 使用独立目录，并必须包含 `README.md` 和 `upstream.json`。
- `upstream.json` 固定记录上游仓库、默认分支、同步 commit、同步日期、许可和实体路径；更新时以 commit 为比较基准。
- 能独立运行的 Skill 存入 `skill/`；依赖仓库内运行时的 Skill 存入 `source/`，保存上游仓库全部已跟踪文件。
- 完整上游快照的 `source/` 作为不可拆分的供应商目录管理，`STRUCTURE.md` 只登记根目录，不逐项展开内部文件。
- 上游许可证、NOTICE、依赖锁文件和运行脚本必须随快照保存；`.git/`、虚拟环境、缓存、输出文件、凭据和个人数据不得入库。
- 不直接修改 `source/` 内的上游文件。确需本地补丁时，放在条目目录的 `patches/` 或修订记录中，并说明原因与重放方式。

## 标准更新流程

1. 读取条目 `upstream.json`，获取仓库地址、默认分支和当前固定 commit。
2. 在临时目录抓取上游，比较新旧 commit、许可证、依赖和目录结构。
3. 以新版本全部已跟踪文件原子替换 `source/` 或 `skill/`，不要只覆盖部分文件。
4. 更新 `upstream.json` 的 commit、同步日期和必要说明，检查条目 README 是否仍准确。
5. 运行仓库校验和对应 Skill 自检，确认后再提交。

## 读取边界

- 查找、调用或更新 Skill 时先读本文件，再读对应条目 README 和 `upstream.json`。
- 只有真正执行 Skill 时才读取其 `SKILL.md` 及按需引用文件；不要默认加载完整上游源码。
- 上游 URL 只负责追踪更新，仓库中的固定 commit 快照才是当前可复现版本。
