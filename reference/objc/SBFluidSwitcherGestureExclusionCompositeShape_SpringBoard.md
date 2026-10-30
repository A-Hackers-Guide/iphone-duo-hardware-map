# `SBFluidSwitcherGestureExclusionCompositeShape`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFluidSwitcherGestureExclusionShape`
- 3 instance variables, 7 properties, 8 instance methods, 1 class methods

## Instance variables

```
B _allowHorizontalSwipesInsideShapes;
@"NSArray" _rects;
d _topEdgeY;
```

## Properties

```
@property (T@"NSArray",&,N,V_rects) rects;
@property (TB,N,V_allowHorizontalSwipesInsideShapes) allowHorizontalSwipesInsideShapes;
@property (Td,N,V_topEdgeY) topEdgeY;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBFluidSwitcherGestureExclusionCompositeShape exclusionCompositeShapeWithRects:allowHorizontalSwipes:];
```

## Instance methods

```
-[SBFluidSwitcherGestureExclusionCompositeShape debugView];
-[SBFluidSwitcherGestureExclusionCompositeShape rects];
-[SBFluidSwitcherGestureExclusionCompositeShape setRects:];
-[SBFluidSwitcherGestureExclusionCompositeShape allowHorizontalSwipesInsideShapes];
-[SBFluidSwitcherGestureExclusionCompositeShape setAllowHorizontalSwipesInsideShapes:];
-[SBFluidSwitcherGestureExclusionCompositeShape setTopEdgeY:];
-[SBFluidSwitcherGestureExclusionCompositeShape shouldBeginGestureAtStartingPoint:velocity:bounds:];
-[SBFluidSwitcherGestureExclusionCompositeShape topEdgeY];
```
