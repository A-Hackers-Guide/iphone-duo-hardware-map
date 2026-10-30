# `CMMotionActivity`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CMLogItem`
- 3 instance variables, 19 properties, 31 instance methods, 1 class methods

## Instance variables

```
{CLMotionActivity="type"i"confidence"i"source"i"mountedState"i"mountedConfidence"i"conservativeMountedState"i"conservativeMountedProbability"d"isStanding"B"tilt"f"timestamp"d"isVehicleConnected"B"exitState"i"estExitTime"d"vehicleType"i"fsmTransitionData"{FsmTransitionData="fFsmFromToStates"C"fFsmStateTransEvent"C"fFsmGuards"C"fConsecStatic"S}"vehicleProbabilityShortTermMean" "startTime"d"rawType"i"rawConfidence"i"vehicularFlags"{?="motionHint"b1"gpsHint"b1"basebandHint"b1"wifiHint"b1"btHint"b1}"vehicularConfidence"i"workoutDetectionType"i"workoutDetectionTime"d"workoutEscalationTime"Q"typeYouth"i} fState;
d fEndTime;
B _isRunWalk;
```

## Properties

```
@property (TB,V_isRunWalk) isRunWalk;
@property (T@"NSDate",R,N) endDate;
@property (TB,R,N,GisVehicleConnected) vehicleConnected;
@property (TB,R,N,GisVehicleWifiHint) vehicleWifiHint;
@property (TB,R,N,GisVehicleGpsHint) vehicleGpsHint;
@property (TB,R,N,GisVehicleBasebandHint) vehicleBasebandHint;
@property (TB,R,N,GisVehicleMotionHint) vehicleMotionHint;
@property (TB,R,N,GisVehicleBTHint) vehicleBTHint;
@property (TB,R,N,GisMounted) mounted;
@property (Td,R,N) mountedProbability;
@property (Tq,R,N) vehicleType;
@property (Tq,R,N) confidence;
@property (T@"NSDate",R,N) startDate;
@property (TB,R,N) unknown;
@property (TB,R,N) stationary;
@property (TB,R,N) walking;
@property (TB,R,N) running;
@property (TB,R,N) automotive;
@property (TB,R,N) cycling;
```

## Class methods

```
+[CMMotionActivity supportsSecureCoding];
```

## Instance methods

```
-[CMMotionActivity isMounted];
-[CMMotionActivity startDate];
-[CMMotionActivity unknown];
-[CMMotionActivity isSameStateAs:];
-[CMMotionActivity setEndTime:];
-[CMMotionActivity walking];
-[CMMotionActivity initWithMotionActivity:];
-[CMMotionActivity descriptionInternal];
-[CMMotionActivity dealloc];
-[CMMotionActivity vehicleType];
-[CMMotionActivity endDate];
-[CMMotionActivity automotive];
-[CMMotionActivity isVehicleWifiHint];
-[CMMotionActivity running];
-[CMMotionActivity setIsRunWalk:];
-[CMMotionActivity isVehicleGpsHint];
-[CMMotionActivity encodeWithCoder:];
-[CMMotionActivity isVehicleMotionHint];
-[CMMotionActivity isRunWalk];
-[CMMotionActivity mountedProbability];
-[CMMotionActivity description];
-[CMMotionActivity isVehicleBTHint];
-[CMMotionActivity initWithCoder:];
-[CMMotionActivity isVehicleBasebandHint];
-[CMMotionActivity cycling];
-[CMMotionActivity copyWithZone:];
-[CMMotionActivity isVehicleConnected];
-[CMMotionActivity confidence];
-[CMMotionActivity initWithMotionActivity:endDate:];
-[CMMotionActivity motionActivity];
-[CMMotionActivity stationary];
```
