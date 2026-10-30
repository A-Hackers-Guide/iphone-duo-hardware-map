# `_UISimpleTransitioningDelegate`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIViewControllerTransitioningDelegate`, `UINavigationControllerDelegate`
- 2 instance variables, 5 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"<UIViewControllerAnimatedTransitioning>" _animator;
B __suppressCrossFadeNavigationBarAnimation;
```

## Properties

```
@property (TB,N,S_setSuppressCrossFadeNavigationBarAnimation:,V__suppressCrossFadeNavigationBarAnimation) _suppressCrossFadeNavigationBarAnimation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UISimpleTransitioningDelegate navigationController:animationControllerForOperation:fromViewController:toViewController:];
-[_UISimpleTransitioningDelegate _navigationControllerShouldCrossFadeNavigationBar:];
-[_UISimpleTransitioningDelegate _setSuppressCrossFadeNavigationBarAnimation:];
-[_UISimpleTransitioningDelegate _suppressCrossFadeNavigationBarAnimation];
-[_UISimpleTransitioningDelegate initWithAnimator:];
```
