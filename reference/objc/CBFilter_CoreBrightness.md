# `CBFilter`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_os_log>" _logHandle;
@"NSObject<OS_dispatch_queue>" _notificationQueue;
@? _notificationBlock;
```

## Instance methods

```
-[CBFilter copyPropertyForKey:];
-[CBFilter sendNotificationForKey:andValue:];
-[CBFilter setProperty:forKey:];
-[CBFilter registerNotificationBlock:];
-[CBFilter filterEvent:];
-[CBFilter unregisterNotificationBlock];
-[CBFilter filterEvents:];
-[CBFilter forgetDataForService:];
-[CBFilter scheduleWithDispatchQueue:];
-[CBFilter unscheduleWithDispatchQueue:];
```
