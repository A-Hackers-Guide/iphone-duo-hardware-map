# `_UIDiffableDataSourceDiffer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 0 properties, 2 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _updates;
@"_UIDiffableDataSourceState" _beforeDataSourceState;
@"_UIDiffableDataSourceState" _afterDataSourceState;
@"_UIIdentifierDiffer" _itemIdentifierDiffer;
@"_UIIdentifierDiffer" _sectionIdentifierDiffer;
@"NSHashTable" _affectedSectionIdentifiers;
@"NSIndexSet" _deletedSections;
@"NSIndexSet" _insertedSections;
```

## Instance methods

```
-[_UIDiffableDataSourceDiffer description];
-[_UIDiffableDataSourceDiffer _verifyForUpdates:];
```
