# `CAFFuelLevel`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 19 properties, 31 instance methods, 2 class methods

## Properties

```
@property (T@"CAFMeasurementCharacteristic",R,N) fuelLevelCharacteristic;
@property (T@"CAFFuelLevelStateCharacteristic",R,N) fuelLevelStateCharacteristic;
@property (T@"CAFMeasurementCharacteristic",R,N) fuelLevelMarkerLowCharacteristic;
@property (T@"CAFFillLevelLabelCharacteristic",R,N) fillLevelLabelCharacteristic;
@property (T@"CAFPortSideIndicatorCharacteristic",R,N) portSideIndicatorCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) hiddenCharacteristic;
@property (T@"NSMeasurement",R,N) fuelLevel;
@property (T@"CAFUInt8Range",R,N) fuelLevelRange;
@property (T@"CAFMeasurementRange",R,N) fuelLevelMeasurementRange;
@property (TB,R,N) fuelLevelInvalid;
@property (TC,R,N) fuelLevelState;
@property (T@"NSMeasurement",R,N) fuelLevelMarkerLow;
@property (T@"CAFUInt8Range",R,N) fuelLevelMarkerLowRange;
@property (T@"CAFMeasurementRange",R,N) fuelLevelMarkerLowMeasurementRange;
@property (TB,R,N) hasFuelLevelMarkerLow;
@property (TC,R,N) fillLevelLabel;
@property (TC,R,N) portSideIndicator;
@property (TB,R,N) hidden;
@property (TB,R,N) hasHidden;
```

## Class methods

```
+[CAFFuelLevel serviceIdentifier];
+[CAFFuelLevel observerProtocol];
```

## Instance methods

```
-[CAFFuelLevel removeObserver:];
-[CAFFuelLevel addObserver:];
-[CAFFuelLevel registerObserver:];
-[CAFFuelLevel name];
-[CAFFuelLevel unregisterObserver:];
-[CAFFuelLevel hidden];
-[CAFFuelLevel hasHidden];
-[CAFFuelLevel registeredForFuelLevelMarkerLow];
-[CAFFuelLevel fillLevelLabel];
-[CAFFuelLevel fuelLevel];
-[CAFFuelLevel fuelLevelMarkerLow];
-[CAFFuelLevel fuelLevelState];
-[CAFFuelLevel portSideIndicator];
-[CAFFuelLevel registeredForFillLevelLabel];
-[CAFFuelLevel registeredForFuelLevel];
-[CAFFuelLevel registeredForFuelLevelState];
-[CAFFuelLevel registeredForHidden];
-[CAFFuelLevel registeredForPortSideIndicator];
-[CAFFuelLevel portSideIndicatorCharacteristic];
-[CAFFuelLevel _characteristicDidUpdate:fromGroupUpdate:];
-[CAFFuelLevel fillLevelLabelCharacteristic];
-[CAFFuelLevel fuelLevelCharacteristic];
-[CAFFuelLevel fuelLevelInvalid];
-[CAFFuelLevel fuelLevelMarkerLowCharacteristic];
-[CAFFuelLevel fuelLevelMarkerLowMeasurementRange];
-[CAFFuelLevel fuelLevelMarkerLowRange];
-[CAFFuelLevel fuelLevelMeasurementRange];
-[CAFFuelLevel fuelLevelRange];
-[CAFFuelLevel fuelLevelStateCharacteristic];
-[CAFFuelLevel hasFuelLevelMarkerLow];
-[CAFFuelLevel hiddenCharacteristic];
```
