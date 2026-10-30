# `DSTableWelcomeController`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`](../userland/System__Library__PrivateFrameworks__DigitalSeparationUI.framework__DigitalSeparationUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `OBTableWelcomeController`
- Protocols: `UISearchBarDelegate`, `UISearchResultsUpdating`, `UISearchControllerDelegate`, `UITableViewDelegate`, `UITableViewDataSource`
- 12 instance variables, 16 properties, 56 instance methods, 0 class methods

## Instance variables

```
B _shouldShowSearchBar;
B _isFiltering;
B _isModelEmpty;
B _isShowingNoSharingView;
B _isShowingNoResultsView;
B _isSpinnerActive;
@"OBBoldTrayButton" _boldButton;
@"OBLinkTrayButton" _linkButton;
@"UISearchController" _searchController;
@"UIActivityIndicatorView" _spinner;
@"UIBarButtonItem" _quickExitButton;
@"UITapGestureRecognizer" _tapGesture;
```

## Properties

```
@property (TB,N,V_isSpinnerActive) isSpinnerActive;
@property (T@"UITapGestureRecognizer",&,N,V_tapGesture) tapGesture;
@property (T@"OBBoldTrayButton",&,N,V_boldButton) boldButton;
@property (T@"OBLinkTrayButton",&,N,V_linkButton) linkButton;
@property (T@"UISearchController",&,N,V_searchController) searchController;
@property (TB,N,V_shouldShowSearchBar) shouldShowSearchBar;
@property (TB,N,V_isFiltering) isFiltering;
@property (TB,N,V_isModelEmpty) isModelEmpty;
@property (T@"UIActivityIndicatorView",&,N,V_spinner) spinner;
@property (T@"UIBarButtonItem",&,N,V_quickExitButton) quickExitButton;
@property (TB,N,V_isShowingNoSharingView) isShowingNoSharingView;
@property (TB,N,V_isShowingNoResultsView) isShowingNoResultsView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[DSTableWelcomeController tableView:numberOfRowsInSection:];
-[DSTableWelcomeController tableView:editingStyleForRowAtIndexPath:];
-[DSTableWelcomeController tableView:cellForRowAtIndexPath:];
-[DSTableWelcomeController setSearchController:];
-[DSTableWelcomeController hideKeyboard];
-[DSTableWelcomeController isFiltering];
-[DSTableWelcomeController searchController];
-[DSTableWelcomeController willPresentSearchController:];
-[DSTableWelcomeController viewDidLoad];
-[DSTableWelcomeController viewDidLayoutSubviews];
-[DSTableWelcomeController willDismissSearchController:];
-[DSTableWelcomeController tableView:heightForRowAtIndexPath:];
-[DSTableWelcomeController setBoldButton:];
-[DSTableWelcomeController scrollViewWillBeginDragging:];
-[DSTableWelcomeController setSpinner:];
-[DSTableWelcomeController boldButton];
-[DSTableWelcomeController tapGesture];
-[DSTableWelcomeController setTapGesture:];
-[DSTableWelcomeController tableView:estimatedHeightForRowAtIndexPath:];
-[DSTableWelcomeController spinner];
-[DSTableWelcomeController tableView:viewForHeaderInSection:];
-[DSTableWelcomeController updateSearchResultsForSearchController:];
-[DSTableWelcomeController tableView:didHighlightRowAtIndexPath:];
-[DSTableWelcomeController linkButton];
-[DSTableWelcomeController setupSearchBar];
-[DSTableWelcomeController setupTableView];
-[DSTableWelcomeController hideNoResultsView];
-[DSTableWelcomeController setLinkButton:];
-[DSTableWelcomeController isSpinnerActive];
-[DSTableWelcomeController quickExitButton];
-[DSTableWelcomeController setIsFiltering:];
-[DSTableWelcomeController addBorderedIcon:];
-[DSTableWelcomeController addIcon:withBorder:];
-[DSTableWelcomeController hideButtonsIfSearching];
-[DSTableWelcomeController hideNoSharingView];
-[DSTableWelcomeController initWithTitle:detailText:icon:adoptTableViewScrollView:shouldShowSearchBar:];
-[DSTableWelcomeController initWithTitle:detailText:symbolName:adoptTableViewScrollView:shouldShowSearchBar:];
-[DSTableWelcomeController isKeyboardActive];
-[DSTableWelcomeController isModelEmpty];
-[DSTableWelcomeController isSearchBarEmpty];
-[DSTableWelcomeController isShowingNoResultsView];
-[DSTableWelcomeController isShowingNoSharingView];
-[DSTableWelcomeController presentErrorAlertController:];
-[DSTableWelcomeController presentErrorAlertController:okHandler:];
-[DSTableWelcomeController presentErrorAlertWithTitle:message:continueHandler:tryAgainHandler:];
-[DSTableWelcomeController setIsModelEmpty:];
-[DSTableWelcomeController setIsShowingNoResultsView:];
-[DSTableWelcomeController setIsShowingNoSharingView:];
-[DSTableWelcomeController setIsSpinnerActive:];
-[DSTableWelcomeController setQuickExitButton:];
-[DSTableWelcomeController setShouldShowSearchBar:];
-[DSTableWelcomeController shouldShowSearchBar];
-[DSTableWelcomeController showNoResultsViewWithSearchText:];
-[DSTableWelcomeController showNoSharingViewWithText:image:];
-[DSTableWelcomeController startContentSpinner];
-[DSTableWelcomeController stopContentSpinner];
```
