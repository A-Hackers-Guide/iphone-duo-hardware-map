# `_UIDiffableDataSourceSectionSnapshotRebaser`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 1 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSDiffableDataSourceSnapshot" _initialSnapshot;
@"NSDiffableDataSourceSnapshot" _finalSnapshot;
@"_UIDiffableDataSourceDiffer" _dataSourceDiffer;
@"NSMapTable" _initialSectionSnapshots;
@"NSMapTable" _rebasedSectionSnapshots;
```

## Properties

```
@property (T@"NSMapTable",R,N,V_rebasedSectionSnapshots) rebasedSectionSnapshots;
```

## Instance methods

```
-[_UIDiffableDataSourceSectionSnapshotRebaser computeApplyTransactionIncludingSectionDifferences:];
-[_UIDiffableDataSourceSectionSnapshotRebaser initWithInitialSnapshot:finalSnapshot:initialSectionSnapshots:];
-[_UIDiffableDataSourceSectionSnapshotRebaser rebasedSectionSnapshots];
-[_UIDiffableDataSourceSectionSnapshotRebaser computeReorderingTransaction];
-[_UIDiffableDataSourceSectionSnapshotRebaser _rebaseForInitialSnapshot:finalSnapshot:initialSectionSnapshots:dataSourceDiffer:shouldPerformChildSnapshotMoves:];
-[_UIDiffableDataSourceSectionSnapshotRebaser _transactionIncludingSectionDifferences:source:];
-[_UIDiffableDataSourceSectionSnapshotRebaser _computeSectionTransactionsIncludingSectionDifferences:];
-[_UIDiffableDataSourceSectionSnapshotRebaser initWithInitialSnapshot:finalSnapshot:initialSectionSnapshots:dataSourceDiffer:shouldPerformChildSnapshotMoves:];
-[_UIDiffableDataSourceSectionSnapshotRebaser initWithInitialSnapshot:finalSnapshot:initialSectionSnapshots:dataSourceDiffer:];
```
