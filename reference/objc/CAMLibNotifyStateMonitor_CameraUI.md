# `CAMLibNotifyStateMonitor`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 7 properties, 15 instance methods, 0 class methods

## Instance variables

```
B __notifyRegistered;
B __monitoredValue;
i __notifyToken;
r* __notifyName;
@"NSObject<OS_dispatch_queue>" __notifyQueue;
@? __updateHandler;
```

## Properties

```
@property (Tr*,R,N,V__notifyName) _notifyName;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V__notifyQueue) _notifyQueue;
@property (T@?,R,N,V__updateHandler) _updateHandler;
@property (Ti,N,V__notifyToken) _notifyToken;
@property (TB,N,V__notifyRegistered) _notifyRegistered;
@property (TB,N,V__monitoredValue) _monitoredValue;
@property (TB,R) monitoredValue;
```

## Instance methods

```
-[CAMLibNotifyStateMonitor dealloc];
-[CAMLibNotifyStateMonitor setNeedsUpdate];
-[CAMLibNotifyStateMonitor _notifyQueue];
-[CAMLibNotifyStateMonitor _monitoredValue];
-[CAMLibNotifyStateMonitor _notifyName];
-[CAMLibNotifyStateMonitor _notifyRegistered];
-[CAMLibNotifyStateMonitor _notifyToken];
-[CAMLibNotifyStateMonitor _startMonitoringIfNeeded];
-[CAMLibNotifyStateMonitor _updateHandler];
-[CAMLibNotifyStateMonitor _updateMonitoredValue];
-[CAMLibNotifyStateMonitor initWithNotificationName:queue:updateHandler:];
-[CAMLibNotifyStateMonitor monitoredValue];
-[CAMLibNotifyStateMonitor set_monitoredValue:];
-[CAMLibNotifyStateMonitor set_notifyRegistered:];
-[CAMLibNotifyStateMonitor set_notifyToken:];
```
