# `CBDeviceNearbyActionData`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBDeviceDataComponent`, `CUXPCCodable`, `NSSecureCoding`, `NSCopying`
- 7 instance variables, 11 properties, 26 instance methods, 1 class methods

## Instance variables

```
C _nearbyActionType;
C _nearbyActionColorCode;
C _nearbyActionDeviceClass;
I _nearbyActionFlags;
@"NSData" _nearbyActionAuthTag;
@"NSData" _nearbyActionExtraData;
@"NSData" _nearbyActionTargetAuthTag;
```

## Properties

```
@property (T@"NSData",C,N,V_nearbyActionAuthTag) nearbyActionAuthTag;
@property (TC,N,V_nearbyActionColorCode) nearbyActionColorCode;
@property (T@"NSData",C,N,V_nearbyActionTargetAuthTag) nearbyActionTargetAuthTag;
@property (TC,N,V_nearbyActionDeviceClass) nearbyActionDeviceClass;
@property (T@"NSData",C,N,V_nearbyActionExtraData) nearbyActionExtraData;
@property (TI,N,V_nearbyActionFlags) nearbyActionFlags;
@property (TC,N,V_nearbyActionType) nearbyActionType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CBDeviceNearbyActionData supportsSecureCoding];
```

## Instance methods

```
-[CBDeviceNearbyActionData memoryFootprint];
-[CBDeviceNearbyActionData encodeWithXPCObject:];
-[CBDeviceNearbyActionData setNearbyActionType:];
-[CBDeviceNearbyActionData setNearbyActionFlags:];
-[CBDeviceNearbyActionData initWithDictionary:error:];
-[CBDeviceNearbyActionData nearbyActionExtraData];
-[CBDeviceNearbyActionData setNearbyActionExtraData:];
-[CBDeviceNearbyActionData nearbyActionColorCode];
-[CBDeviceNearbyActionData nearbyActionFlags];
-[CBDeviceNearbyActionData clear];
-[CBDeviceNearbyActionData nearbyActionType];
-[CBDeviceNearbyActionData setNearbyActionColorCode:];
-[CBDeviceNearbyActionData initWithXPCObject:error:];
-[CBDeviceNearbyActionData descriptionWithLevel:];
-[CBDeviceNearbyActionData nearbyActionAuthTag];
-[CBDeviceNearbyActionData setNearbyActionAuthTag:];
-[CBDeviceNearbyActionData encodeWithCoder:];
-[CBDeviceNearbyActionData nearbyActionDeviceClass];
-[CBDeviceNearbyActionData description];
-[CBDeviceNearbyActionData setNearbyActionDeviceClass:];
-[CBDeviceNearbyActionData initWithCoder:];
-[CBDeviceNearbyActionData setNearbyActionTargetAuthTag:];
-[CBDeviceNearbyActionData hasAnyData];
-[CBDeviceNearbyActionData nearbyActionTargetAuthTag];
-[CBDeviceNearbyActionData copyWithZone:];
-[CBDeviceNearbyActionData dictionaryRepresentation];
```
