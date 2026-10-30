# `SBBannerPoofTransitionAnimator`

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
+[SBBannerPoofTransitionAnimator settings];
+[SBBannerPoofTransitionAnimator performAnimationsForTransition:completion:];
```

## Instance methods

```
-[SBBannerPoofTransitionAnimator settings];
-[SBBannerPoofTransitionAnimator _addGaussianBlurToViewIfNeeded:inputRadius:];
-[SBBannerPoofTransitionAnimator _removeBlurFilterFromView:];
-[SBBannerPoofTransitionAnimator _viewHasGaussianBlurFilter:];
-[SBBannerPoofTransitionAnimator blurProgressProperty];
-[SBBannerPoofTransitionAnimator performActionsForTransition:];
-[SBBannerPoofTransitionAnimator prepareForTransition:];
-[SBBannerPoofTransitionAnimator setBlurProgressProperty:];
```
