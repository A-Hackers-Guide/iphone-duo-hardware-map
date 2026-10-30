# `UICollectionViewLayoutInvalidationContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 14 instance variables, 14 properties, 35 instance methods, 0 class methods

## Instance variables

```
@"NSMutableSet" _invalidatedItemIndexPaths;
@"NSMutableDictionary" _invalidatedSupplementaryIndexPaths;
@"NSMutableDictionary" _invalidatedDecorationIndexPaths;
@"NSArray" _updateItems;
@"NSArray" _previousIndexPathsForReorderedItems;
@"NSArray" _targetIndexPathsForReorderedItems;
{CGPoint="x"d"y"d} _reorderingTarget;
{CGPoint="x"d"y"d} _contentOffsetAdjustment;
{CGSize="width"d"height"d} _contentSizeAdjustment;
@"NSMutableIndexSet" _orthogonalSectionsWithContentSizeChanges;
{?="invalidateDataSource"b1"invalidateEverything"b1"invalidateContentSize"b1"isLazy"b1"forceRequireFullCacheInvalidation"b1} _invalidationContextFlags;
B _retainExistingSizingInfoForEstimates;
q _intent;
@"NSOrderedSet" __indexPathsForItemsRequiringPreferredAttributes;
```

## Properties

```
@property (TB,N,S_setInvalidateDataSourceCounts:) invalidateDataSourceCounts;
@property (TB,N,S_setInvalidateEverything:) invalidateEverything;
@property (T@"NSArray",&,N,G_updateItems,S_setUpdateItems:) updateItems;
@property (T@"NSArray",C,N,S_setPreviousIndexPathsForInteractivelyMovingItems:) previousIndexPathsForInteractivelyMovingItems;
@property (T@"NSArray",C,N,S_setTargetIndexPathsForInteractivelyMovingItems:) targetIndexPathsForInteractivelyMovingItems;
@property (T{CGPoint=dd},N,S_setInteractiveMovementTarget:) interactiveMovementTarget;
@property (TB,N,S_setShouldInvalidateCollectionViewContentSize:) _shouldInvalidateCollectionViewContentSize;
@property (TB,N,G_retainExistingSizingInfoForEstimates,S_setRetainExistingSizingInfoForEstimates:,V_retainExistingSizingInfoForEstimates) retainExistingSizingInfoForEstimates;
@property (Tq,N,G_intent,S_setIntent:,V_intent) intent;
@property (T@"NSArray",R,N) invalidatedItemIndexPaths;
@property (T@"NSDictionary",R,N) invalidatedSupplementaryIndexPaths;
@property (T@"NSDictionary",R,N) invalidatedDecorationIndexPaths;
@property (T{CGPoint=dd},N) contentOffsetAdjustment;
@property (T{CGSize=dd},N) contentSizeAdjustment;
```

## Instance methods

```
-[UICollectionViewLayoutInvalidationContext setContentOffsetAdjustment:];
-[UICollectionViewLayoutInvalidationContext _intent];
-[UICollectionViewLayoutInvalidationContext _setInvalidateDataSourceCounts:];
-[UICollectionViewLayoutInvalidationContext invalidatedDecorationIndexPaths];
-[UICollectionViewLayoutInvalidationContext _invalidateSupplementaryElementsOfKind:atIndexPaths:];
-[UICollectionViewLayoutInvalidationContext _invalidatedSupplementaryViews];
-[UICollectionViewLayoutInvalidationContext _removeInvalidatedDecorationOfKind:indexPath:];
-[UICollectionViewLayoutInvalidationContext _removeInvalidatedItemIndexPath:];
-[UICollectionViewLayoutInvalidationContext _removeInvalidatedSupplementaryOfKind:indexPath:];
-[UICollectionViewLayoutInvalidationContext _retainExistingSizingInfoForEstimates];
-[UICollectionViewLayoutInvalidationContext _setIntent:];
-[UICollectionViewLayoutInvalidationContext _setInteractiveMovementTarget:];
-[UICollectionViewLayoutInvalidationContext _setInvalidateEverything:];
-[UICollectionViewLayoutInvalidationContext _setInvalidatedSupplementaryViews:];
-[UICollectionViewLayoutInvalidationContext _setPreviousIndexPathsForInteractivelyMovingItems:];
-[UICollectionViewLayoutInvalidationContext _setRequiresFullCacheInvalidation];
-[UICollectionViewLayoutInvalidationContext _setRetainExistingSizingInfoForEstimates:];
-[UICollectionViewLayoutInvalidationContext _setShouldInvalidateCollectionViewContentSize:];
-[UICollectionViewLayoutInvalidationContext _setTargetIndexPathsForInteractivelyMovingItems:];
-[UICollectionViewLayoutInvalidationContext _setUpdateItems:];
-[UICollectionViewLayoutInvalidationContext _shouldInvalidateCollectionViewContentSize];
-[UICollectionViewLayoutInvalidationContext _updateItems];
-[UICollectionViewLayoutInvalidationContext contentOffsetAdjustment];
-[UICollectionViewLayoutInvalidationContext contentSizeAdjustment];
-[UICollectionViewLayoutInvalidationContext interactiveMovementTarget];
-[UICollectionViewLayoutInvalidationContext invalidateDataSourceCounts];
-[UICollectionViewLayoutInvalidationContext invalidateDecorationElementsOfKind:atIndexPaths:];
-[UICollectionViewLayoutInvalidationContext invalidateEverything];
-[UICollectionViewLayoutInvalidationContext invalidateItemsAtIndexPaths:];
-[UICollectionViewLayoutInvalidationContext invalidateSupplementaryElementsOfKind:atIndexPaths:];
-[UICollectionViewLayoutInvalidationContext invalidatedItemIndexPaths];
-[UICollectionViewLayoutInvalidationContext invalidatedSupplementaryIndexPaths];
-[UICollectionViewLayoutInvalidationContext previousIndexPathsForInteractivelyMovingItems];
-[UICollectionViewLayoutInvalidationContext setContentSizeAdjustment:];
-[UICollectionViewLayoutInvalidationContext targetIndexPathsForInteractivelyMovingItems];
```
