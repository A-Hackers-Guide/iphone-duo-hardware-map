# `SBFluidSwitcherGestureExclusionPercentageDistanceTrapezoid`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_SBFluidSwitcherGestureExclusionTrapezoidDebugViewDelegate`, `SBFluidSwitcherGestureExclusionShape`
- 5 instance variables, 9 properties, 16 instance methods, 1 class methods

## Instance variables

```
B _allowHorizontalSwipesOutsideTrapezoid;
d _baseHeight;
d _trapezoidHeight;
d _adjacentBaseXPercentageFromEdge;
d _opposingBaseXPercentageFromEdge;
```

## Properties

```
@property (Td,N,V_baseHeight) baseHeight;
@property (Td,N,V_trapezoidHeight) trapezoidHeight;
@property (Td,N,V_adjacentBaseXPercentageFromEdge) adjacentBaseXPercentageFromEdge;
@property (Td,N,V_opposingBaseXPercentageFromEdge) opposingBaseXPercentageFromEdge;
@property (TB,N,V_allowHorizontalSwipesOutsideTrapezoid) allowHorizontalSwipesOutsideTrapezoid;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBFluidSwitcherGestureExclusionPercentageDistanceTrapezoid exclusionTrapezoidWithBaseHeight:trapezoidHeight:adjacentBaseXPercentageFromEdge:opposingBaseXPercentageFromEdge:allowHorizontalSwipesOutsideTrapezoid:];
```

## Instance methods

```
-[SBFluidSwitcherGestureExclusionPercentageDistanceTrapezoid baseHeight];
-[SBFluidSwitcherGestureExclusionPercentageDistanceTrapezoid debugView];
-[SBFluidSwitcherGestureExclusionPercentageDistanceTrapezoid opposingBaseXPercentageFromEdge];
-[SBFluidSwitcherGestureExclusionPercentageDistanceTrapezoid trapezoidHeight];
-[SBFluidSwitcherGestureExclusionPercentageDistanceTrapezoid adjacentBaseXPercentageFromEdge];
-[SBFluidSwitcherGestureExclusionPercentageDistanceTrapezoid adjacentBaseXDistanceFromEdgeForFluidSwitcherGestureExclusionTrapezoidDebugView:];
-[SBFluidSwitcherGestureExclusionPercentageDistanceTrapezoid allowHorizontalSwipesOutsideTrapezoid];
-[SBFluidSwitcherGestureExclusionPercentageDistanceTrapezoid baseHeightForFluidSwitcherGestureExclusionTrapezoidDebugView:];
-[SBFluidSwitcherGestureExclusionPercentageDistanceTrapezoid opposingBaseXDistanceFromEdgeForFluidSwitcherGestureExclusionTrapezoidDebugView:];
-[SBFluidSwitcherGestureExclusionPercentageDistanceTrapezoid setAdjacentBaseXPercentageFromEdge:];
-[SBFluidSwitcherGestureExclusionPercentageDistanceTrapezoid setAllowHorizontalSwipesOutsideTrapezoid:];
-[SBFluidSwitcherGestureExclusionPercentageDistanceTrapezoid setBaseHeight:];
-[SBFluidSwitcherGestureExclusionPercentageDistanceTrapezoid setOpposingBaseXPercentageFromEdge:];
-[SBFluidSwitcherGestureExclusionPercentageDistanceTrapezoid setTrapezoidHeight:];
-[SBFluidSwitcherGestureExclusionPercentageDistanceTrapezoid shouldBeginGestureAtStartingPoint:velocity:bounds:];
-[SBFluidSwitcherGestureExclusionPercentageDistanceTrapezoid trapezoidHeightForFluidSwitcherGestureExclusionTrapezoidDebugView:];
```
