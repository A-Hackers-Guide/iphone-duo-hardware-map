# `BIBatteryAnalysisOutput`

- Image: [`/System/Library/PrivateFrameworks/BatteryIntelligence.framework/BatteryIntelligence`](../userland/System__Library__PrivateFrameworks__BatteryIntelligence.framework__BatteryIntelligence.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 8 instance variables, 8 properties, 19 instance methods, 1 class methods

## Instance variables

```
B _isFirstEstimate;
B _isEstimateOverridden;
d _estimate;
q _socAtEstimateTime;
q _endSOC;
d _confidenceScore;
q _additionalInformation;
@"NSString" _formattedEstimate;
```

## Properties

```
@property (Td,N,V_estimate) estimate;
@property (Tq,N,V_socAtEstimateTime) socAtEstimateTime;
@property (Tq,N,V_endSOC) endSOC;
@property (Td,N,V_confidenceScore) confidenceScore;
@property (Tq,N,V_additionalInformation) additionalInformation;
@property (T@"NSString",&,N,V_formattedEstimate) formattedEstimate;
@property (TB,N,V_isFirstEstimate) isFirstEstimate;
@property (TB,N,V_isEstimateOverridden) isEstimateOverridden;
```

## Class methods

```
+[BIBatteryAnalysisOutput supportsSecureCoding];
```

## Instance methods

```
-[BIBatteryAnalysisOutput setConfidenceScore:];
-[BIBatteryAnalysisOutput estimate];
-[BIBatteryAnalysisOutput formattedEstimate];
-[BIBatteryAnalysisOutput confidenceScore];
-[BIBatteryAnalysisOutput endSOC];
-[BIBatteryAnalysisOutput setFormattedEstimate:];
-[BIBatteryAnalysisOutput socAtEstimateTime];
-[BIBatteryAnalysisOutput isEstimateOverridden];
-[BIBatteryAnalysisOutput setIsFirstEstimate:];
-[BIBatteryAnalysisOutput encodeWithCoder:];
-[BIBatteryAnalysisOutput setAdditionalInformation:];
-[BIBatteryAnalysisOutput description];
-[BIBatteryAnalysisOutput initWithCoder:];
-[BIBatteryAnalysisOutput setIsEstimateOverridden:];
-[BIBatteryAnalysisOutput additionalInformation];
-[BIBatteryAnalysisOutput isFirstEstimate];
-[BIBatteryAnalysisOutput setEndSOC:];
-[BIBatteryAnalysisOutput setEstimate:];
-[BIBatteryAnalysisOutput setSocAtEstimateTime:];
```
