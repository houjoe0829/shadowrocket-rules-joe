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
- **特点**：包含 22 个外部规则集，覆盖面广，开箱即用
- **适合**：不想折腾，希望有完整分流体验的用户
- **优势**：规则覆盖全面，各种 App 都有专门优化

### ⚡ **极简版（推荐进阶用户）**
- **链接**：`https://raw.githubusercontent.com/houjoe0829/shadowrocket-rules-joe/refs/heads/main/shadowrocket-rules-simplified.conf`
- **特点**：只保留 3 个核心规则集，主要依靠自定义规则
- **适合**：追求简洁高效，不需要过多外部依赖的用户
- **优势**：
  - 🚀 加载速度更快（减少 85% 的外部规则集）
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
| 外部规则集数量 | 22 个 | 3 个 |
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

---

**简单来说，只需要复制链接，粘贴到 Shadowrocket 里面就可以使用了！记得开启自动更新，省心又方便！**
