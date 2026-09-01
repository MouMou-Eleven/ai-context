# 参数化与 Studio 编辑契约

参数化不是把若干变量写在组件顶部，也不是把图层拆开后就算可编辑。默认交付必须让用户在 Remotion Studio 选中 Composition 后，通过右侧 `Inspector → Default Props` 面板改值，预览画面立即反映变化。

## 必须满足的结构

```tsx
// Composition.tsx
export const VideoSchema = z.object({
  title: z.string().min(1).max(80),
  chapter: z.string().min(1).max(8),
  accent: zColor(),
});

export type VideoProps = z.infer<typeof VideoSchema>;

export const Video: React.FC<VideoProps> = ({title, chapter, accent}) => {
  // 每个字段必须真实绑定到画面元素。
};

// Root.tsx
<Composition
  id="Video"
  component={Video}
  schema={VideoSchema}
  defaultProps={{
    title: "默认标题",
    chapter: "01",
    accent: "#22D3EE",
  }}
/>
```

- `schema` 和 `defaultProps` 必须同时直接写在 `<Composition>` 上，不能只在组件内部定义、只放到 `calculateMetadata()`、或只保存到自定义配置对象。
- `defaultProps` 必须是可序列化的内联对象；不要传入 `undefined`、函数、类实例、Promise、`Date`、`Map`、`Set` 或未处理的文件对象。
- Schema 的字段名、默认值、组件 Props 解构名和画面绑定名必须一一对应；删除、重命名或新增字段时同步更新四处。
- 需要颜色选择器的字段使用当前版本 `@remotion/zod-types` 的 `zColor()`；颜色字符串必须是可解析的 CSS 颜色。
- 用户会改的文字、编号、颜色、素材路径和开关必须暴露为 Props；不要把同一份文案复制成多个互不联动的常量。

## 右侧面板验收

实现后必须实际启动 Studio，选择目标 Composition，在右侧 `Default Props` 中逐项修改一组非默认值，并观察画面，不得只检查源码。

至少验证：

1. 主标题和副标题修改后，预览中的对应文字即时变化，未出现旧文案残留。
2. 编号、期数、排名或百分比修改后，容器宽度、对齐和动效仍然正确。
3. 背景色、主色和强调色修改后，绑定的背景、边框、光效或装饰同步变化，文字对比度仍可读。
4. 刷新 Studio 或重新选择 Composition 后，字段仍显示默认值/当前值，且不会报 `undefined is not valid JSON`。
5. 恢复默认值后再渲染；MP4 只作为当前 Props 快照，不能声称 MP4 文件本身可在侧栏编辑。

## 常见失败模式

- 只有 `Interactive.Div` 图层名称，没有 `schema` + 内联 `defaultProps`：图层可选不等于内容可编辑。
- Schema 写在组件外但未传给 `<Composition>`：Studio 不会生成 Default Props 表单。
- 字段只在 Default Props 面板出现，却没有传入实际 DOM/SVG/Canvas/Three 元素：属于“空参数”，必须删除或接入画面。
- 只把整张参考图作为 `<Img>` 放入画面，再暴露一个不会影响图片的标题字段：不满足参数化；需要重建被修改的文字/颜色层，或明确交付固定成片。
- 将所有画面内容包进一个 JSON 字符串字段：会失去字段类型、颜色选择器和可读的 Studio 编辑体验。

## 交付报告

报告中单独列出：

- Studio 右侧可编辑字段及其绑定元素。
- 非默认测试值和对应观察结果。
- 参数化工程源码路径；明确 MP4 是哪一组 Props 的渲染快照。
- 若侧栏不可编辑、只看到图层选择器或出现 JSON 错误，交付判定为失败，继续修复而不是用文字解释掩盖。
