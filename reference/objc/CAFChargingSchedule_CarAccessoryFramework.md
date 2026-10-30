# `CAFChargingSchedule`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 5 properties, 12 instance methods, 2 class methods

## Properties

```
@property (T@"CAFMeasurementCharacteristic",R,N) timeToStartCharacteristic;
@property (T@"NSMeasurement",R,N) timeToStart;
@property (T@"CAFUInt64Range",R,N) timeToStartRange;
@property (T@"CAFMeasurementRange",R,N) timeToStartMeasurementRange;
@property (TB,R,N) timeToStartInvalid;
```

## Class methods

```
+[CAFChargingSchedule serviceIdentifier];
+[CAFChargingSchedule observerProtocol];
```

## Instance methods

```
-[CAFChargingSchedule removeObserver:];
-[CAFChargingSchedule addObserver:];
-[CAFChargingSchedule registerObserver:];
-[CAFChargingSchedule name];
-[CAFChargingSchedule unregisterObserver:];
-[CAFChargingSchedule registeredForTimeToStart];
-[CAFChargingSchedule timeToStart];
-[CAFChargingSchedule _characteristicDidUpdate:fromGroupUpdate:];
-[CAFChargingSchedule timeToStartCharacteristic];
-[CAFChargingSchedule timeToStartInvalid];
-[CAFChargingSchedule timeToStartMeasurementRange];
-[CAFChargingSchedule timeToStartRange];
```
