# Web Demo 实现与验收记录

> 实现与修订日期：2026-08-24
>
> 状态：本地可一键启动、已构建、已完成桌面/移动浏览器验收
>
> 本地源码：`C:\Users\Administrator\Documents\居- 项目\ai-sixty-jiazi-demo`

## 最终范围

Demo 使用 React 19、TypeScript、Vite、`lunar-javascript`、Web Audio API 和原生 SVG 实现。网站只包含以下四个模块；五个甲子神潮玩 IP 是另一条独立工作线，未接入网站。

| 模块 | 已实现能力 |
|---|---|
| 听命 | 公历日期时间输入、四柱与纳音、干支音位、可开关四分轨、Web Audio 合成音景、年柱档案 |
| 寻甲子 | 60 条数据检索、五行筛选、表格浏览、单条档案精读 |
| 合音 | 干支音位选择、A/B 试听、原始差值、上行/下行距离、十二律环形最短距离、五合六合预设 |
| 造曲 | 选择甲子、场景、情绪与时长，生成含完整 Melody、节奏、配器、意象和禁止项的可复制简报 |

## 空白/无法访问问题修复

- 浏览器实测为 `ERR_CONNECTION_REFUSED`：预览服务已经停止，不是 React 渲染白屏。
- Vite `base` 改为相对路径 `./`，增强静态构建兼容性。
- 新增 `npm run start:demo`，固定在 `127.0.0.1:4173` 启动生产预览。
- 新增 `启动甲音Demo.cmd`：双击后检查 npm、按需安装依赖、重新构建、打开浏览器并持续运行服务。
- 使用者必须保持命令窗口开启；关闭窗口后本地网页服务停止。

## 数据与算法口径

- 60 条数据从工作簿审计结果机械导出，每条保留 Excel 源文件追溯信息；解读字段标记 `needs-review`。
- 公历转四柱验收样例：`2005-12-23 08:37 → 乙酉 / 戊子 / 辛巳 / 壬辰`。
- 合音同时返回上行、下行和 `min(上行, 下行)` 的十二律环形最短距离。
- 四柱 `40 / 30 / 20 / 10` 仅是 Demo 混音权重，界面已显示“待确认”。
- 不导入约 690 MB 原始 WAV；首版使用 Web Audio 实时合成。

## 设计与验证

- 视觉基线：Superdesign v3“甲音 · 玄金夜谱精密古音仪”。
- 桌面验收：1440 × 1000；移动验收：390 × 844。
- `npm run typecheck`：通过。
- `npm test`：4 个测试文件，6 项测试全部通过。
- `npm run build`：通过；主 JS 约 578.5 KB（gzip 约 187.7 KB），仅有 Vite 体积提示。
- Playwright 逐页验证听命、寻甲子、合音、造曲；桌面和移动会话均为 0 错误、0 警告。
- 最终截图位于源码目录 `output\playwright\`，含四页桌面图和四页移动图。

## 本地运行

推荐直接双击：

`C:\Users\Administrator\Documents\居- 项目\ai-sixty-jiazi-demo\启动甲音Demo.cmd`

开发模式：

```powershell
Set-Location -LiteralPath 'C:\Users\Administrator\Documents\居- 项目\ai-sixty-jiazi-demo'
npm install
npm run dev
```

## 已知约束与下一步

- 尚未创建独立源码仓库和部署地址；按上下文仓库规则，不把整套源码或构建产物放入 `ai-context`。
- Vite 对单个主 JS 块给出大于 500 KB 提示；正式上线前再做路由拆包与性能基线。
- 上线前仍需确认历法边界、四柱权重、原始音频权属、文化史料和存疑字段。
- 独立潮玩 IP 的图像、提示词与验收报告位于 `C:\Users\Administrator\Documents\居- 项目\ai-sixty-jiazi-ip`，不要与网站交付混用。
