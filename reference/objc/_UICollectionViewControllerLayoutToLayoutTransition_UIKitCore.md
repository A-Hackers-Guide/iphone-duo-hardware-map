# `_UICollectionViewControllerLayoutToLayoutTransition`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIViewControllerAnimatedTransitioning`
- 5 instance variables, 9 properties, 15 instance methods, 1 class methods

## Instance variables

```
B _crossFadeNavigationBar;
B _crossFadeBottomBars;
@"UICollectionViewLayout" _toLayout;
@"UIPercentDrivenInteractiveTransition" _interactionController;
q _operation;
```

## Properties

```
@property (T@"UICollectionViewLayout",&,N,V_toLayout) toLayout;
@property (TB,N,V_crossFadeNavigationBar) crossFadeNavigationBar;
@property (TB,N,V_crossFadeBottomBars) crossFadeBottomBars;
@property (T@"UIPercentDrivenInteractiveTransition",N,V_interactionController) interactionController;
@property (Tq,N,V_operation) operation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UICollectionViewControllerLayoutToLayoutTransition transitionForOperation:fromViewController:toViewController:];
```

## Instance methods

```
-[_UICollectionViewControllerLayoutToLayoutTransition toLayout];
-[_UICollectionViewControllerLayoutToLayoutTransition setOperation:];
-[_UICollectionViewControllerLayoutToLayoutTransition operation];
-[_UICollectionViewControllerLayoutToLayoutTransition animateTransition:];
-[_UICollectionViewControllerLayoutToLayoutTransition transitionDuration:];
-[_UICollectionViewControllerLayoutToLayoutTransition _shouldCrossFadeBottomBars];
-[_UICollectionViewControllerLayoutToLayoutTransition animationEnded:];
-[_UICollectionViewControllerLayoutToLayoutTransition setInteractionController:];
-[_UICollectionViewControllerLayoutToLayoutTransition interactionController];
-[_UICollectionViewControllerLayoutToLayoutTransition _shouldCrossFadeNavigationBar];
-[_UICollectionViewControllerLayoutToLayoutTransition setToLayout:];
-[_UICollectionViewControllerLayoutToLayoutTransition crossFadeBottomBars];
-[_UICollectionViewControllerLayoutToLayoutTransition crossFadeNavigationBar];
-[_UICollectionViewControllerLayoutToLayoutTransition setCrossFadeBottomBars:];
-[_UICollectionViewControllerLayoutToLayoutTransition setCrossFadeNavigationBar:];
```
