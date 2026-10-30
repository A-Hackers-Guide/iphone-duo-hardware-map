# `ICDocCamReorderingThumbnailCollectionViewLayout`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UICollectionViewLayout`
- Protocols: `UICollectionViewDelegate`
- 18 instance variables, 23 properties, 55 instance methods, 1 class methods

## Instance variables

```
B _movingItem;
B _isScrollingBetweenPages;
B _isScrubbing;
B _isUndergoingOrientationChange;
B _layoutCacheIsValid;
@"<ICDocCamThumbnailViewLayoutDelegate>" _delegate;
d _itemSpacing;
d _topBottomMargins;
d _leftMargin;
d _rightMargin;
d _itemHeight;
@"NSArray" _itemAttributes;
@"NSMutableArray" _imageSizeCache;
Q _currentItem;
d _currentInterPageScrollPosition;
@"NSMutableArray" _deleteIndexPaths;
@"NSMutableArray" _insertIndexPaths;
{CGSize="width"d"height"d} _cachedContentSize;
```

## Properties

```
@property (Td,N,V_itemSpacing) itemSpacing;
@property (Td,N,V_topBottomMargins) topBottomMargins;
@property (Td,N,V_leftMargin) leftMargin;
@property (Td,N,V_rightMargin) rightMargin;
@property (Td,N,V_itemHeight) itemHeight;
@property (TB,N,V_layoutCacheIsValid) layoutCacheIsValid;
@property (T{CGSize=dd},N,V_cachedContentSize) cachedContentSize;
@property (T@"NSArray",C,N,V_itemAttributes) itemAttributes;
@property (T@"NSMutableArray",&,N,V_imageSizeCache) imageSizeCache;
@property (TQ,N,V_currentItem) currentItem;
@property (Td,N,V_currentInterPageScrollPosition) currentInterPageScrollPosition;
@property (Td,R,N) extraSpacingForCurrentItem;
@property (T@"NSMutableArray",&,N,V_deleteIndexPaths) deleteIndexPaths;
@property (T@"NSMutableArray",&,N,V_insertIndexPaths) insertIndexPaths;
@property (T@"<ICDocCamThumbnailViewLayoutDelegate>",R,W,N,V_delegate) delegate;
@property (TB,N,V_movingItem) movingItem;
@property (TB,N,V_isScrollingBetweenPages) isScrollingBetweenPages;
@property (TB,N,V_isScrubbing) isScrubbing;
@property (TB,N,V_isUndergoingOrientationChange) isUndergoingOrientationChange;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[ICDocCamReorderingThumbnailCollectionViewLayout effectiveAspectRatioForSize:];
```

## Instance methods

```
-[ICDocCamReorderingThumbnailCollectionViewLayout currentItem];
-[ICDocCamReorderingThumbnailCollectionViewLayout setIsScrubbing:];
-[ICDocCamReorderingThumbnailCollectionViewLayout initWithDelegate:];
-[ICDocCamReorderingThumbnailCollectionViewLayout invalidateLayoutWithContext:];
-[ICDocCamReorderingThumbnailCollectionViewLayout shouldInvalidateLayoutForBoundsChange:];
-[ICDocCamReorderingThumbnailCollectionViewLayout isScrubbing];
-[ICDocCamReorderingThumbnailCollectionViewLayout collectionViewContentSize];
-[ICDocCamReorderingThumbnailCollectionViewLayout finalLayoutAttributesForDisappearingItemAtIndexPath:];
-[ICDocCamReorderingThumbnailCollectionViewLayout itemSpacing];
-[ICDocCamReorderingThumbnailCollectionViewLayout delegate];
-[ICDocCamReorderingThumbnailCollectionViewLayout prepareForCollectionViewUpdates:];
-[ICDocCamReorderingThumbnailCollectionViewLayout setItemSpacing:];
-[ICDocCamReorderingThumbnailCollectionViewLayout targetContentOffsetForProposedContentOffset:withScrollingVelocity:];
-[ICDocCamReorderingThumbnailCollectionViewLayout initialLayoutAttributesForAppearingItemAtIndexPath:];
-[ICDocCamReorderingThumbnailCollectionViewLayout finalizeCollectionViewUpdates];
-[ICDocCamReorderingThumbnailCollectionViewLayout prepareLayout];
-[ICDocCamReorderingThumbnailCollectionViewLayout layoutAttributesForItemAtIndexPath:];
-[ICDocCamReorderingThumbnailCollectionViewLayout layoutAttributesForElementsInRect:];
-[ICDocCamReorderingThumbnailCollectionViewLayout setCurrentItem:];
-[ICDocCamReorderingThumbnailCollectionViewLayout setRightMargin:];
-[ICDocCamReorderingThumbnailCollectionViewLayout deleteIndexPaths];
-[ICDocCamReorderingThumbnailCollectionViewLayout insertIndexPaths];
-[ICDocCamReorderingThumbnailCollectionViewLayout rightMargin];
-[ICDocCamReorderingThumbnailCollectionViewLayout setDeleteIndexPaths:];
-[ICDocCamReorderingThumbnailCollectionViewLayout setInsertIndexPaths:];
-[ICDocCamReorderingThumbnailCollectionViewLayout itemHeight];
-[ICDocCamReorderingThumbnailCollectionViewLayout setLeftMargin:];
-[ICDocCamReorderingThumbnailCollectionViewLayout cachedContentSize];
-[ICDocCamReorderingThumbnailCollectionViewLayout setCachedContentSize:];
-[ICDocCamReorderingThumbnailCollectionViewLayout leftMargin];
-[ICDocCamReorderingThumbnailCollectionViewLayout itemAttributes];
-[ICDocCamReorderingThumbnailCollectionViewLayout setItemAttributes:];
-[ICDocCamReorderingThumbnailCollectionViewLayout horizontalContentOffsetForItem:];
-[ICDocCamReorderingThumbnailCollectionViewLayout currentInterPageScrollPosition];
-[ICDocCamReorderingThumbnailCollectionViewLayout extraSpacingForCurrentItem];
-[ICDocCamReorderingThumbnailCollectionViewLayout horizontalContentOffsetAdjustmentForItem:];
-[ICDocCamReorderingThumbnailCollectionViewLayout imageSizeCache];
-[ICDocCamReorderingThumbnailCollectionViewLayout isScrollingBetweenPages];
-[ICDocCamReorderingThumbnailCollectionViewLayout isUndergoingOrientationChange];
-[ICDocCamReorderingThumbnailCollectionViewLayout itemSizeForImageSize:];
-[ICDocCamReorderingThumbnailCollectionViewLayout layoutCacheIsValid];
-[ICDocCamReorderingThumbnailCollectionViewLayout movingItem];
-[ICDocCamReorderingThumbnailCollectionViewLayout setContentOffsetForItem:animated:];
-[ICDocCamReorderingThumbnailCollectionViewLayout setCurrentInterPageScrollPosition:];
-[ICDocCamReorderingThumbnailCollectionViewLayout setCurrentItem:animated:];
-[ICDocCamReorderingThumbnailCollectionViewLayout setImageSizeCache:];
-[ICDocCamReorderingThumbnailCollectionViewLayout setInterPageScrollPosition:];
-[ICDocCamReorderingThumbnailCollectionViewLayout setIsScrollingBetweenPages:];
-[ICDocCamReorderingThumbnailCollectionViewLayout setIsUndergoingOrientationChange:];
-[ICDocCamReorderingThumbnailCollectionViewLayout setItemHeight:];
-[ICDocCamReorderingThumbnailCollectionViewLayout setLayoutCacheIsValid:];
-[ICDocCamReorderingThumbnailCollectionViewLayout setMovingItem:];
-[ICDocCamReorderingThumbnailCollectionViewLayout setTopBottomMargins:];
-[ICDocCamReorderingThumbnailCollectionViewLayout topBottomMargins];
-[ICDocCamReorderingThumbnailCollectionViewLayout updateLayoutCacheIfNecessary];
```
