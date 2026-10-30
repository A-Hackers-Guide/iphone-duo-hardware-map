# `CMPedometerData`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampling`, `NSSecureCoding`, `NSCopying`
- 19 instance variables, 22 properties, 28 instance methods, 2 class methods

## Instance variables

```
@"NSDate" fStartDate;
@"NSDate" fEndDate;
@"NSNumber" fNumberOfSteps;
@"NSNumber" fDistance;
@"NSNumber" fFloorsAscended;
@"NSNumber" fFloorsDescended;
@"NSNumber" fRecordId;
@"NSNumber" fCurrentPace;
@"NSNumber" fCurrentCadence;
@"NSDate" fFirstStepTime;
@"NSNumber" fActiveTime;
@"NSUUID" fSourceId;
@"NSNumber" fIsOdometerDistance;
@"NSNumber" fIsOdometerPace;
@"NSNumber" fNumberOfPushes;
@"NSNumber" fWorkoutType;
@"NSNumber" fElevationAscended;
@"NSNumber" fElevationDescended;
@"NSNumber" fDistanceSource;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Tq,R,N) recordId;
@property (T@"NSUUID",R,N) sourceId;
@property (T@"NSNumber",R,N) numberOfPushes;
@property (T@"NSNumber",R,N) workoutType;
@property (T@"NSNumber",R,N) elevationAscended;
@property (T@"NSNumber",R,N) elevationDescended;
@property (T@"NSNumber",R,N) distanceSource;
@property (T@"NSDate",R,N) firstStepTime;
@property (T@"NSNumber",R,N) activeTime;
@property (T@"NSDate",R,N) startDate;
@property (T@"NSDate",R,N) endDate;
@property (T@"NSNumber",R,N) numberOfSteps;
@property (T@"NSNumber",R,N) distance;
@property (T@"NSNumber",R,N) floorsAscended;
@property (T@"NSNumber",R,N) floorsDescended;
@property (T@"NSNumber",R,N) currentPace;
@property (T@"NSNumber",R,N) currentCadence;
@property (T@"NSNumber",R,N) averageActivePace;
```

## Class methods

```
+[CMPedometerData supportsSecureCoding];
+[CMPedometerData maxPedometerEntries];
```

## Instance methods

```
-[CMPedometerData startDate];
-[CMPedometerData distance];
-[CMPedometerData sourceId];
-[CMPedometerData recordId];
-[CMPedometerData dealloc];
-[CMPedometerData endDate];
-[CMPedometerData numberOfSteps];
-[CMPedometerData encodeWithCoder:];
-[CMPedometerData workoutType];
-[CMPedometerData description];
-[CMPedometerData initWithCoder:];
-[CMPedometerData copyWithZone:];
-[CMPedometerData floorsDescended];
-[CMPedometerData activeTime];
-[CMPedometerData averageActivePace];
-[CMPedometerData binarySampleRepresentation];
-[CMPedometerData currentCadence];
-[CMPedometerData currentPace];
-[CMPedometerData distanceSource];
-[CMPedometerData elevationAscended];
-[CMPedometerData elevationDescended];
-[CMPedometerData firstStepTime];
-[CMPedometerData floorsAscended];
-[CMPedometerData initWithBinarySampleRepresentation:metadata:timestamp:];
-[CMPedometerData initWithStartDate:endDate:steps:distance:floorsAscended:floorsDescended:recordID:currentPace:currentCadence:firstStepTime:activeTime:sourceId:isOdometerDistance:isOdometerPace:pushes:workoutType:elevationAscended:elevationDescended:distanceSource:];
-[CMPedometerData isOdometerDistance];
-[CMPedometerData isOdometerPace];
-[CMPedometerData numberOfPushes];
```
