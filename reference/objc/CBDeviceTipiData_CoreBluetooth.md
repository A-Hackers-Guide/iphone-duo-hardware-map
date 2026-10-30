# `CBDeviceTipiData`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBDeviceDataComponent`, `CUXPCCodable`, `NSSecureCoding`, `NSCopying`
- 3 instance variables, 7 properties, 18 instance methods, 1 class methods

## Instance variables

```
C _tipiConnectionStatus;
C _tipiState;
@"NSArray" _tipiDevices;
```

## Properties

```
@property (TC,N,V_tipiConnectionStatus) tipiConnectionStatus;
@property (T@"NSArray",C,N,V_tipiDevices) tipiDevices;
@property (TC,N,V_tipiState) tipiState;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CBDeviceTipiData supportsSecureCoding];
```

## Instance methods

```
-[CBDeviceTipiData memoryFootprint];
-[CBDeviceTipiData encodeWithXPCObject:];
-[CBDeviceTipiData initWithDictionary:error:];
-[CBDeviceTipiData clear];
-[CBDeviceTipiData initWithXPCObject:error:];
-[CBDeviceTipiData descriptionWithLevel:];
-[CBDeviceTipiData encodeWithCoder:];
-[CBDeviceTipiData description];
-[CBDeviceTipiData initWithCoder:];
-[CBDeviceTipiData hasAnyData];
-[CBDeviceTipiData copyWithZone:];
-[CBDeviceTipiData dictionaryRepresentation];
-[CBDeviceTipiData setTipiDevices:];
-[CBDeviceTipiData setTipiConnectionStatus:];
-[CBDeviceTipiData setTipiState:];
-[CBDeviceTipiData tipiConnectionStatus];
-[CBDeviceTipiData tipiDevices];
-[CBDeviceTipiData tipiState];
```
