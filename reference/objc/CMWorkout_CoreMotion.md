# `CMWorkout`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 9 instance variables, 8 properties, 24 instance methods, 15 class methods

## Instance variables

```
@"NSUUID" fSessionId;
q fType;
q fLocationType;
@"NSDate" fStartDate;
@"NSDate" fEndDate;
B fIsUserInitiated;
Q fMode;
@"NSString" fAppId;
B _isUserInitiated;
```

## Properties

```
@property (TB,R,N,V_isUserInitiated) isUserInitiated;
@property (T@"NSUUID",R,N) sessionId;
@property (Tq,R,N) type;
@property (Tq,R,N) locationType;
@property (TQ,R,N) mode;
@property (T@"NSDate",R,N) startDate;
@property (T@"NSDate",R,N) endDate;
@property (T@"NSString",C,N,VfAppId) appId;
```

## Class methods

```
+[CMWorkout supportsSecureCoding];
+[CMWorkout isAvailable];
+[CMWorkout CMSwimWorkoutLocationFromCMWorkoutLocationType:];
+[CMWorkout CMWorkoutTypeFromCLMotionActivityType:];
+[CMWorkout CLMotionActivityTypeFromCMWorkoutType:];
+[CMWorkout CMWorkoutLocationTypeFromCMSwimWorkoutLocation:];
+[CMWorkout workoutIsSupportedForLowPower:];
+[CMWorkout workoutIsTypePedestrian:];
+[CMWorkout workoutIsTypeRunning:];
+[CMWorkout workoutIsTypeWalking:];
+[CMWorkout workoutLocationName:];
+[CMWorkout workoutLocationTypeFromCMWorkoutType:];
+[CMWorkout workoutModeIsExtended:];
+[CMWorkout workoutModeName:];
+[CMWorkout workoutName:];
```

## Instance methods

```
-[CMWorkout startDate];
-[CMWorkout setLocationType:];
-[CMWorkout sessionId];
-[CMWorkout dealloc];
-[CMWorkout endDate];
-[CMWorkout type];
-[CMWorkout setWorkoutType:];
-[CMWorkout encodeWithCoder:];
-[CMWorkout mode];
-[CMWorkout isUserInitiated];
-[CMWorkout description];
-[CMWorkout initWithCoder:];
-[CMWorkout copyWithZone:];
-[CMWorkout locationType];
-[CMWorkout appId];
-[CMWorkout setIsUserInitiated:];
-[CMWorkout setAppId:];
-[CMWorkout setWorkoutMode:];
-[CMWorkout _initWithSessionId:type:locationType:mode:startDate:endDate:];
-[CMWorkout initWithSessionId:type:];
-[CMWorkout initWithSessionId:type:locationType:];
-[CMWorkout initWithSessionId:type:locationType:mode:];
-[CMWorkout initWithSessionId:type:locationType:mode:startDate:endDate:];
-[CMWorkout isSameWorkout:];
```
