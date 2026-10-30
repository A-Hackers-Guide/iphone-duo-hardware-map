# `MCDBrowsableContentTableViewController`

- Image: [`/System/Library/PrivateFrameworks/MusicCarDisplayUI.framework/MusicCarDisplayUI`](../userland/System__Library__PrivateFrameworks__MusicCarDisplayUI.framework__MusicCarDisplayUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `UITableViewDataSource`, `UITableViewDelegate`, `UIGestureRecognizerDelegate`, `MCDPCContainerDelegate`, `MCDErrorViewDelegate`, `CARSessionObserving`
- 26 instance variables, 14 properties, 59 instance methods, 0 class methods

## Instance variables

```
@"UITableView" _tableView;
@"UIBarButtonItem" _nowPlayingButton;
q _count;
@"NSIndexPath" _selectedNextIndexPath;
@"_UIFilteredDataSource" _dataSource;
@"NSIndexPath" _reselectIndexPath;
@"MPWeakTimer" _loadingTimer;
@"MPWeakTimer" _delayTimer;
@"UIView" _MCD_tableView;
@"NSObject<OS_dispatch_queue>" _serialQueue;
@"CARSessionStatus" _carSessionStatus;
B _limited;
B _hasCarScreen;
B _hasNoBrowsableContent;
B _didPushToNowPlayingAtLaunch;
B _isRootTableViewController;
B _hasTabbedBrowsing;
B _visible;
B _currentlyPlayingApp;
B _pushToNowPlaying;
B _didFinishInitialLoad;
B _didFinishInitialViewAppear;
@"MCDPCContainer" _container;
@"NSIndexPath" _selectedIndexPath;
@"UIView" _placeholderView;
@"UIAlertController" _alertController;
```

## Properties

```
@property (TB,N,GisVisible,V_visible) visible;
@property (T@"NSIndexPath",&,N,V_selectedIndexPath) selectedIndexPath;
@property (T@"UIView",&,N,V_placeholderView) placeholderView;
@property (TB,N,V_currentlyPlayingApp) currentlyPlayingApp;
@property (T@"MPWeakTimer",&,N,V_loadingTimer) loadingTimer;
@property (T@"UIAlertController",&,N,V_alertController) alertController;
@property (TB,N,V_pushToNowPlaying) pushToNowPlaying;
@property (T@"MCDPCContainer",&,N,V_container) container;
@property (TB,N,V_didFinishInitialLoad) didFinishInitialLoad;
@property (TB,N,V_didFinishInitialViewAppear) didFinishInitialViewAppear;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MCDBrowsableContentTableViewController tableView:numberOfRowsInSection:];
-[MCDBrowsableContentTableViewController tableView:cellForRowAtIndexPath:];
-[MCDBrowsableContentTableViewController setVisible:];
-[MCDBrowsableContentTableViewController setPlaceholderView:];
-[MCDBrowsableContentTableViewController viewWillDisappear:];
-[MCDBrowsableContentTableViewController alertController];
-[MCDBrowsableContentTableViewController dealloc];
-[MCDBrowsableContentTableViewController setContainer:];
-[MCDBrowsableContentTableViewController isVisible];
-[MCDBrowsableContentTableViewController viewDidLoad];
-[MCDBrowsableContentTableViewController viewDidLayoutSubviews];
-[MCDBrowsableContentTableViewController initWithNibName:bundle:];
-[MCDBrowsableContentTableViewController initWithContainer:];
-[MCDBrowsableContentTableViewController viewWillAppear:];
-[MCDBrowsableContentTableViewController viewDidAppear:];
-[MCDBrowsableContentTableViewController tableView:didSelectRowAtIndexPath:];
-[MCDBrowsableContentTableViewController description];
-[MCDBrowsableContentTableViewController viewDidDisappear:];
-[MCDBrowsableContentTableViewController preferredFocusEnvironments];
-[MCDBrowsableContentTableViewController traitCollectionDidChange:];
-[MCDBrowsableContentTableViewController _playbackStateChanged:];
-[MCDBrowsableContentTableViewController setAlertController:];
-[MCDBrowsableContentTableViewController contentScrollView];
-[MCDBrowsableContentTableViewController placeholderView];
-[MCDBrowsableContentTableViewController container];
-[MCDBrowsableContentTableViewController selectedIndexPath];
-[MCDBrowsableContentTableViewController setSelectedIndexPath:];
-[MCDBrowsableContentTableViewController tableView:didFocusRowAtIndexPath:];
-[MCDBrowsableContentTableViewController _configureCell:forIndexPath:];
-[MCDBrowsableContentTableViewController _limitedUIChanged:];
-[MCDBrowsableContentTableViewController reloadTable];
-[MCDBrowsableContentTableViewController reloadWithCompletion:];
-[MCDBrowsableContentTableViewController didFinishInitialLoad];
-[MCDBrowsableContentTableViewController setDidFinishInitialLoad:];
-[MCDBrowsableContentTableViewController _nowPlayingButtonTapped:];
-[MCDBrowsableContentTableViewController _appRegisteredForContent:];
-[MCDBrowsableContentTableViewController _clearLoadingActivity];
-[MCDBrowsableContentTableViewController _clearTableViewSelectionAnimated:];
-[MCDBrowsableContentTableViewController _displayErrorAlertController:];
-[MCDBrowsableContentTableViewController _displayLoadingActivity];
-[MCDBrowsableContentTableViewController _nowPlayingDidChange:];
-[MCDBrowsableContentTableViewController _pushToNowPlaying:];
-[MCDBrowsableContentTableViewController _replacePlaceholderViewWithView:];
-[MCDBrowsableContentTableViewController _shouldLimitLists];
-[MCDBrowsableContentTableViewController _showLoadingScreen];
-[MCDBrowsableContentTableViewController _showTimeoutScreen];
-[MCDBrowsableContentTableViewController _updateNowPlayingButtonVisibility];
-[MCDBrowsableContentTableViewController container:didInvalidateIndicies:];
-[MCDBrowsableContentTableViewController containerDidChangeCount:];
-[MCDBrowsableContentTableViewController currentlyPlayingApp];
-[MCDBrowsableContentTableViewController didFinishInitialViewAppear];
-[MCDBrowsableContentTableViewController errorViewDidTapButton:];
-[MCDBrowsableContentTableViewController initWithContainer:tabbedBrowsing:];
-[MCDBrowsableContentTableViewController loadingTimer];
-[MCDBrowsableContentTableViewController pushToNowPlaying];
-[MCDBrowsableContentTableViewController setCurrentlyPlayingApp:];
-[MCDBrowsableContentTableViewController setDidFinishInitialViewAppear:];
-[MCDBrowsableContentTableViewController setLoadingTimer:];
-[MCDBrowsableContentTableViewController setPushToNowPlaying:];
```
