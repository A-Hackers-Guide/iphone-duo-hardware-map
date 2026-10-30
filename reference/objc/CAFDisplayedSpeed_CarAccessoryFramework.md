# `CAFDisplayedSpeed`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFSpeedDisplay`
- 0 instance variables, 11 properties, 20 instance methods, 2 class methods

## Properties

```
@property (T@"CAFMeasurementCharacteristic",R,N) speedMaxKMHCharacteristic;
@property (T@"CAFMeasurementCharacteristic",R,N) speedMaxMPHCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) showSecondarySpeedCharacteristic;
@property (T@"NSMeasurement",R,N) speedMaxKMH;
@property (T@"CAFUInt32Range",R,N) speedMaxKMHRange;
@property (T@"CAFMeasurementRange",R,N) speedMaxKMHMeasurementRange;
@property (T@"NSMeasurement",R,N) speedMaxMPH;
@property (T@"CAFUInt32Range",R,N) speedMaxMPHRange;
@property (T@"CAFMeasurementRange",R,N) speedMaxMPHMeasurementRange;
@property (TB,R,N) showSecondarySpeed;
@property (TB,R,N) hasShowSecondarySpeed;
```

## Class methods

```
+[CAFDisplayedSpeed serviceIdentifier];
+[CAFDisplayedSpeed observerProtocol];
```

## Instance methods

```
-[CAFDisplayedSpeed removeObserver:];
-[CAFDisplayedSpeed addObserver:];
-[CAFDisplayedSpeed registerObserver:];
-[CAFDisplayedSpeed name];
-[CAFDisplayedSpeed unregisterObserver:];
-[CAFDisplayedSpeed registeredForShowSecondarySpeed];
-[CAFDisplayedSpeed hasShowSecondarySpeed];
-[CAFDisplayedSpeed registeredForSpeedMaxKMH];
-[CAFDisplayedSpeed registeredForSpeedMaxMPH];
-[CAFDisplayedSpeed showSecondarySpeed];
-[CAFDisplayedSpeed speedMaxKMH];
-[CAFDisplayedSpeed speedMaxMPH];
-[CAFDisplayedSpeed _characteristicDidUpdate:fromGroupUpdate:];
-[CAFDisplayedSpeed showSecondarySpeedCharacteristic];
-[CAFDisplayedSpeed speedMaxKMHCharacteristic];
-[CAFDisplayedSpeed speedMaxKMHMeasurementRange];
-[CAFDisplayedSpeed speedMaxKMHRange];
-[CAFDisplayedSpeed speedMaxMPHCharacteristic];
-[CAFDisplayedSpeed speedMaxMPHMeasurementRange];
-[CAFDisplayedSpeed speedMaxMPHRange];
```
