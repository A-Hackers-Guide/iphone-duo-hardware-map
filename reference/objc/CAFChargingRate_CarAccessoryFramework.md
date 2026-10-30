# `CAFChargingRate`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 11 properties, 19 instance methods, 2 class methods

## Properties

```
@property (T@"CAFMeasurementCharacteristic",R,N) powerCharacteristic;
@property (T@"CAFMeasurementCharacteristic",R,N) chargingSpeedCharacteristic;
@property (T@"NSMeasurement",R,N) power;
@property (T@"CAFInt32Range",R,N) powerRange;
@property (T@"CAFMeasurementRange",R,N) powerMeasurementRange;
@property (TB,R,N) powerInvalid;
@property (T@"NSMeasurement",R,N) chargingSpeed;
@property (T@"CAFInt32Range",R,N) chargingSpeedRange;
@property (T@"CAFMeasurementRange",R,N) chargingSpeedMeasurementRange;
@property (TB,R,N) hasChargingSpeed;
@property (TB,R,N) chargingSpeedInvalid;
```

## Class methods

```
+[CAFChargingRate serviceIdentifier];
+[CAFChargingRate observerProtocol];
```

## Instance methods

```
-[CAFChargingRate power];
-[CAFChargingRate removeObserver:];
-[CAFChargingRate addObserver:];
-[CAFChargingRate registerObserver:];
-[CAFChargingRate name];
-[CAFChargingRate unregisterObserver:];
-[CAFChargingRate chargingSpeed];
-[CAFChargingRate registeredForChargingSpeed];
-[CAFChargingRate registeredForPower];
-[CAFChargingRate _characteristicDidUpdate:fromGroupUpdate:];
-[CAFChargingRate chargingSpeedCharacteristic];
-[CAFChargingRate chargingSpeedInvalid];
-[CAFChargingRate chargingSpeedMeasurementRange];
-[CAFChargingRate chargingSpeedRange];
-[CAFChargingRate hasChargingSpeed];
-[CAFChargingRate powerCharacteristic];
-[CAFChargingRate powerInvalid];
-[CAFChargingRate powerMeasurementRange];
-[CAFChargingRate powerRange];
```
