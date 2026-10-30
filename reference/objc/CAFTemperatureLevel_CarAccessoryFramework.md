# `CAFTemperatureLevel`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- Protocols: `CAFPositionedRequired`
- 0 instance variables, 18 properties, 25 instance methods, 3 class methods

## Properties

```
@property (T@"CAFInt32Characteristic",R,N) heatingCoolingLevelCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) onCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) vehicleLayoutKeyCharacteristic;
@property (Ti,N) heatingCoolingLevel;
@property (T@"CAFInt32Range",R,N) heatingCoolingLevelRange;
@property (TB,R,N) heatingCoolingLevelDisabled;
@property (TB,R,N) heatingCoolingLevelInvalid;
@property (TB,R,N) heatingCoolingLevelRestricted;
@property (TB,N) on;
@property (TB,R,N) hasOn;
@property (TB,R,N) onDisabled;
@property (TB,R,N) onInvalid;
@property (TB,R,N) onRestricted;
@property (T@"NSString",R,N) vehicleLayoutKey;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CAFTemperatureLevel serviceIdentifier];
+[CAFTemperatureLevel indexBy];
+[CAFTemperatureLevel observerProtocol];
```

## Instance methods

```
-[CAFTemperatureLevel on];
-[CAFTemperatureLevel removeObserver:];
-[CAFTemperatureLevel addObserver:];
-[CAFTemperatureLevel setOn:];
-[CAFTemperatureLevel registerObserver:];
-[CAFTemperatureLevel name];
-[CAFTemperatureLevel unregisterObserver:];
-[CAFTemperatureLevel registeredForOn];
-[CAFTemperatureLevel hasOn];
-[CAFTemperatureLevel heatingCoolingLevel];
-[CAFTemperatureLevel onDisabled];
-[CAFTemperatureLevel onInvalid];
-[CAFTemperatureLevel onRestricted];
-[CAFTemperatureLevel registeredForHeatingCoolingLevel];
-[CAFTemperatureLevel registeredForVehicleLayoutKey];
-[CAFTemperatureLevel setHeatingCoolingLevel:];
-[CAFTemperatureLevel vehicleLayoutKey];
-[CAFTemperatureLevel heatingCoolingLevelDisabled];
-[CAFTemperatureLevel _characteristicDidUpdate:fromGroupUpdate:];
-[CAFTemperatureLevel heatingCoolingLevelCharacteristic];
-[CAFTemperatureLevel heatingCoolingLevelInvalid];
-[CAFTemperatureLevel heatingCoolingLevelRange];
-[CAFTemperatureLevel heatingCoolingLevelRestricted];
-[CAFTemperatureLevel onCharacteristic];
-[CAFTemperatureLevel vehicleLayoutKeyCharacteristic];
```
