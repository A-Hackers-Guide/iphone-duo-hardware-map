# `AVAssetResourceLoadingRequest`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVAssetResourceLoaderRequest`
- 1 instance variables, 12 properties, 48 instance methods, 1 class methods

## Instance variables

```
@"AVAssetResourceLoadingRequestInternal" _loadingRequest;
```

## Properties

```
@property (T@"NSURLRequest",R,N) request;
@property (TB,R,N,GisFinished) finished;
@property (TB,R,N,GisCancelled) cancelled;
@property (T@"AVAssetResourceLoadingContentInformationRequest",R,N) contentInformationRequest;
@property (T@"AVAssetResourceLoadingDataRequest",R,N) dataRequest;
@property (T@"NSURLResponse",C,N) response;
@property (T@"NSURLRequest",C,N) redirect;
@property (T@"AVAssetResourceLoadingRequestor",R,N) requestor;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[AVAssetResourceLoadingRequest _selectorForInformingDelegateOfCancellationByFig];
```

## Instance methods

```
-[AVAssetResourceLoadingRequest _resourceLoader];
-[AVAssetResourceLoadingRequest isFinished];
-[AVAssetResourceLoadingRequest setResponse:];
-[AVAssetResourceLoadingRequest _requestID];
-[AVAssetResourceLoadingRequest finished];
-[AVAssetResourceLoadingRequest init];
-[AVAssetResourceLoadingRequest dealloc];
-[AVAssetResourceLoadingRequest isCancelled];
-[AVAssetResourceLoadingRequest request];
-[AVAssetResourceLoadingRequest _weakReference];
-[AVAssetResourceLoadingRequest _requestInfo];
-[AVAssetResourceLoadingRequest _shouldInformDelegateOfFigCancellation];
-[AVAssetResourceLoadingRequest description];
-[AVAssetResourceLoadingRequest _performCancellationByClient];
-[AVAssetResourceLoadingRequest requestor];
-[AVAssetResourceLoadingRequest response];
-[AVAssetResourceLoadingRequest _appendToCachedData:];
-[AVAssetResourceLoadingRequest _cacheContentInformation:];
-[AVAssetResourceLoadingRequest _canSetOrUseCachedContentInformation];
-[AVAssetResourceLoadingRequest _contentKeySessionIsAttached];
-[AVAssetResourceLoadingRequest _copyContentKeySessionCustomURLHandler];
-[AVAssetResourceLoadingRequest _customURLHandler];
-[AVAssetResourceLoadingRequest _customURLLoader];
-[AVAssetResourceLoadingRequest _ensureResponseInfoSentToCustomURLHandler];
-[AVAssetResourceLoadingRequest _getAndClearCachedData];
-[AVAssetResourceLoadingRequest _isRequestForContentKey];
-[AVAssetResourceLoadingRequest _sendDataToCustomURLHandler:];
-[AVAssetResourceLoadingRequest _sendFinishLoadingToCustomURLHandler];
-[AVAssetResourceLoadingRequest _sendFinishLoadingToCustomURLHandlerWithError:];
-[AVAssetResourceLoadingRequest _sendResponseInfoToCustomURLHandler];
-[AVAssetResourceLoadingRequest _setContentInformationRequest:];
-[AVAssetResourceLoadingRequest _setDataRequest:];
-[AVAssetResourceLoadingRequest _tryToMarkAsCancelled];
-[AVAssetResourceLoadingRequest contentInformationRequest];
-[AVAssetResourceLoadingRequest dataRequest];
-[AVAssetResourceLoadingRequest finishLoading];
-[AVAssetResourceLoadingRequest finishLoadingWithError:];
-[AVAssetResourceLoadingRequest finishLoadingWithResponse:data:redirect:];
-[AVAssetResourceLoadingRequest forwardRequestToContentKeySession];
-[AVAssetResourceLoadingRequest generateStreamingContentKeyRequestDataAsynchronouslyForApp:contentIdentifier:options:completionHandler:];
-[AVAssetResourceLoadingRequest initWithResourceLoader:URL:httpRequestHeaders:requestOffset:requestLength:allowedContentTypes:figCryptor:cryptorKeyRequestID:];
-[AVAssetResourceLoadingRequest initWithResourceLoader:requestInfo:requestID:];
-[AVAssetResourceLoadingRequest keyRequestDataUsingCryptorForApp:contentIdentifier:options:performAsync:error:];
-[AVAssetResourceLoadingRequest persistentContentKeyFromKeyVendorResponse:options:error:];
-[AVAssetResourceLoadingRequest redirect];
-[AVAssetResourceLoadingRequest serializableRepresentation];
-[AVAssetResourceLoadingRequest setRedirect:];
-[AVAssetResourceLoadingRequest streamingContentKeyRequestDataForApp:contentIdentifier:options:error:];
```
