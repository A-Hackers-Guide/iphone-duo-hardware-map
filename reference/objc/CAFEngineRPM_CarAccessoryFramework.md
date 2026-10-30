# `CAFEngineRPM`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 17 properties, 27 instance methods, 2 class methods

## Properties

```
@property (T@"CAFMeasurementCharacteristic",R,N) rotationalSpeedCharacteristic;
@property (T@"CAFRotationalSpeedStateCharacteristic",R,N) rotationalSpeedStateCharacteristic;
@property (T@"CAFMeasurementCharacteristic",R,N) rotationalSpeedMarkerRedlineCharacteristic;
@property (T@"CAFMeasurementCharacteristic",R,N) rotationalSpeedMaxCharacteristic;
@property (T@"NSMeasurement",R,N) rotationalSpeed;
@property (T@"CAFUInt32Range",R,N) rotationalSpeedRange;
@property (T@"CAFMeasurementRange",R,N) rotationalSpeedMeasurementRange;
@property (TB,R,N) rotationalSpeedInvalid;
@property (TC,R,N) rotationalSpeedState;
@property (TB,R,N) hasRotationalSpeedState;
@property (T@"NSMeasurement",R,N) rotationalSpeedMarkerRedline;
@property (T@"CAFUInt32Range",R,N) rotationalSpeedMarkerRedlineRange;
@property (T@"CAFMeasurementRange",R,N) rotationalSpeedMarkerRedlineMeasurementRange;
@property (TB,R,N) hasRotationalSpeedMarkerRedline;
@property (T@"NSMeasurement",R,N) rotationalSpeedMax;
@property (T@"CAFUInt32Range",R,N) rotationalSpeedMaxRange;
@property (T@"CAFMeasurementRange",R,N) rotationalSpeedMaxMeasurementRange;
```

## Class methods

```
+[CAFEngineRPM serviceIdentifier];
+[CAFEngineRPM observerProtocol];
```

## Instance methods

```
-[CAFEngineRPM removeObserver:];
-[CAFEngineRPM addObserver:];
-[CAFEngineRPM registerObserver:];
-[CAFEngineRPM name];
-[CAFEngineRPM unregisterObserver:];
-[CAFEngineRPM registeredForRotationalSpeedMax];
-[CAFEngineRPM rotationalSpeed];
-[CAFEngineRPM hasRotationalSpeedState];
-[CAFEngineRPM registeredForRotationalSpeed];
-[CAFEngineRPM registeredForRotationalSpeedMarkerRedline];
-[CAFEngineRPM registeredForRotationalSpeedState];
-[CAFEngineRPM rotationalSpeedMarkerRedline];
-[CAFEngineRPM rotationalSpeedMax];
-[CAFEngineRPM rotationalSpeedState];
-[CAFEngineRPM hasRotationalSpeedMarkerRedline];
-[CAFEngineRPM rotationalSpeedMeasurementRange];
-[CAFEngineRPM _characteristicDidUpdate:fromGroupUpdate:];
-[CAFEngineRPM rotationalSpeedCharacteristic];
-[CAFEngineRPM rotationalSpeedInvalid];
-[CAFEngineRPM rotationalSpeedMarkerRedlineCharacteristic];
-[CAFEngineRPM rotationalSpeedMarkerRedlineMeasurementRange];
-[CAFEngineRPM rotationalSpeedMarkerRedlineRange];
-[CAFEngineRPM rotationalSpeedMaxCharacteristic];
-[CAFEngineRPM rotationalSpeedMaxMeasurementRange];
-[CAFEngineRPM rotationalSpeedMaxRange];
-[CAFEngineRPM rotationalSpeedRange];
-[CAFEngineRPM rotationalSpeedStateCharacteristic];
```
