# Remotion Skill 参数化验收修订

## 变更原因

2026-09-01 生成的 Remotion 片头已经拆分图层并声明了 Zod Schema，但建委在 Studio 右侧无法按预期修改并看到可编辑结果。问题不在“是否有图层”，而在 Skill 没有把 Default Props 面板的真实交互设成独立验收项，也没有明确区分图层选择和参数编辑。

## 新口径

- `jianwei-ai-community-remotion-video` 的默认交付仍为参数化 Remotion 工程。
- `schema` 与可序列化的内联 `defaultProps` 必须直接写在 `<Composition>` 上；字段名、默认值、组件 Props 和真实画面绑定必须一致。
- 交付前必须启动 Studio，选中 Composition，在右侧 `Inspector → Default Props` 修改至少一组主文字、编号和颜色，并确认预览中的真实元素即时变化，再恢复默认值。
- 只有 `Interactive` 图层可选、源码存在变量或面板出现但画面不变，均判定为参数化失败。
- MP4 仍然只是当前 Props 的渲染快照；可编辑能力来自随附工程，报告必须明确这一点。

## 同步范围

- 本地安装：`C:\Users\Administrator\.codex\skills\jianwei-ai-community-remotion-video`
- 上下文仓库实体：`work/ai/programming/experience/skill-repository/jianwei-ai-community-remotion-video/skill/`
- 新增参考：`references/parameterization-contract.md`
- `upstream.json` 的 `workflowRevision` 从 3 提升到 4，`syncedAt` 更新为 2026-09-02。
