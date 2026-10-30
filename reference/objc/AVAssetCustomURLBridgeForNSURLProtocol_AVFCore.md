# `AVAssetCustomURLBridgeForNSURLProtocol`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _requestIDToDownload;
^{OpaqueFigCustomURLHandler=} _handler;
@"NSObject<OS_dispatch_queue>" _callbackQueue;
```

## Instance methods

```
-[AVAssetCustomURLBridgeForNSURLProtocol reportSuccessfulURLLoad];
-[AVAssetCustomURLBridgeForNSURLProtocol _cancelRequestID:];
-[AVAssetCustomURLBridgeForNSURLProtocol _didReceiveResponse:response:];
-[AVAssetCustomURLBridgeForNSURLProtocol dealloc];
-[AVAssetCustomURLBridgeForNSURLProtocol _didFinish:error:];
-[AVAssetCustomURLBridgeForNSURLProtocol _cancelAndFinishRequest:error:];
-[AVAssetCustomURLBridgeForNSURLProtocol _willSendRequest:request:redirectionResponse:];
-[AVAssetCustomURLBridgeForNSURLProtocol _handleRequest:requestID:];
-[AVAssetCustomURLBridgeForNSURLProtocol initWithFigAsset:];
-[AVAssetCustomURLBridgeForNSURLProtocol _cancelPendingRequests];
-[AVAssetCustomURLBridgeForNSURLProtocol _didReceiveData:data:];
```
