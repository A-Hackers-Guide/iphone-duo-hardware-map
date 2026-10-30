# `CMCaptureFrameSenderService`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 24 instance variables, 0 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"NSString" _endpointUniqueID;
@"NSString" _endpointType;
@"NSString" _endpointCameraUniqueID;
@"NSData" _endpointAuditToken;
@"NSData" _endpointProxyAuditToken;
i _endpointPID;
i _endpointProxyPID;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSObject<OS_xpc_object>" _listener;
@"NSObject<OS_xpc_object>" _endpoint;
@"NSMutableArray" _clients;
@"NSObject<OS_dispatch_queue>" _clientQueue;
^{__CVPixelBufferPool=} _sendingPixelBufferPool;
^{opaqueCMFormatDescription=} _sendingSampleBufferFormatDescription;
^{OpaqueVTPixelTransferSession=} _sendingPixelTransferSession;
^{OpaqueVTPixelRotationSession=} _sendingPixelRotationSession;
@"NSObject<OS_dispatch_source>" _reapSendingPixelTransferSessionTimer;
d _sendingPixelBufferPoolAgeOutTime;
Q _sendingPixelBufferWidth;
Q _sendingPixelBufferHeight;
I _sendingPixelBufferPixelFormatType;
i _crossPlatformRotationDegrees;
i _sendingPixelBufferPoolSize;
B _sendingPixelBufferIsAWeirdSize;
```

## Class methods

```
+[CMCaptureFrameSenderService initialize];
```

## Instance methods

```
-[CMCaptureFrameSenderService _addConnection:];
-[CMCaptureFrameSenderService init];
-[CMCaptureFrameSenderService dealloc];
-[CMCaptureFrameSenderService _cleanupSendingPixelBufferMachinery];
-[CMCaptureFrameSenderService _newSampleBufferToSendFromSampleBuffer:];
-[CMCaptureFrameSenderService initWithEndpointType:];
-[CMCaptureFrameSenderService initWithEndpointType:endpointCameraUniqueID:];
-[CMCaptureFrameSenderService initWithEndpointType:endpointPID:endpointProxyPID:endpointAuditToken:endpointProxyAuditToken:endpointCameraUniqueID:];
-[CMCaptureFrameSenderService sendFrame:];
```
