# `IOKMatchingNotification`

- Image: [`/System/Library/PrivateFrameworks/IOKitten.framework/IOKitten`](../userland/System__Library__PrivateFrameworks__IOKitten.framework__IOKitten.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
@? _handler;
@"IOKIterator" _iterator;
@"NSObject<OS_dispatch_queue>" _queue;
@"IOKMatchingNotificationRef" _notificationRef;
```

## Properties

```
@property (T@?,C,N,V_handler) handler;
@property (T@"IOKIterator",&,N,V_iterator) iterator;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"IOKMatchingNotificationRef",R,N,V_notificationRef) notificationRef;
```

## Instance methods

```
-[IOKMatchingNotification notificationRef];
-[IOKMatchingNotification init];
-[IOKMatchingNotification primeNotification];
-[IOKMatchingNotification dealloc];
-[IOKMatchingNotification setHandler:];
-[IOKMatchingNotification queue];
-[IOKMatchingNotification iterator];
-[IOKMatchingNotification handler];
-[IOKMatchingNotification setIterator:];
-[IOKMatchingNotification setQueue:];
```
