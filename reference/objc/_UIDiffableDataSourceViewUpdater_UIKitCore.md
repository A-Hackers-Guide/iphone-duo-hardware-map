# `_UIDiffableDataSourceViewUpdater`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UICollectionViewUpdateItemApplying`
- 7 instance variables, 11 properties, 28 instance methods, 0 class methods

## Instance variables

```
B _hasPerformedInitialUpdate;
q _tableViewRowAnimation;
q _sinkKind;
@"<_UICollectionViewUpdateItemApplying>" _updatesSink;
@"UICollectionView" _collectionView;
@"<_UICollectionDataSourceSnapshotTranslating>" _dataSourceSnapshot;
@"UITableView" _tableView;
```

## Properties

```
@property (T@"<_UICollectionViewUpdateItemApplying>",W,N,V_updatesSink) updatesSink;
@property (T@"UICollectionView",W,N,V_collectionView) collectionView;
@property (Tq,N,V_sinkKind) sinkKind;
@property (T@"<_UICollectionDataSourceSnapshotTranslating>",&,N,V_dataSourceSnapshot) dataSourceSnapshot;
@property (TB,N,V_hasPerformedInitialUpdate) hasPerformedInitialUpdate;
@property (T@"UITableView",W,N,V_tableView) tableView;
@property (Tq,N,V_tableViewRowAnimation) tableViewRowAnimation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIDiffableDataSourceViewUpdater tableView];
-[_UIDiffableDataSourceViewUpdater initWithCollectionView:];
-[_UIDiffableDataSourceViewUpdater targetView];
-[_UIDiffableDataSourceViewUpdater tableViewRowAnimation];
-[_UIDiffableDataSourceViewUpdater _performMoveUpdate:onCollectionView:];
-[_UIDiffableDataSourceViewUpdater collectionView];
-[_UIDiffableDataSourceViewUpdater setHasPerformedInitialUpdate:];
-[_UIDiffableDataSourceViewUpdater dataSourceSnapshot];
-[_UIDiffableDataSourceViewUpdater hasPerformedInitialUpdate];
-[_UIDiffableDataSourceViewUpdater setCollectionView:];
-[_UIDiffableDataSourceViewUpdater setTableView:];
-[_UIDiffableDataSourceViewUpdater initWithTableView:];
-[_UIDiffableDataSourceViewUpdater _doesExpectedUpdate:matchActualUpdates:allowingEmptyUpdates:];
-[_UIDiffableDataSourceViewUpdater _performUpdateWithCollectionViewUpdateItems:dataSourceSnapshot:updateHandler:completion:viewPropertyAnimator:customAnimationsProvider:animated:];
-[_UIDiffableDataSourceViewUpdater initWithUpdatesSink:collectionView:tableView:];
-[_UIDiffableDataSourceViewUpdater _willPerformDiff:];
-[_UIDiffableDataSourceViewUpdater setTableViewRowAnimation:];
-[_UIDiffableDataSourceViewUpdater _deleteAllItems];
-[_UIDiffableDataSourceViewUpdater _reloadData];
-[_UIDiffableDataSourceViewUpdater setUpdatesSink:];
-[_UIDiffableDataSourceViewUpdater _performMoveUpdate:onTableView:];
-[_UIDiffableDataSourceViewUpdater _performViewUpdates:];
-[_UIDiffableDataSourceViewUpdater setSinkKind:];
-[_UIDiffableDataSourceViewUpdater setDataSourceSnapshot:];
-[_UIDiffableDataSourceViewUpdater _sectionIndexesToReloadForTableViewCompatibility:];
-[_UIDiffableDataSourceViewUpdater initWithCollectionViewUpdatesSink:];
-[_UIDiffableDataSourceViewUpdater updatesSink];
-[_UIDiffableDataSourceViewUpdater sinkKind];
```
