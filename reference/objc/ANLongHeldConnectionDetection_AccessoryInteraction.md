# `ANLongHeldConnectionDetection`

- Image: [`/System/Library/PrivateFrameworks/AccessoryInteraction.framework/AccessoryInteraction`](../userland/System__Library__PrivateFrameworks__AccessoryInteraction.framework__AccessoryInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 0 properties, 7 instance methods, 2 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"<ANSystemUtilsProtocol>" _systemUtils;
@"ANSettings" _settings;
@"LSApplicationWorkspace" _applicationWorkspace;
B _isInternalInstall;
B _isInPrivateVehicle;
```

## Class methods

```
+[ANLongHeldConnectionDetection userAction30msTimeForUserStats:];
+[ANLongHeldConnectionDetection total30msTimeForUserStats:];
```

## Instance methods

```
-[ANLongHeldConnectionDetection dealloc];
-[ANLongHeldConnectionDetection didReceiveUserStats:forDevice:];
-[ANLongHeldConnectionDetection didUpdateVehicularState:];
-[ANLongHeldConnectionDetection initWithQueue:systemUtils:settings:applicationWorkspace:isInternalInstall:];
-[ANLongHeldConnectionDetection isIssueDetectedInUserStats:deviceUUID:];
-[ANLongHeldConnectionDetection showNotificationForDeviceUUID:deviceName:timestamp:userStats:];
-[ANLongHeldConnectionDetection triggerAutoBugCaptureForDeviceUUID:];
```
