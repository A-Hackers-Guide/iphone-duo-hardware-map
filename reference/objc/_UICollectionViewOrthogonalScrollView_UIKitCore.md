# `_UICollectionViewOrthogonalScrollView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIScrollView`
- Protocols: `_UICollectionViewOrthogonalScrollView`
- 6 instance variables, 9 properties, 27 instance methods, 1 class methods

## Instance variables

```
{?="isConfiguring"I} _orthogonalScrollViewFlags;
@"UICollectionView" _collectionView;
q _section;
@"_UICollectionViewSubviewRouter" _subviewRouter;
@"_UICollectionLayoutSectionDescriptor" _descriptor;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _baseContentInsets;
```

## Properties

```
@property (T{CGPoint=dd},R,N) contentOffset;
@property (T{CGSize=dd},R,N) contentSize;
@property (TB,R,N,GisTracking) tracking;
@property (TB,R,N,GisDragging) dragging;
@property (TB,R,N,GisDecelerating) decelerating;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UICollectionViewOrthogonalScrollView _supportsInvalidatingFocusCache];
```

## Instance methods

```
-[_UICollectionViewOrthogonalScrollView touchesEnded:withEvent:];
-[_UICollectionViewOrthogonalScrollView touchesCancelled:withEvent:];
-[_UICollectionViewOrthogonalScrollView focusItemsInRect:];
-[_UICollectionViewOrthogonalScrollView _edgesPropagatingSafeAreaInsetsToSubviews];
-[_UICollectionViewOrthogonalScrollView _notifyDidScroll];
-[_UICollectionViewOrthogonalScrollView _autoScrollAssistantUpdateContentOffset:];
-[_UICollectionViewOrthogonalScrollView dealloc];
-[_UICollectionViewOrthogonalScrollView _focusScrollBoundaryMetricsForItem:];
-[_UICollectionViewOrthogonalScrollView touchesBegan:withEvent:];
-[_UICollectionViewOrthogonalScrollView touchesMoved:withEvent:];
-[_UICollectionViewOrthogonalScrollView _focusPrimaryScrollableAxis];
-[_UICollectionViewOrthogonalScrollView _addSubview:positioned:relativeTo:];
-[_UICollectionViewOrthogonalScrollView exchangeSubviewAtIndex:withSubviewAtIndex:];
-[_UICollectionViewOrthogonalScrollView sendSubviewToBack:];
-[_UICollectionViewOrthogonalScrollView bringSubviewToFront:];
-[_UICollectionViewOrthogonalScrollView _contentOffsetForScrollingToTop];
-[_UICollectionViewOrthogonalScrollView _contentOffsetForScrollingToItemAtIndexPath:atScrollPosition:additionalInsets:itemFrame:];
-[_UICollectionViewOrthogonalScrollView _existingFocusItemsInRect:];
-[_UICollectionViewOrthogonalScrollView _extantFocusItemsInRect:];
-[_UICollectionViewOrthogonalScrollView _focusScrollableAreaInsets];
-[_UICollectionViewOrthogonalScrollView _panGestureLocationInView:];
-[_UICollectionViewOrthogonalScrollView _panGestureVelocityInView:];
-[_UICollectionViewOrthogonalScrollView _pointByApplyingBaseContentInsetsToPoint:];
-[_UICollectionViewOrthogonalScrollView _pointByRemovingBaseContentInsetsFromPoint:];
-[_UICollectionViewOrthogonalScrollView _scrollViewWillEndDraggingWithVelocity:targetContentOffset:];
-[_UICollectionViewOrthogonalScrollView _willRemoveSubview:];
-[_UICollectionViewOrthogonalScrollView contentOffsetAdjustedForCurrentScrollingBehavior:itemFrame:];
```
