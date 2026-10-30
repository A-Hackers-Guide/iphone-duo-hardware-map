# `CBDeviceData`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBDeviceDataComponent`, `CUXPCCodable`, `NSSecureCoding`, `NSCopying`
- 15 instance variables, 19 properties, 42 instance methods, 2 class methods

## Instance variables

```
@"CBDeviceHeySiriData" _heySiri;
@"CBDeviceBatteryData" _battery;
@"CBDeviceNearbyData" _nearby;
@"CBDeviceAirDropData" _airDrop;
@"CBDeviceProximityPairingData" _proximityPairing;
@"CBDeviceSafetyAlertsData" _safetyAlerts;
@"CBDeviceTipiData" _tipi;
@"CBDeviceNearbyActionNoWakeData" _nearbyActionNoWake;
@"CBDeviceDataProximityService" _proximityService;
@"CBDeviceObjectDiscoveryData" _objectDiscovery;
@"CBDeviceAirPlayData" _airPlay;
@"CBDeviceSpatialInteractionData" _spatialInteraction;
@"CBDeviceHomeKitV1Data" _homeKitV1;
@"CBDeviceHomeKitV2Data" _homeKitV2;
@"CBDeviceServiceDiscoveryData" _serviceDiscovery;
```

## Properties

```
@property (T@"CBDeviceHeySiriData",&,N,V_heySiri) heySiri;
@property (T@"CBDeviceBatteryData",&,N,V_battery) battery;
@property (T@"CBDeviceNearbyData",&,N,V_nearby) nearby;
@property (T@"CBDeviceAirDropData",&,N,V_airDrop) airDrop;
@property (T@"CBDeviceProximityPairingData",&,N,V_proximityPairing) proximityPairing;
@property (T@"CBDeviceSafetyAlertsData",&,N,V_safetyAlerts) safetyAlerts;
@property (T@"CBDeviceTipiData",&,N,V_tipi) tipi;
@property (T@"CBDeviceNearbyActionNoWakeData",&,N,V_nearbyActionNoWake) nearbyActionNoWake;
@property (T@"CBDeviceDataProximityService",&,N,V_proximityService) proximityService;
@property (T@"CBDeviceObjectDiscoveryData",&,N,V_objectDiscovery) objectDiscovery;
@property (T@"CBDeviceAirPlayData",&,N,V_airPlay) airPlay;
@property (T@"CBDeviceSpatialInteractionData",&,N,V_spatialInteraction) spatialInteraction;
@property (T@"CBDeviceHomeKitV1Data",&,N,V_homeKitV1) homeKitV1;
@property (T@"CBDeviceHomeKitV2Data",&,N,V_homeKitV2) homeKitV2;
@property (T@"CBDeviceServiceDiscoveryData",&,N,V_serviceDiscovery) serviceDiscovery;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CBDeviceData supportsSecureCoding];
+[CBDeviceData propertyMetadata];
```

## Instance methods

```
-[CBDeviceData memoryFootprint];
-[CBDeviceData encodeWithXPCObject:];
-[CBDeviceData setProximityService:];
-[CBDeviceData initWithDictionary:error:];
-[CBDeviceData clear];
-[CBDeviceData airDrop];
-[CBDeviceData homeKitV2];
-[CBDeviceData initWithXPCObject:error:];
-[CBDeviceData descriptionWithLevel:];
-[CBDeviceData setTipi:];
-[CBDeviceData setAirDrop:];
-[CBDeviceData setProximityPairing:];
-[CBDeviceData setObjectDiscovery:];
-[CBDeviceData setServiceDiscovery:];
-[CBDeviceData setAirPlay:];
-[CBDeviceData setSafetyAlerts:];
-[CBDeviceData homeKitV1];
-[CBDeviceData setHeySiri:];
-[CBDeviceData setHomeKitV1:];
-[CBDeviceData setSpatialInteraction:];
-[CBDeviceData setHomeKitV2:];
-[CBDeviceData tipi];
-[CBDeviceData setBattery:];
-[CBDeviceData nearby];
-[CBDeviceData encodeWithCoder:];
-[CBDeviceData spatialInteraction];
-[CBDeviceData setNearby:];
-[CBDeviceData battery];
-[CBDeviceData safetyAlerts];
-[CBDeviceData description];
-[CBDeviceData initWithCoder:];
-[CBDeviceData nearbyActionNoWake];
-[CBDeviceData serviceDiscovery];
-[CBDeviceData hasAnyData];
-[CBDeviceData copyWithZone:];
-[CBDeviceData objectDiscovery];
-[CBDeviceData proximityService];
-[CBDeviceData proximityPairing];
-[CBDeviceData airPlay];
-[CBDeviceData setNearbyActionNoWake:];
-[CBDeviceData heySiri];
-[CBDeviceData dictionaryRepresentation];
```
