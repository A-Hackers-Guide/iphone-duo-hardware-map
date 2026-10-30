# `SBGridSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifier`
- 6 instance variables, 0 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"SBGridLayoutSwitcherModifier" _gridLayoutModifier;
@"_SBGridFloorSwitcherModifier" _floorModifier;
Q _ongoingAppLayoutRemovals;
@"SBAppLayout" _currentAppLayout;
@"SBAppLayout" _activeAppLayoutInSwitcher;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _containerViewBounds_lastBounds;
```

## Instance methods

```
-[SBGridSwitcherModifier jetsamModeForAppLayout:];
-[SBGridSwitcherModifier foregroundAppLayouts];
-[SBGridSwitcherModifier didMoveToParentModifier:];
-[SBGridSwitcherModifier topMostLayoutElements];
-[SBGridSwitcherModifier activityModeForAppLayout:];
-[SBGridSwitcherModifier containerViewBounds];
-[SBGridSwitcherModifier handleTransitionEvent:];
-[SBGridSwitcherModifier handleTapOutsideToDismissEvent:];
-[SBGridSwitcherModifier handleRemovalEvent:];
-[SBGridSwitcherModifier handleTapAppLayoutEvent:];
-[SBGridSwitcherModifier handleScrollEvent:];
-[SBGridSwitcherModifier gridLayoutModifier];
-[SBGridSwitcherModifier handleSwipeToKillEvent:];
```
