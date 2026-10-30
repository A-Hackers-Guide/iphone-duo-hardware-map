# `SBGestureInitiatedIconZoomAnimationAttributesSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifier`
- 5 instance variables, 0 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"SBAppLayout" _appLayout;
Q _gestureEdge;
{CGPoint="x"d"y"d} _liftOffVelocity;
@"NSString" _iconGridSizeClass;
B _overshootScaleForWidgetZoomDown;
```

## Instance methods

```
-[SBGestureInitiatedIconZoomAnimationAttributesSwitcherModifier scaleForIndex:];
-[SBGestureInitiatedIconZoomAnimationAttributesSwitcherModifier animationAttributesForLayoutElement:];
-[SBGestureInitiatedIconZoomAnimationAttributesSwitcherModifier _layoutSettings];
-[SBGestureInitiatedIconZoomAnimationAttributesSwitcherModifier handleTransitionEvent:];
-[SBGestureInitiatedIconZoomAnimationAttributesSwitcherModifier handleTimerEvent:];
-[SBGestureInitiatedIconZoomAnimationAttributesSwitcherModifier _settingsByInterpolatingBetween:and:progress:];
-[SBGestureInitiatedIconZoomAnimationAttributesSwitcherModifier genieAttributesForAppLayout:];
-[SBGestureInitiatedIconZoomAnimationAttributesSwitcherModifier completesWhenChildrenComplete];
-[SBGestureInitiatedIconZoomAnimationAttributesSwitcherModifier _normalizedHomeScreenIconZoomPercentBetweenTopAndBottom];
-[SBGestureInitiatedIconZoomAnimationAttributesSwitcherModifier _positionSettings];
-[SBGestureInitiatedIconZoomAnimationAttributesSwitcherModifier _scaleSettings];
-[SBGestureInitiatedIconZoomAnimationAttributesSwitcherModifier initWithAppLayout:gestureEdge:liftOffVelocity:];
```
