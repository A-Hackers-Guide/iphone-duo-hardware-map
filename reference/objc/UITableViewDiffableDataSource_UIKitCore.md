# `UITableViewDiffableDataSource`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIDiffableDataSourceIdentifying`, `UITableViewDataSource`
- 1 instance variables, 6 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"__UIDiffableDataSource" _impl;
```

## Properties

```
@property (T@"__UIDiffableDataSource",&,N,V_impl) impl;
@property (Tq,N) defaultRowAnimation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UITableViewDiffableDataSource sectionIdentifierForIndex:];
-[UITableViewDiffableDataSource indexForSectionIdentifier:];
-[UITableViewDiffableDataSource tableView:numberOfRowsInSection:];
-[UITableViewDiffableDataSource impl];
-[UITableViewDiffableDataSource indexPathForItemIdentifier:];
-[UITableViewDiffableDataSource numberOfSectionsInTableView:];
-[UITableViewDiffableDataSource itemIdentifierForIndexPath:];
-[UITableViewDiffableDataSource tableView:cellForRowAtIndexPath:];
-[UITableViewDiffableDataSource setImpl:];
-[UITableViewDiffableDataSource snapshot];
-[UITableViewDiffableDataSource initWithViewUpdatesSink:];
-[UITableViewDiffableDataSource validateIdentifiers];
-[UITableViewDiffableDataSource initWithTableView:cellProvider:];
-[UITableViewDiffableDataSource applySnapshot:animatingDifferences:completion:];
-[UITableViewDiffableDataSource _isDiffableDataSource];
-[UITableViewDiffableDataSource description];
-[UITableViewDiffableDataSource _diffableDataSourceImpl];
-[UITableViewDiffableDataSource _applySnapshot:animatingDifferences:completion:];
-[UITableViewDiffableDataSource _subclassOverridesMethodWithSelector:];
-[UITableViewDiffableDataSource applySnapshot:animatingDifferences:];
-[UITableViewDiffableDataSource applySnapshotUsingReloadData:];
-[UITableViewDiffableDataSource applySnapshotUsingReloadData:completion:];
-[UITableViewDiffableDataSource defaultRowAnimation];
-[UITableViewDiffableDataSource setDefaultRowAnimation:];
```
