# 2026-07-24 chatgptshare.com 访问故障复核

> 记录时间：2026-07-24
> 目标地址：`https://chatgptshare.com/list/?partner=6iwhbhzxFqH`
> 设备：台式电脑1

## 一、结论

本次无法访问的主因是目标站源服务器不可用，不是本机 DNS 污染、浏览器缓存或 Clash 主节点整体失效。当前 `chatgptshare.com` 在阿里 DNS、Cloudflare DNS、Google DNS 上都解析为 `154.26.186.65`；本机对该地址的 TCP 80 和 443 均无法建立连接。

通过 Clash `127.0.0.1:7890` 测试时，目标站 HTTPS 握手失败并返回 502；对多个香港、日本、新加坡、美国、欧洲节点逐一调用 Clash delay 接口，目标站均失败。作为对照，同一代理访问 `www.gstatic.com/generate_204` 返回 204、访问 `github.com` 返回 200，说明 Clash 和当前主节点并非整体断网。

另通过 Globalping 发起 5 个独立公网 HTTP 探针，结果全部为 `failed`。这些探针不经过台式电脑1或本机 Clash，进一步确认故障在目标站服务端。

证书透明度记录显示该域名及 `chatgpt`、`claude`、`gemini`、`grok` 等子域在 2026-07 仍有新证书，但这些名称当前也解析到同一地址或没有 A 记录，不能据此推断存在可用备用入口。

## 二、Clash 运行态核验

- Clash 仍运行在规则模式，控制器端口为随机端口 `127.0.0.1:55647`，代理端口为 `127.0.0.1:7890`。
- 当前主选择组仍为 `🇭🇰 香港S04 | IEPL`；本次没有切换节点。
- 运行时规则尾部为 `DomainKeyword . -> 🐟 漏网之鱼`、`Match -> 🐟 漏网之鱼`，并非 `DIRECT`。因此目标站即使没有专用域名规则，也会进入代理组，不存在被错误分到国内直连的问题。
- 持久配置的预处理器仍包含 `DOMAIN-SUFFIX,chatgptshare.com,🔰 选择节点`，但当前订阅运行内核没有加载这条专用规则；文件配置和运行内核必须分开核验。由于 Codex 可能有活动长连接，本次不强制重载 Clash。

## 三、处理边界

1. 不重启 Codex、CC Switch、Clash，不切换主节点，不强制重载内核，避免中断正在执行的任务。
2. 不修改 hosts 把域名指向猜测地址；当前所有公开 DNS 结果一致，且源地址端口关闭，hosts 不能修复源站宕机。
3. 不把第三方“备用域名”直接写入配置；证书记录只能证明域名曾签发证书，不能证明业务入口可用。
4. 在目标站恢复 TCP 443 后，再用当前主节点和至少一个备用节点各测试一次，并确认 `/rules` 命中专用规则。

## 四、后续验证命令

```powershell
Resolve-DnsName chatgptshare.com -Type A
Test-NetConnection chatgptshare.com -Port 443
curl.exe -I --proxy http://127.0.0.1:7890 https://chatgptshare.com/list/?partner=6iwhbhzxFqH
```

本次没有产生新的本机修复项：本地代理链路和 DNS 均正常，阻塞点在目标站源服务器。
