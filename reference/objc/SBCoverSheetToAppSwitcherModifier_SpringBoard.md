# `SBCoverSheetToAppSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransitionSwitcherModifier`
- 8 instance variables, 0 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"SBAppLayout" _appLayout;
d _progress;
d _velocity;
B _supportsBlur;
@"CADisplayLink" _displayLink;
d _appFlyInSettleDeadline;
d _appFlyInSettleStartTime;
d _appFlyInPeakScaleVelocityMagnitude;
```

## Instance methods

```
-[SBCoverSheetToAppSwitcherModifier scaleForIndex:];
-[SBCoverSheetToAppSwitcherModifier _displayLinkFired:];
-[SBCoverSheetToAppSwitcherModifier didMoveToParentModifier:];
-[SBCoverSheetToAppSwitcherModifier animationAttributesForLayoutElement:];
-[SBCoverSheetToAppSwitcherModifier transitionWillUpdate];
-[SBCoverSheetToAppSwitcherModifier opacityForLayoutRole:inAppLayout:atIndex:];
-[SBCoverSheetToAppSwitcherModifier transitionDidEnd];
-[SBCoverSheetToAppSwitcherModifier dealloc];
-[SBCoverSheetToAppSwitcherModifier transitionWillBegin];
-[SBCoverSheetToAppSwitcherModifier _blurParameters];
-[SBCoverSheetToAppSwitcherModifier _beginObservingAppFlyInSettle];
-[SBCoverSheetToAppSwitcherModifier _blurAnimationSettings];
-[SBCoverSheetToAppSwitcherModifier _isFlyOutAnimation];
-[SBCoverSheetToAppSwitcherModifier _opacityAnimationSettings];
-[SBCoverSheetToAppSwitcherModifier _scaleAnimationSettings];
-[SBCoverSheetToAppSwitcherModifier _stopObservingAppFlyInSettle];
-[SBCoverSheetToAppSwitcherModifier initWithTransitionID:appLayout:progress:velocity:supportsBlur:];
```
