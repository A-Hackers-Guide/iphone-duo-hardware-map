# `AWDMETRICSKCellularPowerLogLteNrTxPowerHist`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 5 instance variables, 7 properties, 27 instance methods, 1 class methods

## Instance variables

```
Q _timestamp;
I _durationMs;
@"NSMutableArray" _hists;
I _subsId;
{?="timestamp"b1"durationMs"b1"subsId"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
@property (TB,N) hasDurationMs;
@property (TI,N,V_durationMs) durationMs;
@property (T@"NSMutableArray",&,N,V_hists) hists;
```

## Class methods

```
+[AWDMETRICSKCellularPowerLogLteNrTxPowerHist histType];
```

## Instance methods

```
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHist hasTimestamp];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHist setHasTimestamp:];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHist setTimestamp:];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHist writeTo:];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHist mergeFrom:];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHist timestamp];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHist hash];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHist copyTo:];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHist description];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHist readFrom:];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHist copyWithZone:];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHist isEqual:];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHist dictionaryRepresentation];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHist durationMs];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHist hasDurationMs];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHist setDurationMs:];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHist setHasDurationMs:];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHist addHist:];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHist clearHists];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHist hasSubsId];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHist histAtIndex:];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHist hists];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHist histsCount];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHist setHasSubsId:];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHist setHists:];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHist setSubsId:];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHist subsId];
```
