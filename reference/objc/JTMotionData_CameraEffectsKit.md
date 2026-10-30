# `JTMotionData`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 22 instance methods, 1 class methods

## Instance variables

```
B _started;
@"CMMotionManager" _motionManager;
@"NSOperationQueue" _motionQueue;
@"CMAttitude" _refAttitude;
d _yawRadians;
d _rollRadians;
d _pitchRadians;
{?="x"d"y"d"z"d"w"d} _currentAttitude;
```

## Properties

```
@property (T@"CMMotionManager",&,N,V_motionManager) motionManager;
@property (T@"NSOperationQueue",&,N,V_motionQueue) motionQueue;
@property (T@"CMAttitude",&,N,V_refAttitude) refAttitude;
@property (T{?=dddd},N,V_currentAttitude) currentAttitude;
@property (Td,N,V_yawRadians) yawRadians;
@property (Td,N,V_rollRadians) rollRadians;
@property (Td,N,V_pitchRadians) pitchRadians;
@property (TB,V_started) started;
```

## Class methods

```
+[JTMotionData sharedInstance];
```

## Instance methods

```
-[JTMotionData currentOrientation];
-[JTMotionData setStarted:];
-[JTMotionData init];
-[JTMotionData started];
-[JTMotionData motionManager];
-[JTMotionData setMotionManager:];
-[JTMotionData setRollRadians:];
-[JTMotionData pitchRadians];
-[JTMotionData setPitchRadians:];
-[JTMotionData setYawRadians:];
-[JTMotionData yawRadians];
-[JTMotionData rollRadians];
-[JTMotionData setMotionQueue:];
-[JTMotionData setRefAttitude:];
-[JTMotionData currentAttitude];
-[JTMotionData getOrientation:];
-[JTMotionData motionQueue];
-[JTMotionData refAttitude];
-[JTMotionData setCurrentAttitude:];
-[JTMotionData startMotion];
-[JTMotionData stopMotion];
-[JTMotionData syntheticOrientation];
```
