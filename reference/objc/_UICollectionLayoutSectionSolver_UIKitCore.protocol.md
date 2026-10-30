# `_UICollectionLayoutSectionSolver` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`, `_UICollectionLayoutAuxillaryHosting`
- 0 instance variables, 15 properties, 35 instance methods, 0 class methods

## Properties

```
@property (T@"NSCollectionLayoutSection",R,N) layoutSection;
@property (T@"_UICollectionLayoutContainer",R,N) container;
@property (T@"_UICollectionLayoutContainer",R,N) supplementaryContainer;
@property (T@"UITraitCollection",R,N) traitCollection;
@property (TB,R,N) layoutRTL;
@property (TQ,R,N) layoutAxis;
@property (TQ,R,N) containerSizeDependentAxes;
@property (Tq,R,N) frameCount;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) contentFrameIncludingAuxiliaries;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) primaryContentFrame;
@property (T@"NSIndexSet",R,N) pinnedSupplementaryIndexes;
@property (T@"NSString",R,N) errorDescription;
@property (TB,N) shouldAdjustContentSizeForPartialLastGroupSolution;
@property (T{CGPoint=dd},N) orthogonalOffset;
@property (T{CGVector=dd},R,N) orthogonalScrollingPrefetchingUnitVector;
```

## Instance methods

```
-[_UICollectionLayoutSectionSolver frameCount];
-[_UICollectionLayoutSectionSolver pinnedSupplementaryIndexes];
-[_UICollectionLayoutSectionSolver errorDescription];
-[_UICollectionLayoutSectionSolver traitCollection];
-[_UICollectionLayoutSectionSolver solveForContainer:supplementaryContainer:traitCollection:layoutAxis:frameCount:preferredSizes:layoutRTL:];
-[_UICollectionLayoutSectionSolver solveForContainer:traitCollection:layoutAxis:frameCount:preferredSizes:];
-[_UICollectionLayoutSectionSolver layoutAxis];
-[_UICollectionLayoutSectionSolver supplementaryContainer];
-[_UICollectionLayoutSectionSolver frameForIndex:];
-[_UICollectionLayoutSectionSolver preferredSizeGroupingRangeForItemAtIndex:];
-[_UICollectionLayoutSectionSolver shouldAdjustContentSizeForPartialLastGroupSolution];
-[_UICollectionLayoutSectionSolver unpinnedSectionSupplementaryFrameForIndex:];
-[_UICollectionLayoutSectionSolver contentFrameIncludingAuxiliaries];
-[_UICollectionLayoutSectionSolver solveForContainer:traitCollection:layoutAxis:frameCount:];
-[_UICollectionLayoutSectionSolver setShouldAdjustContentSizeForPartialLastGroupSolution:];
-[_UICollectionLayoutSectionSolver _dimensionForRootGroupAlongAxis:];
-[_UICollectionLayoutSectionSolver visualDescription];
-[_UICollectionLayoutSectionSolver layoutRTL];
-[_UICollectionLayoutSectionSolver sectionSupplementaryFrameWithKind:index:];
-[_UICollectionLayoutSectionSolver primaryContentFrame];
-[_UICollectionLayoutSectionSolver queryFramesIntersectingRect:];
-[_UICollectionLayoutSectionSolver setOrthogonalOffset:];
-[_UICollectionLayoutSectionSolver updatePinnedSupplementaryItemsWithVisibleBounds:overrideContentRectForPinning:];
-[_UICollectionLayoutSectionSolver sectionSupplementaryFrameForIndex:];
-[_UICollectionLayoutSectionSolver resolveWithParameters:preferredSizes:];
-[_UICollectionLayoutSectionSolver orthogonalScrollingPrefetchingUnitVector];
-[_UICollectionLayoutSectionSolver queryFramesIntersectingRect:frameOffset:];
-[_UICollectionLayoutSectionSolver sectionSupplementaryKindIndexForEnrollmentIdentifier:];
-[_UICollectionLayoutSectionSolver updatePinnedSupplementaryItemsWithVisibleBounds:];
-[_UICollectionLayoutSectionSolver orthogonalOffset];
-[_UICollectionLayoutSectionSolver supplementaryFrameWithKind:index:];
-[_UICollectionLayoutSectionSolver unpinnedSectionSupplementaryFrameWithKind:forIndex:];
-[_UICollectionLayoutSectionSolver layoutSection];
-[_UICollectionLayoutSectionSolver container];
-[_UICollectionLayoutSectionSolver containerSizeDependentAxes];
```
