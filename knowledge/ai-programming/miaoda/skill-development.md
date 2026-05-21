# 自定义技能开发指南（实战版）

> 写给以后再为秒哒做技能包的人。所有内容都是真实上传被秒哒接受后总结的，与官方文档对照过。

## 一、最小可用的 .zip 包结构

```
your-skill.zip                          ← 不要套子文件夹，根目录直接是这些
├── SKILL.md                            ← 必需，秒哒解析入口
├── scripts/                            ← 可选，可执行脚本
│   ├── _shared.py                      ← 内部工具（下划线开头表示不对外暴露的入口）
│   └── do_something.py                 ← 业务脚本
├── references/                         ← 可选，参考资料，AI 在生成代码时会查阅
│   └── *.md / *.ts / *.html
└── assets/                             ← 可选，图标 / 模板 / 字体等
    └── icon.png
```

**关键规则**：
- 根目录直接放 SKILL.md，**不要**套类似 `.skills/<name>/SKILL.md` 这种两层目录
- 秒哒官方插件生成的包默认套了两层，需要先解压重新打包
- 文件名小写、kebab-case，避免空格和中文

## 二、SKILL.md 强制格式

文件必须以 YAML frontmatter 开头，否则上传校验失败。最小可用模板：

```markdown
---
name: your-skill-name
description: 一句话说清这个技能能做什么、何时触发。当用户需要 X、Y、Z 时必须触发。
license: Proprietary
---

# 技能标题

## 技能名称
...

## 技能描述
...

## 使用许可
...

## 执行说明
- 环境变量：`YOUR_API_KEY` —— 用途说明
- 调用入口：scripts/xxx.py —— 何时调用
```

**字段要点**：
- `name`：kebab-case，与压缩包文件名对齐，便于用户 `@name` 调用
- `description`：决定 AI 是否选择触发这个技能，越具体越好；要含"何时使用"
- `license`：随意（Proprietary / MIT 都行），不能省略

## 三、scripts/ 脚本约定（我们自己定的，但很好用）

为了让秒哒应用层调用脚本时一致，统一约定：

| 维度 | 约定 |
|---|---|
| 入参 | 从 stdin 读取一个 UTF-8 JSON 对象 |
| 出参成功 | `{"ok": true, "data": {...}}` 输出到 stdout |
| 出参失败 | `{"ok": false, "error": "原因"}` 输出到 stdout |
| 退出码 | 0=成功；2=参数/环境错；3=上游业务错；4=网络错 |
| 密钥读取 | `os.environ.get("YOUR_KEY")`，为空时立即报错退出，不做 fallback |
| 依赖 | 优先 Python 标准库（hashlib、urllib、json、os、sys），避免 pip 依赖 |

## 四、环境变量是放密钥的唯一安全位置

秒哒控制台「技能 > 我的 > 本技能 > 环境变量」是文档明确说"安全注入、不会对外暴露"的地方。**禁止**把密钥写进：
- SKILL.md 的任何位置（包括"密钥安全警告"那种讽刺的反例）
- scripts/ 任何 .py 文件
- references/ 任何参考文档
- assets/ 文件

实际操作建议：
1. 打包前用 `grep -r <密钥前 8 位> ./` 全文扫一遍
2. 打包后用 `unzip -p X.zip <每个文件>` 二次扫
3. zip 包文件大小应该在 30KB 以内，超过先看有没有意外塞进去的文件（如 `__pycache__`、`.git`）

## 五、references/ 是放给应用层后端复制的代码

秒哒应用层后端（Edge Function）需要的代码不能直接写进 scripts/（运行时不同），但可以放在 references/ 让 AI 在生成应用代码时复制过去。常见类型：

- `references/edge_function_*.ts`：Supabase Edge Function 形态的后端代码
- `references/frontend_*.html`：前端片段（如 WeixinJSBridge 调用）
- `references/*.md`：接口速查表、字段映射、错误码表

提示词里要明确告诉秒哒"原样使用 references/X 文件，不要重写"，否则它会自己生成一份（大概率有 bug）。

## 六、必须做的静态验证（打包前）

1. `python -m py_compile scripts/*.py references/*.py` —— 所有 Python 语法对
2. 字节级密钥泄漏扫描——任何字面密钥都应返回 0 hits
3. `unzip -l X.zip` —— 确认 SKILL.md 在根目录、无 `__pycache__`、无 `.pyc`、无 `.git`
4. `unzip -p X.zip SKILL.md | head -5` —— 第一行必须是 `---`
5. 如果脚本里有 MD5/HMAC 签名，用一组已知答案的样例做自检（参考 [pitfalls.md](./pitfalls.md) MD5 章节）

## 七、上传后的配置流程

1. 在「技能 > 创建技能」拖入 .zip → 等 AI 解析 ≤1 分钟
2. 解析成功后会展示「基本信息」「环境变量」「技能定义」三个面板
3. 在「环境变量」面板填入 Value（密钥），保存
4. 在应用对话框 `@<技能名>` 引用，发指令使用

## 八、迭代更新技能

如果改了 .zip 重新上传，环境变量不会自动迁移到新版本，需要重新填一遍。所以小改动最好直接改 SKILL.md 在线编辑（如果秒哒支持），避免反复重填密钥的麻烦。