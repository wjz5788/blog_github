# blog_github
好，我们来做一个完整方案，把你的 GitHub Pages 博客升级为：

* **导航栏 + 文章目录**
* **全文搜索**
* **评论系统**
* **浏览量统计**
* **Google AdSense 广告**

我假设你的博客是 **Hugo 静态站点**，如果是纯 HTML 我可以再改方案。

---

# 1️⃣ 目录 / 导航栏

在 `config.toml` 里添加菜单：

```toml
baseURL = "https://wjz5788.github.io/"
title = "我的博客"
theme = "ananke"  # 或你正在使用的主题

[params]
  author = "wjz5788"

[menu]
  [[menu.main]]
    name = "首页"
    url = "/"
    weight = 1

  [[menu.main]]
    name = "分类"
    url = "/categories/"
    weight = 2

  [[menu.main]]
    name = "关于"
    url = "/about/"
    weight = 3
```

文章自动生成目录（TOC）：

```toml
[markup]
  [markup.tableOfContents]
    startLevel = 2
    endLevel = 4
```

在模板里显示 TOC（一般在 `layouts/_default/single.html` 里）：

```html
<aside class="toc">
  {{ .TableOfContents }}
</aside>
```

---

# 2️⃣ 搜索功能（Lunr.js）

1. 在 `config.toml` 添加：

```toml
[outputs]
  home = ["HTML", "JSON"]  # 用于生成搜索索引 JSON
```

2. 创建 `layouts/_default/list.json.json`：

```html
[
{{- range .Pages -}}
{
  "title": {{ .Title | jsonify }},
  "url": {{ .RelPermalink | jsonify }},
  "content": {{ .Plain | jsonify }}
}{{ if not (last .) }},{{ end }}
{{- end -}}
]
```

3. 前端搜索框 + 脚本（放在 `layouts/partials/search.html`）：

```html
<input type="text" id="searchBox" placeholder="搜索文章">
<div id="results"></div>

<script src="https://cdn.jsdelivr.net/npm/lunr/lunr.min.js"></script>
<script>
fetch('/index.json')
  .then(response => response.json())
  .then(pages => {
    window.pagesIndex = lunr(function() {
      this.ref('url')
      this.field('title')
      this.field('content')
      pages.forEach(p => this.add(p))
    });
    window.pagesData = pages
  });

document.getElementById('searchBox').addEventListener('input', function() {
  const resultsDiv = document.getElementById('results')
  const query = this.value
  if(!query) { resultsDiv.innerHTML = ''; return }
  const results = window.pagesIndex.search(query)
  resultsDiv.innerHTML = results.map(r => {
    const page = window.pagesData.find(p => p.url === r.ref)
    return `<div><a href="${page.url}">${page.title}</a></div>`
  }).join('')
})
</script>
```

---

# 3️⃣ 评论系统（Valine 推荐国内访问快）

1. 注册 [LeanCloud](https://leancloud.cn/)
2. 创建应用，拿到 `APP_ID` 和 `APP_KEY`
3. 在文章模板里添加：

```html
<div id="vcomments"></div>
<script src="https://unpkg.com/valine/dist/Valine.min.js"></script>
<script>
  new Valine({
    el: '#vcomments',
    appId: 'YOUR_APPID',
    appKey: 'YOUR_APPKEY',
    placeholder: '写下你的评论...',
    notify: true,
    verify: true
  });
</script>
```

---

# 4️⃣ 浏览量统计

**Google Analytics**：

```html
<script async src="https://www.googletagmanager.com/gtag/js?id=YOUR_TRACKING_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'YOUR_TRACKING_ID');
</script>
```

如果国内访问量为主，可以用 **百度统计**，在 `<head>` 里加统计代码即可。

---

# 5️⃣ Google AdSense 广告

1. 申请 AdSense 并拿到广告代码
2. 在模板里合适位置添加（例如文章页底部）：

```html
<div class="adsense">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- 文章广告 -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-XXXXXXXXXXXX"
     data-ad-slot="YYYYYYYYYY"
     data-ad-format="auto"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div>
```

3. 可在 CSS 调整位置、间距：

```css
.adsense {
  margin: 20px 0;
  text-align: center;
}
```

---

# ✅ 最终效果

1. 页面顶部有 **导航栏**
2. 文章内显示 **目录（TOC）**
3. 顶部或侧边可 **搜索文章**
4. 文章底部显示 **评论区**
5. 每篇文章有 **浏览量统计**
6. 合理位置显示 **广告**

---

我可以帮你写一个 **完整的 Hugo 模板修改示例**，直接复制到你的仓库就可以使用，包括导航、TOC、搜索、评论、浏览量和广告。

你希望我直接帮你生成这个完整模板吗？
