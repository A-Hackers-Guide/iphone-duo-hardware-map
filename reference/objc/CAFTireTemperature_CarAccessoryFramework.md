# `CAFTireTemperature`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- Protocols: `CAFPositionedRequired`
- 0 instance variables, 13 properties, 18 instance methods, 3 class methods

## Properties

```
@property (T@"CAFMeasurementCharacteristic",R,N) temperatureCharacteristic;
@property (T@"CAFTemperatureStateCharacteristic",R,N) temperatureStateCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) vehicleLayoutKeyCharacteristic;
@property (T@"NSMeasurement",R,N) temperature;
@property (T@"CAFFloatRange",R,N) temperatureRange;
@property (T@"CAFMeasurementRange",R,N) temperatureMeasurementRange;
@property (TB,R,N) temperatureInvalid;
@property (TC,R,N) temperatureState;
@property (T@"NSString",R,N) vehicleLayoutKey;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CAFTireTemperature serviceIdentifier];
+[CAFTireTemperature indexBy];
+[CAFTireTemperature observerProtocol];
```

## Instance methods

```
-[CAFTireTemperature removeObserver:];
-[CAFTireTemperature addObserver:];
-[CAFTireTemperature registerObserver:];
-[CAFTireTemperature name];
-[CAFTireTemperature temperature];
-[CAFTireTemperature unregisterObserver:];
-[CAFTireTemperature registeredForTemperature];
-[CAFTireTemperature registeredForTemperatureState];
-[CAFTireTemperature registeredForVehicleLayoutKey];
-[CAFTireTemperature temperatureState];
-[CAFTireTemperature vehicleLayoutKey];
-[CAFTireTemperature _characteristicDidUpdate:fromGroupUpdate:];
-[CAFTireTemperature temperatureCharacteristic];
-[CAFTireTemperature temperatureInvalid];
-[CAFTireTemperature temperatureMeasurementRange];
-[CAFTireTemperature temperatureRange];
-[CAFTireTemperature temperatureStateCharacteristic];
-[CAFTireTemperature vehicleLayoutKeyCharacteristic];
```
