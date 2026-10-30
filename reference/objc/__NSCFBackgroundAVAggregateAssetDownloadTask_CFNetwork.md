# `__NSCFBackgroundAVAggregateAssetDownloadTask`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `__NSCFBackgroundSessionTask`
- Protocols: `AVAssetDownloadDelegate`, `AVAssetDownloadDelegatePrivate`
- 11 instance variables, 5 properties, 17 instance methods, 0 class methods

## Instance variables

```
B _sentWillDownloadToURL;
B _sentWillBeginDelayedRequest;
@"AVURLAsset" _URLAsset;
Q _AVAssetDownloadToken;
@"NSArray" _mediaSelections;
@"NSString" _assetTitle;
@"NSData" _assetArtworkData;
@"NSDictionary" _options;
@"NSString" _childAssetDownloadTasksSessionIdentifier;
@"NSURLSession" _childAssetDownloadSession;
@"NSArray" _childAssetDownloadTasks;
```

## Properties

```
@property (T@"AVURLAsset",&,V_URLAsset) URLAsset;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[__NSCFBackgroundAVAggregateAssetDownloadTask currentRequest];
-[__NSCFBackgroundAVAggregateAssetDownloadTask _onqueue_cancel];
-[__NSCFBackgroundAVAggregateAssetDownloadTask _onqueue_resume];
-[__NSCFBackgroundAVAggregateAssetDownloadTask _onqueue_suspend];
-[__NSCFBackgroundAVAggregateAssetDownloadTask URLAsset];
-[__NSCFBackgroundAVAggregateAssetDownloadTask URLSession:task:didCompleteWithError:];
-[__NSCFBackgroundAVAggregateAssetDownloadTask dealloc];
-[__NSCFBackgroundAVAggregateAssetDownloadTask originalRequest];
-[__NSCFBackgroundAVAggregateAssetDownloadTask isKindOfClass:];
-[__NSCFBackgroundAVAggregateAssetDownloadTask _isAVAssetTask];
-[__NSCFBackgroundAVAggregateAssetDownloadTask response];
-[__NSCFBackgroundAVAggregateAssetDownloadTask URLSession:task:willBeginDelayedRequest:completionHandler:];
-[__NSCFBackgroundAVAggregateAssetDownloadTask URLSession:assetDownloadTask:didLoadTimeRange:totalTimeRangesLoaded:timeRangeExpectedToLoad:];
-[__NSCFBackgroundAVAggregateAssetDownloadTask URLSession:assetDownloadTask:willDownloadToURL:];
-[__NSCFBackgroundAVAggregateAssetDownloadTask cookiesForCurrentRequest];
-[__NSCFBackgroundAVAggregateAssetDownloadTask initWithTaskInfo:taskGroup:ident:];
-[__NSCFBackgroundAVAggregateAssetDownloadTask setURLAsset:];
```
