# 结构镜像同步与表达/自媒体分流

> 历史记录：以下正文保留本次修订发生时的分类、路径和规则，供追溯，不是当前执行指令。2026-09-12已采用四个主入口与集中项目管理，当前规则从[现行入口](../README.md)读取。文中的旧路径只描述当时位置；可点击链接已指向现存资料。

## 背景

本次维护来自建委对长期 AI 协作仓库的两个明确要求：

1. 仓库的 `STRUCTURE.html` 必须随每次 GitHub 更新保持同步，桌面上的 `GitHub仓库完整结构.html` 不能成为过期副本。
2. 通用口语化表达要有唯一来源；AI 培训与 AI 自媒体只记录各自场景的应用。自媒体素材还要按发布渠道分流，避免后续材料堆在一个目录里。

## 已确认的新规则

- `brain/ai-expression/oral-expression/` 是跨领域通用口语表达、口语推进和口语化论证的唯一维护位置。
- `work/ai/training/` 只记录培训受众、课程结构、演示和授课复盘；不复制通用口语规则。
- `work/ai/self-media/` 按主要发布渠道维护文章、营销文案、朋友圈、社群话术、口播、直播销售、标题和运营经验。同一材料只保留一个主归属，其他场景只引用。
- 每次提交前都从最新 `STRUCTURE.md` 生成并暂存仓库 `STRUCTURE.html`；提交后同步桌面 HTML，并用 SHA-256 核对一致性。

## 本次结构变化

- 将通用口语方法从 `brain/ai-expression/experience/` 归一到 `brain/ai-expression/oral-expression/`。
- 新增 `work/ai/self-media/marketing-copy/`、`moments-copy/`、`community-copy/` 三个有独立边界的入口。
- Git Hook、维护 README、`AGENTS.md`、`llms.txt` 和 `STRUCTURE.md` 统一采用上述路由和同步口径。

## 维护要求

- 新增表达经验前，先判断它是跨领域通用规则，还是培训/自媒体的场景应用；通用规则不得在领域目录复制。
- 新增自媒体材料先判断主要发布渠道；跨平台且没有单一渠道归属的推广内容才进入 `marketing-copy/`。
- 目录变化后先更新 `STRUCTURE.md`，再运行结构生成、桌面同步和 `validate-context.ps1`；提交前检查 `git status --short`，推送后核验远端 `main`。
