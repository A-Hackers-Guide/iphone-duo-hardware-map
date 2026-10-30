# `IOUSBHostInterestNotifier`

- Image: [`/System/Library/PrivateFrameworks/IOUSBHost.framework/IOUSBHost`](../userland/System__Library__PrivateFrameworks__IOUSBHost.framework__IOUSBHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 9 properties, 23 instance methods, 0 class methods

## Instance variables

```
B _destroyed;
I _service;
I _notifier;
I _matchingIterator;
@"NSObject" _owner;
@"NSRecursiveLock" _lock;
@"NSObject<OS_dispatch_queue>" _queue;
^{IONotificationPort=} _notificationPortRef;
^? _callback;
```

## Properties

```
@property (T@"NSObject",W,N,V_owner) owner;
@property (TB,N,V_destroyed) destroyed;
@property (T@"NSRecursiveLock",&,N,V_lock) lock;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T^{IONotificationPort=},N,V_notificationPortRef) notificationPortRef;
@property (T^?,N,V_callback) callback;
@property (TI,N,V_service) service;
@property (TI,N,V_notifier) notifier;
@property (TI,N,V_matchingIterator) matchingIterator;
```

## Instance methods

```
-[IOUSBHostInterestNotifier owner];
-[IOUSBHostInterestNotifier callback];
-[IOUSBHostInterestNotifier setLock:];
-[IOUSBHostInterestNotifier setCallback:];
-[IOUSBHostInterestNotifier setService:];
-[IOUSBHostInterestNotifier destroy];
-[IOUSBHostInterestNotifier dealloc];
-[IOUSBHostInterestNotifier queue];
-[IOUSBHostInterestNotifier setOwner:];
-[IOUSBHostInterestNotifier service];
-[IOUSBHostInterestNotifier lock];
-[IOUSBHostInterestNotifier setQueue:];
-[IOUSBHostInterestNotifier notifier];
-[IOUSBHostInterestNotifier setNotifier:];
-[IOUSBHostInterestNotifier destroyed];
-[IOUSBHostInterestNotifier initWithOwner:service:callback:];
-[IOUSBHostInterestNotifier initWithOwner:callback:];
-[IOUSBHostInterestNotifier initWithOwner:matchingDictionary:callback:];
-[IOUSBHostInterestNotifier matchingIterator];
-[IOUSBHostInterestNotifier notificationPortRef];
-[IOUSBHostInterestNotifier setDestroyed:];
-[IOUSBHostInterestNotifier setMatchingIterator:];
-[IOUSBHostInterestNotifier setNotificationPortRef:];
```
