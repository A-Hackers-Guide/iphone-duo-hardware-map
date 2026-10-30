# `_UIFloatingBarContainerProxy`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 6 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"_UIFloatingBarContainerView" _floatingBarContainerView;
q _splitViewControllerColumn;
q _updateMode;
q _host;
@"UIViewController" _owningViewController;
```

## Properties

```
@property (T{UIEdgeInsets=dddd},N,R) overlayInsetsForVerticalBar;
@property (T@"UIViewController",R,W,N,V_owningViewController) owningViewController;
@property (T@"_UIFloatingBarContainerView",W,N,V_floatingBarContainerView) floatingBarContainerView;
@property (Tq,N,V_splitViewControllerColumn) splitViewControllerColumn;
@property (Tq,R,N,V_updateMode) updateMode;
@property (Tq,R,N,V_host) host;
```

## Instance methods

```
-[_UIFloatingBarContainerProxy overlayInsetsForVerticalBar];
-[_UIFloatingBarContainerProxy owningViewController];
-[_UIFloatingBarContainerProxy updateMode];
-[_UIFloatingBarContainerProxy splitViewControllerColumn];
-[_UIFloatingBarContainerProxy toolbarOverlayInsetsInSafeAreaInsets:];
-[_UIFloatingBarContainerProxy initWithFloatingBarContainerView:updateMode:host:owningViewController:];
-[_UIFloatingBarContainerProxy description];
-[_UIFloatingBarContainerProxy floatingBarContainerView];
-[_UIFloatingBarContainerProxy setFloatingBarContainerView:];
-[_UIFloatingBarContainerProxy host];
-[_UIFloatingBarContainerProxy setSplitViewControllerColumn:];
```
