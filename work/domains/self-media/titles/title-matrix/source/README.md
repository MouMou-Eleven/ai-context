# Title Matrix 标题矩阵

> 把同一篇内容改写成适合不同发布形态、能被正文兑现的中文标题。

Title Matrix 用于公众号、小红书、X 短帖与长文、抖音和视频号等内容的标题工作。它从素材中提炼值得被看见的事实、动作和冲突，再按发布形态生成标题；也支持已有标题诊断、候选评审、账号数据复盘与案例收录。

它将标题的力度与事实范围分开处理。标题可以有画面、情绪和口语判断，但不能扩大比较范围、领先程度、自动化程度或作者实际完成的工作。

## 使用

最短调用：

```text
使用 $title-matrix，给这篇文章写 6 个适合公众号发布的标题。
```

多平台矩阵：

```text
使用 $title-matrix，基于下面的产品评测内容，分别为公众号、小红书和 X 短帖生成标题。保留作者第一人称语气，并说明你最推荐的一条。

[粘贴文章或素材]
```

已有标题诊断：

```text
使用 $title-matrix，诊断这个标题为什么平，并给 4 个可以直接替换的版本：
“我体验了一个新的 AI 写作工具”
```

数据复盘：

```text
使用 $title-matrix，复盘下面 8 篇公众号文章的标题和阅读数据。请先说明哪些数据可以比较，再给出标题相关的候选解释，不要把关联说成因果。
```

## 它处理什么

| 常见问题 | Skill 的处理方式 |
| --- | --- |
| 同一条标题发到所有平台 | 先区分发布形态，再按可见区、读者状态和内容用途改写 |
| 标题有情绪却夸大事实 | 拆分数字、实体、动作、结果、范围与程度等承诺，逐项回素材核对 |
| 候选全是同义句 | 从画面动作、反差、交付物、读者利害、机制等不同角度展开 |
| 已有标题太平 | 保留有效对象和方向，强化真实动作、反差或代价 |
| 数据低就归咎于标题 | 按账号、内容类型、观察窗口和指标恢复可比基线，区分标题、选题和分发因素 |

## 工作模式

- **生成**：基于内容、素材或话题生成标题。
- **诊断**：优化已有标题，并说明问题所在。
- **评审**：比较多个候选，给出推荐顺序和理由。
- **复盘**：分析标题与阅读、播放、互动等数据的关联和限制。
- **收录**：只有明确要求保存时，才记录已验证案例及其后续回填。

完整矩阵可使用稳妥、有点冲、顶格三档，并按需要提供作者语气与通用语气。轻量请求会优先给少量差异明显的候选和一条推荐，避免机械凑数。

## 安装

### Codex

克隆仓库后，将完整 Skill 目录复制到 Codex 的技能目录。不要只复制 `SKILL.md`，它依赖 `references/` 中的平台、证据与复盘规则。

```powershell
git clone https://github.com/zhouwei713/title-matrix.git
Copy-Item -Recurse -LiteralPath ".\title-matrix\skills\title-matrix" -Destination "$env:USERPROFILE\.codex\skills\"
```

预期路径：

```text
C:\Users\<用户名>\.codex\skills\title-matrix\SKILL.md
```

安装完成后，新开一个 Codex 任务并使用 `$title-matrix` 调用。

### Claude Code

仓库保留了 Claude 插件清单 `.claude-plugin/plugin.json`，Skill 位于 `skills/title-matrix/`。通过 Claude Code 的插件管理功能选择本仓库目录或其发布压缩包后，按客户端当前版本的插件安装流程启用即可。

## 仓库结构

| 路径 | 用途 |
| --- | --- |
| `.claude-plugin/plugin.json` | Claude 插件元数据 |
| `skills/title-matrix/SKILL.md` | 核心规则、模式路由与交付要求 |
| `skills/title-matrix/agents/openai.yaml` | Codex 界面名称与默认调用词 |
| `skills/title-matrix/references/evidence.md` | 研究、案例与数据证据边界 |
| `skills/title-matrix/references/platforms.md` | 各发布形态与字数核验建议 |
| `skills/title-matrix/references/review-and-library.md` | 数据复盘与案例库规则 |
| `skills/title-matrix/data/.gitkeep` | 本地案例数据目录占位文件 |

## 验证与边界

已验证：Skill frontmatter、引用路径和 Codex 结构校验。

尚未验证：不同模型对同一素材的标题表现、平台实际分发效果与真实点击率。研究、账号历史数据和公开案例只在其明确的样本范围内作为参考，不能推出平台算法或确定收益。

本仓库默认忽略本地收录的标题数据，避免把账号数据或未公开内容提交到公开仓库。

## 设计原则

标题的承诺应当能在正文中得到充分回应。单项跑分或局部案例只能支持对应范围内的表达；“实测”“教程”“模板”“免费”“一键”等词也需要逐项兑现。

平台展示、编辑器字段和规则会变化。临近字数上限或准备发布时，以当前官方编辑器和内容规范为准。

## License

本项目采用 [MIT License](LICENSE)。
