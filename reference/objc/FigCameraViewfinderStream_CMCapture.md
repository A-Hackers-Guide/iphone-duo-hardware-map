# `FigCameraViewfinderStream`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 0 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"FigDelegateStorage" _delegateStorage;
@"FigStateMachine" _stateMachine;
^{OpaqueFigEndpoint=} _endpoint;
^{OpaqueFigEndpointStream=} _stream;
^{OpaqueFigVirtualDisplaySource=} _displaySource;
@"FigCaptureFrameRateMonitor" _frameRateMonitor;
@ _endpointsChangedNotificationToken;
@ _streamsChangedNotificationToken;
```

## Class methods

```
+[FigCameraViewfinderStream initialize];
```

## Instance methods

```
-[FigCameraViewfinderStream setDelegate:queue:];
-[FigCameraViewfinderStream close];
-[FigCameraViewfinderStream init];
-[FigCameraViewfinderStream dealloc];
-[FigCameraViewfinderStream enqueueVideoSampleBuffer:];
-[FigCameraViewfinderStream openWithDestination:];
```
