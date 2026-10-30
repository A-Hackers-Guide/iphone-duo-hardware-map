# `SBSystemActionBannerTransitionAnimator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBBannerCustomTransitionAnimator`
- 1 instance variables, 1 properties, 8 instance methods, 2 class methods

## Instance variables

```
@"UIViewFloatAnimatableProperty" _blurProgressProperty;
```

## Properties

```
@property (T@"UIViewFloatAnimatableProperty",&,N,V_blurProgressProperty) blurProgressProperty;
```

## Class methods

```
+[SBSystemActionBannerTransitionAnimator settings];
+[SBSystemActionBannerTransitionAnimator performAnimationsForTransition:completion:];
```

## Instance methods

```
-[SBSystemActionBannerTransitionAnimator settings];
-[SBSystemActionBannerTransitionAnimator _addGaussianBlurToViewIfNeeded:inputRadius:];
-[SBSystemActionBannerTransitionAnimator _removeBlurFilterFromView:];
-[SBSystemActionBannerTransitionAnimator _viewHasGaussianBlurFilter:];
-[SBSystemActionBannerTransitionAnimator blurProgressProperty];
-[SBSystemActionBannerTransitionAnimator performActionsForTransition:];
-[SBSystemActionBannerTransitionAnimator prepareForTransition:];
-[SBSystemActionBannerTransitionAnimator setBlurProgressProperty:];
```
