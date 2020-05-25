---
layout: post
title: SwiftUI - 开发图片模糊的 MAC 小应用
slug: SwiftUI - 开发图片模糊的 MAC 小应用
date: 2020/05/23
status: publish
author: 灰桑
categories: 
  - iOS
tags:
  - iOS
---

> 看完喵神的 《 SwiftUI 与 编程思想》，尝试使用了书中类 Redux 的架构写了给图片添加模糊和修改饱和度的 MAC 上的小应用。文章记录一些其中的要点，文章部分引用了书中的段落来记录。

## 🌠成果

![演示.gif](https://cdn.jsdelivr.net/gh/linsyorozuya/Pics@master/uPic/2020-05-25%2000-30-47.2020-05-25%2000_34_42.gif)

应用功能很简单：

1. 可以拖动图片到应用中
2. 调节模糊程度
3. 调节饱和度
4. 拖动图片到其他软件

## 架构

![图](https://cdn.jsdelivr.net/gh/linsyorozuya/Pics@master/uPic/截屏2020-05-25%20下午2.21.32.png)

### 数据流动方式的特点

1. 将 app 当作一个状态机，状态决定用户界面。
2. 这些状态都保存在一个 Store 对象中。
3. View 不能直接操作 State，而只能通过发送 Action 的方式，间接改变存储在 Store 中的 State。
4. Reducer 接受原有的 State 和发送过来的 Action，生成新的 State 。并返回执行相关额外操作的副作用 Command。
5. Store 接受并执行副作用 Command （网络操作、文件操作等与状态变更无关的操作）来继而发送新的 Action 再次触发 Reducer 返回新的 State。
6. 用新的 State 替换 Store 中原有的状态，并用新状态来驱动更新界面。
7. 使用 Binding 来完成界面和状态的双向绑定。

使用这种架构的优势将 View 中的状态操作完全解耦到了 Store 上去操作，所以对 State 的状态修改得以集中到了一个地方去处理。对项目的阅读和维护都有很好的帮助。避免了项目复杂之后散落各处的状态修改。

### 相关解释

#### ![文件结构](https://cdn.jsdelivr.net/gh/linsyorozuya/Pics@master/uPic/截屏2020-05-25%20下午2.09.29.png)

**Store**: 主要持有了 State 属性和一个接受和处理 Action 的 Reduce 函数。

```swift
 class Store: ObservableObject {

 		@Published var appState = AppState()

    static func reduce(state: AppState, action: AppAction) -> (AppState, AppCommand?) {
        var appState = state
        var appCommond: AppCommand?
        
        switch action {
        case .action(let something):
 
        ....
        }
        
        return (appState,appCommond)
    }
    
    func dispatch(_ action: AppAction) {
        #if DEBUG
        print("Action: \(action)")
        #endif
        
        let result = Store.reduce(state: appState, action: action)
        appState = result.0
        if let command = result.1{
            #if DEBUG
            print("AppCommand:\(command)")
            #endif
            
            command.execute(in: self)
        }
    }
}
```

**State**: 存放相关状态的位置。

**Action**：一个定义相关操作的枚举

```swift
enum AppAction {
    case .action(something: String)
    ...
}
```

**Command**：执行相关副作用操作的地方

```swift
protocol AppCommand {
    func execute(in store: Store)
}

struct WriteUserAppCommand: AppCommand {
    let user: User
    
    func execute(in store: Store) {
        try? FileHelper.writeJSON(user, to: .documentDirectory, fileName: "user.json")
    }
    
}
```

## 三种改变 State 的途径

更准确的应该是两种，Command 的方式最终也是通过 Action 来处理相关状态改变。

### 通过 Action 来改变 State

通过向 Store 发送并处理 Action 来直接修改或间接通过 Command 来修改相关状态。

### 通过 Binding 双向绑定改变 State

利用 SwiftUI 的双向绑定的特性，可以直接把 State 和 View 绑定起来。当 View 的状态改变直接修改了 Store 中的原始状态。

### 通过 Command 副作用来改变 State

> “Reducer 的唯一职责应该是计算新的 State，而发送请求和接收响应，显然和返回新的 State 没什么关系，它们属于设置状态这一操作的“副作用”。在我们的架构中我们使用 Command 来代表“在设置状态的同时需要触发一些其他操作”这个语境。Reducer 在返回新的 State 的同时，还返回一个代表需要进行何种副作用的 Command 值 (对应上一段中的第一个时间点)。Store 在接收到这个 Command 后，开始进行额外操作，并在操作完成后发送一个新的 Action。这个 Action 中带有异步操作所获取到的数据。它将再次触发 Reducer 并返回新的 State，继而完成异步操作结束时的 UI 更新 (对应上一段中的第二个时间点)。”

Store 在接收到这个 Command 后，开始进行额外操作，并在操作完成后发送一个新的 Action。这个 Action 中带有异步操作所获取到的数据。它将再次触发 Reducer 并返回新的 State，继而完成异步操作结束时的 UI 更新 (对应上一段中的第二个时间点)。

## 用绑定来更新的状态时通过 Publisher 来订阅并处理事件

对于通过 Action 改变的状态，如果我们想要执行网络请求这样的副作用，可以通过同时返回合适的 Command 完成。但是对于通过绑定来更新的状态，由于不会经过 Store 的 reducer 来处理状态并返回 Command，我们缺少一种有效的手段来在它们改变时执行副作用。

在 SwiftUI 中可以使用 combine 来解决这个问题。最简单的方法是在属性前加上 @Published 来为相关属性创建 Publisher 。然后在合适的位置订阅相关事件来执行额外的操作。

## 总结

通过这个架构体验到了 SwiftUI 开发数据驱动页面更新的便利和优势，而且 SwiftUI 还能用来开发 Mac 端的应用。虽然目前 SwiftUI 还在开始不成熟的阶段，但是有理由相信以后 SwiftUI 统一苹果全平台的时候。期待下个月的 WWDC 的 SwiftUI。