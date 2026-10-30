# `FigCapturePowerMonitor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 2 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _notificationQueue;
i _registrationToken;
@? _torchHandler;
^{OpaqueFigSimpleMutex=} _lock;
f _maxTorchLevel;
I _powerPressureLevel;
```

## Properties

```
@property (Tf,R) maxTorchLevel;
@property (TI,R) powerPressureLevel;
```

## Class methods

```
+[FigCapturePowerMonitor initialize];
```

## Instance methods

```
-[FigCapturePowerMonitor init];
-[FigCapturePowerMonitor dealloc];
-[FigCapturePowerMonitor maxTorchLevel];
-[FigCapturePowerMonitor powerPressureLevel];
-[FigCapturePowerMonitor setPowerHandler:];
```
