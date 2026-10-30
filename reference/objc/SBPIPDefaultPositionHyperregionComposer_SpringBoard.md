# `SBPIPDefaultPositionHyperregionComposer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBPIPPositionHyperregionComposing`
- 9 instance variables, 7 properties, 12 instance methods, 0 class methods

## Instance variables

```
B _isPad;
@"SBPIPPositionHyperregionLibrary" _regionsLibrary;
{SBPIPPositionInteractionStateContext="isStashed"B"isInteractive"B"hasActiveGesture"B"isFreelyPositionable"B"isStagingSplitPIP"B"projectedPosition"{CGPoint="x"d"y"d}"initialPosition"{CGPoint="x"d"y"d}"currentPosition"{CGPoint="x"d"y"d}"currentPositionStashProgress"d"projectedPositionStashProgress"d} _lastInteractionStateContext;
@"NSDictionary" _lastRegionsMap;
@"NSDictionary" _lastResolvedRegionsMap;
{SBPIPPositionGeometryContext="pipCurrentSize"{CGSize="width"d"height"d}"pipLastSteadySize"{CGSize="width"d"height"d}"pipStashedSize"{CGSize="width"d"height"d}"pipAnchorPointOffset"{CGPoint="x"d"y"d}"containerBounds"{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}"edgeInsets"{UIEdgeInsets="top"d"left"d"bottom"d"right"d}"minimumPadding"{UIEdgeInsets="top"d"left"d"bottom"d"right"d}"stashedMinimumPadding"{UIEdgeInsets="top"d"left"d"bottom"d"right"d}"stashedOcclusionRect"{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}"splitPIPSlotRect"{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}"offscreenCorners"Q"orientation"q"isContinuity"B} _lastGeometryContext;
@"<BSInvalidatable>" _stateCaptureInvalidatable;
@"<SBPIPPositionHyperregionComposerDelegate>" _delegate;
@"SBWindowScene" _representedWindowScene;
```

## Properties

```
@property (T@"SBWindowScene",W,N,V_representedWindowScene) representedWindowScene;
@property (T@"<SBPIPPositionHyperregionComposerDelegate>",W,N,V_delegate) delegate;
@property (T@"NSArray",?,C,N) connectedWindowScenes;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBPIPDefaultPositionHyperregionComposer init];
-[SBPIPDefaultPositionHyperregionComposer invalidate];
-[SBPIPDefaultPositionHyperregionComposer setDelegate:];
-[SBPIPDefaultPositionHyperregionComposer delegate];
-[SBPIPDefaultPositionHyperregionComposer _addRegionWithType:geometry:toMap:];
-[SBPIPDefaultPositionHyperregionComposer _pruneRegionsMap:geometry:interaction:];
-[SBPIPDefaultPositionHyperregionComposer _unprunedCornersForGeometry:];
-[SBPIPDefaultPositionHyperregionComposer canonicalPositionForPoint:proposedPosition:geometry:interaction:];
-[SBPIPDefaultPositionHyperregionComposer defaultCornerPositionForLayoutSettingsPosition:proposedCenter:geometry:interaction:];
-[SBPIPDefaultPositionHyperregionComposer positionRegionsForRegions:geometry:interaction:];
-[SBPIPDefaultPositionHyperregionComposer representedWindowScene];
-[SBPIPDefaultPositionHyperregionComposer setRepresentedWindowScene:];
```
