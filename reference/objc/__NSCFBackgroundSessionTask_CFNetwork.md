# `__NSCFBackgroundSessionTask`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSURLSessionTask`
- Protocols: `NSURLSessionTaskSubclass`
- 5 instance variables, 4 properties, 27 instance methods, 0 class methods

## Instance variables

```
@"NSMutableSet" _secKeyProxies;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _proxyLock;
B _sentCancel;
B _sentDidFinish;
@"NSError" _immediateError;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[__NSCFBackgroundSessionTask _onqueue_adjustLoadingPoolPriority];
-[__NSCFBackgroundSessionTask _onqueue_cancel];
-[__NSCFBackgroundSessionTask _onqueue_didFinishWithError:];
-[__NSCFBackgroundSessionTask set_TLSMaximumSupportedProtocolVersion:];
-[__NSCFBackgroundSessionTask _onqueue_resume];
-[__NSCFBackgroundSessionTask _onqueue_willSendRequestForEstablishedConnection:withCompletion:];
-[__NSCFBackgroundSessionTask initWithOriginalRequest:ident:taskGroup:];
-[__NSCFBackgroundSessionTask _onqueue_adjustBytesPerSecondLimit:];
-[__NSCFBackgroundSessionTask _onqueue_suspend];
-[__NSCFBackgroundSessionTask _onqueue_adjustPriorityHint:incremental:];
-[__NSCFBackgroundSessionTask _onqueue_adjustPoolPriority];
-[__NSCFBackgroundSessionTask set_TLSMinimumSupportedProtocolVersion:];
-[__NSCFBackgroundSessionTask _onSessionQueue_disavow];
-[__NSCFBackgroundSessionTask dealloc];
-[__NSCFBackgroundSessionTask _onqueue_didReceiveResponse:];
-[__NSCFBackgroundSessionTask setDelegate:];
-[__NSCFBackgroundSessionTask set_discretionaryOverride:];
-[__NSCFBackgroundSessionTask _timingData];
-[__NSCFBackgroundSessionTask setTaskDescription:];
-[__NSCFBackgroundSessionTask addSecKeyProxy:];
-[__NSCFBackgroundSessionTask _applyBackgroundTaskOverrides:];
-[__NSCFBackgroundSessionTask _onqueue_didReceiveInformationalResponse:];
-[__NSCFBackgroundSessionTask cookiesForCurrentRequest];
-[__NSCFBackgroundSessionTask initWithBackgroundTask:];
-[__NSCFBackgroundSessionTask initWithTaskInfo:taskGroup:ident:];
-[__NSCFBackgroundSessionTask removeSecKeyProxy:];
-[__NSCFBackgroundSessionTask requestWithCookiesApplied:];
```
