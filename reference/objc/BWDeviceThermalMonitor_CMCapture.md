# `BWDeviceThermalMonitor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 1 properties, 4 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _notificationQueue;
i _registrationToken;
@? _thermalHandler;
^{OpaqueFigSimpleMutex=} _thermalNotificationLock;
i _thermalLevel;
```

## Properties

```
@property (Ti,R) thermalLevel;
```

## Class methods

```
+[BWDeviceThermalMonitor initialize];
```

## Instance methods

```
-[BWDeviceThermalMonitor init];
-[BWDeviceThermalMonitor dealloc];
-[BWDeviceThermalMonitor thermalLevel];
-[BWDeviceThermalMonitor setThermalHandler:];
```
