# `CMActivity`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CMLogItem`
- 1 instance variables, 7 properties, 13 instance methods, 1 class methods

## Instance variables

```
{CLMotionActivity="type"i"confidence"i"source"i"mountedState"i"mountedConfidence"i"conservativeMountedState"i"conservativeMountedProbability"d"isStanding"B"tilt"f"timestamp"d"isVehicleConnected"B"exitState"i"estExitTime"d"vehicleType"i"fsmTransitionData"{FsmTransitionData="fFsmFromToStates"C"fFsmStateTransEvent"C"fFsmGuards"C"fConsecStatic"S}"vehicleProbabilityShortTermMean" "startTime"d"rawType"i"rawConfidence"i"vehicularFlags"{?="motionHint"b1"gpsHint"b1"basebandHint"b1"wifiHint"b1"btHint"b1}"vehicularConfidence"i"workoutDetectionType"i"workoutDetectionTime"d"workoutEscalationTime"Q"typeYouth"i} fActivity;
```

## Properties

```
@property (Ti,R,N) confidence;
@property (TB,R,N) isMoving;
@property (TB,R,N) isWalking;
@property (TB,R,N) isRunning;
@property (TB,R,N) isDriving;
@property (TB,R,N) maybeExitingVehicle;
@property (TB,R,N) hasExitedVehicle;
```

## Class methods

```
+[CMActivity supportsSecureCoding];
```

## Instance methods

```
-[CMActivity isRunning];
-[CMActivity initWithMotionActivity:];
-[CMActivity hasExitedVehicle];
-[CMActivity activity];
-[CMActivity isMoving];
-[CMActivity isWalking];
-[CMActivity encodeWithCoder:];
-[CMActivity isDriving];
-[CMActivity description];
-[CMActivity initWithCoder:];
-[CMActivity maybeExitingVehicle];
-[CMActivity copyWithZone:];
-[CMActivity confidence];
```
