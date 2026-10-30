# `CMCaptureFrameSenderClient`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 2 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_xpc_object>" _connection;
@"NSObject<OS_dispatch_queue>" _queue;
i _pid;
B _connectionIsValid;
```

## Properties

```
@property (TB,R,V_connectionIsValid) connectionIsValid;
@property (Ti,R,V_pid) pid;
```

## Instance methods

```
-[CMCaptureFrameSenderClient _invalidate];
-[CMCaptureFrameSenderClient dealloc];
-[CMCaptureFrameSenderClient pid];
-[CMCaptureFrameSenderClient initWithConnection:queue:];
-[CMCaptureFrameSenderClient connectionIsValid];
-[CMCaptureFrameSenderClient sendXCPSampleBuffer:];
```
