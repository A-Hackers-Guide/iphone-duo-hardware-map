# `CAFChargingTime`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 11 properties, 19 instance methods, 2 class methods

## Properties

```
@property (T@"CAFMeasurementCharacteristic",R,N) elapsedTimeCharacteristic;
@property (T@"CAFMeasurementCharacteristic",R,N) remainingTimeCharacteristic;
@property (T@"NSMeasurement",R,N) elapsedTime;
@property (T@"CAFUInt64Range",R,N) elapsedTimeRange;
@property (T@"CAFMeasurementRange",R,N) elapsedTimeMeasurementRange;
@property (TB,R,N) hasElapsedTime;
@property (TB,R,N) elapsedTimeInvalid;
@property (T@"NSMeasurement",R,N) remainingTime;
@property (T@"CAFUInt64Range",R,N) remainingTimeRange;
@property (T@"CAFMeasurementRange",R,N) remainingTimeMeasurementRange;
@property (TB,R,N) remainingTimeInvalid;
```

## Class methods

```
+[CAFChargingTime serviceIdentifier];
+[CAFChargingTime observerProtocol];
```

## Instance methods

```
-[CAFChargingTime elapsedTime];
-[CAFChargingTime hasElapsedTime];
-[CAFChargingTime remainingTime];
-[CAFChargingTime removeObserver:];
-[CAFChargingTime addObserver:];
-[CAFChargingTime registerObserver:];
-[CAFChargingTime name];
-[CAFChargingTime unregisterObserver:];
-[CAFChargingTime registeredForElapsedTime];
-[CAFChargingTime registeredForRemainingTime];
-[CAFChargingTime _characteristicDidUpdate:fromGroupUpdate:];
-[CAFChargingTime elapsedTimeCharacteristic];
-[CAFChargingTime elapsedTimeInvalid];
-[CAFChargingTime elapsedTimeMeasurementRange];
-[CAFChargingTime elapsedTimeRange];
-[CAFChargingTime remainingTimeCharacteristic];
-[CAFChargingTime remainingTimeInvalid];
-[CAFChargingTime remainingTimeMeasurementRange];
-[CAFChargingTime remainingTimeRange];
```
