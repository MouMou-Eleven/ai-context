# 2026-09-01 AI 编程 Skill 仓库

## 变更原因

建委需要长期收录可直接调用、可追踪上游版本的 Agent Skills。只记录 GitHub 地址无法保证离线读取、版本复现和依赖完整性；把大型第三方运行仓库的每个内部文件都列入 `STRUCTURE.md`，又会让上下文结构索引失去可读性。

## 已确认的新口径

- 在 `work/ai/programming/experience/` 下新增五级目录 `skill-repository/`，中文名称为“Skill 仓库”。
- 每个条目必须保存 Skill 实体，并用 `upstream.json` 固定上游地址、分支、commit、同步日期和存放模式。
- 自包含 Skill 存入 `skill/`；依赖同仓运行时的项目保存完整 `source/` 快照。
- 完整快照只复制上游已跟踪文件，不保存 `.git/`、缓存、虚拟环境、凭据或运行输出。
- `STRUCTURE.md` 必须登记每个 `source/` 根目录；当 `upstream.json` 声明 `full-repository-snapshot` 时，校验器不要求把其内部供应商文件逐项展开。

## 首批内容

- `jianwei-ai-community-remotion-video`：建委内部维护的 Remotion 视频制作 Skill；由原名 `jianwei-ai-community-video` 更名。
- `editaplot`：保存 `hang-jin/editaplot` 完整已跟踪文件快照，固定在 commit `4aa986f3f84da9cb2a2297159a8f20e42b7e527c`。之所以不是只复制 `skill/editaplot/`，是因为上游明确依赖 `runtime/` 与根目录启动脚本。

## 影响范围

- 更新 AI 编程与通用经验入口、根 `llms.txt` 路由和完整结构树。
- 扩展仓库校验器，检查 Skill 条目的 README、来源元数据和完整快照根目录，同时保持供应商目录为不展开的结构节点。
- 后续更新必须先比较固定 commit，再整体替换快照并运行校验，不能无痕覆盖来源信息。
