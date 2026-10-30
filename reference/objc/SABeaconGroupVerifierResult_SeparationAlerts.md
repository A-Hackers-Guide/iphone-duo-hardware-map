# `SABeaconGroupVerifierResult`

- Image: [`/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts`](../userland/System__Library__PrivateFrameworks__SeparationAlerts.framework__SeparationAlerts.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
B _beaconGroupComplete;
B _beaconGroupSafeLocationsMatch;
@"NSMutableDictionary" _deviceUUIDtoDeviceMap;
@"NSMutableDictionary" _deviceToSafeLocationMap;
```

## Properties

```
@property (TB,N,V_beaconGroupComplete) beaconGroupComplete;
@property (TB,N,V_beaconGroupSafeLocationsMatch) beaconGroupSafeLocationsMatch;
@property (T@"NSMutableDictionary",&,N,V_deviceUUIDtoDeviceMap) deviceUUIDtoDeviceMap;
@property (T@"NSMutableDictionary",&,N,V_deviceToSafeLocationMap) deviceToSafeLocationMap;
```

## Instance methods

```
-[SABeaconGroupVerifierResult init];
-[SABeaconGroupVerifierResult setBeaconGroupSafeLocationsMatch:];
-[SABeaconGroupVerifierResult beaconGroupComplete];
-[SABeaconGroupVerifierResult beaconGroupSafeLocationsMatch];
-[SABeaconGroupVerifierResult setBeaconGroupComplete:];
-[SABeaconGroupVerifierResult deviceToSafeLocationMap];
-[SABeaconGroupVerifierResult deviceUUIDtoDeviceMap];
-[SABeaconGroupVerifierResult setDeviceToSafeLocationMap:];
-[SABeaconGroupVerifierResult setDeviceUUIDtoDeviceMap:];
```
