# `FigCapturePowerLogMissingCameraStopEventObserver`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FigCaptureDisplayLayoutObserver`
- 6 instance variables, 4 properties, 2 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _observerQueue;
B _observing;
@"FigCaptureDisplayLayoutMonitor" _layoutMonitor;
@"NSObject<OS_dispatch_source>" _cameraAppStreamingTimer;
B _previousLayoutHasForegroundCameraApp;
@"NSDateFormatter" _eventDateFormatter;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FigCapturePowerLogMissingCameraStopEventObserver layoutMonitor:didUpdateLayout:];
-[FigCapturePowerLogMissingCameraStopEventObserver dealloc];
```
