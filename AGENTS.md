# AI 协作规则

> 本仓库是杨建委的长期 AI 协作上下文中枢，不是普通资料备份。任何 AI 在仓库内工作时，都应先路由、再按需读取，并保持事实可追溯。

## 开始方式

1. 先读 [`llms.txt`](./llms.txt)，判断当前任务需要哪些最小文件。
2. 只读取任务相关入口，不默认遍历全部修订、历史、原始材料或二进制附件。
3. 涉及仓库写入、移动或结构调整时，再读 [`STRUCTURE.md`](./STRUCTURE.md)。
4. 涉及对外身份、荣誉或数字时，同时检查 [`personal/open-questions.md`](./personal/open-questions.md)。
5. 涉及会持续更新的产品、功能、价格、界面或 API 时，遵守 [`repository/versioned-knowledge-policy.md`](./repository/versioned-knowledge-policy.md)，必要时重新核验官方资料或当前环境。

## 仓库触发语义

当建委提到 GitHub、仓库、repo、ai-context、上下文仓库、项目记录、历史资料、之前整理过、仓库里有没有、推送或持续推进项目时，必须实际检查 `MouMou-Eleven/ai-context`，不能只凭当前对话记忆回答。

先看目录树或 `llms.txt`，再读相关 README、修订索引和必要专题。不要一开始加载全部长文档；回答时尽量给出具体仓库路径。

## 事实优先级

出现冲突时，按以下顺序判断，不得混用新旧口径：

1. 建委在当前对话中的最新明确确认。
2. `personal/open-questions.md` 中登记的跨文件冲突。
3. `personal/current-focus.md` 的当前状态与优先级。
4. 对应项目或工作领域 README，再结合 `revisions/README.md` 和最新有效修订。
5. `personal/identity.md`、`personal/achievements.md` 等稳定个人档案。
6. `expression/`、`knowledge/` 和工作领域中的已验证方法。
7. `history/`、旧修订、原始材料和附件，只用于追溯。

仍无法判断时，明确列出“已确认、待确认、已失效”，再向建委确认。

## 六类写入位置

- 建委本人：`personal/`，包括身份、当前状态、能力、荣誉、兴趣、工具和待确认事实。
- 表达与知识传达：`expression/`，包括沟通偏好、教程写法、讲解方法和优秀来源材料。
- 工作领域与长期项目：`projects/`，包括当前事实、执行经验、案例、决策和修订。
- 跨项目认知：`knowledge/`，包括思维方法、第一性原理、商业增长和长期见解。
- 仓库治理：`repository/`，包括维护规则、动态版本治理、校验和安全。
- 历史追溯：`history/`，包括跨项目时间线和已归档项目。

每个长期工作领域或项目必须有 `README.md`。新增资料必须进入最近一层 README 索引；重要方向变化新增 `revisions/YYYY-MM-DD-<slug>.md` 并更新修订索引。不得无痕覆盖重要历史。

## 工作领域边界

### 表达与写作

用户说“参考仓库里的语言表达习惯”“按我沉淀的表达和讲解经验来写”“减少 AI 味”时，读取 `expression/README.md`。调用按方法语义进行，不要求用户记住“飞天闪客”等来源作者姓名。来源材料只用于追溯和继续提炼，不机械仿写。

### AI 培训

涉及 AI 培训、企业培训、公开课、授课、讲师备课、培训课程、培训课件、学员资料或授课复盘时，先读：

- `projects/ai-training/README.md`
- `projects/ai-training/teaching-and-course-design.md`

这里负责建委“怎样作为讲师完成培训”，不负责教师委托的微课制作。

### 微课

涉及微课、精品课、参赛课、教师委托、哞哞微课、VR 交互课件或教育案例制作时，先读：

- `projects/microcourse/README.md`
- 追溯边界变化时再读 `projects/microcourse/revisions/README.md`

微课与 AI 培训是并列工作领域。只出现“课程”或“课件”且语境不明时，先确认服务对象和交付物，不得把两个领域合并后自行猜测。

### AI 编程与动态产品

涉及网站、应用、自动化或开发方法时，先读 `projects/ai-programming/README.md`。涉及百度秒哒时，先读 `projects/ai-programming/miaoda/llms.txt`，当前入口优先，历史版本只在追溯时读取。新功能必须写明来源、适用环境和核验日期，旧功能必须标记取代关系。

## 特殊项目规则

### 飞书书籍

涉及《飞书高效办公》时，先读：

- `projects/feishu-efficient-office/README.md`
- `projects/feishu-efficient-office/writing-style-analysis.md`
- `projects/feishu-efficient-office/revisions/README.md`

飞书菜单名、按钮名和功能路径必须通过飞书官方文档或实际界面验证。面向小白写细步骤，不能凭经验推断功能。

### Inshan / POPUPIANO

涉及 Inshan、POPUPIANO、海外电商、代运营、Amazon 或独立站时，先读：

- `projects/inshan-popupiano/README.md`
- `projects/inshan-popupiano/revisions/README.md`
- `projects/inshan-popupiano/competitive-references.md`

当前有效口径是“授权经销 + 自建店铺 + 内容代运营”；我方自建 `inshan.cc` 和 Amazon 店铺；价格自主权已确认；货款流向和收入形式仍待澄清；海外叙事采用“编曲人 + 儿童/初学者”双钩子；AI 是生产与本地化工具，不是产品核心卖点。

### 付费社群课程

涉及付费社群、课程研发、自媒体引流或 AI 编程课程时，先读 `projects/paid-community-course/README.md`，再按任务只读取一到两个专题文件。课程项目事实服从社群项目；通用讲师经验按需调用 AI 培训；语言表达按需调用 `expression/`，三者不得互相覆盖。

### 电脑、网络与本地 AI 工具

涉及电脑故障、Windows、网络、VPN、Clash、Codex、CC Switch、Codex++、插件或本地代理时，先读 `projects/computers/README.md` 和对应设备 README；当前设备是 `projects/computers/desktop-1/README.md`。

正在执行 Codex 任务时，不得直接重启 Codex、CC Switch、Clash 或切换代理节点。先做只读诊断并保存回滚点；确需中断连接的变更，必须等安全窗口并明确说明。不得把 API Key、Token、Cookie、局域网地址或机器真实主机名写入仓库。

## 提交与完成标准

- 使用 UTF-8、LF、相对链接；文件名采用 kebab-case。
- “索引最后整理时间”和“业务事实最后确认时间”分开表达。
- 推送前查看 `git status --short`，确认没有无关文件或敏感信息。
- 运行 `powershell -ExecutionPolicy Bypass -File repository/maintenance/validate-context.ps1`。
- 推送后验证远端分支和对应文件存在。
- 当前事实有来源，冲突没有被掩盖，历史仍可追溯，未为了完整而补写未经确认的信息。
