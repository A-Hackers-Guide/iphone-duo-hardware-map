# `_UICollectionLayoutItemSolver`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `_UICollectionLayoutAuxillaryHosting`
- 14 instance variables, 4 properties, 14 instance methods, 0 class methods

## Instance variables

```
B _layoutRTL;
B _solvingConsumedDirtyPreferredSizes;
@"NSCollectionLayoutItem" _item;
@"_UICollectionLayoutContainer" _container;
@"UITraitCollection" _traitCollection;
Q _containerSizeDependentLayoutAxes;
@"_UICollectionLayoutItemSolverState" _solveResult;
@"_UICollectionPreferredSizes" _preferredSizes;
@"_UICollectionLayoutSupplementaryEnroller" _supplementaryEnroller;
q _solutionRecursionDepth;
q _maxFrameCount;
Q _layoutAxis;
{CGSize="width"d"height"d} _largestKnownItemSize;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _uncommittedSolvedItemFrame;
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
-[_UICollectionLayoutItemSolver auxillaryHostAuxillaryItems];
-[_UICollectionLayoutItemSolver auxillaryHostPinningRect];
-[_UICollectionLayoutItemSolver auxillaryHostTraitCollection];
-[_UICollectionLayoutItemSolver auxillaryHostContentSize];
-[_UICollectionLayoutItemSolver auxillaryHostAdditionalFrameOffset];
-[_UICollectionLayoutItemSolver auxillaryHostShouldLayoutRTL];
-[_UICollectionLayoutItemSolver auxillaryHostLayoutAxis];
-[_UICollectionLayoutItemSolver auxillaryHostSupplementaryEnroller];
-[_UICollectionLayoutItemSolver description];
-[_UICollectionLayoutItemSolver auxillaryHostContainer];
-[_UICollectionLayoutItemSolver auxillaryHostWantsOverlapAdjustmentForMatchingAlignmentsOnly];
-[_UICollectionLayoutItemSolver copyWithZone:];
-[_UICollectionLayoutItemSolver auxillaryHostAuxillaryKind];
-[_UICollectionLayoutItemSolver auxillaryHostPreferredSizes];
```
