# `CMRecoverySession`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampleExporting`, `NSSecureCoding`, `NSCopying`
- 16 instance variables, 20 properties, 28 instance methods, 3 class methods

## Instance variables

```
Q fRecordId;
@"NSDate" fStartDate;
d fActivityEndTime;
@"NSUUID" fWorkoutSessionId;
q fWorkoutType;
d fHrRecovery;
d fLambda;
d fHrMax;
d fHrMinAdjusted;
d fRecoveryOnsetTime;
d fSteadyStateHR;
q fStatus;
d fSessionHrRecovery;
d fPeakHR;
d fHrRecoveryReference;
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
@property (Td,R,N) activityEndTime;
@property (T@"NSUUID",R,&,N) workoutSessionId;
@property (Tq,R,N) workoutType;
@property (Td,R,N) hrRecovery;
@property (Td,R,N) lambda;
@property (Td,R,N) hrMax;
@property (Td,R,N) hrMinAdjusted;
@property (Td,R,N) recoveryOnsetTime;
@property (Td,R,N) steadyStateHR;
@property (Tq,R,N) status;
@property (Td,R,N) sessionHrRecovery;
@property (Td,R,N) peakHR;
@property (Td,R,N) hrRecoveryReference;
@property (Tq,R,N) testType;
```

## Class methods

```
+[CMRecoverySession supportsSecureCoding];
+[CMRecoverySession HRRecoverySessionFromCMRecoverySession:];
+[CMRecoverySession inputFromPreparedStatement:];
```

## Instance methods

```
-[CMRecoverySession startDate];
-[CMRecoverySession recordId];
-[CMRecoverySession dealloc];
-[CMRecoverySession status];
-[CMRecoverySession encodeWithCoder:];
-[CMRecoverySession hash];
-[CMRecoverySession workoutType];
-[CMRecoverySession description];
-[CMRecoverySession initWithCoder:];
-[CMRecoverySession copyWithZone:];
-[CMRecoverySession isEqual:];
-[CMRecoverySession lambda];
-[CMRecoverySession activityEndTime];
-[CMRecoverySession initWithSample:];
-[CMRecoverySession binarySampleRepresentation];
-[CMRecoverySession hrMax];
-[CMRecoverySession hrMinAdjusted];
-[CMRecoverySession hrRecovery];
-[CMRecoverySession hrRecoveryReference];
-[CMRecoverySession initWithBinarySampleRepresentation:metadata:timestamp:];
-[CMRecoverySession initWithRecordId:startDate:activityEndTime:workoutSessionId:workoutType:hrRecovery:lambda:hrMax:hrMinAdjusted:recoveryOnsetTime:steadyStateHR:status:sessionHrRecovery:peakHR:hrRecoveryReference:testType:];
-[CMRecoverySession peakHR];
-[CMRecoverySession recoveryOnsetTime];
-[CMRecoverySession sessionHrRecovery];
-[CMRecoverySession sr_dictionaryRepresentation];
-[CMRecoverySession steadyStateHR];
-[CMRecoverySession testType];
-[CMRecoverySession workoutSessionId];
```
