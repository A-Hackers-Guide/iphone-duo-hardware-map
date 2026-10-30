# `NWURLLoaderTCP`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NWURLLoader`
- 13 instance variables, 9 properties, 15 instance methods, 0 class methods

## Instance variables

```
B _ready;
B _cancelled;
B _TLS;
B _addedTLS;
@"NSString" _hostname;
q _port;
@"NWURLSessionTaskConfiguration" _configuration;
@"<NWURLLoaderClient>" _client;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSMutableArray" _pendingWork;
@"NSObject<OS_nw_connection>" _connection;
@"NWURLError" _error;
@"NSObject<OS_sec_trust>" _peerTrustInternal;
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
-[NWURLLoaderTCP start:];
-[NWURLLoaderTCP allowsWriteAfterBecomingStream];
-[NWURLLoaderTCP peerTrust];
-[NWURLLoaderTCP canHandleRedirectionToRequest:];
-[NWURLLoaderTCP underlyingConnection];
-[NWURLLoaderTCP stop];
-[NWURLLoaderTCP writeData:complete:completionHandler:];
-[NWURLLoaderTCP updateClient:];
-[NWURLLoaderTCP takeCachedResponse];
-[NWURLLoaderTCP readDataOfMinimumIncompleteLength:maximumLength:completionHandler:];
-[NWURLLoaderTCP trailerFields];
-[NWURLLoaderTCP multipartMixedReplaceBoundary];
-[NWURLLoaderTCP notifyRequestCompletion:];
-[NWURLLoaderTCP requestComplete];
-[NWURLLoaderTCP readResponse:];
```
