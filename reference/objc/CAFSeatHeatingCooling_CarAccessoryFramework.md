# `CAFSeatHeatingCooling`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- Protocols: `CAFPositionedRequired`
- 0 instance variables, 22 properties, 30 instance methods, 3 class methods

## Properties

```
@property (T@"CAFBoolCharacteristic",R,N) onCharacteristic;
@property (T@"CAFInt32Characteristic",R,N) heatingCoolingLevelCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) autoModeCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) vehicleLayoutKeyCharacteristic;
@property (TB,N) on;
@property (TB,R,N) hasOn;
@property (TB,R,N) onDisabled;
@property (TB,R,N) onInvalid;
@property (TB,R,N) onRestricted;
@property (Ti,N) heatingCoolingLevel;
@property (T@"CAFInt32Range",R,N) heatingCoolingLevelRange;
@property (TB,R,N) heatingCoolingLevelDisabled;
@property (TB,R,N) heatingCoolingLevelInvalid;
@property (TB,R,N) heatingCoolingLevelRestricted;
@property (TB,R,N) autoMode;
@property (TB,R,N) hasAutoMode;
@property (T@"NSString",R,N) vehicleLayoutKey;
@property (T@"NSString",R,N) positionKey;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CAFSeatHeatingCooling serviceIdentifier];
+[CAFSeatHeatingCooling indexBy];
+[CAFSeatHeatingCooling observerProtocol];
```

## Instance methods

```
-[CAFSeatHeatingCooling on];
-[CAFSeatHeatingCooling removeObserver:];
-[CAFSeatHeatingCooling addObserver:];
-[CAFSeatHeatingCooling setOn:];
-[CAFSeatHeatingCooling registerObserver:];
-[CAFSeatHeatingCooling name];
-[CAFSeatHeatingCooling unregisterObserver:];
-[CAFSeatHeatingCooling positionKey];
-[CAFSeatHeatingCooling registeredForOn];
-[CAFSeatHeatingCooling autoMode];
-[CAFSeatHeatingCooling hasAutoMode];
-[CAFSeatHeatingCooling hasOn];
-[CAFSeatHeatingCooling heatingCoolingLevel];
-[CAFSeatHeatingCooling onDisabled];
-[CAFSeatHeatingCooling onInvalid];
-[CAFSeatHeatingCooling onRestricted];
-[CAFSeatHeatingCooling registeredForAutoMode];
-[CAFSeatHeatingCooling registeredForHeatingCoolingLevel];
-[CAFSeatHeatingCooling registeredForVehicleLayoutKey];
-[CAFSeatHeatingCooling setHeatingCoolingLevel:];
-[CAFSeatHeatingCooling vehicleLayoutKey];
-[CAFSeatHeatingCooling heatingCoolingLevelDisabled];
-[CAFSeatHeatingCooling _characteristicDidUpdate:fromGroupUpdate:];
-[CAFSeatHeatingCooling autoModeCharacteristic];
-[CAFSeatHeatingCooling heatingCoolingLevelCharacteristic];
-[CAFSeatHeatingCooling heatingCoolingLevelInvalid];
-[CAFSeatHeatingCooling heatingCoolingLevelRange];
-[CAFSeatHeatingCooling heatingCoolingLevelRestricted];
-[CAFSeatHeatingCooling onCharacteristic];
-[CAFSeatHeatingCooling vehicleLayoutKeyCharacteristic];
```
