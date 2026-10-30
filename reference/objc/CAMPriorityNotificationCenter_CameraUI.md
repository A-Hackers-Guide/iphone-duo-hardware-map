# `CAMPriorityNotificationCenter`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 17 instance methods, 1 class methods

## Instance variables

```
@"NSNotificationCenter" __notificationCenter;
@"NSMutableDictionary" __observersByNameHighPriority;
@"NSMutableDictionary" __observersByNameNormalPriority;
@"NSObject<OS_dispatch_queue>" __mutexQueue;
```

## Properties

```
@property (T@"NSNotificationCenter",R,&,N,V__notificationCenter) _notificationCenter;
@property (T@"NSMutableDictionary",R,&,N,V__observersByNameHighPriority) _observersByNameHighPriority;
@property (T@"NSMutableDictionary",R,&,N,V__observersByNameNormalPriority) _observersByNameNormalPriority;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V__mutexQueue) _mutexQueue;
```

## Class methods

```
+[CAMPriorityNotificationCenter defaultCenter];
```

## Instance methods

```
-[CAMPriorityNotificationCenter _notificationCenter];
-[CAMPriorityNotificationCenter _allSubscriptions];
-[CAMPriorityNotificationCenter removeObserver:];
-[CAMPriorityNotificationCenter init];
-[CAMPriorityNotificationCenter dealloc];
-[CAMPriorityNotificationCenter addObserver:selector:name:object:];
-[CAMPriorityNotificationCenter _observersForPriority:];
-[CAMPriorityNotificationCenter _entriesByName:forPriority:creatingEmptyIfNeeded:];
-[CAMPriorityNotificationCenter _mutexQueue];
-[CAMPriorityNotificationCenter _mutexQueue_addObserver:priority:selector:name:object:];
-[CAMPriorityNotificationCenter _mutexQueue_removeObserver:];
-[CAMPriorityNotificationCenter _notificationReceiver:];
-[CAMPriorityNotificationCenter _observersByNameHighPriority];
-[CAMPriorityNotificationCenter _observersByNameNormalPriority];
-[CAMPriorityNotificationCenter _postNotification:forEntries:];
-[CAMPriorityNotificationCenter _removeObserver:fromObserversByName:];
-[CAMPriorityNotificationCenter addObserver:priority:selector:name:object:];
```
