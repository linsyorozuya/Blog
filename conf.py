# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "local",
    "path": "../Galileo"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "linsyorozuya/Blog@gh-pages"
}

# 站点设置
site_name = "Lin's よろづ屋"
site_logo = "${static_prefix}logo.png"
site_build_date = "2020-01-11T12:00+08:00"
author = "linsyorozuya"
email = "linsyorozuya@yahoo.com"
author_homepage = "https://www.linsyorozuya.com"
description = "吾性自足，不假外求"
key_words = ['Maverick', 'Galileo', 'blog']
language = 'zh-CN'
external_links = [
    {
        "name": "Maverick",
        "url": "https://github.com/AlanDecode/Maverick",
        "brief": "🏄‍ Go My Own Way."
    },
    {
        "name": "三無計劃",
        "url": "https://www.imalan.cn",
        "brief": "熊猫小A的主页。"
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
'''

footer_addon = ''

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
