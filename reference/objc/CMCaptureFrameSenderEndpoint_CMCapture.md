# `CMCaptureFrameSenderEndpoint`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_xpc_object>" _endpoint;
@"NSString" _endpointUniqueID;
@"NSString" _endpointType;
@"NSData" _endpointAuditToken;
@"NSData" _endpointProxyAuditToken;
i _endpointPID;
i _endpointProxyPID;
@"NSString" _endpointCameraUniqueID;
```

## Properties

```
@property (T@"NSObject<OS_xpc_object>",R,C,V_endpoint) endpoint;
@property (T@"NSString",R,C,V_endpointUniqueID) endpointUniqueID;
@property (T@"NSString",R,C,V_endpointType) endpointType;
@property (Ti,R,V_endpointPID) endpointPID;
@property (Ti,R,V_endpointProxyPID) endpointProxyPID;
@property (T@"NSData",R,C,V_endpointAuditToken) endpointAuditToken;
@property (T@"NSData",R,C,V_endpointProxyAuditToken) endpointProxyAuditToken;
@property (T@"NSString",R,C,V_endpointCameraUniqueID) endpointCameraUniqueID;
```

## Instance methods

```
-[CMCaptureFrameSenderEndpoint endpointType];
-[CMCaptureFrameSenderEndpoint initWithDictionary:];
-[CMCaptureFrameSenderEndpoint dealloc];
-[CMCaptureFrameSenderEndpoint endpoint];
-[CMCaptureFrameSenderEndpoint description];
-[CMCaptureFrameSenderEndpoint endpointAuditToken];
-[CMCaptureFrameSenderEndpoint endpointCameraUniqueID];
-[CMCaptureFrameSenderEndpoint endpointPID];
-[CMCaptureFrameSenderEndpoint endpointProxyAuditToken];
-[CMCaptureFrameSenderEndpoint endpointProxyPID];
-[CMCaptureFrameSenderEndpoint endpointUniqueID];
```
