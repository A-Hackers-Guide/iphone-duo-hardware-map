# `CAFEngineTemperature`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 25 properties, 37 instance methods, 2 class methods

## Properties

```
@property (T@"CAFMeasurementCharacteristic",R,N) temperatureCharacteristic;
@property (T@"CAFTemperatureStateCharacteristic",R,N) temperatureStateCharacteristic;
@property (T@"CAFMeasurementCharacteristic",R,N) temperatureMinCharacteristic;
@property (T@"CAFMeasurementCharacteristic",R,N) temperatureMaxCharacteristic;
@property (T@"CAFMeasurementCharacteristic",R,N) temperatureMarkerColdCharacteristic;
@property (T@"CAFMeasurementCharacteristic",R,N) temperatureMarkerHotCharacteristic;
@property (T@"NSMeasurement",R,N) temperature;
@property (T@"CAFFloatRange",R,N) temperatureRange;
@property (T@"CAFMeasurementRange",R,N) temperatureMeasurementRange;
@property (TB,R,N) temperatureInvalid;
@property (TC,R,N) temperatureState;
@property (T@"NSMeasurement",R,N) temperatureMin;
@property (T@"CAFFloatRange",R,N) temperatureMinRange;
@property (T@"CAFMeasurementRange",R,N) temperatureMinMeasurementRange;
@property (T@"NSMeasurement",R,N) temperatureMax;
@property (T@"CAFFloatRange",R,N) temperatureMaxRange;
@property (T@"CAFMeasurementRange",R,N) temperatureMaxMeasurementRange;
@property (T@"NSMeasurement",R,N) temperatureMarkerCold;
@property (T@"CAFFloatRange",R,N) temperatureMarkerColdRange;
@property (T@"CAFMeasurementRange",R,N) temperatureMarkerColdMeasurementRange;
@property (TB,R,N) hasTemperatureMarkerCold;
@property (T@"NSMeasurement",R,N) temperatureMarkerHot;
@property (T@"CAFFloatRange",R,N) temperatureMarkerHotRange;
@property (T@"CAFMeasurementRange",R,N) temperatureMarkerHotMeasurementRange;
@property (TB,R,N) hasTemperatureMarkerHot;
```

## Class methods

```
+[CAFEngineTemperature serviceIdentifier];
+[CAFEngineTemperature observerProtocol];
```

## Instance methods

```
-[CAFEngineTemperature removeObserver:];
-[CAFEngineTemperature addObserver:];
-[CAFEngineTemperature registerObserver:];
-[CAFEngineTemperature name];
-[CAFEngineTemperature temperature];
-[CAFEngineTemperature unregisterObserver:];
-[CAFEngineTemperature registeredForTemperature];
-[CAFEngineTemperature registeredForTemperatureMarkerCold];
-[CAFEngineTemperature registeredForTemperatureMarkerHot];
-[CAFEngineTemperature registeredForTemperatureMax];
-[CAFEngineTemperature registeredForTemperatureMin];
-[CAFEngineTemperature registeredForTemperatureState];
-[CAFEngineTemperature temperatureMarkerCold];
-[CAFEngineTemperature temperatureMarkerHot];
-[CAFEngineTemperature temperatureMax];
-[CAFEngineTemperature temperatureMin];
-[CAFEngineTemperature temperatureState];
-[CAFEngineTemperature _characteristicDidUpdate:fromGroupUpdate:];
-[CAFEngineTemperature hasTemperatureMarkerCold];
-[CAFEngineTemperature hasTemperatureMarkerHot];
-[CAFEngineTemperature temperatureCharacteristic];
-[CAFEngineTemperature temperatureInvalid];
-[CAFEngineTemperature temperatureMarkerColdCharacteristic];
-[CAFEngineTemperature temperatureMarkerColdMeasurementRange];
-[CAFEngineTemperature temperatureMarkerColdRange];
-[CAFEngineTemperature temperatureMarkerHotCharacteristic];
-[CAFEngineTemperature temperatureMarkerHotMeasurementRange];
-[CAFEngineTemperature temperatureMarkerHotRange];
-[CAFEngineTemperature temperatureMaxCharacteristic];
-[CAFEngineTemperature temperatureMaxMeasurementRange];
-[CAFEngineTemperature temperatureMaxRange];
-[CAFEngineTemperature temperatureMeasurementRange];
-[CAFEngineTemperature temperatureMinCharacteristic];
-[CAFEngineTemperature temperatureMinMeasurementRange];
-[CAFEngineTemperature temperatureMinRange];
-[CAFEngineTemperature temperatureRange];
-[CAFEngineTemperature temperatureStateCharacteristic];
```
