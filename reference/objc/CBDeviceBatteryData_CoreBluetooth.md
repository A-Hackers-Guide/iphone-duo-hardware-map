# `CBDeviceBatteryData`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBDeviceDataComponent`, `CUXPCCodable`, `NSSecureCoding`, `NSCopying`
- 4 instance variables, 8 properties, 20 instance methods, 1 class methods

## Instance variables

```
S _batteryInfoMain;
S _batteryInfoCase;
S _batteryInfoLeft;
S _batteryInfoRight;
```

## Properties

```
@property (TS,N,V_batteryInfoMain) batteryInfoMain;
@property (TS,N,V_batteryInfoLeft) batteryInfoLeft;
@property (TS,N,V_batteryInfoRight) batteryInfoRight;
@property (TS,N,V_batteryInfoCase) batteryInfoCase;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CBDeviceBatteryData supportsSecureCoding];
```

## Instance methods

```
-[CBDeviceBatteryData memoryFootprint];
-[CBDeviceBatteryData encodeWithXPCObject:];
-[CBDeviceBatteryData initWithDictionary:error:];
-[CBDeviceBatteryData clear];
-[CBDeviceBatteryData initWithXPCObject:error:];
-[CBDeviceBatteryData descriptionWithLevel:];
-[CBDeviceBatteryData encodeWithCoder:];
-[CBDeviceBatteryData description];
-[CBDeviceBatteryData initWithCoder:];
-[CBDeviceBatteryData hasAnyData];
-[CBDeviceBatteryData copyWithZone:];
-[CBDeviceBatteryData dictionaryRepresentation];
-[CBDeviceBatteryData batteryInfoCase];
-[CBDeviceBatteryData batteryInfoMain];
-[CBDeviceBatteryData batteryInfoLeft];
-[CBDeviceBatteryData batteryInfoRight];
-[CBDeviceBatteryData setBatteryInfoCase:];
-[CBDeviceBatteryData setBatteryInfoLeft:];
-[CBDeviceBatteryData setBatteryInfoMain:];
-[CBDeviceBatteryData setBatteryInfoRight:];
```
