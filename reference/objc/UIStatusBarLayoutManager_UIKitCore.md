# `UIStatusBarLayoutManager`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 4 properties, 47 instance methods, 0 class methods

## Instance variables

```
i _region;
[52@"UIStatusBarItemView"] _itemViews;
B _persistentAnimationsEnabled;
B _usesVerticalLayout;
@"UIStatusBarForegroundView" _foregroundView;
@"NSNumber" _assignedStartPosition;
```

## Properties

```
@property (T@"UIStatusBarForegroundView",W,N,V_foregroundView) foregroundView;
@property (TB,N,V_persistentAnimationsEnabled) persistentAnimationsEnabled;
@property (TB,R,N,V_usesVerticalLayout) usesVerticalLayout;
@property (T@"NSNumber",&,N,V_assignedStartPosition) assignedStartPosition;
```

## Instance methods

```
-[UIStatusBarLayoutManager foregroundView];
-[UIStatusBarLayoutManager dealloc];
-[UIStatusBarLayoutManager setForegroundView:];
-[UIStatusBarLayoutManager itemViewOfType:];
-[UIStatusBarLayoutManager setPersistentAnimationsEnabled:];
-[UIStatusBarLayoutManager _addOriginDelta:toPoint:];
-[UIStatusBarLayoutManager _createViewForItem:withData:actions:];
-[UIStatusBarLayoutManager _dimensionForSize:];
-[UIStatusBarLayoutManager _frameForItemView:startPosition:firstView:];
-[UIStatusBarLayoutManager _itemViews];
-[UIStatusBarLayoutManager _itemViewsSortedForLayout];
-[UIStatusBarLayoutManager _positionAfterPlacingItemView:startPosition:firstView:];
-[UIStatusBarLayoutManager _positionNewItemViewsWithEnabledItems:];
-[UIStatusBarLayoutManager _prepareEnabledItemType:withEnabledItems:withData:actions:itemAppearing:itemDisappearing:];
-[UIStatusBarLayoutManager _processDelta:forView:];
-[UIStatusBarLayoutManager _repositionedNewFrame:sizeDelta:];
-[UIStatusBarLayoutManager _setOrigin:forPoint:];
-[UIStatusBarLayoutManager _sizeNeededForItemView:];
-[UIStatusBarLayoutManager _startPosition];
-[UIStatusBarLayoutManager _updateItemView:withData:actions:animated:];
-[UIStatusBarLayoutManager _viewForItem:];
-[UIStatusBarLayoutManager allItemViews];
-[UIStatusBarLayoutManager assignedStartPosition];
-[UIStatusBarLayoutManager clearOverlapFromItems:];
-[UIStatusBarLayoutManager distributeOverlap:amongItems:];
-[UIStatusBarLayoutManager initWithRegion:foregroundView:usesVerticalLayout:];
-[UIStatusBarLayoutManager itemIsVisible:];
-[UIStatusBarLayoutManager itemView:sizeChangedBy:];
-[UIStatusBarLayoutManager makeVisibleItemsPerformPendedActions];
-[UIStatusBarLayoutManager persistentAnimationsEnabled];
-[UIStatusBarLayoutManager positionInvisibleItems];
-[UIStatusBarLayoutManager prepareDoubleHeightItemWithEnabledItems:];
-[UIStatusBarLayoutManager prepareEnabledItems:withData:actions:];
-[UIStatusBarLayoutManager rectForItems:];
-[UIStatusBarLayoutManager reflowWithVisibleItems:duration:];
-[UIStatusBarLayoutManager removeDisabledItems:];
-[UIStatusBarLayoutManager removeOverlap:fromItems:];
-[UIStatusBarLayoutManager setAssignedStartPosition:];
-[UIStatusBarLayoutManager setVisibilityOfAllItems:];
-[UIStatusBarLayoutManager setVisibilityOfItem:visible:];
-[UIStatusBarLayoutManager setVisibilityOfItemType:visible:];
-[UIStatusBarLayoutManager sizeNeededForItem:];
-[UIStatusBarLayoutManager sizeNeededForItems:];
-[UIStatusBarLayoutManager updateDoubleHeightItem];
-[UIStatusBarLayoutManager updateItemsWithData:actions:animated:];
-[UIStatusBarLayoutManager usesVerticalLayout];
-[UIStatusBarLayoutManager visibleItemViewAtPoint:inForegroundView:];
```
