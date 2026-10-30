# `_UITabBarHostedPlatterViewsHandle`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 5 properties, 11 instance methods, 0 class methods

## Instance variables

```
B _suppressesBackground;
@"UIView" _hostView;
@"NSArray" _borrowedViewHandles;
@? _updateHandler;
```

## Properties

```
@property (T@"NSArray",R,N,V_borrowedViewHandles) borrowedViewHandles;
@property (T@?,R,N,V_updateHandler) updateHandler;
@property (T@"UIView",W,N,V_hostView) hostView;
@property (TB,R,N,V_suppressesBackground) suppressesBackground;
@property (TB,R,N) isValid;
```

## Instance methods

```
-[_UITabBarHostedPlatterViewsHandle updateHandler];
-[_UITabBarHostedPlatterViewsHandle hostView];
-[_UITabBarHostedPlatterViewsHandle setHostView:];
-[_UITabBarHostedPlatterViewsHandle dealloc];
-[_UITabBarHostedPlatterViewsHandle invalidate];
-[_UITabBarHostedPlatterViewsHandle isValid];
-[_UITabBarHostedPlatterViewsHandle suppressesBackground];
-[_UITabBarHostedPlatterViewsHandle borrowedViewHandleForView:];
-[_UITabBarHostedPlatterViewsHandle borrowedViewHandles];
-[_UITabBarHostedPlatterViewsHandle initWithSuppressingBackground:updateHandler:];
-[_UITabBarHostedPlatterViewsHandle updateBorrowedViewHandles:];
```
