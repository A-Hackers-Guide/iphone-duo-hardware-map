# `VTTriggerEventMonitorManager`

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"NSMutableSet" _connections;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Class methods

```
+[VTTriggerEventMonitorManager sharedManager];
```

## Instance methods

```
-[VTTriggerEventMonitorManager init];
-[VTTriggerEventMonitorManager addConnection:];
-[VTTriggerEventMonitorManager removeConnection:];
-[VTTriggerEventMonitorManager notifyEarlyDetect];
-[VTTriggerEventMonitorManager notifyVoiceTrigger];
```
