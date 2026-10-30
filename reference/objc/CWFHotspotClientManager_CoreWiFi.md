# `CWFHotspotClientManager`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CWFDeviceDiscoveryManagerDelegate`
- 4 instance variables, 4 properties, 19 instance methods, 1 class methods

## Instance variables

```
@"NSMutableSet" _activeHotspotClients;
@"CWFDeviceDiscoveryManager" _deviceDiscoveryManager;
@"NSObject<OS_dispatch_queue>" _hotspotQueue;
Q _cellularInterfaceType;
```

## Properties

```
@property (T@"CWFDeviceDiscoveryManager",&,N,V_deviceDiscoveryManager) deviceDiscoveryManager;
@property (T@"NSMutableSet",&,N,V_activeHotspotClients) activeHotspotClients;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_hotspotQueue) hotspotQueue;
@property (TQ,N,V_cellularInterfaceType) cellularInterfaceType;
```

## Class methods

```
+[CWFHotspotClientManager sharedInstance];
```

## Instance methods

```
-[CWFHotspotClientManager init];
-[CWFHotspotClientManager dealloc];
-[CWFHotspotClientManager didDiscoverDevice:];
-[CWFHotspotClientManager didLoseDevice:];
-[CWFHotspotClientManager hotspotDisabled];
-[CWFHotspotClientManager activeHotspotClients];
-[CWFHotspotClientManager cellularInterfaceType];
-[CWFHotspotClientManager clientAssociated:thisDeviceMACAddress:];
-[CWFHotspotClientManager clientAssociatedToHostPersonalHotspot:];
-[CWFHotspotClientManager clientDisassociated:];
-[CWFHotspotClientManager deviceDiscoveryManager];
-[CWFHotspotClientManager didFetchWifiInfoForDevice:];
-[CWFHotspotClientManager getCellularInterfaceType];
-[CWFHotspotClientManager hotspotQueue];
-[CWFHotspotClientManager saveCellularInterfaceType:];
-[CWFHotspotClientManager setActiveHotspotClients:];
-[CWFHotspotClientManager setCellularInterfaceType:];
-[CWFHotspotClientManager setDeviceDiscoveryManager:];
-[CWFHotspotClientManager setHotspotQueue:];
```
