# `NSDiffableDataSourceTransaction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 31 instance methods, 3 class methods

## Instance variables

```
@"NSDiffableDataSourceSnapshot" _initialSnapshot;
@"NSDiffableDataSourceSnapshot" _finalSnapshot;
@"NSOrderedCollectionDifference" _difference;
@"NSArray" _sectionTransactions;
@"NSArray" _reorderedItemIdentifiers;
q _source;
```

## Properties

```
@property (T@"NSArray",R,N,V_reorderedItemIdentifiers) reorderedItemIdentifiers;
@property (Tq,R,N,V_source) source;
@property (T@"NSDiffableDataSourceSnapshot",R,N,V_initialSnapshot) initialSnapshot;
@property (T@"NSDiffableDataSourceSnapshot",R,N,V_finalSnapshot) finalSnapshot;
@property (T@"NSOrderedCollectionDifference",R,N,V_difference) difference;
@property (T@"NSArray",R,N,V_sectionTransactions) sectionTransactions;
```

## Class methods

```
+[NSDiffableDataSourceTransaction _computeReorderingTransactionWithInitialSnapshot:reorderingUpdate:sectionSnapshotProvider:];
+[NSDiffableDataSourceTransaction applyTransactionWithInitialSnapshot:finalSnapshot:difference:sectionTransactions:];
+[NSDiffableDataSourceTransaction reorderingTransactionWithInitialSnapshot:finalSnapshot:difference:sectionTransactions:];
```

## Instance methods

```
-[NSDiffableDataSourceTransaction finalDataSourceSnapshotter];
-[NSDiffableDataSourceTransaction initalSectionGlobalItemRangeForSection:];
-[NSDiffableDataSourceTransaction finalIndexPathForSupplementaryElementOfKind:forInitialIndexPath:];
-[NSDiffableDataSourceTransaction initWithInitialSnapshot:finalSnapshot:source:difference:finalSectionSnapshots:];
-[NSDiffableDataSourceTransaction _spiCopy];
-[NSDiffableDataSourceTransaction finalSnapshot];
-[NSDiffableDataSourceTransaction finalSectionIndexForInitialSectionIndex:];
-[NSDiffableDataSourceTransaction _containsItemIdentifier:];
-[NSDiffableDataSourceTransaction isReorderingTransaction];
-[NSDiffableDataSourceTransaction reorderedItemIdentifiers];
-[NSDiffableDataSourceTransaction finalGlobalIndexForInitialGlobalIndex:];
-[NSDiffableDataSourceTransaction sectionTransactions];
-[NSDiffableDataSourceTransaction initialGlobalIndexForFinalGlobalIndex:];
-[NSDiffableDataSourceTransaction finalSectionGlobalItemRangeForSection:];
-[NSDiffableDataSourceTransaction initialSectionCount];
-[NSDiffableDataSourceTransaction initWithInitialSnapshot:finalSnapshot:source:difference:reorderedItemIdentifiers:sectionTransactions:];
-[NSDiffableDataSourceTransaction initialIndexPathForSupplementaryElementOfKind:forFinalIndexPath:];
-[NSDiffableDataSourceTransaction transactionWithSectionTransactions:];
-[NSDiffableDataSourceTransaction initialDataSourceSnapshotter];
-[NSDiffableDataSourceTransaction finalIndexPathForInitialIndexPath:];
-[NSDiffableDataSourceTransaction description];
-[NSDiffableDataSourceTransaction finalSectionCount];
-[NSDiffableDataSourceTransaction difference];
-[NSDiffableDataSourceTransaction initialSnapshot];
-[NSDiffableDataSourceTransaction isEqual:];
-[NSDiffableDataSourceTransaction isApplyTransaction];
-[NSDiffableDataSourceTransaction source];
-[NSDiffableDataSourceTransaction performDiffGeneratingUpdates];
-[NSDiffableDataSourceTransaction initialIndexPathForFinalIndexPath:];
-[NSDiffableDataSourceTransaction initWithInitialSnapshot:finalSnapshot:source:reorderedItemIdentifiers:difference:sectionTransactions:];
-[NSDiffableDataSourceTransaction initialSectionIndexForFinalSectionIndex:];
```
