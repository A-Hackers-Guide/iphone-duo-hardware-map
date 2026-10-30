# `SBFlexibleWindowingExposeToHomePeekWindowingModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifier`
- 4 instance variables, 0 properties, 13 instance methods, 0 class methods

## Instance variables

```
q _direction;
@"SBHomePeekWindowingModifier" _homePeekModifier;
@"SBWindowingModifier" _exposeModifier;
@"NSUUID" _transitionID;
```

## Instance methods

```
-[SBFlexibleWindowingExposeToHomePeekWindowingModifier shouldUseAnchorPointToPinLayoutRolesToSpace:];
-[SBFlexibleWindowingExposeToHomePeekWindowingModifier scaleForLayoutRole:inAppLayout:];
-[SBFlexibleWindowingExposeToHomePeekWindowingModifier frameForLayoutRole:inAppLayout:withBounds:];
-[SBFlexibleWindowingExposeToHomePeekWindowingModifier transitionWillBegin:];
-[SBFlexibleWindowingExposeToHomePeekWindowingModifier visibleItems];
-[SBFlexibleWindowingExposeToHomePeekWindowingModifier cornersForItem:];
-[SBFlexibleWindowingExposeToHomePeekWindowingModifier animationAttributesForItem:];
-[SBFlexibleWindowingExposeToHomePeekWindowingModifier opacityForItem:];
-[SBFlexibleWindowingExposeToHomePeekWindowingModifier frameForItem:];
-[SBFlexibleWindowingExposeToHomePeekWindowingModifier titleStyleForItem:];
-[SBFlexibleWindowingExposeToHomePeekWindowingModifier initWithTransitionID:direction:exposeModifier:];
-[SBFlexibleWindowingExposeToHomePeekWindowingModifier shouldInterruptForActivity:];
-[SBFlexibleWindowingExposeToHomePeekWindowingModifier transitionDidComplete:];
```
