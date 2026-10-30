# `NDBackgroundSessionClient` (protocol)

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 40 instance methods, 0 class methods

## Instance methods

```
-[NDBackgroundSessionClient credStorage_removeCredential:forProtectionSpace:];
-[NDBackgroundSessionClient credStorage_allCredentialsWithReply:];
-[NDBackgroundSessionClient credStorage_setCredential:forProtectionSpace:];
-[NDBackgroundSessionClient credStorage_credentialsForProtectionSpace:reply:];
-[NDBackgroundSessionClient backgroundTask:didSendBodyData:totalBytesSent:totalBytesExpectedToSend:];
-[NDBackgroundSessionClient backgroundSessionDidFinishAppWake:reply:];
-[NDBackgroundSessionClient credStorage_defaultCredentialForProtectionSpace:reply:];
-[NDBackgroundSessionClient backgroundTask:willPerformHTTPRedirection:withNewRequest:reply:];
-[NDBackgroundSessionClient willRetryBackgroundDataTask:withError:transactionMetrics:];
-[NDBackgroundSessionClient credStorage_getInitialCredentialDictionariesWithReply:];
-[NDBackgroundSessionClient credStorage_setDefaultCredential:forProtectionSpace:];
-[NDBackgroundSessionClient backgroundTask:willBeginDelayedRequest:reply:];
-[NDBackgroundSessionClient backgroundTask:getAuthHeadersForResponse:reply:];
-[NDBackgroundSessionClient backgroundDownloadTask:didFinishDownloadingToURL:response:reply:];
-[NDBackgroundSessionClient backgroundAVAssetDownloadTask:didResolveMediaSelectionProperyList:reply:];
-[NDBackgroundSessionClient backgroundTask:didReceiveResponse:transactionMetrics:];
-[NDBackgroundSessionClient backgroundAVAssetDownloadTask:didLoadTimeRange:totalTimeRangesLoaded:timeRangeExpectedToLoad:forMediaSelectionPropertyList:];
-[NDBackgroundSessionClient backgroundAVAssetDownloadTask:didFinishDownloadForMediaSelectionPropertyList:];
-[NDBackgroundSessionClient backgroundTask:didReceiveChallenge:reply:];
-[NDBackgroundSessionClient backgroundTaskDidResume:];
-[NDBackgroundSessionClient backgroundAVAssetDownloadTask:didReceiveMetricEvent:reply:];
-[NDBackgroundSessionClient backgroundTask:didReceiveResponse:transactionMetrics:reply:];
-[NDBackgroundSessionClient backgroundDownloadTask:didResumeAtOffset:expectedTotalBytes:];
-[NDBackgroundSessionClient backgroundTask:_willSendRequestForEstablishedConnection:reply:];
-[NDBackgroundSessionClient backgroundAVAssetDownloadTask:willDownloadVariants:reply:];
-[NDBackgroundSessionClient backgroundDataTask:didReceiveData:withReply:];
-[NDBackgroundSessionClient backgroundTask:didCompleteWithError:taskMetrics:info:reply:];
-[NDBackgroundSessionClient backgroundAVAssetDownloadTask:willDownloadToURL:];
-[NDBackgroundSessionClient backgroundTaskHasConnectionWaiting:];
-[NDBackgroundSessionClient backgroundDataTaskDidBecomeDownloadTask:];
-[NDBackgroundSessionClient backgroundTaskDidSuspend:];
-[NDBackgroundSessionClient backgroundAVAssetDownloadTask:didReceiveDownloadToken:];
-[NDBackgroundSessionClient backgroundTask:hasConnectionWaitingWithError:];
-[NDBackgroundSessionClient backgroundTask:didReceiveInformationalResponse:];
-[NDBackgroundSessionClient backgroundTask:needNewBodyStream:withReply:];
-[NDBackgroundSessionClient openFileAtPath:mode:withReply:];
-[NDBackgroundSessionClient backgroundDownloadTask:didWriteData:totalBytesWritten:totalBytesExpectedToWrite:];
-[NDBackgroundSessionClient backgroundAVAssetDownloadTaskDidUpdateProgress:totalBytesWritten:totalBytesExpectedToWrite:];
-[NDBackgroundSessionClient backgroundTask:hasConnectionWaitingWithReason:];
-[NDBackgroundSessionClient backgroundSessionDidStartAppWake:reply:];
```
