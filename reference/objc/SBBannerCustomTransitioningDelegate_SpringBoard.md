# `SBBannerCustomTransitioningDelegate`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BNDefaultBannerTransitioningDelegate`
- Protocols: `BNBannerInteractiveTransitioningDelegate`
- 3 instance variables, 7 properties, 14 instance methods, 0 class methods

## Instance variables

```
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _restFrameForActiveGesture;
q _style;
{CGPoint="x"d"y"d} _lastGestureVelocity;
```

## Properties

```
@property (Tq,N,V_style) style;
@property (T{CGPoint=dd},N,V_lastGestureVelocity) lastGestureVelocity;
@property (TB,?,N,GisResizeAnimationCustomizationPermitted) resizeAnimationCustomizationPermitted;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBBannerCustomTransitioningDelegate animationControllerForDismissedController:];
-[SBBannerCustomTransitioningDelegate animationControllerForPresentedController:presentingController:sourceController:];
-[SBBannerCustomTransitioningDelegate style];
-[SBBannerCustomTransitioningDelegate setStyle:];
-[SBBannerCustomTransitioningDelegate interactiveGestureDidEndWithDismiss:velocity:forViewController:];
-[SBBannerCustomTransitioningDelegate animationControllerForDismissedController:userInfo:];
-[SBBannerCustomTransitioningDelegate animationControllerForPresentedController:presentingController:sourceController:userInfo:];
-[SBBannerCustomTransitioningDelegate interactiveGestureDidBeginForViewController:];
-[SBBannerCustomTransitioningDelegate interactiveGestureDidUpdateWithFrame:forViewController:];
-[SBBannerCustomTransitioningDelegate shouldHandleInteractiveGestureForViewController:];
-[SBBannerCustomTransitioningDelegate animatorForDismissalTransitionWithStyle:];
-[SBBannerCustomTransitioningDelegate animatorForPresentationTransitionWithStyle:];
-[SBBannerCustomTransitioningDelegate lastGestureVelocity];
-[SBBannerCustomTransitioningDelegate setLastGestureVelocity:];
```
