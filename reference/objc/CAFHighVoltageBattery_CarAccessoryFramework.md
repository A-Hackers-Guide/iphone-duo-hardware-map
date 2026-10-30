# `CAFHighVoltageBattery`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFAccessory`
- 0 instance variables, 10 properties, 14 instance methods, 2 class methods

## Properties

```
@property (T@"CAFBatteryLevel",R,N) batteryLevelService;
@property (T@"CAFBatteryTemperature",R,N) batteryTemperatureService;
@property (T@"CAFBatteryRemainingRange",R,N) batteryRemainingRangeService;
@property (T@"CAFBatteryConditioning",R,N) batteryConditioningService;
@property (T@"CAFEnergyConsumption",R,N) energyConsumptionService;
@property (T@"CAFBatteryLevel",R,N) batteryLevel;
@property (T@"CAFBatteryTemperature",R,N) batteryTemperature;
@property (T@"CAFBatteryRemainingRange",R,N) batteryRemainingRange;
@property (T@"CAFBatteryConditioning",R,N) batteryConditioning;
@property (T@"CAFEnergyConsumption",R,N) energyConsumption;
```

## Class methods

```
+[CAFHighVoltageBattery accessoryIdentifier];
+[CAFHighVoltageBattery observerProtocol];
```

## Instance methods

```
-[CAFHighVoltageBattery batteryLevel];
-[CAFHighVoltageBattery removeObserver:];
-[CAFHighVoltageBattery batteryTemperature];
-[CAFHighVoltageBattery addObserver:];
-[CAFHighVoltageBattery registerObserver:];
-[CAFHighVoltageBattery unregisterObserver:];
-[CAFHighVoltageBattery energyConsumption];
-[CAFHighVoltageBattery batteryConditioning];
-[CAFHighVoltageBattery batteryConditioningService];
-[CAFHighVoltageBattery batteryLevelService];
-[CAFHighVoltageBattery batteryRemainingRange];
-[CAFHighVoltageBattery batteryRemainingRangeService];
-[CAFHighVoltageBattery batteryTemperatureService];
-[CAFHighVoltageBattery energyConsumptionService];
```
