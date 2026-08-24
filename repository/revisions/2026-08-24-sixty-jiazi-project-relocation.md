# 六十甲子项目迁移到 Other

> 日期：2026-08-24
>
> 范围：工作项目分类、读取路由、唯一写入位置

## 变更原因

“AI 六十甲子古音律与 IP 孵化”最初因首个交付物包含 Web Demo，被放入 AI 编程项目。建委最新确认该分类错误：项目的本体是文化产品、古音律声音体验和 IP 孵化，编程与 AI 只是实现方式。

## 权威位置

- 新位置：`work/other/ai-sixty-jiazi-music-ip/`
- 失效旧位置：`work/ai/programming/projects/ai-sixty-jiazi-music-ip/`

## 防止复发

- `AGENTS.md` 已加入本项目特殊路由和旧路径禁用规则。
- `llms.txt` 已加入“六十甲子网站、甲音、音乐算命、出生节律声音、甲子神 IP”等关键词路由。
- `work/other/README.md` 成为项目的上级唯一索引。
- `work/ai/programming/projects/README.md` 明确链接新位置并禁止建立重复目录。
- `STRUCTURE.md` 与派生的 `STRUCTURE.html` 同步反映新结构。

项目未来即使继续开发网站、App、小程序、AI 音乐、生图或 AI 综艺，也不得改变这一归属。只有可跨项目复用的纯编程经验，才可单独提炼到 AI 编程经验目录。
