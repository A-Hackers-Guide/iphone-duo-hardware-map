# `UISearchDisplayController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIScrollViewScrollObserver_Internal`
- 35 instance variables, 23 properties, 113 instance methods, 1 class methods

## Instance variables

```
@"UIViewController" _viewController;
@"UITableView" _tableView;
@"UIView" _dimmingView;
@"UISearchBar" _searchBar;
@"UILabel" _noResultsLabel;
@"NSString" _noResultsMessage;
@"NSString" _resultsTitle;
^{__CFArray=} _containingScrollViews;
d _lastKeyboardAdjustment;
d _lastFooterAdjustment;
@"UIPopoverController" _popoverController;
q _searchResultsTableViewStyle;
@ _navigationControllerBookkeeper;
@"NSArray" _savedSelectedCellsWhenViewWillAppear;
@"UIScrollView" _savedContainingScrollView;
@"UISearchDisplayControllerContainerView" _containerView;
Q _savedSearchBarResizingMask;
@"UINavigationItem" _navigationItem;
{CGPoint="x"d"y"d} _containingScrollViewContentOffset;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _searchFieldInNavigationBarFrame;
@"_UINavigationControllerPalette" _attachedNavigationPalette;
@"UIButton" _animatingAppearanceNavigationButton;
d _animatingAppearanceNavigationSearchBarWidth;
@"UIColor" _dimmingOverlayColor;
@"UIView" _tableViewBackgroundHeaderView;
q _unactivatedBarPosition;
@"_UISearchControllerDidScrollDelegate" _didScrollDelegate;
{?="visible"b1"animating"b1"hidIndexBar"b1"hidNavigationBar"b1"noResultsMessageVisible"b1"noResultsMessageAutoDisplay"b1"navigationBarHidingEnabled"b1"dimTableViewOnEmptySearchString"b1"isRotatingWithPopover"b1"cancelButtonManagementDisabled"b1"allowDisablingNavigationBarHiding"b1"showsResultsForEmptyField"b1"searchBarCanBeHoisted"b1"animatingSearchResultsDisappearance"b1"navigationBarShadowWasHidden"b1"hoistingSearchBar"b1} _searchDisplayControllerFlags;
B _displaysSearchBarInNavigationBar;
@"<UISearchDisplayDelegate>" _delegate;
@"<UITableViewDataSource>" _tableViewDataSource;
@"<UITableViewDelegate>" _tableViewDelegate;
Q _navigationBarSearchFieldSizing;
d __activationGapHeight;
d __additionalNonCollapsingHeightAboveSearchBar;
```

## Properties

```
@property (TB,N) noResultsMessageVisible;
@property (TB,N) automaticallyShowsNoResultsMessage;
@property (T@"NSString",C,N) noResultsMessage;
@property (TB,N,GisNavigationBarHidingEnabled) navigationBarHidingEnabled;
@property (TB,N) dimTableViewOnEmptySearchString;
@property (TB,N,G_isCancelButtonManagementDisabled,S_setCancelButtonManagementDisabled:) cancelButtonManagementDisabled;
@property (TQ,N,V_navigationBarSearchFieldSizing) navigationBarSearchFieldSizing;
@property (Td,N,V__activationGapHeight) _activationGapHeight;
@property (Td,N,V__additionalNonCollapsingHeightAboveSearchBar) _additionalNonCollapsingHeightAboveSearchBar;
@property (T@"<UISearchDisplayDelegate>",N,V_delegate) delegate;
@property (TB,N,GisActive) active;
@property (T@"UISearchBar",R,N,V_searchBar) searchBar;
@property (T@"UIViewController",R,W,N,V_viewController) searchContentsController;
@property (T@"UITableView",R,N,V_tableView) searchResultsTableView;
@property (T@"<UITableViewDataSource>",W,N,V_tableViewDataSource) searchResultsDataSource;
@property (T@"<UITableViewDelegate>",W,N,V_tableViewDelegate) searchResultsDelegate;
@property (T@"NSString",C,N,V_resultsTitle) searchResultsTitle;
@property (TB,N,V_displaysSearchBarInNavigationBar) displaysSearchBarInNavigationBar;
@property (T@"UINavigationItem",R,N) navigationItem;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UISearchDisplayController _uiibSetRequiresSearchDisplayControllerSupport];
```

## Instance methods

```
-[UISearchDisplayController _keyboardWillShow:];
-[UISearchDisplayController searchBarSearchButtonClicked:];
-[UISearchDisplayController _observeScrollViewDidScroll:];
-[UISearchDisplayController searchBar];
-[UISearchDisplayController _keyboardWillHide:];
-[UISearchDisplayController _statusBarHeight];
-[UISearchDisplayController init];
-[UISearchDisplayController dealloc];
-[UISearchDisplayController setActive:];
-[UISearchDisplayController searchBarCancelButtonClicked:];
-[UISearchDisplayController setDelegate:];
-[UISearchDisplayController searchBarTextDidBeginEditing:];
-[UISearchDisplayController windowWillAnimateRotation:];
-[UISearchDisplayController encodeWithCoder:];
-[UISearchDisplayController _containerView];
-[UISearchDisplayController delegate];
-[UISearchDisplayController searchBar:textDidChange:];
-[UISearchDisplayController navigationItem];
-[UISearchDisplayController initWithCoder:];
-[UISearchDisplayController searchBar:selectedScopeButtonIndexDidChange:];
-[UISearchDisplayController isActive];
-[UISearchDisplayController setSearchBar:];
-[UISearchDisplayController _hoistSearchBar];
-[UISearchDisplayController _updateSearchBarMaskIfNecessary];
-[UISearchDisplayController _configureSearchBarForTableView];
-[UISearchDisplayController _setupNoResultsLabelIfNecessary];
-[UISearchDisplayController dimTableViewOnEmptySearchString];
-[UISearchDisplayController _activationGapHeight];
-[UISearchDisplayController _additionalNonCollapsingHeightAboveSearchBar];
-[UISearchDisplayController _adjustTableViewContentInsetsAndOffsetsIgnoringCurrent:];
-[UISearchDisplayController _allowDisablingNavigationBarHiding];
-[UISearchDisplayController _animateNavigationBarSearchBarAppearance:];
-[UISearchDisplayController _areSearchContentsSplitViewMaster];
-[UISearchDisplayController _cleanUpSearchBar];
-[UISearchDisplayController _clearSavedSelectedCellsWeUsedWhenHedgingOurBets];
-[UISearchDisplayController _clearViewController];
-[UISearchDisplayController _configureContainerView];
-[UISearchDisplayController _configureNewSearchBar];
-[UISearchDisplayController _containedInPopover];
-[UISearchDisplayController _containingTableView];
-[UISearchDisplayController _containingViewOfClass:];
-[UISearchDisplayController _createPopoverController];
-[UISearchDisplayController _destroyManagedTableView];
-[UISearchDisplayController _dimmingOverlayColor];
-[UISearchDisplayController _dimmingViewAlpha];
-[UISearchDisplayController _dimmingViewColor];
-[UISearchDisplayController _disableParentScrollViews];
-[UISearchDisplayController _enableParentScrollViews];
-[UISearchDisplayController _hideVisibleRefreshControl];
-[UISearchDisplayController _isCancelButtonManagementDisabled];
-[UISearchDisplayController _isSearchBarInBar];
-[UISearchDisplayController _managedTableViewDidScroll];
-[UISearchDisplayController _noResultsMessageLabel];
-[UISearchDisplayController _popoverClearButtonPressed:];
-[UISearchDisplayController _popoverKeyboardDidHide:];
-[UISearchDisplayController _popoverKeyboardDidShow:];
-[UISearchDisplayController _restoreSelectedCellsInCaseViewDidNotReallyAppear];
-[UISearchDisplayController _saveSelectedRowsInCaseViewDoesNotReallyAppear];
-[UISearchDisplayController _searchBarInNavigationControllerComponent];
-[UISearchDisplayController _searchBarShouldScrollToVisible:];
-[UISearchDisplayController _searchBarSuperviewChanged];
-[UISearchDisplayController _searchBarSuperviewWillChange];
-[UISearchDisplayController _sendDelegateDidBeginDidEndSearch];
-[UISearchDisplayController _setAllowDisablingNavigationBarHiding:];
-[UISearchDisplayController _setCancelButtonManagementDisabled:];
-[UISearchDisplayController _setDimmingOverlayColor:];
-[UISearchDisplayController _setShowsResultsForEmptyField:];
-[UISearchDisplayController _setTableViewVisible:inView:];
-[UISearchDisplayController _shouldAccountForStatusBarHeight];
-[UISearchDisplayController _showsResultsForEmptyField];
-[UISearchDisplayController _tableViewContentInsets];
-[UISearchDisplayController _topShadowView];
-[UISearchDisplayController _updateNavigationPalette];
-[UISearchDisplayController _updateNoSearchResultsMessageVisiblity];
-[UISearchDisplayController _updatePinnedSearchBar];
-[UISearchDisplayController _updateTableHeaderBackgroundViewInTableView:amountScrolledUnder:];
-[UISearchDisplayController _watchContainingTableViewForScrolling:];
-[UISearchDisplayController automaticallyShowsNoResultsMessage];
-[UISearchDisplayController displaysSearchBarInNavigationBar];
-[UISearchDisplayController hidNavigationBar];
-[UISearchDisplayController initWithSearchBar:contentsController:];
-[UISearchDisplayController initWithSearchBar:contentsController:searchResultsTableViewStyle:];
-[UISearchDisplayController isNavigationBarHidingEnabled];
-[UISearchDisplayController navigationBarSearchFieldSizing];
-[UISearchDisplayController navigationControllerDidCancelShowingViewController:];
-[UISearchDisplayController navigationControllerDidShowViewController:];
-[UISearchDisplayController navigationControllerWillShowViewController:];
-[UISearchDisplayController noResultsMessage];
-[UISearchDisplayController noResultsMessageVisible];
-[UISearchDisplayController popoverController:animationCompleted:];
-[UISearchDisplayController popoverControllerShouldDismissPopover:];
-[UISearchDisplayController searchBarResultsListButtonClicked:];
-[UISearchDisplayController searchContentsController];
-[UISearchDisplayController searchResultsDataSource];
-[UISearchDisplayController searchResultsDelegate];
-[UISearchDisplayController searchResultsTableView];
-[UISearchDisplayController searchResultsTitle];
-[UISearchDisplayController setActive:animated:];
-[UISearchDisplayController setAutomaticallyShowsNoResultsMessage:];
-[UISearchDisplayController setDimTableViewOnEmptySearchString:];
-[UISearchDisplayController setDisplaysSearchBarInNavigationBar:];
-[UISearchDisplayController setNavigationBarHidingEnabled:];
-[UISearchDisplayController setNavigationBarSearchFieldSizing:];
-[UISearchDisplayController setNoResultsMessage:];
-[UISearchDisplayController setNoResultsMessageVisible:];
-[UISearchDisplayController setSearchContentsController:];
-[UISearchDisplayController setSearchResultsDataSource:];
-[UISearchDisplayController setSearchResultsDelegate:];
-[UISearchDisplayController setSearchResultsTitle:];
-[UISearchDisplayController set_activationGapHeight:];
-[UISearchDisplayController set_additionalNonCollapsingHeightAboveSearchBar:];
-[UISearchDisplayController showHideAnimationDidFinish];
-[UISearchDisplayController windowDidRotate:];
```
