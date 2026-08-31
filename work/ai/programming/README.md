# AI Programming — AI 编程

> 本目录按“工具、经验、项目”三级分类。工具是实现手段，经验是跨工具方法，项目是有明确产品目标的实际开发。

## 目录结构

```text
programming/
├── README.md      AI 编程总入口
├── tools/         编程工具知识包
│   └── miaoda/    百度秒哒
├── experience/    跨工具开发经验、Skill 仓库与参考材料
│   └── skill-repository/ 可直接调用并追踪上游版本的 Skill 实体
└── projects/      建委实际开发的长期项目
    └── yancut-ai/ 言剪 AI
```

## 读取路由

| 任务 | 首读 |
|---|---|
| 百度秒哒功能、开发、排错 | [`tools/miaoda/llms.txt`](./tools/miaoda/llms.txt) |
| 创意前端、视频交互、3D首屏 | [`experience/README.md`](./experience/README.md) |
| 收录、查找、调用或同步 Skill | [`experience/skill-repository/README.md`](./experience/skill-repository/README.md) |
| 查找或继续开发源码项目 | [`projects/README.md`](./projects/README.md) |
| 言剪 AI | [`projects/yancut-ai/README.md`](./projects/yancut-ai/README.md) |

## 边界

- 工具知识不能当作项目事实；项目使用某工具时用链接引用。
- 某次项目排错只有重复验证后才能提炼为经验。
- 非科班、AI 辅助开发是建委当前能力边界，不把仓库中的技术资料等同于传统全栈能力。
- AI 培训中的“AI 编程课程”属于培训项目；只有涉及真实开发方法时才组合本目录。

## 激活规则

- “AI 编程、开发网站、开发应用、自动化工具”进入本目录。
- “Skill 仓库、收录 Skill、同步 Skill、调用 Skill”进入 `experience/skill-repository/`。
- 只提“秒哒”进入 `tools/miaoda/`，不自动读取言剪 AI。
- 只提“言剪 AI”进入该项目，不自动加载全部秒哒经验；只有涉及秒哒交付时再组合。
- 只提“AI 编程课程”首先进入 `../training/`，除非任务明确需要开发事实。

*结构确认：2026-08-18*
