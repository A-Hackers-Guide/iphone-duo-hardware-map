# `AWDMETRICSKCellularPowerLogPowerEstimator`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 5 instance variables, 7 properties, 29 instance methods, 1 class methods

## Instance variables

```
Q _timestamp;
I _durationMs;
i _lastSdmState;
@"NSMutableArray" _powerStats;
{?="timestamp"b1"durationMs"b1"lastSdmState"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasDurationMs;
@property (TI,N,V_durationMs) durationMs;
@property (T@"NSMutableArray",&,N,V_powerStats) powerStats;
@property (TB,N) hasLastSdmState;
@property (Ti,N,V_lastSdmState) lastSdmState;
```

## Class methods

```
+[AWDMETRICSKCellularPowerLogPowerEstimator powerStatsType];
```

## Instance methods

```
-[AWDMETRICSKCellularPowerLogPowerEstimator hasTimestamp];
-[AWDMETRICSKCellularPowerLogPowerEstimator setHasTimestamp:];
-[AWDMETRICSKCellularPowerLogPowerEstimator setTimestamp:];
-[AWDMETRICSKCellularPowerLogPowerEstimator writeTo:];
-[AWDMETRICSKCellularPowerLogPowerEstimator mergeFrom:];
-[AWDMETRICSKCellularPowerLogPowerEstimator timestamp];
-[AWDMETRICSKCellularPowerLogPowerEstimator hash];
-[AWDMETRICSKCellularPowerLogPowerEstimator copyTo:];
-[AWDMETRICSKCellularPowerLogPowerEstimator description];
-[AWDMETRICSKCellularPowerLogPowerEstimator readFrom:];
-[AWDMETRICSKCellularPowerLogPowerEstimator copyWithZone:];
-[AWDMETRICSKCellularPowerLogPowerEstimator isEqual:];
-[AWDMETRICSKCellularPowerLogPowerEstimator dictionaryRepresentation];
-[AWDMETRICSKCellularPowerLogPowerEstimator durationMs];
-[AWDMETRICSKCellularPowerLogPowerEstimator hasDurationMs];
-[AWDMETRICSKCellularPowerLogPowerEstimator setDurationMs:];
-[AWDMETRICSKCellularPowerLogPowerEstimator setHasDurationMs:];
-[AWDMETRICSKCellularPowerLogPowerEstimator powerStatsCount];
-[AWDMETRICSKCellularPowerLogPowerEstimator StringAsLastSdmState:];
-[AWDMETRICSKCellularPowerLogPowerEstimator clearPowerStats];
-[AWDMETRICSKCellularPowerLogPowerEstimator hasLastSdmState];
-[AWDMETRICSKCellularPowerLogPowerEstimator addPowerStats:];
-[AWDMETRICSKCellularPowerLogPowerEstimator lastSdmState];
-[AWDMETRICSKCellularPowerLogPowerEstimator lastSdmStateAsString:];
-[AWDMETRICSKCellularPowerLogPowerEstimator powerStats];
-[AWDMETRICSKCellularPowerLogPowerEstimator powerStatsAtIndex:];
-[AWDMETRICSKCellularPowerLogPowerEstimator setHasLastSdmState:];
-[AWDMETRICSKCellularPowerLogPowerEstimator setLastSdmState:];
-[AWDMETRICSKCellularPowerLogPowerEstimator setPowerStats:];
```
