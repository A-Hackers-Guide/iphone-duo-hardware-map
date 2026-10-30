# `_UICollectionViewDragAndDropController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UICollectionViewShadowUpdatesController`
- Protocols: `_UICollectionViewPlaceholderContextDelegate`, `_UICollectionViewDropCoordinator`, `UICollectionViewDropCoordinator`
- 20 instance variables, 10 properties, 52 instance methods, 0 class methods

## Instance variables

```
B _dragInteractionEnabled;
B _flockSelectedItemsOnDrag;
B _rebaseShadowUpdatesOnly;
B _hasReorderedItemInSession;
@"_UICollectionViewDragDestinationController" _destinationController;
@"_UICollectionViewDragSourceController" _sourceController;
Q _sessionKind;
q _preferredDragDestinationVisualStyle;
@"_UICollectionViewPlaceholderContext" _currentlyInsertingPlaceholderContext;
@"NSMutableDictionary" _placeholderContextsByIndexPath;
@"NSMutableSet" _placeholderContexts;
@"_UICollectionViewSubviewCollection" _viewsWithAppearanceUpdates;
@"NSMutableDictionary" _cellAppearanceStatesByIndexPaths;
@"NSMutableArray" _dropCoordinatorItems;
@"NSMapTable" _dropCoordinatorItemsMap;
@"NSMutableSet" _cellsDeferredForReuse;
q _sessionRefCount;
@"_UIDropAnimationHandlers" _defaultAnimationHandlers;
@"NSUUID" _currentDropInsertionShadowUpdateIdentifier;
@"NSMutableArray" __reorderedItems;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UICollectionViewDropProposal",R,N) dropProposal;
@property (T@"<UIDropSession>",R,N) dropSession;
@property (T@"NSArray",R,N) items;
@property (T@"NSIndexPath",R,N) destinationIndexPath;
@property (T@"UICollectionViewDropProposal",R,N) proposal;
@property (T@"<UIDropSession>",R,N) session;
```

## Instance methods

```
-[_UICollectionViewDragAndDropController dropSession];
-[_UICollectionViewDragAndDropController initWithCollectionView:];
-[_UICollectionViewDragAndDropController numberOfItemsInSection:];
-[_UICollectionViewDragAndDropController placeholderContextNeedsCellUpdate:];
-[_UICollectionViewDragAndDropController _removeMoveShadowUpdateMatchingReorderedItem:];
-[_UICollectionViewDragAndDropController placeholderContext:didCommitInsertionWithDataSourceUpdates:];
-[_UICollectionViewDragAndDropController dropItem:toPlaceholder:];
-[_UICollectionViewDragAndDropController numberOfSections];
-[_UICollectionViewDragAndDropController dropToLocation:inContainerView:withTransform:forDragItem:];
-[_UICollectionViewDragAndDropController dropItem:toPlaceholderInsertedAtIndexPath:withReuseIdentifier:cellUpdateHandler:];
-[_UICollectionViewDragAndDropController placeholderContextDidDismiss:];
-[_UICollectionViewDragAndDropController _resetReorderedItems];
-[_UICollectionViewDragAndDropController _updateCellAppearancesForItemsAtIndexPaths:];
-[_UICollectionViewDragAndDropController _resetAllAnimationHandlers];
-[_UICollectionViewDragAndDropController _rollbackCurrentDropInsertion];
-[_UICollectionViewDragAndDropController presentationIndexPathForDataSourceIndexPath:];
-[_UICollectionViewDragAndDropController reset];
-[_UICollectionViewDragAndDropController dropItem:toItemAtIndexPath:];
-[_UICollectionViewDragAndDropController insertPlaceholderForItemAtIndexPath:forDragItem:reuseIdentifier:cellUpdateHandler:];
-[_UICollectionViewDragAndDropController _shouldPerformTranslationForDelegateBasedFlowLayoutSizing];
-[_UICollectionViewDragAndDropController _removeAnyDeferredReuseCells];
-[_UICollectionViewDragAndDropController items];
-[_UICollectionViewDragAndDropController dropToTarget:forDragItem:];
-[_UICollectionViewDragAndDropController _addAnimationHandlers:toAnimator:];
-[_UICollectionViewDragAndDropController _decrementSessionRefCount];
-[_UICollectionViewDragAndDropController _presentationIndexPathForIndexPath:allowingAppendingInserts:];
-[_UICollectionViewDragAndDropController _shadowUpdateReuseIdentifierForItemItemAtIndexPath:];
-[_UICollectionViewDragAndDropController proposal];
-[_UICollectionViewDragAndDropController dropToItemAtIndexPath:forDragItem:];
-[_UICollectionViewDragAndDropController dropItem:intoItemAtIndexPath:rect:];
-[_UICollectionViewDragAndDropController _incrementSessionRefCount];
-[_UICollectionViewDragAndDropController rebaseForUpdates:];
-[_UICollectionViewDragAndDropController _cellForDropCoordinatorItem:];
-[_UICollectionViewDragAndDropController dropToPlaceholderInsertedAtIndexPath:reuseIdentifier:forDragItem:cellUpdateHandler:];
-[_UICollectionViewDragAndDropController dataSourceIndexPathForPresentationIndexPath:];
-[_UICollectionViewDragAndDropController description];
-[_UICollectionViewDragAndDropController dropItem:toTarget:];
-[_UICollectionViewDragAndDropController _invokeAllCompletionHandlers];
-[_UICollectionViewDragAndDropController destinationIndexPath];
-[_UICollectionViewDragAndDropController _updatePreferredDraggedCellAppearanceForSessionUpdate];
-[_UICollectionViewDragAndDropController _dropCoordinatorItemForIndexPath:];
-[_UICollectionViewDragAndDropController _updateCellIfNeeded:atIndexPath:];
-[_UICollectionViewDragAndDropController isDragDestinationInteractivelyReordering];
-[_UICollectionViewDragAndDropController _addDropCoordinatorItem:];
-[_UICollectionViewDragAndDropController session];
-[_UICollectionViewDragAndDropController dropToPlaceholderCellAtIndexPath:reuseIdentifier:forDragItem:cellUpdateHandler:];
-[_UICollectionViewDragAndDropController dropProposal];
-[_UICollectionViewDragAndDropController _cleanupAfterOutstandingSessionCompletion];
-[_UICollectionViewDragAndDropController _cellAppearanceStateForIndexPath:];
-[_UICollectionViewDragAndDropController _handleForcedDruidSessionEnd];
-[_UICollectionViewDragAndDropController _deleteShadowUpdateWithIdentifier:];
-[_UICollectionViewDragAndDropController _dropCoordinatorItemForDragItem:];
```
