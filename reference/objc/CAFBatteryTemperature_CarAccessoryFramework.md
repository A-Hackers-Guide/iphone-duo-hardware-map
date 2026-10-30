# `CAFBatteryTemperature`

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
+[CAFBatteryTemperature serviceIdentifier];
+[CAFBatteryTemperature observerProtocol];
```

## Instance methods

```
-[CAFBatteryTemperature removeObserver:];
-[CAFBatteryTemperature addObserver:];
-[CAFBatteryTemperature registerObserver:];
-[CAFBatteryTemperature name];
-[CAFBatteryTemperature temperature];
-[CAFBatteryTemperature unregisterObserver:];
-[CAFBatteryTemperature registeredForTemperature];
-[CAFBatteryTemperature registeredForTemperatureMarkerCold];
-[CAFBatteryTemperature registeredForTemperatureMarkerHot];
-[CAFBatteryTemperature registeredForTemperatureMax];
-[CAFBatteryTemperature registeredForTemperatureMin];
-[CAFBatteryTemperature registeredForTemperatureState];
-[CAFBatteryTemperature temperatureMarkerCold];
-[CAFBatteryTemperature temperatureMarkerHot];
-[CAFBatteryTemperature temperatureMax];
-[CAFBatteryTemperature temperatureMin];
-[CAFBatteryTemperature temperatureState];
-[CAFBatteryTemperature _characteristicDidUpdate:fromGroupUpdate:];
-[CAFBatteryTemperature hasTemperatureMarkerCold];
-[CAFBatteryTemperature hasTemperatureMarkerHot];
-[CAFBatteryTemperature temperatureCharacteristic];
-[CAFBatteryTemperature temperatureInvalid];
-[CAFBatteryTemperature temperatureMarkerColdCharacteristic];
-[CAFBatteryTemperature temperatureMarkerColdMeasurementRange];
-[CAFBatteryTemperature temperatureMarkerColdRange];
-[CAFBatteryTemperature temperatureMarkerHotCharacteristic];
-[CAFBatteryTemperature temperatureMarkerHotMeasurementRange];
-[CAFBatteryTemperature temperatureMarkerHotRange];
-[CAFBatteryTemperature temperatureMaxCharacteristic];
-[CAFBatteryTemperature temperatureMaxMeasurementRange];
-[CAFBatteryTemperature temperatureMaxRange];
-[CAFBatteryTemperature temperatureMeasurementRange];
-[CAFBatteryTemperature temperatureMinCharacteristic];
-[CAFBatteryTemperature temperatureMinMeasurementRange];
-[CAFBatteryTemperature temperatureMinRange];
-[CAFBatteryTemperature temperatureRange];
-[CAFBatteryTemperature temperatureStateCharacteristic];
```
