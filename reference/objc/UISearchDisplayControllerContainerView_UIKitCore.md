# `UISearchDisplayControllerContainerView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 6 instance variables, 5 properties, 17 instance methods, 0 class methods

## Instance variables

```
B _collapsedTopView;
@"NSLayoutConstraint" _topViewHeightConstraint;
@"NSLayoutConstraint" _topViewAttributeTopConstraint;
@"UIView" _topView;
@"UIView" _bottomView;
@"UIView" _behindView;
```

## Properties

```
@property (T@"NSLayoutConstraint",&,N,V_topViewHeightConstraint) topViewHeightConstraint;
@property (T@"NSLayoutConstraint",&,N,V_topViewAttributeTopConstraint) topViewAttributeTopConstraint;
@property (T@"UIView",R,N,V_topView) topView;
@property (T@"UIView",R,N,V_bottomView) bottomView;
@property (T@"UIView",R,N,V_behindView) behindView;
```

## Instance methods

```
-[UISearchDisplayControllerContainerView hitTest:withEvent:];
-[UISearchDisplayControllerContainerView _didMoveFromWindow:toWindow:];
-[UISearchDisplayControllerContainerView collapseTopView];
-[UISearchDisplayControllerContainerView topView];
-[UISearchDisplayControllerContainerView adjustTopAttributeConstantByDelta:];
-[UISearchDisplayControllerContainerView behindView];
-[UISearchDisplayControllerContainerView bottomView];
-[UISearchDisplayControllerContainerView configureInteractionForContainment:];
-[UISearchDisplayControllerContainerView initWithFrame:topViewHeight:];
-[UISearchDisplayControllerContainerView setBottomViewUserInteractionEnabled:];
-[UISearchDisplayControllerContainerView setTopViewAttributeTopConstraint:];
-[UISearchDisplayControllerContainerView setTopViewHeightConstraint:];
-[UISearchDisplayControllerContainerView topViewAttributeTopConstraint];
-[UISearchDisplayControllerContainerView topViewHeightConstraint];
-[UISearchDisplayControllerContainerView updateTopAttributeConstant:];
-[UISearchDisplayControllerContainerView updateTopViewHeight:];
-[UISearchDisplayControllerContainerView updateTopViewHeight:animateUpdate:];
```
