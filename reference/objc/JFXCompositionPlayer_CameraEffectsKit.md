# `JFXCompositionPlayer`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 17 instance variables, 20 properties, 92 instance methods, 1 class methods

## Instance variables

```
B _wasAudioMuted;
B _wasPlaying;
B _restoringPlayerStateAfterCompositionUpdate;
I _parentCode;
@"NSString" _displayName;
@"<JFXCompositionPlayerDelegate>" _playbackDelegate;
@"NSObject<JFXAVPlayerViewer>" _playerView;
@"<JFXCompositionPlayableElementsDataSource>" _clipsDataSource;
@"JFXComposition" _composition;
@"AVPlayer" _player;
@ _playerProVideoPeriodicObserver;
@ _playerPlaybackTimePeriodicObserver;
@"JFXCompositionPlayerRequest" _pendingRequest;
@"NSMutableArray" _requestQueue;
{?="value"q"timescale"i"flags"I"epoch"q} _playbackTimeChangedObserverInterval;
{?="value"q"timescale"i"flags"I"epoch"q} _wasCurrentTime;
{?="value"q"timescale"i"flags"I"epoch"q} _cachedCurrentTimeForCompositionUpdate;
```

## Properties

```
@property (T@"<JFXCompositionPlayableElementsDataSource>",&,N,V_clipsDataSource) clipsDataSource;
@property (T@"JFXComposition",&,N,V_composition) composition;
@property (T@"AVPlayer",&,N,V_player) player;
@property (T@,&,N,V_playerProVideoPeriodicObserver) playerProVideoPeriodicObserver;
@property (T@,&,N,V_playerPlaybackTimePeriodicObserver) playerPlaybackTimePeriodicObserver;
@property (T@"JFXCompositionPlayerRequest",&,N,V_pendingRequest) pendingRequest;
@property (T@"NSMutableArray",&,N,V_requestQueue) requestQueue;
@property (T{?=qiIq},N,V_wasCurrentTime) wasCurrentTime;
@property (T{?=qiIq},N,V_cachedCurrentTimeForCompositionUpdate) cachedCurrentTimeForCompositionUpdate;
@property (TB,N,V_wasAudioMuted) wasAudioMuted;
@property (TB,N,V_wasPlaying) wasPlaying;
@property (TB,N,V_restoringPlayerStateAfterCompositionUpdate) restoringPlayerStateAfterCompositionUpdate;
@property (T@"NSString",C,N,V_displayName) displayName;
@property (TI,N,V_parentCode) parentCode;
@property (T@"<JFXCompositionPlayerDelegate>",W,N,V_playbackDelegate) playbackDelegate;
@property (T@"NSObject<JFXAVPlayerViewer>",R,N,V_playerView) playerView;
@property (T{CGSize=dd},R,N) renderSize;
@property (T{?=qiIq},N,V_playbackTimeChangedObserverInterval) playbackTimeChangedObserverInterval;
@property (Ti,R,N) currentTime;
@property (T{?=qiIq},R,N) currentCMTime;
```

## Class methods

```
+[JFXCompositionPlayer compositionClass];
```

## Instance methods

```
-[JFXCompositionPlayer setComposition:];
-[JFXCompositionPlayer renderSize];
-[JFXCompositionPlayer requestQueue];
-[JFXCompositionPlayer player];
-[JFXCompositionPlayer setPlaybackDelegate:];
-[JFXCompositionPlayer playbackDelegate];
-[JFXCompositionPlayer play:];
-[JFXCompositionPlayer observeValueForKeyPath:ofObject:change:context:];
-[JFXCompositionPlayer isAudioMuted];
-[JFXCompositionPlayer displayName];
-[JFXCompositionPlayer dealloc];
-[JFXCompositionPlayer isPlaying];
-[JFXCompositionPlayer currentTime];
-[JFXCompositionPlayer setDisplayName:];
-[JFXCompositionPlayer pause:];
-[JFXCompositionPlayer composition];
-[JFXCompositionPlayer setPlayer:];
-[JFXCompositionPlayer duration];
-[JFXCompositionPlayer updateComposition:];
-[JFXCompositionPlayer enqueueRequest:];
-[JFXCompositionPlayer setRequestQueue:];
-[JFXCompositionPlayer playerView];
-[JFXCompositionPlayer pendingRequest];
-[JFXCompositionPlayer setPendingRequest:];
-[JFXCompositionPlayer destroyPlayer];
-[JFXCompositionPlayer removeAllRequests];
-[JFXCompositionPlayer JFX_clipDataSourceHasClip:];
-[JFXCompositionPlayer appendRequests:];
-[JFXCompositionPlayer handleChangeAudioMutedCompleted];
-[JFXCompositionPlayer clipsDataSource];
-[JFXCompositionPlayer doPause];
-[JFXCompositionPlayer isRequestOfTypePendingOrQueued:];
-[JFXCompositionPlayer removeCompositorCompletionBlock];
-[JFXCompositionPlayer cachedCurrentTimeForCompositionUpdate];
-[JFXCompositionPlayer cancelQueuedCompositionUpdateRequestFromClip:];
-[JFXCompositionPlayer cancelQueuedRequestOfType:];
-[JFXCompositionPlayer checkPendingRequestForTimeOut];
-[JFXCompositionPlayer clearQueuedRequests];
-[JFXCompositionPlayer completePendingRequest:wasCancelled:error:];
-[JFXCompositionPlayer completeRequest:success:wasCancelled:error:];
-[JFXCompositionPlayer configureCompositorCompletionBlock];
-[JFXCompositionPlayer createPlayer];
-[JFXCompositionPlayer currentCMTime];
-[JFXCompositionPlayer dispatchBlockWhenDone:];
-[JFXCompositionPlayer doClipCompositionUpdate:];
-[JFXCompositionPlayer doMuteAudio:];
-[JFXCompositionPlayer doPlay];
-[JFXCompositionPlayer doUpdateComposition];
-[JFXCompositionPlayer executeNextRequest];
-[JFXCompositionPlayer executeRequestCompletionBlock:success:wasCancelled:error:];
-[JFXCompositionPlayer firstQueuedRequestOfType:];
-[JFXCompositionPlayer handleClipCompositionUpdateTimedOut];
-[JFXCompositionPlayer handleCompositionRefreshCompleted:];
-[JFXCompositionPlayer handlePlaybackBegan];
-[JFXCompositionPlayer handlePlaybackPaused];
-[JFXCompositionPlayer handleReadyForDisplay:];
-[JFXCompositionPlayer handleSeekCompleted:];
-[JFXCompositionPlayer handleUpdateCompositionCompleted:wasCancelled:error:];
-[JFXCompositionPlayer handleUpdateCompositionForClipCompleted:];
-[JFXCompositionPlayer initWithClipsDataSource:seekPosition:audioMuted:];
-[JFXCompositionPlayer isRequestOfTypeQueued:];
-[JFXCompositionPlayer notifyPlayerViewSizeChanged];
-[JFXCompositionPlayer parentCode];
-[JFXCompositionPlayer playbackTimeChangedObserverInterval];
-[JFXCompositionPlayer playerPlaybackTimePeriodicObserver];
-[JFXCompositionPlayer playerProVideoPeriodicObserver];
-[JFXCompositionPlayer removeRequestOfType:];
-[JFXCompositionPlayer requestWithBlock:ofType:completion:];
-[JFXCompositionPlayer resetPlaybackTimeChangedObserverInterval];
-[JFXCompositionPlayer restoringPlayerStateAfterCompositionUpdate];
-[JFXCompositionPlayer seek:cancelQueuedRequest:tolerance:completion:];
-[JFXCompositionPlayer seek:tolerance:completion:];
-[JFXCompositionPlayer setAudioMuted:completionBlock:];
-[JFXCompositionPlayer setCachedCurrentTimeForCompositionUpdate:];
-[JFXCompositionPlayer setClipsDataSource:];
-[JFXCompositionPlayer setParentCode:];
-[JFXCompositionPlayer setPlaybackTimeChangedObserverInterval:];
-[JFXCompositionPlayer setPlayerPlaybackTimePeriodicObserver:];
-[JFXCompositionPlayer setPlayerProVideoPeriodicObserver:];
-[JFXCompositionPlayer setPlayerView:completionBlock:];
-[JFXCompositionPlayer setRestoringPlayerStateAfterCompositionUpdate:];
-[JFXCompositionPlayer setWasAudioMuted:];
-[JFXCompositionPlayer setWasCurrentTime:];
-[JFXCompositionPlayer setWasPlaying:];
-[JFXCompositionPlayer setupPlaybackTimeChangedObserver];
-[JFXCompositionPlayer teardownSetPlaceHolder:];
-[JFXCompositionPlayer throttleRequestWithCompletionBlock:ofType:];
-[JFXCompositionPlayer updateCompositionForClip:completion:];
-[JFXCompositionPlayer warnTooManyLiveCompositors:];
-[JFXCompositionPlayer wasAudioMuted];
-[JFXCompositionPlayer wasCurrentTime];
-[JFXCompositionPlayer wasPlaying];
```
