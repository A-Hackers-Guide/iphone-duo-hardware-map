# `ULBuddyMonitor`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ULEventMonitor`
- 2 instance variables, 2 properties, 11 instance methods, 0 class methods

## Instance variables

```
B _buddyComplete;
@"ULDarwinNotificationHelper" _notificationHelper;
```

## Properties

```
@property (T@"ULDarwinNotificationHelper",&,N,V_notificationHelper) notificationHelper;
@property (TB,N,V_buddyComplete) buddyComplete;
```

## Instance methods

```
-[ULBuddyMonitor notificationHelper];
-[ULBuddyMonitor stopMonitoring:];
-[ULBuddyMonitor setNotificationHelper:];
-[ULBuddyMonitor init];
-[ULBuddyMonitor latestEventAfterAddingObserverForEventName:];
-[ULBuddyMonitor startMonitoring:];
-[ULBuddyMonitor _checkBuddyComplete];
-[ULBuddyMonitor _handleBuddyCompleteNotification];
-[ULBuddyMonitor buddyComplete];
-[ULBuddyMonitor initWithNotificationHelper:];
-[ULBuddyMonitor setBuddyComplete:];
```
