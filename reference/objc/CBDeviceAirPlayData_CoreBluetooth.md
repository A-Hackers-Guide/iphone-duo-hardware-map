# `CBDeviceAirPlayData`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBDeviceDataComponent`, `CUXPCCodable`, `NSSecureCoding`, `NSCopying`
- 8 instance variables, 12 properties, 28 instance methods, 1 class methods

## Instance variables

```
C _airplaySourceFlags;
C _airplayTargetConfigSeed;
C _airplayTargetFlags;
S _airplayTargetPort;
I _airplayTargetIPv4;
@"NSData" _airplaySourceAuthTagData;
@"NSData" _airplaySourceUWBConfigData;
@"NSData" _airplayTargetIPv6;
```

## Properties

```
@property (T@"NSData",C,N,V_airplaySourceAuthTagData) airplaySourceAuthTagData;
@property (TC,N,V_airplaySourceFlags) airplaySourceFlags;
@property (T@"NSData",C,N,V_airplaySourceUWBConfigData) airplaySourceUWBConfigData;
@property (TC,N,V_airplayTargetConfigSeed) airplayTargetConfigSeed;
@property (TC,N,V_airplayTargetFlags) airplayTargetFlags;
@property (TI,N,V_airplayTargetIPv4) airplayTargetIPv4;
@property (T@"NSData",C,N,V_airplayTargetIPv6) airplayTargetIPv6;
@property (TS,N,V_airplayTargetPort) airplayTargetPort;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CBDeviceAirPlayData supportsSecureCoding];
```

## Instance methods

```
-[CBDeviceAirPlayData memoryFootprint];
-[CBDeviceAirPlayData encodeWithXPCObject:];
-[CBDeviceAirPlayData airplaySourceAuthTagData];
-[CBDeviceAirPlayData initWithDictionary:error:];
-[CBDeviceAirPlayData clear];
-[CBDeviceAirPlayData initWithXPCObject:error:];
-[CBDeviceAirPlayData descriptionWithLevel:];
-[CBDeviceAirPlayData airplayTargetPort];
-[CBDeviceAirPlayData setAirplayTargetIPv4:];
-[CBDeviceAirPlayData airplaySourceUWBConfigData];
-[CBDeviceAirPlayData airplayTargetConfigSeed];
-[CBDeviceAirPlayData airplayTargetIPv4];
-[CBDeviceAirPlayData setAirplaySourceFlags:];
-[CBDeviceAirPlayData airplaySourceFlags];
-[CBDeviceAirPlayData encodeWithCoder:];
-[CBDeviceAirPlayData setAirplayTargetPort:];
-[CBDeviceAirPlayData setAirplayTargetFlags:];
-[CBDeviceAirPlayData description];
-[CBDeviceAirPlayData setAirplaySourceAuthTagData:];
-[CBDeviceAirPlayData initWithCoder:];
-[CBDeviceAirPlayData hasAnyData];
-[CBDeviceAirPlayData setAirplayTargetConfigSeed:];
-[CBDeviceAirPlayData copyWithZone:];
-[CBDeviceAirPlayData airplayTargetFlags];
-[CBDeviceAirPlayData setAirplaySourceUWBConfigData:];
-[CBDeviceAirPlayData dictionaryRepresentation];
-[CBDeviceAirPlayData airplayTargetIPv6];
-[CBDeviceAirPlayData setAirplayTargetIPv6:];
```
