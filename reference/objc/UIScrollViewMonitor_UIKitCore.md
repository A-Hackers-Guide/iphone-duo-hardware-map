# `UIScrollViewMonitor`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIViewSubtreeMonitor`, `_UIScrollViewScrollObserver`
- 3 instance variables, 5 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"UIScrollView" _scrollView;
@"UIWindow" _window;
@"<UIScrollViewMonitorDelegate>" _delegate;
```

## Properties

```
@property (T@"<UIScrollViewMonitorDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIScrollViewMonitor _observeScrollViewDidScroll:];
-[UIScrollViewMonitor initWithScrollView:];
-[UIScrollViewMonitor stopMonitoring];
-[UIScrollViewMonitor _monitoredView:didMoveFromSuperview:toSuperview:];
-[UIScrollViewMonitor _monitoredView:willMoveFromSuperview:toSuperview:];
-[UIScrollViewMonitor setDelegate:];
-[UIScrollViewMonitor delegate];
-[UIScrollViewMonitor _monitorsView:];
```
