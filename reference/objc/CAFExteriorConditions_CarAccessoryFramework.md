# `CAFExteriorConditions`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 15 properties, 24 instance methods, 2 class methods

## Properties

```
@property (T@"CAFMeasurementCharacteristic",R,N) temperatureCharacteristic;
@property (T@"CAFIcyConditionsCharacteristic",R,N) icyConditionsCharacteristic;
@property (T@"CAFMeasurementCharacteristic",R,N) aqiCharacteristic;
@property (T@"NSMeasurement",R,N) temperature;
@property (T@"CAFFloatRange",R,N) temperatureRange;
@property (T@"CAFMeasurementRange",R,N) temperatureMeasurementRange;
@property (TB,R,N) temperatureInvalid;
@property (TB,R,N) temperatureHidden;
@property (TC,R,N) icyConditions;
@property (TB,R,N) hasIcyConditions;
@property (T@"NSMeasurement",R,N) aqi;
@property (T@"CAFFloatRange",R,N) aqiRange;
@property (T@"CAFMeasurementRange",R,N) aqiMeasurementRange;
@property (TB,R,N) hasAqi;
@property (TB,R,N) aqiInvalid;
```

## Class methods

```
+[CAFExteriorConditions serviceIdentifier];
+[CAFExteriorConditions observerProtocol];
```

## Instance methods

```
-[CAFExteriorConditions removeObserver:];
-[CAFExteriorConditions addObserver:];
-[CAFExteriorConditions registerObserver:];
-[CAFExteriorConditions name];
-[CAFExteriorConditions temperature];
-[CAFExteriorConditions unregisterObserver:];
-[CAFExteriorConditions aqi];
-[CAFExteriorConditions hasIcyConditions];
-[CAFExteriorConditions icyConditions];
-[CAFExteriorConditions registeredForAQI];
-[CAFExteriorConditions registeredForIcyConditions];
-[CAFExteriorConditions registeredForTemperature];
-[CAFExteriorConditions _characteristicDidUpdate:fromGroupUpdate:];
-[CAFExteriorConditions aqiCharacteristic];
-[CAFExteriorConditions aqiInvalid];
-[CAFExteriorConditions aqiMeasurementRange];
-[CAFExteriorConditions aqiRange];
-[CAFExteriorConditions hasAqi];
-[CAFExteriorConditions icyConditionsCharacteristic];
-[CAFExteriorConditions temperatureCharacteristic];
-[CAFExteriorConditions temperatureHidden];
-[CAFExteriorConditions temperatureInvalid];
-[CAFExteriorConditions temperatureMeasurementRange];
-[CAFExteriorConditions temperatureRange];
```
