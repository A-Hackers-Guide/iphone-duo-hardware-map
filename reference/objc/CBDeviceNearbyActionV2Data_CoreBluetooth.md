# `CBDeviceNearbyActionV2Data`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBDeviceDataComponent`, `CUXPCCodable`, `NSSecureCoding`, `NSCopying`
- 3 instance variables, 7 properties, 18 instance methods, 1 class methods

## Instance variables

```
C _nearbyActionV2Type;
I _nearbyActionV2Flags;
@"NSData" _nearbyActionV2TargetData;
```

## Properties

```
@property (TI,N,V_nearbyActionV2Flags) nearbyActionV2Flags;
@property (T@"NSData",C,N,V_nearbyActionV2TargetData) nearbyActionV2TargetData;
@property (TC,N,V_nearbyActionV2Type) nearbyActionV2Type;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CBDeviceNearbyActionV2Data supportsSecureCoding];
```

## Instance methods

```
-[CBDeviceNearbyActionV2Data memoryFootprint];
-[CBDeviceNearbyActionV2Data encodeWithXPCObject:];
-[CBDeviceNearbyActionV2Data initWithDictionary:error:];
-[CBDeviceNearbyActionV2Data setNearbyActionV2Type:];
-[CBDeviceNearbyActionV2Data clear];
-[CBDeviceNearbyActionV2Data initWithXPCObject:error:];
-[CBDeviceNearbyActionV2Data nearbyActionV2Type];
-[CBDeviceNearbyActionV2Data descriptionWithLevel:];
-[CBDeviceNearbyActionV2Data nearbyActionV2Flags];
-[CBDeviceNearbyActionV2Data setNearbyActionV2TargetData:];
-[CBDeviceNearbyActionV2Data encodeWithCoder:];
-[CBDeviceNearbyActionV2Data description];
-[CBDeviceNearbyActionV2Data initWithCoder:];
-[CBDeviceNearbyActionV2Data setNearbyActionV2Flags:];
-[CBDeviceNearbyActionV2Data hasAnyData];
-[CBDeviceNearbyActionV2Data nearbyActionV2TargetData];
-[CBDeviceNearbyActionV2Data copyWithZone:];
-[CBDeviceNearbyActionV2Data dictionaryRepresentation];
```
