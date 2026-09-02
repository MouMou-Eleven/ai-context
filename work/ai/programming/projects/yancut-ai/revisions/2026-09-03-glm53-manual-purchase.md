# 2026-09-03：GLM-5.3-Flash 与客服人工购买流程

## 变更结论

言剪 AI 的主规划模型切换为智谱 `glm-5.3-flash`。服务端仍通过统一的 OpenAI 兼容适配层
调用，默认接口为 `https://open.bigmodel.cn/api/paas/v4`，推理强度为 `max`。模型规划请求
会在有证据时携带真实图片 URL、视频 URL 和字幕/转写文本，系统提示要求模型区分观察结果与
推断，不得编造镜头、人物或素材 ID。结构化计划仍必须通过 Zod 校验，用户确认后才执行。

本地以用户提供的密钥进行了最小连通性验证：官方接口返回 HTTP 200、模型为
`glm-5.3-flash`、choices 数量为 1。密钥没有写入源码、文档、Git 历史或 `ai-context`。

## 购买流程

根据产品决策，价格页不接入自动收银台。用户点击“联系客服购买”后，前端读取
`/api/yancut/billing/support?sku=...`，展示套餐、积分、客服二维码、客服联系方式和人工开通
说明。二维码、客服名称和联系方式由 `/admin` 的服务配置维护；当前本地环境未填入真实值，
因此页面会明确显示“客服二维码尚未配置”和“联系方式尚未配置”，不会生成虚假收款信息。

旧 `/api/yancut/billing/checkout` 路由保留为兼容入口，但只返回 `PURCHASE_CONTACT_ONLY`，
不创建订单、不跳转收银台、不发起扣款。后续在秒嗒上线时，人工核验付款并通过后台或运营流程
开通积分即可；是否引入正式支付网关属于另行确认的产品决策。

## 配置项

```dotenv
YANCUT_LLM_BASE_URL=https://open.bigmodel.cn/api/paas/v4
YANCUT_LLM_API_KEY=<仅服务端密钥>
YANCUT_LLM_MODEL=glm-5.3-flash
YANCUT_LLM_REASONING_EFFORT=max
YANCUT_PAYMENT_PURCHASE_QR_URL=<客服收款二维码，部署时填写>
YANCUT_PAYMENT_CUSTOMER_SERVICE_NAME=<客服名称，部署时填写>
YANCUT_PAYMENT_CUSTOMER_SERVICE_CONTACT=<客服联系方式，部署时填写>
```

## 验证与上线条件

- TypeScript `--noEmit` 通过。
- 言剪 AI 单元测试通过（187 个用例；本轮新增后以提交时实际结果为准）。
- Next.js 生产构建通过，价格页和管理后台路由可访问。
- Playwright 商业主流程通过：中文页面、管理员配置、价格页弹窗、客服未配置提示和新建项目路径均已覆盖。
- 秒嗒部署前必须使用真实管理员账号与共享数据库，并录入真实客服二维码、名称、联系方式；
  删除本地演示管理员模式。模型密钥只进入秒嗒服务端密钥管理。

## 事实来源

- 智谱开放平台对话补全文档：<https://docs.bigmodel.cn/api-reference/模型-api/对话补全>
- 智谱开放平台 HTTP 接口说明：<https://docs.bigmodel.cn/cn/guide/develop/http/introduction>
- 言剪 AI 源码仓库：<https://github.com/MouMou-Eleven/yancut-ai>
