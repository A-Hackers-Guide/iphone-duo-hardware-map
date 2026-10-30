# `ACCUserNotificationManager`

- Image: [`/System/Library/CoreAccessories/PlugIns/Transports/IOAccessoryManager.transport/IOAccessoryManager`](../userland/System__Library__CoreAccessories__PlugIns__Transports__IOAccessoryManager.transport__IOAccessoryManager.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 17 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"NSMutableSet" _userNotifications;
@"NSMutableDictionary" _completionHandlers;
@"NSRecursiveLock" _lock;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"NSMutableSet",&,N,V_userNotifications) userNotifications;
@property (T@"NSMutableDictionary",&,N,V_completionHandlers) completionHandlers;
@property (T@"NSRecursiveLock",&,N,V_lock) lock;
```

## Class methods

```
+[ACCUserNotificationManager sharedManager];
```

## Instance methods

```
-[ACCUserNotificationManager setLock:];
-[ACCUserNotificationManager completionHandlers];
-[ACCUserNotificationManager init];
-[ACCUserNotificationManager setCompletionHandlers:];
-[ACCUserNotificationManager queue];
-[ACCUserNotificationManager lock];
-[ACCUserNotificationManager userNotifications];
-[ACCUserNotificationManager setQueue:];
-[ACCUserNotificationManager dismissAllNotifications];
-[ACCUserNotificationManager dismissNotification:];
-[ACCUserNotificationManager dismissNotificationWithIdentifier:];
-[ACCUserNotificationManager dismissNotificationsWithGroupIdentifier:];
-[ACCUserNotificationManager presentNotification:completionHandler:];
-[ACCUserNotificationManager removeUserNotification:];
-[ACCUserNotificationManager setUserNotifications:];
-[ACCUserNotificationManager updateNotification:];
-[ACCUserNotificationManager userNotificationWithUUID:];
```
