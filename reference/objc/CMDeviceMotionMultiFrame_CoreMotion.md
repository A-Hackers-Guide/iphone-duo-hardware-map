# `CMDeviceMotionMultiFrame`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CMLogItem`
- 4 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
d _referenceFrameDeltaYawFromArbitraryToTrueNorth;
{?="headingAccuracy"f"biasEstimateVariance"{?="x"f"y"f"z"f}"angle"f"angleVelocity"f} _deviceMotionInternal;
{?="w"d"x"d"y"d"z"d} _bodyFrameRotationFromSensorToDefault;
{?="quaternion"{?="w"d"x"d"y"d"z"d}"userAcceleration"{?="x"f"y"f"z"f}"rotationRate"{?="x"f"y"f"z"f}"magneticField"{?="x"f"y"f"z"f}"magneticFieldCalibrationLevel"i"doingYawCorrection"B"doingBiasEstimation"B"isInitialized"B"heading"f"fusedWithVision"B"usingVisionCorrections"B"sensorLocation"i} _deviceMotion;
```

## Properties

```
@property (T{?={?=dddd}{?=fff}{?=fff}{?=fff}iBBBfBBi},N,V_deviceMotion) deviceMotion;
@property (T{?=f{?=fff}ff},N,V_deviceMotionInternal) deviceMotionInternal;
@property (T{?=dddd},N,V_bodyFrameRotationFromSensorToDefault) bodyFrameRotationFromSensorToDefault;
@property (Td,N,V_referenceFrameDeltaYawFromArbitraryToTrueNorth) referenceFrameDeltaYawFromArbitraryToTrueNorth;
```

## Instance methods

```
-[CMDeviceMotionMultiFrame deviceMotion];
-[CMDeviceMotionMultiFrame bodyFrameRotationFromSensorToDefault];
-[CMDeviceMotionMultiFrame deviceMotionInternal];
-[CMDeviceMotionMultiFrame deviceMotionWithReferenceFrame:bodyFrame:];
-[CMDeviceMotionMultiFrame initWithDeviceMotion:internal:timestamp:];
-[CMDeviceMotionMultiFrame referenceFrameDeltaYawFromArbitraryToTrueNorth];
-[CMDeviceMotionMultiFrame setBodyFrameRotationFromSensorToDefault:];
-[CMDeviceMotionMultiFrame setDeviceMotion:];
-[CMDeviceMotionMultiFrame setDeviceMotionInternal:];
-[CMDeviceMotionMultiFrame setReferenceFrameDeltaYawFromArbitraryToTrueNorth:];
```
