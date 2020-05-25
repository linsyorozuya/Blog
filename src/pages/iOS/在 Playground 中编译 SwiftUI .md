---
layout: post
title: 在 Playground 中编译 SwiftUI 
slug: 在 Playground 中编译 SwiftUI
date: 2020/05/14
status: publish
author: 灰桑
categories: 
  - iOS
tags:
  - iOS
  - SwiftUI
excerpt: 
---

> 记录下在 Playground 中编译 SwiftUI 的代码。

```swift
import SwiftUI
import PlaygroundSupport

struct ContentView: View {
    @State var counter = 0
    var body: some View {
        VStack {
            Button(action: { self.counter += 1 }, label: {
                Text("Tap me!")
                    .padding()
                    .background(Color(.tertiarySystemFill))
                    .cornerRadius(5)
            })
            if counter > 0 {
                Text("You've tapped \(counter) times")
            } else {
                Text("You've not yet tapped")
            }
        }
    }
}

PlaygroundPage.current.setLiveView(ContentView())

```

![截屏2020-05-14 上午11.43.34](https://cdn.jsdelivr.net/gh/linsyorozuya/Pics@master/uPic/截屏2020-05-14%20上午11.43.34.png)

