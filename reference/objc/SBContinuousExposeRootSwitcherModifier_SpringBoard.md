# `SBContinuousExposeRootSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBFullScreenFluidSwitcherRootSwitcherModifier`
- 8 instance variables, 0 properties, 33 instance methods, 0 class methods

## Instance variables

```
@"SBAppLayout" _currentAppLayout;
q _currentEnvironmentMode;
@"SBAppLayout" _effectiveAppLayoutOnStage;
@"SBAppLayout" _peekingAppLayout;
B _isStripTonguePresented;
@"SBSwitcherModifier" _initialFloorModifierForWindowDrag;
@"SBTransitionSwitcherModifierEvent" _unmodifiedCurrentTransitionEvent;
B _isTransitionToNilAppLayoutInProgress;
```

## Instance methods

```
-[SBContinuousExposeRootSwitcherModifier handleGestureEvent:];
-[SBContinuousExposeRootSwitcherModifier shouldScaleContentToFillBoundsAtIndex:];
-[SBContinuousExposeRootSwitcherModifier shouldUseWallpaperGradientTreatment];
-[SBContinuousExposeRootSwitcherModifier handleEvent:];
-[SBContinuousExposeRootSwitcherModifier _effectiveEnvironmentMode];
-[SBContinuousExposeRootSwitcherModifier highlightModifierForHighlightEvent:];
-[SBContinuousExposeRootSwitcherModifier peekingAppLayout];
-[SBContinuousExposeRootSwitcherModifier displayItemsToExcludeFromStrip];
-[SBContinuousExposeRootSwitcherModifier appLayoutOnStage];
-[SBContinuousExposeRootSwitcherModifier userScrollingModifierForScrollEvent:];
-[SBContinuousExposeRootSwitcherModifier multitaskingModifierForEvent:];
-[SBContinuousExposeRootSwitcherModifier switcherModifierLevelForTransitionEvent:];
-[SBContinuousExposeRootSwitcherModifier handleContinuousExposeStripEdgeProtectTongueEvent:];
-[SBContinuousExposeRootSwitcherModifier handleTransitionEvent:];
-[SBContinuousExposeRootSwitcherModifier handleMoveDisplayItemFromOtherDisplayEvent:];
-[SBContinuousExposeRootSwitcherModifier reduceMotionModifierForReduceMotionChangedEvent:];
-[SBContinuousExposeRootSwitcherModifier _isActivatingAppLayoutUnoccludedForEvent:];
-[SBContinuousExposeRootSwitcherModifier insertionModifierForInsertionEvent:];
-[SBContinuousExposeRootSwitcherModifier handleTimerEvent:];
-[SBContinuousExposeRootSwitcherModifier removalModifierForRemovalEvent:];
-[SBContinuousExposeRootSwitcherModifier floorModifierForTransitionEvent:];
-[SBContinuousExposeRootSwitcherModifier handleDidEdgeProtectResizeGrabberEvent:];
-[SBContinuousExposeRootSwitcherModifier shouldUseNonuniformSnapshotScalingForLayoutRole:inAppLayout:];
-[SBContinuousExposeRootSwitcherModifier handleSlideOverEdgeProtectTongueEvent:];
-[SBContinuousExposeRootSwitcherModifier handleContinuousExposeIdentifiersChangedEvent:];
-[SBContinuousExposeRootSwitcherModifier focusedAppModifierForUpdateFocusedAppLayoutEvent:];
-[SBContinuousExposeRootSwitcherModifier floorModifierForGestureEvent:];
-[SBContinuousExposeRootSwitcherModifier transitionModifierForMainTransitionEvent:];
-[SBContinuousExposeRootSwitcherModifier assistantIslandModifierForEvent:];
-[SBContinuousExposeRootSwitcherModifier lowEndHardwareModifier];
-[SBContinuousExposeRootSwitcherModifier swipeToKillModifierForSwipeToKillEvent:];
-[SBContinuousExposeRootSwitcherModifier continuousExposeStripTongueAttributes];
-[SBContinuousExposeRootSwitcherModifier gestureModifierForGestureEvent:];
```
