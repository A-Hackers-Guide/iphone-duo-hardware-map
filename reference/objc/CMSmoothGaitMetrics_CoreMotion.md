# `CMSmoothGaitMetrics`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampleExporting`, `NSSecureCoding`, `NSCopying`
- 9 instance variables, 13 properties, 20 instance methods, 2 class methods

## Instance variables

```
Q fRecordId;
@"NSDate" fStartDate;
d fWalkingSpeed;
d fStepLength;
d fCycleTime;
d fDistance;
d fDoubleSupportPercentage;
d fAsymmetryProbability;
I fNumGaitMetrics;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R,N) recordId;
@property (T@"NSDate",R,N) startDate;
@property (Td,R,N) walkingSpeed;
@property (Td,R,N) stepLength;
@property (Td,R,N) cycleTime;
@property (Td,R,N) distance;
@property (Td,R,N) doubleSupportPercentage;
@property (Td,R,N) asymmetryProbability;
@property (TI,R,N) numGaitMetrics;
```

## Class methods

```
+[CMSmoothGaitMetrics supportsSecureCoding];
+[CMSmoothGaitMetrics inputFromPreparedStatement:];
```

## Instance methods

```
-[CMSmoothGaitMetrics startDate];
-[CMSmoothGaitMetrics distance];
-[CMSmoothGaitMetrics recordId];
-[CMSmoothGaitMetrics dealloc];
-[CMSmoothGaitMetrics encodeWithCoder:];
-[CMSmoothGaitMetrics description];
-[CMSmoothGaitMetrics initWithCoder:];
-[CMSmoothGaitMetrics copyWithZone:];
-[CMSmoothGaitMetrics isEqual:];
-[CMSmoothGaitMetrics initWithSample:];
-[CMSmoothGaitMetrics asymmetryProbability];
-[CMSmoothGaitMetrics binarySampleRepresentation];
-[CMSmoothGaitMetrics cycleTime];
-[CMSmoothGaitMetrics doubleSupportPercentage];
-[CMSmoothGaitMetrics initWithBinarySampleRepresentation:metadata:timestamp:];
-[CMSmoothGaitMetrics initWithRecordId:startDate:walkingSpeed:stepLength:cycleTime:distance:doubleSupportPercentage:asymmetryProbability:numGaitMetrics:];
-[CMSmoothGaitMetrics numGaitMetrics];
-[CMSmoothGaitMetrics sr_dictionaryRepresentation];
-[CMSmoothGaitMetrics stepLength];
-[CMSmoothGaitMetrics walkingSpeed];
```
