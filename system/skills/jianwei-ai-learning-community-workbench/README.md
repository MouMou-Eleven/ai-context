# jianwei-ai-learning-community-workbench

由杨建委**自研并维护**的通用身份适配型 AI 工作台设计 Skill。名称用于定位社群专属工具，能力不绑定任何个人业务；用户输入任意职业、角色或场景后，Skill 先识别角色与首要结果，再通过少轮高信息量对话补齐关键变量，最后输出工作台产品方案、信息架构、视觉系统、跨端策略或可执行前端实现要求。

## 版本、依赖与边界

- 来源为自研，`origin=internal`；没有登记第三方上游仓库。自研事实与外部参考分开记录，不为完整性编造来源。
- 固定实体版本：`workflowRevision=3`，同步日期2026-09-04；具体内容按本仓Git版本追溯。2026-09-12只整理能力说明，未修改实体。
- 适用于“给教师/销售/律师等角色做AI工作台”“把我的工作流变成可操作界面”等任务；先辨明角色、结果、数据与AI责任，再设计和实现。
- 不把预设行业、个人或社群案例强塞给当前用户；不把界面方案当成已接真实接口的上线应用。名称不决定项目或课程归属。
- 方案阶段需要AI宿主和真实需求；实现阶段检查目标工程声明的框架、运行时、包管理器及接口依赖。仓库有快照不表示本机已安装或有统一预装运行环境。

## 查看与执行

查能力读本页和 `upstream.json`；执行角色工作台任务时再读实体 `SKILL.md` 与必要参考，按当前任务已有信息与授权推进，缺少关键事实再补齐，不为资料查询启动产品访谈。

当前实体revision 3仍带有制作前访谈与用户确认要求，未在本轮修改。实际执行结合宿主指令和当前会话已确认的信息判断这些要求是否已满足，不重复索取已有事实或再次确认同一授权；未确定的角色、数据和结果仍须补齐。

## 调用

- Skill 名称：`jianwei-ai-learning-community-workbench`
- Codex 调用：`$jianwei-ai-learning-community-workbench`
- 实体入口：[`skill/SKILL.md`](./skill/SKILL.md)
- 来源记录：[`upstream.json`](./upstream.json)

### 实体参考索引

以下只在执行或维护对应内容时按需读取，不为查阅能力一次性加载。

- [代理配置](./skill/agents/openai.yaml)
- [对话协议](./skill/references/conversation-protocol.md)
- [角色适配](./skill/references/role-adaptation.md)
- [设计系统](./skill/references/design-system.md)
- [质量门槛](./skill/references/quality-gate.md)

## 能力范围

- 任意身份识别与角色画像建模
- 两轮以内的精准选项式对话
- 工作循环、协作边界、AI 边界和数据状态设计
- 工作中枢型 UI、响应式跨端、无障碍与完整状态
- 交付前的产品完整性、视觉反套路和工程品控

## 维护边界

- 这是通用 Skill，不预设个人、组织、品牌、行业或案例。
- 当前任务需要建委的业务、经历或项目资料时，从已授权仓库读取相关来源作为输入；不要要求重复提供，也不把无关个人资料或预设案例强塞到其他角色的工作台。
- 修改前同步检查 `skill/SKILL.md`、`skill/references/` 与 `skill/agents/openai.yaml`。

实体变更时更新workflowRevision与同步日期，并验证主文件、引用和代理配置；能力变化同步本页、upstream.json、上层Skill索引与业务入口。只改说明不声称实体已更新。
