# `__NSURLSessionLocal`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSURLSession`
- Protocols: `NSURLSessionDataDelegate`, `NSURLSessionDataDelegatePrivate`, `NSURLSessionTaskDelegatePrivate`, `NSURLSessionDelegate_Internal`, `NSURLSessionSubclass`, `__NSURLSessionTaskGroupForConfiguration`
- 18 instance variables, 6 properties, 21 instance methods, 0 class methods

## Instance variables

```
Q _identSeed;
^v _tubeManager;
@"NSMutableArray" _outstandingTasks;
@"NSHashTable" _unownedUnresumedTasks;
@"NSObject<OS_dispatch_queue>" _invalidateQueue;
@? _invalidateCallback;
r^{XCookieStorage=^^?^{__CFAllocator}i} _xCookies;
r^{XCredentialStorage=^^?^{__CFAllocator}i} _xCreds;
B _xCookiesInitComplete;
B _xCredsInitComplete;
{mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}} _xCookieStorageInitLock;
{mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}} _xCredStorageInitLock;
B _isInvalid;
@"NSURLSessionConfiguration" _proxyConfig;
@"NSURLSession" _proxySession;
B _shouldRecreateProxySession;
@"NSURLSession" _sessionForCacheLookups;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _unownedUnresumedTasksLock;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSURLSessionConfiguration",R,W) _groupConfiguration;
@property (T@"NSURLSession",R,W) _groupSession;
```

## Instance methods

```
-[__NSURLSessionLocal initWithConfiguration:delegate:delegateQueue:delegateDispatchQueue:];
-[__NSURLSessionLocal URLSession:didBecomeInvalidWithError:];
-[__NSURLSessionLocal _uploadTaskWithTaskForClass:];
-[__NSURLSessionLocal AVAggregateAssetDownloadTaskForURLAsset:mediaSelections:assetTitle:assetArtworkData:options:];
-[__NSURLSessionLocal nextSeed];
-[__NSURLSessionLocal _dataTaskWithTaskForClass:];
-[__NSURLSessionLocal dealloc];
-[__NSURLSessionLocal _onqueue_handleConnectionsAtAPSleep];
-[__NSURLSessionLocal _AVAssetDownloadTaskForURL:destinationURL:options:];
-[__NSURLSessionLocal _onqueue_getTasksWithCompletionHandler:];
-[__NSURLSessionLocal _onqueue_markConnectionsReusedAfterAPSleepWake];
-[__NSURLSessionLocal _onqueue_completeInvalidation:];
-[__NSURLSessionLocal _onqueue_flushWithCompletionHandler:];
-[__NSURLSessionLocal webSocketTaskForURL:protocols:];
-[__NSURLSessionLocal _useTLSSessionCacheFromSession:];
-[__NSURLSessionLocal _onqueue_resetStorageWithCompletionHandler:];
-[__NSURLSessionLocal webSocketTaskForRequest:];
-[__NSURLSessionLocal copyWithZone:];
-[__NSURLSessionLocal _downloadTaskWithTaskForClass:];
-[__NSURLSessionLocal AVAssetDownloadTaskForURLAsset:assetTitle:assetArtworkData:options:downloadConfiguration:];
-[__NSURLSessionLocal AVAssetDownloadTaskForURLAsset:destinationURL:options:];
```
