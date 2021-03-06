---
layout: post
title: Git 命令备忘
slug: Git 命令备忘
date: 2020/01/26
status: publish
author: 灰桑
tags:
  - Git
excerpt: 
---



> 笔记用于回顾。



### 查看当前文件状态

要查看哪些文件处于什么状态，可以用 `git status` 命令。 

`git status` 命令的输出十分详细，但其用语有些繁琐。 如果你使用 git status -s 命令或 git status --short 命令，你将得到一种更为紧凑的格式输出。



### 查看提交历史

`git log` 会按提交时间列出所有的更新。

`git log -p`用来显示每次提交的内容差异。

`git log -p -2`用来显示每次提交的内容差异，-2 显示最近两次提交。



### 创建新分支并切换

`git checkout -b newBranch` 创建一个新的叫 `newBranch` 的分支，并切换到该分支。



### 创建嵌套目录

`mkdir -p a/b` 创建嵌套的文件夹 a 和 b。



### 合并分支

`git merge` 在这个命令下，Git 会找到两个分支的共同祖先，将这三者进行一个三方合并。这种三方合并会产生一个新的提交，当前会指向这个新的提交。

`git rebase` 则不采用三方合并，它会比较要「合并的分支」和「两个分支的共同祖先」这两个提交，将其中的修改提取成一个补丁。然后在「当前分支」的提交上应用这个补丁，从而生成一个新的「提交」。这种方式被叫做「rebase」，中文叫「变基」。



### 解决 Merge 冲突

 `git merge --abort` 可以恢复到 merge 之前的状态。



### 查看到所有关联到当前仓库的远程仓库

通过 `git remote` 命令，我们可以查看到所有关联到当前仓库的远程仓库。

通过 `git remote show` 命令，我们可以查看某一个远程仓库的详细信息。



### git stash

`git stash` 这个命令可以将你当前进行到一半的工作保存到一个暂存区域，然后将当前目录回滚到上一次提交。

`git stash apply`把之前放到储藏区的最新的那个修改切回来。

`git stash list`可以把所有放到储藏区的修改都列出来。

`git stash --list` 查看`git stash`命令列表。

