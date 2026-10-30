# `CAFFuelConsumption`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 17 properties, 26 instance methods, 2 class methods

## Properties

```
@property (T@"CAFMeasurementCharacteristic",R,N) fuelEfficiencyCharacteristic;
@property (T@"CAFMeasurementCharacteristic",R,N) averageFuelEfficiencyCharacteristic;
@property (T@"CAFMeasurementCharacteristic",R,N) fuelEfficiencyMaxCharacteristic;
@property (T@"NSMeasurement",R,N) fuelEfficiency;
@property (T@"CAFFloatRange",R,N) fuelEfficiencyRange;
@property (T@"CAFMeasurementRange",R,N) fuelEfficiencyMeasurementRange;
@property (TB,R,N) fuelEfficiencyInvalid;
@property (T@"NSMeasurement",R,N) averageFuelEfficiency;
@property (T@"CAFFloatRange",R,N) averageFuelEfficiencyRange;
@property (T@"CAFMeasurementRange",R,N) averageFuelEfficiencyMeasurementRange;
@property (TB,R,N) hasAverageFuelEfficiency;
@property (TB,R,N) averageFuelEfficiencyInvalid;
@property (TB,R,N) averageFuelEfficiencyHidden;
@property (T@"NSMeasurement",R,N) fuelEfficiencyMax;
@property (T@"CAFFloatRange",R,N) fuelEfficiencyMaxRange;
@property (T@"CAFMeasurementRange",R,N) fuelEfficiencyMaxMeasurementRange;
@property (TB,R,N) hasFuelEfficiencyMax;
```

## Class methods

```
+[CAFFuelConsumption serviceIdentifier];
+[CAFFuelConsumption observerProtocol];
```

## Instance methods

```
-[CAFFuelConsumption removeObserver:];
-[CAFFuelConsumption addObserver:];
-[CAFFuelConsumption registerObserver:];
-[CAFFuelConsumption name];
-[CAFFuelConsumption unregisterObserver:];
-[CAFFuelConsumption averageFuelEfficiency];
-[CAFFuelConsumption fuelEfficiency];
-[CAFFuelConsumption fuelEfficiencyMax];
-[CAFFuelConsumption registeredForAverageFuelEfficiency];
-[CAFFuelConsumption registeredForFuelEfficiency];
-[CAFFuelConsumption registeredForFuelEfficiencyMax];
-[CAFFuelConsumption fuelEfficiencyInvalid];
-[CAFFuelConsumption fuelEfficiencyMaxCharacteristic];
-[CAFFuelConsumption _characteristicDidUpdate:fromGroupUpdate:];
-[CAFFuelConsumption averageFuelEfficiencyCharacteristic];
-[CAFFuelConsumption averageFuelEfficiencyHidden];
-[CAFFuelConsumption averageFuelEfficiencyInvalid];
-[CAFFuelConsumption averageFuelEfficiencyMeasurementRange];
-[CAFFuelConsumption averageFuelEfficiencyRange];
-[CAFFuelConsumption fuelEfficiencyCharacteristic];
-[CAFFuelConsumption fuelEfficiencyMaxMeasurementRange];
-[CAFFuelConsumption fuelEfficiencyMaxRange];
-[CAFFuelConsumption fuelEfficiencyMeasurementRange];
-[CAFFuelConsumption fuelEfficiencyRange];
-[CAFFuelConsumption hasAverageFuelEfficiency];
-[CAFFuelConsumption hasFuelEfficiencyMax];
```
