# `_UICollectionLayoutSectionEstimatedSolver`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UICollectionLayoutSectionSolver`, `_UICollectionLayoutAuxillaryHosting`
- 19 instance variables, 19 properties, 56 instance methods, 0 class methods

## Instance variables

```
B _layoutRTL;
B _shouldAdjustContentSizeForPartialLastGroupSolution;
@"NSCollectionLayoutSection" _layoutSection;
@"_UICollectionLayoutContainer" _container;
@"UITraitCollection" _traitCollection;
Q _layoutAxis;
q _frameCount;
@"_UICollectionPreferredSizes" _preferredSizes;
@"NSString" _errorDescription;
Q _containerSizeDependentAxes;
@"_UICollectionLayoutAuxillaryItemSolver" _sectionSupplementarySolution;
@"_UICollectionLayoutSupplementaryEnroller" _sectionSupplementaryEnroller;
@"_UICollectionLayoutContainer" _memoizedSupplementaryHostContainer;
@"_UICollectionLayoutSolutionState" _solutionState;
Q _containerLayoutAxis;
@"_UICollectionLayoutContainer" _supplementaryContainer;
{CGPoint="x"d"y"d} _orthogonalOffset;
{CGVector="dx"d"dy"d} _orthogonalScrollingPrefetchingUnitVector;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _overrideContentRectForPinning;
```

## Properties

```
@property (T{CGVector=dd},N,V_orthogonalScrollingPrefetchingUnitVector) orthogonalScrollingPrefetchingUnitVector;
@property (T@"_UICollectionLayoutContainer",&,N,V_supplementaryContainer) supplementaryContainer;
@property (T@"NSCollectionLayoutSection",R,N,V_layoutSection) layoutSection;
@property (T@"_UICollectionLayoutContainer",R,N,V_container) container;
@property (T@"UITraitCollection",R,N,V_traitCollection) traitCollection;
@property (TB,R,N,V_layoutRTL) layoutRTL;
@property (TQ,R,N,V_layoutAxis) layoutAxis;
@property (TQ,R,N,V_containerSizeDependentAxes) containerSizeDependentAxes;
@property (Tq,R,N,V_frameCount) frameCount;
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
-[_UICollectionLayoutSectionEstimatedSolver frameCount];
-[_UICollectionLayoutSectionEstimatedSolver pinnedSupplementaryIndexes];
-[_UICollectionLayoutSectionEstimatedSolver errorDescription];
-[_UICollectionLayoutSectionEstimatedSolver auxillaryHostAuxillaryItems];
-[_UICollectionLayoutSectionEstimatedSolver _rectWithContentInsetTrailingLayoutDimensionAddedToToRect:insets:layoutAxis:];
-[_UICollectionLayoutSectionEstimatedSolver _rangeOfBookmarksAffectedByResolveItems:];
-[_UICollectionLayoutSectionEstimatedSolver traitCollection];
-[_UICollectionLayoutSectionEstimatedSolver auxillaryHostPinningRect];
-[_UICollectionLayoutSectionEstimatedSolver solveForContainer:supplementaryContainer:traitCollection:layoutAxis:frameCount:preferredSizes:layoutRTL:];
-[_UICollectionLayoutSectionEstimatedSolver solveForContainer:traitCollection:layoutAxis:frameCount:preferredSizes:];
-[_UICollectionLayoutSectionEstimatedSolver auxillaryHostPaddingBeforeBoundarySupplementaries];
-[_UICollectionLayoutSectionEstimatedSolver auxillaryHostTraitCollection];
-[_UICollectionLayoutSectionEstimatedSolver layoutAxis];
-[_UICollectionLayoutSectionEstimatedSolver supplementaryContainer];
-[_UICollectionLayoutSectionEstimatedSolver frameForIndex:];
-[_UICollectionLayoutSectionEstimatedSolver _adjustContentFrameForLastPartialSolutionIfNeededForContentFrame:bookmarks:];
-[_UICollectionLayoutSectionEstimatedSolver auxillaryHostContentSize];
-[_UICollectionLayoutSectionEstimatedSolver preferredSizeGroupingRangeForItemAtIndex:];
-[_UICollectionLayoutSectionEstimatedSolver shouldAdjustContentSizeForPartialLastGroupSolution];
-[_UICollectionLayoutSectionEstimatedSolver unpinnedSectionSupplementaryFrameForIndex:];
-[_UICollectionLayoutSectionEstimatedSolver contentFrameIncludingAuxiliaries];
-[_UICollectionLayoutSectionEstimatedSolver solveForContainer:traitCollection:layoutAxis:frameCount:];
-[_UICollectionLayoutSectionEstimatedSolver setShouldAdjustContentSizeForPartialLastGroupSolution:];
-[_UICollectionLayoutSectionEstimatedSolver _dimensionForRootGroupAlongAxis:];
-[_UICollectionLayoutSectionEstimatedSolver setSupplementaryContainer:];
-[_UICollectionLayoutSectionEstimatedSolver visualDescription];
-[_UICollectionLayoutSectionEstimatedSolver layoutRTL];
-[_UICollectionLayoutSectionEstimatedSolver sectionSupplementaryFrameWithKind:index:];
-[_UICollectionLayoutSectionEstimatedSolver primaryContentFrame];
-[_UICollectionLayoutSectionEstimatedSolver queryFramesIntersectingRect:];
-[_UICollectionLayoutSectionEstimatedSolver auxillaryHostShouldLayoutRTL];
-[_UICollectionLayoutSectionEstimatedSolver auxillaryHostLayoutAxis];
-[_UICollectionLayoutSectionEstimatedSolver _configureInitialOrthogonalPrefetchingUnitVector];
-[_UICollectionLayoutSectionEstimatedSolver _updateSolutionAuxillaryRangeIndexerKindDict:fromBookmark:];
-[_UICollectionLayoutSectionEstimatedSolver setOrthogonalOffset:];
-[_UICollectionLayoutSectionEstimatedSolver auxillaryHostSupplementaryEnroller];
-[_UICollectionLayoutSectionEstimatedSolver updatePinnedSupplementaryItemsWithVisibleBounds:overrideContentRectForPinning:];
-[_UICollectionLayoutSectionEstimatedSolver sectionSupplementaryFrameForIndex:];
-[_UICollectionLayoutSectionEstimatedSolver auxillaryHostContainer];
-[_UICollectionLayoutSectionEstimatedSolver resolveWithParameters:preferredSizes:];
-[_UICollectionLayoutSectionEstimatedSolver orthogonalScrollingPrefetchingUnitVector];
-[_UICollectionLayoutSectionEstimatedSolver queryFramesIntersectingRect:frameOffset:];
-[_UICollectionLayoutSectionEstimatedSolver sectionSupplementaryKindIndexForEnrollmentIdentifier:];
-[_UICollectionLayoutSectionEstimatedSolver _solveWithParameters:];
-[_UICollectionLayoutSectionEstimatedSolver auxillaryHostWantsOverlapAdjustmentForMatchingAlignmentsOnly];
-[_UICollectionLayoutSectionEstimatedSolver updatePinnedSupplementaryItemsWithVisibleBounds:];
-[_UICollectionLayoutSectionEstimatedSolver orthogonalOffset];
-[_UICollectionLayoutSectionEstimatedSolver setOrthogonalScrollingPrefetchingUnitVector:];
-[_UICollectionLayoutSectionEstimatedSolver supplementaryFrameWithKind:index:];
-[_UICollectionLayoutSectionEstimatedSolver _sectionContainer];
-[_UICollectionLayoutSectionEstimatedSolver auxillaryHostAuxillaryKind];
-[_UICollectionLayoutSectionEstimatedSolver unpinnedSectionSupplementaryFrameWithKind:forIndex:];
-[_UICollectionLayoutSectionEstimatedSolver layoutSection];
-[_UICollectionLayoutSectionEstimatedSolver auxillaryHostPreferredSizes];
-[_UICollectionLayoutSectionEstimatedSolver container];
-[_UICollectionLayoutSectionEstimatedSolver containerSizeDependentAxes];
```
