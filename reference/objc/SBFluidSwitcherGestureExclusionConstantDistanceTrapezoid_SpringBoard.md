# `SBFluidSwitcherGestureExclusionConstantDistanceTrapezoid`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_SBFluidSwitcherGestureExclusionTrapezoidDebugViewDelegate`, `SBFluidSwitcherGestureExclusionShape`
- 5 instance variables, 9 properties, 16 instance methods, 1 class methods

## Instance variables

```
B _allowHorizontalSwipesOutsideTrapezoid;
d _baseHeight;
d _trapezoidHeight;
d _adjacentBaseXDistanceFromEdge;
d _opposingBaseXDistanceFromEdge;
```

## Properties

```
@property (Td,N,V_baseHeight) baseHeight;
@property (Td,N,V_trapezoidHeight) trapezoidHeight;
@property (Td,N,V_adjacentBaseXDistanceFromEdge) adjacentBaseXDistanceFromEdge;
@property (Td,N,V_opposingBaseXDistanceFromEdge) opposingBaseXDistanceFromEdge;
@property (TB,N,V_allowHorizontalSwipesOutsideTrapezoid) allowHorizontalSwipesOutsideTrapezoid;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBFluidSwitcherGestureExclusionConstantDistanceTrapezoid exclusionTrapezoidWithBaseHeight:trapezoidHeight:adjacentBaseXDistanceFromEdge:opposingBaseXDistanceFromEdge:allowHorizontalSwipesOutsideTrapezoid:];
```

## Instance methods

```
-[SBFluidSwitcherGestureExclusionConstantDistanceTrapezoid baseHeight];
-[SBFluidSwitcherGestureExclusionConstantDistanceTrapezoid debugView];
-[SBFluidSwitcherGestureExclusionConstantDistanceTrapezoid trapezoidHeight];
-[SBFluidSwitcherGestureExclusionConstantDistanceTrapezoid adjacentBaseXDistanceFromEdge];
-[SBFluidSwitcherGestureExclusionConstantDistanceTrapezoid adjacentBaseXDistanceFromEdgeForFluidSwitcherGestureExclusionTrapezoidDebugView:];
-[SBFluidSwitcherGestureExclusionConstantDistanceTrapezoid allowHorizontalSwipesOutsideTrapezoid];
-[SBFluidSwitcherGestureExclusionConstantDistanceTrapezoid baseHeightForFluidSwitcherGestureExclusionTrapezoidDebugView:];
-[SBFluidSwitcherGestureExclusionConstantDistanceTrapezoid opposingBaseXDistanceFromEdge];
-[SBFluidSwitcherGestureExclusionConstantDistanceTrapezoid opposingBaseXDistanceFromEdgeForFluidSwitcherGestureExclusionTrapezoidDebugView:];
-[SBFluidSwitcherGestureExclusionConstantDistanceTrapezoid setAdjacentBaseXDistanceFromEdge:];
-[SBFluidSwitcherGestureExclusionConstantDistanceTrapezoid setAllowHorizontalSwipesOutsideTrapezoid:];
-[SBFluidSwitcherGestureExclusionConstantDistanceTrapezoid setBaseHeight:];
-[SBFluidSwitcherGestureExclusionConstantDistanceTrapezoid setOpposingBaseXDistanceFromEdge:];
-[SBFluidSwitcherGestureExclusionConstantDistanceTrapezoid setTrapezoidHeight:];
-[SBFluidSwitcherGestureExclusionConstantDistanceTrapezoid shouldBeginGestureAtStartingPoint:velocity:bounds:];
-[SBFluidSwitcherGestureExclusionConstantDistanceTrapezoid trapezoidHeightForFluidSwitcherGestureExclusionTrapezoidDebugView:];
```
