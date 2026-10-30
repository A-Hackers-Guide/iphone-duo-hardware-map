# `SBSwipeToKillSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifier`
- 12 instance variables, 0 properties, 27 instance methods, 0 class methods

## Instance variables

```
q _layoutRole;
@"SBAppLayout" _appLayout;
@"SBAppLayout" _leafAppLayout;
B _fadeOutSwipedItems;
d _progress;
{CGPoint="x"d"y"d} _translation;
d _decelerationTargetProgress;
B _isDragging;
B _hasPrepared;
B _simulatingPostRemovalState;
Q _interpolationDirection;
@"SBHighlightSwitcherModifier" _highlightModifier;
```

## Instance methods

```
-[SBSwipeToKillSwitcherModifier scaleForIndex:];
-[SBSwipeToKillSwitcherModifier titleOpacityForIndex:];
-[SBSwipeToKillSwitcherModifier shouldUseAnchorPointToPinLayoutRolesToSpace:];
-[SBSwipeToKillSwitcherModifier clipsToUnobscuredMarginAtIndex:];
-[SBSwipeToKillSwitcherModifier animationAttributesForLayoutElement:];
-[SBSwipeToKillSwitcherModifier titleAndIconOpacityForIndex:];
-[SBSwipeToKillSwitcherModifier dimmingAlphaForLayoutRole:inAppLayout:];
-[SBSwipeToKillSwitcherModifier handleTransitionEvent:];
-[SBSwipeToKillSwitcherModifier visibleAppLayouts];
-[SBSwipeToKillSwitcherModifier opacityForLayoutRole:inAppLayout:atIndex:];
-[SBSwipeToKillSwitcherModifier isScrollEnabled];
-[SBSwipeToKillSwitcherModifier shadowOpacityForLayoutRole:atIndex:];
-[SBSwipeToKillSwitcherModifier frameForIndex:];
-[SBSwipeToKillSwitcherModifier wallpaperOverlayAlphaForIndex:];
-[SBSwipeToKillSwitcherModifier cornerRadiiForLayoutRole:inAppLayout:withCornerRadii:];
-[SBSwipeToKillSwitcherModifier handleRemovalEvent:];
-[SBSwipeToKillSwitcherModifier contentViewOffsetForAccessoriesOfAppLayout:];
-[SBSwipeToKillSwitcherModifier handleScrollEvent:];
-[SBSwipeToKillSwitcherModifier lighteningAlphaForIndex:];
-[SBSwipeToKillSwitcherModifier shadowOffsetForIndex:];
-[SBSwipeToKillSwitcherModifier contentViewOffsetForLayoutRole:inAppLayout:];
-[SBSwipeToKillSwitcherModifier _calculateInterpolationDirection];
-[SBSwipeToKillSwitcherModifier _dragHasBeenReleasedTowardKill];
-[SBSwipeToKillSwitcherModifier _interpolatingAdjacentIndexForIndex:];
-[SBSwipeToKillSwitcherModifier _performBlockWhileSimulatingPostRemovalAppLayoutState:];
-[SBSwipeToKillSwitcherModifier handleSwipeToKillEvent:];
-[SBSwipeToKillSwitcherModifier initWithLayoutRole:inAppLayout:fadeOutSwipedItems:];
```
