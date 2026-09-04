# jianwei-ai-community-remotion-video

建委 AI 社群的 Remotion 视频制作 Skill。它接收一句话、参考图片或“文字 + 图片”，先完成目标最终帧、状态反差、记忆点、动作回扣和重叠节奏的导演判断，再输出可直接指导 Remotion 实现的画面、动作、镜头、层级、音效和质量约束，重点避免“规范正确但缺少观赏性”的幻灯片式动画。

默认工作方式为三阶段：先公开输出“制作规划确认单”，等待建委明确确认；确认后实现并交付覆盖完整时长的低分辨率预览；建委再次确认后才执行最终全量渲染。规划必须逐元素说明触发、起始状态、动作路径、速度变化、因果、结束状态与微动，不能用通用淡入和镜头推拉代替动作编排。

默认输出为参数化 Remotion 工程：通过 Zod Schema 和 Studio 参数面板编辑主文字、画面中存在的编号以及关键颜色；同时可渲染当前默认参数的 MP4。MP4 是参数快照，可编辑能力来自随附工程。只有建委明确选择固定值、硬编码或只要不可编辑成片时，才改用固定成片模式。

## 调用

- Skill 名称：`jianwei-ai-community-remotion-video`
- Codex 调用：`$jianwei-ai-community-remotion-video`
- 实体入口：[`skill/SKILL.md`](./skill/SKILL.md)
- 参数化契约：[`skill/references/parameterization-contract.md`](./skill/references/parameterization-contract.md)
- 参考图保真契约：[`skill/references/reference-fidelity-contract.md`](./skill/references/reference-fidelity-contract.md)
- 渲染性能与预览流程：[`skill/references/render-performance-contract.md`](./skill/references/render-performance-contract.md)
- 最终帧对比工具：[`skill/scripts/compare_reference_frame.py`](./skill/scripts/compare_reference_frame.py)
- 来源记录：[`upstream.json`](./upstream.json)

该目录保存完整、自包含的 Skill 快照。名称已于 2026-09-01 从 `jianwei-ai-community-video` 调整为当前名称。

## 维护边界

- 这是建委内部维护的 Skill，不自动镜像某一个外部仓库。
- Remotion 官方 Skills 与 `buainoai/remotion-skills` 是规范和设计参考；更新前必须先比较规范变化，再人工合并并运行 Skill 校验。
- 修改提示词契约时，同步检查 `references/`、JSON Schema、验证脚本和 `agents/openai.yaml`，避免只改主文件造成模型间输出漂移。
- 2026-09-01 根据首个图片开场动画实测，增加默认确认门与逐元素动作契约；旧的“内部规划后直接实现”流程停止使用。
- 2026-09-01 对比 `motion-director` 实测后增加导演层：目标最终帧、状态反差、最值得记住的一秒、收尾回扣与因果重叠成为实施前硬门槛；同时将参数化工程提升为默认输出。
- 2026-09-02 根据 Studio 实测补充参数化与右侧面板编辑契约：`schema` 与内联 `defaultProps` 必须直接挂在 `<Composition>`，并实际在 `Inspector → Default Props` 修改文字、编号和颜色，确认真实画面即时变化；仅有可选图层或“空参数”不再视为可编辑。
- 2026-09-04 根据参考图定帧偏差与 5 秒视频渲染过慢的实测，增加参考图保真模式、关键区域对比工具、只重建必要元素、低清预览后最终渲染确认门、默认渲染器优先级和动态滤镜性能预算；更新 JSON Schema 与 Blueprint 校验器，避免模型只写口号不执行。
