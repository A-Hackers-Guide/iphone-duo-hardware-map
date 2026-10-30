# `AVAssetCustomURLBridgeForNSURLSession`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSURLSessionDataDelegate`
- 4 instance variables, 5 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _taskToRequest;
@"NSURLSession" _session;
^{OpaqueFigCustomURLHandler=} _handler;
@"NSObject<OS_dispatch_queue>" _callbackQueue;
```

## Properties

```
@property (T@"NSURLSession",&,N,V_session) session;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AVAssetCustomURLBridgeForNSURLSession URLSession:dataTask:didReceiveData:];
-[AVAssetCustomURLBridgeForNSURLSession _cancelRequestID:];
-[AVAssetCustomURLBridgeForNSURLSession URLSession:task:didFinishCollectingMetrics:];
-[AVAssetCustomURLBridgeForNSURLSession init];
-[AVAssetCustomURLBridgeForNSURLSession URLSession:task:didCompleteWithError:];
-[AVAssetCustomURLBridgeForNSURLSession dealloc];
-[AVAssetCustomURLBridgeForNSURLSession URLSession:dataTask:didReceiveResponse:completionHandler:];
-[AVAssetCustomURLBridgeForNSURLSession setSession:];
-[AVAssetCustomURLBridgeForNSURLSession initWithFigAsset:];
-[AVAssetCustomURLBridgeForNSURLSession URLSession:dataTask:willCacheResponse:completionHandler:];
-[AVAssetCustomURLBridgeForNSURLSession session];
-[AVAssetCustomURLBridgeForNSURLSession _handleRequest:requestID:canHandleRequestOut:];
-[AVAssetCustomURLBridgeForNSURLSession _lookupRequestForDataTask:];
-[AVAssetCustomURLBridgeForNSURLSession _registerRequest:id:forDataTask:];
-[AVAssetCustomURLBridgeForNSURLSession _unregisterRequestForDataTask:];
```
