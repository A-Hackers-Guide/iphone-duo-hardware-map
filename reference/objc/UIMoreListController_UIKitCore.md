# `UIMoreListController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `UITableViewDelegate`, `UITableViewDataSource`
- 8 instance variables, 7 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"UITableView" _table;
B _allowsCustomizing;
B _disableCustomizing;
B _hideNavigationBar;
@"NSArray" _moreViewControllers;
@"UIMoreListCellLayoutManager" _layoutManager;
@"UIBarButtonItem" _moreEditButtonItem;
B _moreViewControllersChanged;
```

## Properties

```
@property (T@"NSArray",&,N) moreViewControllers;
@property (TB,N) allowsCustomizing;
@property (TB,N) moreViewControllersChanged;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIMoreListController tableView:numberOfRowsInSection:];
-[UIMoreListController numberOfSectionsInTableView:];
-[UIMoreListController decodeRestorableStateWithCoder:];
-[UIMoreListController tableView:cellForRowAtIndexPath:];
-[UIMoreListController encodeRestorableStateWithCoder:];
-[UIMoreListController init];
-[UIMoreListController table];
-[UIMoreListController tableView:willDisplayCell:forRowAtIndexPath:];
-[UIMoreListController viewWillAppear:];
-[UIMoreListController loadView];
-[UIMoreListController tableView:didSelectRowAtIndexPath:];
-[UIMoreListController tabBarItem];
-[UIMoreListController _isSupportedInterfaceOrientation:];
-[UIMoreListController _layoutCells];
-[UIMoreListController _targetNavigationController];
-[UIMoreListController _updateEditButton];
-[UIMoreListController _viewControllerWasSelected];
-[UIMoreListController _willChangeToIdiom:onScreen:];
-[UIMoreListController allowsCustomizing];
-[UIMoreListController moreViewControllers];
-[UIMoreListController moreViewControllersChanged];
-[UIMoreListController setAllowsCustomizing:];
-[UIMoreListController setMoreViewControllers:];
-[UIMoreListController setMoreViewControllersChanged:];
```
