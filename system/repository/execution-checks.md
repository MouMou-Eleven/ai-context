# 用仓库经验做成品时怎么自查

适用于：用仓库里的经验做出实际成品（课件、方案、文章、视频、应用），交付之前。只查事实或位置时不用。

读到规则不等于做到了。常见情况是 AI 明明读了"课件不写讲师安排"，交出来的稿子里还是有"本节讲 20 分钟"。所以交付前要拿成品逐条对照。

## 动手前（在心里或草稿里过一遍，不写进成品）

1. 这次交付什么、给谁看？给学员的课件、给主办方的方案、给讲师的备课稿，是三种东西。
2. 读了哪几个文件？里面有哪几条红线？
3. 这次有没有建委的特别要求，会不会跟默认规则冲突？冲突时按 [AGENTS](../../AGENTS.md) 第 3 步的优先顺序取舍。

## 交付前逐条检查

| 成品 | 重点查 |
|---|---|
| 学员课件 / 分享资料 | 标题、表头、提示框、正文里有没有讲师视角的话（时长、"讲师演示"、"课堂要看什么"）；读出来像不像建委在说话（对照[口语样稿](../expression/voice-samples.md)）；每个知识点有没有画面或例子 |
| 讲师备课稿 | 开头写明"仅内部使用"；时间和备用方案符合本场安排 |
| 对外方案 | 有没有内部内容（谈判策略、提示词原文、操作路径、"待核实"）；价值写得具体，没有假大空 |
| 宣传 / 招生 | 身份、荣誉、价格、权益和[背书表](../../personal/credentials.md)、项目记录一致；每个问题都是潜在学员真关心的 |
| 书稿 | 功能、菜单名是否查证过；小白能不能照着做 |
| 设计 / 视频 / 界面 | 看实际导出的画面：有没有裁字、漏镜头、声音错位；对照[设计原则检查表](../../work/domains/design/common/design-principles/README.md#交付前检查表)；画面里有会动的框和卡片时跑[逐帧自动检查](../../work/domains/design/common/code-driven-video/motion-and-verification.md#验收流程红线) |
| 应用开发 | 真实走一遍用户流程和出错的情况，不能只看构建通过 |
| 比赛评审材料（申报书、技术报告、逐字稿） | 每句是不是写给评委的：没有填写提示、代做、多余澄清；团队表只空姓名；标题黑体、图注居中（[天津大赛文档规范](../../work/domains/development/industry-cases/education/tianjin-ai-contest/document-format.md)）；链接按下一节比对 |
| 仓库写入 | 按[写入规范](./ingestion-workflow.md)跑校验 |

发现问题先改，改完回看受影响的上下文，再交付。

## 链接要整条复制（红线）

AI 从网页、截图、对话里“提取”链接时，常常只拿到前半段：问号后面的参数、`&` 后面的部分、换行后的部分丢了，链接看起来对，点开却进不去。

做法：

1. 链接只从平台的“复制链接”按钮或地址栏整条复制，原样存进一个核对文件（每行一条，例如 `作品访问说明.txt` 旁的 `links.txt`）。不从截图识别，不手打，不按“看起来是链接”的文字截取。
2. 申报书、技术报告、访问说明、视频画面里的链接，全部从这个核对文件里取，不各自重新提取。
3. 交付前用脚本比对（能运行 Python 就必须跑）：

```text
python system/repository/maintenance/check-deliverable.py <成品> --profile competition --links <核对文件>
```

脚本会把成品正文和 Word 超链接目标里的每条链接，和核对文件逐字比对：少了参数报 `link-incomplete` 并给出完整版本，核对文件里没有的报 `link-unverified`。另外在不登录的浏览器里实际打开一次。

## 交付时告诉建委

一两句话即可："这次用了仓库里的 ××、×× 经验；××那条因为……没有照做。"不要附一大张自评表。

## 自动检查工具

能运行 Python 时，交付前用脚本扫一遍常见问题。比赛评审材料和带链接的对外成品**必须跑**（红线），其他成品建议跑：

```text
python system/repository/maintenance/check-deliverable.py <草稿路径> --profile learner            # 学员课件
python system/repository/maintenance/check-deliverable.py <草稿路径> --profile external-proposal  # 对外方案，支持 DOCX
python system/repository/maintenance/check-deliverable.py <docx或txt> --profile competition --layout tianjin-contest-word  # 天津大赛评审材料（txt 不加 --layout）
python system/repository/maintenance/check-deliverable.py <成品> --profile general --links <核对文件>              # 任何带链接的成品
```

[脚本](./maintenance/check-deliverable.py)只能发现已知的几类问题（讲师视角词、方案里的内部内容、DOCX 隐藏链接等）。没报错不代表没问题，仍然要自己读一遍。

## 同样的错又犯了

说明规则写得不够具体，或者没被读到。按[写入规范](./ingestion-workflow.md)第三步第 5 条处理：改规则的写法和检查动作，不要再加一条"必须"。能用脚本判断的错（禁用词、链接、字体、版式参数），把它加进检查脚本并写一条测试：脚本对任何模型都一样执行，不靠这一次的 AI 记不记得。
