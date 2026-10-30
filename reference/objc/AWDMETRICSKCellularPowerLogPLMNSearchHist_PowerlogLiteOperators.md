# `AWDMETRICSKCellularPowerLogPLMNSearchHist`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 7 instance variables, 11 properties, 37 instance methods, 1 class methods

## Instance variables

```
Q _timestamp;
@"NSMutableArray" _bins;
I _durationMs;
i _lastSdmState;
I _subsId;
B _isDataPreferred;
{?="timestamp"b1"durationMs"b1"lastSdmState"b1"subsId"b1"isDataPreferred"b1} _has;
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
@property (TB,N) hasIsDataPreferred;
@property (TB,N,V_isDataPreferred) isDataPreferred;
@property (TB,N) hasLastSdmState;
@property (Ti,N,V_lastSdmState) lastSdmState;
```

## Class methods

```
+[AWDMETRICSKCellularPowerLogPLMNSearchHist binType];
```

## Instance methods

```
-[AWDMETRICSKCellularPowerLogPLMNSearchHist hasTimestamp];
-[AWDMETRICSKCellularPowerLogPLMNSearchHist setHasTimestamp:];
-[AWDMETRICSKCellularPowerLogPLMNSearchHist setTimestamp:];
-[AWDMETRICSKCellularPowerLogPLMNSearchHist writeTo:];
-[AWDMETRICSKCellularPowerLogPLMNSearchHist mergeFrom:];
-[AWDMETRICSKCellularPowerLogPLMNSearchHist timestamp];
-[AWDMETRICSKCellularPowerLogPLMNSearchHist hash];
-[AWDMETRICSKCellularPowerLogPLMNSearchHist copyTo:];
-[AWDMETRICSKCellularPowerLogPLMNSearchHist description];
-[AWDMETRICSKCellularPowerLogPLMNSearchHist readFrom:];
-[AWDMETRICSKCellularPowerLogPLMNSearchHist copyWithZone:];
-[AWDMETRICSKCellularPowerLogPLMNSearchHist isEqual:];
-[AWDMETRICSKCellularPowerLogPLMNSearchHist dictionaryRepresentation];
-[AWDMETRICSKCellularPowerLogPLMNSearchHist durationMs];
-[AWDMETRICSKCellularPowerLogPLMNSearchHist hasDurationMs];
-[AWDMETRICSKCellularPowerLogPLMNSearchHist setDurationMs:];
-[AWDMETRICSKCellularPowerLogPLMNSearchHist setHasDurationMs:];
-[AWDMETRICSKCellularPowerLogPLMNSearchHist bins];
-[AWDMETRICSKCellularPowerLogPLMNSearchHist setBins:];
-[AWDMETRICSKCellularPowerLogPLMNSearchHist isDataPreferred];
-[AWDMETRICSKCellularPowerLogPLMNSearchHist StringAsLastSdmState:];
-[AWDMETRICSKCellularPowerLogPLMNSearchHist addBin:];
-[AWDMETRICSKCellularPowerLogPLMNSearchHist hasLastSdmState];
-[AWDMETRICSKCellularPowerLogPLMNSearchHist binAtIndex:];
-[AWDMETRICSKCellularPowerLogPLMNSearchHist binsCount];
-[AWDMETRICSKCellularPowerLogPLMNSearchHist clearBins];
-[AWDMETRICSKCellularPowerLogPLMNSearchHist hasIsDataPreferred];
-[AWDMETRICSKCellularPowerLogPLMNSearchHist hasSubsId];
-[AWDMETRICSKCellularPowerLogPLMNSearchHist lastSdmState];
-[AWDMETRICSKCellularPowerLogPLMNSearchHist lastSdmStateAsString:];
-[AWDMETRICSKCellularPowerLogPLMNSearchHist setHasIsDataPreferred:];
-[AWDMETRICSKCellularPowerLogPLMNSearchHist setHasLastSdmState:];
-[AWDMETRICSKCellularPowerLogPLMNSearchHist setHasSubsId:];
-[AWDMETRICSKCellularPowerLogPLMNSearchHist setIsDataPreferred:];
-[AWDMETRICSKCellularPowerLogPLMNSearchHist setLastSdmState:];
-[AWDMETRICSKCellularPowerLogPLMNSearchHist setSubsId:];
-[AWDMETRICSKCellularPowerLogPLMNSearchHist subsId];
```
