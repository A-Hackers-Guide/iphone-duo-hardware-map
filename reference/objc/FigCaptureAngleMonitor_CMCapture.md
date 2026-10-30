# `FigCaptureAngleMonitor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 2 properties, 6 instance methods, 1 class methods

## Instance variables

```
@? _angleHandler;
^{OpaqueFigSimpleMutex=} _angleNotificationLock;
f _normalizedAngle;
@"NSOperationQueue" _queue;
B _started;
B _active;
@"CMAngleManager" _angleManager;
```

## Properties

```
@property (Tf,R,N) normalizedAngle;
@property (TB,R,N) active;
```

## Class methods

```
+[FigCaptureAngleMonitor initialize];
```

## Instance methods

```
-[FigCaptureAngleMonitor startMonitoring];
-[FigCaptureAngleMonitor active];
-[FigCaptureAngleMonitor dealloc];
-[FigCaptureAngleMonitor stopMonitoring];
-[FigCaptureAngleMonitor normalizedAngle];
-[FigCaptureAngleMonitor initWithAngleHandler:];
```
