# 项目上下文迁移到 Other

> 日期：2026-08-24
>
> 性质：项目归属与唯一写入位置修订

## 用户最新确认

“AI 六十甲子古音律与 IP 孵化”不应位于 AI 编程项目目录，应移动到 `other`；后续不得继续向错误位置推送。

## 归属判断

本项目的长期主体是六十甲子文化、中国古音律、个性化声音体验和甲子神 IP 孵化。网站、App、小程序、AI 音乐、生图和 AI 综艺都是产品载体或实现手段，不是仓库的一级分类依据。

因此，项目固定归入：

`work/other/ai-sixty-jiazi-music-ip/`

旧位置已经失效：

`work/ai/programming/projects/ai-sixty-jiazi-music-ip/`

## 本次迁移

- 整体移动项目 README、产品规划、数据审计、Demo 实现、IP 提示词和全部修订记录。
- 从 `work/ai/programming/projects/README.md` 删除项目入口。
- 在 `work/other/README.md` 建立唯一项目入口。
- 更新根 README、`work/README.md`、`STRUCTURE.md`、`AGENTS.md` 和 `llms.txt`。
- 增加明确禁止规则：不得因后续执行 Web、App、AI 音乐或生图任务而在 AI 编程目录重建同名项目。

## 后续写入规则

1. 项目事实、方向、产品文档、IP 规则和修订记录只写入新路径。
2. 完整源码仍应进入单独的源码仓库；`ai-context` 只保存长期上下文。
3. 如果项目过程中形成可跨项目复用的编程经验，可以提炼到 `work/ai/programming/experience/`，但不能复制项目 README 或在 AI 编程目录建立第二份项目上下文。
4. 网站产品与甲子神 IP 继续作为本项目内两条独立工作线管理。
