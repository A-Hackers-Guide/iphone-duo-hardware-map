# `_UIDataSourceUpdateMap`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 7 properties, 45 instance methods, 3 class methods

## Instance variables

```
@"_UIDataSourceSnapshotter" _initialSnapshot;
@"_UIDataSourceSnapshotter" _finalSnapshot;
@"NSArray" _originalUpdateItems;
@"NSArray" _updateItems;
@"NSArray" _reverseUpdateItems;
@"_UIDataSourceBatchUpdateMapHelper" _batchUpdateMapHelper;
```

## Properties

```
@property (T@"_UIDataSourceSnapshotter",&,N,V_initialSnapshot) initialSnapshot;
@property (T@"NSArray",C,N,V_originalUpdateItems) originalUpdateItems;
@property (T@"NSArray",&,N,V_updateItems) updateItems;
@property (T@"NSArray",&,N,V_reverseUpdateItems) reverseUpdateItems;
@property (T@"_UIDataSourceSnapshotter",&,N,V_finalSnapshot) finalSnapshot;
@property (T@"_UIDataSourceBatchUpdateMapHelper",&,N,V_batchUpdateMapHelper) batchUpdateMapHelper;
@property (TB,R,N) isBatchUpdateMap;
```

## Class methods

```
+[_UIDataSourceUpdateMap mapForInitialSnapshot:finalSnapshot:batchUpdateItems:];
+[_UIDataSourceUpdateMap mapForInitialSnapshot:orderedUpdateItems:];
+[_UIDataSourceUpdateMap validatedMapForInitialSnapshot:finalSnapshot:batchUpdateItems:];
```

## Instance methods

```
-[_UIDataSourceUpdateMap updates];
-[_UIDataSourceUpdateMap setInitialSnapshot:];
-[_UIDataSourceUpdateMap finalSnapshot];
-[_UIDataSourceUpdateMap finalSectionIndexForInitialSectionIndex:];
-[_UIDataSourceUpdateMap finalIndexPathForInitialIndexPath:];
-[_UIDataSourceUpdateMap description];
-[_UIDataSourceUpdateMap initialSnapshot];
-[_UIDataSourceUpdateMap initialIndexPathForFinalIndexPath:];
-[_UIDataSourceUpdateMap initialSectionIndexForFinalSectionIndex:];
-[_UIDataSourceUpdateMap setUpdateItems:];
-[_UIDataSourceUpdateMap _computeFinalSnapshotAndReverseUpdateItemsForCollectionViewUpdateItems:];
-[_UIDataSourceUpdateMap _findUpdateForIdentifier:];
-[_UIDataSourceUpdateMap _isSectionOnlyIndexPath:];
-[_UIDataSourceUpdateMap _mapIsSimpleInsertMoveSequence];
-[_UIDataSourceUpdateMap _mapUpdateForCollectionUpdateItem:snapshot:];
-[_UIDataSourceUpdateMap _newGlobalItemMapDescription];
-[_UIDataSourceUpdateMap _newSectionMapDescription];
-[_UIDataSourceUpdateMap _oldGlobalItemMapDescription];
-[_UIDataSourceUpdateMap _oldSectionMapDescription];
-[_UIDataSourceUpdateMap _performAppendingInsertsFixups];
-[_UIDataSourceUpdateMap _rebasedUpdatesForUpdate:];
-[_UIDataSourceUpdateMap _sectionIndexPathForSection:];
-[_UIDataSourceUpdateMap _transformIndexPath:applyingUpdateItem:withSnapshot:];
-[_UIDataSourceUpdateMap _transformSectionIndex:applyingUpdateItem:withSnapshot:];
-[_UIDataSourceUpdateMap _updateMapByRevertingAllUpdatesExceptUpdateWithIdentifier:];
-[_UIDataSourceUpdateMap _updateSnapshot:forUpdateItem:];
-[_UIDataSourceUpdateMap batchUpdateMapHelper];
-[_UIDataSourceUpdateMap finalIndexPathForIndexPath:startingAtUpdateWithIdentifier:];
-[_UIDataSourceUpdateMap finalUpdateForInitialUpdate:];
-[_UIDataSourceUpdateMap initWithInitialSnapshot:finalSnapshot:updateItems:assertForInvalidUpdates:];
-[_UIDataSourceUpdateMap initialIndexPathForIndexPath:beforeUpdateWithIdentifier:];
-[_UIDataSourceUpdateMap initialUpdateForFinalUpdate:];
-[_UIDataSourceUpdateMap initialUpdateForUpdateIdentifier:];
-[_UIDataSourceUpdateMap isBatchUpdateMap];
-[_UIDataSourceUpdateMap originalUpdateItems];
-[_UIDataSourceUpdateMap rebasedMapFromNewBaseMap:];
-[_UIDataSourceUpdateMap reverseUpdateItems];
-[_UIDataSourceUpdateMap setBatchUpdateMapHelper:];
-[_UIDataSourceUpdateMap setFinalSnapshot:];
-[_UIDataSourceUpdateMap setOriginalUpdateItems:];
-[_UIDataSourceUpdateMap setReverseUpdateItems:];
-[_UIDataSourceUpdateMap submapAfterUpdate:];
-[_UIDataSourceUpdateMap submapBeforeUpdate:];
-[_UIDataSourceUpdateMap updateItems];
-[_UIDataSourceUpdateMap updateMapByRevertingUpdateWithIdentifier:];
```
