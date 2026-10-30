# `CAFFan`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- Protocols: `CAFPositionedRequired`
- 0 instance variables, 21 properties, 29 instance methods, 3 class methods

## Properties

```
@property (T@"CAFUInt8Characteristic",R,N) fanLevelCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) onCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) autoModeCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) vehicleLayoutKeyCharacteristic;
@property (TC,N) fanLevel;
@property (T@"CAFUInt8Range",R,N) fanLevelRange;
@property (TB,R,N) fanLevelDisabled;
@property (TB,R,N) fanLevelInvalid;
@property (TB,R,N) fanLevelRestricted;
@property (TB,N) on;
@property (TB,R,N) hasOn;
@property (TB,R,N) onDisabled;
@property (TB,R,N) onInvalid;
@property (TB,R,N) onRestricted;
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
+[CAFFan serviceIdentifier];
+[CAFFan indexBy];
+[CAFFan observerProtocol];
```

## Instance methods

```
-[CAFFan on];
-[CAFFan removeObserver:];
-[CAFFan addObserver:];
-[CAFFan setOn:];
-[CAFFan registerObserver:];
-[CAFFan name];
-[CAFFan unregisterObserver:];
-[CAFFan fanLevelInvalid];
-[CAFFan registeredForOn];
-[CAFFan autoMode];
-[CAFFan fanLevel];
-[CAFFan fanLevelDisabled];
-[CAFFan fanLevelRange];
-[CAFFan hasAutoMode];
-[CAFFan hasOn];
-[CAFFan onDisabled];
-[CAFFan onInvalid];
-[CAFFan onRestricted];
-[CAFFan registeredForAutoMode];
-[CAFFan registeredForFanLevel];
-[CAFFan registeredForVehicleLayoutKey];
-[CAFFan setFanLevel:];
-[CAFFan vehicleLayoutKey];
-[CAFFan _characteristicDidUpdate:fromGroupUpdate:];
-[CAFFan autoModeCharacteristic];
-[CAFFan fanLevelCharacteristic];
-[CAFFan fanLevelRestricted];
-[CAFFan onCharacteristic];
-[CAFFan vehicleLayoutKeyCharacteristic];
```
