# `UITableViewDataSource`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UITableViewDataSource`, `UITableViewDelegate`, `NSCoding`
- 1 instance variables, 5 properties, 18 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _sections;
```

## Properties

```
@property (T@"NSArray",C,N,V_sections) sections;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UITableViewDataSource staticDataSourceWithSections:];
```

## Instance methods

```
-[UITableViewDataSource tableView:titleForFooterInSection:];
-[UITableViewDataSource tableView:canMoveRowAtIndexPath:];
-[UITableViewDataSource tableView:heightForFooterInSection:];
-[UITableViewDataSource tableView:numberOfRowsInSection:];
-[UITableViewDataSource numberOfSectionsInTableView:];
-[UITableViewDataSource tableView:viewForFooterInSection:];
-[UITableViewDataSource tableView:editingStyleForRowAtIndexPath:];
-[UITableViewDataSource tableView:cellForRowAtIndexPath:];
-[UITableViewDataSource sections];
-[UITableViewDataSource tableView:titleForHeaderInSection:];
-[UITableViewDataSource tableView:heightForRowAtIndexPath:];
-[UITableViewDataSource encodeWithCoder:];
-[UITableViewDataSource setSections:];
-[UITableViewDataSource initWithCoder:];
-[UITableViewDataSource tableView:viewForHeaderInSection:];
-[UITableViewDataSource tableView:heightForHeaderInSection:];
-[UITableViewDataSource tableView:canEditRowAtIndexPath:];
-[UITableViewDataSource tableView:indentationLevelForRowAtIndexPath:];
```
