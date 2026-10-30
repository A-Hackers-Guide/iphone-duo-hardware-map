# `AVAssetResourceLoader`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSURLAuthenticationChallengeSender`
- 1 instance variables, 12 properties, 47 instance methods, 0 class methods

## Instance variables

```
@"AVAssetResourceLoaderInternal" _resourceLoader;
```

## Properties

```
@property (TB,N) preloadsEligibleContentKeys;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<NSURLSessionDataDelegate>",R,N) URLSessionDataDelegate;
@property (T@"NSOperationQueue",R,N) URLSessionDataDelegateQueue;
@property (T@"NSURLSession",&,N) URLSession;
@property (TB,N) sendsCommonMediaClientDataAsHTTPHeaders;
@property (TQ,N) allowedCommonMediaClientDataKeys;
@property (T@"<AVAssetResourceLoaderDelegate>",R,W,N) delegate;
@property (T@"NSObject<OS_dispatch_queue>",R,N) delegateQueue;
```

## Instance methods

```
-[AVAssetResourceLoader setDelegate:queue:];
-[AVAssetResourceLoader URLSession];
-[AVAssetResourceLoader asset];
-[AVAssetResourceLoader init];
-[AVAssetResourceLoader dealloc];
-[AVAssetResourceLoader continueWithoutCredentialForAuthenticationChallenge:];
-[AVAssetResourceLoader useCredential:forAuthenticationChallenge:];
-[AVAssetResourceLoader cancelAuthenticationChallenge:];
-[AVAssetResourceLoader delegate];
-[AVAssetResourceLoader stateQueue];
-[AVAssetResourceLoader delegateQueue];
-[AVAssetResourceLoader cancelLoading];
-[AVAssetResourceLoader setURLSession:];
-[AVAssetResourceLoader performDefaultHandlingForAuthenticationChallenge:];
-[AVAssetResourceLoader rejectProtectionSpaceAndContinueWithChallenge:];
-[AVAssetResourceLoader cacheContentInformation:forURL:];
-[AVAssetResourceLoader setPreloadsEligibleContentKeys:];
-[AVAssetResourceLoader cachedContentInformationForURL:];
-[AVAssetResourceLoader initWithURLRequestHelper:asset:];
-[AVAssetResourceLoader URLRequestHelper];
-[AVAssetResourceLoader URLSessionDataDelegate];
-[AVAssetResourceLoader URLSessionDataDelegateQueue];
-[AVAssetResourceLoader _authHandler];
-[AVAssetResourceLoader _cancelRequest:requestID:];
-[AVAssetResourceLoader _cancelRequestWithKey:fallbackHandler:];
-[AVAssetResourceLoader _copyContentKeySessionCustomURLHandler];
-[AVAssetResourceLoader _customURLHandler];
-[AVAssetResourceLoader _customURLLoader];
-[AVAssetResourceLoader _getDelegateOnStateQueue];
-[AVAssetResourceLoader _getDelegateQueueOnStateQueue];
-[AVAssetResourceLoader _handleRequest:requestID:willHandleRequest:];
-[AVAssetResourceLoader _issueLoadingRequestWithKey:loadingRequest:isRenewalRequest:fallbackHandler:];
-[AVAssetResourceLoader _noteFinishingOfRequest:];
-[AVAssetResourceLoader _performDelegateCallbackSynchronouslyIfCurrentDelegateQueueIsQueue:delegateCallbackBlock:];
-[AVAssetResourceLoader _performDelegateSelector:withObject:representingNewRequest:key:fallbackHandler:];
-[AVAssetResourceLoader _poseAuthenticationChallengeWithKey:challenge:fallbackHandler:];
-[AVAssetResourceLoader _poseAuthenticationChallengeWithRequestInfo:requestID:challenge:];
-[AVAssetResourceLoader _sendAuthResponseForChallenge:disposition:credential:error:];
-[AVAssetResourceLoader _setContentKeySessionCustomURLHandler:];
-[AVAssetResourceLoader _setDelegateOnStateQueue:];
-[AVAssetResourceLoader allowedCommonMediaClientDataKeys];
-[AVAssetResourceLoader initWithURLRequestHelper:asset:remoteCustomURLHandlerContext:];
-[AVAssetResourceLoader preloadsEligibleContentKeys];
-[AVAssetResourceLoader remoteCustomURLHandlerContextForPID:];
-[AVAssetResourceLoader sendsCommonMediaClientDataAsHTTPHeaders];
-[AVAssetResourceLoader setAllowedCommonMediaClientDataKeys:];
-[AVAssetResourceLoader setSendsCommonMediaClientDataAsHTTPHeaders:];
```
