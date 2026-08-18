# AI 协作规则

本仓库是杨建委的长期 AI 协作事实中枢。所有 AI 必须先路由、再读取、后回答，不得只凭当前对话记忆或模型经验猜测仓库内容。

## 1. 任务开始

1. 用户提到 GitHub、仓库、repo、ai-context、上下文仓库、项目记录、历史资料、之前整理过、仓库里有没有、推送或持续推进项目时，必须实际检查本仓库。
2. 先读 [`llms.txt`](./llms.txt)，再读任务对应的最近一层 `README.md`。
3. 只读取完成任务必需的文件。不要默认加载全部 `history.md`、时间线、原始材料、长文档或二进制附件。
4. 涉及新增、移动、重命名或清理时，再读 [`STRUCTURE.md`](./STRUCTURE.md)。

## 2. 事实优先级

出现冲突时按以下顺序判断：

1. 建委在当前对话中的最新明确确认。
2. 对应领域或项目的当前 `README.md`。
3. 当前专题文件、当前工具说明或实际环境核验结果。
4. `personal/` 中稳定的个人事实。
5. 领域经验与建委大脑中的长期方法。
6. 项目 `history.md`、跨领域时间线、归档材料和 Git 历史，只用于追溯。

无法判断时必须列出“已确认、待确认、已失效”，不能混用或自行补空白。

## 3. 一级目录职责

- `personal/`：个人概要，回答建委是谁、业务概要、项目概要、背书、成长路径和能力。不得写具体项目过程。
- `brain/`：建委本人的认知、思考方式、口语习惯和个人表达。不得收纳某个工作领域专用的语言规则。
- `work/`：设计、AI 和其他领域的工作经验、工具与项目。
- `repository/`：仓库治理、版本规则、电脑环境和校验工具。
- `history/`：跨领域时间线与已归档项目，不作为当前事实入口。

## 4. 严格激活规则

- 默认只激活一个最具体的领域。用户说“AI 自媒体”，只读 `work/ai/self-media/`，不得加载 AI 培训。
- 用户说“AI 培训”，只读 `work/ai/training/`；只有明确提到某个培训项目，才继续进入该项目。
- 用户说“参考建委本人的思考或说话方式”，才读 `brain/`。
- 用户要求“结合多个领域”或提示中明确出现多个独立任务时，才组合读取，并说明组合了哪些入口。
- “课程”或“课件”语义不明时，先判断服务对象和交付物：建委作为讲师属于 AI 培训；为教师制作成品微课属于设计下的微课与 MG 动画。

## 5. 工作归属

### 设计

- PPT、海报折页、书籍装帧、微课与 MG 动画、AE 宣传视频、AI 设计都归 `work/design/`。
- AI 设计仍是设计，只是使用了 AI，不得移入 AI 门类。
- 微课是给教师、学校或教育项目制作成品课件；它与建委作为讲师开展 AI 培训并列。

### AI

- AI 编程：`work/ai/programming/`，内部再分工具、经验、项目。百度秒哒是工具；言剪 AI 是项目。
- AI 培训：`work/ai/training/`，内部再分经验、大纲、资料、项目。付费会员社群属于培训项目。
- AI 视频：`work/ai/video/`，内部再分通用方法、类型、工具、项目。
- AI 书籍出版：`work/ai/publishing/`，飞书书籍项目在此。
- AI 自媒体：`work/ai/self-media/`，标题、文章、口播、直播销售和增长经验均在此，不归 AI 培训。

### 其他

- 海外电商等不属于设计或 AI 的项目进入 `work/other/`。

## 6. 特殊项目

### 《飞书高效办公》

必须先读：

- `work/ai/publishing/projects/feishu-efficient-office/README.md`
- `work/ai/publishing/projects/feishu-efficient-office/writing-style-analysis.md`

飞书菜单名、按钮名、功能路径必须通过官方文档或实际界面核验。面向小白写细步骤，禁止凭经验推断。只在需要追溯版本变化时读取项目 `history.md`。

### Inshan / POPUPIANO

必须先读：

- `work/other/inshan-popupiano/README.md`
- `work/other/inshan-popupiano/competitive-references.md`

当前口径：授权经销 + 自建店铺 + 内容代运营；不是简单分销，也不是托管品牌方现有 Amazon 店铺；我方自建 `inshan.cc` 和 Amazon 店铺；价格自主权已确认；货款流向和收入形式待澄清；海外叙事为“编曲人 + 儿童/初学者”双钩子；AI 是生产与本地化工具，不是产品核心卖点。

### 电脑与本地环境

涉及 Windows、网络、VPN、Clash、Codex、CC Switch、插件或本地工具时，先读 `repository/environment/computers/README.md` 并确认设备。正在执行任务时不要直接重启 Codex、CC Switch、Clash 或切换代理；先做只读诊断。

## 7. 写入与清洗

- 每个长期领域、工具或项目必须有 `README.md` 作为入口。
- 新文件必须被最近一层 README 索引；禁止出现无法路由的孤岛文件。
- 先去重、去旧、合并同义内容。当前入口只保留当前有效结论。
- 重大变化先更新项目 README，再把必要的原因、新旧差异和日期追加到项目 `history.md`。普通小改动只留在 Git 提交，不单独建修订文件。
- 历史细节由 Git 保留。不要为了“完整”让大量失效版本继续出现在当前读取树中。
- 动态产品、功能、价格、界面和 API 遵守 `repository/versioned-knowledge-policy.md`，回答前重新核验。

## 8. 提交标准

- 使用 UTF-8、LF、相对链接，英文路径采用 kebab-case。
- 提交前检查 `git status --short`，确认没有无关文件和敏感信息。
- 运行 `repository/maintenance/validate-context.ps1`。
- 推送后验证远端分支和对应文件存在。
