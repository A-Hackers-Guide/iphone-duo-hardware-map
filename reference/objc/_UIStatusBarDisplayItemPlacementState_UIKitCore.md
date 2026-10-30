# `_UIStatusBarDisplayItemPlacementState`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIStatusBarPrioritized`
- 3 instance variables, 7 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"_UIStatusBarDisplayItemPlacement" _placement;
@"_UIStatusBarRegion" _region;
@"NSMutableArray" _relations;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V_relations) relations;
@property (T@"_UIStatusBarDisplayItemPlacement",R,N,V_placement) placement;
@property (T@"_UIStatusBarRegion",R,W,N,V_region) region;
@property (TB,R,N,GareRelationsFulfilled) relationsFulfilled;
@property (TB,R,N) canBeEnabled;
@property (TB,R,N,GisEnabled) enabled;
@property (Tq,R,N) priority;
```

## Class methods

```
+[_UIStatusBarDisplayItemPlacementState stateForDisplayItemPlacement:region:];
```

## Instance methods

```
-[_UIStatusBarDisplayItemPlacementState priority];
-[_UIStatusBarDisplayItemPlacementState region];
-[_UIStatusBarDisplayItemPlacementState placement];
-[_UIStatusBarDisplayItemPlacementState isEnabled];
-[_UIStatusBarDisplayItemPlacementState relations];
-[_UIStatusBarDisplayItemPlacementState description];
-[_UIStatusBarDisplayItemPlacementState areRelationsFulfilled];
-[_UIStatusBarDisplayItemPlacementState canBeEnabled];
-[_UIStatusBarDisplayItemPlacementState setRelations:];
```
