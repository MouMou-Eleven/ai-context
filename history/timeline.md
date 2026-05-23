# History — 时间线 & 里程碑

> 时间戳均通过 Python datetime 验证，格式：`YYYY-MM-DDTHH:MM:SS+08:00 (unix_ms)`

## 2026

### 2026-05-24

**01:33:29+08:00** `1779557609951`
- 在 [`knowledge/microcourse.md`](../knowledge/microcourse.md) 中新增「业务官网：哞哞微课」章节，沉淀两件事：
  - 平台事实：建委的微课设计业务有了对外官网「**哞哞微课 AI 教育案例展示平台**」（用 AI 编程工具自建，含管理后台）。**注意定位**：这不是 `projects/` 下的独立编程项目，而是微课业务本身的展示门面/官网入口
  - **案例描述写作规范**（重要约定）：每个新案例的简介必须遵循一段话/三要素/技术加粗/200 字内/不分点的格式，并附两条已沉淀范例（《大班健康活动：闽超小将》《快乐购物小超市》）作为模板对照
- 目的：建委后续上传新案例时，AI 看到本档案即可直接按规范生成对应简介，无需反复口头描述要求

### 2026-05-22

**06:49:33+08:00** `1779403773263`
- 澄清「VR + AI + 交互教育」的归位：经建委本人口述确认，它**不是独立平台/项目**，而是微课设计业务下的 VR 交互课件案例之一
- 新建 [`knowledge/microcourse.md`](../knowledge/microcourse.md) 系统记录「微课设计业务」全景（建委的常态业务之一，给老师做参赛微课），含微课形态矩阵：精品课 / PPT 微课 / 万彩微课 / AI 视频微课 / VR 交互课件 / Coze 智能体微课 / VBA 制作 PPT
- 修正 2026-05-21 条目中「⚠️ 缺口」标注为「✅ 已澄清」

**06:38:59+08:00** `1779403139970`
- 完成历史遗留待办清理：
  - 删除 `projects/ai-context-management.md`（旧单文件，唯一独特信息「飞书科普文档链接」迁入根 [`README.md`](../README.md) 的「对外科普版」章节）
  - 同步更新 [`projects/README.md`](../projects/README.md) 项目索引：移除已迁移条目
  - 移除 [`STRUCTURE.md`](../STRUCTURE.md) 第五节「旧项目文件迁移说明」整块（feishu-book.md / openclaw-agent.md / videoai.md / ai-context-management.md 均已实际删除，"待迁移"标注与现实矛盾）
  - 修复 [`history/timeline.md`](../history/timeline.md) 末尾历史粘贴遗留的重复块（2026-04-05 与 2026-03-18 条目误重复）

**06:07:55+08:00** `1779401275020`
- 重构 `knowledge/` 目录：新增 `ai-programming/` 大类子目录，将原 `knowledge/miaoda/` 整体迁移到 `knowledge/ai-programming/miaoda/`（git mv 保留历史）；为后续 Cursor / Claude Code / v0 等 AI 编程类工具实战经验预留同级位置
- 在 `knowledge/ai-programming/miaoda/` 下补充 4 个新文档（事实均经百度官方文档核验）：
  - [`disambiguation.md`](../knowledge/ai-programming/miaoda/disambiguation.md)：百度秒哒 MIAODA 与飞书妙搭 Spark 同名产品辨析
  - [`version-features.md`](../knowledge/ai-programming/miaoda/version-features.md)：26 年版本节点速查（V3.0 → V1.3 倒序）
  - [`publish-channels.md`](../knowledge/ai-programming/miaoda/publish-channels.md)：4 种发布渠道能力边界（含微信小程序 web-view 限制：禁付款/禁朋友圈/禁文件下载/域名白名单）
  - [`skill-as-callable.md`](../knowledge/ai-programming/miaoda/skill-as-callable.md)：V2.5 反向能力——秒哒打包为 Skill 被 OpenClaw / Claude Code 调用
- 同步更新 [`STRUCTURE.md`](../STRUCTURE.md)：在结构图与结构规则中加入 `knowledge/<大类>/<工具>/` 三层模式说明
- 同步更新 [`knowledge/ai-programming/miaoda/README.md`](../knowledge/ai-programming/miaoda/README.md) 索引：从 5 行扩到 9 行覆盖全部新文档
- 维护原则：现有 6 个 miaoda 高质量文件（platform-basics / skill-development / pitfalls / prompt-patterns / case-yungouos-jsapi / 旧 README）仅 README.md 作为索引追加新条目，其余实质内容未改动

### 2026-05-21

**20:09:00+08:00** `1779365340000`
- 受邀向「万融汇金 OPC 社区」展厅提供个人 & 公司展示资料（OPC 大赛一等奖后续延伸合作；展厅装修中，需展示十一创公司介绍 + 个人简介 + 代表案例）
- 整理输出展厅资料 Word 文档：[`万融汇金OPC社区展厅-十一创动画科技有限公司展示资料.docx`](f:/桌面文件/万融汇金OPC社区展厅-十一创动画科技有限公司展示资料.docx)（本地，未入库）
- 展厅展示的代表案例选定为四类：① VideoAI（AI 编程落地）② VR + AI + 交互教育平台 ③ AI 视频创作 ④ AI 设计
- ✅ 2026-05-22 澄清：「VR + AI + 交互教育」不是独立平台/项目，而是建委微课设计业务下的 VR 交互课件案例之一。已新建 [`knowledge/microcourse.md`](../knowledge/microcourse.md) 系统化记录微课业务全景（精品课/PPT 微课/万彩微课/AI 视频微课/VR 交互课件/Coze 智能体微课/VBA 制作 PPT 等形态），原"projects/ 下尚无 VR + AI + 交互教育平台"的缺口标注作废
- 副产物：沉淀「对外简练版个人介绍」模板（聊天侧产出，含一句话定位「用 AI 帮企业把想法变成产品，把培训变成产值」）→ 后续可考虑迁入 `identity.md` 或新建 `pitch.md`
- 关联引用：公司/个人/荣誉信息全部在 [`identity.md`](../identity.md) 与 [`knowledge/achievements.md`](../knowledge/achievements.md) 已有；OPC 大赛获奖见下方 2026-05-08 条目

### 2026-05-08 ~ 2026-05-09

- 参加“创赢未来”2026创业大赛选拔赛暨第六届“创业威海”创业大赛
- 5月8日决赛，5月9日颁奖仪式颁奖
- 获 OPC 赛道一等奖，奖金 2 万元（税前，偶然所得扣税 20%，预计到手 16,000 元）


### 2026-04-05

**03:17:00+08:00** `1775330220000`
- 完善 AI Context 仓库内容，基于详细个人信息全面更新 identity / preferences / tech-stack / knowledge 等文件

**03:00:00+08:00** `1775329200000`
- 在 GitHub 创建私有仓库 `MouMou-Eleven/ai-context`
- 安装 GitHub CLI (gh v2.89.0)，完成首次 push

### 2026-03-18

- OpenClaw AI Agent 首次上线运行

## 2025

- 参与 2025 AI 春晚《AI 奥运》项目创作（核心创作团队成员 & 主力剪辑）
- 为北京日报《新春 AI 短片》提供技术共创与主力剪辑
- AI 绘画作品参展红树林湿地 AI 艺术万人展
- 承办秒哒、即梦、EasyClaw 济南线下 AI 活动
- 获百度文旅 AI 短视频大赛全国第三名（爆款人气奖）
- 获微博「任意门」AI 绘画赛全国人气奖 TOP 2（30万参赛者）
- 获深圳阿里云通义智能硬件展「创作新青年」全国季军
- 受邀担任山东高速集团、万融集团、山东省图书馆等政企机构特邀 AIGC 讲师
- VideoAI 营销视频自动化平台上线

## 2024

- 本科毕业（宿州学院 · 美术与设计学院 · 环境设计专业）
- 注册宿州市十一创动画科技有限公司，担任法人代表

## 2020–2024（本科期间）

- 发表 SCI 论文一篇，国内四刊论文三篇
- 以项目负责人身份成功立项校创、省创、国创并结项
- 微课设计作品获国家级、省级、市级一等奖及部级精品微课
- 获安徽省环境设计大赛二等奖
- 为哈尔滨工业大学、东北大学、江南大学等高校提供创赛视频设计服务

---

<!-- 重要事件发生时在此追加记录，时间戳用 Python 验证 -->
