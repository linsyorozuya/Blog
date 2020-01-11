---
layout: post
title: 禁止 Chrome 自动更新 (Mac)
slug: typography
date: 2019-09-21 16:50
status: publish
author: H。H
categories: 
  - 其他
tags:
  - 其他
excerpt: 
---

> 自从把电脑的默认浏览器设置为 Chrome，Clean My Mac 就时不时弹出窗口提示更新程序没响应。再次记录方法。

### [谷歌官方方法](https://support.google.com/chrome/a/answer/7591084?hl=zh-Hans)

这里拷贝一份

```
适用于 Chrome 浏览器以及通过 Google 软件更新管理的所有应用。

Chrome 浏览器会自动更新功能并应用安全更新，确保您的用户能及时获取重要的安全更新，并且不会错过新功能。

如果某个 Chrome 浏览器版本将会给您的单位造成问题，您可以停用自动更新功能，直至问题得到解决。如果贵单位希望手动推送 Chrome 浏览器更新，您也可以停用自动更新功能。

在您的首选 XML 编辑器中打开 com.google.Keystone.plist 文件。
com.google.Keystone.plist 文件地址在 /Library/LaunchAgents

在 updatePolicies 键下方，添加 Chrome 浏览器 UpdateDefault 键条目，并将键值设为 2。以下示例显示的是停用了自动更新功能的 Chrome 浏览器 (com.google.Chrome) 的设置：

<key>updatePolicies</key>
<dict>
  <key>global</key>
  <dict>
    <key>UpdateDefault</key>
    <integer>2</integer>
  </dict>
</dict>
保存更改。
此表显示了 UpdateDefault 键的所有有效设置。
```

发现没效果了，发现直接 CleanMyMac 里面禁用扩展好像生效了。。。。。。

