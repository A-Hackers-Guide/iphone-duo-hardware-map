# `CBContainer`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_os_log>" _logHandle;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSObject<OS_dispatch_queue>" _notificationQueue;
@? _notificationBlock;
```

## Instance methods

```
-[CBContainer registerNotificationBlock:];
-[CBContainer dealloc];
-[CBContainer unregisterNotificationBlock];
-[CBContainer scheduleWithDispatchQueue:];
-[CBContainer unscheduleWithDispatchQueue:];
```
