# `MCDPCModel`

- Image: [`/System/Library/PrivateFrameworks/MusicCarDisplayUI.framework/MusicCarDisplayUI`](../userland/System__Library__PrivateFrameworks__MusicCarDisplayUI.framework__MusicCarDisplayUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MCDNowPlayingContentManagerDelegate`
- 16 instance variables, 21 properties, 55 instance methods, 0 class methods

## Instance variables

```
B _currentPlayingApp;
B _didFinishInitialLoad;
I _supportedAPIMask;
@"NSString" _bundleID;
@"MCDPCItem" _rootItem;
@"MCDPlayableContentPlaybackManager" _playableContentPlaybackManager;
@? _playbackCompletion;
@? _containerCompletion;
@"NSIndexPath" _selectedIndexPath;
@"NSMutableDictionary" _items;
@"NSMutableDictionary" _beginLoadingBlocks;
@"MPWeakTimer" _beginLoadingTimeoutTimer;
@"MPWeakTimer" _playbackProgressTimeoutTimer;
@"NSObject<OS_dispatch_queue>" _mediaRemoteNotificationQueue;
@"NSObject<OS_dispatch_queue>" _mediaRemoteItemQueue;
{CGSize="width"d"height"d} _imageSize;
```

## Properties

```
@property (T@"MCDPlayableContentPlaybackManager",&,N,V_playableContentPlaybackManager) playableContentPlaybackManager;
@property (TB,N,GisCurrentPlayingApp,V_currentPlayingApp) currentPlayingApp;
@property (T@?,C,N,V_playbackCompletion) playbackCompletion;
@property (T@?,C,N,V_containerCompletion) containerCompletion;
@property (T@"NSIndexPath",&,N,V_selectedIndexPath) selectedIndexPath;
@property (T@"NSMutableDictionary",&,N,V_items) items;
@property (TB,N,V_didFinishInitialLoad) didFinishInitialLoad;
@property (TI,N,V_supportedAPIMask) supportedAPIMask;
@property (T@"NSMutableDictionary",&,N,V_beginLoadingBlocks) beginLoadingBlocks;
@property (T@"MPWeakTimer",&,N,V_beginLoadingTimeoutTimer) beginLoadingTimeoutTimer;
@property (T@"MPWeakTimer",&,N,V_playbackProgressTimeoutTimer) playbackProgressTimeoutTimer;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_mediaRemoteNotificationQueue) mediaRemoteNotificationQueue;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_mediaRemoteItemQueue) mediaRemoteItemQueue;
@property (T@"NSString",R,C,N,V_bundleID) bundleID;
@property (T@"MCDPCItem",R,N,V_rootItem) rootItem;
@property (T@"NSString",R,N) appTitle;
@property (T{CGSize=dd},N,V_imageSize) imageSize;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MCDPCModel imageSize];
-[MCDPCModel initWithBundleID:];
-[MCDPCModel setItems:];
-[MCDPCModel dealloc];
-[MCDPCModel items];
-[MCDPCModel setImageSize:];
-[MCDPCModel bundleID];
-[MCDPCModel _registerNotifications];
-[MCDPCModel selectedIndexPath];
-[MCDPCModel setSelectedIndexPath:];
-[MCDPCModel rootItem];
-[MCDPCModel didFinishInitialLoad];
-[MCDPCModel setDidFinishInitialLoad:];
-[MCDPCModel appTitle];
-[MCDPCModel getChildrenSupportsPlaybackProgressForIndexPath:withCompletion:];
-[MCDPCModel _browsableContentDidRegisterNotification:];
-[MCDPCModel _contentItemsUpdated:];
-[MCDPCModel _dataSourceInvalidated:];
-[MCDPCModel _errorForNotification:];
-[MCDPCModel _finishBeginLoadingNotification:];
-[MCDPCModel _finishPlaybackNotification:];
-[MCDPCModel _invalidateBeginLoadingTimeoutTimer];
-[MCDPCModel _invalidatePlaybackProgressTimeoutTimer];
-[MCDPCModel _nowPlayingDidChangeNotification:];
-[MCDPCModel _registerForClientContent];
-[MCDPCModel _setupBeginLoadingTimeoutTimerWithCompletion:];
-[MCDPCModel _setupPlaybackProgressTimeoutTimerWithCompletion:];
-[MCDPCModel beginLoadingBlocks];
-[MCDPCModel beginLoadingItemAtIndexPath:completion:];
-[MCDPCModel beginLoadingTimeoutTimer];
-[MCDPCModel containerCompletion];
-[MCDPCModel containerForRoot];
-[MCDPCModel contentManager:itemDidChange:response:];
-[MCDPCModel getChildrenAtIndexPath:inRange:completion:];
-[MCDPCModel getCountOfChildrenAtIndexPath:withCompletion:];
-[MCDPCModel getNowPlayingIdentifiersWithCompletion:];
-[MCDPCModel initiatePlaybackAtIndexPath:completion:];
-[MCDPCModel isCurrentPlayingApp];
-[MCDPCModel itemsFromMRContentItems:];
-[MCDPCModel mediaRemoteItemQueue];
-[MCDPCModel mediaRemoteNotificationQueue];
-[MCDPCModel playableContentPlaybackManager];
-[MCDPCModel playbackCompletion];
-[MCDPCModel playbackProgressTimeoutTimer];
-[MCDPCModel setBeginLoadingBlocks:];
-[MCDPCModel setBeginLoadingTimeoutTimer:];
-[MCDPCModel setContainerCompletion:];
-[MCDPCModel setCurrentPlayingApp:];
-[MCDPCModel setMediaRemoteItemQueue:];
-[MCDPCModel setMediaRemoteNotificationQueue:];
-[MCDPCModel setPlayableContentPlaybackManager:];
-[MCDPCModel setPlaybackCompletion:];
-[MCDPCModel setPlaybackProgressTimeoutTimer:];
-[MCDPCModel setSupportedAPIMask:];
-[MCDPCModel supportedAPIMask];
```
