# `CAFDimensionManager`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAFCarObserver`, `CAFCarObserverPrivate`, `CAFDisplayUnitsObserver`
- 8 instance variables, 20 properties, 40 instance methods, 0 class methods

## Instance variables

```
S _fuelEfficiencyUnit;
S _energyEfficiencyUnit;
@ _observableCache;
@"CAFCar" _car;
@"NSLocale" _locale;
@"CARObserverHashTable" _observers;
@"NSObject<OS_dispatch_queue>" _workQueue;
@"CAFDisplayUnits" _displayUnitsService;
```

## Properties

```
@property (T@"CARObserverHashTable",&,N,V_observers) observers;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_workQueue) workQueue;
@property (T@"NSLocale",&,V_locale) locale;
@property (TS,N,V_fuelEfficiencyUnit) fuelEfficiencyUnit;
@property (TS,N,V_energyEfficiencyUnit) energyEfficiencyUnit;
@property (T@"CAFDisplayUnits",W,N,V_displayUnitsService) displayUnitsService;
@property (T@"CAFCar",R,W,N,V_car) car;
@property (T@"NSUnitTemperature",R,N) unitTemperature;
@property (T@"NSUnitPressure",R,N) tirePressureUnit;
@property (T@"NSUnitSpeed",R,N) vehicleSpeedUnit;
@property (T@"NSUnitLength",R,N) vehicleRangeUnit;
@property (T@"NSUnitFuelEfficiency",R,N) vehicleFuelEfficiencyUnit;
@property (T@"NSUnitVolume",R,N) vehicleFuelVolumeUnit;
@property (T@"CAFUnitEnergyEfficiency",R,N) vehicleEnergyEfficiencyUnit;
@property (T@"NSUnitPower",R,N) vehicleChargePowerUnit;
@property (TQ,R,N) measurementSystem;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAFDimensionManager removeObserver:];
-[CAFDimensionManager workQueue];
-[CAFDimensionManager setLocale:];
-[CAFDimensionManager addObserver:];
-[CAFDimensionManager invalidate];
-[CAFDimensionManager locale];
-[CAFDimensionManager measurementSystem];
-[CAFDimensionManager setObservers:];
-[CAFDimensionManager observers];
-[CAFDimensionManager registerObserver:];
-[CAFDimensionManager unregisterObserver:];
-[CAFDimensionManager car];
-[CAFDimensionManager carDidUpdate:receivedAllValues:];
-[CAFDimensionManager carDidUpdate:accessory:service:characteristic:];
-[CAFDimensionManager carDidUpdateAccessories:];
-[CAFDimensionManager unitTemperature];
-[CAFDimensionManager observableCache];
-[CAFDimensionManager displayUnitsService:didUpdateDistanceUnitRawValue:];
-[CAFDimensionManager displayUnitsService:didUpdateEnergyEfficiencyUnitRawValue:];
-[CAFDimensionManager displayUnitsService:didUpdateFuelEfficiencyUnitRawValue:];
-[CAFDimensionManager displayUnitsService:didUpdateSpeedUnitRawValue:];
-[CAFDimensionManager displayUnitsService:didUpdateTemperatureUnitRawValue:];
-[CAFDimensionManager setObservableCache:];
-[CAFDimensionManager tirePressureUnit];
-[CAFDimensionManager vehicleChargePowerUnit];
-[CAFDimensionManager vehicleEnergyEfficiencyUnit];
-[CAFDimensionManager vehicleFuelEfficiencyUnit];
-[CAFDimensionManager vehicleFuelVolumeUnit];
-[CAFDimensionManager vehicleRangeUnit];
-[CAFDimensionManager vehicleSpeedUnit];
-[CAFDimensionManager _registerIfNeededforReason:];
-[CAFDimensionManager carIsConfigured:];
-[CAFDimensionManager currentLocaleChanged];
-[CAFDimensionManager displayUnitsService];
-[CAFDimensionManager energyEfficiencyUnit];
-[CAFDimensionManager fuelEfficiencyUnit];
-[CAFDimensionManager initWithCar:];
-[CAFDimensionManager setDisplayUnitsService:];
-[CAFDimensionManager setEnergyEfficiencyUnit:];
-[CAFDimensionManager setFuelEfficiencyUnit:];
```
