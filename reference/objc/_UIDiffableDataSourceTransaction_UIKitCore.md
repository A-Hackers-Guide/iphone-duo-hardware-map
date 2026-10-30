# `_UIDiffableDataSourceTransaction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 4 properties, 26 instance methods, 2 class methods

## Instance variables

```
@"NSArray" _reorderedItemIdentifiers;
q _source;
@"NSDiffableDataSourceSnapshot" _initialSnapshot;
@"NSDiffableDataSourceSnapshot" _finalSnapshot;
@"NSOrderedCollectionDifference" _difference;
@"NSArray" _sectionTransactions;
```

## Properties

```
@property (T@"NSDiffableDataSourceSnapshot",R,N,V_initialSnapshot) initialSnapshot;
@property (T@"NSDiffableDataSourceSnapshot",R,N,V_finalSnapshot) finalSnapshot;
@property (T@"NSOrderedCollectionDifference",R,N,V_difference) difference;
@property (T@"NSArray",R,N,V_sectionTransactions) sectionTransactions;
```

## Class methods

```
+[_UIDiffableDataSourceTransaction applyTransactionWithInitialSnapshot:finalSnapshot:difference:sectionTransactions:];
+[_UIDiffableDataSourceTransaction reorderingTransactionWithInitialSnapshot:finalSnapshot:difference:sectionTransactions:];
```

## Instance methods

```
-[_UIDiffableDataSourceTransaction finalDataSourceSnapshotter];
-[_UIDiffableDataSourceTransaction initalSectionGlobalItemRangeForSection:];
-[_UIDiffableDataSourceTransaction finalIndexPathForSupplementaryElementOfKind:forInitialIndexPath:];
-[_UIDiffableDataSourceTransaction finalSnapshot];
-[_UIDiffableDataSourceTransaction finalSectionIndexForInitialSectionIndex:];
-[_UIDiffableDataSourceTransaction isReorderingTransaction];
-[_UIDiffableDataSourceTransaction reorderedItemIdentifiers];
-[_UIDiffableDataSourceTransaction finalGlobalIndexForInitialGlobalIndex:];
-[_UIDiffableDataSourceTransaction sectionTransactions];
-[_UIDiffableDataSourceTransaction initialGlobalIndexForFinalGlobalIndex:];
-[_UIDiffableDataSourceTransaction finalSectionGlobalItemRangeForSection:];
-[_UIDiffableDataSourceTransaction initialSectionCount];
-[_UIDiffableDataSourceTransaction initialIndexPathForSupplementaryElementOfKind:forFinalIndexPath:];
-[_UIDiffableDataSourceTransaction initialDataSourceSnapshotter];
-[_UIDiffableDataSourceTransaction finalIndexPathForInitialIndexPath:];
-[_UIDiffableDataSourceTransaction description];
-[_UIDiffableDataSourceTransaction finalSectionCount];
-[_UIDiffableDataSourceTransaction difference];
-[_UIDiffableDataSourceTransaction initialSnapshot];
-[_UIDiffableDataSourceTransaction isEqual:];
-[_UIDiffableDataSourceTransaction isApplyTransaction];
-[_UIDiffableDataSourceTransaction source];
-[_UIDiffableDataSourceTransaction performDiffGeneratingUpdates];
-[_UIDiffableDataSourceTransaction initialIndexPathForFinalIndexPath:];
-[_UIDiffableDataSourceTransaction initWithInitialSnapshot:finalSnapshot:source:reorderedItemIdentifiers:difference:sectionTransactions:];
-[_UIDiffableDataSourceTransaction initialSectionIndexForFinalSectionIndex:];
```
