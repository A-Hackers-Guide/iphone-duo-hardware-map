# `SBMainSwitcherRootSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBFluidSwitcherRootSwitcherModifier`
- 4 instance variables, 0 properties, 25 instance methods, 0 class methods

## Instance variables

```
{CGSize="width"d"height"d} _fullScreenCardSize;
{CGSize="width"d"height"d} _floatingCardSize;
q _environmentMode;
@"SBAppLayout" _appLayout;
```

## Instance methods

```
-[SBMainSwitcherRootSwitcherModifier highlightModifierForHighlightEvent:];
-[SBMainSwitcherRootSwitcherModifier adjustedAppLayoutsForAppLayouts:];
-[SBMainSwitcherRootSwitcherModifier userScrollingModifierForScrollEvent:];
-[SBMainSwitcherRootSwitcherModifier multitaskingModifierForEvent:];
-[SBMainSwitcherRootSwitcherModifier handleTransitionEvent:];
-[SBMainSwitcherRootSwitcherModifier handleMoveDisplayItemFromOtherDisplayEvent:];
-[SBMainSwitcherRootSwitcherModifier reduceMotionModifierForReduceMotionChangedEvent:];
-[SBMainSwitcherRootSwitcherModifier init];
-[SBMainSwitcherRootSwitcherModifier insertionModifierForInsertionEvent:];
-[SBMainSwitcherRootSwitcherModifier removalModifierForRemovalEvent:];
-[SBMainSwitcherRootSwitcherModifier floorModifierForTransitionEvent:];
-[SBMainSwitcherRootSwitcherModifier focusedAppModifierForUpdateFocusedAppLayoutEvent:];
-[SBMainSwitcherRootSwitcherModifier floorModifierForGestureEvent:];
-[SBMainSwitcherRootSwitcherModifier transitionModifierForMainTransitionEvent:];
-[SBMainSwitcherRootSwitcherModifier hiddenWindowsPillModifierForTransitionEvent:];
-[SBMainSwitcherRootSwitcherModifier assistantIslandModifierForEvent:];
-[SBMainSwitcherRootSwitcherModifier swipeToKillModifierForSwipeToKillEvent:];
-[SBMainSwitcherRootSwitcherModifier gestureModifierForGestureEvent:];
-[SBMainSwitcherRootSwitcherModifier shelfModifierForTransitionEvent:];
-[SBMainSwitcherRootSwitcherModifier _correctFloorModifierToHandleEvent];
-[SBMainSwitcherRootSwitcherModifier _createNewDefaultFloorModifier];
-[SBMainSwitcherRootSwitcherModifier _ensureModifier:startsInFinalStateOfEvent:];
-[SBMainSwitcherRootSwitcherModifier _newMultitaskingModifierForEnvironmentMode:];
-[SBMainSwitcherRootSwitcherModifier _setCardSizesWithEvent:];
-[SBMainSwitcherRootSwitcherModifier responseForProposedChildResponse:childModifier:event:];
```
