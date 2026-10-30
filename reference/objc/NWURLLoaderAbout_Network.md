# `NWURLLoaderAbout`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NWURLLoader`
- 1 instance variables, 9 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSURL" _URL;
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
-[NWURLLoaderAbout start:];
-[NWURLLoaderAbout allowsWriteAfterBecomingStream];
-[NWURLLoaderAbout peerTrust];
-[NWURLLoaderAbout canHandleRedirectionToRequest:];
-[NWURLLoaderAbout underlyingConnection];
-[NWURLLoaderAbout stop];
-[NWURLLoaderAbout writeData:complete:completionHandler:];
-[NWURLLoaderAbout updateClient:];
-[NWURLLoaderAbout takeCachedResponse];
-[NWURLLoaderAbout readDataOfMinimumIncompleteLength:maximumLength:completionHandler:];
-[NWURLLoaderAbout trailerFields];
-[NWURLLoaderAbout multipartMixedReplaceBoundary];
-[NWURLLoaderAbout notifyRequestCompletion:];
-[NWURLLoaderAbout requestComplete];
-[NWURLLoaderAbout readResponse:];
```
