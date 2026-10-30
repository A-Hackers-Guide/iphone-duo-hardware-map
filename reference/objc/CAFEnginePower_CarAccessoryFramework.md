# `CAFEnginePower`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 26 properties, 38 instance methods, 2 class methods

## Properties

```
@property (T@"CAFMeasurementCharacteristic",R,N) powerCharacteristic;
@property (T@"CAFMeasurementCharacteristic",R,N) powerMinCharacteristic;
@property (T@"CAFMeasurementCharacteristic",R,N) powerMaxCharacteristic;
@property (T@"CAFMeasurementCharacteristic",R,N) powerMarkerAvailableMinCharacteristic;
@property (T@"CAFMeasurementCharacteristic",R,N) powerMarkerAvailableMaxCharacteristic;
@property (T@"CAFPowerStateCharacteristic",R,N) powerStateCharacteristic;
@property (T@"NSMeasurement",R,N) power;
@property (T@"CAFInt32Range",R,N) powerRange;
@property (T@"CAFMeasurementRange",R,N) powerMeasurementRange;
@property (TB,R,N) powerInvalid;
@property (T@"NSMeasurement",R,N) powerMin;
@property (T@"CAFInt32Range",R,N) powerMinRange;
@property (T@"CAFMeasurementRange",R,N) powerMinMeasurementRange;
@property (T@"NSMeasurement",R,N) powerMax;
@property (T@"CAFInt32Range",R,N) powerMaxRange;
@property (T@"CAFMeasurementRange",R,N) powerMaxMeasurementRange;
@property (T@"NSMeasurement",R,N) powerMarkerAvailableMin;
@property (T@"CAFInt32Range",R,N) powerMarkerAvailableMinRange;
@property (T@"CAFMeasurementRange",R,N) powerMarkerAvailableMinMeasurementRange;
@property (TB,R,N) hasPowerMarkerAvailableMin;
@property (T@"NSMeasurement",R,N) powerMarkerAvailableMax;
@property (T@"CAFInt32Range",R,N) powerMarkerAvailableMaxRange;
@property (T@"CAFMeasurementRange",R,N) powerMarkerAvailableMaxMeasurementRange;
@property (TB,R,N) hasPowerMarkerAvailableMax;
@property (TC,R,N) powerState;
@property (TB,R,N) hasPowerState;
```

## Class methods

```
+[CAFEnginePower serviceIdentifier];
+[CAFEnginePower observerProtocol];
```

## Instance methods

```
-[CAFEnginePower power];
-[CAFEnginePower powerState];
-[CAFEnginePower removeObserver:];
-[CAFEnginePower addObserver:];
-[CAFEnginePower registerObserver:];
-[CAFEnginePower name];
-[CAFEnginePower unregisterObserver:];
-[CAFEnginePower hasPowerState];
-[CAFEnginePower powerMarkerAvailableMax];
-[CAFEnginePower powerMarkerAvailableMin];
-[CAFEnginePower powerMax];
-[CAFEnginePower powerMin];
-[CAFEnginePower registeredForPower];
-[CAFEnginePower registeredForPowerMarkerAvailableMax];
-[CAFEnginePower registeredForPowerMarkerAvailableMin];
-[CAFEnginePower registeredForPowerMax];
-[CAFEnginePower registeredForPowerMin];
-[CAFEnginePower registeredForPowerState];
-[CAFEnginePower _characteristicDidUpdate:fromGroupUpdate:];
-[CAFEnginePower hasPowerMarkerAvailableMax];
-[CAFEnginePower hasPowerMarkerAvailableMin];
-[CAFEnginePower powerCharacteristic];
-[CAFEnginePower powerInvalid];
-[CAFEnginePower powerMarkerAvailableMaxCharacteristic];
-[CAFEnginePower powerMarkerAvailableMaxMeasurementRange];
-[CAFEnginePower powerMarkerAvailableMaxRange];
-[CAFEnginePower powerMarkerAvailableMinCharacteristic];
-[CAFEnginePower powerMarkerAvailableMinMeasurementRange];
-[CAFEnginePower powerMarkerAvailableMinRange];
-[CAFEnginePower powerMaxCharacteristic];
-[CAFEnginePower powerMaxMeasurementRange];
-[CAFEnginePower powerMaxRange];
-[CAFEnginePower powerMeasurementRange];
-[CAFEnginePower powerMinCharacteristic];
-[CAFEnginePower powerMinMeasurementRange];
-[CAFEnginePower powerMinRange];
-[CAFEnginePower powerRange];
-[CAFEnginePower powerStateCharacteristic];
```
