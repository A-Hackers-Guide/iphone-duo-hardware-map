# `AWDMETRICSKCellularPowerLogAggregatedDLTBSHist`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 7 instance variables, 11 properties, 35 instance methods, 1 class methods

## Instance variables

```
Q _timestamp;
@"NSMutableArray" _bins;
I _durationMs;
I _numSubs;
I _subsId;
B _isDataPreferred;
{?="timestamp"b1"durationMs"b1"numSubs"b1"subsId"b1"isDataPreferred"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (T@"NSMutableArray",&,N,V_bins) bins;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
@property (TB,N) hasDurationMs;
@property (TI,N,V_durationMs) durationMs;
@property (TB,N) hasNumSubs;
@property (TI,N,V_numSubs) numSubs;
@property (TB,N) hasIsDataPreferred;
@property (TB,N,V_isDataPreferred) isDataPreferred;
```

## Class methods

```
+[AWDMETRICSKCellularPowerLogAggregatedDLTBSHist binType];
```

## Instance methods

```
-[AWDMETRICSKCellularPowerLogAggregatedDLTBSHist hasTimestamp];
-[AWDMETRICSKCellularPowerLogAggregatedDLTBSHist setHasTimestamp:];
-[AWDMETRICSKCellularPowerLogAggregatedDLTBSHist setTimestamp:];
-[AWDMETRICSKCellularPowerLogAggregatedDLTBSHist writeTo:];
-[AWDMETRICSKCellularPowerLogAggregatedDLTBSHist mergeFrom:];
-[AWDMETRICSKCellularPowerLogAggregatedDLTBSHist timestamp];
-[AWDMETRICSKCellularPowerLogAggregatedDLTBSHist hash];
-[AWDMETRICSKCellularPowerLogAggregatedDLTBSHist copyTo:];
-[AWDMETRICSKCellularPowerLogAggregatedDLTBSHist description];
-[AWDMETRICSKCellularPowerLogAggregatedDLTBSHist readFrom:];
-[AWDMETRICSKCellularPowerLogAggregatedDLTBSHist copyWithZone:];
-[AWDMETRICSKCellularPowerLogAggregatedDLTBSHist isEqual:];
-[AWDMETRICSKCellularPowerLogAggregatedDLTBSHist dictionaryRepresentation];
-[AWDMETRICSKCellularPowerLogAggregatedDLTBSHist durationMs];
-[AWDMETRICSKCellularPowerLogAggregatedDLTBSHist hasDurationMs];
-[AWDMETRICSKCellularPowerLogAggregatedDLTBSHist setDurationMs:];
-[AWDMETRICSKCellularPowerLogAggregatedDLTBSHist setHasDurationMs:];
-[AWDMETRICSKCellularPowerLogAggregatedDLTBSHist bins];
-[AWDMETRICSKCellularPowerLogAggregatedDLTBSHist setBins:];
-[AWDMETRICSKCellularPowerLogAggregatedDLTBSHist isDataPreferred];
-[AWDMETRICSKCellularPowerLogAggregatedDLTBSHist numSubs];
-[AWDMETRICSKCellularPowerLogAggregatedDLTBSHist addBin:];
-[AWDMETRICSKCellularPowerLogAggregatedDLTBSHist binAtIndex:];
-[AWDMETRICSKCellularPowerLogAggregatedDLTBSHist binsCount];
-[AWDMETRICSKCellularPowerLogAggregatedDLTBSHist clearBins];
-[AWDMETRICSKCellularPowerLogAggregatedDLTBSHist hasIsDataPreferred];
-[AWDMETRICSKCellularPowerLogAggregatedDLTBSHist hasNumSubs];
-[AWDMETRICSKCellularPowerLogAggregatedDLTBSHist hasSubsId];
-[AWDMETRICSKCellularPowerLogAggregatedDLTBSHist setHasIsDataPreferred:];
-[AWDMETRICSKCellularPowerLogAggregatedDLTBSHist setHasNumSubs:];
-[AWDMETRICSKCellularPowerLogAggregatedDLTBSHist setHasSubsId:];
-[AWDMETRICSKCellularPowerLogAggregatedDLTBSHist setIsDataPreferred:];
-[AWDMETRICSKCellularPowerLogAggregatedDLTBSHist setNumSubs:];
-[AWDMETRICSKCellularPowerLogAggregatedDLTBSHist setSubsId:];
-[AWDMETRICSKCellularPowerLogAggregatedDLTBSHist subsId];
```
