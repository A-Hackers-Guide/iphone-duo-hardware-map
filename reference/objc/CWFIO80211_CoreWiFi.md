# `CWFIO80211`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 1 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _mutexQueue;
@"NSObject<OS_dispatch_queue>" _eventQueue;
^{IONotificationPort=} _portRef;
^{IONotificationPort=} _portRefVirtual;
I _publishIO80211SkywalkInterface;
I _terminatedIO80211SkywalkInterface;
@"NSMutableDictionary" _publishIO80211VirtualInterfaceMap;
@"NSMutableDictionary" _terminatedIO80211VirtualInterfaceMap;
B _isMonitoringEvents;
@? _eventHandler;
```

## Properties

```
@property (T@?,C,V_eventHandler) eventHandler;
```

## Instance methods

```
-[CWFIO80211 IO80211ControllerInfo];
-[CWFIO80211 eventHandler];
-[CWFIO80211 setEventHandler:];
-[CWFIO80211 startEventMonitoring];
-[CWFIO80211 isMonitoringEvents];
-[CWFIO80211 init];
-[CWFIO80211 dealloc];
-[CWFIO80211 stopEventMonitoring];
-[CWFIO80211 IO80211InterfaceInfo:error:];
-[CWFIO80211 __IO80211InfoMatchingService:];
```
