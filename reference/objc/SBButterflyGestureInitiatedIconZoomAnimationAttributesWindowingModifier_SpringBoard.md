# `SBButterflyGestureInitiatedIconZoomAnimationAttributesWindowingModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifier`
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
-[SBButterflyGestureInitiatedIconZoomAnimationAttributesWindowingModifier _layoutSettings];
-[SBButterflyGestureInitiatedIconZoomAnimationAttributesWindowingModifier transitionDidUpdate:];
-[SBButterflyGestureInitiatedIconZoomAnimationAttributesWindowingModifier _settingsByInterpolatingBetween:and:progress:];
-[SBButterflyGestureInitiatedIconZoomAnimationAttributesWindowingModifier genieAttributesForAppLayout:];
-[SBButterflyGestureInitiatedIconZoomAnimationAttributesWindowingModifier completesWhenChildrenComplete];
-[SBButterflyGestureInitiatedIconZoomAnimationAttributesWindowingModifier animationAttributesForItem:];
-[SBButterflyGestureInitiatedIconZoomAnimationAttributesWindowingModifier timerFired:];
-[SBButterflyGestureInitiatedIconZoomAnimationAttributesWindowingModifier frameForItem:];
-[SBButterflyGestureInitiatedIconZoomAnimationAttributesWindowingModifier _normalizedHomeScreenIconZoomPercentBetweenTopAndBottom];
-[SBButterflyGestureInitiatedIconZoomAnimationAttributesWindowingModifier _positionSettings];
-[SBButterflyGestureInitiatedIconZoomAnimationAttributesWindowingModifier _scaleSettings];
-[SBButterflyGestureInitiatedIconZoomAnimationAttributesWindowingModifier initWithAppLayout:gestureEdge:liftOffVelocity:];
```
