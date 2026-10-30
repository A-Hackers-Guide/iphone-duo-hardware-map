# `SBAppExposeToAppWindowingModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifier`
- 8 instance variables, 0 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"NSUUID" _transitionID;
@"SBTransitionSwitcherModifier" _transitionSwitcherModifier;
@"SBAppExposeWindowingModifier" _fromAppExposeModifier;
@"SBFullScreenContinuousExposeSwitcherModifier" _toFullScreenContinuousExposeModifier;
@"NSArray" _adjustedAppLayoutsBeforeTransition;
@"NSSet" _visibleItemsInAppExpose;
@"SBAppLayout" _toAppLayout;
B _hasForwardedUpdate;
```

## Instance methods

```
-[SBAppExposeToAppWindowingModifier adjustedSpaceAccessoryViewAnchorPoint:forAppLayout:];
-[SBAppExposeToAppWindowingModifier adjustedAppLayoutsForAppLayouts:];
-[SBAppExposeToAppWindowingModifier adjustedSpaceAccessoryViewFrame:forAppLayout:];
-[SBAppExposeToAppWindowingModifier adjustedSpaceAccessoryViewScale:forAppLayout:];
-[SBAppExposeToAppWindowingModifier opacityForLayoutRole:inAppLayout:atIndex:];
-[SBAppExposeToAppWindowingModifier scaleForLayoutRole:inAppLayout:];
-[SBAppExposeToAppWindowingModifier frameForLayoutRole:inAppLayout:withBounds:];
-[SBAppExposeToAppWindowingModifier adjustedSpaceAccessoryViewPerspectiveAngle:forAppLayout:];
-[SBAppExposeToAppWindowingModifier transitionWillBegin:];
-[SBAppExposeToAppWindowingModifier visibleItems];
-[SBAppExposeToAppWindowingModifier cornersForItem:];
-[SBAppExposeToAppWindowingModifier animationAttributesForLayoutRole:inAppLayout:withAnimationAttributes:];
-[SBAppExposeToAppWindowingModifier perspectiveAngleForItem:];
-[SBAppExposeToAppWindowingModifier frameForItem:];
-[SBAppExposeToAppWindowingModifier titleStyleForItem:];
-[SBAppExposeToAppWindowingModifier willBegin];
-[SBAppExposeToAppWindowingModifier stripDidChange:];
-[SBAppExposeToAppWindowingModifier initWithSwitcherTransitionModifier:fromAppExposeModifier:toFullScreenContinuousExposeModifier:];
-[SBAppExposeToAppWindowingModifier shouldInterruptForActivity:];
-[SBAppExposeToAppWindowingModifier transitionDidComplete:];
```
