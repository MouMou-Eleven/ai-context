# 表达规则来源与适用边界

本页保存证据身份与提炼去向，[纠错表](./corrections.md)保存可执行动作。原中文数据目录的重复入口、长逐字稿与检查表已精简为这两份文件；默认不加载原始资料。本次为结构与规则复核，不宣称重新核验了所有外部仓库。

## 实际反馈与仓库来源

| 编号 | 来源 | 可复用结论及边界 |
|---|---|---|
| T1 | [培训默认风格与高频失误](../../work/domains/training/experience/jianwei-training-style.md)及[培训来源表](../../work/domains/training/experience/sources.md) | 已整理多轮课堂反馈：学员视角、可朗读、每部分有知识、媒体不复读、保护编辑成果；课程系列仍按来源表区分 |
| T2 | [问题驱动技术讲解](../../work/domains/training/experience/technical-explanation/problem-driven-technical-explanation.md) | 具体动作、机制与限制替代抽象话；包含外部参考提炼，不把全文称为建委逐句改稿 |
| B1 | [当前出版规则](../../work/projects/feishu-efficient-office/writing-style-analysis.md) | 小白可操作、唯一案例主线、删同义复述、保护已接受稿；飞书功能仍需按版本核验 |
| B2 | [第2章编辑反馈](../../work/projects/feishu-efficient-office/ch2-editor-feedback-lessons.md)与[出版验收](../../work/projects/feishu-efficient-office/publication-acceptance-checklist.md) | 实际编辑与图文要求；具体章节、专名与排版例外不提升为所有写作默认 |
| C1 | [对外交付语言](../../work/domains/other/commercial/experience/external-deliverable-language.md) | 原记录来源为2026-08-21“琅琅分级悦读”旁白交付校准；2026-09-12明确保留影响责任和决策的未定状态 |
| M1 | [成果展示与用户动机](../../work/domains/self-media/experience/outcome-and-motivation.md) | 自媒体选题、体验分享与商业论证的方法；外部逐字稿缺账号效果数据，不能证明留存或转化提升 |
| G1 | [迁移前共享纠偏记录](https://github.com/MouMou-Eleven/ai-context/blob/da9d88eba870ea221043ceb8c7ea9be4ea031e62/system/expression/cross-domain-rules.md) | 保留搭配、问句与选项检查；原记录没有每句的原始反馈链接，标为已有规则，不冒充本人原话 |
| G2 | 建委2026-09-12本轮仓库调整对话 | 明确要求自然、符合不同专业体裁、从真实错误提炼、压缩来源文件；领域样稿不归个人信息。此行是对话摘要，不是认可成品样稿 |

## 外部表达参考

| 编号 | 来源与核验状态 | 提炼去向与限制 |
|---|---|---|
| O1 | 建委2026-08-02提供的两段短视频逐字稿；作者、原链接、日期、平台与授权未提供 | 结果与具体场景、疑问与论据的承接方式已压缩到[口语](./oral.md)，商业方法留M1。不能复制金句、补造画面、继承赚钱论断或声称提高完播率 |
| O2 | 2026-07-23整理的“飞天闪客”技术科普参考；作者标注来自用户材料，原视频链接与转载授权未独立核验 | 问题、旧办法、缺口、新机制及限制的讲解方法留T2；模型参数、排行与时效事实不能直接引用 |

需要重新核对原措辞时，可查固定旧版本的[两段短视频原稿](https://github.com/MouMou-Eleven/ai-context/blob/da9d88eba870ea221043ceb8c7ea9be4ea031e62/system/expression/chinese-datasets/short-video-outcome-and-motivation/raw/two-video-transcripts.md)和[技术科普原稿](https://github.com/MouMou-Eleven/ai-context/blob/da9d88eba870ea221043ceb8c7ea9be4ea031e62/system/expression/chinese-datasets/feitian-shanke/raw/feitian-shanke-transcript.txt)。它们不作为当前默认读链，也不是本轮新核验的外部原视频来源。原稿精简不损失已提炼的专项方法，不把这些材料声明为可训练语料。

## 语法与工具参考

以下为旧记录标注2026-08-21的版本／许可快照，本次仅保留来源，不代表当前上游仍是这些版本。实际调用或再分发前重新查README、许可和模型／数据各自条款。

| 编号 | 来源 | 原记录版本与许可 | 作用与限制 |
|---|---|---|---|
| F1 | [FCGEC](https://github.com/xlxwalex/FCGEC) | `851cfb0`，Apache-2.0 | 中文病句分类与纠错评估；试题和新闻来源权利另查，不复制全量语料 |
| F2 | [CodaBench](https://github.com/codalab/codabench) | `0a0ed87`，Apache-2.0 | 评测任务、评分和可复现环境；是平台，不是中文语料或语法规则；[论文](https://doi.org/10.1016/j.patter.2022.100543)供评测设计参考 |
| F3 | [LanguageTool中文模块](https://github.com/languagetool-org/languagetool/tree/master/languagetool-language-modules/zh) | `5041497`，LGPL-2.1 | 词语和句法候选检查；不复制整套规则制造更新分叉 |
| F4 | [pycorrector](https://github.com/shibing624/pycorrector) | `fc8aa56`，Apache-2.0 | 错字、多字、漏字、词序候选；模型和数据来源分别判断，不自动接受修改 |
| F5 | [MuCGEC](https://github.com/HillZhang1999/MuCGEC) | `3922193`，仓库标注Apache-2.0，标注规范PDF另有限制 | 多来源、多参考纠错；不转发受限PDF，不把二语学习者错误概括为全部母语写作 |
| F6 | [NaSGEC](https://github.com/HillZhang1999/NaSGEC) | `13044f1`，原记录未声明许可证 | 社交、学术、语文考试场景参考；许可未明确前不复制数据或模型 |
| F7 | [中文技术文档写作规范](https://github.com/ruanyf/document-style-guide) | `5719517`，README声明public domain | 技术说明结构与格式；句长建议不是所有体裁的语法硬限制 |
| F8 | [中文文案排版指北](https://github.com/sparanoid/chinese-copywriting-guidelines) | `9a5fbeb`，MIT | 空格、全半角、标点与专名；不承担事实、逻辑与专业判断 |

本仓库未因收录链接而安装这些工具、运行模型训练或完成效果测试。默认由AI依规则检查；批量校对才按实际环境选工具，接受候选前核对原意。

## 后续反馈怎样进入规则

1. AI在原项目／领域记录实际问题句、修改后文本（如果已有）、用途、用户反馈日期与依据；未知认可状态不得补为认可。正文只存一份。
2. 找到纠错表已有同类问题就补该行证据，优先修正读取入口、执行或验收漏洞；不为每次失败另建同义文件。
3. 单次特例留项目；多任务反复出现或建委明确要求长期执行时，提炼“错误类型—修正动作—适用／排除范围—来源—验收”。缺反复验证但值得试用的标为候选，不默认激活。
4. 若新规则涉及结构与语气，检查培训、出版、自媒体、正式交付四种边界。能兼容的合并，互为选项的限定条件，不能平均拼接多位作者文风。
5. 更新纠错表、来源表和必要体裁入口；只有高频通用底线变化才改短卡。以真实成品和反馈评估是否有效，方法示例不作实战效果证据。
