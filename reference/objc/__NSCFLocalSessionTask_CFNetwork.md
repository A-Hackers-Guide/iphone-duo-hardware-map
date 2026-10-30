# `__NSCFLocalSessionTask`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSURLSessionTask`
- Protocols: `NSURLSessionTaskSubclass`, `NSURLSessionDataTaskSubclass`, `__NSCFURLSessionConnectionDelegate`
- 28 instance variables, 5 properties, 61 instance methods, 0 class methods

## Instance variables

```
@"__NSCFURLSessionConnection" _cfConn;
@"NSURL" _uploadFile;
@"NSObject<OS_dispatch_data>" _dataTaskData;
@? _dataTaskCompletion;
@"NSObject<OS_dispatch_data>" _pendingResponseBytes;
Q _suspendCount;
@? _async_initialization;
@"NSObject<OS_dispatch_source>" _resourceTimeout;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _connKeyLock;
^v _connKey;
d _startTimeoutTime;
@"NSObject<OS_dispatch_source>" _startTimeoutTimer;
@"NSObject<OS_dispatch_source>" _payloadTransmissionTimer;
@"NSObject<OS_dispatch_source>" _willSendRequestTimer;
@"NSInputStream" _socketReadStreamForUpgrade;
@"NSOutputStream" _socketWriteStreamForUpgrade;
{shared_ptr<TransportConnection>="__ptr_"^{TransportConnection}"__cntrl_"^{__shared_weak_count}} _connectionForUpgrade;
@"NSObject<OS_dispatch_data>" _extraBytes;
@"NSOperationQueue" _connectionWorkQueue;
i _connectionWorkQueueSuspensionCount;
B _pendingResponseDisposition;
B _pendingResponseDisposition_didFinish;
B _didIssueWaitingForConnectivity;
B _didIssueDidFinish;
B _suspendedForDisposition;
B _didCheckMixedReplace;
B _isMixedReplace;
B _sentDidFinishCollectingMetrics;
```

## Properties

```
@property (T@"__NSCFURLSessionConnection",&,V_cfConn) cfConn;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[__NSCFLocalSessionTask resourceTimeoutError];
-[__NSCFLocalSessionTask connection:willCacheResponse:responseCallback:];
-[__NSCFLocalSessionTask _onqueue_didReceiveChallenge:request:withCompletion:];
-[__NSCFLocalSessionTask _onqueue_adjustLoadingPoolPriority];
-[__NSCFLocalSessionTask error:code:];
-[__NSCFLocalSessionTask cancel_with_error:];
-[__NSCFLocalSessionTask _needSendingMetrics];
-[__NSCFLocalSessionTask _onqueue_cancel_with_error:];
-[__NSCFLocalSessionTask _onqueue_cancel];
-[__NSCFLocalSessionTask _onqueue_didFinishWithError:];
-[__NSCFLocalSessionTask connection:didReceiveInformationalResponse:];
-[__NSCFLocalSessionTask cfConn];
-[__NSCFLocalSessionTask _onqueue_didSendBodyBytes:totalBytesSent:totalBytesExpectedToSend:];
-[__NSCFLocalSessionTask _onqueue_alternatePathAvailable:];
-[__NSCFLocalSessionTask _private_onqueue_didReceiveResponseDisposition:completion:];
-[__NSCFLocalSessionTask _onqueue_setupNextEffectiveConfigurationWithCompletionHandler:];
-[__NSCFLocalSessionTask _onqueue_connectionWaitingWithReason:];
-[__NSCFLocalSessionTask _onqueue_didReceiveResponse:completion:];
-[__NSCFLocalSessionTask connectionWillFinishLoading:];
-[__NSCFLocalSessionTask _onqueue_didReceiveResponse:redirectRequest:withCompletion:];
-[__NSCFLocalSessionTask set_TLSMaximumSupportedProtocolVersion:];
-[__NSCFLocalSessionTask _onqueue_resume];
-[__NSCFLocalSessionTask connection:request:needsNewBodyStreamFromOffset:callback:];
-[__NSCFLocalSessionTask connection:alternatePathAvailable:];
-[__NSCFLocalSessionTask startResourceTimer];
-[__NSCFLocalSessionTask connection:didFinishLoadingWithError:];
-[__NSCFLocalSessionTask connection:_willSendRequestForEstablishedConnection:completion:];
-[__NSCFLocalSessionTask _onqueue_willSendRequestForEstablishedConnection:withCompletion:];
-[__NSCFLocalSessionTask connection:didReceiveResponse:completion:];
-[__NSCFLocalSessionTask _didSendMetrics];
-[__NSCFLocalSessionTask _onqueue_needNewBodyStream:withCompletion:];
-[__NSCFLocalSessionTask connection:_conditionalRequirementsChanged:];
-[__NSCFLocalSessionTask initWithOriginalRequest:ident:taskGroup:];
-[__NSCFLocalSessionTask _onqueue_strippedMutableRequest];
-[__NSCFLocalSessionTask _onqueue_adjustBytesPerSecondLimit:];
-[__NSCFLocalSessionTask _onqueue_conditionalRequirementsChanged:];
-[__NSCFLocalSessionTask connection:wasRedirected:newRequest:responseCallback:];
-[__NSCFLocalSessionTask connection:didReceiveSocketInputStream:outputStream:];
-[__NSCFLocalSessionTask _onqueue_expectedProgressTargetChanged];
-[__NSCFLocalSessionTask initWithBackgroundTaskInfo:taskGroup:];
-[__NSCFLocalSessionTask _onqueue_needNewBodyStream:fromOffset:withCompletion:];
-[__NSCFLocalSessionTask _onqueue_suspend];
-[__NSCFLocalSessionTask _onqueue_willCacheResponse:withCompletion:];
-[__NSCFLocalSessionTask _onqueue_adjustPriorityHint:incremental:];
-[__NSCFLocalSessionTask _task_onqueue_didReceiveDispatchData:completionHandler:];
-[__NSCFLocalSessionTask _onqueue_adjustPoolPriority];
-[__NSCFLocalSessionTask set_timeoutIntervalForResource:];
-[__NSCFLocalSessionTask setCfConn:];
-[__NSCFLocalSessionTask _onqueue_didReceiveDispatchData:completion:];
-[__NSCFLocalSessionTask _setConnectionCacheKey:];
-[__NSCFLocalSessionTask _task_onqueue_didFinish];
-[__NSCFLocalSessionTask connection:didReceiveData:completion:];
-[__NSCFLocalSessionTask _onqueue_completeInitialization];
-[__NSCFLocalSessionTask connection:request:needsNewBodyStreamCallback:];
-[__NSCFLocalSessionTask connection:challenged:authCallback:];
-[__NSCFLocalSessionTask connection:didReceiveTCPConnection:extraBytes:];
-[__NSCFLocalSessionTask connection:waitingWithReason:];
-[__NSCFLocalSessionTask set_TLSMinimumSupportedProtocolVersion:];
-[__NSCFLocalSessionTask _onSessionQueue_disavow];
-[__NSCFLocalSessionTask connection:sentBodyBytes:totalBytes:expectedBytes:];
-[__NSCFLocalSessionTask dealloc];
```
