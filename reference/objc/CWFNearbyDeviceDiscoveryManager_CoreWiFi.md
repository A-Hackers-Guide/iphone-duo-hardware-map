# `CWFNearbyDeviceDiscoveryManager`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 25 instance methods, 0 class methods

## Instance variables

```
B __didDriverCrash;
@? _sendNDDRequest;
@? _isNDDAllowed;
@? _sendNDDXPCEvent;
@"CWFNearbyDeviceDiscoveryParameter" __currentNDDRequest;
@"NSString" __interface;
@"NSObject<OS_dispatch_queue>" __serviceQueue;
```

## Properties

```
@property (T@"CWFNearbyDeviceDiscoveryParameter",&,N,V__currentNDDRequest) _currentNDDRequest;
@property (T@"NSString",&,N,V__interface) _interface;
@property (TB,N,V__didDriverCrash) _didDriverCrash;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V__serviceQueue) _serviceQueue;
@property (T@?,C,V_isNDDAllowed) isNDDAllowed;
@property (T@?,C,V_sendNDDRequest) sendNDDRequest;
@property (T@?,C,V_sendNDDXPCEvent) sendNDDXPCEvent;
```

## Instance methods

```
-[CWFNearbyDeviceDiscoveryManager init];
-[CWFNearbyDeviceDiscoveryManager _serviceQueue];
-[CWFNearbyDeviceDiscoveryManager set_serviceQueue:];
-[CWFNearbyDeviceDiscoveryManager handleNDDResultEvent:interface:];
-[CWFNearbyDeviceDiscoveryManager _didDriverCrash];
-[CWFNearbyDeviceDiscoveryManager handleEvent:withData:interface:];
-[CWFNearbyDeviceDiscoveryManager sendNDDXPCEvent];
-[CWFNearbyDeviceDiscoveryManager _currentNDDRequest];
-[CWFNearbyDeviceDiscoveryManager _interface];
-[CWFNearbyDeviceDiscoveryManager getEDSResultFromReport:];
-[CWFNearbyDeviceDiscoveryManager getRequestDataFromParams:];
-[CWFNearbyDeviceDiscoveryManager handleDextCrashEvent];
-[CWFNearbyDeviceDiscoveryManager handleDriverAvailableEvent];
-[CWFNearbyDeviceDiscoveryManager handleNDDDoneEvent:interface:];
-[CWFNearbyDeviceDiscoveryManager handleNDDRequestWithParams:clientName:interface:];
-[CWFNearbyDeviceDiscoveryManager handleRequest:withData:interface:];
-[CWFNearbyDeviceDiscoveryManager isNDDAllowed];
-[CWFNearbyDeviceDiscoveryManager isNDDRequestValid:];
-[CWFNearbyDeviceDiscoveryManager sendNDDRequest];
-[CWFNearbyDeviceDiscoveryManager setIsNDDAllowed:];
-[CWFNearbyDeviceDiscoveryManager setSendNDDRequest:];
-[CWFNearbyDeviceDiscoveryManager setSendNDDXPCEvent:];
-[CWFNearbyDeviceDiscoveryManager set_currentNDDRequest:];
-[CWFNearbyDeviceDiscoveryManager set_didDriverCrash:];
-[CWFNearbyDeviceDiscoveryManager set_interface:];
```
