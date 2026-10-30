# `UICollectionViewFlowLayout`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UICollectionViewLayout`
- 25 instance variables, 12 properties, 102 instance methods, 1 class methods

## Instance variables

```
{?="delegateSizeForItem"b1"delegateReferenceSizeForHeader"b1"delegateReferenceSizeForFooter"b1"delegateInsetForSection"b1"delegateInteritemSpacingForSection"b1"delegateLineSpacingForSection"b1"delegateAlignmentOptions"b1"layoutDataIsValid"b1"delegateInfoIsValid"b1"roundsToScreenScale"b1"delegateSizesForSection"b1"sectionHeadersFloat"b1"sectionFootersFloat"b1"headerFollowsSectionMargins"b1"footerFollowsSectionMargins"b1"fetchingItemsInfoForRect"b1"isInUpdateVisibleCellsPass"b1} _gridLayoutFlags;
d _interitemSpacing;
d _lineSpacing;
{CGSize="width"d"height"d} _itemSize;
{CGSize="width"d"height"d} _estimatedItemSize;
{CGSize="width"d"height"d} _headerReferenceSize;
{CGSize="width"d"height"d} _footerReferenceSize;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _sectionInset;
@"_UIFlowLayoutInfo" _data;
{CGSize="width"d"height"d} _currentLayoutSize;
@"NSMutableDictionary" _insertedItemsAttributesDict;
@"NSMutableDictionary" _insertedSectionHeadersAttributesDict;
@"NSMutableDictionary" _insertedSectionFootersAttributesDict;
@"NSMutableDictionary" _deletedItemsAttributesDict;
@"NSMutableDictionary" _deletedSectionHeadersAttributesDict;
@"NSMutableDictionary" _deletedSectionFootersAttributesDict;
q _scrollDirection;
@"NSDictionary" _rowAlignmentsOptionsDictionary;
{CGPoint="x"d"y"d} _contentOffsetAdjustment;
{CGSize="width"d"height"d} _contentSizeAdjustment;
@"NSMutableDictionary" _cachedItemAttributes;
@"NSMutableDictionary" _cachedItemFrames;
@"_UIUpdateVisibleCellsContext" _updateVisibleCellsContext;
@"<_UICollectionViewUpdateTranslating>" _currentUpdateTranslator;
q _sectionInsetReference;
```

## Properties

```
@property (TB,R,N,G_estimatesSizes) estimatesSizes;
@property (Td,N,V_lineSpacing) minimumLineSpacing;
@property (Td,N,V_interitemSpacing) minimumInteritemSpacing;
@property (T{CGSize=dd},N,V_itemSize) itemSize;
@property (T{CGSize=dd},N,V_estimatedItemSize) estimatedItemSize;
@property (Tq,N) scrollDirection;
@property (T{CGSize=dd},N,V_headerReferenceSize) headerReferenceSize;
@property (T{CGSize=dd},N,V_footerReferenceSize) footerReferenceSize;
@property (T{UIEdgeInsets=dddd},N,V_sectionInset) sectionInset;
@property (Tq,N,V_sectionInsetReference) sectionInsetReference;
@property (TB,N) sectionHeadersPinToVisibleBounds;
@property (TB,N) sectionFootersPinToVisibleBounds;
```

## Class methods

```
+[UICollectionViewFlowLayout invalidationContextClass];
```

## Instance methods

```
-[UICollectionViewFlowLayout layoutAttributesForSupplementaryViewOfKind:atIndexPath:];
-[UICollectionViewFlowLayout scrollDirection];
-[UICollectionViewFlowLayout init];
-[UICollectionViewFlowLayout invalidateLayoutWithContext:];
-[UICollectionViewFlowLayout shouldInvalidateLayoutForBoundsChange:];
-[UICollectionViewFlowLayout _shouldScrollToContentBeginningInRightToLeft];
-[UICollectionViewFlowLayout invalidationContextForBoundsChange:];
-[UICollectionViewFlowLayout collectionViewContentSize];
-[UICollectionViewFlowLayout setScrollDirection:];
-[UICollectionViewFlowLayout encodeWithCoder:];
-[UICollectionViewFlowLayout initWithCoder:];
-[UICollectionViewFlowLayout prepareLayout];
-[UICollectionViewFlowLayout layoutAttributesForItemAtIndexPath:];
-[UICollectionViewFlowLayout layoutAttributesForElementsInRect:];
-[UICollectionViewFlowLayout _estimatesSizes];
-[UICollectionViewFlowLayout _sectionArrayIndexForIndexPath:];
-[UICollectionViewFlowLayout indexesForSectionHeadersInRect:];
-[UICollectionViewFlowLayout indexesForSectionFootersInRect:];
-[UICollectionViewFlowLayout _adjustedSectionInsetForSectionInset:forAxis:];
-[UICollectionViewFlowLayout _boundsAndInsetsAreValidForReferenceDimension];
-[UICollectionViewFlowLayout _calculateAttributesForRect:];
-[UICollectionViewFlowLayout _cellsShouldConferWithAutolayoutEngineForSizingInfo];
-[UICollectionViewFlowLayout _didPerformUpdateVisibleCellsPassWithLayoutOffset:];
-[UICollectionViewFlowLayout _dimensionFromCollectionView];
-[UICollectionViewFlowLayout _effectiveEstimatedItemSize];
-[UICollectionViewFlowLayout _existingLayoutAttributesForItemAtIndexPath:];
-[UICollectionViewFlowLayout _fetchAndCacheNewLayoutAttributesForCellWithIndexPath:frame:];
-[UICollectionViewFlowLayout _fetchItemsInfoForRect:];
-[UICollectionViewFlowLayout _finalizeCollectionViewUpdate:];
-[UICollectionViewFlowLayout _focusFastScrollingIndexBarInsets];
-[UICollectionViewFlowLayout _footerFollowsSectionMargins];
-[UICollectionViewFlowLayout _frameForFooterInSection:usingData:];
-[UICollectionViewFlowLayout _frameForHeaderInSection:usingData:];
-[UICollectionViewFlowLayout _frameForItem:inSection:usingData:];
-[UICollectionViewFlowLayout _frameForScrollingToFirstElementInSectionAtIndex:];
-[UICollectionViewFlowLayout _getSizingInfosWithExistingSizingDictionary:];
-[UICollectionViewFlowLayout _headerFollowsSectionMargins];
-[UICollectionViewFlowLayout _insetsHaveChangedOnOrthogonalAxisFromOldInsets:newInsets:];
-[UICollectionViewFlowLayout _invalidateButKeepAllInfo];
-[UICollectionViewFlowLayout _invalidateButKeepDelegateInfo];
-[UICollectionViewFlowLayout _invalidationContextForUpdatedInsets:oldInsets:];
-[UICollectionViewFlowLayout _invalidationContextForUpdatedLayoutMargins:];
-[UICollectionViewFlowLayout _invalidationContextForUpdatedLayoutMargins:oldMargins:];
-[UICollectionViewFlowLayout _invalidationContextForUpdatedSafeAreaInsets:oldInsets:];
-[UICollectionViewFlowLayout _invalidationContextForUpdatedScrollAccessoryInsets:oldInsets:];
-[UICollectionViewFlowLayout _layoutAttributesForItemsInRect:];
-[UICollectionViewFlowLayout _layoutAxis];
-[UICollectionViewFlowLayout _layoutFrameForSection:];
-[UICollectionViewFlowLayout _layoutTypeForSection:];
-[UICollectionViewFlowLayout _prepareForCollectionViewUpdates:withDataSourceTranslator:];
-[UICollectionViewFlowLayout _resetCachedItems];
-[UICollectionViewFlowLayout _roundsToScreenScale];
-[UICollectionViewFlowLayout _rowAlignmentOptions];
-[UICollectionViewFlowLayout _setCollectionView:];
-[UICollectionViewFlowLayout _setFooterFollowsSectionMargins:];
-[UICollectionViewFlowLayout _setHeaderFollowsSectionMargins:];
-[UICollectionViewFlowLayout _setNeedsLayoutComputationWithoutInvalidation];
-[UICollectionViewFlowLayout _setRoundsToScreenScale:];
-[UICollectionViewFlowLayout _setRowAlignmentsOptions:];
-[UICollectionViewFlowLayout _updateCollectionViewScrollableAxis];
-[UICollectionViewFlowLayout _updateContentSizeScrollingDimensionWithDelta:];
-[UICollectionViewFlowLayout _updateDelegateFlags];
-[UICollectionViewFlowLayout _updateItemsLayoutForRect:allowsPartialUpdate:];
-[UICollectionViewFlowLayout _willPerformUpdateVisibleCellsPass];
-[UICollectionViewFlowLayout developmentLayoutDirection];
-[UICollectionViewFlowLayout estimatedItemSize];
-[UICollectionViewFlowLayout finalLayoutAttributesForDeletedItemAtIndexPath:];
-[UICollectionViewFlowLayout finalLayoutAttributesForFooterInDeletedSection:];
-[UICollectionViewFlowLayout finalLayoutAttributesForHeaderInDeletedSection:];
-[UICollectionViewFlowLayout footerReferenceSize];
-[UICollectionViewFlowLayout headerReferenceSize];
-[UICollectionViewFlowLayout indexPathForItemAtPoint:];
-[UICollectionViewFlowLayout indexesForSectionFootersInRect:usingData:];
-[UICollectionViewFlowLayout indexesForSectionHeadersInRect:usingData:];
-[UICollectionViewFlowLayout initialLayoutAttributesForFooterInInsertedSection:];
-[UICollectionViewFlowLayout initialLayoutAttributesForHeaderInInsertedSection:];
-[UICollectionViewFlowLayout initialLayoutAttributesForInsertedItemAtIndexPath:];
-[UICollectionViewFlowLayout invalidationContextForPreferredLayoutAttributes:withOriginalAttributes:];
-[UICollectionViewFlowLayout itemSize];
-[UICollectionViewFlowLayout layoutAttributesForFooterInSection:];
-[UICollectionViewFlowLayout layoutAttributesForFooterInSection:usingData:];
-[UICollectionViewFlowLayout layoutAttributesForHeaderInSection:];
-[UICollectionViewFlowLayout layoutAttributesForHeaderInSection:usingData:];
-[UICollectionViewFlowLayout layoutAttributesForItemAtIndexPath:usingData:];
-[UICollectionViewFlowLayout minimumInteritemSpacing];
-[UICollectionViewFlowLayout minimumLineSpacing];
-[UICollectionViewFlowLayout sectionFootersPinToVisibleBounds];
-[UICollectionViewFlowLayout sectionHeadersPinToVisibleBounds];
-[UICollectionViewFlowLayout sectionInset];
-[UICollectionViewFlowLayout sectionInsetReference];
-[UICollectionViewFlowLayout setEstimatedItemSize:];
-[UICollectionViewFlowLayout setFooterReferenceSize:];
-[UICollectionViewFlowLayout setHeaderReferenceSize:];
-[UICollectionViewFlowLayout setItemSize:];
-[UICollectionViewFlowLayout setMinimumInteritemSpacing:];
-[UICollectionViewFlowLayout setMinimumLineSpacing:];
-[UICollectionViewFlowLayout setSectionFootersPinToVisibleBounds:];
-[UICollectionViewFlowLayout setSectionHeadersPinToVisibleBounds:];
-[UICollectionViewFlowLayout setSectionInset:];
-[UICollectionViewFlowLayout setSectionInsetReference:];
-[UICollectionViewFlowLayout shouldInvalidateLayoutForPreferredLayoutAttributes:withOriginalAttributes:];
-[UICollectionViewFlowLayout synchronizeLayout];
```
