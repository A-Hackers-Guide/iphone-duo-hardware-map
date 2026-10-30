# `MCDNowPlayingViewController`

- Image: [`/System/Library/PrivateFrameworks/MusicCarDisplayUI.framework/MusicCarDisplayUI`](../userland/System__Library__PrivateFrameworks__MusicCarDisplayUI.framework__MusicCarDisplayUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CPUINowPlayingViewController`
- Protocols: `MCDNowPlayingContentManagerDelegate`
- 15 instance variables, 19 properties, 61 instance methods, 0 class methods

## Instance variables

```
B _showNavigationBar;
B _trackBuffering;
B _handledWillAppear;
B _shouldShowPlaybackQueue;
@"UITableViewController<PlaybackQueueViewControllerProtocol>" _playbackQueueViewController;
@"NSObject<MCDNowPlayingContentManagerProtocol>" _contentManager;
@"MPCPlayerResponse" _playerResponse;
@"UIActivityIndicatorView" _activityIndicator;
@"UIBarButtonItem" _activityIndicatorBarButtonItem;
@"NSString" _appName;
@"MPWeakTimer" _activityTimer;
@"UILabel" _rightTitleLabel;
@"UIBarButtonItem" _rightTitleLabelBarButtonItem;
@"UIBarButtonItem" _queueBarButtonItem;
@"NSArray" _additionalBarButtonItems;
```

## Properties

```
@property (T@"UIActivityIndicatorView",&,N,V_activityIndicator) activityIndicator;
@property (T@"UIBarButtonItem",&,N,V_activityIndicatorBarButtonItem) activityIndicatorBarButtonItem;
@property (TB,N,V_trackBuffering) trackBuffering;
@property (T@"NSString",&,N,V_appName) appName;
@property (T@"MPWeakTimer",&,N,V_activityTimer) activityTimer;
@property (T@"UILabel",&,N,V_rightTitleLabel) rightTitleLabel;
@property (T@"UIBarButtonItem",&,N,V_rightTitleLabelBarButtonItem) rightTitleLabelBarButtonItem;
@property (T@"UIBarButtonItem",&,N,V_queueBarButtonItem) queueBarButtonItem;
@property (T@"NSArray",&,N,V_additionalBarButtonItems) additionalBarButtonItems;
@property (TB,N,V_handledWillAppear) handledWillAppear;
@property (TB,N,V_shouldShowPlaybackQueue) shouldShowPlaybackQueue;
@property (TB,N,V_showNavigationBar) showNavigationBar;
@property (T@"UITableViewController<PlaybackQueueViewControllerProtocol>",&,N,V_playbackQueueViewController) playbackQueueViewController;
@property (T@"NSObject<MCDNowPlayingContentManagerProtocol>",&,N,V_contentManager) contentManager;
@property (T@"MPCPlayerResponse",&,N,V_playerResponse) playerResponse;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MCDNowPlayingViewController appName];
-[MCDNowPlayingViewController viewWillDisappear:];
-[MCDNowPlayingViewController activityIndicator];
-[MCDNowPlayingViewController dealloc];
-[MCDNowPlayingViewController willMoveToParentViewController:];
-[MCDNowPlayingViewController viewDidLoad];
-[MCDNowPlayingViewController viewWillAppear:];
-[MCDNowPlayingViewController viewDidAppear:];
-[MCDNowPlayingViewController viewSafeAreaInsetsDidChange];
-[MCDNowPlayingViewController setAppName:];
-[MCDNowPlayingViewController viewDidDisappear:];
-[MCDNowPlayingViewController updateBarButtonItems];
-[MCDNowPlayingViewController setActivityIndicator:];
-[MCDNowPlayingViewController setShowNavigationBar:];
-[MCDNowPlayingViewController showNavigationBar];
-[MCDNowPlayingViewController upNextButtonTapped:];
-[MCDNowPlayingViewController setRightTitle:];
-[MCDNowPlayingViewController _updateBackButton];
-[MCDNowPlayingViewController _upNextBarButtonItem];
-[MCDNowPlayingViewController rightTitleLabel];
-[MCDNowPlayingViewController setPlaybackQueueViewController:];
-[MCDNowPlayingViewController _adjustRightTitleLabelToFit];
-[MCDNowPlayingViewController _handleWillAppear];
-[MCDNowPlayingViewController _invalidateActivityTimer];
-[MCDNowPlayingViewController _popViewControllerAnimated];
-[MCDNowPlayingViewController _setupActivityTimer];
-[MCDNowPlayingViewController activityIndicatorBarButtonItem];
-[MCDNowPlayingViewController activityTimer];
-[MCDNowPlayingViewController additionalBarButtonItems];
-[MCDNowPlayingViewController contentManager];
-[MCDNowPlayingViewController contentManager:bufferingItem:];
-[MCDNowPlayingViewController contentManager:displayItemIndex:totalItemCount:];
-[MCDNowPlayingViewController contentManager:presentViewController:];
-[MCDNowPlayingViewController contentManager:processResponse:error:];
-[MCDNowPlayingViewController contentManager:pushViewController:];
-[MCDNowPlayingViewController contentManager:sectionName:];
-[MCDNowPlayingViewController contentManager:setAdditionalBarButtonItems:];
-[MCDNowPlayingViewController contentManager:shouldShowPlaybackQueue:];
-[MCDNowPlayingViewController contentManagerCompletedAllPlayback:];
-[MCDNowPlayingViewController contentManagerInitiatedPlaybackFromPlaybackQueue:];
-[MCDNowPlayingViewController contentManagerReloadData:];
-[MCDNowPlayingViewController handledWillAppear];
-[MCDNowPlayingViewController initWithBundleID:appName:];
-[MCDNowPlayingViewController initWithPlayableBundleID:appName:];
-[MCDNowPlayingViewController playbackQueueViewController];
-[MCDNowPlayingViewController playerResponse];
-[MCDNowPlayingViewController queueBarButtonItem];
-[MCDNowPlayingViewController rightTitleLabelBarButtonItem];
-[MCDNowPlayingViewController setActivityIndicatorBarButtonItem:];
-[MCDNowPlayingViewController setActivityTimer:];
-[MCDNowPlayingViewController setAdditionalBarButtonItems:];
-[MCDNowPlayingViewController setContentManager:];
-[MCDNowPlayingViewController setHandledWillAppear:];
-[MCDNowPlayingViewController setPlayerResponse:];
-[MCDNowPlayingViewController setQueueBarButtonItem:];
-[MCDNowPlayingViewController setRightTitleLabel:];
-[MCDNowPlayingViewController setRightTitleLabelBarButtonItem:];
-[MCDNowPlayingViewController setShouldShowPlaybackQueue:];
-[MCDNowPlayingViewController setTrackBuffering:];
-[MCDNowPlayingViewController shouldShowPlaybackQueue];
-[MCDNowPlayingViewController trackBuffering];
```
