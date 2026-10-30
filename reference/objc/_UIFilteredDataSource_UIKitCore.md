# `_UIFilteredDataSource`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UITableViewDataSource`
- 5 instance variables, 6 properties, 10 instance methods, 0 class methods

## Instance variables

```
B _limitingWithSections;
q _maxVisibleSection;
q _numberOfVisibleItemsInLastSection;
q _filterType;
@"<UITableViewDataSource>" _tableDataSource;
```

## Properties

```
@property (Tq,N,V_filterType) filterType;
@property (T@"<UITableViewDataSource>",N,V_tableDataSource) tableDataSource;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIFilteredDataSource tableView:numberOfRowsInSection:];
-[_UIFilteredDataSource numberOfSectionsInTableView:];
-[_UIFilteredDataSource tableView:cellForRowAtIndexPath:];
-[_UIFilteredDataSource _filteredNumberOfItemsGivenSection:numberOfItems:];
-[_UIFilteredDataSource filterType];
-[_UIFilteredDataSource forwardingTargetForSelector:];
-[_UIFilteredDataSource tableDataSource];
-[_UIFilteredDataSource respondsToSelector:];
-[_UIFilteredDataSource setFilterType:];
-[_UIFilteredDataSource setTableDataSource:];
```
