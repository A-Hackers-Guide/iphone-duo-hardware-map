# `SBStashSlideOverItemAnimationModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifier`
- 4 instance variables, 0 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"NSUUID" _transitionID;
Q _direction;
@"SBDisplayItem" _slideOverDisplayItem;
B _transitioningToHome;
```

## Instance methods

```
-[SBStashSlideOverItemAnimationModifier shouldUseAnchorPointToPinLayoutRolesToSpace:];
-[SBStashSlideOverItemAnimationModifier appLayoutsToEnsureExistForMainTransitionEvent:];
-[SBStashSlideOverItemAnimationModifier isHomeScreenContentRequired];
-[SBStashSlideOverItemAnimationModifier adjustedAppLayoutsForAppLayouts:];
-[SBStashSlideOverItemAnimationModifier isSwitcherWindowVisible];
-[SBStashSlideOverItemAnimationModifier transitionDidUpdate:];
-[SBStashSlideOverItemAnimationModifier opacityForLayoutRole:inAppLayout:atIndex:];
-[SBStashSlideOverItemAnimationModifier frameForLayoutRole:inAppLayout:withBounds:];
-[SBStashSlideOverItemAnimationModifier transitionWillBegin:];
-[SBStashSlideOverItemAnimationModifier visibleItems];
-[SBStashSlideOverItemAnimationModifier cornersForItem:];
-[SBStashSlideOverItemAnimationModifier animationAttributesForItem:];
-[SBStashSlideOverItemAnimationModifier topMostItems];
-[SBStashSlideOverItemAnimationModifier appLayoutToAttachSlideOverTongue];
-[SBStashSlideOverItemAnimationModifier frameForItem:];
-[SBStashSlideOverItemAnimationModifier initWithDirection:];
-[SBStashSlideOverItemAnimationModifier willBegin];
-[SBStashSlideOverItemAnimationModifier didComplete];
-[SBStashSlideOverItemAnimationModifier _layOutSlideOverItemFullyOffscreen];
-[SBStashSlideOverItemAnimationModifier _slideOverAppLayout];
-[SBStashSlideOverItemAnimationModifier shouldInterruptForActivity:];
-[SBStashSlideOverItemAnimationModifier transitionDidComplete:];
```
