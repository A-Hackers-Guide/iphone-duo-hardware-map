# `CMDeviceMotionInternal`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 15 instance variables, 0 properties, 5 instance methods, 0 class methods

## Instance variables

```
{?="x"d"y"d"z"d} fGravity;
{?="x"d"y"d"z"d} fUserAcceleration;
{?="x"d"y"d"z"d} fRotationRate;
@"CMAttitude" fAttitude;
{?="x"d"y"d"z"d} fMagneticField;
i fMagneticFieldCalibrationLevel;
B fDoingYawCorrection;
B fDoingBiasEstimation;
B fIsInitialized;
f fHeading;
f fHeadingAccuracy;
B fFusedWithVision;
B fUsingVisionCorrections;
q fSensorLocation;
{?="x"f"y"f"z"f} fMagnetometerBiasEstimateVariance;
```

## Instance methods

```
-[CMDeviceMotionInternal dealloc];
-[CMDeviceMotionInternal copyWithZone:];
-[CMDeviceMotionInternal isEqual:];
-[CMDeviceMotionInternal initWithDeviceMotion:internal:];
-[CMDeviceMotionInternal setDeviceMotion:internal:];
```
