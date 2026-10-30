# `CAFBatteryLevel`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 20 properties, 31 instance methods, 2 class methods

## Properties

```
@property (T@"CAFMeasurementCharacteristic",R,N) batteryLevelCharacteristic;
@property (T@"CAFBatteryLevelStateCharacteristic",R,N) batteryLevelStateCharacteristic;
@property (T@"CAFMeasurementCharacteristic",R,N) batteryLevelMarkerLowCharacteristic;
@property (T@"CAFMeasurementCharacteristic",R,N) batteryLevelMarkerCriticalLowCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) hiddenCharacteristic;
@property (T@"NSMeasurement",R,N) batteryLevel;
@property (T@"CAFUInt8Range",R,N) batteryLevelRange;
@property (T@"CAFMeasurementRange",R,N) batteryLevelMeasurementRange;
@property (TB,R,N) batteryLevelInvalid;
@property (TC,R,N) batteryLevelState;
@property (T@"NSMeasurement",R,N) batteryLevelMarkerLow;
@property (T@"CAFUInt8Range",R,N) batteryLevelMarkerLowRange;
@property (T@"CAFMeasurementRange",R,N) batteryLevelMarkerLowMeasurementRange;
@property (TB,R,N) hasBatteryLevelMarkerLow;
@property (T@"NSMeasurement",R,N) batteryLevelMarkerCriticalLow;
@property (T@"CAFUInt8Range",R,N) batteryLevelMarkerCriticalLowRange;
@property (T@"CAFMeasurementRange",R,N) batteryLevelMarkerCriticalLowMeasurementRange;
@property (TB,R,N) hasBatteryLevelMarkerCriticalLow;
@property (TB,R,N) hidden;
@property (TB,R,N) hasHidden;
```

## Class methods

```
+[CAFBatteryLevel serviceIdentifier];
+[CAFBatteryLevel observerProtocol];
```

## Instance methods

```
-[CAFBatteryLevel batteryLevel];
-[CAFBatteryLevel removeObserver:];
-[CAFBatteryLevel addObserver:];
-[CAFBatteryLevel registerObserver:];
-[CAFBatteryLevel name];
-[CAFBatteryLevel unregisterObserver:];
-[CAFBatteryLevel hidden];
-[CAFBatteryLevel hasHidden];
-[CAFBatteryLevel batteryLevelMarkerCriticalLow];
-[CAFBatteryLevel batteryLevelMarkerLow];
-[CAFBatteryLevel batteryLevelState];
-[CAFBatteryLevel registeredForBatteryLevel];
-[CAFBatteryLevel registeredForBatteryLevelMarkerCriticalLow];
-[CAFBatteryLevel registeredForBatteryLevelMarkerLow];
-[CAFBatteryLevel registeredForBatteryLevelState];
-[CAFBatteryLevel registeredForHidden];
-[CAFBatteryLevel batteryLevelStateCharacteristic];
-[CAFBatteryLevel _characteristicDidUpdate:fromGroupUpdate:];
-[CAFBatteryLevel batteryLevelCharacteristic];
-[CAFBatteryLevel batteryLevelInvalid];
-[CAFBatteryLevel batteryLevelMarkerCriticalLowCharacteristic];
-[CAFBatteryLevel batteryLevelMarkerCriticalLowMeasurementRange];
-[CAFBatteryLevel batteryLevelMarkerCriticalLowRange];
-[CAFBatteryLevel batteryLevelMarkerLowCharacteristic];
-[CAFBatteryLevel batteryLevelMarkerLowMeasurementRange];
-[CAFBatteryLevel batteryLevelMarkerLowRange];
-[CAFBatteryLevel batteryLevelMeasurementRange];
-[CAFBatteryLevel batteryLevelRange];
-[CAFBatteryLevel hasBatteryLevelMarkerCriticalLow];
-[CAFBatteryLevel hasBatteryLevelMarkerLow];
-[CAFBatteryLevel hiddenCharacteristic];
```
