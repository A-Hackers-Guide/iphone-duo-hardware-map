# `__NSURLBackgroundSession`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSURLSession`
- Protocols: `NDBackgroundSessionClient`, `NSURLSessionSubclass`
- 19 instance variables, 5 properties, 63 instance methods, 0 class methods

## Instance variables

```
Q _identSeed;
@"<NDBackgroundSessionProtocol>" _remoteSession;
@"NSXPCConnection" _xpcConn;
@"NSMutableDictionary" _tasks;
@"NSMutableArray" _taskIDsToFailOnReconnection;
@"NSMutableSet" _taskIDsGettingAuthHeaders;
@"NSObject<OS_dispatch_queue>" _invalidateQueue;
@? _invalidateCallback;
{SmartBlockWithArgs<bool>="__ptr_"^v"__cntrl_"^{__shared_weak_count}} _backgroundSessionDidFinishAppWakeBlock;
@"NSString" _appWakeUUID;
@"NSURL" _downloadDirectory;
@"NSURL" _assetDownloadDirectory;
B _isPrivileged;
B _isInvalid;
B _companionAvailable;
@"NSError" _invalidationError;
B _tryToReconnect;
B _immediatelyReconnectAfterInterruption;
i _notifyToken;
```

## Properties

```
@property (T@"NSString",C,V_appWakeUUID) appWakeUUID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[__NSURLBackgroundSession credStorage_removeCredential:forProtectionSpace:];
-[__NSURLBackgroundSession initWithConfiguration:delegate:delegateQueue:delegateDispatchQueue:];
-[__NSURLBackgroundSession credStorage_allCredentialsWithReply:];
-[__NSURLBackgroundSession credStorage_setCredential:forProtectionSpace:];
-[__NSURLBackgroundSession credStorage_credentialsForProtectionSpace:reply:];
-[__NSURLBackgroundSession _uploadTaskWithTaskForClass:];
-[__NSURLBackgroundSession cameIntoForeground:];
-[__NSURLBackgroundSession appWasLaunchedForBackgroundSession:];
-[__NSURLBackgroundSession backgroundTask:didSendBodyData:totalBytesSent:totalBytesExpectedToSend:];
-[__NSURLBackgroundSession backgroundSessionDidFinishAppWake:reply:];
-[__NSURLBackgroundSession AVAggregateAssetDownloadTaskForURLAsset:mediaSelections:assetTitle:assetArtworkData:options:];
-[__NSURLBackgroundSession wentToBackground:];
-[__NSURLBackgroundSession credStorage_defaultCredentialForProtectionSpace:reply:];
-[__NSURLBackgroundSession _dataTaskWithTaskForClass:];
-[__NSURLBackgroundSession backgroundTask:willPerformHTTPRedirection:withNewRequest:reply:];
-[__NSURLBackgroundSession dealloc];
-[__NSURLBackgroundSession willRetryBackgroundDataTask:withError:transactionMetrics:];
-[__NSURLBackgroundSession credStorage_getInitialCredentialDictionariesWithReply:];
-[__NSURLBackgroundSession _onqueue_handleConnectionsAtAPSleep];
-[__NSURLBackgroundSession _AVAssetDownloadTaskForURL:destinationURL:options:];
-[__NSURLBackgroundSession credStorage_setDefaultCredential:forProtectionSpace:];
-[__NSURLBackgroundSession _onqueue_getTasksWithCompletionHandler:];
-[__NSURLBackgroundSession backgroundTask:willBeginDelayedRequest:reply:];
-[__NSURLBackgroundSession _onqueue_markConnectionsReusedAfterAPSleepWake];
-[__NSURLBackgroundSession _onqueue_completeInvalidation:];
-[__NSURLBackgroundSession _onqueue_flushWithCompletionHandler:];
-[__NSURLBackgroundSession backgroundTask:getAuthHeadersForResponse:reply:];
-[__NSURLBackgroundSession backgroundDownloadTask:didFinishDownloadingToURL:response:reply:];
-[__NSURLBackgroundSession setAppWakeUUID:];
-[__NSURLBackgroundSession backgroundAVAssetDownloadTask:didResolveMediaSelectionProperyList:reply:];
-[__NSURLBackgroundSession backgroundTask:didReceiveResponse:transactionMetrics:];
-[__NSURLBackgroundSession backgroundAVAssetDownloadTask:didLoadTimeRange:totalTimeRangesLoaded:timeRangeExpectedToLoad:forMediaSelectionPropertyList:];
-[__NSURLBackgroundSession backgroundAVAssetDownloadTask:didFinishDownloadForMediaSelectionPropertyList:];
-[__NSURLBackgroundSession webSocketTaskForURL:protocols:];
-[__NSURLBackgroundSession backgroundTask:didReceiveChallenge:reply:];
-[__NSURLBackgroundSession backgroundTaskDidResume:];
-[__NSURLBackgroundSession backgroundAVAssetDownloadTask:didReceiveMetricEvent:reply:];
-[__NSURLBackgroundSession backgroundTask:didReceiveResponse:transactionMetrics:reply:];
-[__NSURLBackgroundSession backgroundDownloadTask:didResumeAtOffset:expectedTotalBytes:];
-[__NSURLBackgroundSession backgroundTask:_willSendRequestForEstablishedConnection:reply:];
-[__NSURLBackgroundSession backgroundAVAssetDownloadTask:willDownloadVariants:reply:];
-[__NSURLBackgroundSession backgroundDataTask:didReceiveData:withReply:];
-[__NSURLBackgroundSession _useTLSSessionCacheFromSession:];
-[__NSURLBackgroundSession _onqueue_resetStorageWithCompletionHandler:];
-[__NSURLBackgroundSession backgroundTask:didCompleteWithError:taskMetrics:info:reply:];
-[__NSURLBackgroundSession backgroundAVAssetDownloadTask:willDownloadToURL:];
-[__NSURLBackgroundSession appWakeUUID];
-[__NSURLBackgroundSession webSocketTaskForRequest:];
-[__NSURLBackgroundSession backgroundTaskHasConnectionWaiting:];
-[__NSURLBackgroundSession backgroundDataTaskDidBecomeDownloadTask:];
-[__NSURLBackgroundSession backgroundTaskDidSuspend:];
-[__NSURLBackgroundSession backgroundAVAssetDownloadTask:didReceiveDownloadToken:];
-[__NSURLBackgroundSession backgroundTask:hasConnectionWaitingWithError:];
-[__NSURLBackgroundSession backgroundTask:didReceiveInformationalResponse:];
-[__NSURLBackgroundSession backgroundTask:needNewBodyStream:withReply:];
-[__NSURLBackgroundSession _downloadTaskWithTaskForClass:];
-[__NSURLBackgroundSession openFileAtPath:mode:withReply:];
-[__NSURLBackgroundSession backgroundDownloadTask:didWriteData:totalBytesWritten:totalBytesExpectedToWrite:];
-[__NSURLBackgroundSession backgroundAVAssetDownloadTaskDidUpdateProgress:totalBytesWritten:totalBytesExpectedToWrite:];
-[__NSURLBackgroundSession AVAssetDownloadTaskForURLAsset:assetTitle:assetArtworkData:options:downloadConfiguration:];
-[__NSURLBackgroundSession backgroundTask:hasConnectionWaitingWithReason:];
-[__NSURLBackgroundSession backgroundSessionDidStartAppWake:reply:];
-[__NSURLBackgroundSession AVAssetDownloadTaskForURLAsset:destinationURL:options:];
```
