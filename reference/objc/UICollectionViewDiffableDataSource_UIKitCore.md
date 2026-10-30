# `UICollectionViewDiffableDataSource`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIDiffableDataSourceIdentifying`, `UICollectionViewDataSource`
- 2 instance variables, 10 properties, 49 instance methods, 0 class methods

## Instance variables

```
@? _didReorderItemsHandler;
@"__UIDiffableDataSource" _impl;
```

## Properties

```
@property (T@"__UIDiffableDataSource",&,N,V_impl) impl;
@property (T@?,C,N,S_setCanReorderItemHandler:) _canReorderItemHandler;
@property (T@?,C,N,S_setDidReorderItemsHandler:,V_didReorderItemsHandler) _didReorderItemsHandler;
@property (T@?,C,N) supplementaryViewProvider;
@property (T@"UICollectionViewDiffableDataSourceReorderingHandlers",C,N) reorderingHandlers;
@property (T@"UICollectionViewDiffableDataSourceSectionSnapshotHandlers",C,N) sectionSnapshotHandlers;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UICollectionViewDiffableDataSource sectionIdentifierForIndex:];
-[UICollectionViewDiffableDataSource indexForSectionIdentifier:];
-[UICollectionViewDiffableDataSource impl];
-[UICollectionViewDiffableDataSource indexPathForItemIdentifier:];
-[UICollectionViewDiffableDataSource itemIdentifierForIndexPath:];
-[UICollectionViewDiffableDataSource setImpl:];
-[UICollectionViewDiffableDataSource setSectionSnapshotHandlers:];
-[UICollectionViewDiffableDataSource setSupplementaryViewProvider:];
-[UICollectionViewDiffableDataSource collectionView:numberOfItemsInSection:];
-[UICollectionViewDiffableDataSource initWithCollectionView:itemRenderers:rendererIdentifierProvider:];
-[UICollectionViewDiffableDataSource snapshot];
-[UICollectionViewDiffableDataSource collectionView:cellForItemAtIndexPath:];
-[UICollectionViewDiffableDataSource numberOfSectionsInCollectionView:];
-[UICollectionViewDiffableDataSource initWithViewUpdatesSink:];
-[UICollectionViewDiffableDataSource sectionSnapshotHandlers];
-[UICollectionViewDiffableDataSource collectionView];
-[UICollectionViewDiffableDataSource collectionView:canMoveItemAtIndexPath:];
-[UICollectionViewDiffableDataSource validateIdentifiers];
-[UICollectionViewDiffableDataSource applySnapshot:toSection:animatingDifferences:completion:];
-[UICollectionViewDiffableDataSource _performBatchApplyUsingReloadData:];
-[UICollectionViewDiffableDataSource supplementaryViewProvider];
-[UICollectionViewDiffableDataSource applySnapshot:animatingDifferences:completion:];
-[UICollectionViewDiffableDataSource setReorderingHandlers:];
-[UICollectionViewDiffableDataSource _isDiffableDataSource];
-[UICollectionViewDiffableDataSource snapshotForSection:];
-[UICollectionViewDiffableDataSource initWithCollectionView:sectionControllers:rendererIdentifierProvider:];
-[UICollectionViewDiffableDataSource initWithCollectionView:cellProvider:];
-[UICollectionViewDiffableDataSource _registerItemRenderers:rendererIdentifierProvider:];
-[UICollectionViewDiffableDataSource _snapshotForSection:];
-[UICollectionViewDiffableDataSource description];
-[UICollectionViewDiffableDataSource _expandCollapseAnimationContextForCollectionView:];
-[UICollectionViewDiffableDataSource collectionView:viewForSupplementaryElementOfKind:atIndexPath:];
-[UICollectionViewDiffableDataSource reorderingHandlers];
-[UICollectionViewDiffableDataSource collectionView:moveItemAtIndexPath:toIndexPath:];
-[UICollectionViewDiffableDataSource _diffableDataSourceImpl];
-[UICollectionViewDiffableDataSource _applySnapshot:animatingDifferences:completion:];
-[UICollectionViewDiffableDataSource _applySnapshot:toSection:animatingDifferences:completion:];
-[UICollectionViewDiffableDataSource _associatedSectionControllerForItemIdentifier:];
-[UICollectionViewDiffableDataSource _associatedSectionControllerForSectionIdentifier:];
-[UICollectionViewDiffableDataSource _canReorderItemHandler];
-[UICollectionViewDiffableDataSource _didReorderItemsHandler];
-[UICollectionViewDiffableDataSource _setCanReorderItemHandler:];
-[UICollectionViewDiffableDataSource _setDidReorderItemsHandler:];
-[UICollectionViewDiffableDataSource _subclassOverridesMethodWithSelector:];
-[UICollectionViewDiffableDataSource applySnapshot:animatingDifferences:];
-[UICollectionViewDiffableDataSource applySnapshot:toSection:animatingDifferences:];
-[UICollectionViewDiffableDataSource applySnapshotUsingReloadData:];
-[UICollectionViewDiffableDataSource applySnapshotUsingReloadData:completion:];
-[UICollectionViewDiffableDataSource initWithCollectionView:itemRenderer:];
```
