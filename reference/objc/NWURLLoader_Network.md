# `NWURLLoader`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NWURLLoader`, `NSURLProtocolClient`
- 17 instance variables, 9 properties, 23 instance methods, 0 class methods

## Instance variables

```
B _receivedResponse;
B _complete;
@"NSURLRequest" _request;
@"NWURLSessionTaskConfiguration" _configuration;
@"<NWURLLoaderClient>" _client;
@"NSObject<OS_dispatch_queue>" _queue;
# _protocolClass;
@"NSURLCache" _cache;
@"NSURLProtocol" _protocol;
Q _cacheStoragePolicy;
@"NSObject<OS_dispatch_data>" _dataToCache;
@"NSCachedURLResponse" _cachedResponseInternal;
Q _maxItemSizeToCache;
@? _awaitingResponse;
@"NSURLResponse" _response;
@"NWURLSessionReadRequest" _readRequest;
@"NWURLError" _error;
```

## Properties

```
@property (T@"NSString",R,N) multipartMixedReplaceBoundary;
@property (T@"NSObject<OS_sec_trust>",R,N) peerTrust;
@property (TB,R,N) requestComplete;
@property (T@"NSObject<OS_nw_http_fields>",R,N) trailerFields;
@property (T@"NSObject<OS_nw_connection>",R,N) underlyingConnection;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[NWURLLoader start:];
-[NWURLLoader allowsWriteAfterBecomingStream];
-[NWURLLoader peerTrust];
-[NWURLLoader canHandleRedirectionToRequest:];
-[NWURLLoader underlyingConnection];
-[NWURLLoader stop];
-[NWURLLoader writeData:complete:completionHandler:];
-[NWURLLoader updateClient:];
-[NWURLLoader takeCachedResponse];
-[NWURLLoader readDataOfMinimumIncompleteLength:maximumLength:completionHandler:];
-[NWURLLoader trailerFields];
-[NWURLLoader multipartMixedReplaceBoundary];
-[NWURLLoader notifyRequestCompletion:];
-[NWURLLoader requestComplete];
-[NWURLLoader readResponse:];
-[NWURLLoader URLProtocol:cachedResponseIsValid:];
-[NWURLLoader URLProtocol:didFailWithError:];
-[NWURLLoader URLProtocol:didReceiveAuthenticationChallenge:];
-[NWURLLoader URLProtocol:wasRedirectedToRequest:redirectResponse:];
-[NWURLLoader URLProtocol:didCancelAuthenticationChallenge:];
-[NWURLLoader URLProtocol:didLoadData:];
-[NWURLLoader URLProtocol:didReceiveResponse:cacheStoragePolicy:];
-[NWURLLoader URLProtocolDidFinishLoading:];
```
