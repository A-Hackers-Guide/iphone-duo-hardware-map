# `CAFTargetSpeed`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 13 properties, 23 instance methods, 2 class methods

## Properties

```
@property (T@"CAFTargetSpeedStateCharacteristic",R,N) targetSpeedStateCharacteristic;
@property (T@"CAFMeasurementCharacteristic",R,N) speedKMHCharacteristic;
@property (T@"CAFMeasurementCharacteristic",R,N) speedMPHCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) speedLimitedCharacteristic;
@property (TC,R,N) targetSpeedState;
@property (T@"NSMeasurement",R,N) speedKMH;
@property (T@"CAFUInt32Range",R,N) speedKMHRange;
@property (T@"CAFMeasurementRange",R,N) speedKMHMeasurementRange;
@property (T@"NSMeasurement",R,N) speedMPH;
@property (T@"CAFUInt32Range",R,N) speedMPHRange;
@property (T@"CAFMeasurementRange",R,N) speedMPHMeasurementRange;
@property (TB,R,N) speedLimited;
@property (TB,R,N) hasSpeedLimited;
```

## Class methods

```
+[CAFTargetSpeed serviceIdentifier];
+[CAFTargetSpeed observerProtocol];
```

## Instance methods

```
-[CAFTargetSpeed removeObserver:];
-[CAFTargetSpeed addObserver:];
-[CAFTargetSpeed registerObserver:];
-[CAFTargetSpeed name];
-[CAFTargetSpeed unregisterObserver:];
-[CAFTargetSpeed hasSpeedLimited];
-[CAFTargetSpeed registeredForSpeedKMH];
-[CAFTargetSpeed registeredForSpeedLimited];
-[CAFTargetSpeed registeredForSpeedMPH];
-[CAFTargetSpeed registeredForTargetSpeedState];
-[CAFTargetSpeed speedKMH];
-[CAFTargetSpeed speedLimited];
-[CAFTargetSpeed speedMPH];
-[CAFTargetSpeed targetSpeedState];
-[CAFTargetSpeed _characteristicDidUpdate:fromGroupUpdate:];
-[CAFTargetSpeed speedKMHCharacteristic];
-[CAFTargetSpeed speedKMHMeasurementRange];
-[CAFTargetSpeed speedKMHRange];
-[CAFTargetSpeed speedLimitedCharacteristic];
-[CAFTargetSpeed speedMPHCharacteristic];
-[CAFTargetSpeed speedMPHMeasurementRange];
-[CAFTargetSpeed speedMPHRange];
-[CAFTargetSpeed targetSpeedStateCharacteristic];
```
