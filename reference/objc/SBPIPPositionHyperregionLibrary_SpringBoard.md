# `SBPIPPositionHyperregionLibrary`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBPIPPositionHyperregionProviding`
- 9 instance variables, 4 properties, 17 instance methods, 0 class methods

## Instance variables

```
B _isPad;
{SBPIPPositionGeometryContext="pipCurrentSize"{CGSize="width"d"height"d}"pipLastSteadySize"{CGSize="width"d"height"d}"pipStashedSize"{CGSize="width"d"height"d}"pipAnchorPointOffset"{CGPoint="x"d"y"d}"containerBounds"{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}"edgeInsets"{UIEdgeInsets="top"d"left"d"bottom"d"right"d}"minimumPadding"{UIEdgeInsets="top"d"left"d"bottom"d"right"d}"stashedMinimumPadding"{UIEdgeInsets="top"d"left"d"bottom"d"right"d}"stashedOcclusionRect"{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}"splitPIPSlotRect"{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}"offscreenCorners"Q"orientation"q"isContinuity"B} _lastGeometryContext;
@"_UIHyperregionUnion" _lastCornersRegion;
@"_UIHyperregionUnion" _lastStashedLeftRegion;
@"_UIHyperregionUnion" _lastStashedRightRegion;
@"_UIHyperregionUnion" _lastOffscreenCorners;
@"_UIHyperregionUnion" _lastContainerInsetRegion;
@"_UIHyperregionUnion" _lastAllUnified;
@"_UIHyperregionUnion" _lastSplitPIPStagingSlot;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBPIPPositionHyperregionLibrary init];
-[SBPIPPositionHyperregionLibrary description];
-[SBPIPPositionHyperregionLibrary _stashedLeftRegionWithGeometry:];
-[SBPIPPositionHyperregionLibrary _allUnifiedRegionWithGeometry:];
-[SBPIPPositionHyperregionLibrary _containerInsetRegionWithGeometry:];
-[SBPIPPositionHyperregionLibrary _cornersRegionWithGeometry:];
-[SBPIPPositionHyperregionLibrary _insetRectForEdgeInsets:pipSize:containerBounds:];
-[SBPIPPositionHyperregionLibrary _lastKnownRegionForType:];
-[SBPIPPositionHyperregionLibrary _offscreenCornersRegionWithGeometry:];
-[SBPIPPositionHyperregionLibrary _resetLastKnownRegions];
-[SBPIPPositionHyperregionLibrary _splitPIPStagingSlotRegionWithGeometry:];
-[SBPIPPositionHyperregionLibrary _stashedInsetRectForContainerEdge:geometry:];
-[SBPIPPositionHyperregionLibrary _stashedRightRegionWithGeometry:];
-[SBPIPPositionHyperregionLibrary _validatedInsetRectWithinContainerBoundsWithGeometry:];
-[SBPIPPositionHyperregionLibrary _validatedMinimumPaddingAndEdgeInsetInsetRect:];
-[SBPIPPositionHyperregionLibrary _validatedStashedToStashedMaximumumRectWithGeometry:];
-[SBPIPPositionHyperregionLibrary regionWithType:geometry:];
```
