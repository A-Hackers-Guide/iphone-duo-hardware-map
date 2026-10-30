# `_UILiquidLensView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 22 instance variables, 28 properties, 61 instance methods, 0 class methods

## Instance variables

```
B _lifted;
B warpsContentBelow;
? liftedContainerView;
? liftedContentView;
q liftedContentMode;
? overridePunchoutView;
@"UIColor" restingBackgroundColor;
@"UIColor" restingBorderColor;
@"_UIShadowProperties" restingShadowProperties;
@"_UIFlexInteraction" flexInteraction;
$__lazy_storage_$_liftPortal;
@"_TtCE5UIKitCSo17_UILiquidLensViewP33_4C400BD973F5E4E0B779D1A21A7AEB2712BackdropView" belowGlassWarpBackdrop;
@"_TtCE5UIKitCSo17_UILiquidLensViewP33_4C400BD973F5E4E0B779D1A21A7AEB2711DestOutView" liftedContentPunchout;
B hasCustomRestingBackground;
@"UIView" restingBackground;
@"UIView" contentWrapper;
@"_TtCE5UIKitCSo17_UILiquidLensViewP33_4C400BD973F5E4E0B779D1A21A7AEB2714ClearGlassView" glass;
$__lazy_storage_$_liftProgress;
@"NSTimer" unliftDelayTimer;
liftTimestamp;
B forceUnliftTimerWithoutAnimations;
@"_UIGroupCompletion" groupCompletion;
```

## Properties

```
@property (TB,N,R) lifted;
@property (TB,N,V_lifted) _lifted;
@property (Tq,N) style;
@property (TB,N,VwarpsContentBelow) warpsContentBelow;
@property (T@"UIView",N,W,VliftedContainerView) liftedContainerView;
@property (T@"UIView",N,W,VliftedContentView) liftedContentView;
@property (Tq,N,VliftedContentMode) liftedContentMode;
@property (T@"UIView",N,W,VoverridePunchoutView) overridePunchoutView;
@property (T@"UIColor",N,&,VrestingBackgroundColor) restingBackgroundColor;
@property (T@"UIColor",N,&,VrestingBorderColor) restingBorderColor;
@property (T@"_UIShadowProperties",N,&,VrestingShadowProperties) restingShadowProperties;
@property (T@"UIView",N,R) restingBackgroundView;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N) frame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N) bounds;
@property (Td,N) alpha;
@property (T@"_UIFlexInteraction",N,R,VflexInteraction) flexInteraction;
@property (T@"_UIPortalView",N,&) liftPortal;
@property (T@"_TtCE5UIKitCSo17_UILiquidLensViewP33_4C400BD973F5E4E0B779D1A21A7AEB2712BackdropView",N,&,VbelowGlassWarpBackdrop) belowGlassWarpBackdrop;
@property (T@"_TtCE5UIKitCSo17_UILiquidLensViewP33_4C400BD973F5E4E0B779D1A21A7AEB2711DestOutView",N,&,VliftedContentPunchout) liftedContentPunchout;
@property (TB,N,R,VhasCustomRestingBackground) hasCustomRestingBackground;
@property (T@"UIView",N,R,VrestingBackground) restingBackground;
@property (T@"UIView",N,R,VcontentWrapper) contentWrapper;
@property (T@"_TtCE5UIKitCSo17_UILiquidLensViewP33_4C400BD973F5E4E0B779D1A21A7AEB2714ClearGlassView",N,R,Vglass) glass;
@property (T@"_TtC5UIKit28_UIDebouncingAnimatableFloat",N,&) liftProgress;
@property (T@"NSTimer",N,&,VunliftDelayTimer) unliftDelayTimer;
@property (TB,N,VforceUnliftTimerWithoutAnimations) forceUnliftTimerWithoutAnimations;
@property (T@"_UIGroupCompletion",N,R,VgroupCompletion) groupCompletion;
@property (T@"_TtC5UIKit28_UILiquidLensViewVariantSpec",N,R) spec;
```

## Instance methods

```
-[_UILiquidLensView restingBackgroundView];
-[_UILiquidLensView setWarpsContentBelow:];
-[_UILiquidLensView didMoveToWindow];
-[_UILiquidLensView setLiftedContentPunchout:];
-[_UILiquidLensView setBelowGlassWarpBackdrop:];
-[_UILiquidLensView restingBackground];
-[_UILiquidLensView setOverridePunchoutView:];
-[_UILiquidLensView set_lifted:];
-[_UILiquidLensView setLiftedContentView:];
-[_UILiquidLensView setLiftPortal:];
-[_UILiquidLensView updatePunchoutView];
-[_UILiquidLensView updateGlassPlacementIfNeededWithAnimated:];
-[_UILiquidLensView spec];
-[_UILiquidLensView belowGlassWarpBackdrop];
-[_UILiquidLensView updateRestingBackgroundView];
-[_UILiquidLensView actuallySetLifted:animated:alongsideAnimations:completion:];
-[_UILiquidLensView groupCompletion];
-[_UILiquidLensView _lifted];
-[_UILiquidLensView setLiftedContainerView:];
-[_UILiquidLensView layoutSubviews];
-[_UILiquidLensView overridePunchoutView];
-[_UILiquidLensView liftPortal];
-[_UILiquidLensView liftedContentMode];
-[_UILiquidLensView glass];
-[_UILiquidLensView style];
-[_UILiquidLensView setBounds:];
-[_UILiquidLensView updateProgressBasedAnimationsForPresentation:];
-[_UILiquidLensView setLiftedContentMode:];
-[_UILiquidLensView setStyle:];
-[_UILiquidLensView contentWrapper];
-[_UILiquidLensView hasCustomRestingBackground];
-[_UILiquidLensView setRestingBackgroundColor:];
-[_UILiquidLensView liftedContentView];
-[_UILiquidLensView flexInteraction];
-[_UILiquidLensView setLifted:animated:alongsideAnimations:completion:];
-[_UILiquidLensView liftProgress];
-[_UILiquidLensView lifted];
-[_UILiquidLensView setAlpha:];
-[_UILiquidLensView _removeAllAnimations:];
-[_UILiquidLensView setRestingBorderColor:];
-[_UILiquidLensView setUnliftDelayTimer:];
-[_UILiquidLensView restingShadowProperties];
-[_UILiquidLensView setLiftProgress:];
-[_UILiquidLensView setFrame:];
-[_UILiquidLensView bounds];
-[_UILiquidLensView forceUnliftWithoutAnimations];
-[_UILiquidLensView initWithRestingBackground:];
-[_UILiquidLensView _visibilityDidChange];
-[_UILiquidLensView initWithCoder:];
-[_UILiquidLensView liftedContainerView];
-[_UILiquidLensView restingBorderColor];
-[_UILiquidLensView alpha];
-[_UILiquidLensView setForceUnliftTimerWithoutAnimations:];
-[_UILiquidLensView liftedContentPunchout];
-[_UILiquidLensView restingBackgroundColor];
-[_UILiquidLensView initWithFrame:];
-[_UILiquidLensView forceUnliftTimerWithoutAnimations];
-[_UILiquidLensView setRestingShadowProperties:];
-[_UILiquidLensView warpsContentBelow];
-[_UILiquidLensView unliftDelayTimer];
-[_UILiquidLensView frame];
```
