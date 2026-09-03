# jianwei-ai-learning-community-workbench

通用身份适配型 AI 学习社群工作台 Skill。它不绑定建委个人、公司、课程或社群事实；用户输入任意职业、角色或场景后，Skill 先识别角色与首要结果，再通过少轮高信息量对话补齐关键变量，最后输出工作台产品方案、信息架构、视觉系统、跨端策略或可执行前端实现要求。

## 调用

- Skill 名称：`jianwei-ai-learning-community-workbench`
- Codex 调用：`$jianwei-ai-learning-community-workbench`
- 实体入口：[`skill/SKILL.md`](./skill/SKILL.md)
- 来源记录：[`upstream.json`](./upstream.json)

## 能力范围

- 任意身份识别与角色画像建模
- 两轮以内的精准选项式对话
- 学习循环、社群循环、AI 边界和数据状态设计
- 工作中枢型 UI、响应式跨端、无障碍与完整状态
- 交付前的产品完整性、视觉反套路和工程品控

## 维护边界

- 这是通用 Skill，不自动读取建委上下文仓库中的个人项目、培训项目或付费社群资料。
- 用户明确提供具体案例、仓库或品牌资料并要求对齐时，才读取对应资料。
- Skill 内容采用内部快照方式维护；修改前同步检查 `skill/SKILL.md`、`skill/references/` 与 `skill/agents/openai.yaml`。
