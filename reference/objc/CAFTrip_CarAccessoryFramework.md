# `CAFTrip`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 58 properties, 78 instance methods, 2 class methods

## Properties

```
@property (T@"CAFStringCharacteristic",R,N) userVisibleLabelCharacteristic;
@property (T@"CAFUInt8Characteristic",R,N) sortOrderCharacteristic;
@property (T@"CAFMeasurementCharacteristic",R,N) averageSpeedCharacteristic;
@property (T@"CAFMeasurementCharacteristic",R,N) distanceCharacteristic;
@property (T@"CAFMeasurementCharacteristic",R,N) durationCharacteristic;
@property (T@"CAFMeasurementCharacteristic",R,N) energyCharacteristic;
@property (T@"CAFMeasurementCharacteristic",R,N) energyEfficiencyCharacteristic;
@property (T@"CAFMeasurementCharacteristic",R,N) fuelEfficiencyCharacteristic;
@property (T@"CAFMeasurementCharacteristic",R,N) fuelConsumptionCharacteristic;
@property (T@"CAFMeasurementCharacteristic",R,N) combinedEfficiencyCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) showOdometerCharacteristic;
@property (T@"CAFResetControl",R,N) resetControl;
@property (T@"NSString",R,N) userVisibleLabel;
@property (TB,R,N) hasUserVisibleLabel;
@property (TC,R,N) sortOrder;
@property (T@"NSMeasurement",R,N) averageSpeed;
@property (T@"CAFUInt32Range",R,N) averageSpeedRange;
@property (T@"CAFMeasurementRange",R,N) averageSpeedMeasurementRange;
@property (TB,R,N) hasAverageSpeed;
@property (TB,R,N) averageSpeedInvalid;
@property (T@"NSMeasurement",R,N) distance;
@property (T@"CAFUInt64Range",R,N) distanceRange;
@property (T@"CAFMeasurementRange",R,N) distanceMeasurementRange;
@property (TB,R,N) hasDistance;
@property (TB,R,N) distanceInvalid;
@property (T@"NSMeasurement",R,N) duration;
@property (T@"CAFUInt64Range",R,N) durationRange;
@property (T@"CAFMeasurementRange",R,N) durationMeasurementRange;
@property (TB,R,N) hasDuration;
@property (TB,R,N) durationInvalid;
@property (T@"NSMeasurement",R,N) energy;
@property (T@"CAFInt32Range",R,N) energyRange;
@property (T@"CAFMeasurementRange",R,N) energyMeasurementRange;
@property (TB,R,N) hasEnergy;
@property (TB,R,N) energyInvalid;
@property (T@"NSMeasurement",R,N) energyEfficiency;
@property (T@"CAFFloatRange",R,N) energyEfficiencyRange;
@property (T@"CAFMeasurementRange",R,N) energyEfficiencyMeasurementRange;
@property (TB,R,N) hasEnergyEfficiency;
@property (TB,R,N) energyEfficiencyInvalid;
@property (T@"NSMeasurement",R,N) fuelEfficiency;
@property (T@"CAFFloatRange",R,N) fuelEfficiencyRange;
@property (T@"CAFMeasurementRange",R,N) fuelEfficiencyMeasurementRange;
@property (TB,R,N) hasFuelEfficiency;
@property (TB,R,N) fuelEfficiencyInvalid;
@property (T@"NSMeasurement",R,N) fuelConsumption;
@property (T@"CAFUInt32Range",R,N) fuelConsumptionRange;
@property (T@"CAFMeasurementRange",R,N) fuelConsumptionMeasurementRange;
@property (TB,R,N) hasFuelConsumption;
@property (TB,R,N) fuelConsumptionInvalid;
@property (T@"NSMeasurement",R,N) combinedEfficiency;
@property (T@"CAFFloatRange",R,N) combinedEfficiencyRange;
@property (T@"CAFMeasurementRange",R,N) combinedEfficiencyMeasurementRange;
@property (TB,R,N) hasCombinedEfficiency;
@property (TB,R,N) combinedEfficiencyInvalid;
@property (TB,N) showOdometer;
@property (TB,R,N) hasShowOdometer;
@property (TB,R,N) hasReset;
```

## Class methods

```
+[CAFTrip serviceIdentifier];
+[CAFTrip observerProtocol];
```

## Instance methods

```
-[CAFTrip sortOrder];
-[CAFTrip distance];
-[CAFTrip removeObserver:];
-[CAFTrip hasDuration];
-[CAFTrip energy];
-[CAFTrip duration];
-[CAFTrip addObserver:];
-[CAFTrip hasDistance];
-[CAFTrip registerObserver:];
-[CAFTrip name];
-[CAFTrip unregisterObserver:];
-[CAFTrip averageSpeed];
-[CAFTrip resetWithCompletion:];
-[CAFTrip durationRange];
-[CAFTrip distanceRange];
-[CAFTrip fuelConsumption];
-[CAFTrip hasShowOdometer];
-[CAFTrip registeredForCombinedEfficiency];
-[CAFTrip combinedEfficiency];
-[CAFTrip energyEfficiency];
-[CAFTrip fuelEfficiency];
-[CAFTrip registeredForAverageSpeed];
-[CAFTrip registeredForDistance];
-[CAFTrip registeredForDuration];
-[CAFTrip registeredForEnergy];
-[CAFTrip registeredForEnergyEfficiency];
-[CAFTrip registeredForFuelConsumption];
-[CAFTrip registeredForFuelEfficiency];
-[CAFTrip registeredForShowOdometer];
-[CAFTrip registeredForSortOrder];
-[CAFTrip registeredForUserVisibleLabel];
-[CAFTrip setShowOdometer:];
-[CAFTrip showOdometer];
-[CAFTrip userVisibleLabel];
-[CAFTrip durationInvalid];
-[CAFTrip distanceInvalid];
-[CAFTrip averageSpeedInvalid];
-[CAFTrip combinedEfficiencyInvalid];
-[CAFTrip energyEfficiencyInvalid];
-[CAFTrip energyInvalid];
-[CAFTrip fuelEfficiencyInvalid];
-[CAFTrip hasAverageSpeed];
-[CAFTrip fuelConsumptionMeasurementRange];
-[CAFTrip _characteristicDidUpdate:fromGroupUpdate:];
-[CAFTrip averageSpeedCharacteristic];
-[CAFTrip averageSpeedMeasurementRange];
-[CAFTrip averageSpeedRange];
-[CAFTrip combinedEfficiencyCharacteristic];
-[CAFTrip combinedEfficiencyMeasurementRange];
-[CAFTrip combinedEfficiencyRange];
-[CAFTrip distanceCharacteristic];
-[CAFTrip distanceMeasurementRange];
-[CAFTrip durationCharacteristic];
-[CAFTrip durationMeasurementRange];
-[CAFTrip energyCharacteristic];
-[CAFTrip energyEfficiencyCharacteristic];
-[CAFTrip energyEfficiencyMeasurementRange];
-[CAFTrip energyEfficiencyRange];
-[CAFTrip energyMeasurementRange];
-[CAFTrip energyRange];
-[CAFTrip fuelConsumptionCharacteristic];
-[CAFTrip fuelConsumptionInvalid];
-[CAFTrip fuelConsumptionRange];
-[CAFTrip fuelEfficiencyCharacteristic];
-[CAFTrip fuelEfficiencyMeasurementRange];
-[CAFTrip fuelEfficiencyRange];
-[CAFTrip hasCombinedEfficiency];
-[CAFTrip hasEnergy];
-[CAFTrip hasEnergyEfficiency];
-[CAFTrip hasFuelConsumption];
-[CAFTrip hasFuelEfficiency];
-[CAFTrip hasReset];
-[CAFTrip hasUserVisibleLabel];
-[CAFTrip registeredForReset];
-[CAFTrip resetControl];
-[CAFTrip showOdometerCharacteristic];
-[CAFTrip sortOrderCharacteristic];
-[CAFTrip userVisibleLabelCharacteristic];
```
