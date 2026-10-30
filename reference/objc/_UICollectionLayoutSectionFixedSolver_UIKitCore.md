# `_UICollectionLayoutSectionFixedSolver`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UICollectionLayoutSectionSolver`, `_UICollectionLayoutAuxillaryHosting`
- 18 instance variables, 20 properties, 57 instance methods, 0 class methods

## Instance variables

```
B _shouldAdjustContentSizeForPartialLastGroupSolution;
B _layoutRTL;
@"NSString" _errorDescription;
@"_UICollectionLayoutItemSolver" _solution;
@"_UICollectionLayoutAuxillaryItemSolver" _sectionAuxillarySolution;
@"_UICollectionLayoutSupplementaryEnroller" _sectionSupplementaryEnroller;
@"_UICollectionLayoutSectionGeometryTranslator" _sectionGeometryTranslator;
@"_UICollectionLayoutContainer" _memoizedAuxillaryHostContainer;
@"NSCollectionLayoutSection" _layoutSection;
@"_UICollectionLayoutContainer" _container;
@"_UICollectionLayoutContainer" _supplementaryContainer;
@"UITraitCollection" _traitCollection;
Q _layoutAxis;
Q _containerLayoutAxis;
q _frameCount;
{CGPoint="x"d"y"d} _orthogonalOffset;
{CGVector="dx"d"dy"d} _orthogonalScrollingPrefetchingUnitVector;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _overrideContentRectForPinning;
```

## Properties

```
@property (T@"NSCollectionLayoutSection",&,N,V_layoutSection) layoutSection;
@property (T@"_UICollectionLayoutContainer",&,N,V_container) container;
@property (T@"_UICollectionLayoutContainer",&,N,V_supplementaryContainer) supplementaryContainer;
@property (T@"UITraitCollection",&,N,V_traitCollection) traitCollection;
@property (TB,N,V_layoutRTL) layoutRTL;
@property (TQ,N,V_layoutAxis) layoutAxis;
@property (TQ,N,V_containerLayoutAxis) containerLayoutAxis;
@property (Tq,N,V_frameCount) frameCount;
@property (T{CGVector=dd},N,V_orthogonalScrollingPrefetchingUnitVector) orthogonalScrollingPrefetchingUnitVector;
@property (TQ,R,N) containerSizeDependentAxes;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) contentFrameIncludingAuxiliaries;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) primaryContentFrame;
@property (T@"NSIndexSet",R,N) pinnedSupplementaryIndexes;
@property (T@"NSString",R,N,V_errorDescription) errorDescription;
@property (TB,N,V_shouldAdjustContentSizeForPartialLastGroupSolution) shouldAdjustContentSizeForPartialLastGroupSolution;
@property (T{CGPoint=dd},N,V_orthogonalOffset) orthogonalOffset;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UICollectionLayoutSectionFixedSolver frameCount];
-[_UICollectionLayoutSectionFixedSolver pinnedSupplementaryIndexes];
-[_UICollectionLayoutSectionFixedSolver errorDescription];
-[_UICollectionLayoutSectionFixedSolver setTraitCollection:];
-[_UICollectionLayoutSectionFixedSolver auxillaryHostAuxillaryItems];
-[_UICollectionLayoutSectionFixedSolver traitCollection];
-[_UICollectionLayoutSectionFixedSolver auxillaryHostPinningRect];
-[_UICollectionLayoutSectionFixedSolver solveForContainer:supplementaryContainer:traitCollection:layoutAxis:frameCount:preferredSizes:layoutRTL:];
-[_UICollectionLayoutSectionFixedSolver solveForContainer:traitCollection:layoutAxis:frameCount:preferredSizes:];
-[_UICollectionLayoutSectionFixedSolver auxillaryHostPaddingBeforeBoundarySupplementaries];
-[_UICollectionLayoutSectionFixedSolver auxillaryHostTraitCollection];
-[_UICollectionLayoutSectionFixedSolver setContainerLayoutAxis:];
-[_UICollectionLayoutSectionFixedSolver layoutAxis];
-[_UICollectionLayoutSectionFixedSolver supplementaryContainer];
-[_UICollectionLayoutSectionFixedSolver frameForIndex:];
-[_UICollectionLayoutSectionFixedSolver setContainer:];
-[_UICollectionLayoutSectionFixedSolver auxillaryHostContentSize];
-[_UICollectionLayoutSectionFixedSolver setLayoutRTL:];
-[_UICollectionLayoutSectionFixedSolver preferredSizeGroupingRangeForItemAtIndex:];
-[_UICollectionLayoutSectionFixedSolver shouldAdjustContentSizeForPartialLastGroupSolution];
-[_UICollectionLayoutSectionFixedSolver unpinnedSectionSupplementaryFrameForIndex:];
-[_UICollectionLayoutSectionFixedSolver contentFrameIncludingAuxiliaries];
-[_UICollectionLayoutSectionFixedSolver solveForContainer:traitCollection:layoutAxis:frameCount:];
-[_UICollectionLayoutSectionFixedSolver setShouldAdjustContentSizeForPartialLastGroupSolution:];
-[_UICollectionLayoutSectionFixedSolver _dimensionForRootGroupAlongAxis:];
-[_UICollectionLayoutSectionFixedSolver setSupplementaryContainer:];
-[_UICollectionLayoutSectionFixedSolver visualDescription];
-[_UICollectionLayoutSectionFixedSolver layoutRTL];
-[_UICollectionLayoutSectionFixedSolver sectionSupplementaryFrameWithKind:index:];
-[_UICollectionLayoutSectionFixedSolver primaryContentFrame];
-[_UICollectionLayoutSectionFixedSolver queryFramesIntersectingRect:];
-[_UICollectionLayoutSectionFixedSolver auxillaryHostShouldLayoutRTL];
-[_UICollectionLayoutSectionFixedSolver auxillaryHostLayoutAxis];
-[_UICollectionLayoutSectionFixedSolver setLayoutAxis:];
-[_UICollectionLayoutSectionFixedSolver setOrthogonalOffset:];
-[_UICollectionLayoutSectionFixedSolver auxillaryHostSupplementaryEnroller];
-[_UICollectionLayoutSectionFixedSolver updatePinnedSupplementaryItemsWithVisibleBounds:overrideContentRectForPinning:];
-[_UICollectionLayoutSectionFixedSolver sectionSupplementaryFrameForIndex:];
-[_UICollectionLayoutSectionFixedSolver auxillaryHostContainer];
-[_UICollectionLayoutSectionFixedSolver resolveWithParameters:preferredSizes:];
-[_UICollectionLayoutSectionFixedSolver orthogonalScrollingPrefetchingUnitVector];
-[_UICollectionLayoutSectionFixedSolver queryFramesIntersectingRect:frameOffset:];
-[_UICollectionLayoutSectionFixedSolver sectionSupplementaryKindIndexForEnrollmentIdentifier:];
-[_UICollectionLayoutSectionFixedSolver auxillaryHostWantsOverlapAdjustmentForMatchingAlignmentsOnly];
-[_UICollectionLayoutSectionFixedSolver updatePinnedSupplementaryItemsWithVisibleBounds:];
-[_UICollectionLayoutSectionFixedSolver setFrameCount:];
-[_UICollectionLayoutSectionFixedSolver orthogonalOffset];
-[_UICollectionLayoutSectionFixedSolver setOrthogonalScrollingPrefetchingUnitVector:];
-[_UICollectionLayoutSectionFixedSolver supplementaryFrameWithKind:index:];
-[_UICollectionLayoutSectionFixedSolver auxillaryHostAuxillaryKind];
-[_UICollectionLayoutSectionFixedSolver setLayoutSection:];
-[_UICollectionLayoutSectionFixedSolver unpinnedSectionSupplementaryFrameWithKind:forIndex:];
-[_UICollectionLayoutSectionFixedSolver layoutSection];
-[_UICollectionLayoutSectionFixedSolver containerLayoutAxis];
-[_UICollectionLayoutSectionFixedSolver auxillaryHostPreferredSizes];
-[_UICollectionLayoutSectionFixedSolver container];
-[_UICollectionLayoutSectionFixedSolver containerSizeDependentAxes];
```
