# `_UICollectionViewLayoutSwipeActionsModule`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UISwipeActionHost_Internal`
- 3 instance variables, 7 properties, 42 instance methods, 0 class methods

## Instance variables

```
{?="layoutUpdateOrRefreshPending"b1"hasDeferredLayoutUpdateOrRefresh"b1"preserveExistingLayoutAttributesForSwipedViews"b1} _flags;
@"UICollectionViewLayout" _host;
@"UISwipeActionController" _swipeActionController;
```

## Properties

```
@property (T@"UICollectionViewLayout",W,N,V_host) host;
@property (T@"UISwipeActionController",&,N,V_swipeActionController) swipeActionController;
@property (T@"UISwipeOccurrence",R,N) currentSwipeOccurrence;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UICollectionViewLayoutSwipeActionsModule setHost:];
-[_UICollectionViewLayoutSwipeActionsModule processLayoutInvalidationWithContext:updateConfigurations:];
-[_UICollectionViewLayoutSwipeActionsModule swipeActionController:didBeginSwipeForItemAtIndexPath:];
-[_UICollectionViewLayoutSwipeActionsModule swipeActionController:insertActionsView:forItemAtIndexPath:];
-[_UICollectionViewLayoutSwipeActionsModule propertyAnimatorForCollectionViewUpdates:withCustomAnimator:];
-[_UICollectionViewLayoutSwipeActionsModule swipeViewManipulatorForSwipeActionController:];
-[_UICollectionViewLayoutSwipeActionsModule _performForcedCollectionViewLayoutPreservingExistingLayoutAttributes];
-[_UICollectionViewLayoutSwipeActionsModule swipeActionController:leadingSwipeConfigurationForItemAtIndexPath:];
-[_UICollectionViewLayoutSwipeActionsModule layoutDirectionForSwipeActionController:];
-[_UICollectionViewLayoutSwipeActionsModule finalizeCollectionViewUpdate:];
-[_UICollectionViewLayoutSwipeActionsModule swipeActionController:trailingSwipeConfigurationForItemAtIndexPath:];
-[_UICollectionViewLayoutSwipeActionsModule _transformLayoutAttributes:ofSeparatorAtBottom:forSwipeOccurrence:isDisappearing:];
-[_UICollectionViewLayoutSwipeActionsModule swipeActionController:didEndSwipeForItemAtIndexPath:];
-[_UICollectionViewLayoutSwipeActionsModule initWithHost:];
-[_UICollectionViewLayoutSwipeActionsModule swipeActionController:viewForItemAtIndexPath:];
-[_UICollectionViewLayoutSwipeActionsModule editingStateDidChange];
-[_UICollectionViewLayoutSwipeActionsModule indexPathsWithActiveSwipes];
-[_UICollectionViewLayoutSwipeActionsModule transformDecorationLayoutAttributes:isDisappearing:];
-[_UICollectionViewLayoutSwipeActionsModule updateWithDataSourceTranslator:];
-[_UICollectionViewLayoutSwipeActionsModule swipeActionController:cleanupActionsView:forItemAtIndexPath:];
-[_UICollectionViewLayoutSwipeActionsModule swipeActionController];
-[_UICollectionViewLayoutSwipeActionsModule transformCellLayoutAttributes:isDisappearing:];
-[_UICollectionViewLayoutSwipeActionsModule swipeActionController:swipeOccurrence:didChangeStateFrom:to:];
-[_UICollectionViewLayoutSwipeActionsModule swipeItemAtIndexPath:direction:animated:completion:];
-[_UICollectionViewLayoutSwipeActionsModule swipeActionController:willBeginSwipeForItemAtIndexPath:];
-[_UICollectionViewLayoutSwipeActionsModule itemContainerViewForSwipeActionController:];
-[_UICollectionViewLayoutSwipeActionsModule swipeActionController:extraInsetsForItemAtIndexPath:];
-[_UICollectionViewLayoutSwipeActionsModule currentSwipeOccurrence];
-[_UICollectionViewLayoutSwipeActionsModule _canSwipeItemAtIndexPath:];
-[_UICollectionViewLayoutSwipeActionsModule hasActiveSwipe];
-[_UICollectionViewLayoutSwipeActionsModule _canIgnoreInvalidationContext:];
-[_UICollectionViewLayoutSwipeActionsModule _invalidateSwipeActionsLayoutRefreshingActiveConfigurations:];
-[_UICollectionViewLayoutSwipeActionsModule _updateSwipeActionsConfiguration:forIndexPath:];
-[_UICollectionViewLayoutSwipeActionsModule gestureRecognizerViewForSwipeActionController:];
-[_UICollectionViewLayoutSwipeActionsModule _cellWithCustomGroupingAtIndexPath:];
-[_UICollectionViewLayoutSwipeActionsModule swipeActionsStyleForSwipedItemAtIndexPath:];
-[_UICollectionViewLayoutSwipeActionsModule teardown];
-[_UICollectionViewLayoutSwipeActionsModule revealTrailingSwipeActionsForIndexPath:];
-[_UICollectionViewLayoutSwipeActionsModule swipeActionController:indexPathForTouchLocation:];
-[_UICollectionViewLayoutSwipeActionsModule swipeActionController:mayBeginSwipeForItemAtIndexPath:];
-[_UICollectionViewLayoutSwipeActionsModule host];
-[_UICollectionViewLayoutSwipeActionsModule setSwipeActionController:];
```
