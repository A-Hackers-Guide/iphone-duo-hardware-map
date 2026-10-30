# `AVAssetDownloadLiveActivity`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 19 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _clientStates;
@"AVActivityProgressClient" _activityClient;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _stateLock;
q _cooldownMS;
```

## Class methods

```
+[AVAssetDownloadLiveActivity sharedInstance];
```

## Instance methods

```
-[AVAssetDownloadLiveActivity dealloc];
-[AVAssetDownloadLiveActivity _initInternal];
-[AVAssetDownloadLiveActivity notifyProgress:];
-[AVAssetDownloadLiveActivity _firePendingFinalizeForBundleID:];
-[AVAssetDownloadLiveActivity _handleActivityCancellation:];
-[AVAssetDownloadLiveActivity _isBundleIDBlocked:];
-[AVAssetDownloadLiveActivity _loadConfiguration];
-[AVAssetDownloadLiveActivity _subtitleForCompleted:failed:];
-[AVAssetDownloadLiveActivity _unsafeCancelPendingFinalizeForClientState:];
-[AVAssetDownloadLiveActivity _unsafeClientStateForDownload:];
-[AVAssetDownloadLiveActivity _unsafeEndActivityForClientState:];
-[AVAssetDownloadLiveActivity _unsafeRouteTerminalForClientState:];
-[AVAssetDownloadLiveActivity _unsafeSchedulePendingFinalizeForClientState:];
-[AVAssetDownloadLiveActivity _unsafeStartActivityForClientState:];
-[AVAssetDownloadLiveActivity _unsafeUpdateActivityTitleAndSubtitleForClientState:];
-[AVAssetDownloadLiveActivity _unsafeUpdateProgressForClientState:];
-[AVAssetDownloadLiveActivity downloadDidEnterRetry:];
-[AVAssetDownloadLiveActivity registerDownload:];
-[AVAssetDownloadLiveActivity unregisterDownload:terminalStatus:error:];
```
