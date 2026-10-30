# `__NSCFBackgroundAVAssetDownloadTask`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `__NSCFBackgroundSessionTask`
- 15 instance variables, 6 properties, 32 instance methods, 0 class methods

## Instance variables

```
Q _downloadToken;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _progressLock;
B _didCleanupProgress;
B _enableSPIDelegateCallbacks;
@"NSProgress" _progress;
Q _AVAssetDownloadToken;
@"NSURL" _URL;
@"NSURL" _destinationURL;
@"AVURLAsset" _URLAsset;
@"NSDictionary" _options;
@"NSArray" _loadedTimeRanges;
@"NSURL" _temporaryDestinationURL;
@"NSString" _assetTitle;
@"NSData" _assetArtworkData;
@"AVMediaSelection" _resolvedMediaSelection;
```

## Properties

```
@property (TQ,V_AVAssetDownloadToken) AVAssetDownloadToken;
@property (T@"NSURL",C,V_URL) URL;
@property (T@"NSURL",C,V_destinationURL) destinationURL;
@property (T@"AVURLAsset",&,V_URLAsset) URLAsset;
@property (T@"NSDictionary",C,V_options) options;
@property (T@"NSArray",C,V_loadedTimeRanges) loadedTimeRanges;
```

## Instance methods

```
-[__NSCFBackgroundAVAssetDownloadTask currentRequest];
-[__NSCFBackgroundAVAssetDownloadTask _onqueue_didFinishWithError:];
-[__NSCFBackgroundAVAssetDownloadTask setOptions:];
-[__NSCFBackgroundAVAssetDownloadTask URLAsset];
-[__NSCFBackgroundAVAssetDownloadTask dealloc];
-[__NSCFBackgroundAVAssetDownloadTask setLoadedTimeRanges:];
-[__NSCFBackgroundAVAssetDownloadTask originalRequest];
-[__NSCFBackgroundAVAssetDownloadTask destinationURL];
-[__NSCFBackgroundAVAssetDownloadTask loadedTimeRanges];
-[__NSCFBackgroundAVAssetDownloadTask progress];
-[__NSCFBackgroundAVAssetDownloadTask setURL:];
-[__NSCFBackgroundAVAssetDownloadTask isKindOfClass:];
-[__NSCFBackgroundAVAssetDownloadTask options];
-[__NSCFBackgroundAVAssetDownloadTask _isAVAssetTask];
-[__NSCFBackgroundAVAssetDownloadTask URL];
-[__NSCFBackgroundAVAssetDownloadTask response];
-[__NSCFBackgroundAVAssetDownloadTask setDestinationURL:];
-[__NSCFBackgroundAVAssetDownloadTask AVAssetDownloadToken];
-[__NSCFBackgroundAVAssetDownloadTask _onqueue_didReceiveMetricEvent:];
-[__NSCFBackgroundAVAssetDownloadTask _finishProgressReporting];
-[__NSCFBackgroundAVAssetDownloadTask _onqueue_didFinishDownloadforMediaSelectionPropertyList:];
-[__NSCFBackgroundAVAssetDownloadTask _onqueue_didFinishDownloadingToURL:];
-[__NSCFBackgroundAVAssetDownloadTask _onqueue_didLoadTimeRange:totalTimeRangesLoaded:timeRangeExpectedToLoad:forMediaSelectionPropertyList:];
-[__NSCFBackgroundAVAssetDownloadTask _onqueue_didReceiveProgressUpdateWithTotalBytesWritten:totalBytesExpectedToWrite:];
-[__NSCFBackgroundAVAssetDownloadTask _onqueue_didResolveMediaSelectionPropertyList:];
-[__NSCFBackgroundAVAssetDownloadTask _onqueue_willDownloadToURL:];
-[__NSCFBackgroundAVAssetDownloadTask _onqueue_willDownloadVariants:];
-[__NSCFBackgroundAVAssetDownloadTask cookiesForCurrentRequest];
-[__NSCFBackgroundAVAssetDownloadTask initWithTaskGroup:URLAsset:URL:destinationURL:temporaryDestinationURL:assetTitle:assetArtworkData:ident:enableSPIDelegateCallbacks:];
-[__NSCFBackgroundAVAssetDownloadTask initWithTaskInfo:taskGroup:ident:];
-[__NSCFBackgroundAVAssetDownloadTask setAVAssetDownloadToken:];
-[__NSCFBackgroundAVAssetDownloadTask setURLAsset:];
```
