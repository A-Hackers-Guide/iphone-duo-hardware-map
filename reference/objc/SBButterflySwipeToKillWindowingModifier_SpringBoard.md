# `SBButterflySwipeToKillWindowingModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifier`
- 10 instance variables, 0 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"SBAppLayout" _appLayout;
d _progress;
{CGPoint="x"d"y"d} _translation;
d _decelerationTargetProgress;
B _isDragging;
B _hasPrepared;
B _simulatingPostRemovalState;
Q _interpolationDirection;
@"SBButterflyHighlightWindowingModifier" _highlightModifier;
@"SBButterflyOverrideAppLayoutsWindowingModifier" _overrideAppLayoutsModifier;
```

## Instance methods

```
-[SBButterflySwipeToKillWindowingModifier clipsToUnobscuredMarginAtIndex:];
-[SBButterflySwipeToKillWindowingModifier initWithAppLayout:];
-[SBButterflySwipeToKillWindowingModifier isScrollEnabled];
-[SBButterflySwipeToKillWindowingModifier wallpaperOverlayAlphaForIndex:];
-[SBButterflySwipeToKillWindowingModifier transitionWillBegin:];
-[SBButterflySwipeToKillWindowingModifier shadowForItem:];
-[SBButterflySwipeToKillWindowingModifier visibleItems];
-[SBButterflySwipeToKillWindowingModifier animationAttributesForItem:];
-[SBButterflySwipeToKillWindowingModifier opacityForItem:];
-[SBButterflySwipeToKillWindowingModifier dimmingAlphaForItem:];
-[SBButterflySwipeToKillWindowingModifier lighteningAlphaForIndex:];
-[SBButterflySwipeToKillWindowingModifier shadowOffsetForIndex:];
-[SBButterflySwipeToKillWindowingModifier visibleAppSpaces];
-[SBButterflySwipeToKillWindowingModifier frameForItem:];
-[SBButterflySwipeToKillWindowingModifier titleStyleForItem:];
-[SBButterflySwipeToKillWindowingModifier didScroll:];
-[SBButterflySwipeToKillWindowingModifier _calculateInterpolationDirection];
-[SBButterflySwipeToKillWindowingModifier _dragHasBeenReleasedTowardKill];
-[SBButterflySwipeToKillWindowingModifier _interpolatingIndexForIndex:];
-[SBButterflySwipeToKillWindowingModifier _interpolatingItemForItem:];
-[SBButterflySwipeToKillWindowingModifier _interpolatingSpaceForSpace:];
-[SBButterflySwipeToKillWindowingModifier _interpolatingSpaceIndexForSpaceIndex:];
-[SBButterflySwipeToKillWindowingModifier _performBlockWhileSimulatingPostRemovalAppLayoutState:];
-[SBButterflySwipeToKillWindowingModifier itemRemoved:];
-[SBButterflySwipeToKillWindowingModifier itemSwipedToKill:];
```
