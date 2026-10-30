# `CMCardioFitnessResults`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampleExporting`, `NSSecureCoding`, `NSCopying`
- 19 instance variables, 23 properties, 31 instance methods, 3 class methods

## Instance variables

```
Q fRecordId;
@"NSDate" fStartDate;
q fWorkoutType;
@"NSUUID" fSessionId;
d fEstimatedVo2Max;
d fDurationInSeconds;
d fHRMax;
d fHRMin;
d fVariance;
d fFilteredVo2Max;
q fSessionType;
B fEligibleForHealthKit;
B fEligibleForCalorimetry;
Q fNumWorkoutsContrToEstimate;
d fEstimatedHRResponseParam;
d fEstimatedHRRecoveryParam;
d fSessionVo2Max;
q fPlatformSource;
q fTestType;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R,N) recordId;
@property (T@"NSDate",R,N) startDate;
@property (Tq,R,N) workoutType;
@property (T@"NSUUID",R,&,N) sessionId;
@property (Td,R,N) estimatedVo2Max;
@property (Td,R,N) durationInSeconds;
@property (Td,R,N) hrMax;
@property (Td,R,N) hrMin;
@property (Td,R,N) variance;
@property (Td,R,N) filteredVo2Max;
@property (Tq,R,N) sessionType;
@property (TB,R,N) eligibleForHealthKit;
@property (TB,R,N) eligibleForCalorimetry;
@property (TQ,R,N) numWorkoutsContrToEstimate;
@property (Td,R,N) estimatedHRResponseParam;
@property (Td,R,N) estimatedHRRecoveryParam;
@property (Td,R,N) sessionVo2Max;
@property (Tq,R,N) platformSource;
@property (Tq,R,N) testType;
```

## Class methods

```
+[CMCardioFitnessResults supportsSecureCoding];
+[CMCardioFitnessResults VO2MaxOutputFromCMCardioFitnessResults:];
+[CMCardioFitnessResults inputFromPreparedStatement:];
```

## Instance methods

```
-[CMCardioFitnessResults startDate];
-[CMCardioFitnessResults sessionId];
-[CMCardioFitnessResults recordId];
-[CMCardioFitnessResults dealloc];
-[CMCardioFitnessResults sessionType];
-[CMCardioFitnessResults encodeWithCoder:];
-[CMCardioFitnessResults hash];
-[CMCardioFitnessResults workoutType];
-[CMCardioFitnessResults description];
-[CMCardioFitnessResults initWithCoder:];
-[CMCardioFitnessResults copyWithZone:];
-[CMCardioFitnessResults durationInSeconds];
-[CMCardioFitnessResults isEqual:];
-[CMCardioFitnessResults variance];
-[CMCardioFitnessResults estimatedVo2Max];
-[CMCardioFitnessResults initWithSample:];
-[CMCardioFitnessResults binarySampleRepresentation];
-[CMCardioFitnessResults eligibleForCalorimetry];
-[CMCardioFitnessResults eligibleForHealthKit];
-[CMCardioFitnessResults estimatedHRRecoveryParam];
-[CMCardioFitnessResults estimatedHRResponseParam];
-[CMCardioFitnessResults filteredVo2Max];
-[CMCardioFitnessResults hrMax];
-[CMCardioFitnessResults hrMin];
-[CMCardioFitnessResults initWithBinarySampleRepresentation:metadata:timestamp:];
-[CMCardioFitnessResults initWithRecordId:startDate:workoutType:sessionId:estimatedVo2Max:durationInSeconds:hrMax:hrMin:variance:filteredVo2Max:sessionType:eligibleForHealthKit:eligibleForCalorimetry:numWorkoutsContrToEstimate:estimatedHRResponseParam:estimatedHRRecoveryParam:sessionVo2Max:platformSource:testType:];
-[CMCardioFitnessResults numWorkoutsContrToEstimate];
-[CMCardioFitnessResults platformSource];
-[CMCardioFitnessResults sessionVo2Max];
-[CMCardioFitnessResults sr_dictionaryRepresentation];
-[CMCardioFitnessResults testType];
```
