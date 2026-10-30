# `_UIViewControllerOneToOneTransitionContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIViewControllerTransitionContext`
- 13 instance variables, 11 properties, 29 instance methods, 0 class methods

## Instance variables

```
B _isToViewSet;
B _isFromViewSet;
@"UIView" _toView;
@"UIView" _fromView;
B __isDeferred;
@"UIViewController" _fromViewController;
@"UIViewController" _toViewController;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _fromStartFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _fromEndFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _toEndFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _toStartFrame;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _toEndTransform;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _fromEndTransform;
```

## Properties

```
@property (T@"UIViewController",&,N,S_setFromViewController:,V_fromViewController) fromViewController;
@property (T@"UIViewController",&,N,S_setToViewController:,V_toViewController) toViewController;
@property (T@"UIView",&,N,G_fromView,S_setFromView:) fromView;
@property (T@"UIView",&,N,G_toView,S_setToView:) toView;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,S_setFromStartFrame:,V_fromStartFrame) fromStartFrame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,S_setFromEndFrame:,V_fromEndFrame) fromEndFrame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,S_setToEndFrame:,V_toEndFrame) toEndFrame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,S_setToStartFrame:,V_toStartFrame) toStartFrame;
@property (T{CGAffineTransform=dddddd},N,S_setToEndTransform:,V_toEndTransform) toEndTransform;
@property (T{CGAffineTransform=dddddd},N,S_setFromEndTransform:,V_fromEndTransform) fromEndTransform;
@property (TB,N,S_setIsDeferred:,V__isDeferred) _isDeferred;
```

## Instance methods

```
-[_UIViewControllerOneToOneTransitionContext _setToView:];
-[_UIViewControllerOneToOneTransitionContext _setFromView:];
-[_UIViewControllerOneToOneTransitionContext viewControllerForKey:];
-[_UIViewControllerOneToOneTransitionContext viewForKey:];
-[_UIViewControllerOneToOneTransitionContext fromStartFrame];
-[_UIViewControllerOneToOneTransitionContext init];
-[_UIViewControllerOneToOneTransitionContext finalFrameForViewController:];
-[_UIViewControllerOneToOneTransitionContext _toView];
-[_UIViewControllerOneToOneTransitionContext dealloc];
-[_UIViewControllerOneToOneTransitionContext _setToViewController:];
-[_UIViewControllerOneToOneTransitionContext initialFrameForViewController:];
-[_UIViewControllerOneToOneTransitionContext fromEndTransform];
-[_UIViewControllerOneToOneTransitionContext toViewController];
-[_UIViewControllerOneToOneTransitionContext toStartFrame];
-[_UIViewControllerOneToOneTransitionContext toEndTransform];
-[_UIViewControllerOneToOneTransitionContext _setToEndTransform:];
-[_UIViewControllerOneToOneTransitionContext fromViewController];
-[_UIViewControllerOneToOneTransitionContext _fromView];
-[_UIViewControllerOneToOneTransitionContext _setIsDeferred:];
-[_UIViewControllerOneToOneTransitionContext _setFromStartFrame:];
-[_UIViewControllerOneToOneTransitionContext toEndFrame];
-[_UIViewControllerOneToOneTransitionContext _setFromViewController:];
-[_UIViewControllerOneToOneTransitionContext _isDeferred];
-[_UIViewControllerOneToOneTransitionContext _setFromEndFrame:];
-[_UIViewControllerOneToOneTransitionContext _setFromEndTransform:];
-[_UIViewControllerOneToOneTransitionContext fromEndFrame];
-[_UIViewControllerOneToOneTransitionContext _setToEndFrame:];
-[_UIViewControllerOneToOneTransitionContext finalTransformForViewController:];
-[_UIViewControllerOneToOneTransitionContext _setToStartFrame:];
```
