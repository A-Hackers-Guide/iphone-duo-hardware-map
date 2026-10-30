# `_UIDiffableDataSource`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 4 properties, 48 instance methods, 0 class methods

## Instance variables

```
@"__UIDiffableDataSource" _dsImpl;
```

## Properties

```
@property (Tq,R,N) numberOfItems;
@property (Tq,R,N) numberOfSections;
@property (T@"NSArray",R,N) sectionIdentifiers;
@property (T@"NSArray",R,N) itemIdentifiers;
```

## Instance methods

```
-[_UIDiffableDataSource numberOfItems];
-[_UIDiffableDataSource moveSectionWithIdentifier:beforeSectionWithIdentifier:];
-[_UIDiffableDataSource reloadSectionsWithIdentifiers:];
-[_UIDiffableDataSource appendSectionWithIdentifier:];
-[_UIDiffableDataSource applySnapshot:];
-[_UIDiffableDataSource appendItemsWithIdentifiers:intoSectionWithIdentifier:];
-[_UIDiffableDataSource itemIdentifiersInSectionWithIdentifier:];
-[_UIDiffableDataSource insertItemsWithIdentifiers:afterItemWithIdentifier:];
-[_UIDiffableDataSource sectionIdentifierForSectionContainingItemIdentifier:];
-[_UIDiffableDataSource insertSectionWithIdentifier:afterSectionWithIdentifier:];
-[_UIDiffableDataSource deleteAllItems];
-[_UIDiffableDataSource indexPathForItemIdentifier:];
-[_UIDiffableDataSource deleteSectionsWithIdentifiers:];
-[_UIDiffableDataSource appendSectionsWithIdentifiers:];
-[_UIDiffableDataSource deleteItemsWithIdentifiers:];
-[_UIDiffableDataSource itemIdentifierForIndexPath:];
-[_UIDiffableDataSource insertItemsWithIdentifiers:beforeItemWithIdentifier:];
-[_UIDiffableDataSource insertSectionsWithIdentifiers:afterSectionWithIdentifier:];
-[_UIDiffableDataSource appendItemsWithIdentifiers:];
-[_UIDiffableDataSource sectionIdentifiers];
-[_UIDiffableDataSource reloadItemsWithIdentifiers:];
-[_UIDiffableDataSource numberOfItemsInSection:];
-[_UIDiffableDataSource insertSectionsWithIdentifiers:beforeSectionWithIdentifier:];
-[_UIDiffableDataSource indexOfItemIdentifier:];
-[_UIDiffableDataSource moveItemWithIdentifier:afterItemWithIdentifier:];
-[_UIDiffableDataSource itemIdentifiers];
-[_UIDiffableDataSource numberOfSections];
-[_UIDiffableDataSource snapshot];
-[_UIDiffableDataSource init];
-[_UIDiffableDataSource initWithViewUpdatesSink:];
-[_UIDiffableDataSource moveSectionWithIdentifier:afterSectionWithIdentifier:];
-[_UIDiffableDataSource initWithTableView:cellProvider:];
-[_UIDiffableDataSource indexOfSectionIdentifier:];
-[_UIDiffableDataSource initWithCollectionView:reuseIdentifierProvider:cellConfigurationHandler:];
-[_UIDiffableDataSource applyDifferencesFromSnapshot:];
-[_UIDiffableDataSource initWithTableView:reuseIdentifierProvider:cellConfigurationHandler:];
-[_UIDiffableDataSource reloadFromSnapshot:];
-[_UIDiffableDataSource initWithCollectionView:cellProvider:];
-[_UIDiffableDataSource reloadFromSnapshot:completion:];
-[_UIDiffableDataSource emptySnapshot];
-[_UIDiffableDataSource insertSectionWithIdentifier:beforeSectionWithIdentifier:];
-[_UIDiffableDataSource applyDifferencesFromSnapshot:completion:];
-[_UIDiffableDataSource moveItemWithIdentifier:beforeItemWithIdentifier:];
-[_UIDiffableDataSource _impl];
-[_UIDiffableDataSource defaultRowAnimation];
-[_UIDiffableDataSource dsImpl];
-[_UIDiffableDataSource initWithDiffableDataSource:];
-[_UIDiffableDataSource setDefaultRowAnimation:];
```
