# `CMCardioFitnessInputsSessionMetrics`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampleExporting`, `NSSecureCoding`, `NSCopying`
- 8 instance variables, 12 properties, 19 instance methods, 3 class methods

## Instance variables

```
Q fRecordId;
@"NSDate" fStartDate;
@"NSUUID" fSessionId;
d fMeanMaxMets;
d fPrior;
I fHardwareType;
B fBetaBlockerUse;
q fAlgorithmVersion;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R,N) recordId;
@property (T@"NSDate",R,N) startDate;
@property (T@"NSUUID",R,&,N) sessionId;
@property (Td,R,N) meanMaxMets;
@property (Td,R,N) prior;
@property (TI,R,N) hardwareType;
@property (TB,R,N) betaBlockerUse;
@property (Tq,R,N) algorithmVersion;
```

## Class methods

```
+[CMCardioFitnessInputsSessionMetrics supportsSecureCoding];
+[CMCardioFitnessInputsSessionMetrics VO2MaxSessionAttributesFromCMCardioFitnessInputsSessionMetrics:];
+[CMCardioFitnessInputsSessionMetrics inputFromPreparedStatement:];
```

## Instance methods

```
-[CMCardioFitnessInputsSessionMetrics startDate];
-[CMCardioFitnessInputsSessionMetrics hardwareType];
-[CMCardioFitnessInputsSessionMetrics sessionId];
-[CMCardioFitnessInputsSessionMetrics recordId];
-[CMCardioFitnessInputsSessionMetrics dealloc];
-[CMCardioFitnessInputsSessionMetrics encodeWithCoder:];
-[CMCardioFitnessInputsSessionMetrics description];
-[CMCardioFitnessInputsSessionMetrics initWithCoder:];
-[CMCardioFitnessInputsSessionMetrics copyWithZone:];
-[CMCardioFitnessInputsSessionMetrics isEqual:];
-[CMCardioFitnessInputsSessionMetrics algorithmVersion];
-[CMCardioFitnessInputsSessionMetrics initWithSample:];
-[CMCardioFitnessInputsSessionMetrics betaBlockerUse];
-[CMCardioFitnessInputsSessionMetrics binarySampleRepresentation];
-[CMCardioFitnessInputsSessionMetrics initWithBinarySampleRepresentation:metadata:timestamp:];
-[CMCardioFitnessInputsSessionMetrics initWithRecordId:startDate:sessionId:meanMaxMets:prior:hardwareType:betaBlockerUse:algorithmVersion:];
-[CMCardioFitnessInputsSessionMetrics meanMaxMets];
-[CMCardioFitnessInputsSessionMetrics prior];
-[CMCardioFitnessInputsSessionMetrics sr_dictionaryRepresentation];
```
