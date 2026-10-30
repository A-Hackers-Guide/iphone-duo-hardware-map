# `__NSCFURLSessionConnection`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 8 instance variables, 0 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSURLSessionTask" _task;
@"NSObject<OS_dispatch_queue>" _workQueue;
@"<__NSCFURLSessionConnectionDelegate>" _delegate;
B _isFromCache;
@"NSURLResponse" _cacheResponse;
@"NSObject<OS_dispatch_data>" _cacheData;
Q _cacheDataMax;
q _maxCacheEntrySize;
```

## Instance methods

```
-[__NSCFURLSessionConnection setBytesPerSecondLimit:];
-[__NSCFURLSessionConnection setTLSMinimumSupportedProtocolVersion:];
-[__NSCFURLSessionConnection setIsDownload:];
-[__NSCFURLSessionConnection suspend];
-[__NSCFURLSessionConnection setTLSMaximumSupportedProtocolVersion:];
-[__NSCFURLSessionConnection setPoolPriority:];
-[__NSCFURLSessionConnection expectedProgressTargetChanged];
-[__NSCFURLSessionConnection setPriorityHint:incremental:];
-[__NSCFURLSessionConnection initWithTask:delegate:delegateQueue:];
-[__NSCFURLSessionConnection dealloc];
-[__NSCFURLSessionConnection copyWithZone:];
-[__NSCFURLSessionConnection cancel];
-[__NSCFURLSessionConnection resume];
```
