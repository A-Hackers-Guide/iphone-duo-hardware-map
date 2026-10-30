# `_UICollectionCompositionalLayoutSolver`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UICollectionLayoutAuxillaryHosting`, `_UIDynamicReferenceSystem`
- 44 instance variables, 5 properties, 16 instance methods, 0 class methods

## Instance variables

```
{?="solutionBookmarksLocked"b1} _solverFlags;
B _estimatesSizes;
B _hasOrthogonalScrollingSections;
B _hasSectionsWithCustomContainers;
B _shouldPerformPhysicalRTLTransforms;
B _roundsToScreenScale;
B _layoutRTL;
@"_UITypedStorage" _typedStorage;
@? _cellLayoutAttributesTransformer;
@? _sectionDecorationLayoutAttributesTransformer;
@? _sectionSupplementaryLayoutAttributesTransformer;
@"_UICollectionLayoutContainer" _container;
@"UITraitCollection" _traitCollection;
Q _layoutAxis;
@"_UIDataSourceSnapshotter" _dataSourceSnapshot;
d _interSectionSpacing;
@"NSIndexSet" _orthogonalScrollingSectionIndexes;
@"NSIndexSet" _customContainerSectionIndexes;
@? _dynamicsConfigurationHandler;
@"_UICollectionCompositionalLayoutSolverOptions" _options;
# _layoutAttributeClass;
# _invalidationContextClass;
@? _invalidationHandler;
d _memoizedScreenScale;
@? _sectionProvider;
@"NSIndexSet" _solutionBookmarkIndexesWithPinnedSupplementaryItems;
@"_UICollectionCompositionalLayoutDynamicAnimator" _dynamicAnimator;
@"_UICollectionLayoutDynamicsConfiguration" _dynamicsConfiguration;
@"NSArray" _solutionBookmarks;
@"_UIRTree" _sectionIndexer;
@"_UICollectionLayoutSectionGeometryTranslator" _sectionGeometryTranslator;
@"NSMutableDictionary" _cachedItemAttributes;
@"NSMutableDictionary" _cachedSupplementaryAttributes;
@"NSMutableDictionary" _cachedDecorationAttributes;
Q _preUpdateCachedItemCount;
@"NSArray" _preUpdateSolutionBookmarks;
@"_UICollectionLayoutContainer" _preUpdateContainer;
@"_UIDataSourceSnapshotter" _preUpdateDataSourceSnapshot;
@"NSArray" _globalSupplementaryItems;
@"_UICollectionLayoutAuxillaryItemSolver" _globalSupplementarySolver;
@"_UICollectionPreferredSizes" _globalSupplementaryPreferredSizes;
q _numberOfSectionsWithTransformVisibleItemsHandler;
Q _containerSizeDependentAxes;
{CGSize="width"d"height"d} _actualContentSize;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) bounds;
```

## Instance methods

```
-[_UICollectionCompositionalLayoutSolver auxillaryHostAuxillaryItems];
-[_UICollectionCompositionalLayoutSolver auxillaryHostPinningRect];
-[_UICollectionCompositionalLayoutSolver auxillaryHostTraitCollection];
-[_UICollectionCompositionalLayoutSolver dealloc];
-[_UICollectionCompositionalLayoutSolver auxillaryHostContentSize];
-[_UICollectionCompositionalLayoutSolver _dynamicReferenceBounds];
-[_UICollectionCompositionalLayoutSolver auxillaryHostShouldLayoutRTL];
-[_UICollectionCompositionalLayoutSolver auxillaryHostLayoutAxis];
-[_UICollectionCompositionalLayoutSolver _fetchUpdatedSectionDefinitionsFromSectionProvider];
-[_UICollectionCompositionalLayoutSolver auxillaryHostSupplementaryEnroller];
-[_UICollectionCompositionalLayoutSolver bounds];
-[_UICollectionCompositionalLayoutSolver auxillaryHostContainer];
-[_UICollectionCompositionalLayoutSolver _fetchUpdatedSectionDefinitionsFromSectionProviderWithObservationTracking];
-[_UICollectionCompositionalLayoutSolver auxillaryHostWantsOverlapAdjustmentForMatchingAlignmentsOnly];
-[_UICollectionCompositionalLayoutSolver auxillaryHostAuxillaryKind];
-[_UICollectionCompositionalLayoutSolver auxillaryHostPreferredSizes];
```
