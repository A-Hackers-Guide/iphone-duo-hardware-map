# `AWDMETRICSKCellularPowerLogNRBWPHist`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 6 instance variables, 9 properties, 31 instance methods, 1 class methods

## Instance variables

```
Q _timestamp;
@"NSMutableArray" _bins;
I _durationMs;
I _subsId;
B _isDataPreferred;
{?="timestamp"b1"durationMs"b1"subsId"b1"isDataPreferred"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
@property (TB,N) hasDurationMs;
@property (TI,N,V_durationMs) durationMs;
@property (T@"NSMutableArray",&,N,V_bins) bins;
@property (TB,N) hasIsDataPreferred;
@property (TB,N,V_isDataPreferred) isDataPreferred;
```

## Class methods

```
+[AWDMETRICSKCellularPowerLogNRBWPHist binType];
```

## Instance methods

```
-[AWDMETRICSKCellularPowerLogNRBWPHist hasTimestamp];
-[AWDMETRICSKCellularPowerLogNRBWPHist setHasTimestamp:];
-[AWDMETRICSKCellularPowerLogNRBWPHist setTimestamp:];
-[AWDMETRICSKCellularPowerLogNRBWPHist writeTo:];
-[AWDMETRICSKCellularPowerLogNRBWPHist mergeFrom:];
-[AWDMETRICSKCellularPowerLogNRBWPHist timestamp];
-[AWDMETRICSKCellularPowerLogNRBWPHist hash];
-[AWDMETRICSKCellularPowerLogNRBWPHist copyTo:];
-[AWDMETRICSKCellularPowerLogNRBWPHist description];
-[AWDMETRICSKCellularPowerLogNRBWPHist readFrom:];
-[AWDMETRICSKCellularPowerLogNRBWPHist copyWithZone:];
-[AWDMETRICSKCellularPowerLogNRBWPHist isEqual:];
-[AWDMETRICSKCellularPowerLogNRBWPHist dictionaryRepresentation];
-[AWDMETRICSKCellularPowerLogNRBWPHist durationMs];
-[AWDMETRICSKCellularPowerLogNRBWPHist hasDurationMs];
-[AWDMETRICSKCellularPowerLogNRBWPHist setDurationMs:];
-[AWDMETRICSKCellularPowerLogNRBWPHist setHasDurationMs:];
-[AWDMETRICSKCellularPowerLogNRBWPHist bins];
-[AWDMETRICSKCellularPowerLogNRBWPHist setBins:];
-[AWDMETRICSKCellularPowerLogNRBWPHist isDataPreferred];
-[AWDMETRICSKCellularPowerLogNRBWPHist addBin:];
-[AWDMETRICSKCellularPowerLogNRBWPHist binAtIndex:];
-[AWDMETRICSKCellularPowerLogNRBWPHist binsCount];
-[AWDMETRICSKCellularPowerLogNRBWPHist clearBins];
-[AWDMETRICSKCellularPowerLogNRBWPHist hasIsDataPreferred];
-[AWDMETRICSKCellularPowerLogNRBWPHist hasSubsId];
-[AWDMETRICSKCellularPowerLogNRBWPHist setHasIsDataPreferred:];
-[AWDMETRICSKCellularPowerLogNRBWPHist setHasSubsId:];
-[AWDMETRICSKCellularPowerLogNRBWPHist setIsDataPreferred:];
-[AWDMETRICSKCellularPowerLogNRBWPHist setSubsId:];
-[AWDMETRICSKCellularPowerLogNRBWPHist subsId];
```
