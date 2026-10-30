# `_UICollectionLayoutSectionListSolver`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UICollectionLayoutSectionSolver`, `_UICollectionLayoutAuxillaryHosting`
- 21 instance variables, 20 properties, 57 instance methods, 0 class methods

## Instance variables

```
{vector<_UIRegionSolveResult, std::allocator<_UIRegionSolveResult>>="__begin_"^{_UIRegionSolveResult}"__end_"^{_UIRegionSolveResult}""{?="__cap_"^{_UIRegionSolveResult}}} _regions;
{unique_ptr<_UIItemSolveResult, std::default_delete<_UIItemSolveResult>>=""{?="__ptr_"^{_UIItemSolveResult}}} _templateItemSolveResult;
B _shouldAdjustContentSizeForPartialLastGroupSolution;
B _layoutRTL;
@"NSString" _errorDescription;
@"_UICollectionLayoutItemSolver" _solution;
@"_UICollectionLayoutAuxillaryItemSolver" _sectionAuxillarySolution;
@"_UICollectionLayoutSupplementaryEnroller" _sectionSupplementaryEnroller;
@"_UICollectionLayoutSectionGeometryTranslator" _sectionGeometryTranslator;
@"_UICollectionLayoutContainer" _memoizedAuxillaryHostContainer;
@"_UICollectionPreferredSizes" _preferredSizes;
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
-[_UICollectionLayoutSectionListSolver frameCount];
-[_UICollectionLayoutSectionListSolver pinnedSupplementaryIndexes];
-[_UICollectionLayoutSectionListSolver errorDescription];
-[_UICollectionLayoutSectionListSolver setTraitCollection:];
-[_UICollectionLayoutSectionListSolver auxillaryHostAuxillaryItems];
-[_UICollectionLayoutSectionListSolver traitCollection];
-[_UICollectionLayoutSectionListSolver auxillaryHostPinningRect];
-[_UICollectionLayoutSectionListSolver solveForContainer:supplementaryContainer:traitCollection:layoutAxis:frameCount:preferredSizes:layoutRTL:];
-[_UICollectionLayoutSectionListSolver solveForContainer:traitCollection:layoutAxis:frameCount:preferredSizes:];
-[_UICollectionLayoutSectionListSolver auxillaryHostPaddingBeforeBoundarySupplementaries];
-[_UICollectionLayoutSectionListSolver auxillaryHostTraitCollection];
-[_UICollectionLayoutSectionListSolver setContainerLayoutAxis:];
-[_UICollectionLayoutSectionListSolver layoutAxis];
-[_UICollectionLayoutSectionListSolver supplementaryContainer];
-[_UICollectionLayoutSectionListSolver frameForIndex:];
-[_UICollectionLayoutSectionListSolver setContainer:];
-[_UICollectionLayoutSectionListSolver auxillaryHostContentSize];
-[_UICollectionLayoutSectionListSolver setLayoutRTL:];
-[_UICollectionLayoutSectionListSolver preferredSizeGroupingRangeForItemAtIndex:];
-[_UICollectionLayoutSectionListSolver shouldAdjustContentSizeForPartialLastGroupSolution];
-[_UICollectionLayoutSectionListSolver unpinnedSectionSupplementaryFrameForIndex:];
-[_UICollectionLayoutSectionListSolver contentFrameIncludingAuxiliaries];
-[_UICollectionLayoutSectionListSolver solveForContainer:traitCollection:layoutAxis:frameCount:];
-[_UICollectionLayoutSectionListSolver setShouldAdjustContentSizeForPartialLastGroupSolution:];
-[_UICollectionLayoutSectionListSolver _dimensionForRootGroupAlongAxis:];
-[_UICollectionLayoutSectionListSolver setSupplementaryContainer:];
-[_UICollectionLayoutSectionListSolver visualDescription];
-[_UICollectionLayoutSectionListSolver layoutRTL];
-[_UICollectionLayoutSectionListSolver sectionSupplementaryFrameWithKind:index:];
-[_UICollectionLayoutSectionListSolver primaryContentFrame];
-[_UICollectionLayoutSectionListSolver queryFramesIntersectingRect:];
-[_UICollectionLayoutSectionListSolver auxillaryHostShouldLayoutRTL];
-[_UICollectionLayoutSectionListSolver auxillaryHostLayoutAxis];
-[_UICollectionLayoutSectionListSolver setLayoutAxis:];
-[_UICollectionLayoutSectionListSolver setOrthogonalOffset:];
-[_UICollectionLayoutSectionListSolver auxillaryHostSupplementaryEnroller];
-[_UICollectionLayoutSectionListSolver updatePinnedSupplementaryItemsWithVisibleBounds:overrideContentRectForPinning:];
-[_UICollectionLayoutSectionListSolver sectionSupplementaryFrameForIndex:];
-[_UICollectionLayoutSectionListSolver auxillaryHostContainer];
-[_UICollectionLayoutSectionListSolver resolveWithParameters:preferredSizes:];
-[_UICollectionLayoutSectionListSolver orthogonalScrollingPrefetchingUnitVector];
-[_UICollectionLayoutSectionListSolver queryFramesIntersectingRect:frameOffset:];
-[_UICollectionLayoutSectionListSolver sectionSupplementaryKindIndexForEnrollmentIdentifier:];
-[_UICollectionLayoutSectionListSolver auxillaryHostWantsOverlapAdjustmentForMatchingAlignmentsOnly];
-[_UICollectionLayoutSectionListSolver updatePinnedSupplementaryItemsWithVisibleBounds:];
-[_UICollectionLayoutSectionListSolver setFrameCount:];
-[_UICollectionLayoutSectionListSolver orthogonalOffset];
-[_UICollectionLayoutSectionListSolver setOrthogonalScrollingPrefetchingUnitVector:];
-[_UICollectionLayoutSectionListSolver supplementaryFrameWithKind:index:];
-[_UICollectionLayoutSectionListSolver auxillaryHostAuxillaryKind];
-[_UICollectionLayoutSectionListSolver setLayoutSection:];
-[_UICollectionLayoutSectionListSolver unpinnedSectionSupplementaryFrameWithKind:forIndex:];
-[_UICollectionLayoutSectionListSolver layoutSection];
-[_UICollectionLayoutSectionListSolver containerLayoutAxis];
-[_UICollectionLayoutSectionListSolver auxillaryHostPreferredSizes];
-[_UICollectionLayoutSectionListSolver container];
-[_UICollectionLayoutSectionListSolver containerSizeDependentAxes];
```
