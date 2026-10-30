# `CBDeviceSpatialInteractionData`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBDeviceDataComponent`, `CUXPCCodable`, `NSSecureCoding`, `NSCopying`
- 11 instance variables, 15 properties, 34 instance methods, 1 class methods

## Instance variables

```
C _spatialInteractionConfigFlags;
C _spatialInteractionFlags;
I _spatialInteractionPeerID;
I _spatialInteractionUWBTokenFlags;
@"NSArray" _spatialInteractionIdentifiers;
@"NSData" _spatialInteractionPresenceConfigData;
@"NSData" _spatialInteractionTokenData;
@"NSDictionary" _spatialInteractionUserInfo;
@"NSData" _spatialInteractionUWBConfigData;
@"NSMutableArray" _spatialInteractionDeviceTimestampArrayClientIDs;
@"NSMutableDictionary" _spatialInteractionDeviceTimestampArrayDictionary;
```

## Properties

```
@property (TC,N,V_spatialInteractionConfigFlags) spatialInteractionConfigFlags;
@property (TC,N,V_spatialInteractionFlags) spatialInteractionFlags;
@property (T@"NSArray",C,N,V_spatialInteractionIdentifiers) spatialInteractionIdentifiers;
@property (TI,N,V_spatialInteractionPeerID) spatialInteractionPeerID;
@property (T@"NSData",C,N,V_spatialInteractionPresenceConfigData) spatialInteractionPresenceConfigData;
@property (T@"NSData",C,N,V_spatialInteractionTokenData) spatialInteractionTokenData;
@property (T@"NSDictionary",C,N,V_spatialInteractionUserInfo) spatialInteractionUserInfo;
@property (T@"NSData",C,N,V_spatialInteractionUWBConfigData) spatialInteractionUWBConfigData;
@property (TI,N,V_spatialInteractionUWBTokenFlags) spatialInteractionUWBTokenFlags;
@property (T@"NSMutableArray",&,N,V_spatialInteractionDeviceTimestampArrayClientIDs) spatialInteractionDeviceTimestampArrayClientIDs;
@property (T@"NSMutableDictionary",&,N,V_spatialInteractionDeviceTimestampArrayDictionary) spatialInteractionDeviceTimestampArrayDictionary;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CBDeviceSpatialInteractionData supportsSecureCoding];
```

## Instance methods

```
-[CBDeviceSpatialInteractionData memoryFootprint];
-[CBDeviceSpatialInteractionData encodeWithXPCObject:];
-[CBDeviceSpatialInteractionData initWithDictionary:error:];
-[CBDeviceSpatialInteractionData clear];
-[CBDeviceSpatialInteractionData initWithXPCObject:error:];
-[CBDeviceSpatialInteractionData descriptionWithLevel:];
-[CBDeviceSpatialInteractionData encodeWithCoder:];
-[CBDeviceSpatialInteractionData description];
-[CBDeviceSpatialInteractionData initWithCoder:];
-[CBDeviceSpatialInteractionData hasAnyData];
-[CBDeviceSpatialInteractionData copyWithZone:];
-[CBDeviceSpatialInteractionData dictionaryRepresentation];
-[CBDeviceSpatialInteractionData setSpatialInteractionTokenData:];
-[CBDeviceSpatialInteractionData spatialInteractionUWBTokenFlags];
-[CBDeviceSpatialInteractionData spatialInteractionUWBConfigData];
-[CBDeviceSpatialInteractionData setSpatialInteractionConfigFlags:];
-[CBDeviceSpatialInteractionData setSpatialInteractionDeviceTimestampArrayClientIDs:];
-[CBDeviceSpatialInteractionData setSpatialInteractionDeviceTimestampArrayDictionary:];
-[CBDeviceSpatialInteractionData setSpatialInteractionFlags:];
-[CBDeviceSpatialInteractionData setSpatialInteractionIdentifiers:];
-[CBDeviceSpatialInteractionData setSpatialInteractionPeerID:];
-[CBDeviceSpatialInteractionData setSpatialInteractionPresenceConfigData:];
-[CBDeviceSpatialInteractionData setSpatialInteractionUWBConfigData:];
-[CBDeviceSpatialInteractionData setSpatialInteractionUWBTokenFlags:];
-[CBDeviceSpatialInteractionData setSpatialInteractionUserInfo:];
-[CBDeviceSpatialInteractionData spatialInteractionConfigFlags];
-[CBDeviceSpatialInteractionData spatialInteractionDeviceTimestampArrayClientIDs];
-[CBDeviceSpatialInteractionData spatialInteractionDeviceTimestampArrayDictionary];
-[CBDeviceSpatialInteractionData spatialInteractionFlags];
-[CBDeviceSpatialInteractionData spatialInteractionIdentifiers];
-[CBDeviceSpatialInteractionData spatialInteractionPeerID];
-[CBDeviceSpatialInteractionData spatialInteractionPresenceConfigData];
-[CBDeviceSpatialInteractionData spatialInteractionTokenData];
-[CBDeviceSpatialInteractionData spatialInteractionUserInfo];
```
