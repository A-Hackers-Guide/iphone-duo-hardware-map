# `SBStripLayoutWindowingModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifier`
- 4 instance variables, 0 properties, 28 instance methods, 0 class methods

## Instance variables

```
d _stripOriginX;
B _isTrackingInteractiveStripGesture;
@"NSMutableSet" _highlightedByTouchAppLayouts;
@"NSMutableSet" _highlightedByHoverAppLayouts;
```

## Instance methods

```
-[SBStripLayoutWindowingModifier adjustedAppLayoutsForAppLayouts:];
-[SBStripLayoutWindowingModifier transitionDidUpdate:];
-[SBStripLayoutWindowingModifier layoutViewModelsIfNeeded];
-[SBStripLayoutWindowingModifier init];
-[SBStripLayoutWindowingModifier didUpdate];
-[SBStripLayoutWindowingModifier frameForLayoutRole:inAppLayout:withBounds:];
-[SBStripLayoutWindowingModifier transitionWillBegin:];
-[SBStripLayoutWindowingModifier visibleItems];
-[SBStripLayoutWindowingModifier topMostItems];
-[SBStripLayoutWindowingModifier frameForItem:];
-[SBStripLayoutWindowingModifier willBegin];
-[SBStripLayoutWindowingModifier _isStripStashed];
-[SBStripLayoutWindowingModifier _appLayout:isContainedInStrip:];
-[SBStripLayoutWindowingModifier _applyAnimationAttributes:forAppLayout:];
-[SBStripLayoutWindowingModifier _flexibleAutoLayoutSpaceForStripAppLayout:];
-[SBStripLayoutWindowingModifier _highlightScaleForAppLayout:pileIndex:];
-[SBStripLayoutWindowingModifier _isGroupForAppLayoutHighlightedFromHover:];
-[SBStripLayoutWindowingModifier _isGroupForAppLayoutHighlightedFromTouch:];
-[SBStripLayoutWindowingModifier _positionForPositionIn3DContainerSpace:layerPosition:layerSize:layerAnchorPoint:layerTransform:containerPerspective:];
-[SBStripLayoutWindowingModifier _stripIdentifierForAppLayout:];
-[SBStripLayoutWindowingModifier _stripItems];
-[SBStripLayoutWindowingModifier _stripOriginX];
-[SBStripLayoutWindowingModifier _visibleStripItems];
-[SBStripLayoutWindowingModifier _wallpaperDimmingForAppLayout:row:pileIndex:];
-[SBStripLayoutWindowingModifier _wallpaperGradientAttributesForAppLayout:viewModel:row:pileIndex:];
-[SBStripLayoutWindowingModifier gestureDidComplete:];
-[SBStripLayoutWindowingModifier gestureWillBegin:];
-[SBStripLayoutWindowingModifier highlightDidChange:];
```
