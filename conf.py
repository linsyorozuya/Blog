# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
category_by_folder = True
# fetch_remote_imgs = True

template = {
    "name": "Galileo",
    "type": "local",
    "path": "../Galileo"
}

enable_jsdelivr = {
    "enabled": True,
    "repo": "linsyorozuya/i-code-log@gh-pages"
}

# 站点设置
site_name = "「Coder」灰桑"
site_logo = "${static_prefix}logo.png"
site_build_date = "2020-01-11T12:00+08:00"
author = "linsyorozuya"
email = "linsyorozuya@yahoo.com"
author_homepage = "https://code.linsyorozuya.com"
description = "图难于其易，于大为其细"
key_words = ['灰桑', 'Coder 灰桑', 'blog']
language = 'zh-CN'
external_links = [
    {
        "name": "灰桑",
        "url": "https://life.linsyorozuya.com",
        "brief": "Who"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    },
    {
        "name": "简历",
        "url": "${site_prefix}resume/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/linsyorozuya",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/linsyorozuya",
        "icon": "gi gi-github"
    },
    {
        "name": "Weibo",
        "url": "https://weibo.com/2630651323/",
        "icon": "gi gi-weibo"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-83202512-2"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-83202512-2');
</script>

'''

footer_addon = footer_addon = r'''
'''

body_addon = ''

# 评论设置
valine = {
    "enable": True,
    "el": '#vcomments',
    "appId": "eMmVkL0FDqrmunWuz9m5sBGn-gzGzoHsz",
    "appKey": "RsDa5XAzjj8cWQLigV7YezRM",
    "visitor": True,
    "recordIP": True
}
