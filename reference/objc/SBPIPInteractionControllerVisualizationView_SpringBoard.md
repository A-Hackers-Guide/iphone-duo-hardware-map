# `SBPIPInteractionControllerVisualizationView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 11 instance variables, 4 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"UIView" _containerView;
@"UIView" _unionView;
@"UIView" _mainGeometryView;
@"UIView" _extendedGeometryView;
@"UIView" _insetsGeometryView;
@"UIView" _fakePIPView;
@"NSMutableArray" _regionViews;
@"_UIHyperregionUnion" _regionUnion;
{SBPIPPositionInteractionStateContext="isStashed"B"isInteractive"B"hasActiveGesture"B"isFreelyPositionable"B"isStagingSplitPIP"B"projectedPosition"{CGPoint="x"d"y"d}"initialPosition"{CGPoint="x"d"y"d}"currentPosition"{CGPoint="x"d"y"d}"currentPositionStashProgress"d"projectedPositionStashProgress"d} _interactionContext;
{SBPIPPositionGeometryContext="pipCurrentSize"{CGSize="width"d"height"d}"pipLastSteadySize"{CGSize="width"d"height"d}"pipStashedSize"{CGSize="width"d"height"d}"pipAnchorPointOffset"{CGPoint="x"d"y"d}"containerBounds"{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}"edgeInsets"{UIEdgeInsets="top"d"left"d"bottom"d"right"d}"minimumPadding"{UIEdgeInsets="top"d"left"d"bottom"d"right"d}"stashedMinimumPadding"{UIEdgeInsets="top"d"left"d"bottom"d"right"d}"stashedOcclusionRect"{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}"splitPIPSlotRect"{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}"offscreenCorners"Q"orientation"q"isContinuity"B} _mainGeometryContext;
{SBPIPPositionGeometryContext="pipCurrentSize"{CGSize="width"d"height"d}"pipLastSteadySize"{CGSize="width"d"height"d}"pipStashedSize"{CGSize="width"d"height"d}"pipAnchorPointOffset"{CGPoint="x"d"y"d}"containerBounds"{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}"edgeInsets"{UIEdgeInsets="top"d"left"d"bottom"d"right"d}"minimumPadding"{UIEdgeInsets="top"d"left"d"bottom"d"right"d}"stashedMinimumPadding"{UIEdgeInsets="top"d"left"d"bottom"d"right"d}"stashedOcclusionRect"{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}"splitPIPSlotRect"{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}"offscreenCorners"Q"orientation"q"isContinuity"B} _extendedGeometryContext;
```

## Properties

```
@property (T@"_UIHyperregionUnion",&,N,V_regionUnion) regionUnion;
@property (T{SBPIPPositionGeometryContext={CGSize=dd}{CGSize=dd}{CGSize=dd}{CGPoint=dd}{CGRect={CGPoint=dd}{CGSize=dd}}{UIEdgeInsets=dddd}{UIEdgeInsets=dddd}{UIEdgeInsets=dddd}{CGRect={CGPoint=dd}{CGSize=dd}}{CGRect={CGPoint=dd}{CGSize=dd}}QqB},N,V_mainGeometryContext) mainGeometryContext;
@property (T{SBPIPPositionGeometryContext={CGSize=dd}{CGSize=dd}{CGSize=dd}{CGPoint=dd}{CGRect={CGPoint=dd}{CGSize=dd}}{UIEdgeInsets=dddd}{UIEdgeInsets=dddd}{UIEdgeInsets=dddd}{CGRect={CGPoint=dd}{CGSize=dd}}{CGRect={CGPoint=dd}{CGSize=dd}}QqB},N,V_extendedGeometryContext) extendedGeometryContext;
@property (T{SBPIPPositionInteractionStateContext=BBBBB{CGPoint=dd}{CGPoint=dd}{CGPoint=dd}dd},N,V_interactionContext) interactionContext;
```

## Instance methods

```
-[SBPIPInteractionControllerVisualizationView layoutSubviews];
-[SBPIPInteractionControllerVisualizationView hitTest:withEvent:];
-[SBPIPInteractionControllerVisualizationView pointInside:withEvent:];
-[SBPIPInteractionControllerVisualizationView _backgroundFrame];
-[SBPIPInteractionControllerVisualizationView interactionContext];
-[SBPIPInteractionControllerVisualizationView setInteractionContext:];
-[SBPIPInteractionControllerVisualizationView setRegionUnion:];
-[SBPIPInteractionControllerVisualizationView _unionFrame];
-[SBPIPInteractionControllerVisualizationView extendedGeometryContext];
-[SBPIPInteractionControllerVisualizationView mainGeometryContext];
-[SBPIPInteractionControllerVisualizationView regionUnion];
-[SBPIPInteractionControllerVisualizationView setExtendedGeometryContext:];
-[SBPIPInteractionControllerVisualizationView setMainGeometryContext:];
```
