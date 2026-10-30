# `CMWorkoutPhysicalEffort`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampleExporting`, `NSSecureCoding`, `NSCopying`
- 7 instance variables, 11 properties, 18 instance methods, 3 class methods

## Instance variables

```
Q fRecordId;
@"NSDate" fStartDate;
d fMets;
q fGradeType;
d fGrade;
d fUserMets;
q fMetsSource;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R,N) recordId;
@property (T@"NSDate",R,N) startDate;
@property (Td,R,N) mets;
@property (Tq,R,N) gradeType;
@property (Td,R,N) grade;
@property (Td,R,N) userMets;
@property (Tq,R,N) metsSource;
```

## Class methods

```
+[CMWorkoutPhysicalEffort supportsSecureCoding];
+[CMWorkoutPhysicalEffort HRRecoveryInputWRFromCMWorkoutPhysicalEffort:];
+[CMWorkoutPhysicalEffort inputFromPreparedStatement:];
```

## Instance methods

```
-[CMWorkoutPhysicalEffort startDate];
-[CMWorkoutPhysicalEffort grade];
-[CMWorkoutPhysicalEffort recordId];
-[CMWorkoutPhysicalEffort dealloc];
-[CMWorkoutPhysicalEffort encodeWithCoder:];
-[CMWorkoutPhysicalEffort description];
-[CMWorkoutPhysicalEffort initWithCoder:];
-[CMWorkoutPhysicalEffort copyWithZone:];
-[CMWorkoutPhysicalEffort isEqual:];
-[CMWorkoutPhysicalEffort initWithSample:];
-[CMWorkoutPhysicalEffort binarySampleRepresentation];
-[CMWorkoutPhysicalEffort gradeType];
-[CMWorkoutPhysicalEffort initWithBinarySampleRepresentation:metadata:timestamp:];
-[CMWorkoutPhysicalEffort initWithRecordId:startDate:mets:gradeType:grade:userMets:metsSource:];
-[CMWorkoutPhysicalEffort mets];
-[CMWorkoutPhysicalEffort metsSource];
-[CMWorkoutPhysicalEffort sr_dictionaryRepresentation];
-[CMWorkoutPhysicalEffort userMets];
```
