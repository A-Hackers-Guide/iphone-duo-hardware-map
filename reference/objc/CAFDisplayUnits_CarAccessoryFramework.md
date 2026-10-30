# `CAFDisplayUnits`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 17 properties, 28 instance methods, 2 class methods

## Properties

```
@property (T@"CAFUnitTypeCharacteristic",R,N) speedUnitRawValueCharacteristic;
@property (T@"CAFUnitTypeCharacteristic",R,N) distanceUnitRawValueCharacteristic;
@property (T@"CAFUnitTypeCharacteristic",R,N) temperatureUnitRawValueCharacteristic;
@property (T@"CAFUnitTypeCharacteristic",R,N) energyEfficiencyUnitRawValueCharacteristic;
@property (T@"CAFUnitTypeCharacteristic",R,N) fuelEfficiencyUnitRawValueCharacteristic;
@property (TS,R,N) speedUnitRawValue;
@property (T@"NSUnitSpeed",R,N) speedUnit;
@property (TS,R,N) distanceUnitRawValue;
@property (T@"NSUnitLength",R,N) distanceUnit;
@property (TS,R,N) temperatureUnitRawValue;
@property (T@"NSUnitTemperature",R,N) temperatureUnit;
@property (TS,R,N) energyEfficiencyUnitRawValue;
@property (T@"CAFUnitEnergyEfficiency",R,N) energyEfficiencyUnit;
@property (TB,R,N) hasEnergyEfficiencyUnitRawValue;
@property (TS,R,N) fuelEfficiencyUnitRawValue;
@property (T@"NSUnitFuelEfficiency",R,N) fuelEfficiencyUnit;
@property (TB,R,N) hasFuelEfficiencyUnitRawValue;
```

## Class methods

```
+[CAFDisplayUnits serviceIdentifier];
+[CAFDisplayUnits observerProtocol];
```

## Instance methods

```
-[CAFDisplayUnits removeObserver:];
-[CAFDisplayUnits temperatureUnit];
-[CAFDisplayUnits addObserver:];
-[CAFDisplayUnits registerObserver:];
-[CAFDisplayUnits name];
-[CAFDisplayUnits unregisterObserver:];
-[CAFDisplayUnits distanceUnit];
-[CAFDisplayUnits hasEnergyEfficiencyUnitRawValue];
-[CAFDisplayUnits registeredForFuelEfficiencyUnit];
-[CAFDisplayUnits distanceUnitRawValue];
-[CAFDisplayUnits energyEfficiencyUnitRawValue];
-[CAFDisplayUnits fuelEfficiencyUnitRawValue];
-[CAFDisplayUnits hasFuelEfficiencyUnitRawValue];
-[CAFDisplayUnits registeredForDistanceUnit];
-[CAFDisplayUnits registeredForEnergyEfficiencyUnit];
-[CAFDisplayUnits registeredForSpeedUnit];
-[CAFDisplayUnits registeredForTemperatureUnit];
-[CAFDisplayUnits speedUnitRawValue];
-[CAFDisplayUnits temperatureUnitRawValue];
-[CAFDisplayUnits speedUnitRawValueCharacteristic];
-[CAFDisplayUnits _characteristicDidUpdate:fromGroupUpdate:];
-[CAFDisplayUnits distanceUnitRawValueCharacteristic];
-[CAFDisplayUnits energyEfficiencyUnit];
-[CAFDisplayUnits energyEfficiencyUnitRawValueCharacteristic];
-[CAFDisplayUnits fuelEfficiencyUnit];
-[CAFDisplayUnits fuelEfficiencyUnitRawValueCharacteristic];
-[CAFDisplayUnits speedUnit];
-[CAFDisplayUnits temperatureUnitRawValueCharacteristic];
```
