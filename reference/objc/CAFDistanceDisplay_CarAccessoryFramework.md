# `CAFDistanceDisplay`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 10 properties, 18 instance methods, 0 class methods

## Properties

```
@property (T@"CAFMeasurementCharacteristic",R,N) distanceKMCharacteristic;
@property (T@"CAFMeasurementCharacteristic",R,N) distanceMilesCharacteristic;
@property (T@"NSMeasurement",R,N) distanceKM;
@property (T@"CAFUInt64Range",R,N) distanceKMRange;
@property (T@"CAFMeasurementRange",R,N) distanceKMMeasurementRange;
@property (TB,R,N) distanceKMInvalid;
@property (T@"NSMeasurement",R,N) distanceMiles;
@property (T@"CAFUInt64Range",R,N) distanceMilesRange;
@property (T@"CAFMeasurementRange",R,N) distanceMilesMeasurementRange;
@property (TB,R,N) distanceMilesInvalid;
```

## Instance methods

```
-[CAFDistanceDisplay removeObserver:];
-[CAFDistanceDisplay addObserver:];
-[CAFDistanceDisplay registerObserver:];
-[CAFDistanceDisplay name];
-[CAFDistanceDisplay unregisterObserver:];
-[CAFDistanceDisplay distanceKM];
-[CAFDistanceDisplay distanceMiles];
-[CAFDistanceDisplay distanceKMRange];
-[CAFDistanceDisplay _characteristicDidUpdate:fromGroupUpdate:];
-[CAFDistanceDisplay distanceKMCharacteristic];
-[CAFDistanceDisplay distanceKMInvalid];
-[CAFDistanceDisplay distanceKMMeasurementRange];
-[CAFDistanceDisplay distanceMilesCharacteristic];
-[CAFDistanceDisplay distanceMilesInvalid];
-[CAFDistanceDisplay distanceMilesMeasurementRange];
-[CAFDistanceDisplay distanceMilesRange];
-[CAFDistanceDisplay registeredForDistanceKM];
-[CAFDistanceDisplay registeredForDistanceMiles];
```
