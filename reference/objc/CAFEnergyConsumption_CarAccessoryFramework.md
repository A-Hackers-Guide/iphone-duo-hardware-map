# `CAFEnergyConsumption`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 17 properties, 26 instance methods, 2 class methods

## Properties

```
@property (T@"CAFMeasurementCharacteristic",R,N) energyEfficiencyCharacteristic;
@property (T@"CAFMeasurementCharacteristic",R,N) averageEnergyEfficiencyCharacteristic;
@property (T@"CAFMeasurementCharacteristic",R,N) energyEfficiencyMaxCharacteristic;
@property (T@"NSMeasurement",R,N) energyEfficiency;
@property (T@"CAFFloatRange",R,N) energyEfficiencyRange;
@property (T@"CAFMeasurementRange",R,N) energyEfficiencyMeasurementRange;
@property (TB,R,N) energyEfficiencyInvalid;
@property (T@"NSMeasurement",R,N) averageEnergyEfficiency;
@property (T@"CAFFloatRange",R,N) averageEnergyEfficiencyRange;
@property (T@"CAFMeasurementRange",R,N) averageEnergyEfficiencyMeasurementRange;
@property (TB,R,N) hasAverageEnergyEfficiency;
@property (TB,R,N) averageEnergyEfficiencyInvalid;
@property (TB,R,N) averageEnergyEfficiencyHidden;
@property (T@"NSMeasurement",R,N) energyEfficiencyMax;
@property (T@"CAFFloatRange",R,N) energyEfficiencyMaxRange;
@property (T@"CAFMeasurementRange",R,N) energyEfficiencyMaxMeasurementRange;
@property (TB,R,N) hasEnergyEfficiencyMax;
```

## Class methods

```
+[CAFEnergyConsumption serviceIdentifier];
+[CAFEnergyConsumption observerProtocol];
```

## Instance methods

```
-[CAFEnergyConsumption removeObserver:];
-[CAFEnergyConsumption addObserver:];
-[CAFEnergyConsumption registerObserver:];
-[CAFEnergyConsumption name];
-[CAFEnergyConsumption unregisterObserver:];
-[CAFEnergyConsumption averageEnergyEfficiency];
-[CAFEnergyConsumption energyEfficiency];
-[CAFEnergyConsumption energyEfficiencyMax];
-[CAFEnergyConsumption registeredForAverageEnergyEfficiency];
-[CAFEnergyConsumption registeredForEnergyEfficiency];
-[CAFEnergyConsumption registeredForEnergyEfficiencyMax];
-[CAFEnergyConsumption energyEfficiencyInvalid];
-[CAFEnergyConsumption _characteristicDidUpdate:fromGroupUpdate:];
-[CAFEnergyConsumption averageEnergyEfficiencyCharacteristic];
-[CAFEnergyConsumption averageEnergyEfficiencyHidden];
-[CAFEnergyConsumption averageEnergyEfficiencyInvalid];
-[CAFEnergyConsumption averageEnergyEfficiencyMeasurementRange];
-[CAFEnergyConsumption averageEnergyEfficiencyRange];
-[CAFEnergyConsumption energyEfficiencyCharacteristic];
-[CAFEnergyConsumption energyEfficiencyMaxCharacteristic];
-[CAFEnergyConsumption energyEfficiencyMaxMeasurementRange];
-[CAFEnergyConsumption energyEfficiencyMaxRange];
-[CAFEnergyConsumption energyEfficiencyMeasurementRange];
-[CAFEnergyConsumption energyEfficiencyRange];
-[CAFEnergyConsumption hasAverageEnergyEfficiency];
-[CAFEnergyConsumption hasEnergyEfficiencyMax];
```
