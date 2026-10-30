# `_UIViewControllerAnimatedTransitionViewControllerHandoffData`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"UIViewController" _viewController;
@"UIView" _containerView;
@"UIView" _snapshot;
d _dimmingAmount;
d _targetDimmingAmount;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _frame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _targetFrame;
```

## Properties

```
@property (T@"UIViewController",R,W,N,V_viewController) viewController;
@property (T@"UIView",&,N,V_containerView) containerView;
@property (T@"UIView",R,N,V_snapshot) snapshot;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_frame) frame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_targetFrame) targetFrame;
@property (Td,R,N,V_dimmingAmount) dimmingAmount;
@property (Td,R,N,V_targetDimmingAmount) targetDimmingAmount;
```

## Instance methods

```
-[_UIViewControllerAnimatedTransitionViewControllerHandoffData setContainerView:];
-[_UIViewControllerAnimatedTransitionViewControllerHandoffData snapshot];
-[_UIViewControllerAnimatedTransitionViewControllerHandoffData viewController];
-[_UIViewControllerAnimatedTransitionViewControllerHandoffData containerView];
-[_UIViewControllerAnimatedTransitionViewControllerHandoffData frame];
-[_UIViewControllerAnimatedTransitionViewControllerHandoffData dimmingAmount];
-[_UIViewControllerAnimatedTransitionViewControllerHandoffData initWithViewController:containerView:snapshot:frame:targetFrame:dimmingAmount:targetDimmingAmount:];
-[_UIViewControllerAnimatedTransitionViewControllerHandoffData targetDimmingAmount];
-[_UIViewControllerAnimatedTransitionViewControllerHandoffData targetFrame];
```
