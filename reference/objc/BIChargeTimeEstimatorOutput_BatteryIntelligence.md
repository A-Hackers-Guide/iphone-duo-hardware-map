# `BIChargeTimeEstimatorOutput`

- Image: [`/System/Library/PrivateFrameworks/BatteryIntelligence.framework/BatteryIntelligence`](../userland/System__Library__PrivateFrameworks__BatteryIntelligence.framework__BatteryIntelligence.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 4 properties, 11 instance methods, 1 class methods

## Instance variables

```
d _estimate;
q _endSOC;
d _confidenceScore;
q _additionalInformation;
```

## Properties

```
@property (Td,N,V_estimate) estimate;
@property (Tq,N,V_endSOC) endSOC;
@property (Td,N,V_confidenceScore) confidenceScore;
@property (Tq,N,V_additionalInformation) additionalInformation;
```

## Class methods

```
+[BIChargeTimeEstimatorOutput supportsSecureCoding];
```

## Instance methods

```
-[BIChargeTimeEstimatorOutput setConfidenceScore:];
-[BIChargeTimeEstimatorOutput estimate];
-[BIChargeTimeEstimatorOutput confidenceScore];
-[BIChargeTimeEstimatorOutput endSOC];
-[BIChargeTimeEstimatorOutput encodeWithCoder:];
-[BIChargeTimeEstimatorOutput setAdditionalInformation:];
-[BIChargeTimeEstimatorOutput description];
-[BIChargeTimeEstimatorOutput initWithCoder:];
-[BIChargeTimeEstimatorOutput additionalInformation];
-[BIChargeTimeEstimatorOutput setEndSOC:];
-[BIChargeTimeEstimatorOutput setEstimate:];
```
