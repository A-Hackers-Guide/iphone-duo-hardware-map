# `NSURLSession`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `__NSURLSessionTaskGroupForConfiguration`
- 20 instance variables, 13 properties, 65 instance methods, 16 class methods

## Instance variables

```
@"__CFN_ConnectionContextManager" _nwContextManager;
{shared_ptr<NSObject<OS_nw_context>>="__ptr_"@"NSObject<OS_nw_context>""__cntrl_"^{__shared_weak_count}} _nwContext;
@"NSDictionary" _atsState_ivar;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _invalid_ivar;
I _rootPort;
^{IONotificationPort=} _notifyPortRef;
I _notifierObject;
B _isSharedSession_ivar;
@"__NSCFURLSessionDelegateWrapper" _delegateWrapper;
@"NSOperationQueue" _delegateQueue_ivar;
@"NSObject<OS_dispatch_queue>" _delegateDispatchQueue;
@"<NSURLSessionDelegate>" _delegate_ivar;
@"NSString" _sessionDescription_ivar;
@"NSURLSessionConfiguration" _local_immutable_configuration_ivar;
@"NSObject<OS_dispatch_queue>" _workQueue;
@"NSUUID" _uuid_ivar;
@"NSString" _tlsSessionCachePrefix;
@"NSMutableDictionary" _httpFallbackHosts;
@"NSMutableDictionary" _coalescing;
```

## Properties

```
@property (T@"NSString",C,N,V_tlsSessionCachePrefix) _tlsSessionCachePrefix;
@property (TQ,R,D) nextSeed;
@property (T@"NSObject<OS_nw_context>",R) _networkContext;
@property (T@"NSOperationQueue",R,&,D) delegateQueue;
@property (T@"<NSURLSessionDelegate>",R,&,V_delegate_ivar) delegate;
@property (T@"NSURLSessionConfiguration",R,C) configuration;
@property (T@"NSString",C,V_sessionDescription_ivar) sessionDescription;
@property (T@"NSURLSessionConfiguration",R,W,D) _groupConfiguration;
@property (T@"NSURLSession",R,W,D) _groupSession;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[NSURLSession class];
+[NSURLSession sharedSession];
+[NSURLSession new];
+[NSURLSession _disableAppSSO];
+[NSURLSession _enumerateHTTPHeaderFieldsWithRequest:usingBlock:];
+[NSURLSession _strictTrustEvaluate:queue:completionHandler:];
+[NSURLSession sessionWithConfiguration:];
+[NSURLSession sessionWithConfiguration:delegate:delegateQueue:];
+[NSURLSession _releaseProcessAssertionForSessionIdentifier:];
+[NSURLSession _sendPendingCallbacksForSessionIdentifier:];
+[NSURLSession _backgroundServiceAvailable];
+[NSURLSession _disableATS];
+[NSURLSession _enumerateHTTPHeaderFieldsWithCFHTTPMessage:usingBlock:];
+[NSURLSession _getActiveSessionIdentifiersWithCompletionHandler:];
+[NSURLSession _obliterateAllBackgroundSessionsWithCompletionHandler:];
+[NSURLSession _sessionWithConfiguration:delegate:delegateDispatchQueue:];
```

## Instance methods

```
-[NSURLSession finishTasksAndInvalidate];
-[NSURLSession initWithConfiguration:delegate:delegateQueue:delegateDispatchQueue:];
-[NSURLSession _uploadTaskWithTaskForClass:];
-[NSURLSession dataTaskWithRequest:completionHandler:];
-[NSURLSession invalidateAndCancel];
-[NSURLSession dataTaskWithRequest:];
-[NSURLSession init];
-[NSURLSession _dataTaskWithTaskForClass:];
-[NSURLSession dealloc];
-[NSURLSession configuration];
-[NSURLSession delegate];
-[NSURLSession _useTLSSessionCacheFromSession:];
-[NSURLSession copyWithZone:];
-[NSURLSession delegateQueue];
-[NSURLSession _downloadTaskWithTaskForClass:];
-[NSURLSession flushWithCompletionHandler:];
-[NSURLSession _dataTaskWithRequest:delegate:];
-[NSURLSession _dataTaskWithRequest:delegate:completionHandler:];
-[NSURLSession _dataTaskWithURL:delegate:];
-[NSURLSession _dataTaskWithURL:delegate:completionHandler:];
-[NSURLSession _downloadTaskWithRequest:delegate:completionHandler:];
-[NSURLSession _downloadTaskWithResumeData:delegate:completionHandler:];
-[NSURLSession _downloadTaskWithURL:delegate:completionHandler:];
-[NSURLSession _uploadTaskWithRequest:fromData:delegate:completionHandler:];
-[NSURLSession _uploadTaskWithRequest:fromFile:delegate:completionHandler:];
-[NSURLSession _networkContext];
-[NSURLSession uploadTaskWithRequest:fromFile:];
-[NSURLSession webSocketTaskWithURL:protocols:];
-[NSURLSession uploadTaskWithRequest:fromData:];
-[NSURLSession _uploadTaskWithResumeData:delegate:completionHandler:];
-[NSURLSession dataTaskWithURL:];
-[NSURLSession dataTaskWithURL:completionHandler:];
-[NSURLSession downloadTaskWithRequest:];
-[NSURLSession downloadTaskWithRequest:completionHandler:];
-[NSURLSession downloadTaskWithResumeData:];
-[NSURLSession downloadTaskWithResumeData:completionHandler:];
-[NSURLSession downloadTaskWithURL:];
-[NSURLSession downloadTaskWithURL:completionHandler:];
-[NSURLSession getAllTasksWithCompletionHandler:];
-[NSURLSession getTasksWithCompletionHandler:];
-[NSURLSession resetWithCompletionHandler:];
-[NSURLSession sessionDescription];
-[NSURLSession setSessionDescription:];
-[NSURLSession streamTaskWithHostName:port:];
-[NSURLSession streamTaskWithNetService:];
-[NSURLSession uploadTaskWithRequest:fromData:completionHandler:];
-[NSURLSession uploadTaskWithRequest:fromFile:completionHandler:];
-[NSURLSession uploadTaskWithResumeData:];
-[NSURLSession uploadTaskWithResumeData:completionHandler:];
-[NSURLSession uploadTaskWithStreamedRequest:];
-[NSURLSession webSocketTaskWithRequest:];
-[NSURLSession webSocketTaskWithURL:];
-[NSURLSession _AVAssetDownloadTaskWithURL:destinationURL:options:];
-[NSURLSession _downloadTaskWithRequest:downloadFilePath:];
-[NSURLSession _groupConfiguration];
-[NSURLSession _groupSession];
-[NSURLSession _tlsSessionCachePrefix];
-[NSURLSession aggregateAssetDownloadTaskWithURLAsset:mediaSelections:assetTitle:assetArtworkData:options:];
-[NSURLSession assetDownloadTaskWithConfiguration:];
-[NSURLSession assetDownloadTaskWithURLAsset:assetTitle:assetArtworkData:options:];
-[NSURLSession assetDownloadTaskWithURLAsset:destinationURL:options:];
-[NSURLSession dataTaskWithRequest:uniqueIdentifier:];
-[NSURLSession defaultTaskGroup];
-[NSURLSession set_tlsSessionCachePrefix:];
-[NSURLSession taskGroupWithConfiguration:];
```
