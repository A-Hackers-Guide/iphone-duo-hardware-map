# `SAFenceManager`

- Image: [`/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts`](../userland/System__Library__PrivateFrameworks__SeparationAlerts.framework__SeparationAlerts.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SAFenceManagerServiceProtocol`, `SAFenceManagerRequestProtocol`
- 6 instance variables, 6 properties, 28 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _clients;
@"NSMutableDictionary" _deviceUUIDsByUnsafeRegionIdentifier;
@"NSMutableDictionary" _deviceUUIDsBySafeLocation;
@"NSMutableDictionary" _safeLocationsByRegionIdentifier;
@"NSMutableDictionary" _statesByRegionIdentifier;
@"NSMutableDictionary" _regionsByRegionIdentifier;
```

## Properties

```
@property (T@"NSHashTable",&,N,V_clients) clients;
@property (T@"NSMutableDictionary",&,N,V_deviceUUIDsByUnsafeRegionIdentifier) deviceUUIDsByUnsafeRegionIdentifier;
@property (T@"NSMutableDictionary",&,V_deviceUUIDsBySafeLocation) deviceUUIDsBySafeLocation;
@property (T@"NSMutableDictionary",&,N,V_safeLocationsByRegionIdentifier) safeLocationsByRegionIdentifier;
@property (T@"NSMutableDictionary",&,N,V_statesByRegionIdentifier) statesByRegionIdentifier;
@property (T@"NSMutableDictionary",&,N,V_regionsByRegionIdentifier) regionsByRegionIdentifier;
```

## Instance methods

```
-[SAFenceManager clients];
-[SAFenceManager ingestTAEvent:];
-[SAFenceManager removeClient:];
-[SAFenceManager init];
-[SAFenceManager setClients:];
-[SAFenceManager addClient:];
-[SAFenceManager isSafeLocation:];
-[SAFenceManager safeLocationsByRegionIdentifier];
-[SAFenceManager deviceUUIDsBySafeLocation];
-[SAFenceManager deviceUUIDsByUnsafeRegionIdentifier];
-[SAFenceManager getRegionForSafeLocation:];
-[SAFenceManager getSafeLocationCount];
-[SAFenceManager getUnsafeLocationCount];
-[SAFenceManager handleFenceEvent:forRegion:];
-[SAFenceManager notifyState:forSafeLocationRegion:];
-[SAFenceManager notifyState:forUnsafeLocationRegion:];
-[SAFenceManager regionsByRegionIdentifier];
-[SAFenceManager removeLocationsForDeviceUuid:];
-[SAFenceManager setDeviceUUIDsBySafeLocation:];
-[SAFenceManager setDeviceUUIDsByUnsafeRegionIdentifier:];
-[SAFenceManager setRegionsByRegionIdentifier:];
-[SAFenceManager setSafeLocationsByRegionIdentifier:];
-[SAFenceManager setStatesByRegionIdentifier:];
-[SAFenceManager startMonitorSafeLocation:forDevice:];
-[SAFenceManager startMonitorUnsafeLocationExit:forDevice:];
-[SAFenceManager statesByRegionIdentifier];
-[SAFenceManager stopMonitorSafeLocation:forDevice:];
-[SAFenceManager stopMonitorUnsafeLocationExit:forDevice:];
```
