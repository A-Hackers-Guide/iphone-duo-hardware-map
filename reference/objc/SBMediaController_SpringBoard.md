# `SBMediaController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 3 properties, 39 instance methods, 4 class methods

## Instance variables

```
@"SBApplicationController" _applicationController;
@"NSDictionary" _nowPlayingInfo;
@"SBApplication" _lastNowPlayingApplication;
i _lastMediaRemoteAppActivityStatus;
B _lastNowPlayingAppIsPlaying;
@"NSDate" _lastActivityDate;
I _seekGeneration;
Q _seekSourceSenderID;
q _seekDirection;
B _seekingActive;
i _nowPlayingProcessPID;
```

## Properties

```
@property (Ti,N,V_nowPlayingProcessPID) nowPlayingProcessPID;
@property (T@"SBApplication",R,W,N) nowPlayingApplication;
@property (T@"NSDate",R,N) lastActivityDate;
```

## Class methods

```
+[SBMediaController sharedInstance];
+[SBMediaController sharedInstanceIfExists];
+[SBMediaController sendResetPlaybackTimeoutCommand];
+[SBMediaController applicationCanBeConsideredNowPlaying:];
```

## Instance methods

```
-[SBMediaController setNowPlayingInfo:];
-[SBMediaController _unregisterForNotifications];
-[SBMediaController isPaused];
-[SBMediaController _registerForNotifications];
-[SBMediaController initWithApplicationController:];
-[SBMediaController dealloc];
-[SBMediaController isPlaying];
-[SBMediaController lastActivityDate];
-[SBMediaController togglePlayPauseForEventSource:];
-[SBMediaController _nowPlayingInfo];
-[SBMediaController _applicationActivityStatusDidChange:];
-[SBMediaController _mediaRemoteNowPlayingApplicationDidChange:];
-[SBMediaController _mediaRemoteNowPlayingApplicationIsPlayingDidChange:];
-[SBMediaController _mediaRemoteNowPlayingInfoDidChange:];
-[SBMediaController _nowPlayingAppDidExit:];
-[SBMediaController _sendMediaCommand:options:];
-[SBMediaController _setNowPlayingApplication:];
-[SBMediaController _updateLastRecentActivityDate];
-[SBMediaController addTrackToWishListForEventSource:];
-[SBMediaController banTrackForEventSource:];
-[SBMediaController beginSeek:eventSource:];
-[SBMediaController changeTrack:eventSource:];
-[SBMediaController endSeek:eventSource:];
-[SBMediaController handleKeyboardUsagePair:down:senderID:eventSource:];
-[SBMediaController hasTrack];
-[SBMediaController isApplicationActivityActive];
-[SBMediaController isFirstTrack];
-[SBMediaController isLastTrack];
-[SBMediaController likeTrackForEventSource:];
-[SBMediaController nowPlayingApplication];
-[SBMediaController nowPlayingProcessPID];
-[SBMediaController pauseForEventSource:];
-[SBMediaController playForEventSource:];
-[SBMediaController playingMediaType];
-[SBMediaController setNowPlayingProcessPID:];
-[SBMediaController setPlaybackSpeed:eventSource:];
-[SBMediaController stopForEventSource:];
-[SBMediaController toggleRepeatForEventSource:];
-[SBMediaController toggleShuffleForEventSource:];
```
