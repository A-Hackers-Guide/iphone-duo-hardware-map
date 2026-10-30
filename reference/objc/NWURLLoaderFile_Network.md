# `NWURLLoaderFile`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NWURLLoader`
- 6 instance variables, 9 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSURL" _URL;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSNumber" _expectedDevice;
Q _fileSize;
@"NSObject<OS_dispatch_io>" _io;
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
-[NWURLLoaderFile start:];
-[NWURLLoaderFile allowsWriteAfterBecomingStream];
-[NWURLLoaderFile peerTrust];
-[NWURLLoaderFile canHandleRedirectionToRequest:];
-[NWURLLoaderFile underlyingConnection];
-[NWURLLoaderFile stop];
-[NWURLLoaderFile writeData:complete:completionHandler:];
-[NWURLLoaderFile updateClient:];
-[NWURLLoaderFile takeCachedResponse];
-[NWURLLoaderFile readDataOfMinimumIncompleteLength:maximumLength:completionHandler:];
-[NWURLLoaderFile trailerFields];
-[NWURLLoaderFile multipartMixedReplaceBoundary];
-[NWURLLoaderFile notifyRequestCompletion:];
-[NWURLLoaderFile requestComplete];
-[NWURLLoaderFile readResponse:];
```
