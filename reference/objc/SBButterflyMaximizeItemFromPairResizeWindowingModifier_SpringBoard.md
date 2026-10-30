# `SBButterflyMaximizeItemFromPairResizeWindowingModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifier`
- 11 instance variables, 0 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"NSUUID" _transitionID;
@"SBAppLayout" _fromAppLayout;
@"SBAppLayout" _toAppLayout;
@"SBDisplayItem" _evictedDisplayItem;
@"SBAppLayout" _appLayoutSlidingOff;
q _dismissalDirection;
@"SBDisplayItem" _leftItem;
@"SBDisplayItem" _rightItem;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _initialScreenFrameForMinimizingItem;
d _displacementForMinimizingItem;
B _prefersHomeAffordancesInItemContainers;
```

## Instance methods

```
-[SBButterflyMaximizeItemFromPairResizeWindowingModifier isSwitcherWindowUserInteractionEnabled];
-[SBButterflyMaximizeItemFromPairResizeWindowingModifier shouldUseAnchorPointToPinLayoutRolesToSpace:];
-[SBButterflyMaximizeItemFromPairResizeWindowingModifier visibleSplitViewHandleNubViews];
-[SBButterflyMaximizeItemFromPairResizeWindowingModifier isSwitcherWindowVisible];
-[SBButterflyMaximizeItemFromPairResizeWindowingModifier wallpaperStyle];
-[SBButterflyMaximizeItemFromPairResizeWindowingModifier transitionWillBegin:];
-[SBButterflyMaximizeItemFromPairResizeWindowingModifier visibleItems];
-[SBButterflyMaximizeItemFromPairResizeWindowingModifier shouldPerformCrossfadeForReduceMotion];
-[SBButterflyMaximizeItemFromPairResizeWindowingModifier cornersForItem:];
-[SBButterflyMaximizeItemFromPairResizeWindowingModifier frameForSplitViewHandleNubView:];
-[SBButterflyMaximizeItemFromPairResizeWindowingModifier animationAttributesForItem:];
-[SBButterflyMaximizeItemFromPairResizeWindowingModifier prefersHomeAffordanceInItemContainerForLayoutElement:];
-[SBButterflyMaximizeItemFromPairResizeWindowingModifier isLayoutRoleMatchMovedToScene:inAppLayout:];
-[SBButterflyMaximizeItemFromPairResizeWindowingModifier frameForItem:];
-[SBButterflyMaximizeItemFromPairResizeWindowingModifier initWithDismissalDirection:initialScreenFrameForMinimizingItem:leftItem:rightItem:displacementForMinimizingItem:prefersHomeAffordancesInItemContainers:];
-[SBButterflyMaximizeItemFromPairResizeWindowingModifier shouldInterruptForActivity:];
-[SBButterflyMaximizeItemFromPairResizeWindowingModifier transitionDidComplete:];
```
