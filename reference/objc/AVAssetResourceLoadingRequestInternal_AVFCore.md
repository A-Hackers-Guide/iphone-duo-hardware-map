# `AVAssetResourceLoadingRequestInternal`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 23 instance variables, 0 properties, 0 instance methods, 0 class methods

## Instance variables

```
@"AVWeakReference" weakReference;
@"AVWeakReference" weakReferenceToResourceLoader;
^{OpaqueFigCustomURLLoader=} customURLLoader;
^{OpaqueFigCustomURLHandler=} customURLHandler;
^{__CFDictionary=} requestInfo;
Q requestID;
@"AVDispatchOnce" responseInfoSentOnceToken;
@"NSMutableURLRequest" URLRequest;
@"NSObject<OS_dispatch_queue>" ivarAccessQueue;
@"NSURLResponse" response;
@"NSURLRequest" redirect;
@"NSObject<OS_dispatch_queue>" dataCachingQueue;
@"NSMutableData" cachedData;
@"NSDictionary" cachedContentInformation;
@"AVAssetResourceLoadingContentInformationRequest" contentInformationRequest;
@"AVAssetResourceLoadingDataRequest" dataRequest;
i finished;
i cancelled;
i sentContentInfo;
@? streamingKeyRequestCompletionHandler;
^{OpaqueFigCPECryptor=} figCryptor;
@"AVAssetResourceLoadingRequestor" requestor;
Q cryptorKeyRequestID;
```
