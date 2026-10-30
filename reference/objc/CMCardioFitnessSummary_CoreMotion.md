# `CMCardioFitnessSummary`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampleExporting`, `NSSecureCoding`, `NSCopying`
- 19 instance variables, 23 properties, 30 instance methods, 3 class methods

## Instance variables

```
Q fRecordId;
@"NSDate" fStartDate;
q fWorkoutType;
@"NSUUID" fSessionId;
d fDurationInSeconds;
Q fPointCount;
d fHRMax;
d fHRMin;
d fMeanHr;
d fMeanVo2;
d fMeanSpeed;
d fMeanGrade;
d fMeanHrConfidence;
d fMeanHrCadenceAgreement;
d fMeanCadence;
q fVo2MaxModelSource;
q fSessionType;
q fPlatformSource;
d _meanMaxMets;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R,N) recordId;
@property (T@"NSDate",R,N) startDate;
@property (Td,R,N,V_meanMaxMets) meanMaxMets;
@property (Tq,R,N) workoutType;
@property (T@"NSUUID",R,&,N) sessionId;
@property (Td,R,N) durationInSeconds;
@property (TQ,R,N) pointCount;
@property (Td,R,N) hrMax;
@property (Td,R,N) hrMin;
@property (Td,R,N) meanHr;
@property (Td,R,N) meanVo2;
@property (Td,R,N) meanSpeed;
@property (Td,R,N) meanGrade;
@property (Td,R,N) meanHrConfidence;
@property (Td,R,N) meanHrCadenceAgreement;
@property (Td,R,N) meanCadence;
@property (Tq,R,N) vo2MaxModelSource;
@property (Tq,R,N) sessionType;
@property (Tq,R,N) platformSource;
```

## Class methods

```
+[CMCardioFitnessSummary supportsSecureCoding];
+[CMCardioFitnessSummary VO2MaxSummaryFromCMCardioFitnessSummary:];
+[CMCardioFitnessSummary inputFromPreparedStatement:];
```

## Instance methods

```
-[CMCardioFitnessSummary pointCount];
-[CMCardioFitnessSummary startDate];
-[CMCardioFitnessSummary sessionId];
-[CMCardioFitnessSummary recordId];
-[CMCardioFitnessSummary dealloc];
-[CMCardioFitnessSummary sessionType];
-[CMCardioFitnessSummary encodeWithCoder:];
-[CMCardioFitnessSummary workoutType];
-[CMCardioFitnessSummary description];
-[CMCardioFitnessSummary initWithCoder:];
-[CMCardioFitnessSummary copyWithZone:];
-[CMCardioFitnessSummary durationInSeconds];
-[CMCardioFitnessSummary isEqual:];
-[CMCardioFitnessSummary meanVo2];
-[CMCardioFitnessSummary initWithSample:];
-[CMCardioFitnessSummary binarySampleRepresentation];
-[CMCardioFitnessSummary hrMax];
-[CMCardioFitnessSummary hrMin];
-[CMCardioFitnessSummary initWithBinarySampleRepresentation:metadata:timestamp:];
-[CMCardioFitnessSummary initWithRecordId:startDate:workoutType:sessionId:durationInSeconds:pointCount:hrMax:hrMin:meanHr:meanVo2:meanSpeed:meanGrade:meanHrConfidence:meanHrCadenceAgreement:meanCadence:vo2MaxModelSource:sessionType:platformSource:];
-[CMCardioFitnessSummary meanCadence];
-[CMCardioFitnessSummary meanGrade];
-[CMCardioFitnessSummary meanHr];
-[CMCardioFitnessSummary meanHrCadenceAgreement];
-[CMCardioFitnessSummary meanHrConfidence];
-[CMCardioFitnessSummary meanMaxMets];
-[CMCardioFitnessSummary meanSpeed];
-[CMCardioFitnessSummary platformSource];
-[CMCardioFitnessSummary sr_dictionaryRepresentation];
-[CMCardioFitnessSummary vo2MaxModelSource];
```
