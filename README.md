# shadowrocket-rules-joe

Shadowrocket 使用方法可以查看： https://houjoe.me/posts/shadowrocket-guide/

这个仓库放置我的 Shadowrocket 规则，方便在 GitHub 里管理和更新

## 🚀 自动部署

本项目已经集成了 **Cloudflare Pages** 自动部署功能！这意味着：

- ✅ 每次我提交代码更改到 GitHub 仓库时，配置文件会自动部署到 Cloudflare Pages
- ✅ 无需手动操作，规则更新会实时同步到线上
- ✅ 通过 Cloudflare 的全球 CDN 网络，提供更快速、更稳定的访问体验
- ✅ 你使用的配置链接始终指向最新版本的规则文件

## 📦 配置版本选择

我们提供了两个版本的配置文件，您可以根据需要选择：

### 🔥 **完整版（推荐新手）**
- **链接**：`https://shadowrocket-rules-joe.pages.dev/shadowrocket-rules.conf`
- **特点**：包含 26 个外部规则集，覆盖面广，开箱即用
- **适合**：不想折腾，希望有完整分流体验的用户
- **优势**：规则覆盖全面，各种 App 都有专门优化

### ⚡ **极简版（推荐进阶用户）**
- **链接**：`https://raw.githubusercontent.com/houjoe0829/shadowrocket-rules-joe/refs/heads/main/shadowrocket-rules-simplified.conf`
- **特点**：只保留 3 个核心规则集，主要依靠自定义规则
- **适合**：追求简洁高效，不需要过多外部依赖的用户
- **优势**：
  - 🚀 加载速度更快（减少 88% 的外部规则集）
  - 🔧 更稳定（减少外部依赖）
  - 📝 易于维护和自定义
  - 💡 保留所有核心分流功能

## 使用方法

1.  **获取配置链接**

    *   **完整版**：`https://shadowrocket-rules-joe.pages.dev/shadowrocket-rules.conf`
    *   **极简版**：`https://raw.githubusercontent.com/houjoe0829/shadowrocket-rules-joe/refs/heads/main/shadowrocket-rules-simplified.conf`
    *   选择其中一个版本复制链接即可

2.  **在 Shadowrocket 中添加配置**

    *   打开 Shadowrocket 应用。
    *   在配置界面，点击右上角的 " **+** "  加号按钮。
    *   在弹出的窗口中，粘贴你刚刚复制的配置链接。
    *   点击 "下载" 或 "完成" 按钮，Shadowrocket 将会自动下载并应用配置。

3.  **开启自动更新 (可选)**

    *   为了确保你的规则是最新的，建议开启自动更新功能。
    *   在 Shadowrocket 的 "设置" 界面中，找到 "配置" 选项。
    *   在配置列表中，找到你刚刚添加的规则配置。
    *   点击进入配置详情，找到 "自动更新" 选项并开启。
    *   你可以根据需要设置自动更新的时间间隔。

## 📊 版本对比

| 特性 | 完整版 | 极简版 |
|------|--------|--------|
| 外部规则集数量 | 26 个 | 3 个 |
| 配置文件大小 | 较大 | 较小 |
| 加载速度 | 普通 | 更快 |
| 稳定性 | 依赖外部规则集 | 更稳定 |
| 维护难度 | 简单（自动更新） | 简单（自定义规则） |
| 覆盖范围 | 全面 | 核心功能完整 |
| 适用人群 | 新手用户 | 进阶用户 |
| 推荐场景 | 开箱即用 | 追求性能 |

## 🔄 版本切换

如果您想从一个版本切换到另一个版本：

1. 在 Shadowrocket 中删除当前配置
2. 添加新版本的配置链接
3. 重新下载并应用配置

## 🗂️ 策略组说明

| 策略组 | 默认节点 | 说明 |
|--------|----------|------|
| AI 服务 | 美国节点 | OpenAI、Claude、Gemini 等 AI 工具 |
| Typeless | 新加坡节点 | Typeless 写作工具，独立分组 |
| 海外流媒体 | 自选 | Netflix、Disney+、HBO 等 |
| YouTube | 香港节点 | YouTube 及视频 CDN |
| TikTok | 自选 | TikTok 海外版 |
| Spotify | 直连 | Spotify 音乐 |
| Telegram | 自选 | Telegram 即时通讯 |
| 海外社交媒体 | 美国节点 | Twitter/X、Reddit、Facebook、Instagram 等 |
| 游戏平台 | 香港节点 | Steam、Epic、PlayStation、Xbox 等商店 |
| 游戏下载 | 直连 | 游戏内容下载走直连，速度更快 |

## 🛡️ 节点过滤

地区分组（香港 / 台湾 / 日本 / 新加坡 / 韩国 / 美国）均已配置以下过滤规则：

- **自动排除假节点**：过滤机场常见的「套餐到期、到期时间、剩余流量、expire、官网、官方、重置」等非实际节点条目
- **繁简体双覆盖**：支持繁体与简体节点名称（如臺灣 / 台湾、東京 / 东京、獅城 / 狮城等），避免漏匹配
- **地区互斥**：每个地区分组都排除其他地区的名称与代码，避免中转节点被误选。例如名为「美国 03 | 新加坡中转」的节点不会被算作美国节点
- **不使用裸小写代码**：英文关键词统一用 `(?i)` 做大小写不敏感匹配，不再直接匹配 `us`、`jp`、`kr`、`sg` 等小写子串，避免 `Australia`、`Russia` 等节点名被误判

## ⚠️ 使用注意

### Claude Code 等终端工具无法走代理？

如果发现 Claude Code 授权时提示「不在支持的区域」，或者终端里的命令行工具没有走代理，原因是 Shadowrocket 默认只是一个 HTTP 代理，只有主动配置了代理地址的应用（如浏览器）才会走它。

**解决方法：开启隧道的「强制路由」**

在 Shadowrocket → 隧道 页面，开启：

- ✅ **强制路由**：让终端等 CLI 工具的流量也进入隧道，由规则决定走代理还是直连

注意：无需开启「包括所有网络」，国内网站仍会按规则走直连，不影响国内访问速度。

---

**简单来说，只需要复制链接，粘贴到 Shadowrocket 里面就可以使用了！记得开启自动更新，省心又方便！**
