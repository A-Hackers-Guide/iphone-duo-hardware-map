# `AVWaitForNotificationOrDeallocationOperation`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSOperation`
- Protocols: `AVObjectMonitoring`
- 8 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"AVWeakReference" _weakReferenceToSelf;
@"AVWeakReference" _weakReferenceToMonitoredObject;
@"NSObject<OS_dispatch_queue>" _operationStateSerializationQueue;
@"NSObject<OS_dispatch_semaphore>" _monitoringIsFinishedSemaphore;
@"NSArray" _notificationNames;
B _registeredForObjectNotifications;
B _started;
B _finished;
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
-[AVWaitForNotificationOrDeallocationOperation dealloc];
-[AVWaitForNotificationOrDeallocationOperation main];
-[AVWaitForNotificationOrDeallocationOperation cancel];
-[AVWaitForNotificationOrDeallocationOperation _registerForObjectNotifications];
-[AVWaitForNotificationOrDeallocationOperation _balanceMonitoringIsFinishedSemaphore];
-[AVWaitForNotificationOrDeallocationOperation _monitoredObject];
-[AVWaitForNotificationOrDeallocationOperation _signalMonitoringIsFinishedIfNeeded];
-[AVWaitForNotificationOrDeallocationOperation _unregisterForObjectNotifications];
-[AVWaitForNotificationOrDeallocationOperation _waitUntilFinishedIfNeeded];
-[AVWaitForNotificationOrDeallocationOperation initWithObject:notificationNames:];
-[AVWaitForNotificationOrDeallocationOperation monitoredObjectHasDeparted];
```
