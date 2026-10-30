# `CBDeviceNearbyData`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBDeviceDataComponent`, `CUXPCCodable`, `NSSecureCoding`, `NSCopying`
- 5 instance variables, 9 properties, 22 instance methods, 2 class methods

## Instance variables

```
@"NSData" _nearbyAuthTag;
@"CBDeviceNearbyInfoData" _nearbyInfo;
@"CBDeviceNearbyInfoV2Data" _nearbyInfoV2;
@"CBDeviceNearbyActionData" _nearbyAction;
@"CBDeviceNearbyActionV2Data" _nearbyActionV2;
```

## Properties

```
@property (T@"NSData",&,V_nearbyAuthTag) nearbyAuthTag;
@property (T@"CBDeviceNearbyInfoData",&,N,V_nearbyInfo) nearbyInfo;
@property (T@"CBDeviceNearbyInfoV2Data",&,N,V_nearbyInfoV2) nearbyInfoV2;
@property (T@"CBDeviceNearbyActionData",&,N,V_nearbyAction) nearbyAction;
@property (T@"CBDeviceNearbyActionV2Data",&,N,V_nearbyActionV2) nearbyActionV2;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CBDeviceNearbyData supportsSecureCoding];
+[CBDeviceNearbyData nearbyPropertyMetadata];
```

## Instance methods

```
-[CBDeviceNearbyData memoryFootprint];
-[CBDeviceNearbyData encodeWithXPCObject:];
-[CBDeviceNearbyData setNearbyInfoV2:];
-[CBDeviceNearbyData initWithDictionary:error:];
-[CBDeviceNearbyData nearbyInfo];
-[CBDeviceNearbyData clear];
-[CBDeviceNearbyData initWithXPCObject:error:];
-[CBDeviceNearbyData descriptionWithLevel:];
-[CBDeviceNearbyData nearbyInfoV2];
-[CBDeviceNearbyData setNearbyAuthTag:];
-[CBDeviceNearbyData nearbyAuthTag];
-[CBDeviceNearbyData encodeWithCoder:];
-[CBDeviceNearbyData description];
-[CBDeviceNearbyData initWithCoder:];
-[CBDeviceNearbyData hasAnyData];
-[CBDeviceNearbyData setNearbyAction:];
-[CBDeviceNearbyData copyWithZone:];
-[CBDeviceNearbyData nearbyActionV2];
-[CBDeviceNearbyData nearbyAction];
-[CBDeviceNearbyData setNearbyInfo:];
-[CBDeviceNearbyData setNearbyActionV2:];
-[CBDeviceNearbyData dictionaryRepresentation];
```
