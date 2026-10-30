# `CBDeviceObjectSetupData`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBDeviceDataComponent`, `CUXPCCodable`, `NSSecureCoding`, `NSCopying`
- 6 instance variables, 10 properties, 24 instance methods, 1 class methods

## Instance variables

```
C _objectSetupBatteryPerformance;
C _objectSetupBatteryState;
C _objectSetupColorCode;
I _objectSetupFlags;
@"NSString" _objectSetupFontCode;
@"NSString" _objectSetupMessage;
```

## Properties

```
@property (TC,N,V_objectSetupBatteryPerformance) objectSetupBatteryPerformance;
@property (TC,N,V_objectSetupBatteryState) objectSetupBatteryState;
@property (TC,N,V_objectSetupColorCode) objectSetupColorCode;
@property (TI,N,V_objectSetupFlags) objectSetupFlags;
@property (T@"NSString",C,N,V_objectSetupFontCode) objectSetupFontCode;
@property (T@"NSString",C,N,V_objectSetupMessage) objectSetupMessage;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CBDeviceObjectSetupData supportsSecureCoding];
```

## Instance methods

```
-[CBDeviceObjectSetupData memoryFootprint];
-[CBDeviceObjectSetupData encodeWithXPCObject:];
-[CBDeviceObjectSetupData initWithDictionary:error:];
-[CBDeviceObjectSetupData clear];
-[CBDeviceObjectSetupData initWithXPCObject:error:];
-[CBDeviceObjectSetupData descriptionWithLevel:];
-[CBDeviceObjectSetupData encodeWithCoder:];
-[CBDeviceObjectSetupData description];
-[CBDeviceObjectSetupData initWithCoder:];
-[CBDeviceObjectSetupData hasAnyData];
-[CBDeviceObjectSetupData copyWithZone:];
-[CBDeviceObjectSetupData dictionaryRepresentation];
-[CBDeviceObjectSetupData objectSetupBatteryPerformance];
-[CBDeviceObjectSetupData objectSetupBatteryState];
-[CBDeviceObjectSetupData objectSetupColorCode];
-[CBDeviceObjectSetupData objectSetupFlags];
-[CBDeviceObjectSetupData objectSetupFontCode];
-[CBDeviceObjectSetupData objectSetupMessage];
-[CBDeviceObjectSetupData setObjectSetupBatteryPerformance:];
-[CBDeviceObjectSetupData setObjectSetupBatteryState:];
-[CBDeviceObjectSetupData setObjectSetupColorCode:];
-[CBDeviceObjectSetupData setObjectSetupFlags:];
-[CBDeviceObjectSetupData setObjectSetupFontCode:];
-[CBDeviceObjectSetupData setObjectSetupMessage:];
```
