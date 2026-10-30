# `UICollectionViewDiffableDataSourceSectionSnapshotHandlers`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 5 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
@? _shouldExpandItemHandler;
@? _willExpandItemHandler;
@? _shouldCollapseItemHandler;
@? _willCollapseItemHandler;
@? _snapshotForExpandingParentItemHandler;
```

## Properties

```
@property (T@?,C,N,V_shouldExpandItemHandler) shouldExpandItemHandler;
@property (T@?,C,N,V_willExpandItemHandler) willExpandItemHandler;
@property (T@?,C,N,V_shouldCollapseItemHandler) shouldCollapseItemHandler;
@property (T@?,C,N,V_willCollapseItemHandler) willCollapseItemHandler;
@property (T@?,C,N,V_snapshotForExpandingParentItemHandler) snapshotForExpandingParentItemHandler;
```

## Instance methods

```
-[UICollectionViewDiffableDataSourceSectionSnapshotHandlers copyWithZone:];
-[UICollectionViewDiffableDataSourceSectionSnapshotHandlers initWithShouldExpandItemHandler:willExpandItemHandler:shouldCollapseItemHandler:willCollapseItemHandler:snapshotForExpandingParentItemHandler:];
-[UICollectionViewDiffableDataSourceSectionSnapshotHandlers setShouldCollapseItemHandler:];
-[UICollectionViewDiffableDataSourceSectionSnapshotHandlers setShouldExpandItemHandler:];
-[UICollectionViewDiffableDataSourceSectionSnapshotHandlers setSnapshotForExpandingParentItemHandler:];
-[UICollectionViewDiffableDataSourceSectionSnapshotHandlers setWillCollapseItemHandler:];
-[UICollectionViewDiffableDataSourceSectionSnapshotHandlers setWillExpandItemHandler:];
-[UICollectionViewDiffableDataSourceSectionSnapshotHandlers shouldCollapseItemHandler];
-[UICollectionViewDiffableDataSourceSectionSnapshotHandlers shouldExpandItemHandler];
-[UICollectionViewDiffableDataSourceSectionSnapshotHandlers snapshotForExpandingParentItemHandler];
-[UICollectionViewDiffableDataSourceSectionSnapshotHandlers willCollapseItemHandler];
-[UICollectionViewDiffableDataSourceSectionSnapshotHandlers willExpandItemHandler];
```
