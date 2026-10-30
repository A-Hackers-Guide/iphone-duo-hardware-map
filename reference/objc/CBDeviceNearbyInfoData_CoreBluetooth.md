# `CBDeviceNearbyInfoData`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBDeviceDataComponent`, `CUXPCCodable`, `NSSecureCoding`, `NSCopying`
- 6 instance variables, 10 properties, 24 instance methods, 1 class methods

## Instance variables

```
C _nearbyInfoStatusTime;
C _nearbyInfoStatusType;
C _nearbyActivityLevel;
I _nearbyInfoFlags;
d _nearbyInfoStatusProgress;
@"NSData" _nearbyInfoAuthTag;
```

## Properties

```
@property (Td,N,V_nearbyInfoStatusProgress) nearbyInfoStatusProgress;
@property (TC,N,V_nearbyInfoStatusTime) nearbyInfoStatusTime;
@property (TI,N,V_nearbyInfoFlags) nearbyInfoFlags;
@property (TC,N,V_nearbyInfoStatusType) nearbyInfoStatusType;
@property (TC,N,V_nearbyActivityLevel) nearbyActivityLevel;
@property (T@"NSData",C,N,V_nearbyInfoAuthTag) nearbyInfoAuthTag;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CBDeviceNearbyInfoData supportsSecureCoding];
```

## Instance methods

```
-[CBDeviceNearbyInfoData memoryFootprint];
-[CBDeviceNearbyInfoData encodeWithXPCObject:];
-[CBDeviceNearbyInfoData nearbyInfoStatusTime];
-[CBDeviceNearbyInfoData nearbyInfoFlags];
-[CBDeviceNearbyInfoData nearbyInfoStatusProgress];
-[CBDeviceNearbyInfoData setNearbyInfoStatusProgress:];
-[CBDeviceNearbyInfoData initWithDictionary:error:];
-[CBDeviceNearbyInfoData setNearbyInfoStatusType:];
-[CBDeviceNearbyInfoData nearbyInfoStatusType];
-[CBDeviceNearbyInfoData setNearbyInfoStatusTime:];
-[CBDeviceNearbyInfoData clear];
-[CBDeviceNearbyInfoData setNearbyInfoFlags:];
-[CBDeviceNearbyInfoData initWithXPCObject:error:];
-[CBDeviceNearbyInfoData nearbyInfoAuthTag];
-[CBDeviceNearbyInfoData descriptionWithLevel:];
-[CBDeviceNearbyInfoData setNearbyInfoAuthTag:];
-[CBDeviceNearbyInfoData nearbyActivityLevel];
-[CBDeviceNearbyInfoData encodeWithCoder:];
-[CBDeviceNearbyInfoData description];
-[CBDeviceNearbyInfoData initWithCoder:];
-[CBDeviceNearbyInfoData setNearbyActivityLevel:];
-[CBDeviceNearbyInfoData hasAnyData];
-[CBDeviceNearbyInfoData copyWithZone:];
-[CBDeviceNearbyInfoData dictionaryRepresentation];
```
