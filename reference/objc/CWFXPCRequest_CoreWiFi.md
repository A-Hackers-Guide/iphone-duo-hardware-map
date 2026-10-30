# `CWFXPCRequest`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CWFAsyncBlockOperation`
- 10 instance variables, 10 properties, 24 instance methods, 0 class methods

## Instance variables

```
@? _response;
B _isSubrequest;
B _alreadyResponded;
@"NSUUID" _UUID;
q _type;
@"CWFRequestParameters" _requestParameters;
@"NSDate" _receivedAt;
@"NSDictionary" _info;
@? _cancelationHandler;
@? _forwardToCompletionBlock;
```

## Properties

```
@property (TB,N,V_alreadyResponded) alreadyResponded;
@property (T@?,C,V_forwardToCompletionBlock) forwardToCompletionBlock;
@property (T@"NSUUID",C,V_UUID) UUID;
@property (Tq,V_type) type;
@property (T@"CWFRequestParameters",C,V_requestParameters) requestParameters;
@property (T@"NSDate",C,V_receivedAt) receivedAt;
@property (T@"NSDictionary",C,V_info) info;
@property (T@?,C) response;
@property (T@?,C,V_cancelationHandler) cancelationHandler;
@property (TB,V_isSubrequest) isSubrequest;
```

## Instance methods

```
-[CWFXPCRequest requestParameters];
-[CWFXPCRequest isSubrequest];
-[CWFXPCRequest setRequestParameters:];
-[CWFXPCRequest setResponse:];
-[CWFXPCRequest setCompletionBlock:];
-[CWFXPCRequest info];
-[CWFXPCRequest init];
-[CWFXPCRequest setInfo:];
-[CWFXPCRequest setForwardToCompletionBlock:];
-[CWFXPCRequest setUUID:];
-[CWFXPCRequest UUID];
-[CWFXPCRequest setReceivedAt:];
-[CWFXPCRequest alreadyResponded];
-[CWFXPCRequest setAlreadyResponded:];
-[CWFXPCRequest cancelationHandler];
-[CWFXPCRequest setType:];
-[CWFXPCRequest type];
-[CWFXPCRequest setIsSubrequest:];
-[CWFXPCRequest description];
-[CWFXPCRequest receivedAt];
-[CWFXPCRequest cancel];
-[CWFXPCRequest forwardToCompletionBlock];
-[CWFXPCRequest setCancelationHandler:];
-[CWFXPCRequest response];
```
