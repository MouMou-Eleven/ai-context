# qingyun-ip-poster

青云 IP Poster · Visual System Edition：把人物、观点、活动或创意角色素材编译成可持续发布的高级竖版海报与系列视觉系统。

## 来源、固定版本与依赖

- **第三方Skill，非建委自研**。上游：[qingyunAGI/qingyun-ip-poster](https://github.com/qingyunAGI/qingyun-ip-poster)。
- 固定commit：`f0b7d5e17a90e5e9917f136c9b038b60fa3b7f41`，上游版本 `1.2.0`，同步2026-09-08；说明整理2026-09-12，实体未更新。
- 需要支持Skill的AI宿主、人物/品牌/活动等真实素材，以及本轮使用的生图、排版与检查工具；本机生图遵守 `imagegen.cmd` 启动器规则，不因上游示例改变通道。
- 本仓记录不代表本机安装状态、图像工具可用性或作者授权已核验；实际任务开始时检查。

## 调用

- Skill 名称：`qingyun-ip-poster`
- Codex 调用：`$qingyun-ip-poster`
- 实体入口：[`skill/SKILL.md`](skill/SKILL.md)
- 中文说明：[`skill/README.zh-CN.md`](skill/README.zh-CN.md)
- 来源记录：[`upstream.json`](upstream.json)

该目录保存上游仓库在固定提交上的完整 Skill 快照，包括 `SKILL.md`、代理配置、参考规则和视觉资产。需要更新时，先比较上游提交、许可证和目录，再整体替换快照；不要直接修改 `skill/` 内的上游文件。

## 适用范围

- 商务个人 IP 批量海报与账号九宫格视觉诊断。
- Keynote 观点宣言海报。
- 嘉宾与活动总海报、嘉宾观点卡系列。
- 创意 IP 角色档案与世界观 Key Art。

支持 3:4 与 9:16。它负责视觉系统、信息层级、图像层与排版层拆分和交付质检；具体人物身份、奖项、日期、Logo 和商业事实必须由用户提供或另行核验。

## 不适用与使用边界

不用于视频制作或应用开发，也不能替代人物事实、商用授权和传播效果证据。

- 先读本 README 和 `upstream.json`，真正执行时再读 [`skill/SKILL.md`](skill/SKILL.md) 及按任务引用的 `references/` 文件。
- 上游仓库当前未附带开放许可证。该快照仅供建委个人上下文仓库内部读取和迭代，未经作者许可不得默认公开再分发、商业打包或上传敏感原图。
- 示例海报中的姓名、履历、奖项、Logo、日期和文案是版式参考，不是可复用事实。
- 没有数据时只能说明视觉秩序变化，不能把示例前后图包装成流量或转化 A/B 结果。


## 维护

先比较上游候选commit的能力、依赖和许可，再整体替换 `skill/`；更新commit、syncedAt、版本说明和本能力卡，并核对文件完整性。新增适用任务或改入口时同步 [Skill总索引](../README.md) 和相关设计入口。当前说明整理不改变快照内容与许可状态。
