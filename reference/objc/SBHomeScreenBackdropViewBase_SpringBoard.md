# `SBHomeScreenBackdropViewBase`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 4 instance variables, 2 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSMutableSet" _backdropViewRequiringReasons;
@"NSMutableSet" _liveBackdropViewRequiringReasons;
@"SBFluidSwitcherAnimationSettings" _animationSettings;
@"<SBHomeScreenBackdropViewBaseDelegate>" _delegate;
```

## Properties

```
@property (T@"<SBHomeScreenBackdropViewBaseDelegate>",W,N,V_delegate) delegate;
@property (Td,R,N) blurProgress;
```

## Instance methods

```
-[SBHomeScreenBackdropViewBase endRequiringBackdropViewForReason:];
-[SBHomeScreenBackdropViewBase beginRequiringLiveBackdropViewForReason:];
-[SBHomeScreenBackdropViewBase endRequiringLiveBackdropViewForReason:];
-[SBHomeScreenBackdropViewBase beginRequiringBackdropViewForReason:];
-[SBHomeScreenBackdropViewBase cancelInProcessAnimations];
-[SBHomeScreenBackdropViewBase backdropBlurSettings];
-[SBHomeScreenBackdropViewBase isOpaque];
-[SBHomeScreenBackdropViewBase setBlurProgress:behaviorMode:completion:];
-[SBHomeScreenBackdropViewBase setDelegate:];
-[SBHomeScreenBackdropViewBase blurProgress];
-[SBHomeScreenBackdropViewBase delegate];
-[SBHomeScreenBackdropViewBase initWithFrame:];
-[SBHomeScreenBackdropViewBase requiresBackdropView];
-[SBHomeScreenBackdropViewBase requiresLiveBackdropView];
```
