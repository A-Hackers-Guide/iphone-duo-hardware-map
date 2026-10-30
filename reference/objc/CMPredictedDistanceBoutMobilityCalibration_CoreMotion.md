# `CMPredictedDistanceBoutMobilityCalibration`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampleExporting`, `NSSecureCoding`, `NSCopying`
- 7 instance variables, 11 properties, 18 instance methods, 2 class methods

## Instance variables

```
Q fRecordId;
@"NSDate" fStartDate;
@"NSDate" fEndDate;
d fCadenceWatch;
d fCadenceGaitCycle;
d fMeanWalkingSpeed;
d fGaitCycleYield;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R,N) recordId;
@property (T@"NSDate",R,N) startDate;
@property (T@"NSDate",R,N) endDate;
@property (Td,R,N) cadenceWatch;
@property (Td,R,N) cadenceGaitCycle;
@property (Td,R,N) meanWalkingSpeed;
@property (Td,R,N) gaitCycleYield;
```

## Class methods

```
+[CMPredictedDistanceBoutMobilityCalibration supportsSecureCoding];
+[CMPredictedDistanceBoutMobilityCalibration inputFromPreparedStatement:];
```

## Instance methods

```
-[CMPredictedDistanceBoutMobilityCalibration startDate];
-[CMPredictedDistanceBoutMobilityCalibration recordId];
-[CMPredictedDistanceBoutMobilityCalibration dealloc];
-[CMPredictedDistanceBoutMobilityCalibration endDate];
-[CMPredictedDistanceBoutMobilityCalibration encodeWithCoder:];
-[CMPredictedDistanceBoutMobilityCalibration description];
-[CMPredictedDistanceBoutMobilityCalibration initWithCoder:];
-[CMPredictedDistanceBoutMobilityCalibration copyWithZone:];
-[CMPredictedDistanceBoutMobilityCalibration isEqual:];
-[CMPredictedDistanceBoutMobilityCalibration binarySampleRepresentation];
-[CMPredictedDistanceBoutMobilityCalibration cadenceGaitCycle];
-[CMPredictedDistanceBoutMobilityCalibration cadenceWatch];
-[CMPredictedDistanceBoutMobilityCalibration gaitCycleYield];
-[CMPredictedDistanceBoutMobilityCalibration initWithBinarySampleRepresentation:metadata:timestamp:];
-[CMPredictedDistanceBoutMobilityCalibration initWithRecordId:startDate:endDate:cadenceWatch:cadenceGaitCycle:meanWalkingSpeed:gaitCycleYield:];
-[CMPredictedDistanceBoutMobilityCalibration initWithSample:recordId:];
-[CMPredictedDistanceBoutMobilityCalibration meanWalkingSpeed];
-[CMPredictedDistanceBoutMobilityCalibration sr_dictionaryRepresentation];
```
