# `IOAccessorySystemStateMonitor`

- Image: [`/System/Library/PrivateFrameworks/IOAccessoryManager.framework/IOAccessoryManager`](../userland/System__Library__PrivateFrameworks__IOAccessoryManager.framework__IOAccessoryManager.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 13 properties, 36 instance methods, 0 class methods

## Instance variables

```
B _bootComplete;
B _displayEnabled;
B _pmUserActive;
B _userActive;
B _userPresent;
I _discoveryIterator;
I _terminationIterator;
i _bootToken;
i _displayNotifyToken;
@"NSMutableDictionary" _endpointMap;
Q _pmNotificationHandle;
^{IONotificationPort=} _notificationPort;
@"NSObject<OS_dispatch_queue>" _notificationQueue;
```

## Properties

```
@property (T@"NSMutableDictionary",&,N,V_endpointMap) endpointMap;
@property (TQ,N,V_pmNotificationHandle) pmNotificationHandle;
@property (T^{IONotificationPort=},N,V_notificationPort) notificationPort;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_notificationQueue) notificationQueue;
@property (TI,N,V_discoveryIterator) discoveryIterator;
@property (TI,N,V_terminationIterator) terminationIterator;
@property (Ti,N,V_bootToken) bootToken;
@property (Ti,N,V_displayNotifyToken) displayNotifyToken;
@property (TB,N,V_bootComplete) bootComplete;
@property (TB,N,V_displayEnabled) displayEnabled;
@property (TB,N,V_pmUserActive) pmUserActive;
@property (TB,N,V_userActive) userActive;
@property (TB,N,V_userPresent) userPresent;
```

## Instance methods

```
-[IOAccessorySystemStateMonitor setNotificationQueue:];
-[IOAccessorySystemStateMonitor notificationQueue];
-[IOAccessorySystemStateMonitor init];
-[IOAccessorySystemStateMonitor dealloc];
-[IOAccessorySystemStateMonitor setUserActive:];
-[IOAccessorySystemStateMonitor userActive];
-[IOAccessorySystemStateMonitor notificationPort];
-[IOAccessorySystemStateMonitor setEndpointMap:];
-[IOAccessorySystemStateMonitor setUserPresent:];
-[IOAccessorySystemStateMonitor addEndpointForService:];
-[IOAccessorySystemStateMonitor bootComplete];
-[IOAccessorySystemStateMonitor bootToken];
-[IOAccessorySystemStateMonitor discoveryIterator];
-[IOAccessorySystemStateMonitor displayEnabled];
-[IOAccessorySystemStateMonitor displayNotifyToken];
-[IOAccessorySystemStateMonitor endpointMap];
-[IOAccessorySystemStateMonitor notifyEndpointsBootComplete:];
-[IOAccessorySystemStateMonitor notifyEndpointsUserActive:];
-[IOAccessorySystemStateMonitor notifyEndpointsUserPresent:];
-[IOAccessorySystemStateMonitor pmNotificationHandle];
-[IOAccessorySystemStateMonitor pmUserActive];
-[IOAccessorySystemStateMonitor processBootState];
-[IOAccessorySystemStateMonitor processDisplayState];
-[IOAccessorySystemStateMonitor processPMUserActiveState:];
-[IOAccessorySystemStateMonitor removeEndpointForService:];
-[IOAccessorySystemStateMonitor setBootComplete:];
-[IOAccessorySystemStateMonitor setBootToken:];
-[IOAccessorySystemStateMonitor setDiscoveryIterator:];
-[IOAccessorySystemStateMonitor setDisplayEnabled:];
-[IOAccessorySystemStateMonitor setDisplayNotifyToken:];
-[IOAccessorySystemStateMonitor setNotificationPort:];
-[IOAccessorySystemStateMonitor setPmNotificationHandle:];
-[IOAccessorySystemStateMonitor setPmUserActive:];
-[IOAccessorySystemStateMonitor setTerminationIterator:];
-[IOAccessorySystemStateMonitor terminationIterator];
-[IOAccessorySystemStateMonitor userPresent];
```
