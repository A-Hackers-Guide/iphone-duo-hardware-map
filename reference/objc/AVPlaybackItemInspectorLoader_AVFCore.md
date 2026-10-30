# `AVPlaybackItemInspectorLoader`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVAssetMakeReadyForInspectionLoader`
- 5 instance variables, 1 properties, 18 instance methods, 0 class methods

## Instance variables

```
^{OpaqueFigPlaybackItem=} _playbackItem;
@"NSArray" _trackIDs;
B _shouldCacheDuration;
{?="value"q"timescale"i"flags"I"epoch"q} _cachedDuration;
@"NSObject<OS_dispatch_queue>" _notificationProcessingQueue;
```

## Properties

```
@property (T^{OpaqueFigPlaybackItem=},R,N,G_playbackItem) playbackItem;
```

## Instance methods

```
-[AVPlaybackItemInspectorLoader dealloc];
-[AVPlaybackItemInspectorLoader _classForTrackInspectors];
-[AVPlaybackItemInspectorLoader duration];
-[AVPlaybackItemInspectorLoader hash];
-[AVPlaybackItemInspectorLoader assetInspector];
-[AVPlaybackItemInspectorLoader isEqual:];
-[AVPlaybackItemInspectorLoader cancelLoading];
-[AVPlaybackItemInspectorLoader _playbackItemPropertiesForKeys:];
-[AVPlaybackItemInspectorLoader _addFigObjectNotifications];
-[AVPlaybackItemInspectorLoader _copyFormatReaderFromFigObjectWithFigErrorCode:];
-[AVPlaybackItemInspectorLoader _dictionaryOfSpecialGettersForKeyValueStatus];
-[AVPlaybackItemInspectorLoader _handlePlaybackItemNotification:notificationPayload:];
-[AVPlaybackItemInspectorLoader _inspectionRequiresAFormatReader];
-[AVPlaybackItemInspectorLoader _loadValuesUsingDefaultLoadingMethodWhileMutexLockedForKeys:];
-[AVPlaybackItemInspectorLoader _playbackItem];
-[AVPlaybackItemInspectorLoader _processItemReadyForInspection:figErrorCode:];
-[AVPlaybackItemInspectorLoader _removeFigObjectNotifications];
-[AVPlaybackItemInspectorLoader initWithURL:playbackItem:trackIDs:dynamicBehavior:];
```
