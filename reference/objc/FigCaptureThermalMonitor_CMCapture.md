# `FigCaptureThermalMonitor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 2 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _notificationQueue;
i _registrationToken;
@? _thermalHandler;
^{OpaqueFigSimpleMutex=} _thermalNotificationLock;
f _maxTorchLevel;
i _thermalLevel;
```

## Properties

```
@property (Tf,R) maxTorchLevel;
@property (Ti,R) thermalLevel;
```

## Class methods

```
+[FigCaptureThermalMonitor initialize];
```

## Instance methods

```
-[FigCaptureThermalMonitor init];
-[FigCaptureThermalMonitor dealloc];
-[FigCaptureThermalMonitor thermalLevel];
-[FigCaptureThermalMonitor maxTorchLevel];
-[FigCaptureThermalMonitor setThermalHandler:];
```
