# `CMCaptureFrameReceiver`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 5 properties, 7 instance methods, 2 class methods

## Instance variables

```
@"NSString" _endpointUniqueID;
@? _frameReceiverHandler;
@"NSObject<OS_xpc_object>" _connection;
@"NSObject<OS_dispatch_queue>" _queue;
i _endpointPID;
i _endpointProxyPID;
@"NSData" _endpointAuditToken;
@"NSData" _endpointProxyAuditToken;
B _connectionIsValid;
```

## Properties

```
@property (T@"NSString",R,C,V_endpointUniqueID) endpointUniqueID;
@property (Ti,R,V_endpointPID) endpointPID;
@property (Ti,R,V_endpointProxyPID) endpointProxyPID;
@property (T@"NSData",R,C,V_endpointAuditToken) endpointAuditToken;
@property (T@"NSData",R,C,V_endpointProxyAuditToken) endpointProxyAuditToken;
```

## Class methods

```
+[CMCaptureFrameReceiver initialize];
+[CMCaptureFrameReceiver availableFrameSenderEndpointsByPID];
```

## Instance methods

```
-[CMCaptureFrameReceiver dealloc];
-[CMCaptureFrameReceiver endpointAuditToken];
-[CMCaptureFrameReceiver endpointPID];
-[CMCaptureFrameReceiver endpointProxyAuditToken];
-[CMCaptureFrameReceiver endpointProxyPID];
-[CMCaptureFrameReceiver endpointUniqueID];
-[CMCaptureFrameReceiver initWithFrameSenderServerEndpoint:frameReceiverHandler:];
```
