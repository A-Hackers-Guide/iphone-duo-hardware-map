# `UICollectionViewUpdate`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UICollectionViewUpdateTranslating`
- 21 instance variables, 4 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _updateItems;
@"UICollectionViewData" _oldModel;
@"UICollectionViewData" _newModel;
{CGPoint="x"d"y"d} _oldContentOffset;
{CGPoint="x"d"y"d} _newContentOffset;
@"NSIndexSet" _deletedSections;
@"NSIndexSet" _insertedSections;
@"NSMutableArray" _deletedSupplementaryIndexesSectionArray;
@"NSMutableArray" _insertedSupplementaryIndexesSectionArray;
@"NSMutableDictionary" _deletedSupplementaryTopLevelIndexesDict;
@"NSMutableDictionary" _insertedSupplementaryTopLevelIndexesDict;
@"_UICollectionViewFocusedItemState" _oldFocusedItemState;
@"_UICollectionViewFocusedItemState" _newFocusedItemState;
@"UICollectionView" _collectionView;
@"NSSet" _itemAnchoredAuxiliaryElementKinds;
@"NSSet" _moveItemSourceIndexPaths;
@"NSSet" _moveItemDestinationIndexPaths;
{_UIDataSourceUpdateMaps="oldSectionCount"I"newSectionCount"I"oldGlobalItemCount"I"newGlobalItemCount"I"oldSectionMap"^I"newSectionMap"^I"oldGlobalItemMap"^I"newGlobalItemMap"^I"updatesAreInvalid"B} _updateMaps;
{?="layoutPreparedForUpdates"b1"animated"b1} _flags;
@"NSString" _invalidUpdatesErrorMessage;
@"NSUUID" _identifier;
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
-[UICollectionViewUpdate initalSectionGlobalItemRangeForSection:];
-[UICollectionViewUpdate finalIndexPathForSupplementaryElementOfKind:forInitialIndexPath:];
-[UICollectionViewUpdate dealloc];
-[UICollectionViewUpdate finalSectionIndexForInitialSectionIndex:];
-[UICollectionViewUpdate finalGlobalIndexForInitialGlobalIndex:];
-[UICollectionViewUpdate initialGlobalIndexForFinalGlobalIndex:];
-[UICollectionViewUpdate finalSectionGlobalItemRangeForSection:];
-[UICollectionViewUpdate initialSectionCount];
-[UICollectionViewUpdate _generateUpdateMaps];
-[UICollectionViewUpdate initialIndexPathForSupplementaryElementOfKind:forFinalIndexPath:];
-[UICollectionViewUpdate finalIndexPathForInitialIndexPath:];
-[UICollectionViewUpdate description];
-[UICollectionViewUpdate finalSectionCount];
-[UICollectionViewUpdate initialIndexPathForFinalIndexPath:];
-[UICollectionViewUpdate initialSectionIndexForFinalSectionIndex:];
```
