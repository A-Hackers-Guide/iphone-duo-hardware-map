# `SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifier`
- 12 instance variables, 0 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"SBAppLayout" _fromAppLayout;
@"SBAppLayout" _toAppLayout;
@"NSString" _timerReason;
q _animationPhase;
@"NSUUID" _transitionID;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _toAppLayoutInitialBounds;
{CGPoint="x"d"y"d} _toAppLayoutInitialScale;
{CGPoint="x"d"y"d} _toAppLayoutInitialPosition;
d _toAppLayoutInitialCornerRadius;
@"SBAppLayout" _adjustedToAppLayout;
@"SBAppLayout" _adjustedFromAppLayout;
@"SBAppLayout" _slideOverAppLayout;
```

## Instance methods

```
-[SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier adjustedAppLayoutsForAppLayouts:];
-[SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier transitionDidUpdate:];
-[SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier perspectiveAngleForLayoutRole:inAppLayout:withPerspectiveAngle:];
-[SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier perspectiveAngleForIndex:];
-[SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier opacityForLayoutRole:inAppLayout:atIndex:];
-[SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier transitionWillBegin:];
-[SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier cornersForItem:];
-[SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier animationAttributesForItem:];
-[SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier timerFired:];
-[SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier maskedCornersForLayoutRole:inAppLayout:withMaskedCorners:];
-[SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier frameForItem:];
-[SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier titleStyleForItem:];
-[SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier willBegin];
-[SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier didComplete];
-[SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier initWithFromAppLayout:toAppLayout:];
-[SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier shouldInterruptForActivity:];
-[SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier transitionDidComplete:];
```
