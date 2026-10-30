# `SBContinuousExposeFullScreenCrossblurTransitionSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransitionSwitcherModifier`
- 7 instance variables, 0 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"SBAppLayout" _toAppLayout;
@"SBAppLayout" _fromAppLayout;
q _animationPhase;
@"NSString" _timerReason;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _toAppLayoutInitialFrame;
d _toAppLayoutInitialScale;
{UIRectCornerRadii="topLeft"d"bottomLeft"d"bottomRight"d"topRight"d} _toAppLayoutInitialCornerRadius;
```

## Instance methods

```
-[SBContinuousExposeFullScreenCrossblurTransitionSwitcherModifier scaleForIndex:];
-[SBContinuousExposeFullScreenCrossblurTransitionSwitcherModifier anchorPointForIndex:];
-[SBContinuousExposeFullScreenCrossblurTransitionSwitcherModifier didMoveToParentModifier:];
-[SBContinuousExposeFullScreenCrossblurTransitionSwitcherModifier cornerRadiiForIndex:];
-[SBContinuousExposeFullScreenCrossblurTransitionSwitcherModifier animationAttributesForLayoutElement:];
-[SBContinuousExposeFullScreenCrossblurTransitionSwitcherModifier titleAndIconOpacityForIndex:];
-[SBContinuousExposeFullScreenCrossblurTransitionSwitcherModifier transitionWillUpdate];
-[SBContinuousExposeFullScreenCrossblurTransitionSwitcherModifier perspectiveAngleForIndex:];
-[SBContinuousExposeFullScreenCrossblurTransitionSwitcherModifier opacityForLayoutRole:inAppLayout:atIndex:];
-[SBContinuousExposeFullScreenCrossblurTransitionSwitcherModifier handleTimerEvent:];
-[SBContinuousExposeFullScreenCrossblurTransitionSwitcherModifier frameForIndex:];
-[SBContinuousExposeFullScreenCrossblurTransitionSwitcherModifier shouldAllowGroupOpacityForAppLayout:];
-[SBContinuousExposeFullScreenCrossblurTransitionSwitcherModifier _updateLayoutWithAnimationUpdateMode:appendResponse:];
-[SBContinuousExposeFullScreenCrossblurTransitionSwitcherModifier initWithTransitionID:toAppLayout:fromAppLayout:];
```
