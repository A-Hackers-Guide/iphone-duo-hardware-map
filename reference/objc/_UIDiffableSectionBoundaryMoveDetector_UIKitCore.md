# `_UIDiffableSectionBoundaryMoveDetector`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 2 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"_UIIdentifierDiffer" _differ;
@"_UIDiffableDataSourceState" _beforeState;
@"_UIDiffableDataSourceState" _afterState;
@"NSSet" _movePairs;
B _didShortCircuit;
```

## Properties

```
@property (T@"NSSet",R,N,V_movePairs) movePairs;
@property (TB,R,N,V_didShortCircuit) didShortCircuit;
```

## Instance methods

```
-[_UIDiffableSectionBoundaryMoveDetector initWithItemDiffer:beforeDataSourceState:afterDataSourceState:];
-[_UIDiffableSectionBoundaryMoveDetector movePairs];
-[_UIDiffableSectionBoundaryMoveDetector didShortCircuit];
-[_UIDiffableSectionBoundaryMoveDetector _computeMovePairsFoundation];
```
