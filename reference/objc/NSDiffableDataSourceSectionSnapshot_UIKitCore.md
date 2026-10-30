# `NSDiffableDataSourceSectionSnapshot`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 3 instance variables, 10 properties, 56 instance methods, 0 class methods

## Instance variables

```
@"_NSDiffableDataSourceSectionSnapshotState" _state;
@"NSMutableArray" _expandedItemsUpdates;
@"NSMutableArray" _collapsedItemsUpdates;
```

## Properties

```
@property (T@"_NSDiffableDataSourceSectionSnapshotState",R,N) _state;
@property (T@"NSArray",R,N) _rootItems;
@property (T@"NSOrderedSet",R,N) _itemsOrderedSet;
@property (T@"NSOrderedSet",R,N) _visibleItemsOrderedSet;
@property (T@"NSIndexSet",R,N) _visibleIndexes;
@property (T@"NSArray",R,N) expandedItemsUpdates;
@property (T@"NSArray",R,N) collapsedItemsUpdates;
@property (T@"NSArray",R,N) items;
@property (T@"NSArray",R,N) rootItems;
@property (T@"NSArray",R,N) visibleItems;
```

## Instance methods

```
-[NSDiffableDataSourceSectionSnapshot containsItem:];
-[NSDiffableDataSourceSectionSnapshot _state];
-[NSDiffableDataSourceSectionSnapshot deleteAllItems];
-[NSDiffableDataSourceSectionSnapshot insertItems:afterItem:];
-[NSDiffableDataSourceSectionSnapshot insertItems:afterItem:insertionMode:];
-[NSDiffableDataSourceSectionSnapshot isVisible:];
-[NSDiffableDataSourceSectionSnapshot _indexesOfChildrenForParent:recursive:];
-[NSDiffableDataSourceSectionSnapshot replaceChildrenOfParentItem:withSnapshot:];
-[NSDiffableDataSourceSectionSnapshot parentOfChild:];
-[NSDiffableDataSourceSectionSnapshot childrenOfParent:recursive:];
-[NSDiffableDataSourceSectionSnapshot _visibleIndexes];
-[NSDiffableDataSourceSectionSnapshot initWithState:];
-[NSDiffableDataSourceSectionSnapshot appendItems:intoParent:];
-[NSDiffableDataSourceSectionSnapshot levelOfItem:];
-[NSDiffableDataSourceSectionSnapshot _itemsOrderedSet];
-[NSDiffableDataSourceSectionSnapshot init];
-[NSDiffableDataSourceSectionSnapshot _rootItems];
-[NSDiffableDataSourceSectionSnapshot levelForItem:];
-[NSDiffableDataSourceSectionSnapshot rootItems];
-[NSDiffableDataSourceSectionSnapshot deleteItems:];
-[NSDiffableDataSourceSectionSnapshot insertItems:beforeItem:];
-[NSDiffableDataSourceSectionSnapshot isExpanded:];
-[NSDiffableDataSourceSectionSnapshot _itemHasChildren:];
-[NSDiffableDataSourceSectionSnapshot collapseItems:];
-[NSDiffableDataSourceSectionSnapshot items];
-[NSDiffableDataSourceSectionSnapshot _itemBeforeItem:];
-[NSDiffableDataSourceSectionSnapshot expandItems:];
-[NSDiffableDataSourceSectionSnapshot childrenOfParent:];
-[NSDiffableDataSourceSectionSnapshot visibleItems];
-[NSDiffableDataSourceSectionSnapshot _prepareForApplyToDataSource];
-[NSDiffableDataSourceSectionSnapshot _visibleItemsOrderedSet];
-[NSDiffableDataSourceSectionSnapshot deleteItems:orphanDisposition:];
-[NSDiffableDataSourceSectionSnapshot visualDescription];
-[NSDiffableDataSourceSectionSnapshot expandedItemsUpdates];
-[NSDiffableDataSourceSectionSnapshot initWithSnapshot:];
-[NSDiffableDataSourceSectionSnapshot childSnapshotOfParent:];
-[NSDiffableDataSourceSectionSnapshot collapsedItemsUpdates];
-[NSDiffableDataSourceSectionSnapshot _indexesOfItems:];
-[NSDiffableDataSourceSectionSnapshot _replaceItem:withItem:];
-[NSDiffableDataSourceSectionSnapshot description];
-[NSDiffableDataSourceSectionSnapshot insertSnapshot:beforeItem:];
-[NSDiffableDataSourceSectionSnapshot _itemAfterItem:];
-[NSDiffableDataSourceSectionSnapshot snapshotOfParentItem:includingParentItem:];
-[NSDiffableDataSourceSectionSnapshot childSnapshotOfParent:includingParent:];
-[NSDiffableDataSourceSectionSnapshot snapshotOfParentItem:];
-[NSDiffableDataSourceSectionSnapshot parentOfChildItem:];
-[NSDiffableDataSourceSectionSnapshot expandedItems];
-[NSDiffableDataSourceSectionSnapshot _indexesOfItems:ignoringItemsNotFound:];
-[NSDiffableDataSourceSectionSnapshot copyWithZone:];
-[NSDiffableDataSourceSectionSnapshot appendItems:];
-[NSDiffableDataSourceSectionSnapshot isEqual:];
-[NSDiffableDataSourceSectionSnapshot appendItems:intoParentItem:];
-[NSDiffableDataSourceSectionSnapshot setChildrenWithSnapshot:forParent:];
-[NSDiffableDataSourceSectionSnapshot indexOfItem:];
-[NSDiffableDataSourceSectionSnapshot snapshotter];
-[NSDiffableDataSourceSectionSnapshot insertSnapshot:afterItem:];
```
