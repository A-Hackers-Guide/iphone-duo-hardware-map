# `FigCaptureSourceVibeMitigation`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 0 properties, 2 instance methods, 1 class methods

## Instance variables

```
@"NSMutableArray" _positions;
@"NSMutableArray" _deviceTypes;
@"NSObject<OS_dispatch_queue>" _vibeMitigationQueue;
i _deviceVendorClientID;
@"BWFigCaptureDevice" _device;
@"NSArray" _streamsArray;
@"NSObject<OS_dispatch_source>" _timer;
@"FigStateMachine" _stateMachine;
I _hapticDuration;
B _deviceBecameUnavailable;
B _mitigationWhileCameraStreamingSupported;
```

## Class methods

```
+[FigCaptureSourceVibeMitigation initialize];
```

## Instance methods

```
-[FigCaptureSourceVibeMitigation dealloc];
-[FigCaptureSourceVibeMitigation initWithFigCaptureSourceBackings:];
```
