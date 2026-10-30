# `_UIDiffableDataSourceSectionController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 7 instance variables, 4 properties, 44 instance methods, 0 class methods

## Instance variables

```
@"__UIDiffableDataSource" _dataSource;
@"NSMapTable" _snapshotsMap;
@"NSSet" _associatedSectionIdentifiers;
@"<_UIDiffableDataSourceSectionControllerDelegate>" _delegate;
@"_UIDiffableDataSourceExpandCollapseAnimationContext" _expandCollapseAnimationContext;
@"NSArray" _itemRenderers;
@"_UIDiffableDataSourceSectionControllerHandlers" _handlers;
```

## Properties

```
@property (T@"<_UIDiffableDataSourceSectionControllerDelegate>",W,N) delegate;
@property (T@"NSArray",R,N,V_itemRenderers) itemRenderers;
@property (T@"NSSet",R,N,V_associatedSectionIdentifiers) associatedSectionIdentifiers;
@property (T@"_UIDiffableDataSourceSectionControllerHandlers",C,N,V_handlers) handlers;
```

## Instance methods

```
-[_UIDiffableDataSourceSectionController setHandlers:];
-[_UIDiffableDataSourceSectionController handlers];
-[_UIDiffableDataSourceSectionController applySnapshot:toSection:customAnimationsProvider:];
-[_UIDiffableDataSourceSectionController initWithItemRenderers:];
-[_UIDiffableDataSourceSectionController applySnapshot:toSection:animatingDifferences:completion:];
-[_UIDiffableDataSourceSectionController setDataSource:];
-[_UIDiffableDataSourceSectionController configureCell:forItem:];
-[_UIDiffableDataSourceSectionController setDelegate:];
-[_UIDiffableDataSourceSectionController applySnapshot:toSection:viewPropertyAnimator:customAnimationsProvider:];
-[_UIDiffableDataSourceSectionController dataSource];
-[_UIDiffableDataSourceSectionController snapshotForSection:];
-[_UIDiffableDataSourceSectionController delegate];
-[_UIDiffableDataSourceSectionController _expandCollapseAnimationContextForCollectionView:];
-[_UIDiffableDataSourceSectionController _collectionView];
-[_UIDiffableDataSourceSectionController copyWithZone:];
-[_UIDiffableDataSourceSectionController initWithItemRenderers:associatedSectionIdentifiers:];
-[_UIDiffableDataSourceSectionController _queryClientShouldCollapseItem:];
-[_UIDiffableDataSourceSectionController initWithDiffableDataSourceImpl:];
-[_UIDiffableDataSourceSectionController __applySnapshot:toSection:animatingDifferences:viewPropertyAnimator:animationsProvider:isOnDiffableApplyQueue:completion:];
-[_UIDiffableDataSourceSectionController _applySnapshot:toSection:animatingDifferences:viewPropertyAnimator:animationsProvider:isOnDiffableApplyQueue:completion:];
-[_UIDiffableDataSourceSectionController _configureCell:forItem:inSnapshot:];
-[_UIDiffableDataSourceSectionController _configureForDataSource:];
-[_UIDiffableDataSourceSectionController _configureForItemRenderersIfNeeded:];
-[_UIDiffableDataSourceSectionController _extantMutableSnapshotForItem:];
-[_UIDiffableDataSourceSectionController _extantMutableSnapshotForSection:];
-[_UIDiffableDataSourceSectionController _performDisclosureAction:forItem:];
-[_UIDiffableDataSourceSectionController _queryClientShouldExpandItem:];
-[_UIDiffableDataSourceSectionController _queryClientShouldQueryForSnapshotForExpandingParentItem:];
-[_UIDiffableDataSourceSectionController _queryClientSnapshotForExpandingParentItemForItem:currentSectionSnapshot:];
-[_UIDiffableDataSourceSectionController _queryClientWillCollapseItem:];
-[_UIDiffableDataSourceSectionController _queryClientWillExpandItem:];
-[_UIDiffableDataSourceSectionController _sectionIdentifierForItem:];
-[_UIDiffableDataSourceSectionController _shouldPerformCustomCollapseExpandAnimationsForInitialSnapshot:finalSnapshot:];
-[_UIDiffableDataSourceSectionController _snapshotForSectionContainingItem:];
-[_UIDiffableDataSourceSectionController _snapshotHasExpandOrCollapseUpdates:];
-[_UIDiffableDataSourceSectionController _snapshotsMap];
-[_UIDiffableDataSourceSectionController _updatePreparedCellsForExpansionStateWithSnapshot:];
-[_UIDiffableDataSourceSectionController _updateSnapshot:forSectionIdentifier:];
-[_UIDiffableDataSourceSectionController applySnapshot:toSection:animatingDifferences:];
-[_UIDiffableDataSourceSectionController associatedSectionIdentifiers];
-[_UIDiffableDataSourceSectionController initWithDiffableDataSource:];
-[_UIDiffableDataSourceSectionController initWithItemRenderers:associatedSectionIdentifiers:snapshotsMap:dataSource:];
-[_UIDiffableDataSourceSectionController itemRenderers];
-[_UIDiffableDataSourceSectionController snapshotForItem:];
```
