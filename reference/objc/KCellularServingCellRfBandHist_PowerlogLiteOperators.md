# `KCellularServingCellRfBandHist`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 5 instance variables, 7 properties, 27 instance methods, 1 class methods

## Instance variables

```
Q _timestamp;
I _durationMs;
@"NSMutableArray" _pcellBandDurations;
I _subsId;
{?="timestamp"b1"durationMs"b1"subsId"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasDurationMs;
@property (TI,N,V_durationMs) durationMs;
@property (T@"NSMutableArray",&,N,V_pcellBandDurations) pcellBandDurations;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
```

## Class methods

```
+[KCellularServingCellRfBandHist pcellBandDurationType];
```

## Instance methods

```
-[KCellularServingCellRfBandHist hasTimestamp];
-[KCellularServingCellRfBandHist setHasTimestamp:];
-[KCellularServingCellRfBandHist setTimestamp:];
-[KCellularServingCellRfBandHist writeTo:];
-[KCellularServingCellRfBandHist mergeFrom:];
-[KCellularServingCellRfBandHist timestamp];
-[KCellularServingCellRfBandHist hash];
-[KCellularServingCellRfBandHist copyTo:];
-[KCellularServingCellRfBandHist description];
-[KCellularServingCellRfBandHist readFrom:];
-[KCellularServingCellRfBandHist copyWithZone:];
-[KCellularServingCellRfBandHist isEqual:];
-[KCellularServingCellRfBandHist dictionaryRepresentation];
-[KCellularServingCellRfBandHist durationMs];
-[KCellularServingCellRfBandHist hasDurationMs];
-[KCellularServingCellRfBandHist setDurationMs:];
-[KCellularServingCellRfBandHist setHasDurationMs:];
-[KCellularServingCellRfBandHist hasSubsId];
-[KCellularServingCellRfBandHist setHasSubsId:];
-[KCellularServingCellRfBandHist setSubsId:];
-[KCellularServingCellRfBandHist subsId];
-[KCellularServingCellRfBandHist addPcellBandDuration:];
-[KCellularServingCellRfBandHist clearPcellBandDurations];
-[KCellularServingCellRfBandHist pcellBandDurationAtIndex:];
-[KCellularServingCellRfBandHist pcellBandDurations];
-[KCellularServingCellRfBandHist pcellBandDurationsCount];
-[KCellularServingCellRfBandHist setPcellBandDurations:];
```
