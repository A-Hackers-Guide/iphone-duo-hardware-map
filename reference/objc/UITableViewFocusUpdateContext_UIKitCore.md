# `UITableViewFocusUpdateContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIFocusUpdateContext`
- 5 instance variables, 3 properties, 4 instance methods, 1 class methods

## Instance variables

```
B _didSetPreviouslyFocusedIndexPath;
B _didSetNextFocusedIndexPath;
@"NSIndexPath" _previouslyFocusedIndexPath;
@"NSIndexPath" _nextFocusedIndexPath;
@"UITableView" _tableView;
```

## Properties

```
@property (T@"UITableView",R,W,N,V_tableView) tableView;
@property (T@"NSIndexPath",R,N,V_previouslyFocusedIndexPath) previouslyFocusedIndexPath;
@property (T@"NSIndexPath",R,N,V_nextFocusedIndexPath) nextFocusedIndexPath;
```

## Class methods

```
+[UITableViewFocusUpdateContext _contextWithContext:tableView:];
```

## Instance methods

```
-[UITableViewFocusUpdateContext tableView];
-[UITableViewFocusUpdateContext _initWithContext:tableView:];
-[UITableViewFocusUpdateContext nextFocusedIndexPath];
-[UITableViewFocusUpdateContext previouslyFocusedIndexPath];
```
