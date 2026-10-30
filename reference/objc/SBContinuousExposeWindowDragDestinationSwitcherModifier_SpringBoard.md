# `SBContinuousExposeWindowDragDestinationSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifier`
- 17 instance variables, 6 properties, 23 instance methods, 0 class methods

## Instance variables

```
{CGPoint="x"d"y"d} _location;
{CGPoint="x"d"y"d} _velocity;
{CGPoint="x"d"y"d} _initialLocation;
{CGPoint="x"d"y"d} _translation;
@"SBDisplayItemLayoutAttributes" _initialSelectedDisplayItemLayoutAttributesOnThisSwitcher;
B _dragBeganInOtherSwitcher;
@"SBFlexibleWindowingAutoLayoutSpace" _initialFlexibleAutoLayoutSpace;
@"SBAppLayout" _lastAppLayoutForStripCalculation;
d _stripWidthForCancelZone;
@"SBDisplayItemLayoutGrid" _layoutGrid;
B _selectedItemIsInSlideOver;
@"SBDisplayItem" _selectedDisplayItem;
@"SBAppLayout" _initialAppLayout;
@"<SBContinuousExposeWindowDragDestinationSwitcherModifierDelegate>" _destinationDelegate;
Q _proposedDestination;
@"SBAppLayout" _proposedAppLayout;
@"SBAppLayout" _hoveringOverAppLayout;
```

## Properties

```
@property (T@"SBDisplayItem",R,N,V_selectedDisplayItem) selectedDisplayItem;
@property (T@"SBAppLayout",R,N,V_initialAppLayout) initialAppLayout;
@property (T@"<SBContinuousExposeWindowDragDestinationSwitcherModifierDelegate>",R,W,N,V_destinationDelegate) destinationDelegate;
@property (TQ,R,N,V_proposedDestination) proposedDestination;
@property (T@"SBAppLayout",R,N,V_proposedAppLayout) proposedAppLayout;
@property (T@"SBAppLayout",R,N,V_hoveringOverAppLayout) hoveringOverAppLayout;
```

## Instance methods

```
-[SBContinuousExposeWindowDragDestinationSwitcherModifier handleGestureEvent:];
-[SBContinuousExposeWindowDragDestinationSwitcherModifier didMoveToParentModifier:];
-[SBContinuousExposeWindowDragDestinationSwitcherModifier _appLayoutContainingDisplayItem:];
-[SBContinuousExposeWindowDragDestinationSwitcherModifier proposedAppLayoutForWindowDrag];
-[SBContinuousExposeWindowDragDestinationSwitcherModifier _anyProposedAppLayoutContainsSelectedDisplayItem];
-[SBContinuousExposeWindowDragDestinationSwitcherModifier _appLayoutByAddingItem:toAppLayout:size:center:positionIsSystemManaged:];
-[SBContinuousExposeWindowDragDestinationSwitcherModifier _frameForSelectedAppLayout:addingToStage:];
-[SBContinuousExposeWindowDragDestinationSwitcherModifier _frameForSelectedDisplayItemAddingToStage:];
-[SBContinuousExposeWindowDragDestinationSwitcherModifier _layoutAttributesForTileDestination:];
-[SBContinuousExposeWindowDragDestinationSwitcherModifier _projectValue:withVelocityComponent:];
-[SBContinuousExposeWindowDragDestinationSwitcherModifier _projectedPositionWithPosition:velocity:];
-[SBContinuousExposeWindowDragDestinationSwitcherModifier _shouldProjectPositionForVelocity:];
-[SBContinuousExposeWindowDragDestinationSwitcherModifier _tileDestinationForFlickWithPosition:velocity:];
-[SBContinuousExposeWindowDragDestinationSwitcherModifier appLayoutByAddingAppLayout:toAppLayout:];
-[SBContinuousExposeWindowDragDestinationSwitcherModifier destinationDelegate];
-[SBContinuousExposeWindowDragDestinationSwitcherModifier hoveringOverAppLayout];
-[SBContinuousExposeWindowDragDestinationSwitcherModifier initWithSelectedDisplayItem:initialAppLayout:delegate:];
-[SBContinuousExposeWindowDragDestinationSwitcherModifier initialAppLayout];
-[SBContinuousExposeWindowDragDestinationSwitcherModifier proposedAppLayout];
-[SBContinuousExposeWindowDragDestinationSwitcherModifier proposedDestination];
-[SBContinuousExposeWindowDragDestinationSwitcherModifier selectedDisplayItem];
-[SBContinuousExposeWindowDragDestinationSwitcherModifier tileDestinationForEvent:];
-[SBContinuousExposeWindowDragDestinationSwitcherModifier updateProposedAppLayoutWithAppLayout:andInitialAppLayout:];
```
