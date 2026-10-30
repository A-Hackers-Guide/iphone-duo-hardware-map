# `_UICollectionViewDragSourceController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIDragInteractionDelegate_Private`
- 5 instance variables, 4 properties, 38 instance methods, 0 class methods

## Instance variables

```
@"UICollectionView" _collectionView;
@"UIDragInteraction" _dragInteraction;
@"_UICollectionViewDragAndDropController" _delegate;
@"_UICollectionViewDragSourceControllerSessionState" _sessionState;
@"_UICollectionViewDragSourceControllerDragState" _dragState;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UICollectionViewDragSourceController dragInteraction:previewForLiftingItem:session:];
-[_UICollectionViewDragSourceController dragInteraction:itemsForBeginningSession:];
-[_UICollectionViewDragSourceController dragInteraction:previewForCancellingItem:withDefault:];
-[_UICollectionViewDragSourceController dragInteraction:item:willAnimateCancelWithAnimator:];
-[_UICollectionViewDragSourceController dragInteraction:sessionDidMove:];
-[_UICollectionViewDragSourceController dragInteraction:session:didEndWithOperation:];
-[_UICollectionViewDragSourceController dragInteraction:sessionWillBegin:];
-[_UICollectionViewDragSourceController dragInteraction:prefersFullSizePreviewsForSession:];
-[_UICollectionViewDragSourceController _delegateImplementsDragSourceItemsAtIndexPath];
-[_UICollectionViewDragSourceController _dragDelegateProxy];
-[_UICollectionViewDragSourceController dragInteraction:session:willEndWithOperation:];
-[_UICollectionViewDragSourceController _delegateImplementsDragItemsForItemAtIndexPath];
-[_UICollectionViewDragSourceController _configureInteraction];
-[_UICollectionViewDragSourceController dragInteraction:sessionForAddingItems:withTouchAtPoint:];
-[_UICollectionViewDragSourceController dragInteraction:sessionAllowsMoveOperation:];
-[_UICollectionViewDragSourceController _sessionWillBegin:forDragInteraction:];
-[_UICollectionViewDragSourceController dragInteraction:sessionIsRestrictedToDraggingApplication:];
-[_UICollectionViewDragSourceController _dragInteraction:dataOwnerForSession:];
-[_UICollectionViewDragSourceController dealloc];
-[_UICollectionViewDragSourceController dragInteraction:session:willAddItems:forInteraction:];
-[_UICollectionViewDragSourceController _dataOwnerForDragSession:atIndexPath:];
-[_UICollectionViewDragSourceController _dragInteraction:sessionPropertiesForSession:];
-[_UICollectionViewDragSourceController _dragInteraction:dataOwnerForAddingToSession:withTouchAtPoint:];
-[_UICollectionViewDragSourceController initWithCollectionView:delegate:];
-[_UICollectionViewDragSourceController _delegateImplementsDragItemsForItemAtIndexPathWithDefaultPreview];
-[_UICollectionViewDragSourceController _previewParametersForItemAtIndexPath:];
-[_UICollectionViewDragSourceController _delegateImplementsDragSourceDidAddItem];
-[_UICollectionViewDragSourceController description];
-[_UICollectionViewDragSourceController dragInteraction:itemsForAddingToSession:withTouchAtPoint:];
-[_UICollectionViewDragSourceController _delegateImplementsSelector:];
-[_UICollectionViewDragSourceController _queryForItemsFromClientForSession:dataSourceIndexPath:location:isInitialQuery:];
-[_UICollectionViewDragSourceController dragInteraction:willAnimateLiftWithAnimator:session:];
-[_UICollectionViewDragSourceController _filterCandidateIndexPaths:forUserSelectedIndexPath:session:];
-[_UICollectionViewDragSourceController dragInteraction:sessionDidTransferItems:];
-[_UICollectionViewDragSourceController _dragSourceDelegateActual];
-[_UICollectionViewDragSourceController _dragSourceDelegateProxy];
-[_UICollectionViewDragSourceController _addDragItemsToExistingSession:forDataSourceIndexPath:];
-[_UICollectionViewDragSourceController _dragDelegateActual];
```
