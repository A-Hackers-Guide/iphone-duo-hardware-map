# `NWURLSession`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 22 instance variables, 5 properties, 50 instance methods, 7 class methods

## Instance variables

```
[16C] uuid;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} lock;
B _invalidated;
I _nextTaskIdentifier;
I _rootPort;
I _notifierObject;
@"NSObject<OS_nw_http_cookie_storage>" _HTTPCookieStorage;
@"NSObject<OS_nw_authentication_credential_storage>" _URLCredentialStorage;
@"NSObject<OS_nw_array>" _URLCredentialCache;
@"NSObject<OS_nw_http_connection_state_storage>" _connectionStateStorage;
@"NSObject<OS_nw_array>" _connectionProxyArray;
@"NSObject<OS_sec_protocol_configuration>" _atsConfig;
@"NSString" _sessionDescription;
@"NSURLSessionConfiguration" _internalConfiguration;
@"NSHashTable" _weakUnresumedTasks;
@"NSMutableSet" _runningTasks;
@"NSMutableDictionary" _trustExceptions;
^{IONotificationPort=} _notifyPortRef;
@ _retainedSelf;
@"NSObject<OS_dispatch_queue>" _queue;
@"NWURLSessionDelegateWrapper" _delegateWrapper;
@"NSObject<OS_nw_context>" _context;
```

## Properties

```
@property (T@"NSOperationQueue",R,N) delegateQueue;
@property (T@"<NSURLSessionDelegate>",R,N) delegate;
@property (T@"NSURLSessionConfiguration",R,C,N) configuration;
@property (T@"NSString",C,V_sessionDescription) sessionDescription;
@property (T@"NSObject<OS_nw_context>",R,N) _networkContext;
```

## Class methods

```
+[NWURLSession initialize];
+[NWURLSession sharedSession];
+[NWURLSession isSubclassOfClass:];
+[NWURLSession _disableAppSSO];
+[NWURLSession _strictTrustEvaluate:queue:completionHandler:];
+[NWURLSession sessionWithConfiguration:];
+[NWURLSession sessionWithConfiguration:delegate:delegateQueue:];
```

## Instance methods

```
-[NWURLSession finishTasksAndInvalidate];
-[NWURLSession initWithConfiguration:delegate:delegateQueue:];
-[NWURLSession dataTaskWithRequest:completionHandler:];
-[NWURLSession invalidateAndCancel];
-[NWURLSession dataTaskWithRequest:];
-[NWURLSession configuration];
-[NWURLSession delegate];
-[NWURLSession isKindOfClass:];
-[NWURLSession delegateQueue];
-[NWURLSession flushWithCompletionHandler:];
-[NWURLSession _dataTaskWithRequest:delegate:];
-[NWURLSession _dataTaskWithRequest:delegate:completionHandler:];
-[NWURLSession _dataTaskWithURL:delegate:];
-[NWURLSession _dataTaskWithURL:delegate:completionHandler:];
-[NWURLSession _downloadTaskWithRequest:delegate:completionHandler:];
-[NWURLSession _downloadTaskWithResumeData:delegate:completionHandler:];
-[NWURLSession _downloadTaskWithURL:delegate:completionHandler:];
-[NWURLSession _uploadTaskWithRequest:fromData:delegate:completionHandler:];
-[NWURLSession _uploadTaskWithRequest:fromFile:delegate:completionHandler:];
-[NWURLSession _networkContext];
-[NWURLSession uploadTaskWithRequest:fromFile:];
-[NWURLSession webSocketTaskWithURL:protocols:];
-[NWURLSession uploadTaskWithRequest:fromData:];
-[NWURLSession _uploadTaskWithResumeData:delegate:completionHandler:];
-[NWURLSession dataTaskWithResumeInfo:];
-[NWURLSession dataTaskWithURL:];
-[NWURLSession dataTaskWithURL:completionHandler:];
-[NWURLSession downloadTaskWithRequest:];
-[NWURLSession downloadTaskWithRequest:completionHandler:];
-[NWURLSession downloadTaskWithResumeData:];
-[NWURLSession downloadTaskWithResumeData:completionHandler:];
-[NWURLSession downloadTaskWithResumeInfo:];
-[NWURLSession downloadTaskWithURL:];
-[NWURLSession downloadTaskWithURL:completionHandler:];
-[NWURLSession getAllTasksWithCompletionHandler:];
-[NWURLSession getTasksWithCompletionHandler:];
-[NWURLSession initWithConfiguration:UUID:delegate:delegateQueue:delegateDispatchQueue:];
-[NWURLSession resetWithCompletionHandler:];
-[NWURLSession sessionDescription];
-[NWURLSession setSessionDescription:];
-[NWURLSession streamTaskWithHostName:port:];
-[NWURLSession streamTaskWithNetService:];
-[NWURLSession uploadTaskWithRequest:fromData:completionHandler:];
-[NWURLSession uploadTaskWithRequest:fromFile:completionHandler:];
-[NWURLSession uploadTaskWithResumeData:];
-[NWURLSession uploadTaskWithResumeData:completionHandler:];
-[NWURLSession uploadTaskWithResumeInfo:];
-[NWURLSession uploadTaskWithStreamedRequest:];
-[NWURLSession webSocketTaskWithRequest:];
-[NWURLSession webSocketTaskWithURL:];
```
