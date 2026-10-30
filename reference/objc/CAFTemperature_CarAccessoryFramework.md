# `CAFTemperature`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- Protocols: `CAFPositionedRequired`
- 0 instance variables, 37 properties, 48 instance methods, 3 class methods

## Properties

```
@property (T@"CAFMeasurementCharacteristic",R,N) currentTemperatureCharacteristic;
@property (T@"CAFMeasurementCharacteristic",R,N) targetTemperatureCharacteristic;
@property (T@"CAFMeasurementCharacteristic",R,N) targetTemperatureFahrenheitCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) onCharacteristic;
@property (T@"CAFTemperatureMinMaxLabelCharacteristic",R,N) temperatureMinMaxLabelCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) vehicleLayoutKeyCharacteristic;
@property (T@"NSMeasurement",R,N) currentTemperature;
@property (T@"CAFFloatRange",R,N) currentTemperatureRange;
@property (T@"CAFMeasurementRange",R,N) currentTemperatureMeasurementRange;
@property (TB,R,N) hasCurrentTemperature;
@property (TB,R,N) currentTemperatureInvalid;
@property (T@"NSMeasurement",C,N) targetTemperature;
@property (T@"CAFFloatRange",R,N) targetTemperatureRange;
@property (T@"CAFMeasurementRange",R,N) targetTemperatureMeasurementRange;
@property (TB,R,N) targetTemperatureDisabled;
@property (TB,R,N) targetTemperatureInvalid;
@property (TB,R,N) targetTemperatureRestricted;
@property (T@"NSMeasurement",C,N) targetTemperatureFahrenheit;
@property (T@"CAFFloatRange",R,N) targetTemperatureFahrenheitRange;
@property (T@"CAFMeasurementRange",R,N) targetTemperatureFahrenheitMeasurementRange;
@property (TB,R,N) hasTargetTemperatureFahrenheit;
@property (TB,R,N) targetTemperatureFahrenheitDisabled;
@property (TB,R,N) targetTemperatureFahrenheitInvalid;
@property (TB,R,N) targetTemperatureFahrenheitRestricted;
@property (TB,N) on;
@property (TB,R,N) hasOn;
@property (TB,R,N) onDisabled;
@property (TB,R,N) onInvalid;
@property (TB,R,N) onRestricted;
@property (TC,R,N) temperatureMinMaxLabel;
@property (TB,R,N) hasTemperatureMinMaxLabel;
@property (T@"NSString",R,N) vehicleLayoutKey;
@property (T@"NSString",R,N) positionKey;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CAFTemperature serviceIdentifier];
+[CAFTemperature indexBy];
+[CAFTemperature observerProtocol];
```

## Instance methods

```
-[CAFTemperature on];
-[CAFTemperature removeObserver:];
-[CAFTemperature addObserver:];
-[CAFTemperature setOn:];
-[CAFTemperature registerObserver:];
-[CAFTemperature name];
-[CAFTemperature unregisterObserver:];
-[CAFTemperature positionKey];
-[CAFTemperature currentTemperature];
-[CAFTemperature setTargetTemperature:];
-[CAFTemperature targetTemperature];
-[CAFTemperature registeredForCurrentTemperature];
-[CAFTemperature registeredForOn];
-[CAFTemperature setTargetTemperatureFahrenheit:];
-[CAFTemperature hasOn];
-[CAFTemperature hasTargetTemperatureFahrenheit];
-[CAFTemperature hasTemperatureMinMaxLabel];
-[CAFTemperature onDisabled];
-[CAFTemperature onInvalid];
-[CAFTemperature onRestricted];
-[CAFTemperature registeredForTargetTemperature];
-[CAFTemperature registeredForTargetTemperatureFahrenheit];
-[CAFTemperature registeredForTemperatureMinMaxLabel];
-[CAFTemperature registeredForVehicleLayoutKey];
-[CAFTemperature targetTemperatureDisabled];
-[CAFTemperature targetTemperatureFahrenheit];
-[CAFTemperature targetTemperatureFahrenheitDisabled];
-[CAFTemperature targetTemperatureFahrenheitInvalid];
-[CAFTemperature targetTemperatureFahrenheitMeasurementRange];
-[CAFTemperature targetTemperatureFahrenheitRange];
-[CAFTemperature targetTemperatureFahrenheitRestricted];
-[CAFTemperature targetTemperatureInvalid];
-[CAFTemperature targetTemperatureMeasurementRange];
-[CAFTemperature targetTemperatureRange];
-[CAFTemperature targetTemperatureRestricted];
-[CAFTemperature temperatureMinMaxLabel];
-[CAFTemperature vehicleLayoutKey];
-[CAFTemperature targetTemperatureCharacteristic];
-[CAFTemperature _characteristicDidUpdate:fromGroupUpdate:];
-[CAFTemperature currentTemperatureCharacteristic];
-[CAFTemperature currentTemperatureInvalid];
-[CAFTemperature currentTemperatureMeasurementRange];
-[CAFTemperature currentTemperatureRange];
-[CAFTemperature hasCurrentTemperature];
-[CAFTemperature onCharacteristic];
-[CAFTemperature targetTemperatureFahrenheitCharacteristic];
-[CAFTemperature temperatureMinMaxLabelCharacteristic];
-[CAFTemperature vehicleLayoutKeyCharacteristic];
```
