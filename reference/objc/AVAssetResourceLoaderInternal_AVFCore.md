# `AVAssetResourceLoaderInternal`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 20 instance variables, 0 properties, 0 instance methods, 0 class methods

## Instance variables

```
@"AVAssetClientURLRequestHelper" URLRequestHelper;
@"AVWeakReference" weakReferenceToAsset;
@"NSObject<OS_dispatch_queue>" stateQueue;
@"AVWeakReference" weakReferenceToDelegate;
@"NSObject<OS_dispatch_queue>" delegateQueue;
^{OpaqueFigCustomURLLoader=} customURLLoader;
^{OpaqueFigCustomURLHandler=} customURLHandler;
^{OpaqueFigCustomURLHandler=} authHandler;
^{OpaqueFigCustomURLHandler=} contentKeySessionCustomURLHandler;
^{OpaqueFigXPCRemoteClient=} remoteHandlerXPCRemoteClient;
i loadingCancelled;
@"NSMutableDictionary" pendingRequests;
@"NSObject<OS_dispatch_queue>" contentInformationCachingQueue;
@"NSMutableDictionary" contentInformationCache;
B preloadsEligibleContentKeys;
Q allowedCMCDKeys;
B sendsCMCDKeys;
@"NSURLSession" URLSession;
@"AVAssetCustomURLBridgeForNSURLSession" bridgeBetweenHandlerAndSession;
@"NSOperationQueue" URLSessionOperationQueue;
```
