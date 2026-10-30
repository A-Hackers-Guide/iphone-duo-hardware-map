# `CMAPencilFusionResult`

- Image: [`/System/Library/PrivateFrameworks/CoreMotionAlgorithms.framework/CoreMotionAlgorithms`](../userland/System__Library__PrivateFrameworks__CoreMotionAlgorithms.framework__CoreMotionAlgorithms.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 7 instance variables, 7 properties, 16 instance methods, 0 class methods

## Instance variables

```
B _estimated;
f _altitudeAngle;
f _azimuthAngle;
f _rollAngle;
@"NSNumber" _estimationUpdateIndex;
d _timestamp;
_position;
```

## Properties

```
@property (Tf,N,V_altitudeAngle) altitudeAngle;
@property (Tf,N,V_azimuthAngle) azimuthAngle;
@property (Tf,N,V_rollAngle) rollAngle;
@property (T,N,V_position) position;
@property (T@"NSNumber",N,V_estimationUpdateIndex) estimationUpdateIndex;
@property (TB,N,V_estimated) estimated;
@property (Td,N,V_timestamp) timestamp;
```

## Instance methods

```
-[CMAPencilFusionResult position];
-[CMAPencilFusionResult setTimestamp:];
-[CMAPencilFusionResult setRollAngle:];
-[CMAPencilFusionResult timestamp];
-[CMAPencilFusionResult rollAngle];
-[CMAPencilFusionResult description];
-[CMAPencilFusionResult setPosition:];
-[CMAPencilFusionResult copyWithZone:];
-[CMAPencilFusionResult altitudeAngle];
-[CMAPencilFusionResult azimuthAngle];
-[CMAPencilFusionResult estimationUpdateIndex];
-[CMAPencilFusionResult setEstimated:];
-[CMAPencilFusionResult estimated];
-[CMAPencilFusionResult setAltitudeAngle:];
-[CMAPencilFusionResult setAzimuthAngle:];
-[CMAPencilFusionResult setEstimationUpdateIndex:];
```
