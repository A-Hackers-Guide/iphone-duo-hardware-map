# `CAFChargingLevel`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 6 properties, 14 instance methods, 0 class methods

## Properties

```
@property (T@"CAFMeasurementCharacteristic",R,N) chargingLevelCharacteristic;
@property (T@"NSMeasurement",C,N) chargingLevel;
@property (T@"CAFUInt8Range",R,N) chargingLevelRange;
@property (T@"CAFMeasurementRange",R,N) chargingLevelMeasurementRange;
@property (TB,R,N) chargingLevelInvalid;
@property (TB,R,N) chargingLevelHidden;
```

## Instance methods

```
-[CAFChargingLevel removeObserver:];
-[CAFChargingLevel addObserver:];
-[CAFChargingLevel registerObserver:];
-[CAFChargingLevel name];
-[CAFChargingLevel unregisterObserver:];
-[CAFChargingLevel chargingLevel];
-[CAFChargingLevel setChargingLevel:];
-[CAFChargingLevel _characteristicDidUpdate:fromGroupUpdate:];
-[CAFChargingLevel chargingLevelCharacteristic];
-[CAFChargingLevel chargingLevelHidden];
-[CAFChargingLevel chargingLevelInvalid];
-[CAFChargingLevel chargingLevelMeasurementRange];
-[CAFChargingLevel chargingLevelRange];
-[CAFChargingLevel registeredForChargingLevel];
```
