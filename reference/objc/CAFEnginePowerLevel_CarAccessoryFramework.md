# `CAFEnginePowerLevel`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 18 properties, 28 instance methods, 2 class methods

## Properties

```
@property (T@"CAFMeasurementCharacteristic",R,N) powerLevelCharacteristic;
@property (T@"CAFMeasurementCharacteristic",R,N) powerLevelMarkerAvailableMinCharacteristic;
@property (T@"CAFMeasurementCharacteristic",R,N) powerLevelMarkerAvailableMaxCharacteristic;
@property (T@"CAFPowerStateCharacteristic",R,N) powerStateCharacteristic;
@property (T@"NSMeasurement",R,N) powerLevel;
@property (T@"CAFFloatRange",R,N) powerLevelRange;
@property (T@"CAFMeasurementRange",R,N) powerLevelMeasurementRange;
@property (TB,R,N) powerLevelInvalid;
@property (T@"NSMeasurement",R,N) powerLevelMarkerAvailableMin;
@property (T@"CAFFloatRange",R,N) powerLevelMarkerAvailableMinRange;
@property (T@"CAFMeasurementRange",R,N) powerLevelMarkerAvailableMinMeasurementRange;
@property (TB,R,N) hasPowerLevelMarkerAvailableMin;
@property (T@"NSMeasurement",R,N) powerLevelMarkerAvailableMax;
@property (T@"CAFFloatRange",R,N) powerLevelMarkerAvailableMaxRange;
@property (T@"CAFMeasurementRange",R,N) powerLevelMarkerAvailableMaxMeasurementRange;
@property (TB,R,N) hasPowerLevelMarkerAvailableMax;
@property (TC,R,N) powerState;
@property (TB,R,N) hasPowerState;
```

## Class methods

```
+[CAFEnginePowerLevel serviceIdentifier];
+[CAFEnginePowerLevel observerProtocol];
```

## Instance methods

```
-[CAFEnginePowerLevel powerState];
-[CAFEnginePowerLevel removeObserver:];
-[CAFEnginePowerLevel addObserver:];
-[CAFEnginePowerLevel registerObserver:];
-[CAFEnginePowerLevel name];
-[CAFEnginePowerLevel unregisterObserver:];
-[CAFEnginePowerLevel powerLevel];
-[CAFEnginePowerLevel hasPowerState];
-[CAFEnginePowerLevel powerLevelMarkerAvailableMax];
-[CAFEnginePowerLevel powerLevelMarkerAvailableMin];
-[CAFEnginePowerLevel registeredForPowerLevel];
-[CAFEnginePowerLevel registeredForPowerLevelMarkerAvailableMax];
-[CAFEnginePowerLevel registeredForPowerLevelMarkerAvailableMin];
-[CAFEnginePowerLevel registeredForPowerState];
-[CAFEnginePowerLevel hasPowerLevelMarkerAvailableMin];
-[CAFEnginePowerLevel powerLevelRange];
-[CAFEnginePowerLevel hasPowerLevelMarkerAvailableMax];
-[CAFEnginePowerLevel _characteristicDidUpdate:fromGroupUpdate:];
-[CAFEnginePowerLevel powerLevelCharacteristic];
-[CAFEnginePowerLevel powerLevelInvalid];
-[CAFEnginePowerLevel powerLevelMarkerAvailableMaxCharacteristic];
-[CAFEnginePowerLevel powerLevelMarkerAvailableMaxMeasurementRange];
-[CAFEnginePowerLevel powerLevelMarkerAvailableMaxRange];
-[CAFEnginePowerLevel powerLevelMarkerAvailableMinCharacteristic];
-[CAFEnginePowerLevel powerLevelMarkerAvailableMinMeasurementRange];
-[CAFEnginePowerLevel powerLevelMarkerAvailableMinRange];
-[CAFEnginePowerLevel powerLevelMeasurementRange];
-[CAFEnginePowerLevel powerStateCharacteristic];
```
