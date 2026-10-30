# `AWDMETRICSKCellularPowerLogLteNrRxDiversityHist`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 8 instance variables, 13 properties, 41 instance methods, 1 class methods

## Instance variables

```
Q _timestamp;
@"NSMutableArray" _cells;
I _durationMs;
i _lastSdmState;
I _numSubs;
I _subsId;
B _isDataPreferred;
{?="timestamp"b1"durationMs"b1"lastSdmState"b1"numSubs"b1"subsId"b1"isDataPreferred"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (T@"NSMutableArray",&,N,V_cells) cells;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
@property (TB,N) hasDurationMs;
@property (TI,N,V_durationMs) durationMs;
@property (TB,N) hasNumSubs;
@property (TI,N,V_numSubs) numSubs;
@property (TB,N) hasIsDataPreferred;
@property (TB,N,V_isDataPreferred) isDataPreferred;
@property (TB,N) hasLastSdmState;
@property (Ti,N,V_lastSdmState) lastSdmState;
```

## Class methods

```
+[AWDMETRICSKCellularPowerLogLteNrRxDiversityHist cellType];
```

## Instance methods

```
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHist hasTimestamp];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHist setHasTimestamp:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHist setTimestamp:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHist writeTo:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHist mergeFrom:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHist timestamp];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHist hash];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHist copyTo:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHist description];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHist readFrom:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHist copyWithZone:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHist isEqual:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHist dictionaryRepresentation];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHist cells];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHist durationMs];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHist hasDurationMs];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHist setDurationMs:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHist setHasDurationMs:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHist cellsCount];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHist clearCells];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHist setCells:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHist addCell:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHist cellAtIndex:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHist isDataPreferred];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHist numSubs];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHist StringAsLastSdmState:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHist hasLastSdmState];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHist hasIsDataPreferred];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHist hasNumSubs];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHist hasSubsId];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHist lastSdmState];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHist lastSdmStateAsString:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHist setHasIsDataPreferred:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHist setHasLastSdmState:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHist setHasNumSubs:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHist setHasSubsId:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHist setIsDataPreferred:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHist setLastSdmState:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHist setNumSubs:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHist setSubsId:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHist subsId];
```
