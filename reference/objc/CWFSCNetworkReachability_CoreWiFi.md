# `CWFSCNetworkReachability`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 1 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _mutexQueue;
@"NSObject<OS_dispatch_queue>" _eventQueue;
^{__SCNetworkReachability=} _reachabilityRef;
B _isMonitoringEvents;
@? _eventHandler;
```

## Properties

```
@property (T@?,C,V_eventHandler) eventHandler;
```

## Instance methods

```
-[CWFSCNetworkReachability eventHandler];
-[CWFSCNetworkReachability setEventHandler:];
-[CWFSCNetworkReachability startEventMonitoring];
-[CWFSCNetworkReachability flags];
-[CWFSCNetworkReachability isMonitoringEvents];
-[CWFSCNetworkReachability init];
-[CWFSCNetworkReachability dealloc];
-[CWFSCNetworkReachability stopEventMonitoring];
```
