# 中文质量基础层与多来源治理修订

> 日期：2026-08-21
>
> 范围：AI 表达默认读取、中文数据集定位、开源纠错资源、AI 培训外部经验治理

## 一、修订原因

原有 AI 表达架构已经形成“通用中文基础层 + 单一工作专项”的正确关系，但通用层以抽象表达原则为主，缺少完整的语法、病句、语义、语境和翻译腔检查入口。

同时，`chinese-datasets/` 容易被误解为需要把大型数据全部塞进上下文。外部创作者资料继续增加后，如果按人物同时调用，也会出现开头、节奏、结构和语言偏好互相冲突的问题。

## 二、当前确认

1. 不改变“AI 表达总层 + 一个最具体专项”的现有架构。
2. 中文语法与病句检查放入 `brain/ai-expression/chinese-datasets/`，不在 AI 表达根目录再建立新的并列门类。
3. `grammar-and-error-checklist.md` 是从数据和开源规则提炼出的默认执行层；原始数据仍不默认读取。
4. 大型外部仓库和语料不整体复制进本仓库，只保存来源、版本、许可、用途、限制和提炼后的当前规则。
5. 外部创作者不以人物身份激活。资料先拆成具体方法，同义内容去重，兼容内容分工，替代方案按场景选择一种。
6. 建委当前要求、项目事实和真实授课复盘高于外部经验。
7. 仓库校验脚本必须检查新增的默认规则文件，并在 Windows PowerShell 5.1 下稳定解析 `STRUCTURE.md` 的树形字符。

## 三、开源资源核验结论

- FCGEC 是中文语法检错与纠错语料、任务和模型项目；CodaBench 是通用评测平台，不是第二套 FCGEC 数据。
- CodaLab 平台于 2025-12-31 停止接收新的评测任务提交后，FCGEC 于 2026-04-12 把在线提交入口迁移到 CodaBench；迁移不改变语料身份。
- 用户提供的论文是 CodaBench 平台论文，主要贡献是任务包、评分模块、固定运行环境和可复现评测，对中文语法规则本身没有直接贡献。
- FCGEC、LanguageTool、pycorrector、MuCGEC、NaSGEC、中文技术文档写作规范和中文文案排版指北分别承担错误分类、候选检查、研究参考或排版规范，不能互相替代。
- MuCGEC 仓库虽然标注 Apache-2.0，但其纠错标注规范 PDF 首页另有传播限制；本仓库只记录独立提炼结论，不复制或上传该 PDF。
- NaSGEC 未明确声明许可证，当前只作为研究参考。

## 四、默认调用变化

旧调用：

```text
AI 表达入口
→ 跨领域规则
→ AI 表达经验
→ 口语或书面规则
→ 一个专项
```

新调用：

```text
AI 表达入口
→ 跨领域规则
→ 中文语法与病句检查
→ AI 表达经验
→ 口语或书面规则
→ 一个专项
→ 交付前检查事实和意义漂移
```

用户不需要额外要求语法检查，也不需要逐条给数据评分。AI 默认在内部完成检查，只交付最终结果。

## 五、飞天闪客资料的当前归属

- 原始逐字稿保存在 `brain/ai-expression/chinese-datasets/feitian-shanke/raw/`，只用于追溯和重新提炼。
- 已提炼的“问题驱动技术讲解”保存在 `work/ai/training/experience/technical-explanation/`，AI 培训解释技术概念时直接调用该方法。
- 日常任务不按“飞天闪客”人物身份激活，也不默认读取原逐字稿。
- 后续其他讲师资料先进入数据来源层登记，再按教学功能与现有方法去重、合并或分场景保留。

## 六、避免多来源冲突

来源处理统一分为三层：原始来源、候选方法、当前规则。只有当前规则和一个最具体的专项可以默认激活。

冲突处理顺序：

```text
当前任务要求
→ 当前项目事实
→ 建委真实授课复盘
→ 已验证培训方法
→ 外部来源候选方法
→ 原始逐字稿
```

不能判断时保留冲突并向建委确认，不把多套方法取平均或同时拼接。

## 七、涉及文件

- `AGENTS.md`
- `llms.txt`
- `brain/README.md`
- `brain/ai-expression/README.md`
- `brain/ai-expression/cross-domain-rules.md`
- `brain/ai-expression/chinese-datasets/README.md`
- `brain/ai-expression/chinese-datasets/grammar-and-error-checklist.md`
- `brain/ai-expression/chinese-datasets/feitian-shanke/README.md`
- `work/ai/training/experience/README.md`
- `work/ai/training/experience/technical-explanation/README.md`
- `work/ai/training/experience/technical-explanation/problem-driven-technical-explanation.md`
- `repository/maintenance/validate-context.ps1`
- `repository/revisions/README.md`
- `STRUCTURE.md`
- `STRUCTURE.html`
