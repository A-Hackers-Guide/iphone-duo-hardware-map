# `_MCDNowPlayingContentManager`

- Image: [`/System/Library/PrivateFrameworks/MusicCarDisplayUI.framework/MusicCarDisplayUI`](../userland/System__Library__PrivateFrameworks__MusicCarDisplayUI.framework__MusicCarDisplayUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MPRequestResponseControllerDelegate`, `UITableViewDelegate`, `UITableViewDataSource`, `CARSessionObserving`, `MCDNowPlayingContentManagerProtocol`, `CPUINowPlayingViewControllerDataSource`, `CPUINowPlayingViewControllerDelegate`
- 25 instance variables, 30 properties, 106 instance methods, 0 class methods

## Instance variables

```
B limitedUI;
B _shouldHideBackButton;
B _shouldShowPlayState;
B _allowsAlbumArt;
# tableCellClass;
@"MPModelSong" currentPlayingSong;
@"MPModelPlaylistEntry" currentPlayingPlaylistEntry;
@"MPModelPlaylist" currentPlayingPlaylist;
@"MPModelRadioStation" currentPlayingRadioStation;
q _videoPlaybackState;
@"NSObject<OS_dispatch_queue>" _videoPlaybackStateQueue;
@"<MCDNowPlayingContentManagerDelegate>" _delegate;
@"MPCPlayerResponse" _lastReceivedResponse;
@"UITableView" _tableView;
@"MPCPlayerResponseItem" _nowPlayingItem;
@"MPRequestResponseController" _requestController;
@"UIImage" _albumArtwork;
@"MPArtworkCatalog" _artworkCatalog;
@"<MCDNowPlayingDataSource>" _dataSource;
@"NSString" _bundleID;
@"CARSessionStatus" _carSessionStatus;
@"UIAlertController" _alertController;
q _playerState;
@"NSMutableDictionary" _artworkCache;
@"MSVTimer" _artworkTimer;
```

## Properties

```
@property (TB,N,V_shouldShowPlayState) shouldShowPlayState;
@property (Tq,N,V_videoPlaybackState) videoPlaybackState;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_videoPlaybackStateQueue) videoPlaybackStateQueue;
@property (T@"<MCDNowPlayingContentManagerDelegate>",W,N,V_delegate) delegate;
@property (T@"MPCPlayerResponse",&,N,V_lastReceivedResponse) lastReceivedResponse;
@property (T@"UITableView",W,N,V_tableView) tableView;
@property (T@"MPCPlayerResponseItem",&,N,V_nowPlayingItem) nowPlayingItem;
@property (T@"MPRequestResponseController",&,N,V_requestController) requestController;
@property (T@"UIImage",&,N,V_albumArtwork) albumArtwork;
@property (T@"MPArtworkCatalog",&,N,V_artworkCatalog) artworkCatalog;
@property (T@"<MCDNowPlayingDataSource>",W,N,V_dataSource) dataSource;
@property (T@"NSString",&,N,V_bundleID) bundleID;
@property (T@"CARSessionStatus",&,N,V_carSessionStatus) carSessionStatus;
@property (T@"UIAlertController",&,N,V_alertController) alertController;
@property (Tq,N,V_playerState) playerState;
@property (T@"MPModelSong",&,N,VcurrentPlayingSong) currentPlayingSong;
@property (T@"MPModelPlaylistEntry",&,N,VcurrentPlayingPlaylistEntry) currentPlayingPlaylistEntry;
@property (T@"MPModelPlaylist",&,N,VcurrentPlayingPlaylist) currentPlayingPlaylist;
@property (T@"MPModelRadioStation",&,N,VcurrentPlayingRadioStation) currentPlayingRadioStation;
@property (T@"NSMutableDictionary",&,N,V_artworkCache) artworkCache;
@property (T@"MSVTimer",&,N,V_artworkTimer) artworkTimer;
@property (TB,N,V_allowsAlbumArt) allowsAlbumArt;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,N,VlimitedUI) limitedUI;
@property (T#,W,N,VtableCellClass) tableCellClass;
@property (T@"NSString",R,C,N) nowPlayingBundleID;
@property (TB,N,V_shouldHideBackButton) shouldHideBackButton;
```

## Instance methods

```
-[_MCDNowPlayingContentManager tableView:canMoveRowAtIndexPath:];
-[_MCDNowPlayingContentManager tableView];
-[_MCDNowPlayingContentManager tableView:numberOfRowsInSection:];
-[_MCDNowPlayingContentManager numberOfSectionsInTableView:];
-[_MCDNowPlayingContentManager tableView:cellForRowAtIndexPath:];
-[_MCDNowPlayingContentManager setArtworkTimer:];
-[_MCDNowPlayingContentManager setBundleID:];
-[_MCDNowPlayingContentManager alertController];
-[_MCDNowPlayingContentManager dealloc];
-[_MCDNowPlayingContentManager _processResponse:error:];
-[_MCDNowPlayingContentManager setDataSource:];
-[_MCDNowPlayingContentManager artworkTimer];
-[_MCDNowPlayingContentManager setPlayerState:];
-[_MCDNowPlayingContentManager setDelegate:];
-[_MCDNowPlayingContentManager setTableView:];
-[_MCDNowPlayingContentManager dataSource];
-[_MCDNowPlayingContentManager artworkCache];
-[_MCDNowPlayingContentManager setCarSessionStatus:];
-[_MCDNowPlayingContentManager carSessionStatus];
-[_MCDNowPlayingContentManager tableView:didSelectRowAtIndexPath:];
-[_MCDNowPlayingContentManager delegate];
-[_MCDNowPlayingContentManager limitedUI];
-[_MCDNowPlayingContentManager setLimitedUI:];
-[_MCDNowPlayingContentManager bundleID];
-[_MCDNowPlayingContentManager sessionDidConnect:];
-[_MCDNowPlayingContentManager setArtworkCache:];
-[_MCDNowPlayingContentManager setAlertController:];
-[_MCDNowPlayingContentManager playerState];
-[_MCDNowPlayingContentManager session:didUpdateConfiguration:];
-[_MCDNowPlayingContentManager tableView:canEditRowAtIndexPath:];
-[_MCDNowPlayingContentManager _limitedUIChanged:];
-[_MCDNowPlayingContentManager artworkCatalog];
-[_MCDNowPlayingContentManager controller:defersResponseReplacement:];
-[_MCDNowPlayingContentManager nowPlayingItem];
-[_MCDNowPlayingContentManager setNowPlayingItem:];
-[_MCDNowPlayingContentManager shouldHideBackButton];
-[_MCDNowPlayingContentManager viewWillDisappear];
-[_MCDNowPlayingContentManager _showPlaceholderArtwork];
-[_MCDNowPlayingContentManager requestController];
-[_MCDNowPlayingContentManager setArtworkCatalog:];
-[_MCDNowPlayingContentManager setRequestController:];
-[_MCDNowPlayingContentManager tableCellClass];
-[_MCDNowPlayingContentManager _performRequest];
-[_MCDNowPlayingContentManager nowPlayingBundleID];
-[_MCDNowPlayingContentManager albumTextForNowPlayingController:];
-[_MCDNowPlayingContentManager artistTextForNowPlayingController:];
-[_MCDNowPlayingContentManager backgroundArtForNowPlayingController:];
-[_MCDNowPlayingContentManager durationSnapshotForNowPlayingViewController:];
-[_MCDNowPlayingContentManager isScrubbingEnabledForNowPlayingViewController:];
-[_MCDNowPlayingContentManager nowPlayingViewController:didMoveScrubberTo:];
-[_MCDNowPlayingContentManager nowPlayingViewControllerCanRepeat:];
-[_MCDNowPlayingContentManager nowPlayingViewControllerCanShowAlbumArt:];
-[_MCDNowPlayingContentManager nowPlayingViewControllerCanShowAlbumLink:];
-[_MCDNowPlayingContentManager nowPlayingViewControllerCanShowChangePlaybackRate:];
-[_MCDNowPlayingContentManager nowPlayingViewControllerCanShowUpNext:];
-[_MCDNowPlayingContentManager nowPlayingViewControllerCanShuffle:];
-[_MCDNowPlayingContentManager nowPlayingViewControllerChangePlaybackRate:];
-[_MCDNowPlayingContentManager nowPlayingViewControllerGetPlaybackRate:];
-[_MCDNowPlayingContentManager nowPlayingViewControllerIsPlaying:];
-[_MCDNowPlayingContentManager nowPlayingViewControllerIsRightHandDrive:];
-[_MCDNowPlayingContentManager nowPlayingViewControllerIsShowingExplicitTrack:];
-[_MCDNowPlayingContentManager nowPlayingViewControllerShouldHideBackButton:];
-[_MCDNowPlayingContentManager nowPlayingViewControllerShouldOverrideRightBarButtons:];
-[_MCDNowPlayingContentManager nowPlayingViewControllerShouldUseMusicExplicitGlyph:];
-[_MCDNowPlayingContentManager nowPlayingViewControllerToggleRepeat:];
-[_MCDNowPlayingContentManager nowPlayingViewControllerToggleShuffle:];
-[_MCDNowPlayingContentManager nowPlayingViewControllerUpNextButtonTapped:];
-[_MCDNowPlayingContentManager placeholderTypeForNowPlayingViewController:];
-[_MCDNowPlayingContentManager progressBarLocalizedDurationStringForNowPlayingViewController:];
-[_MCDNowPlayingContentManager repeatTypeForNowPlayingViewController:];
-[_MCDNowPlayingContentManager setShouldShowPlayState:];
-[_MCDNowPlayingContentManager shouldShowPlayState];
-[_MCDNowPlayingContentManager shuffleTypeForNowPlayingViewController:];
-[_MCDNowPlayingContentManager titleForNowPlayingController:];
-[_MCDNowPlayingContentManager videoPlaybackStateForNowPlayingController:];
-[_MCDNowPlayingContentManager setCurrentPlayingPlaylistEntry:];
-[_MCDNowPlayingContentManager _numberOfItemsInPlaybackQueue];
-[_MCDNowPlayingContentManager _performChangeRequest:];
-[_MCDNowPlayingContentManager _requestResponseItem];
-[_MCDNowPlayingContentManager _sessionAllowsAlbumArt:];
-[_MCDNowPlayingContentManager _setupRequest];
-[_MCDNowPlayingContentManager _shouldShowPlaybackQueueForItemCount:];
-[_MCDNowPlayingContentManager albumArtwork];
-[_MCDNowPlayingContentManager allowsAlbumArt];
-[_MCDNowPlayingContentManager beginRequestObservation];
-[_MCDNowPlayingContentManager currentPlayingPlaylist];
-[_MCDNowPlayingContentManager currentPlayingPlaylistEntry];
-[_MCDNowPlayingContentManager currentPlayingRadioStation];
-[_MCDNowPlayingContentManager currentPlayingSong];
-[_MCDNowPlayingContentManager endRequestObservation];
-[_MCDNowPlayingContentManager initWithDelegate:dataSource:bundleID:];
-[_MCDNowPlayingContentManager lastReceivedResponse];
-[_MCDNowPlayingContentManager modelResponseDidInvalidate:];
-[_MCDNowPlayingContentManager processArtworkForCurrentlyPlayingSong];
-[_MCDNowPlayingContentManager setAlbumArtwork:];
-[_MCDNowPlayingContentManager setAllowsAlbumArt:];
-[_MCDNowPlayingContentManager setCurrentPlayingPlaylist:];
-[_MCDNowPlayingContentManager setCurrentPlayingRadioStation:];
-[_MCDNowPlayingContentManager setCurrentPlayingSong:];
-[_MCDNowPlayingContentManager setLastReceivedResponse:];
-[_MCDNowPlayingContentManager setShouldHideBackButton:];
-[_MCDNowPlayingContentManager setTableCellClass:];
-[_MCDNowPlayingContentManager setVideoPlaybackState:];
-[_MCDNowPlayingContentManager setVideoPlaybackStateQueue:];
-[_MCDNowPlayingContentManager videoPlaybackState];
-[_MCDNowPlayingContentManager videoPlaybackStateQueue];
```
