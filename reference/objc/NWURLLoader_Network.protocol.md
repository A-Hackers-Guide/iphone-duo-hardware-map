# `NWURLLoader` (protocol)

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 5 properties, 15 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",R,N) multipartMixedReplaceBoundary;
@property (T@"NSObject<OS_sec_trust>",R,N) peerTrust;
@property (TB,R,N) requestComplete;
@property (T@"NSObject<OS_nw_http_fields>",R,N) trailerFields;
@property (T@"NSObject<OS_nw_connection>",R,N) underlyingConnection;
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
```
