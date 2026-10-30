# `CAFSeatFan`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- Protocols: `CAFPositionedRequired`
- 0 instance variables, 21 properties, 29 instance methods, 3 class methods

## Properties

```
@property (T@"CAFBoolCharacteristic",R,N) onCharacteristic;
@property (T@"CAFUInt8Characteristic",R,N) fanLevelCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) autoModeCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) vehicleLayoutKeyCharacteristic;
@property (TB,N) on;
@property (TB,R,N) hasOn;
@property (TB,R,N) onDisabled;
@property (TB,R,N) onInvalid;
@property (TB,R,N) onRestricted;
@property (TC,N) fanLevel;
@property (T@"CAFUInt8Range",R,N) fanLevelRange;
@property (TB,R,N) fanLevelDisabled;
@property (TB,R,N) fanLevelInvalid;
@property (TB,R,N) fanLevelRestricted;
@property (TB,R,N) autoMode;
@property (TB,R,N) hasAutoMode;
@property (T@"NSString",R,N) vehicleLayoutKey;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CAFSeatFan serviceIdentifier];
+[CAFSeatFan indexBy];
+[CAFSeatFan observerProtocol];
```

## Instance methods

```
-[CAFSeatFan on];
-[CAFSeatFan removeObserver:];
-[CAFSeatFan addObserver:];
-[CAFSeatFan setOn:];
-[CAFSeatFan registerObserver:];
-[CAFSeatFan name];
-[CAFSeatFan unregisterObserver:];
-[CAFSeatFan fanLevelInvalid];
-[CAFSeatFan registeredForOn];
-[CAFSeatFan autoMode];
-[CAFSeatFan fanLevel];
-[CAFSeatFan fanLevelDisabled];
-[CAFSeatFan fanLevelRange];
-[CAFSeatFan hasAutoMode];
-[CAFSeatFan hasOn];
-[CAFSeatFan onDisabled];
-[CAFSeatFan onInvalid];
-[CAFSeatFan onRestricted];
-[CAFSeatFan registeredForAutoMode];
-[CAFSeatFan registeredForFanLevel];
-[CAFSeatFan registeredForVehicleLayoutKey];
-[CAFSeatFan setFanLevel:];
-[CAFSeatFan vehicleLayoutKey];
-[CAFSeatFan _characteristicDidUpdate:fromGroupUpdate:];
-[CAFSeatFan autoModeCharacteristic];
-[CAFSeatFan fanLevelCharacteristic];
-[CAFSeatFan fanLevelRestricted];
-[CAFSeatFan onCharacteristic];
-[CAFSeatFan vehicleLayoutKeyCharacteristic];
```
