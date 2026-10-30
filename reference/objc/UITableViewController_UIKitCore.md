# `UITableViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `_UIKeyboardAutoRespondingScrollViewController`, `UITableViewFocusDelegateLegacy`, `UIViewControllerPreviewingDelegate`, `UIViewControllerPreviewingDelegate_Deprecated`, `UITableViewDelegate`, `UITableViewDataSource`
- 6 instance variables, 9 properties, 52 instance methods, 0 class methods

## Instance variables

```
q _tableViewStyle;
@"UIAutoRespondingScrollViewControllerKeyboardSupport" _keyboardSupport;
@"UITableViewDataSource" _staticDataSource;
{?="clearsSelectionOnViewWillAppear"b1"insetsApplied"b1"adjustingInsets"b1"registeredForCarScreenNotification"b1} _tableViewControllerFlags;
@"_UIFilteredDataSource" _filteredDataSource;
q _filteredDataType;
```

## Properties

```
@property (T@"UITableViewDataSource",&,N,G_staticDataSource,S_setStaticDataSource:) staticDataSource;
@property (T@"UITableView",&,N) tableView;
@property (TB,N) clearsSelectionOnViewWillAppear;
@property (T@"UIRefreshControl",&,N) refreshControl;
@property (T@"UIScrollView<_UIKeyboardAutoRespondingScrollView>",R,&,N,G_scrollView) scrollView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UITableViewController tableView:titleForFooterInSection:];
-[UITableViewController tableView];
-[UITableViewController tableView:heightForFooterInSection:];
-[UITableViewController tableView:numberOfRowsInSection:];
-[UITableViewController _scrollView];
-[UITableViewController numberOfSectionsInTableView:];
-[UITableViewController tableView:viewForFooterInSection:];
-[UITableViewController tableView:didEndEditingRowAtIndexPath:];
-[UITableViewController tableView:cellForRowAtIndexPath:];
-[UITableViewController init];
-[UITableViewController viewWillDisappear:];
-[UITableViewController dealloc];
-[UITableViewController tableView:titleForHeaderInSection:];
-[UITableViewController setEditing:animated:];
-[UITableViewController initWithStyle:];
-[UITableViewController initWithNibName:bundle:];
-[UITableViewController viewWillAppear:];
-[UITableViewController tableView:heightForRowAtIndexPath:];
-[UITableViewController setTableView:];
-[UITableViewController viewDidAppear:];
-[UITableViewController loadView];
-[UITableViewController encodeWithCoder:];
-[UITableViewController initWithCoder:];
-[UITableViewController setRefreshControl:];
-[UITableViewController respondsToSelector:];
-[UITableViewController willPresentPreviewViewController:forLocation:inSourceView:];
-[UITableViewController tableView:viewForHeaderInSection:];
-[UITableViewController tableView:heightForHeaderInSection:];
-[UITableViewController _applyDefaultDataSourceToTable:];
-[UITableViewController clearsSelectionOnViewWillAppear];
-[UITableViewController _existingTableView];
-[UITableViewController _filteredDataType];
-[UITableViewController _limitedUIDidChange];
-[UITableViewController _refreshFilteredDataSourceFilterTypeForScreen:];
-[UITableViewController _resolvedDataSourceFilterTypeForScreen:];
-[UITableViewController _setFilteredDataType:];
-[UITableViewController _setStaticDataSource:];
-[UITableViewController _shouldRespondToPreviewingMethods];
-[UITableViewController _staticDataSource];
-[UITableViewController _viewControllerWasSelected];
-[UITableViewController _willChangeToIdiom:onScreen:];
-[UITableViewController previewViewControllerForLocation:inSourceView:];
-[UITableViewController previewViewControllerForRowAtIndexPath:];
-[UITableViewController previewingContext:commitViewController:];
-[UITableViewController previewingContext:viewControllerForLocation:];
-[UITableViewController refreshControl];
-[UITableViewController setClearsSelectionOnViewWillAppear:];
-[UITableViewController tableView:didBeginMultipleSelectionInteractionAtIndexPath:];
-[UITableViewController tableView:indentationLevelForRowAtIndexPath:];
-[UITableViewController tableView:willBeginEditingRowAtIndexPath:];
-[UITableViewController willPresentPreviewViewController:forPosition:inSourceView:];
-[UITableViewController willPresentPreviewViewController:forRowAtIndexPath:];
```
