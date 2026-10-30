# `CBDeviceAirDropData`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBDeviceDataComponent`, `CUXPCCodable`, `NSSecureCoding`, `NSCopying`
- 9 instance variables, 13 properties, 30 instance methods, 1 class methods

## Instance variables

```
C _airdropFlags;
C _airdropVersion;
C _airdropModel;
C _airdropConfigData;
S _airdropHash1;
S _airdropHash2;
S _airdropHash3;
S _airdropHash4;
@"NSData" _airdropTempAuthTagData;
```

## Properties

```
@property (TC,N,V_airdropFlags) airdropFlags;
@property (T@"NSData",C,N,V_airdropTempAuthTagData) airdropTempAuthTagData;
@property (TC,N,V_airdropModel) airdropModel;
@property (TC,N,V_airdropVersion) airdropVersion;
@property (TS,N,V_airdropHash1) airdropHash1;
@property (TS,N,V_airdropHash2) airdropHash2;
@property (TS,N,V_airdropHash3) airdropHash3;
@property (TS,N,V_airdropHash4) airdropHash4;
@property (TC,N,V_airdropConfigData) airdropConfigData;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CBDeviceAirDropData supportsSecureCoding];
```

## Instance methods

```
-[CBDeviceAirDropData memoryFootprint];
-[CBDeviceAirDropData encodeWithXPCObject:];
-[CBDeviceAirDropData initWithDictionary:error:];
-[CBDeviceAirDropData airdropModel];
-[CBDeviceAirDropData clear];
-[CBDeviceAirDropData initWithXPCObject:error:];
-[CBDeviceAirDropData setAirdropTempAuthTagData:];
-[CBDeviceAirDropData descriptionWithLevel:];
-[CBDeviceAirDropData airdropHash3];
-[CBDeviceAirDropData airdropTempAuthTagData];
-[CBDeviceAirDropData setAirdropHash1:];
-[CBDeviceAirDropData airdropFlags];
-[CBDeviceAirDropData airdropHash4];
-[CBDeviceAirDropData setAirdropModel:];
-[CBDeviceAirDropData airdropVersion];
-[CBDeviceAirDropData encodeWithCoder:];
-[CBDeviceAirDropData setAirdropVersion:];
-[CBDeviceAirDropData airdropHash2];
-[CBDeviceAirDropData airdropConfigData];
-[CBDeviceAirDropData description];
-[CBDeviceAirDropData airdropHash1];
-[CBDeviceAirDropData initWithCoder:];
-[CBDeviceAirDropData hasAnyData];
-[CBDeviceAirDropData setAirdropConfigData:];
-[CBDeviceAirDropData setAirdropHash3:];
-[CBDeviceAirDropData copyWithZone:];
-[CBDeviceAirDropData setAirdropFlags:];
-[CBDeviceAirDropData setAirdropHash2:];
-[CBDeviceAirDropData dictionaryRepresentation];
-[CBDeviceAirDropData setAirdropHash4:];
```
