# Title Matrix 标题矩阵

> 为中文文章、短帖和视频内容生成、诊断、评审与复盘跨平台标题。

Title Matrix 从素材中提炼可由正文兑现的事实、动作和冲突，再按公众号、小红书、X 短帖与长文、抖音和视频号等发布形态改写标题。它支持生成、已有标题诊断、候选评审、数据复盘和显式要求下的案例收录。

## 安装

将完整的 `title-matrix` 目录复制到 Codex 技能目录，保留 `references/`、`agents/` 和 `data/`：

```powershell
Copy-Item -Recurse -LiteralPath ".\title-matrix" -Destination "$env:USERPROFILE\.codex\skills\"
```

安装完成后，预期入口为：

```text
C:\Users\<用户名>\.codex\skills\title-matrix\SKILL.md
```

新开一个 Codex 任务后使用 `$title-matrix` 调用。

## 使用

生成标题：

```text
使用 $title-matrix，给这篇文章写 6 个适合公众号发布的标题。
```

诊断已有标题：

```text
使用 $title-matrix，诊断这个标题为什么平，并给 4 个可直接替换的版本：
“我体验了一个新的 AI 写作工具”
```

复盘标题数据：

```text
使用 $title-matrix，复盘下面的标题和阅读数据。先说明哪些数据可比较，再给出标题相关的候选解释，不要把关联说成因果。
```

## 工作方式

- 先判断用户是在生成、诊断、评审、复盘还是收录案例。
- 再区分发布形态，尤其区分 X 短帖首句与 X 长文标题。
- 把标题承诺拆成数字、实体、动作、结果、范围与程度，逐项回素材核对。
- 根据用户需求给轻量候选，或给稳妥、有点冲、顶格三档矩阵。

Skill 可以增强画面和情绪，不能扩大比较范围、领先程度、自动化程度或作者实际完成的工作。

## 验证与边界

已验证 Skill 结构、UTF-8 编码和引用路径。尚未验证不同模型的标题效果、平台真实分发效果或点击率。研究和历史数据仅在各自样本范围内提供参考。

## License

本项目采用 [MIT License](LICENSE)。完整仓库说明与 Claude Code 插件信息见仓库根目录的 `README.md`。
