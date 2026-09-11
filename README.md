# 杨建委长期 AI 协作上下文仓库

这里保存建委的个人事实、长期项目、实战方法、可执行Skill与来源证据，供后续任务检索、复用和修正。内容的价值由下次任务能否找到、用对和验收决定。

## 开始使用

- AI先读[AGENTS.md](./AGENTS.md)与[llms.txt](./llms.txt)，然后按任务进入相关README。
- 建委可以直接说“做一条MG微课”“按之前经验做AE宣传片”“把这次商单经验沉淀到设计”。AI按主任务读取必要方法、平台工具与案例，并负责更新索引。
- 查人物与业务：[personal](./personal/README.md)。查全部当前项目：[项目登记](./repository/navigation/projects.json)，具体状态回到项目权威记录。
- 查可以调用的工具能力：[Skill索引](./work/ai/programming/experience/skill-repository/README.md)。查怎样维护：[写入流程](./repository/ingestion-workflow.md)。
- 看完整目录：[STRUCTURE.md](./STRUCTURE.md)；展开、折叠和搜索：[STRUCTURE.html](./STRUCTURE.html)。桌面镜像由维护脚本生成。

## 五个一级目录

| 入口 | 职责 |
|---|---|
| [personal](./personal/README.md) | 建委是谁、稳定身份、业务概要、能力和背书 |
| [brain](./brain/README.md) | 建委认知与中文表达方法，不代替项目事实 |
| [work](./work/README.md) | 设计、AI、其他工作：项目、经验、工具、案例 |
| [repository](./repository/README.md) | 读取、写入、来源、路由、校验和电脑环境 |
| [history](./history/README.md) | 需要保留的历史追溯，默认不参与当前回答 |

## 运行原则

1. 一个项目/案例/方法只维护一份正文；AI视频与设计等相关领域通过链接自动组合必要依赖。
2. README是入口，当前证据要比较日期、对象与适用范围；不能让漏更新的摘要覆盖建委新确认。
3. 培训必须先核对项目或场次；会员社群与外部授课分开，课号不用于跨项目匹配。
4. 原始资料→案例证据→候选方法→验证→正式复用；已有方法再次失败时修调用、执行或验收。
5. 新内容的归属、README、跨领域引用、路由和结构同步由AI完成。操作要求见[写入流程](./repository/ingestion-workflow.md)。

百度秒嗒/秒哒与飞书妙搭是不同平台；先[识别产品](./work/ai/programming/tools/miaoda/disambiguation.md)。飞书URL不自动触发飞书书籍。当前规则由AGENTS及各权威文件维护，本页只导航。

## 校验与发布

见[维护工具](./repository/maintenance/README.md)。建委要求沉淀到GitHub时，校验后直接提交推送main并核验远端。结构HTML随提交生成，桌面同步故障独立诊断。

仓库配置：[文本规范](./.gitattributes)、[忽略规则](./.gitignore)、[GitHub自动校验](./.github/README.md)。这些是运行配置，业务知识仍在上述五个一级目录。

仓库管理方法的对外科普版：<https://www.feishu.cn/wiki/PqSHwL1nniP2pOkML25cZx2bnSb>
