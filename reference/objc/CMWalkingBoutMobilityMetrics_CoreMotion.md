# `CMWalkingBoutMobilityMetrics`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampleExporting`, `NSSecureCoding`, `NSCopying`
- 41 instance variables, 45 properties, 52 instance methods, 2 class methods

## Instance variables

```
Q fRecordId;
@"NSDate" fStartDate;
@"NSDate" fEndDate;
i fStepCount;
i fWorkoutType;
i fNumGaitMetrics;
q fDeviceSide;
d fWalkingSpeed;
d fDoubleSupportPercentage;
d fStepLength;
d fAsymmetryPercentage;
d fUserHeight;
B fIsHeightSet;
d fUserWeight;
B fIsWeightSet;
q fBoundaryType;
d fCycleTimeMean;
q fTerminationReason;
d fInvalidGradePercentage;
I fSegmentsRejectedByIsSwingStanceCycle;
I fSegmentsRejectedByIsNotRunning;
I fSegmentsRejectedByIsFeasibleWalkingSpeed;
I fSegmentsRejectedByIsPendular;
I fSegmentsRejectedByIsSufficientVerticalTwist;
I fSegmentsRejectedByIsCadenceConcordant;
I fWalkingSpeedRejectionStatus;
I fDoubleSupportPercentageRejectionStatus;
I fStepLengthRejectionStatus;
I fAsymmetryPercentageRejectionStatus;
d fStepLengthEntropy;
d fStepLengthPoincareSD1;
d fStepLengthPoincareSD2;
d fCycleTimeEntropy;
d fCycleTimePoincareSD1;
d fCycleTimePoincareSD2;
d fStepIndexOfHarmonicityAP;
d fStepIndexOfHarmonicityML;
d fStepIndexOfHarmonicityVT;
d fSwingIndexOfHarmonicityAP;
d fSwingIndexOfHarmonicityML;
d fSwingIndexOfHarmonicityVT;
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
@property (Ti,R,N) stepCount;
@property (Ti,R,N) workoutType;
@property (Ti,R,N) numGaitMetrics;
@property (Tq,R,N) deviceSide;
@property (Td,R,N) walkingSpeed;
@property (Td,R,N) doubleSupportPercentage;
@property (Td,R,N) stepLength;
@property (Td,R,N) asymmetryPercentage;
@property (Td,R,N) userHeight;
@property (TB,R,N) isHeightSet;
@property (Td,R,N) userWeight;
@property (TB,R,N) isWeightSet;
@property (Tq,R,N) boundaryType;
@property (Td,R,N) cycleTimeMean;
@property (Tq,R,N) terminationReason;
@property (Td,R,N) invalidGradePercentage;
@property (TI,R,N) segmentsRejectedByIsSwingStanceCycle;
@property (TI,R,N) segmentsRejectedByIsNotRunning;
@property (TI,R,N) segmentsRejectedByIsFeasibleWalkingSpeed;
@property (TI,R,N) segmentsRejectedByIsPendular;
@property (TI,R,N) segmentsRejectedByIsSufficientVerticalTwist;
@property (TI,R,N) segmentsRejectedByIsCadenceConcordant;
@property (TI,R,N) walkingSpeedRejectionStatus;
@property (TI,R,N) doubleSupportPercentageRejectionStatus;
@property (TI,R,N) stepLengthRejectionStatus;
@property (TI,R,N) asymmetryPercentageRejectionStatus;
@property (Td,R,N) stepLengthEntropy;
@property (Td,R,N) stepLengthPoincareSD1;
@property (Td,R,N) stepLengthPoincareSD2;
@property (Td,R,N) cycleTimeEntropy;
@property (Td,R,N) cycleTimePoincareSD1;
@property (Td,R,N) cycleTimePoincareSD2;
@property (Td,R,N) stepIndexOfHarmonicityAP;
@property (Td,R,N) stepIndexOfHarmonicityML;
@property (Td,R,N) stepIndexOfHarmonicityVT;
@property (Td,R,N) swingIndexOfHarmonicityAP;
@property (Td,R,N) swingIndexOfHarmonicityML;
@property (Td,R,N) swingIndexOfHarmonicityVT;
```

## Class methods

```
+[CMWalkingBoutMobilityMetrics supportsSecureCoding];
+[CMWalkingBoutMobilityMetrics inputFromPreparedStatement:];
```

## Instance methods

```
-[CMWalkingBoutMobilityMetrics startDate];
-[CMWalkingBoutMobilityMetrics stepCount];
-[CMWalkingBoutMobilityMetrics recordId];
-[CMWalkingBoutMobilityMetrics dealloc];
-[CMWalkingBoutMobilityMetrics endDate];
-[CMWalkingBoutMobilityMetrics encodeWithCoder:];
-[CMWalkingBoutMobilityMetrics workoutType];
-[CMWalkingBoutMobilityMetrics description];
-[CMWalkingBoutMobilityMetrics initWithCoder:];
-[CMWalkingBoutMobilityMetrics copyWithZone:];
-[CMWalkingBoutMobilityMetrics terminationReason];
-[CMWalkingBoutMobilityMetrics isEqual:];
-[CMWalkingBoutMobilityMetrics initWithSample:];
-[CMWalkingBoutMobilityMetrics asymmetryPercentage];
-[CMWalkingBoutMobilityMetrics asymmetryPercentageRejectionStatus];
-[CMWalkingBoutMobilityMetrics binarySampleRepresentation];
-[CMWalkingBoutMobilityMetrics boundaryType];
-[CMWalkingBoutMobilityMetrics cycleTimeEntropy];
-[CMWalkingBoutMobilityMetrics cycleTimeMean];
-[CMWalkingBoutMobilityMetrics cycleTimePoincareSD1];
-[CMWalkingBoutMobilityMetrics cycleTimePoincareSD2];
-[CMWalkingBoutMobilityMetrics deviceSide];
-[CMWalkingBoutMobilityMetrics doubleSupportPercentage];
-[CMWalkingBoutMobilityMetrics doubleSupportPercentageRejectionStatus];
-[CMWalkingBoutMobilityMetrics initWithBinarySampleRepresentation:metadata:timestamp:];
-[CMWalkingBoutMobilityMetrics initWithRecordId:startTime:endTime:stepCount:workoutType:numGaitMetrics:deviceSide:walkingSpeed:doubleSupportPercentage:stepLength:asymmetryPercentage:userHeight:userWeight:isHeightSet:isWeightSet:boundaryType:cycleTimeMean:terminationReason:invalidGradePercentage:segmentsRejectedByIsSwingStanceCycle:segmentsRejectedByIsNotRunning:segmentsRejectedByIsFeasibleWalkingSpeed:segmentsRejectedByIsPendular:segmentsRejectedByIsSufficientVerticalTwist:segmentsRejectedByIsCadenceConcordant:walkingSpeedRejectionStatus:doubleSupportPercentageRejectionStatus:stepLengthRejectionStatus:asymmetryPercentageRejectionStatus:stepLengthEntropy:stepLengthPoincareSD1:stepLengthPoincareSD2:cycleTimeEntropy:cycleTimePoincareSD1:cycleTimePoincareSD2:stepIndexOfHarmonicityAP:stepIndexOfHarmonicityML:stepIndexOfHarmonicityVT:swingIndexOfHarmonicityAP:swingIndexOfHarmonicityML:swingIndexOfHarmonicityVT:];
-[CMWalkingBoutMobilityMetrics invalidGradePercentage];
-[CMWalkingBoutMobilityMetrics isHeightSet];
-[CMWalkingBoutMobilityMetrics isWeightSet];
-[CMWalkingBoutMobilityMetrics numGaitMetrics];
-[CMWalkingBoutMobilityMetrics segmentsRejectedByIsCadenceConcordant];
-[CMWalkingBoutMobilityMetrics segmentsRejectedByIsFeasibleWalkingSpeed];
-[CMWalkingBoutMobilityMetrics segmentsRejectedByIsNotRunning];
-[CMWalkingBoutMobilityMetrics segmentsRejectedByIsPendular];
-[CMWalkingBoutMobilityMetrics segmentsRejectedByIsSufficientVerticalTwist];
-[CMWalkingBoutMobilityMetrics segmentsRejectedByIsSwingStanceCycle];
-[CMWalkingBoutMobilityMetrics sr_dictionaryRepresentation];
-[CMWalkingBoutMobilityMetrics stepIndexOfHarmonicityAP];
-[CMWalkingBoutMobilityMetrics stepIndexOfHarmonicityML];
-[CMWalkingBoutMobilityMetrics stepIndexOfHarmonicityVT];
-[CMWalkingBoutMobilityMetrics stepLength];
-[CMWalkingBoutMobilityMetrics stepLengthEntropy];
-[CMWalkingBoutMobilityMetrics stepLengthPoincareSD1];
-[CMWalkingBoutMobilityMetrics stepLengthPoincareSD2];
-[CMWalkingBoutMobilityMetrics stepLengthRejectionStatus];
-[CMWalkingBoutMobilityMetrics swingIndexOfHarmonicityAP];
-[CMWalkingBoutMobilityMetrics swingIndexOfHarmonicityML];
-[CMWalkingBoutMobilityMetrics swingIndexOfHarmonicityVT];
-[CMWalkingBoutMobilityMetrics userHeight];
-[CMWalkingBoutMobilityMetrics userWeight];
-[CMWalkingBoutMobilityMetrics walkingSpeed];
-[CMWalkingBoutMobilityMetrics walkingSpeedRejectionStatus];
```
