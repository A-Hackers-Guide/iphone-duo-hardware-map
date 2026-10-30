# `AWDMETRICSKCellularPowerLogSFTRxTxHist`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 5 instance variables, 7 properties, 27 instance methods, 1 class methods

## Instance variables

```
Q _timestamp;
@"NSMutableArray" _bins;
I _durationMs;
I _subsId;
{?="timestamp"b1"durationMs"b1"subsId"b1} _has;
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
```

## Class methods

```
+[AWDMETRICSKCellularPowerLogSFTRxTxHist binType];
```

## Instance methods

```
-[AWDMETRICSKCellularPowerLogSFTRxTxHist hasTimestamp];
-[AWDMETRICSKCellularPowerLogSFTRxTxHist setHasTimestamp:];
-[AWDMETRICSKCellularPowerLogSFTRxTxHist setTimestamp:];
-[AWDMETRICSKCellularPowerLogSFTRxTxHist writeTo:];
-[AWDMETRICSKCellularPowerLogSFTRxTxHist mergeFrom:];
-[AWDMETRICSKCellularPowerLogSFTRxTxHist timestamp];
-[AWDMETRICSKCellularPowerLogSFTRxTxHist hash];
-[AWDMETRICSKCellularPowerLogSFTRxTxHist copyTo:];
-[AWDMETRICSKCellularPowerLogSFTRxTxHist description];
-[AWDMETRICSKCellularPowerLogSFTRxTxHist readFrom:];
-[AWDMETRICSKCellularPowerLogSFTRxTxHist copyWithZone:];
-[AWDMETRICSKCellularPowerLogSFTRxTxHist isEqual:];
-[AWDMETRICSKCellularPowerLogSFTRxTxHist dictionaryRepresentation];
-[AWDMETRICSKCellularPowerLogSFTRxTxHist durationMs];
-[AWDMETRICSKCellularPowerLogSFTRxTxHist hasDurationMs];
-[AWDMETRICSKCellularPowerLogSFTRxTxHist setDurationMs:];
-[AWDMETRICSKCellularPowerLogSFTRxTxHist setHasDurationMs:];
-[AWDMETRICSKCellularPowerLogSFTRxTxHist bins];
-[AWDMETRICSKCellularPowerLogSFTRxTxHist setBins:];
-[AWDMETRICSKCellularPowerLogSFTRxTxHist addBin:];
-[AWDMETRICSKCellularPowerLogSFTRxTxHist binAtIndex:];
-[AWDMETRICSKCellularPowerLogSFTRxTxHist binsCount];
-[AWDMETRICSKCellularPowerLogSFTRxTxHist clearBins];
-[AWDMETRICSKCellularPowerLogSFTRxTxHist hasSubsId];
-[AWDMETRICSKCellularPowerLogSFTRxTxHist setHasSubsId:];
-[AWDMETRICSKCellularPowerLogSFTRxTxHist setSubsId:];
-[AWDMETRICSKCellularPowerLogSFTRxTxHist subsId];
```
