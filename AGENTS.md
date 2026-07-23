# AI 协作规则

> 本仓库是杨建委的长期 AI 协作上下文中枢，不是普通资料备份。任何 AI 在仓库内工作时，都应先路由、再按需读取，并保持事实可追溯。

## 开始方式

1. 先读 [`llms.txt`](./llms.txt)，判断当前任务需要哪些最小文件。
2. 只读取任务相关入口，不要默认遍历长文档、全部修订记录或二进制附件。
3. 写入或调整仓库结构前，再读 [`STRUCTURE.md`](./STRUCTURE.md)。
4. 涉及对外身份、荣誉或数字时，同时检查 [`open-questions.md`](./open-questions.md)，避免使用尚未解决的冲突口径。

## 事实优先级

出现冲突时，按以下顺序判断，不得混用新旧口径：

1. 建委在当前对话中最新明确确认的信息。
2. `open-questions.md`：其中登记的冲突在解决前不得擅自选边。
3. `current.md`：当前状态、正在推进的工作和现阶段社会角色。
4. 项目 `README.md` 的“当前口径”，再结合该项目 `revisions/README.md` 和最新有效修订。
5. `identity.md`、`preferences.md`：相对稳定的个人身份与工作偏好。
6. `knowledge/`：专题知识、能力、荣誉和已验证经验。
7. `history/`、历史修订、原始材料和二进制附件：只用于追溯，不作为当前口径直接引用。

如果仍无法判断，明确列出“已确认 / 待确认 / 已失效”三类信息，并向建委确认。

## 写入要求

- 先确认文件归属：个人当前状态进 `current.md`，稳定身份进 `identity.md`，专题经验进 `knowledge/`，长期项目进 `projects/`，历史事件进 `history/`。
- 每个长期项目必须有 `README.md`；新增文件后同步更新项目文件索引。
- 重要方向变化新增 `revisions/YYYY-MM-DD-{slug}.md`，不要无痕覆盖历史口径。
- 修订目录必须维护 `revisions/README.md`，明确哪些修订仍有效、哪些已被后续口径取代。
- “文件最后整理时间”和“业务事实最后确认时间”要分开表达，不能因为改了索引就暗示业务事实已重新核实。
- 使用 UTF-8、LF 和相对链接；不得写入密钥、Token、Cookie、个人隐私数据或可用凭证。
- 完成后运行 `powershell -ExecutionPolicy Bypass -File scripts/validate-context.ps1`。

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
- `projects/inshan-popupiano/revisions/2026-05-24-agency-pivot.md`
- `projects/inshan-popupiano/competitive-references.md`

当前有效口径是“授权经销 + 自建店铺 + 内容代运营”；我方自建 `inshan.cc` 和 Amazon 店铺；价格自主权已确认；货款流向和收入形式仍待澄清；海外叙事采用“编曲人 + 儿童/初学者”双钩子；AI 是生产与本地化工具，不是产品核心卖点。

### 付费社群课程

涉及付费社群、课程研发、自媒体引流或 AI 编程课程时，先读 `projects/paid-community-course/README.md`，再按任务只读取一到两个专题文件。历史名称和旧营销口径只存在于修订记录，不得覆盖当前“AI 超级个体陪跑社群”口径。

### 电脑、网络与本地 AI 工具

涉及电脑故障、Windows、网络、VPN、Clash、Codex、CC Switch、Codex++、插件或本地代理时，先读：

- `projects/computers/README.md`
- 对应设备的 `README.md`；当前设备是 `projects/computers/desktop-1/README.md`

正在执行 Codex 任务时，不得直接重启 Codex、CC Switch、Clash 或切换代理节点。先做只读诊断并保存回滚点；确需中断连接的变更，必须等安全窗口并明确说明。不得把 API Key、Token、Cookie、局域网地址或机器真实主机名写入仓库。

## 完成标准

- 当前事实有明确来源，冲突没有被掩盖。
- 新文件已进入对应 README 索引。
- 重要变化有修订记录，历史仍可追溯。
- 相对链接、项目入口和目录覆盖通过校验。
- 没有为了显得完整而补写未经确认的信息。
