# 2026-09-16：动效、参考视频、模板与工作台修复

本轮依据建委的八张截图和六个参考仓库升级同一个可编辑工作台，并发布到 Vercel 个人测试环境。建委确认今后每次言剪更新都要同步本地权威源码、验收后的 Vercel 版本和本上下文仓库，无需重复提醒；最终百度秒哒迁移仍待功能稳定及当期平台能力核验。

## 已发布版本

- [固定工作台](https://yancut-ai-personal.vercel.app/studio/workbench)；[填写本人 GLM Key](https://yancut-ai-personal.vercel.app/ai-settings)。同一标签页保存 Key，公网没有共享模型密钥。
- Vercel 部署：`dpl_6DQMEr4s2bmPnk1Gr6KQq5joQt3d`；先在新预览验证，再切换固定域名，切换后已用浏览器回读。
- 上一版本 `dpl_C7kathhPgGXjXoGe6Vw81pVw3ssb` 保留作为回退目标。
- 私有源码：[本轮实现 815a841](https://github.com/MouMou-Eleven/yancut-ai/commit/815a841)、[同步后的主分支 b0b24335](https://github.com/MouMou-Eleven/yancut-ai/commit/b0b243357860f63ccf7cd46d67c22f35e28cb3ce)。本地目录仍为 `F:\桌面文件\言剪AI`。
- 后续 [测试配置修正 22023132](https://github.com/MouMou-Eleven/yancut-ai/commit/2202313224b10eae69faa230e89d257c321cf92f) 只改变测试发现范围和技术记录，未改变已部署的运行时代码。
- [源码验收矩阵](https://github.com/MouMou-Eleven/yancut-ai/blob/b0b243357860f63ccf7cd46d67c22f35e28cb3ce/docs/yancut/upgrade-2026-09-16.md)；[完整人工测试清单](https://github.com/MouMou-Eleven/yancut-ai/blob/b0b243357860f63ccf7cd46d67c22f35e28cb3ce/docs/yancut/manual-test-checklist.md)。

## 本轮改变

| 建委反馈 | 已实现 | 验证范围 |
| --- | --- | --- |
| 片段只见开头 | 未选中时也显示片段全长底色和结束边界 | 浏览器实际检查 |
| 画布移动/缩放关键帧无效 | 从当前动画值开始手势操作，写入当前帧，保留其他通道 | 第 1/2 秒插值与真实 MP4 对照 |
| 播放头不能越过片尾 | 标尺、拖拽、时间码支持尾部空白，预览显示对应空画面 | 本地 5 秒→第 8 秒，线上 12 秒→第 16 秒；导出长度不增长 |
| 调节入口无功能 | 改为 12 个原生动效配方，有编号、预览、文案/区域/时长、拖拽与 AI 引用 | 手工加入、拖拽与原生导出通过；AI 与人工共用编译器 |
| 布局缺乏剪辑工作台层次 | 左侧紧凑资源分类、中央画布、右侧 AI/属性、底部完整时间线 | 保留言剪视觉与可调面板，1600×1000 浏览器检查 |
| 参考视频与模板复用 | 独立参考上传及授权抽取 6 帧，用户调试后命名保存真实时间线，可删除、换素材应用并撤销 | 本地 GLM 真实识别六帧时间码；模板保存和复用实测 |
| 台词、字幕、包装不同步 | 增加稳定关联，跟随锚点移动、改变时长、分割、保留区间和删除 | 关联分割和避免重复压缩动画等回归通过；不是完整 SVML 引擎 |
| 情绪混剪描述不可执行 | 计划可记录情绪方向、起点/过程/落点、缺口类型及连续性证据；支持二维推近、拉远、平移 | 区间和原生动作通过测试；静帧不能证明多机位运动连续 |
| 包装质量不稳定 | 固定配方，检查占位文案、可读停留、时间/关键帧越界、视觉空白及文字重叠 | 结构检查；不是人脸跟踪或逐像素黑帧/闪烁识别 |
| 高频场景要内置能力 | 6 个工作流入口、8 个内部技能合同；157 镜头配方和 214 样式元数据检索进入 AI 编排 | 目录是技法参考，不是 214 个现成渲染特效 |
| 模型格式失败 | 结构/证据校验失败最多修正一次，共用总时限；鉴权失败不重试 | 失败、修正成功及再失败分支测试；不自动执行、不返回假计划 |

个人模板当前保存在浏览器，最多 30 个；不会在每轮调试自动保存，也没有云端同步。参考素材与成片素材分开，参考画面不自动进入成片。没有实施素材沉淀系统。

## 六个参考项目的具体使用

| 项目 | 核验提交 | 读取重点及采用内容 |
| --- | --- | --- |
| [overlay-studio](https://github.com/jeszhou/overlay-studio) | `836e68cd1aea54e0c73fa712aaf8aca4151c9fc2` | `motion-playground/src/overlay/lint.ts`：固定配方、可读停留、占位与时间检查 |
| [montage-vlog-compiler](https://github.com/jeszhou/montage-vlog-compiler) | `a8fe4f5df7586fb6d6cf8d8cef811b0ef8fbe56a` | `references/semantic-anchor-method.md`：语义锚点、抽象要求转动作、可剪辑缺口与需要补素材的缺口分开 |
| [Hypit](https://github.com/hypit-ai/hypit) | `2f2bb3291f9d483b3ed39d5d50f3d56384d4101c` | `docs/zh/guide/studio-temporal-windows.md`：稳定身份与时间投影，关联元素随语义段变化 |
| [video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | `5e71af35a2daee492dd3ea93e5e8903f32dcd13c` | `references/shots`、`gallery/api/library.json`、工作台清单：核验 157/214，按意图检索少量技法并映射原生动作 |
| [anything2explainer](https://github.com/Vincentwei1021/anything2explainer) | `5b57239578284385c72ebfb2d1fce3ab61a3950a` | 编排要求：问题主线、事实依据、具体例子、输入→过程→结果，字幕和图文分区 |
| [video-talkcraft](https://github.com/Vincentwei1021/video-talkcraft) | `8829ca31fb8aeb1b850e85e47a7d7584c349bc4a` | `scripts/beat_lint.py`、`workbench/GUIDE.md`：词句与包装时段绑定、动作后停留、时间线与属性一致 |

没有运行这六个项目的完整生产流程，不能把它们的演示当作言剪输出质量。Shotcraft 目录元数据采用 Apache-2.0 并保留许可与来源；没有将其他受限运行时代码搬入言剪。动画使用原生可撤销关键帧，未执行任意 AI 生成脚本。

## 实测证据

- 143 项相关测试、2818 次断言通过；TypeScript、本地生产构建、Vercel 构建通过。
- 推送后 GitHub 首轮自动检查将 Playwright 场景误交给 Bun 执行，产生 `test.use()` 错误；307 项单元测试本身通过。增加 `bunfig.toml` 限定 `src` 后，本地完整运行 307 项、3166 次断言全部通过，浏览器场景保留独立 `test:e2e` 入口。
- [修正后的 GitHub 检查](https://github.com/MouMou-Eleven/yancut-ai/actions/runs/35014137631)：Ubuntu、macOS、Windows 的构建与测试步骤均已通过；没有删除测试或将真实错误设为忽略。
- 本地：画布手势修改关键帧后，真实导出 5.000 秒、1920×1080、H.264；提取第 1/2 秒画面，文字的位置与大小符合预览。
- 线上：上传 12 秒合成视频、创建项目、加入 YC-01、导出 12.000 秒 H.264，480×270 保留测试素材画幅；提取画面确认动效进入成片。正常导入、编辑与导出没有控制台错误。
- 线上未填 Key 返回 `401 PERSONAL_KEY_REQUIRED` 和中文设置指引；这属于主动验证的预期拒绝。浏览器有 WebGPU 平台提示与欢迎弹窗无障碍警告。
- 真实 GLM 参考分析在本地验证：取样 0.6/2.4/4.8/7.2/9.6/11.4 秒，模型读出对应测试时间码。初次调用曾失败，随后增加有限结构修正并用分支测试验证；没有宣称真实模型永不失败。
- 本人有效 Key 的公网剪辑质量、真人口播内容及多轮成片仍需实测；合成片的导出通过不能代替内容质量验收。

## 源码同步修复

本地与远端曾使用不同根提交保存相同业务代码，不能直接常规推送。本轮先核对文本和二进制差异，确认远端 15 张字体预览 AVIF 被错误按 UTF-8 转换而损坏，再保留两条历史，以经过验收的本地源码合并同步。补全浅克隆历史后正常推送，没有强推。部署的应用代码与同步源码一致，后补的仅为发布记录。

## 下一阶段仍需完成

完整视频及音频语义理解、多机位和运镜连续性、自动跟踪避脸、任意 3D/粒子/AE 特效、长视频流式分析、云端模板同步、数字人、正式声音克隆服务与生产渲染队列仍未完成。本轮完成参考入口和可执行基础，不能表述为任意爆款复刻或已全面商业化验收。
