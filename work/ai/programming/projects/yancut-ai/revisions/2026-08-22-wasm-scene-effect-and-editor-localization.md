# WebAssembly 场景特效兼容与编辑器深层中文化

> 日期：2026-08-22

## 问题

- 加载已有项目时，预览渲染报错：`Invalid frame descriptor: missing field effect_pass_groups`。
- 场景管理面板及导出、字体、曲线预设、转写等编辑器深层交互仍有英文文案。

## 根因与修复

- TypeScript 帧描述符使用 `effectPassGroups`，当前安装的 `opencut-wasm 0.2.5` 却按 Rust 字段名期待 `effect_pass_groups`。
- 在 WebAssembly 边界新增兼容序列化，场景特效同时携带新旧两个字段名，使当前发布包和未来源码构建都可读取。
- Rust 源码将字段明确命名为 `effectPassGroups`，同时保留 `effect_pass_groups` 别名和默认值，防止旧工程数据失效。
- 场景面板、主场景名、关闭按钮、导出流程、字体选择、曲线预设、图形/遮罩/特效名称、字幕语言与转写进度等用户可见文案改为中文。
- 历史项目中的 `Main scene` 和 `Blur` 不强制重写原数据，而是在展示层兼容映射为“主场景”和“模糊”。

## 验证

- TypeScript `--noEmit` 检查通过。
- Biome 针对性检查通过。
- Next.js 16.1.3 生产构建通过，27 个静态页面全部生成。
- 在真实项目 `/editor/837f8cba-2c2b-4452-b63f-b9a8f3cba0f6` 中刷新并等待渲染，未再出现 `effect_pass_groups` 或其他运行时错误。
- 实际点击场景管理，确认显示“场景 / 在项目的不同场景之间切换 / 选择 / 主场景 / 关闭”。

## 升级注意

后续升级 `opencut-wasm` 或改为本地 WASM 构建时，必须保留此边界兼容测试；确认新包稳定接受 `effectPassGroups` 后，才能考虑移除旧字段别名。
