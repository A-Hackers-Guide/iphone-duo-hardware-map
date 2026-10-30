# `CMCardioHealthSample`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 10 instance variables, 10 properties, 18 instance methods, 1 class methods

## Instance variables

```
Q _cardioHealthDataType;
@"CMVO2MaxInputs" _vo2maxInput;
@"CMCardioFitnessResults" _vo2MaxResult;
@"CMCardioFitnessSummary" _vo2MaxSummary;
@"CMCardioFitnessInputsSessionMetrics" _vo2MaxSessionAttribute;
@"CMVO2MaxPriorData" _vo2maxPrior;
@"CMRecoveryHeartRate" _recoveryHeartRate;
@"CMWorkoutPhysicalEffort" _recoveryWorkRate;
@"CMRecoverySession" _recoverySession;
@"CMSedentaryRestingHeartRateData" _sedentaryRestingHR;
```

## Properties

```
@property (TQ,V_cardioHealthDataType) cardioHealthDataType;
@property (T@"CMVO2MaxInputs",R,V_vo2maxInput) vo2maxInput;
@property (T@"CMCardioFitnessResults",R,V_vo2MaxResult) vo2MaxResult;
@property (T@"CMCardioFitnessSummary",R,V_vo2MaxSummary) vo2MaxSummary;
@property (T@"CMCardioFitnessInputsSessionMetrics",R,V_vo2MaxSessionAttribute) vo2MaxSessionAttribute;
@property (T@"CMVO2MaxPriorData",R,V_vo2maxPrior) vo2maxPrior;
@property (T@"CMRecoveryHeartRate",R,V_recoveryHeartRate) recoveryHeartRate;
@property (T@"CMWorkoutPhysicalEffort",R,V_recoveryWorkRate) recoveryWorkRate;
@property (T@"CMRecoverySession",R,V_recoverySession) recoverySession;
@property (T@"CMSedentaryRestingHeartRateData",R,V_sedentaryRestingHR) sedentaryRestingHR;
```

## Class methods

```
+[CMCardioHealthSample supportsSecureCoding];
```

## Instance methods

```
-[CMCardioHealthSample dealloc];
-[CMCardioHealthSample encodeWithCoder:];
-[CMCardioHealthSample description];
-[CMCardioHealthSample initWithCoder:];
-[CMCardioHealthSample copyWithZone:];
-[CMCardioHealthSample isEqual:];
-[CMCardioHealthSample initWithType:object:];
-[CMCardioHealthSample recoverySession];
-[CMCardioHealthSample cardioHealthDataType];
-[CMCardioHealthSample recoveryHeartRate];
-[CMCardioHealthSample recoveryWorkRate];
-[CMCardioHealthSample sedentaryRestingHR];
-[CMCardioHealthSample setCardioHealthDataType:];
-[CMCardioHealthSample vo2MaxResult];
-[CMCardioHealthSample vo2MaxSessionAttribute];
-[CMCardioHealthSample vo2MaxSummary];
-[CMCardioHealthSample vo2maxInput];
-[CMCardioHealthSample vo2maxPrior];
```
