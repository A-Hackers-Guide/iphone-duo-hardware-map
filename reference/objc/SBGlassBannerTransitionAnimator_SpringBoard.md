# `SBGlassBannerTransitionAnimator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBBannerCustomTransitionAnimator`
- 7 instance variables, 1 properties, 16 instance methods, 2 class methods

## Instance variables

```
@"UIViewFloatAnimatableProperty" _swoopTrailProgress;
@"UIViewFloatAnimatableProperty" _dismissFxProgress;
@? _swoopTrailCallback;
@? _dismissFxCallback;
@"UIView" _morphHandleContainer;
@"NSArray" _morphFadedContentViews;
{CGPoint="x"d"y"d} _dismissGestureVelocity;
```

## Properties

```
@property (T{CGPoint=dd},N,V_dismissGestureVelocity) dismissGestureVelocity;
```

## Class methods

```
+[SBGlassBannerTransitionAnimator settings];
+[SBGlassBannerTransitionAnimator performAnimationsForTransition:completion:];
```

## Instance methods

```
-[SBGlassBannerTransitionAnimator dealloc];
-[SBGlassBannerTransitionAnimator _addGaussianBlurToViewIfNeeded:];
-[SBGlassBannerTransitionAnimator _statusBarIsVerticalForManager:];
-[SBGlassBannerTransitionAnimator _clockFollowsAppOrientationForContext:];
-[SBGlassBannerTransitionAnimator _clockStatusBarForManager:clockFrame:];
-[SBGlassBannerTransitionAnimator _cornerCenterForContext:withFrame:scale:grabberHandoffFrame:];
-[SBGlassBannerTransitionAnimator _removeGaussianBlurFromViewIfNeeded:];
-[SBGlassBannerTransitionAnimator _shouldAllowLeftCornerTransition];
-[SBGlassBannerTransitionAnimator _tearDownMorphHandle];
-[SBGlassBannerTransitionAnimator _tearDownSwoopTrackers];
-[SBGlassBannerTransitionAnimator _topSafeAreaInsetForContext:];
-[SBGlassBannerTransitionAnimator _viewHasGaussianBlurFilter:];
-[SBGlassBannerTransitionAnimator dismissGestureVelocity];
-[SBGlassBannerTransitionAnimator performActionsForTransition:];
-[SBGlassBannerTransitionAnimator prepareForTransition:];
-[SBGlassBannerTransitionAnimator setDismissGestureVelocity:];
```
