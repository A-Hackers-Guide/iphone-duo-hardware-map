# `__NSCFURLProxySessionConnection`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `__NSCFURLSessionConnection`
- Protocols: `NSURLSessionDataDelegate`, `NSURLSessionDataDelegatePrivate`, `NSURLSessionTaskDelegatePrivate`, `NSURLSessionDelegate_Internal`
- 11 instance variables, 4 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"NSURLSessionTask" _proxyTask;
@"NSURLSessionTask" _cacheTask;
B _shouldCancelOnCacheTaskCompletion;
B _clientWantsCacheOnly;
B _completedLocalCacheLookup;
B _requestIsUncacheable;
B _handledNeedNewBodyStream;
@"NSCachedURLResponse" _cachedResponseForConditionalRequest;
@"NSURLRequest" _conditionalRequest;
@"NSArray" _cachedResponseDataArray;
@"NSString" _originalUploadFilePath;
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
-[__NSCFURLProxySessionConnection URLSession:task:needNewBodyStream:];
-[__NSCFURLProxySessionConnection setTLSMinimumSupportedProtocolVersion:];
-[__NSCFURLProxySessionConnection URLSession:didBecomeInvalidWithError:];
-[__NSCFURLProxySessionConnection setIsDownload:];
-[__NSCFURLProxySessionConnection URLSession:task:didSendBodyData:totalBytesSent:totalBytesExpectedToSend:];
-[__NSCFURLProxySessionConnection suspend];
-[__NSCFURLProxySessionConnection setTLSMaximumSupportedProtocolVersion:];
-[__NSCFURLProxySessionConnection URLSession:task:didFinishCollectingMetrics:];
-[__NSCFURLProxySessionConnection URLSession:task:willPerformHTTPRedirection:newRequest:completionHandler:];
-[__NSCFURLProxySessionConnection URLSession:task:didReceiveChallenge:completionHandler:];
-[__NSCFURLProxySessionConnection setPoolPriority:];
-[__NSCFURLProxySessionConnection URLSession:task:_conditionalRequirementsChanged:];
-[__NSCFURLProxySessionConnection expectedProgressTargetChanged];
-[__NSCFURLProxySessionConnection setPriorityHint:incremental:];
-[__NSCFURLProxySessionConnection URLSession:dataTask:_didReceiveData:completionHandler:];
-[__NSCFURLProxySessionConnection URLSession:task:_willSendRequestForEstablishedConnection:completionHandler:];
-[__NSCFURLProxySessionConnection initWithTask:delegate:delegateQueue:];
-[__NSCFURLProxySessionConnection URLSession:task:didCompleteWithError:];
-[__NSCFURLProxySessionConnection dealloc];
-[__NSCFURLProxySessionConnection URLSession:dataTask:didReceiveResponse:completionHandler:];
-[__NSCFURLProxySessionConnection URLSession:task:_isWaitingForConnectionWithReason:];
-[__NSCFURLProxySessionConnection cancel];
-[__NSCFURLProxySessionConnection URLSession:task:didReceiveInformationalResponse:];
-[__NSCFURLProxySessionConnection resume];
-[__NSCFURLProxySessionConnection _URLSession:task:getAuthHeadersForResponse:completionHandler:];
```
