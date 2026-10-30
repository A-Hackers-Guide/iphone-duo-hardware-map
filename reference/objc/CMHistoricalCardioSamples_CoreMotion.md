# `CMHistoricalCardioSamples`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampling`, `SRSampleExporting`, `NSSecureCoding`, `NSCopying`
- 8 instance variables, 12 properties, 26 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _cardioFitnessInputs;
@"NSArray" _cardioSessionMetrics;
@"NSArray" _cardioFitnessResults;
@"NSArray" _cardioFitnessSummary;
@"NSArray" _recoveryHeartRate;
@"NSArray" _recoveryWorkRate;
@"NSArray" _recoverySessions;
@"NSArray" _pedestrianGrade;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSArray",&,V_cardioFitnessInputs) cardioFitnessInputs;
@property (T@"NSArray",&,V_cardioSessionMetrics) cardioSessionMetrics;
@property (T@"NSArray",&,V_cardioFitnessResults) cardioFitnessResults;
@property (T@"NSArray",&,V_cardioFitnessSummary) cardioFitnessSummary;
@property (T@"NSArray",&,V_recoveryHeartRate) recoveryHeartRate;
@property (T@"NSArray",&,V_recoveryWorkRate) recoveryWorkRate;
@property (T@"NSArray",&,V_recoverySessions) recoverySessions;
@property (T@"NSArray",&,V_pedestrianGrade) pedestrianGrade;
```

## Class methods

```
+[CMHistoricalCardioSamples supportsSecureCoding];
```

## Instance methods

```
-[CMHistoricalCardioSamples init];
-[CMHistoricalCardioSamples dealloc];
-[CMHistoricalCardioSamples encodeWithCoder:];
-[CMHistoricalCardioSamples description];
-[CMHistoricalCardioSamples initWithCoder:];
-[CMHistoricalCardioSamples copyWithZone:];
-[CMHistoricalCardioSamples isEqual:];
-[CMHistoricalCardioSamples pedestrianGrade];
-[CMHistoricalCardioSamples binarySampleRepresentation];
-[CMHistoricalCardioSamples cardioFitnessInputs];
-[CMHistoricalCardioSamples cardioFitnessResults];
-[CMHistoricalCardioSamples cardioFitnessSummary];
-[CMHistoricalCardioSamples cardioSessionMetrics];
-[CMHistoricalCardioSamples initWithBinarySampleRepresentation:metadata:timestamp:];
-[CMHistoricalCardioSamples recoveryHeartRate];
-[CMHistoricalCardioSamples recoverySessions];
-[CMHistoricalCardioSamples recoveryWorkRate];
-[CMHistoricalCardioSamples setCardioFitnessInputs:];
-[CMHistoricalCardioSamples setCardioFitnessResults:];
-[CMHistoricalCardioSamples setCardioFitnessSummary:];
-[CMHistoricalCardioSamples setCardioSessionMetrics:];
-[CMHistoricalCardioSamples setPedestrianGrade:];
-[CMHistoricalCardioSamples setRecoveryHeartRate:];
-[CMHistoricalCardioSamples setRecoverySessions:];
-[CMHistoricalCardioSamples setRecoveryWorkRate:];
-[CMHistoricalCardioSamples sr_dictionaryRepresentation];
```
