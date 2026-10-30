# `SBBannerCustomTransitionAnimator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BNBannerTransitionAnimator`
- Protocols: `SBBannerCustomTransitionAnimating`
- 1 instance variables, 5 properties, 6 instance methods, 2 class methods

## Instance variables

```
@"SBBannerCustomTransitionAnimatorContext" _customContext;
```

## Properties

```
@property (T@"SBBannerCustomTransitionAnimatorContext",&,N,V_customContext) customContext;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBBannerCustomTransitionAnimator animateInteractive:animations:completion:];
+[SBBannerCustomTransitionAnimator animateWithSettings:animations:completion:];
```

## Instance methods

```
-[SBBannerCustomTransitionAnimator animateTransition:];
-[SBBannerCustomTransitionAnimator animationEnded:];
-[SBBannerCustomTransitionAnimator customContext];
-[SBBannerCustomTransitionAnimator setCustomContext:];
-[SBBannerCustomTransitionAnimator actionsForTransition:];
-[SBBannerCustomTransitionAnimator _updateCustomContextWithTransitionContext:];
```
