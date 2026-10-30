# `NWURLLoaderHTTP`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NWURLLoader`
- 39 instance variables, 9 properties, 16 instance methods, 0 class methods

## Instance variables

```
B _pendingErrorFromFailedConnection;
B _inContinueLoading;
B _inResend;
B _ready;
B _readingResponseHeader;
B _receivedResponseHeader;
B _pendingCompletion;
B _protocolSwitched;
B _becameStream;
B _cancelled;
B _allowCaching;
B _loadingFromCache;
B _revalidateCachedResponse;
B _requestCompleteInternal;
B _requireH1;
B _hasCustomProxyConfigs;
c _preConnectedRetryCount;
C _channelFlowRetryCount;
@"NSURLRequest" _request;
q _bodyKnownSize;
@"NWURLSessionTaskConfiguration" _configuration;
@"<NWURLLoaderClient>" _client;
@"NSObject<OS_dispatch_queue>" _queue;
@"<NWURLSessionRequestBodyProvider>" _requestBodyProvider;
@"NWConcrete_nw_connection" _connection;
@"NSObject<OS_nw_content_context>" _requestContext;
@"NWURLError" _pendingError;
@"NWURLLoaderCache" _cache;
@"NSCachedURLResponse" _cachedResponseFound;
Q _cachedResponseDataOffset;
@"NSCachedURLResponse" _cachedResponseToStore;
@"NSString" _multipartBoundary;
@? _responseCompletionHandler;
@? _requestCompletionHandler;
@"NSObject<OS_nw_protocol_metadata>" _httpConnectionMetadata;
^v _responseStallTimer;
@"NSObject<OS_nw_http_fields>" _trailerFieldsInternal;
@"NSObject<OS_sec_trust>" _peerTrustInternal;
@"NWURLBackgroundScheduler" _scheduler;
```

## Properties

```
@property (T@"NSString",R,N) multipartMixedReplaceBoundary;
@property (T@"NSObject<OS_sec_trust>",R,N) peerTrust;
@property (TB,R,N) requestComplete;
@property (T@"NSObject<OS_nw_http_fields>",R,N) trailerFields;
@property (T@"NWConcrete_nw_connection",R,N) underlyingConnection;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[NWURLLoaderHTTP start:];
-[NWURLLoaderHTTP allowsWriteAfterBecomingStream];
-[NWURLLoaderHTTP peerTrust];
-[NWURLLoaderHTTP canHandleRedirectionToRequest:];
-[NWURLLoaderHTTP underlyingConnection];
-[NWURLLoaderHTTP stop];
-[NWURLLoaderHTTP writeData:complete:completionHandler:];
-[NWURLLoaderHTTP updateClient:];
-[NWURLLoaderHTTP takeCachedResponse];
-[NWURLLoaderHTTP restartStallTimer:];
-[NWURLLoaderHTTP readDataOfMinimumIncompleteLength:maximumLength:completionHandler:];
-[NWURLLoaderHTTP trailerFields];
-[NWURLLoaderHTTP multipartMixedReplaceBoundary];
-[NWURLLoaderHTTP notifyRequestCompletion:];
-[NWURLLoaderHTTP requestComplete];
-[NWURLLoaderHTTP readResponse:];
```
