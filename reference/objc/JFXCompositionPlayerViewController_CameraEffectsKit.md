# `JFXCompositionPlayerViewController`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `UIGestureRecognizerDelegate`
- 21 instance variables, 29 properties, 113 instance methods, 1 class methods

## Instance variables

```
B _disableVideoDisplayGestures;
B _isDisplaying;
B _dontRemovePlaceHolderOnDisplay;
B _cachedWasPlaying;
I _parentCode;
i _cachedDuration;
i _cachedCurrentTime;
i _cachedMuted;
@"<JFXCompositionPlayerViewControllerDelegate>" _delegate;
@"<JFXCompositionPlayableElementsDataSource>" _clipsDataSource;
@"NSString" _displayName;
q _videoContentMode;
@"UIView" _videoDisplayOverlayView;
@"JFXCompositionPlayer" _clipsPlayer;
@"UIView" _viewFlashed;
@"UIColor" _restoreToColor;
@"UIView" _placeHolderView;
{CGSize="width"d"height"d} _cachedRenderSizeInPixels;
{CGSize="width"d"height"d} _lastPlayerViewSize;
{CGSize="width"d"height"d} _lastPlayerViewBoundsSize;
{?="value"q"timescale"i"flags"I"epoch"q} _playbackTimeChangedObserverInterval;
```

## Properties

```
@property (T@"UIView",&,N,V_videoDisplayOverlayView) videoDisplayOverlayView;
@property (T@"JFXCompositionPlayer",&,N,V_clipsPlayer) clipsPlayer;
@property (TB,N,V_dontRemovePlaceHolderOnDisplay) dontRemovePlaceHolderOnDisplay;
@property (Ti,N,V_cachedDuration) cachedDuration;
@property (Ti,N,V_cachedCurrentTime) cachedCurrentTime;
@property (Ti,N,V_cachedMuted) cachedMuted;
@property (TB,N,V_cachedWasPlaying) cachedWasPlaying;
@property (T{CGSize=dd},N,V_cachedRenderSizeInPixels) cachedRenderSizeInPixels;
@property (T@"UIView",W,N,V_viewFlashed) viewFlashed;
@property (T@"UIColor",&,N,V_restoreToColor) restoreToColor;
@property (T{CGSize=dd},N,V_lastPlayerViewSize) lastPlayerViewSize;
@property (T{CGSize=dd},N,V_lastPlayerViewBoundsSize) lastPlayerViewBoundsSize;
@property (T@"UIView",&,N,V_placeHolderView) placeHolderView;
@property (T@"<JFXCompositionPlayerViewControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"<JFXCompositionPlayableElementsDataSource>",W,N,V_clipsDataSource) clipsDataSource;
@property (T@"NSString",C,N,V_displayName) displayName;
@property (TI,N,V_parentCode) parentCode;
@property (TB,N,V_disableVideoDisplayGestures) disableVideoDisplayGestures;
@property (T{?=qiIq},R,N) currentCMTime;
@property (Ti,R,N) currentTime;
@property (T{?=qiIq},N,V_playbackTimeChangedObserverInterval) playbackTimeChangedObserverInterval;
@property (TB,N,GisMuted) muted;
@property (Tq,N,V_videoContentMode) videoContentMode;
@property (T{CGSize=dd},R,N) renderSizeInPixels;
@property (TB,R,N,V_isDisplaying) isDisplaying;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[JFXCompositionPlayerViewController compositionPlayerClass];
```

## Instance methods

```
-[JFXCompositionPlayerViewController setMuted:];
-[JFXCompositionPlayerViewController isMuted];
-[JFXCompositionPlayerViewController videoContentMode];
-[JFXCompositionPlayerViewController pause];
-[JFXCompositionPlayerViewController appWillResignActive:];
-[JFXCompositionPlayerViewController play];
-[JFXCompositionPlayerViewController observeValueForKeyPath:ofObject:change:context:];
-[JFXCompositionPlayerViewController init];
-[JFXCompositionPlayerViewController displayName];
-[JFXCompositionPlayerViewController dealloc];
-[JFXCompositionPlayerViewController isPlaying];
-[JFXCompositionPlayerViewController currentTime];
-[JFXCompositionPlayerViewController viewDidLoad];
-[JFXCompositionPlayerViewController setDisplayName:];
-[JFXCompositionPlayerViewController viewDidLayoutSubviews];
-[JFXCompositionPlayerViewController seekToTime:];
-[JFXCompositionPlayerViewController duration];
-[JFXCompositionPlayerViewController setDelegate:];
-[JFXCompositionPlayerViewController viewDidAppear:];
-[JFXCompositionPlayerViewController playWithCompletionHandler:];
-[JFXCompositionPlayerViewController didReceiveMemoryWarning];
-[JFXCompositionPlayerViewController gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[JFXCompositionPlayerViewController delegate];
-[JFXCompositionPlayerViewController sharedInit];
-[JFXCompositionPlayerViewController appDidEnterBackground:];
-[JFXCompositionPlayerViewController setVideoContentMode:];
-[JFXCompositionPlayerViewController viewDidDisappear:];
-[JFXCompositionPlayerViewController initWithCoder:];
-[JFXCompositionPlayerViewController appDidBecomeActive:];
-[JFXCompositionPlayerViewController frameRate];
-[JFXCompositionPlayerViewController isDisplaying];
-[JFXCompositionPlayerViewController placeHolderView];
-[JFXCompositionPlayerViewController setPlaceHolderView:];
-[JFXCompositionPlayerViewController setCachedMuted:];
-[JFXCompositionPlayerViewController setViewFlashed:];
-[JFXCompositionPlayerViewController clipsDataSource];
-[JFXCompositionPlayerViewController setClipsPlayer:];
-[JFXCompositionPlayerViewController setDisableVideoDisplayGestures:];
-[JFXCompositionPlayerViewController addPlaceHolder];
-[JFXCompositionPlayerViewController beginFlash];
-[JFXCompositionPlayerViewController cachedCurrentTime];
-[JFXCompositionPlayerViewController cachedDuration];
-[JFXCompositionPlayerViewController cachedMuted];
-[JFXCompositionPlayerViewController cachedRenderSizeInPixels];
-[JFXCompositionPlayerViewController cachedWasPlaying];
-[JFXCompositionPlayerViewController clipsPlayer];
-[JFXCompositionPlayerViewController contentModeToVideoGravity:];
-[JFXCompositionPlayerViewController convertPointInPlaybackSizeToClipPoint:];
-[JFXCompositionPlayerViewController convertPointInPlaybackSizeToClipPointNormalized:];
-[JFXCompositionPlayerViewController currentCMTime];
-[JFXCompositionPlayerViewController disableVideoDisplayGestures];
-[JFXCompositionPlayerViewController dispatchBlockWhenDone:];
-[JFXCompositionPlayerViewController displayPlaceHolder];
-[JFXCompositionPlayerViewController dontRemovePlaceHolderOnDisplay];
-[JFXCompositionPlayerViewController endFlash];
-[JFXCompositionPlayerViewController installVideoDisplayGestures];
-[JFXCompositionPlayerViewController isReloadClipDataSourceNeeded];
-[JFXCompositionPlayerViewController lastPlayerViewBoundsSize];
-[JFXCompositionPlayerViewController lastPlayerViewSize];
-[JFXCompositionPlayerViewController mediaserverdCrashed];
-[JFXCompositionPlayerViewController normalizedMinimumTouchSize];
-[JFXCompositionPlayerViewController parentCode];
-[JFXCompositionPlayerViewController pauseWithCompletionBlock:];
-[JFXCompositionPlayerViewController placeholderContainerView];
-[JFXCompositionPlayerViewController playbackAreaDoubleTapped:];
-[JFXCompositionPlayerViewController playbackAreaPanned:];
-[JFXCompositionPlayerViewController playbackAreaPinched:];
-[JFXCompositionPlayerViewController playbackAreaRotated:];
-[JFXCompositionPlayerViewController playbackAreaTapped:];
-[JFXCompositionPlayerViewController playbackDidStart:];
-[JFXCompositionPlayerViewController playbackDidStop:currentTime:];
-[JFXCompositionPlayerViewController playbackReadyForDisplayChanged:isReady:setPlaceHolder:];
-[JFXCompositionPlayerViewController playbackTimeChangedObserverInterval];
-[JFXCompositionPlayerViewController playbackTimeDidChange:currentTime:];
-[JFXCompositionPlayerViewController playerBecameReadyForDisplayChanged:setPlaceHolder:];
-[JFXCompositionPlayerViewController playerContainerView];
-[JFXCompositionPlayerViewController playerViewBoundsSize];
-[JFXCompositionPlayerViewController playerViewer];
-[JFXCompositionPlayerViewController playerWillBeDestroyed:];
-[JFXCompositionPlayerViewController preparePlaceHolder];
-[JFXCompositionPlayerViewController prepareVideoDisplayView];
-[JFXCompositionPlayerViewController reloadClipDataSource];
-[JFXCompositionPlayerViewController reloadClipDataSourceIfNeeded];
-[JFXCompositionPlayerViewController reloadClipDataSourceOnBecomingActive];
-[JFXCompositionPlayerViewController removePlaceHolder];
-[JFXCompositionPlayerViewController renderSizeInPixels];
-[JFXCompositionPlayerViewController resetPlaybackTimeChangedObserverInterval];
-[JFXCompositionPlayerViewController restoreToColor];
-[JFXCompositionPlayerViewController setCachedCurrentTime:];
-[JFXCompositionPlayerViewController setCachedDuration:];
-[JFXCompositionPlayerViewController setCachedRenderSizeInPixels:];
-[JFXCompositionPlayerViewController setCachedWasPlaying:];
-[JFXCompositionPlayerViewController setClipsDataSource:];
-[JFXCompositionPlayerViewController setDontRemovePlaceHolderOnDisplay:];
-[JFXCompositionPlayerViewController setLastPlayerViewBoundsSize:];
-[JFXCompositionPlayerViewController setLastPlayerViewSize:];
-[JFXCompositionPlayerViewController setNeedsCompositionUpdate];
-[JFXCompositionPlayerViewController setNeedsCompositionUpdateForClip:];
-[JFXCompositionPlayerViewController setParentCode:];
-[JFXCompositionPlayerViewController setPlaybackTimeChangeNotificationPeriod:];
-[JFXCompositionPlayerViewController setPlaybackTimeChangedObserverInterval:];
-[JFXCompositionPlayerViewController setRestoreToColor:];
-[JFXCompositionPlayerViewController setVideoDisplayOverlayView:];
-[JFXCompositionPlayerViewController shouldHandleMediaServerCrash];
-[JFXCompositionPlayerViewController unloadClipDataSourceSetPlaceHolder:];
-[JFXCompositionPlayerViewController unloadCompositionSetPlaceHolder:];
-[JFXCompositionPlayerViewController updateCachedPlaybackProperties];
-[JFXCompositionPlayerViewController updateDelegatePlayer];
-[JFXCompositionPlayerViewController updateVideoDisplayViewBounds];
-[JFXCompositionPlayerViewController videoDisplayBounds];
-[JFXCompositionPlayerViewController videoDisplayOverlayView];
-[JFXCompositionPlayerViewController viewFlashed];
-[JFXCompositionPlayerViewController viewToFlash];
```
