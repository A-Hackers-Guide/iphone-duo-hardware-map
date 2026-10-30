# `CMVO2MaxInputs`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampleExporting`, `NSSecureCoding`, `NSCopying`
- 16 instance variables, 20 properties, 28 instance methods, 3 class methods

## Instance variables

```
Q fRecordId;
@"NSDate" fStartDate;
@"NSUUID" fWorkoutSessionId;
d fMets;
q fMetSource;
d fHeartRate;
d fHeartRateConfidence;
q fGradeType;
d fGrade;
d fCadence;
d fPace;
B fHasGPS;
B fHasStrideCal;
q fWorkoutType;
B fIsStroller;
d fHeartRateTime;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R,N) recordId;
@property (T@"NSDate",R,N) startDate;
@property (T@"NSUUID",&,N,VfWorkoutSessionId) workoutSessionId;
@property (Td,R,N) mets;
@property (Tq,R,N) metSource;
@property (Td,R,N) heartRate;
@property (Td,R,N) heartRateConfidence;
@property (Td,R,N) grade;
@property (Tq,R,N) gradeType;
@property (Td,R,N) cadence;
@property (Td,R,N) pace;
@property (TB,R,N) hasGPS;
@property (TB,R,N) hasStrideCal;
@property (Tq,R,N) workoutType;
@property (TB,R,N) isStroller;
@property (Td,R,N) heartRateTime;
```

## Class methods

```
+[CMVO2MaxInputs supportsSecureCoding];
+[CMVO2MaxInputs VO2MaxInputFromCMVO2MaxInputs:];
+[CMVO2MaxInputs inputFromPreparedStatement:];
```

## Instance methods

```
-[CMVO2MaxInputs startDate];
-[CMVO2MaxInputs grade];
-[CMVO2MaxInputs cadence];
-[CMVO2MaxInputs recordId];
-[CMVO2MaxInputs dealloc];
-[CMVO2MaxInputs encodeWithCoder:];
-[CMVO2MaxInputs workoutType];
-[CMVO2MaxInputs description];
-[CMVO2MaxInputs initWithCoder:];
-[CMVO2MaxInputs copyWithZone:];
-[CMVO2MaxInputs isEqual:];
-[CMVO2MaxInputs heartRate];
-[CMVO2MaxInputs hasGPS];
-[CMVO2MaxInputs initWithSample:];
-[CMVO2MaxInputs binarySampleRepresentation];
-[CMVO2MaxInputs gradeType];
-[CMVO2MaxInputs hasStrideCal];
-[CMVO2MaxInputs heartRateConfidence];
-[CMVO2MaxInputs heartRateTime];
-[CMVO2MaxInputs initWithBinarySampleRepresentation:metadata:timestamp:];
-[CMVO2MaxInputs initWithRecordId:startDate:mets:metSource:heartRate:heartRateConfidence:gradeType:grade:cadence:pace:hasGPS:hasStrideCal:workoutType:isStroller:heartRateTime:];
-[CMVO2MaxInputs isStroller];
-[CMVO2MaxInputs metSource];
-[CMVO2MaxInputs mets];
-[CMVO2MaxInputs pace];
-[CMVO2MaxInputs setWorkoutSessionId:];
-[CMVO2MaxInputs sr_dictionaryRepresentation];
-[CMVO2MaxInputs workoutSessionId];
```
