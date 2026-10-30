# `UICollectionViewCompositionalLayout`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UICollectionViewLayout`
- Protocols: `_UICollectionViewLayoutInteractionStateModuleHost`
- 20 instance variables, 21 properties, 172 instance methods, 1 class methods

## Instance variables

```
@"UICollectionViewCompositionalLayoutConfiguration" _configuration;
@"_UICollectionViewLayoutInteractionStateModule" _interactionStateModule;
{?="deferringInitialSolveUntilPrepare"b1"shouldAdjustContentInsetModeForCollectionViewNeverMode"b1"forceFullResolveOnNextInvalidation"b1"skippingDeferredSolvesUntilUpdateOrReloadDataInvalidation"b1"recomputesLayoutForEmptyUpdates"b1} _compositionalLayoutFlags;
Q _deferredResolveType;
B _layoutRTL;
B _roundsToScreenScale;
@"NSCollectionLayoutSection" _layoutSectionTemplate;
@? _layoutSectionProvider;
@"_UICollectionCompositionalLayoutSolver" _solver;
@"_UIDataSourceSnapshotter" _dataSourceSnapshotter;
Q _edgesForSafeAreaPropagation;
@"_UIUpdateVisibleCellsContext" _updateVisibleCellsContext;
@"_UICollectionCompositionalLayoutSolverUpdate" _currentUpdate;
@"_UICollectionCompositionalLayoutSolverResolveResult" _currentResolveResult;
@"<UITraitChangeRegistration>" _collectionViewTraitChangeRegistration;
@? _dynamicsConfigurationHandler;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _memoizedDynamicAnimatorWorldAdjustingInsets;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _memoizedPreviousLayoutMargins;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _memoizedPreviousSolvedCollectionViewBounds;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _contentFrame;
```

## Properties

```
@property (T@"NSCollectionLayoutSection",&,N,V_layoutSectionTemplate) layoutSectionTemplate;
@property (T@?,C,N,V_layoutSectionProvider) layoutSectionProvider;
@property (T@"_UICollectionCompositionalLayoutSolver",&,N,V_solver) solver;
@property (T{UIEdgeInsets=dddd},N,V_memoizedDynamicAnimatorWorldAdjustingInsets) memoizedDynamicAnimatorWorldAdjustingInsets;
@property (T{UIEdgeInsets=dddd},N,V_memoizedPreviousLayoutMargins) memoizedPreviousLayoutMargins;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_memoizedPreviousSolvedCollectionViewBounds) memoizedPreviousSolvedCollectionViewBounds;
@property (T@"_UIDataSourceSnapshotter",&,N,V_dataSourceSnapshotter) dataSourceSnapshotter;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_contentFrame) contentFrame;
@property (TQ,N,V_edgesForSafeAreaPropagation) edgesForSafeAreaPropagation;
@property (T@"_UIUpdateVisibleCellsContext",&,N,V_updateVisibleCellsContext) updateVisibleCellsContext;
@property (T@"_UICollectionCompositionalLayoutSolverUpdate",&,N,V_currentUpdate) currentUpdate;
@property (T@"_UICollectionCompositionalLayoutSolverResolveResult",&,N,V_currentResolveResult) currentResolveResult;
@property (TB,N,V_layoutRTL) layoutRTL;
@property (TB,N,V_roundsToScreenScale) roundsToScreenScale;
@property (TB,N,S_setRecomputesLayoutForEmptyUpdates:) _recomputesLayoutForEmptyUpdates;
@property (T@?,C,N,V_dynamicsConfigurationHandler) dynamicsConfigurationHandler;
@property (T@"UICollectionViewCompositionalLayoutConfiguration",C,N) configuration;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UICollectionViewCompositionalLayout layoutWithListConfiguration:];
```

## Instance methods

```
-[UICollectionViewCompositionalLayout layoutAttributesForSupplementaryViewOfKind:atIndexPath:];
-[UICollectionViewCompositionalLayout scrollDirection];
-[UICollectionViewCompositionalLayout debugDescription];
-[UICollectionViewCompositionalLayout contentFrame];
-[UICollectionViewCompositionalLayout layoutAttributesForDecorationViewOfKind:atIndexPath:];
-[UICollectionViewCompositionalLayout _willBeginSwiping];
-[UICollectionViewCompositionalLayout _trailingSwipeActionsConfigurationForIndexPath:];
-[UICollectionViewCompositionalLayout invalidateLayoutWithContext:];
-[UICollectionViewCompositionalLayout shouldInvalidateLayoutForBoundsChange:];
-[UICollectionViewCompositionalLayout setConfiguration:];
-[UICollectionViewCompositionalLayout initWithSection:configuration:];
-[UICollectionViewCompositionalLayout boundarySupplementaryItems];
-[UICollectionViewCompositionalLayout setLayoutRTL:];
-[UICollectionViewCompositionalLayout setContentFrame:];
-[UICollectionViewCompositionalLayout initWithSectionProvider:configuration:];
-[UICollectionViewCompositionalLayout initWithSection:sectionProvider:configuration:];
-[UICollectionViewCompositionalLayout invalidationContextForBoundsChange:];
-[UICollectionViewCompositionalLayout collectionViewContentSize];
-[UICollectionViewCompositionalLayout layoutRTL];
-[UICollectionViewCompositionalLayout finalLayoutAttributesForDisappearingItemAtIndexPath:];
-[UICollectionViewCompositionalLayout setEditing:];
-[UICollectionViewCompositionalLayout configuration];
-[UICollectionViewCompositionalLayout initWithSection:];
-[UICollectionViewCompositionalLayout _leadingSwipeActionsConfigurationForIndexPath:];
-[UICollectionViewCompositionalLayout layoutAttributesForInteractivelyMovingItemAtIndexPath:withTargetPosition:];
-[UICollectionViewCompositionalLayout initialLayoutAttributesForAppearingItemAtIndexPath:];
-[UICollectionViewCompositionalLayout setBoundarySupplementaryItems:];
-[UICollectionViewCompositionalLayout isEditing];
-[UICollectionViewCompositionalLayout initWithSectionProvider:];
-[UICollectionViewCompositionalLayout prepareLayout];
-[UICollectionViewCompositionalLayout layoutAttributesForItemAtIndexPath:];
-[UICollectionViewCompositionalLayout layoutAttributesForElementsInRect:];
-[UICollectionViewCompositionalLayout _didEndSwiping];
-[UICollectionViewCompositionalLayout _estimatesSizes];
-[UICollectionViewCompositionalLayout _invalidationContextForUpdatedContentMargins:oldContentMargins:];
-[UICollectionViewCompositionalLayout _invokeVisibleItemsInvalidationHandlerIfNeededForVisibleBounds:];
-[UICollectionViewCompositionalLayout _transformCellLayoutAttributes:];
-[UICollectionViewCompositionalLayout setEdgesForSafeAreaPropagation:];
-[UICollectionViewCompositionalLayout _hasOrthogonalScrollingSections];
-[UICollectionViewCompositionalLayout _adjustCollectionViewContentInsetBehaviorForLayoutAxisIfNeeded:container:];
-[UICollectionViewCompositionalLayout _allowsItemInteractionsToBegin];
-[UICollectionViewCompositionalLayout _allowsPanningAcrossConstrainedAxisToBeginMultiSelectInteractionInSection:];
-[UICollectionViewCompositionalLayout _anchorForAuxiliaryElementOfKind:];
-[UICollectionViewCompositionalLayout _boundsChangeResolve];
-[UICollectionViewCompositionalLayout _cellBackgroundOrBottomSeparatorChangedAtIndexPath:separatorOnly:];
-[UICollectionViewCompositionalLayout _cellsShouldConferWithAutolayoutEngineForSizingInfo];
-[UICollectionViewCompositionalLayout _collectionViewWillPerformPendingLayoutBeforeUpdate];
-[UICollectionViewCompositionalLayout _computeAndUpdateAdjustedContentFrame];
-[UICollectionViewCompositionalLayout _containerFromCollectionView];
-[UICollectionViewCompositionalLayout _contentFrameForSection:];
-[UICollectionViewCompositionalLayout _createSwipeActionsModuleIfNeeded];
-[UICollectionViewCompositionalLayout _customContainerSectionIndexes];
-[UICollectionViewCompositionalLayout _dataSourceSnapshotter];
-[UICollectionViewCompositionalLayout _didPerformUpdateVisibleCellsPassWithLayoutOffset:];
-[UICollectionViewCompositionalLayout _disallowsFadeCellsForBoundsChange];
-[UICollectionViewCompositionalLayout _edgesForSafeAreaPropagationToDescendants];
-[UICollectionViewCompositionalLayout _estimatesSupplementaryItems];
-[UICollectionViewCompositionalLayout _extendedAttributesQueryIncludingOrthogonalScrollingRegions:];
-[UICollectionViewCompositionalLayout _finalizeCollectionViewUpdate:];
-[UICollectionViewCompositionalLayout _frameForScrollingToFirstElementInSectionAtIndex:];
-[UICollectionViewCompositionalLayout _fullResolve];
-[UICollectionViewCompositionalLayout _handleEndInteractiveReorderingWithContext:];
-[UICollectionViewCompositionalLayout _handlePreferredSizingDataInvalidation:];
-[UICollectionViewCompositionalLayout _handleSwipeActionsInvalidationWithContext:];
-[UICollectionViewCompositionalLayout _insetsHaveChangedOnOrthogonalAxisFromOldInsets:newInsets:];
-[UICollectionViewCompositionalLayout _interactionStateModule:layoutSectionForIndex:];
-[UICollectionViewCompositionalLayout _interactionStateModule:spacingAfterLayoutSection:];
-[UICollectionViewCompositionalLayout _interactionStateModule:swipeActionsStyleForSwipedItemAtIndexPath:];
-[UICollectionViewCompositionalLayout _invalidationContextForUpdatedInsets:oldInsets:];
-[UICollectionViewCompositionalLayout _invalidationContextForUpdatedLayoutMargins:];
-[UICollectionViewCompositionalLayout _invalidationContextForUpdatedLayoutMargins:oldMargins:];
-[UICollectionViewCompositionalLayout _invalidationContextForUpdatedSafeAreaInsets:oldInsets:];
-[UICollectionViewCompositionalLayout _invalidationContextForUpdatedScrollAccessoryInsets:oldInsets:];
-[UICollectionViewCompositionalLayout _invokeVisibleBoundsUpdateForDynamicAnimatorForNewVisibleBounds:preparingLayout:];
-[UICollectionViewCompositionalLayout _layoutAttributesForIndelibleElements];
-[UICollectionViewCompositionalLayout _layoutAxis];
-[UICollectionViewCompositionalLayout _layoutFrameForSection:];
-[UICollectionViewCompositionalLayout _layoutSectionForSectionIndex:];
-[UICollectionViewCompositionalLayout _layoutTypeForSection:];
-[UICollectionViewCompositionalLayout _marginsChangeResolve];
-[UICollectionViewCompositionalLayout _offsetForOrthogonalScrollingSection:];
-[UICollectionViewCompositionalLayout _orthogonalFrameWithOffsetElidedForItemWithLayoutAttributes:frame:];
-[UICollectionViewCompositionalLayout _orthogonalScrollingAxis];
-[UICollectionViewCompositionalLayout _orthogonalScrollingContentRectForSection:];
-[UICollectionViewCompositionalLayout _orthogonalScrollingElementShouldAppearAboveForAttributes:];
-[UICollectionViewCompositionalLayout _orthogonalScrollingElementShouldAppearBelowForAttributes:];
-[UICollectionViewCompositionalLayout _orthogonalScrollingLayoutRectForSection:];
-[UICollectionViewCompositionalLayout _orthogonalScrollingSections];
-[UICollectionViewCompositionalLayout _overridesSafeAreaPropagationToDescendants];
-[UICollectionViewCompositionalLayout _postProcessPreferredAttributes:forView:];
-[UICollectionViewCompositionalLayout _preferredAttributesResolveWithInvalidatedPreferredAttributes:layoutOffset:visibleRect:];
-[UICollectionViewCompositionalLayout _prepareForCollectionViewUpdates:withDataSourceTranslator:];
-[UICollectionViewCompositionalLayout _prepareForPreferredAttributesQueryForView:withLayoutAttributes:];
-[UICollectionViewCompositionalLayout _prepareForTransitionToLayout:];
-[UICollectionViewCompositionalLayout _prepareLayout];
-[UICollectionViewCompositionalLayout _preparedForBoundsChanges];
-[UICollectionViewCompositionalLayout _propertyAnimatorForCollectionViewUpdates:withCustomAnimator:];
-[UICollectionViewCompositionalLayout _queueDeferredResolveForInvalidationWithContext:];
-[UICollectionViewCompositionalLayout _recomputesLayoutForEmptyUpdates];
-[UICollectionViewCompositionalLayout _resolveImmediatelyForInvalidationWithContext:];
-[UICollectionViewCompositionalLayout _scrollViewAdjustmentsChangeResolve];
-[UICollectionViewCompositionalLayout _scrollViewLayoutAdjustmentsChanged];
-[UICollectionViewCompositionalLayout _sectionDefinitionsUpdateResolve];
-[UICollectionViewCompositionalLayout _sectionDescriptorForSectionIndex:];
-[UICollectionViewCompositionalLayout _sectionsDescription];
-[UICollectionViewCompositionalLayout _setCollectionView:];
-[UICollectionViewCompositionalLayout _setOffset:forOrthogonalScrollingSection:];
-[UICollectionViewCompositionalLayout _setRecomputesLayoutForEmptyUpdates:];
-[UICollectionViewCompositionalLayout _shouldAddElementToSectionContainer:];
-[UICollectionViewCompositionalLayout _shouldAdjustTargetContentOffsetToValidateContentExtents];
-[UICollectionViewCompositionalLayout _shouldInvalidateLayoutForDataSourceChange];
-[UICollectionViewCompositionalLayout _shouldOrthogonalScrollingSectionDecorationScrollWithContentForIndexPath:elementKind:];
-[UICollectionViewCompositionalLayout _shouldOrthogonalScrollingSectionSupplementaryScrollWithContentForIndexPath:elementKind:];
-[UICollectionViewCompositionalLayout _shouldPopulateInitialAndFinalLayoutAttributesForAllUpdateItems:];
-[UICollectionViewCompositionalLayout _solveForPinnedSupplementaryItemsIfNeededWithContext:];
-[UICollectionViewCompositionalLayout _solverObservedTraitsDidChange];
-[UICollectionViewCompositionalLayout _supplementaryViewInsetsForScrollingToItemAtIndexPath:];
-[UICollectionViewCompositionalLayout _supportsPrefetchingWithEstimatedSizes];
-[UICollectionViewCompositionalLayout _supportsSwipeActionsForIndexPath:];
-[UICollectionViewCompositionalLayout _targetPositionForInteractiveMovementOfItemAtIndexPath:withProposedTargetPosition:];
-[UICollectionViewCompositionalLayout _transformDecorationLayoutAttributes:];
-[UICollectionViewCompositionalLayout _transformSupplementaryLayoutAttributes:];
-[UICollectionViewCompositionalLayout _updateCollectionViewBackgroundColor];
-[UICollectionViewCompositionalLayout _updatePinnedSectionSupplementaryItemsForCurrentVisibleBounds];
-[UICollectionViewCompositionalLayout _updateResolve];
-[UICollectionViewCompositionalLayout _updateStyleForSwipeActionsConfiguration:indexPath:];
-[UICollectionViewCompositionalLayout _viewBoundsPermitsLayout:];
-[UICollectionViewCompositionalLayout _wantsAnimationsForOffscreenAuxillaries];
-[UICollectionViewCompositionalLayout _wantsBandSelectionVisualsInSection:];
-[UICollectionViewCompositionalLayout _wantsCustomSectionContainers];
-[UICollectionViewCompositionalLayout _wantsInvalidateLayoutForPreferredLayoutAttributes];
-[UICollectionViewCompositionalLayout _wantsUntrackedAnimationCleanupForAuxillaryItems];
-[UICollectionViewCompositionalLayout _wantsUpdateVisibleCellsPassNotifications];
-[UICollectionViewCompositionalLayout _willPerformUpdateVisibleCellsPass];
-[UICollectionViewCompositionalLayout canBeEdited];
-[UICollectionViewCompositionalLayout currentResolveResult];
-[UICollectionViewCompositionalLayout currentUpdate];
-[UICollectionViewCompositionalLayout dataSourceSnapshotter];
-[UICollectionViewCompositionalLayout developmentLayoutDirection];
-[UICollectionViewCompositionalLayout dynamicsConfigurationHandler];
-[UICollectionViewCompositionalLayout edgesForSafeAreaPropagation];
-[UICollectionViewCompositionalLayout finalLayoutAttributesForDisappearingDecorationElementOfKind:atIndexPath:];
-[UICollectionViewCompositionalLayout indexPathsToDeleteForDecorationViewOfKind:];
-[UICollectionViewCompositionalLayout indexPathsToDeleteForSupplementaryViewOfKind:];
-[UICollectionViewCompositionalLayout indexPathsToInsertForDecorationViewOfKind:];
-[UICollectionViewCompositionalLayout indexPathsToInsertForSupplementaryViewOfKind:];
-[UICollectionViewCompositionalLayout initWithLayoutSection:];
-[UICollectionViewCompositionalLayout initWithLayoutSection:scrollDirection:];
-[UICollectionViewCompositionalLayout initialLayoutAttributesForAppearingDecorationElementOfKind:atIndexPath:];
-[UICollectionViewCompositionalLayout initialLayoutAttributesForAppearingSupplementaryElementOfKind:atIndexPath:];
-[UICollectionViewCompositionalLayout invalidationContextForPreferredLayoutAttributes:withOriginalAttributes:];
-[UICollectionViewCompositionalLayout layoutSectionProvider];
-[UICollectionViewCompositionalLayout layoutSectionTemplate];
-[UICollectionViewCompositionalLayout memoizedDynamicAnimatorWorldAdjustingInsets];
-[UICollectionViewCompositionalLayout memoizedPreviousLayoutMargins];
-[UICollectionViewCompositionalLayout memoizedPreviousSolvedCollectionViewBounds];
-[UICollectionViewCompositionalLayout roundsToScreenScale];
-[UICollectionViewCompositionalLayout setCurrentResolveResult:];
-[UICollectionViewCompositionalLayout setCurrentUpdate:];
-[UICollectionViewCompositionalLayout setDataSourceSnapshotter:];
-[UICollectionViewCompositionalLayout setDynamicsConfigurationHandler:];
-[UICollectionViewCompositionalLayout setLayoutSectionProvider:];
-[UICollectionViewCompositionalLayout setLayoutSectionTemplate:];
-[UICollectionViewCompositionalLayout setMemoizedDynamicAnimatorWorldAdjustingInsets:];
-[UICollectionViewCompositionalLayout setMemoizedPreviousLayoutMargins:];
-[UICollectionViewCompositionalLayout setMemoizedPreviousSolvedCollectionViewBounds:];
-[UICollectionViewCompositionalLayout setRoundsToScreenScale:];
-[UICollectionViewCompositionalLayout setSolver:];
-[UICollectionViewCompositionalLayout setUpdateVisibleCellsContext:];
-[UICollectionViewCompositionalLayout shouldInvalidateLayoutForPreferredLayoutAttributes:withOriginalAttributes:];
-[UICollectionViewCompositionalLayout solver];
-[UICollectionViewCompositionalLayout updateVisibleCellsContext];
```
