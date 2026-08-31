# jianwei-ai-community-remotion-video

建委 AI 社群的 Remotion 视频制作 Skill。它接收一句话、参考图片或“文字 + 图片”，先做视觉理解，再输出可直接指导 Remotion 实现的画面、动作、节奏、镜头、层级、音效和质量约束，重点避免幻灯片式动画。

## 调用

- Skill 名称：`jianwei-ai-community-remotion-video`
- Codex 调用：`$jianwei-ai-community-remotion-video`
- 实体入口：[`skill/SKILL.md`](./skill/SKILL.md)
- 来源记录：[`upstream.json`](./upstream.json)

该目录保存完整、自包含的 Skill 快照。名称已于 2026-09-01 从 `jianwei-ai-community-video` 调整为当前名称。

## 维护边界

- 这是建委内部维护的 Skill，不自动镜像某一个外部仓库。
- Remotion 官方 Skills 与 `buainoai/remotion-skills` 是规范和设计参考；更新前必须先比较规范变化，再人工合并并运行 Skill 校验。
- 修改提示词契约时，同步检查 `references/`、JSON Schema、验证脚本和 `agents/openai.yaml`，避免只改主文件造成模型间输出漂移。
