# `CBDeviceNearbyActionNoWakeData`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBDeviceDataComponent`, `CUXPCCodable`, `NSSecureCoding`, `NSCopying`
- 4 instance variables, 8 properties, 20 instance methods, 1 class methods

## Instance variables

```
C _nearbyActionNoWakeType;
C _nearbyActionNWPrecisionFindingStatus;
@"NSData" _nearbyActionNoWakeAuthTagData;
@"NSData" _nearbyActionNoWakeConfigData;
```

## Properties

```
@property (T@"NSData",C,N,V_nearbyActionNoWakeAuthTagData) nearbyActionNoWakeAuthTagData;
@property (T@"NSData",C,N,V_nearbyActionNoWakeConfigData) nearbyActionNoWakeConfigData;
@property (TC,N,V_nearbyActionNoWakeType) nearbyActionNoWakeType;
@property (TC,N,V_nearbyActionNWPrecisionFindingStatus) nearbyActionNWPrecisionFindingStatus;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CBDeviceNearbyActionNoWakeData supportsSecureCoding];
```

## Instance methods

```
-[CBDeviceNearbyActionNoWakeData memoryFootprint];
-[CBDeviceNearbyActionNoWakeData encodeWithXPCObject:];
-[CBDeviceNearbyActionNoWakeData initWithDictionary:error:];
-[CBDeviceNearbyActionNoWakeData clear];
-[CBDeviceNearbyActionNoWakeData initWithXPCObject:error:];
-[CBDeviceNearbyActionNoWakeData descriptionWithLevel:];
-[CBDeviceNearbyActionNoWakeData setNearbyActionNoWakeConfigData:];
-[CBDeviceNearbyActionNoWakeData nearbyActionNoWakeConfigData];
-[CBDeviceNearbyActionNoWakeData setNearbyActionNWPrecisionFindingStatus:];
-[CBDeviceNearbyActionNoWakeData nearbyActionNoWakeType];
-[CBDeviceNearbyActionNoWakeData encodeWithCoder:];
-[CBDeviceNearbyActionNoWakeData description];
-[CBDeviceNearbyActionNoWakeData initWithCoder:];
-[CBDeviceNearbyActionNoWakeData nearbyActionNoWakeAuthTagData];
-[CBDeviceNearbyActionNoWakeData hasAnyData];
-[CBDeviceNearbyActionNoWakeData setNearbyActionNoWakeType:];
-[CBDeviceNearbyActionNoWakeData copyWithZone:];
-[CBDeviceNearbyActionNoWakeData setNearbyActionNoWakeAuthTagData:];
-[CBDeviceNearbyActionNoWakeData nearbyActionNWPrecisionFindingStatus];
-[CBDeviceNearbyActionNoWakeData dictionaryRepresentation];
```
