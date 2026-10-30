# `CAFSpeedDisplay`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 15 properties, 24 instance methods, 0 class methods

## Properties

```
@property (T@"CAFMeasurementCharacteristic",R,N) speedCharacteristic;
@property (T@"CAFMeasurementCharacteristic",R,N) speedKMHCharacteristic;
@property (T@"CAFMeasurementCharacteristic",R,N) speedMPHCharacteristic;
@property (T@"NSMeasurement",R,N) speed;
@property (T@"CAFUInt32Range",R,N) speedRange;
@property (T@"CAFMeasurementRange",R,N) speedMeasurementRange;
@property (TB,R,N) speedInvalid;
@property (T@"NSMeasurement",R,N) speedKMH;
@property (T@"CAFUInt32Range",R,N) speedKMHRange;
@property (T@"CAFMeasurementRange",R,N) speedKMHMeasurementRange;
@property (TB,R,N) speedKMHInvalid;
@property (T@"NSMeasurement",R,N) speedMPH;
@property (T@"CAFUInt32Range",R,N) speedMPHRange;
@property (T@"CAFMeasurementRange",R,N) speedMPHMeasurementRange;
@property (TB,R,N) speedMPHInvalid;
```

## Instance methods

```
-[CAFSpeedDisplay speed];
-[CAFSpeedDisplay removeObserver:];
-[CAFSpeedDisplay addObserver:];
-[CAFSpeedDisplay registerObserver:];
-[CAFSpeedDisplay name];
-[CAFSpeedDisplay unregisterObserver:];
-[CAFSpeedDisplay registeredForSpeedKMH];
-[CAFSpeedDisplay registeredForSpeedMPH];
-[CAFSpeedDisplay speedKMH];
-[CAFSpeedDisplay speedMPH];
-[CAFSpeedDisplay speedKMHInvalid];
-[CAFSpeedDisplay speedMPHInvalid];
-[CAFSpeedDisplay _characteristicDidUpdate:fromGroupUpdate:];
-[CAFSpeedDisplay registeredForSpeed];
-[CAFSpeedDisplay speedCharacteristic];
-[CAFSpeedDisplay speedInvalid];
-[CAFSpeedDisplay speedKMHCharacteristic];
-[CAFSpeedDisplay speedKMHMeasurementRange];
-[CAFSpeedDisplay speedKMHRange];
-[CAFSpeedDisplay speedMPHCharacteristic];
-[CAFSpeedDisplay speedMPHMeasurementRange];
-[CAFSpeedDisplay speedMPHRange];
-[CAFSpeedDisplay speedMeasurementRange];
-[CAFSpeedDisplay speedRange];
```
