# `CMDeviceMotion`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CMLogItem`
- 1 instance variables, 16 properties, 25 instance methods, 1 class methods

## Instance variables

```
@ _internal;
```

## Properties

```
@property (TB,R,N) usingVisionCorrections;
@property (TB,R,N) doingYawCorrection;
@property (TB,R,N) doingBiasEstimation;
@property (TB,R,N,GisInitialized) initialized;
@property (Ti,R,N) magneticFieldCalibrationLevel;
@property (TB,R,N) fusedWithVision;
@property (T{?=fff},R,N) magnetometerBiasEstimateVariance;
@property (T@"CMAttitude",R,N) forwardPredictedAttitudeForAudio;
@property (T@"CMAttitude",R,N) attitude;
@property (T{?=ddd},R,N) rotationRate;
@property (T{?=ddd},R,N) gravity;
@property (T{?=ddd},R,N) userAcceleration;
@property (T{?={?=ddd}i},R,N) magneticField;
@property (Td,R,N) heading;
@property (Td,R,N) headingAccuracy;
@property (Tq,R,N) sensorLocation;
```

## Class methods

```
+[CMDeviceMotion supportsSecureCoding];
```

## Instance methods

```
-[CMDeviceMotion dealloc];
-[CMDeviceMotion heading];
-[CMDeviceMotion gravity];
-[CMDeviceMotion encodeWithCoder:];
-[CMDeviceMotion description];
-[CMDeviceMotion initWithCoder:];
-[CMDeviceMotion copyWithZone:];
-[CMDeviceMotion isEqual:];
-[CMDeviceMotion isInitialized];
-[CMDeviceMotion attitude];
-[CMDeviceMotion magneticField];
-[CMDeviceMotion headingAccuracy];
-[CMDeviceMotion rotationRate];
-[CMDeviceMotion userAcceleration];
-[CMDeviceMotion fusedWithVision];
-[CMDeviceMotion copyInternalStateFrom:];
-[CMDeviceMotion doingBiasEstimation];
-[CMDeviceMotion doingYawCorrection];
-[CMDeviceMotion forwardPredictedAttitudeForAudio];
-[CMDeviceMotion hasInternalState];
-[CMDeviceMotion initWithDeviceMotion:internal:timestamp:];
-[CMDeviceMotion magneticFieldCalibrationLevel];
-[CMDeviceMotion magnetometerBiasEstimateVariance];
-[CMDeviceMotion sensorLocation];
-[CMDeviceMotion usingVisionCorrections];
```
