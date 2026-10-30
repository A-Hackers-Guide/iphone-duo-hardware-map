# `AVAssetDownloadSession`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 17 properties, 67 instance methods, 5 class methods

## Instance variables

```
@"AVAssetDownloadSessionInternal" _internal;
```

## Properties

```
@property (Tq,R,N) status;
@property (T@"NSError",R,N) error;
@property (T@"NSURL",R,N) URL;
@property (T@"NSURL",R,N) destinationURL;
@property (Tq,R,N) priority;
@property (TQ,R,N) fileSize;
@property (TQ,R,N) availableFileSize;
@property (TQ,R,N) countOfBytesReceived;
@property (TQ,R,N) downloadToken;
@property (T@"NSArray",R,N) loadedTimeRanges;
@property (T@"AVMediaSelection",R,N) resolvedMediaSelection;
@property (T@"NSProgress",R,N) downloadProgress;
@property (T@"NSString",R,N) assetTitle;
@property (T@"NSString",R,N) clientBundleIdentifier;
@property (TB,R,N) isDiscretionary;
@property (TB,R,N) isRetryAttempt;
@property (TB,R,N) isLiveActivityEnabled;
```

## Class methods

```
+[AVAssetDownloadSession assetDownloadSessionWithAsset:mediaSelections:destinationURL:options:];
+[AVAssetDownloadSession registerDownloadLocation:forURLAsset:];
+[AVAssetDownloadSession assetDownloadSessionWithAsset:destinationURL:options:];
+[AVAssetDownloadSession assetDownloadSessionWithDownloadToken:];
+[AVAssetDownloadSession assetDownloadSessionWithURL:destinationURL:options:];
```

## Instance methods

```
-[AVAssetDownloadSession setDelegate:queue:];
-[AVAssetDownloadSession pause];
-[AVAssetDownloadSession priority];
-[AVAssetDownloadSession downloadProgress];
-[AVAssetDownloadSession init];
-[AVAssetDownloadSession stop];
-[AVAssetDownloadSession countOfBytesReceived];
-[AVAssetDownloadSession dealloc];
-[AVAssetDownloadSession start];
-[AVAssetDownloadSession isDiscretionary];
-[AVAssetDownloadSession status];
-[AVAssetDownloadSession destinationURL];
-[AVAssetDownloadSession loadedTimeRanges];
-[AVAssetDownloadSession clientBundleIdentifier];
-[AVAssetDownloadSession error];
-[AVAssetDownloadSession isDefunct];
-[AVAssetDownloadSession _weakReference];
-[AVAssetDownloadSession downloadToken];
-[AVAssetDownloadSession _figAsset];
-[AVAssetDownloadSession fileSize];
-[AVAssetDownloadSession URL];
-[AVAssetDownloadSession assetTitle];
-[AVAssetDownloadSession _removeFigPlaybackItemListeners];
-[AVAssetDownloadSession _addFigAssetListeners];
-[AVAssetDownloadSession _addFigPlaybackItemListeners];
-[AVAssetDownloadSession _common_init];
-[AVAssetDownloadSession _createDuplicateFigAssetFromAVAsset:options:];
-[AVAssetDownloadSession _downloadFailureCallbackWithError:];
-[AVAssetDownloadSession _downloadSuccessCallback];
-[AVAssetDownloadSession _errorForFigNotificationPayload:key:];
-[AVAssetDownloadSession _errorFromAssetNotificationPayload:];
-[AVAssetDownloadSession _extractAndSetCommonPropertiesFromOptions:assetOptionsDictionary:];
-[AVAssetDownloadSession _figAssetNotificationNames];
-[AVAssetDownloadSession _figPlaybackItemNotificationNames];
-[AVAssetDownloadSession _playbackItem];
-[AVAssetDownloadSession _primeCache];
-[AVAssetDownloadSession _primeCacheOnDispatchQueue];
-[AVAssetDownloadSession _readyForInspection];
-[AVAssetDownloadSession _removeFigAssetListeners];
-[AVAssetDownloadSession _sendDidFinishDownloadForMediaSelectionWithMediaSelection:];
-[AVAssetDownloadSession _sendDidReceiveMetricEvent:];
-[AVAssetDownloadSession _sendDidResolveMediaSelectionWithMediaSelection:];
-[AVAssetDownloadSession _sendDownloadFailureToDelegateWithError:];
-[AVAssetDownloadSession _sendDownloadSuccessToDelegate];
-[AVAssetDownloadSession _sendLoadedTimeRangesChangedToDelegateWithNewlyLoadedTimeRange:currentLoadedTimeRanges:timeRangeExpectedToLoad:selectedMediaArray:];
-[AVAssetDownloadSession _sendProgessUpdateWithExpectedBytesToDownload:bytesDownloaded:];
-[AVAssetDownloadSession _sendWillDownloadVariants:];
-[AVAssetDownloadSession _setFileFigAsset:options:];
-[AVAssetDownloadSession _setupFigClientObjectAsync:];
-[AVAssetDownloadSession _setupFigClientObjectForFileDownload:];
-[AVAssetDownloadSession _setupFigClientObjectForStreaming:];
-[AVAssetDownloadSession _startLoadingMetadataOnQueue];
-[AVAssetDownloadSession _startOnQueue];
-[AVAssetDownloadSession _startOnQueueFirstTime];
-[AVAssetDownloadSession _stopUnderlyingDownload];
-[AVAssetDownloadSession _transitionToTerminalStatus:error:];
-[AVAssetDownloadSession _verifyDownloadConfigurationForAssetType];
-[AVAssetDownloadSession availableFileSize];
-[AVAssetDownloadSession cancelAndReleaseProgressTimerOnQueue];
-[AVAssetDownloadSession ensureProgressTimerIsRunningOnQueueWithError:];
-[AVAssetDownloadSession initWithAsset:mediaSelections:destinationURL:options:];
-[AVAssetDownloadSession initWithDownloadToken:];
-[AVAssetDownloadSession initWithURL:destinationURL:options:];
-[AVAssetDownloadSession isLiveActivityEnabled];
-[AVAssetDownloadSession isRetryAttempt];
-[AVAssetDownloadSession resolvedMediaSelection];
-[AVAssetDownloadSession startLoadingMetadata];
```
