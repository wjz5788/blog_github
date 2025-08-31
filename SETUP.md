# 博客功能配置指南

你的Hugo博客已经集成了以下功能：

## ✅ 已完成的功能

1. **导航栏** - 已配置在 `config.toml` 中
2. **文章目录 (TOC)** - 已启用，支持2-4级标题
3. **全文搜索** - 使用 Lunr.js，支持标题、内容、摘要、标签搜索
4. **评论系统** - 使用 Valine (LeanCloud)
5. **浏览量统计** - 本地存储 + Google Analytics
6. **Google AdSense** - 支持文章顶部、底部、侧边栏广告

## 🔧 需要配置的参数

### 1. 评论系统 (Valine)

1. 注册 [LeanCloud](https://leancloud.cn/)
2. 创建应用，获取 `APP_ID` 和 `APP_KEY`
3. 在 `config.toml` 中更新：

```toml
[params.valine]
  appId = "你的APP_ID"
  appKey = "你的APP_KEY"
```

### 2. Google Analytics

1. 在 [Google Analytics](https://analytics.google.com/) 创建账户
2. 获取跟踪ID (格式: G-XXXXXXXXXX)
3. 在 `config.toml` 中更新：

```toml
googleAnalytics = "G-XXXXXXXXXX"
```

### 3. 百度统计 (可选)

1. 在 [百度统计](https://tongji.baidu.com/) 注册
2. 获取统计代码
3. 在 `config.toml` 中更新：

```toml
baiduAnalytics = "你的百度统计代码"
```

### 4. Google AdSense

1. 申请 [Google AdSense](https://www.google.com/adsense)
2. 获取发布商ID和广告位ID
3. 在 `config.toml` 中更新：

```toml
[params.adsense]
  enabled = true  # 设置为 true 启用广告
  client = "ca-pub-XXXXXXXXXXXX"  # 你的发布商ID
  slot = "YYYYYYYYYY"  # 你的广告位ID
  position = "article-bottom"  # 位置: article-top, article-bottom, sidebar
```

## 🚀 使用方法

### 搜索功能
- 在首页顶部有搜索框
- 支持实时搜索
- 搜索结果包含标题、摘要、日期

### 评论功能
- 在每篇文章底部显示评论区
- 支持昵称、邮箱、网站链接
- 支持表情符号

### 浏览量统计
- 每篇文章显示浏览量
- 数据存储在本地浏览器中
- 配合Google Analytics使用

### 广告显示
- 文章顶部广告
- 文章底部广告
- 侧边栏广告 (需要主题支持)

## 📁 文件结构

```
layouts/
├── _default/
│   ├── single.html      # 文章页面模板
│   └── list.html        # 首页模板
├── partials/
│   ├── search.html      # 搜索功能
│   ├── comments.html    # 评论系统
│   ├── analytics.html   # 统计代码
│   ├── adsense.html     # 广告代码
│   └── head.html        # 头部模板
└── _default/
    └── list.json.json   # 搜索索引JSON
```

## 🔍 测试功能

1. **搜索功能**: 访问首页，在搜索框输入关键词
2. **评论功能**: 访问任意文章，查看底部评论区
3. **浏览量**: 刷新文章页面，查看浏览量变化
4. **广告**: 配置AdSense后，查看广告显示

## ⚠️ 注意事项

1. **评论系统**: 需要LeanCloud应用配置正确的域名
2. **Google Analytics**: 需要等待24-48小时才能看到数据
3. **AdSense**: 需要网站有足够流量才能申请通过
4. **搜索功能**: 依赖 `index.json` 文件，确保生成正确

## 🛠️ 故障排除

### 搜索不工作
- 检查 `public/index.json` 文件是否存在
- 确认Lunr.js库加载正常

### 评论不显示
- 检查LeanCloud配置是否正确
- 确认域名已在LeanCloud中配置

### 统计不工作
- 检查Google Analytics跟踪ID格式
- 确认统计代码已正确加载

### 广告不显示
- 确认AdSense申请已通过
- 检查广告位ID是否正确

## 📞 技术支持

如果遇到问题，请检查：
1. Hugo版本是否最新
2. 主题是否兼容
3. 配置文件语法是否正确
4. 浏览器控制台是否有错误信息
