---
layout: post
title: Git 命令
slug: Git 命令
date: 2020-01-26
status: publish
author: H。H
tags:
  - Git
excerpt: 
---



> Git 笔记用于回顾。

### 创建新分支并切换

`git checkout -b newBranch` 创建一个新的叫 `newBranch` 的分支，并切换到该分支。



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

