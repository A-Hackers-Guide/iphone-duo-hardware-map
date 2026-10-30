# `AVAssetDownloadLiveActivityClientState`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 11 properties, 24 instance methods, 0 class methods

## Instance variables

```
B _activityFailed;
@"NSString" _bundleIdentifier;
@"NSUUID" _activityID;
@"NSProgress" _activityProgress;
@"NSMutableDictionary" _activeDownloads;
@"NSMutableSet" _completedDownloadIDs;
@"NSMutableSet" _failedDownloadIDs;
@"NSString" _lastAssetTitle;
@"NSString" _lastPublishedTitle;
@"NSString" _lastPublishedSubtitle;
@"NSObject<OS_dispatch_source>" _pendingFinalizeTimer;
```

## Properties

```
@property (T@"NSString",C,N,V_bundleIdentifier) bundleIdentifier;
@property (T@"NSUUID",&,N,V_activityID) activityID;
@property (T@"NSProgress",&,N,V_activityProgress) activityProgress;
@property (T@"NSMutableDictionary",&,N,V_activeDownloads) activeDownloads;
@property (T@"NSMutableSet",&,N,V_completedDownloadIDs) completedDownloadIDs;
@property (T@"NSMutableSet",&,N,V_failedDownloadIDs) failedDownloadIDs;
@property (T@"NSString",C,N,V_lastAssetTitle) lastAssetTitle;
@property (T@"NSString",C,N,V_lastPublishedTitle) lastPublishedTitle;
@property (T@"NSString",C,N,V_lastPublishedSubtitle) lastPublishedSubtitle;
@property (T@"NSObject<OS_dispatch_source>",&,N,V_pendingFinalizeTimer) pendingFinalizeTimer;
@property (TB,N,V_activityFailed) activityFailed;
```

## Instance methods

```
-[AVAssetDownloadLiveActivityClientState activityID];
-[AVAssetDownloadLiveActivityClientState dealloc];
-[AVAssetDownloadLiveActivityClientState bundleIdentifier];
-[AVAssetDownloadLiveActivityClientState setBundleIdentifier:];
-[AVAssetDownloadLiveActivityClientState initWithBundleIdentifier:];
-[AVAssetDownloadLiveActivityClientState setActivityID:];
-[AVAssetDownloadLiveActivityClientState activeDownloads];
-[AVAssetDownloadLiveActivityClientState activityFailed];
-[AVAssetDownloadLiveActivityClientState activityProgress];
-[AVAssetDownloadLiveActivityClientState completedDownloadIDs];
-[AVAssetDownloadLiveActivityClientState failedDownloadIDs];
-[AVAssetDownloadLiveActivityClientState lastAssetTitle];
-[AVAssetDownloadLiveActivityClientState lastPublishedSubtitle];
-[AVAssetDownloadLiveActivityClientState lastPublishedTitle];
-[AVAssetDownloadLiveActivityClientState pendingFinalizeTimer];
-[AVAssetDownloadLiveActivityClientState setActiveDownloads:];
-[AVAssetDownloadLiveActivityClientState setActivityFailed:];
-[AVAssetDownloadLiveActivityClientState setActivityProgress:];
-[AVAssetDownloadLiveActivityClientState setCompletedDownloadIDs:];
-[AVAssetDownloadLiveActivityClientState setFailedDownloadIDs:];
-[AVAssetDownloadLiveActivityClientState setLastAssetTitle:];
-[AVAssetDownloadLiveActivityClientState setLastPublishedSubtitle:];
-[AVAssetDownloadLiveActivityClientState setLastPublishedTitle:];
-[AVAssetDownloadLiveActivityClientState setPendingFinalizeTimer:];
```
