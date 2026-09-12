# Skill 仓库：能力调用与版本记录

> 同时保存能力入口、来源记录和可复现实体。先看能力卡，真正执行才读 `SKILL.md`；保存到本仓不等于已安装到当前电脑。
> 索引整理：2026-09-12。本轮只校准说明与元数据，实体版本没有更新。

## 按自然任务调用

| 你要做什么 | 先读能力卡 | 来源 | 可交付能力 |
|---|---|---|---|
| 用一句话、脚本或参考图制作可编辑视频、片头或MG动效 | [建委Remotion视频](./jianwei-ai-community-remotion-video/README.md) | 杨建委自研，参考外部规范 | 参数化Remotion工程、完整低清预览与按当前授权渲染的成片 |
| 用实验数据做Origin科研图，保留可编辑项目 | [EditaPlot](./editaplot/README.md) | 第三方：[hang-jin/editaplot](https://github.com/hang-jin/editaplot) | Origin可编辑OPJU与PNG/PDF/TIF |
| 按职业、角色或真实工作场景设计AI工作台 | [建委身份工作台](./jianwei-ai-learning-community-workbench/README.md) | 杨建委自研 | 工作台方案、信息架构、跨端状态与实现要求 |
| 制作个人IP、观点、活动嘉宾或创意角色系列海报 | [青云IP海报](./qingyun-ip-poster/README.md) | 第三方：[qingyunAGI/qingyun-ip-poster](https://github.com/qingyunAGI/qingyun-ip-poster) | 3:4/9:16海报视觉系统、系列规则与质检 |

Skill是能力依赖，不是业务项目归属。商单与实践事实进入[项目与案例](../../work/projects/README.md)，视频方法从[设计视频](../../work/domains/design/video/README.md)读取；名称中的“community/社群”不表示某个课程事实属于会员课程。一个主任务可按需要引用多个能力卡，相关领域只保留链接，不复制实体。

## 查看、执行与来源

1. **查有什么、会做什么**：本索引 → 条目README → `upstream.json`。此时不安装、不运行、不加载全部参考文件，也不触发Skill中的制作确认流程。
2. **实际制作或运行**：确认当前任务需要此能力后，再读实体 `SKILL.md` 与所需参考文件，检查依赖、输入、当前会话授权和交付检查。实际执行记录写回主任务；不把示例人物、数据或截图当用户事实。
3. **版本记录**：第三方以固定commit为准；自研以 `workflowRevision`、`syncedAt` 与本仓Git版本为准。`documentationReviewedAt`仅指能力说明整理日，不冒充代码同步日或本机运行验收日。
4. **来源区别**：自研标 `origin=internal`，第三方标 `origin=third-party` 并给上游链接。自研条目的 `upstreamReferences` 是参考，不表示外部作者开发了本Skill。
5. **本机状态**：调用前检查当前设备是否安装、版本是否匹配、依赖是否满足；不能因仓库保存快照就声称随时可执行。

## 新增与维护

- 每项独立目录必须包含README能力卡、`upstream.json`与实际实体路径。卡片写清能力、适用/不适用、来源、自研归属、固定版本、依赖、交付、查看/执行边界及更新方法。
- 新增后同步本索引、任务所属领域入口和根任务路由；只维护一个实体。README能力变化、调用词变化和路径变化必须同时校验相关索引，不等待建委逐项提醒。
- 自研更新：核对主文件、引用契约、Schema、脚本与代理配置；从实际案例提炼通用能力，增加 `workflowRevision`、更新同步日期并记录必要变更原因。仅改说明不增加实体版本号。
- 第三方更新：先比较固定commit与候选commit的许可、依赖、结构和行为差异，再整体替换已跟踪快照；更新commit、同步日和README，并验证实体完整性及适用自检。
- `source/` 或第三方 `skill/` 是完整供应商快照，不直接手改；需要补丁时另存并写明重放方式。自研 `skill/` 按自己的版本流程维护。
- 保留LICENSE、NOTICE、依赖锁文件和运行脚本；不入库 `.git/`、环境、缓存、输出、凭据或个人输入。`system/repository/navigation/STRUCTURE.md`仅展开能力条目，不遍历完整外部源码。
- `sourcePath`相对条目目录解析；需要完整运行时的Skill从该来源根目录检查依赖。当前四项仍分别使用 `source/` 或 `skill/`，迁移能力库不改变快照内部路径或实体版本。
- 维护完成后运行仓库链接/元数据/快照校验，必要时执行对应Skill验证；没运行的测试明确记录。更新不等于已获部署、发布或对外发送授权。
