# `CAFInteriorConditions`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 6 properties, 13 instance methods, 2 class methods

## Properties

```
@property (T@"CAFMeasurementCharacteristic",R,N) aqiCharacteristic;
@property (T@"NSMeasurement",R,N) aqi;
@property (T@"CAFFloatRange",R,N) aqiRange;
@property (T@"CAFMeasurementRange",R,N) aqiMeasurementRange;
@property (TB,R,N) hasAqi;
@property (TB,R,N) aqiInvalid;
```

## Class methods

```
+[CAFInteriorConditions serviceIdentifier];
+[CAFInteriorConditions observerProtocol];
```

## Instance methods

```
-[CAFInteriorConditions removeObserver:];
-[CAFInteriorConditions addObserver:];
-[CAFInteriorConditions registerObserver:];
-[CAFInteriorConditions name];
-[CAFInteriorConditions unregisterObserver:];
-[CAFInteriorConditions aqi];
-[CAFInteriorConditions registeredForAQI];
-[CAFInteriorConditions _characteristicDidUpdate:fromGroupUpdate:];
-[CAFInteriorConditions aqiCharacteristic];
-[CAFInteriorConditions aqiInvalid];
-[CAFInteriorConditions aqiMeasurementRange];
-[CAFInteriorConditions aqiRange];
-[CAFInteriorConditions hasAqi];
```
