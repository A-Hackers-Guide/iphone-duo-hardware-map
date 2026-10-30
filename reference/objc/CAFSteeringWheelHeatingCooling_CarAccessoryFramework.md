# `CAFSteeringWheelHeatingCooling`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 9 properties, 18 instance methods, 2 class methods

## Properties

```
@property (T@"CAFInt32Characteristic",R,N) heatingCoolingLevelCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) autoModeCharacteristic;
@property (Ti,N) heatingCoolingLevel;
@property (T@"CAFInt32Range",R,N) heatingCoolingLevelRange;
@property (TB,R,N) heatingCoolingLevelDisabled;
@property (TB,R,N) heatingCoolingLevelInvalid;
@property (TB,R,N) heatingCoolingLevelRestricted;
@property (TB,R,N) autoMode;
@property (TB,R,N) hasAutoMode;
```

## Class methods

```
+[CAFSteeringWheelHeatingCooling serviceIdentifier];
+[CAFSteeringWheelHeatingCooling observerProtocol];
```

## Instance methods

```
-[CAFSteeringWheelHeatingCooling removeObserver:];
-[CAFSteeringWheelHeatingCooling addObserver:];
-[CAFSteeringWheelHeatingCooling registerObserver:];
-[CAFSteeringWheelHeatingCooling name];
-[CAFSteeringWheelHeatingCooling unregisterObserver:];
-[CAFSteeringWheelHeatingCooling autoMode];
-[CAFSteeringWheelHeatingCooling hasAutoMode];
-[CAFSteeringWheelHeatingCooling heatingCoolingLevel];
-[CAFSteeringWheelHeatingCooling registeredForAutoMode];
-[CAFSteeringWheelHeatingCooling registeredForHeatingCoolingLevel];
-[CAFSteeringWheelHeatingCooling setHeatingCoolingLevel:];
-[CAFSteeringWheelHeatingCooling heatingCoolingLevelDisabled];
-[CAFSteeringWheelHeatingCooling _characteristicDidUpdate:fromGroupUpdate:];
-[CAFSteeringWheelHeatingCooling autoModeCharacteristic];
-[CAFSteeringWheelHeatingCooling heatingCoolingLevelCharacteristic];
-[CAFSteeringWheelHeatingCooling heatingCoolingLevelInvalid];
-[CAFSteeringWheelHeatingCooling heatingCoolingLevelRange];
-[CAFSteeringWheelHeatingCooling heatingCoolingLevelRestricted];
```
