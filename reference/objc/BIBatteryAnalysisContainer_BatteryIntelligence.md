# `BIBatteryAnalysisContainer`

- Image: [`/System/Library/PrivateFrameworks/BatteryIntelligence.framework/BatteryIntelligence`](../userland/System__Library__PrivateFrameworks__BatteryIntelligence.framework__BatteryIntelligence.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"BIBatteryAnalysisOutput" _estimateObj;
q _lastUpdatedMonotonicTime;
@"NSError" _error;
```

## Properties

```
@property (T@"BIBatteryAnalysisOutput",&,N,V_estimateObj) estimateObj;
@property (Tq,N,V_lastUpdatedMonotonicTime) lastUpdatedMonotonicTime;
@property (T@"NSError",&,N,V_error) error;
```

## Class methods

```
+[BIBatteryAnalysisContainer supportsSecureCoding];
```

## Instance methods

```
-[BIBatteryAnalysisContainer setError:];
-[BIBatteryAnalysisContainer setLastUpdatedMonotonicTime:];
-[BIBatteryAnalysisContainer setEstimateObj:];
-[BIBatteryAnalysisContainer lastUpdatedMonotonicTime];
-[BIBatteryAnalysisContainer error];
-[BIBatteryAnalysisContainer encodeWithCoder:];
-[BIBatteryAnalysisContainer description];
-[BIBatteryAnalysisContainer initWithCoder:];
-[BIBatteryAnalysisContainer estimateObj];
```
