# 最新完整源码基线：ep8e1gojj18g

## 用户约束

用户已明确：下载秒哒完整源码消耗积分和费用，不能每轮要求重新下载。此次完整导出必须长期保存；后续以该基线和每轮增量/云端差异维护。只有现有记录确实不足以恢复关键代码时，先说明缺失范围和原因，优先要少量文件或补丁，而非默认全量导出。

## 已验证归档

- 应用：app-enipq7iozwn5；导出版本：ep8e1gojj18g。
- 文件：app-enipq7iozwn5_app_version-ep8e1gojj18g_8f458d16.zip。
- 用户原件：`F:/桌面文件/app-enipq7iozwn5_app_version-ep8e1gojj18g_8f458d16.zip`。
- 独立长期备份：`C:/Users/Administrator/Documents/Codex/yancut-source-archive/2026-09-27-ep8e1gojj18g/`。
- 最新基线定位文件：`C:/Users/Administrator/Documents/Codex/yancut-source-archive/CURRENT-BASELINE.json`。
- 字节数：529000173。
- ZIP SHA256：`42d0580d40df787a5216378a70e805884c0b7e5a20b2a685c71c041aa2f7fd3e`。
- 原件与备份 SHA256 一致；所有 ZIP 条目 CRC 校验通过。
- 原包 Git HEAD：`fd538fe0c72473d8194bca13ce44ff9cfd0566d1`（直接读取包内 HEAD/ref，未执行包内 hooks）。
- 原包10,514条目；审阅用source目录2,661文件，另有逐文件SHA256清单。
- source-manifest.json SHA256：`2d9d9a9c803cf9e2135d797f9ca2d41e37c6ddca549e9ae87221f9c72f7e38c4`。
- 原始.env、Git历史等仍在完整ZIP；审阅源树不展开环境文件/依赖/构建/历史。原包不提交上下文仓库，避免配置/历史凭据泄漏。
- F盘原件和C盘副本只是同机两个路径，不声称异地灾备。

## 源码核对

相较旧本地B5，preview/apps与supabase下发现28个新增/内容变化文件（非声称全树新增删除总数），哈希差异列表保存在归档cloud-vs-b5-hashes.json。新迁移到00026；不得继续假设只到00023，也不能重放同号历史脚本。

已在代码中确认：后台tabLoading/tabLoaded、accountLoading等待判定、账户hook初始loading与focus静默刷新、二维码上传调用invalidateCustomerQrCache、双Edge platform.ts续签处理。构建/真实登录等尚未在此导出上重新验收，这里只声明源码存在，不把截图成功反馈当独立运行证明。

## B6后续基线

本记录取代“等待用户上传源码”状态；B6在新导出基线上实现运行日志与AI辅助，不在归档source原地开发。新包应与此源树比对，保留v35–v38修复。每轮交付记before/after哈希、迁移、ZIP校验、测试结果；秒哒直接修复只要求修改文件列表/定点diff及回执，合并回本地工作树。完整原包永久保留作为还原起点。

B6功能仍待实现/测试，不能因完成备份就标为交付。此前性能、Worker、真实供应商和跨浏览器未验收项不取消。
