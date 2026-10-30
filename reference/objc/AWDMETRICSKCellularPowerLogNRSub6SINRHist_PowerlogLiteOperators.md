# `AWDMETRICSKCellularPowerLogNRSub6SINRHist`

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
@property (T@"NSMutableArray",&,N,V_bins) bins;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
@property (TB,N) hasDurationMs;
@property (TI,N,V_durationMs) durationMs;
@property (TB,N) hasIsDataPreferred;
@property (TB,N,V_isDataPreferred) isDataPreferred;
```

## Class methods

```
+[AWDMETRICSKCellularPowerLogNRSub6SINRHist binType];
```

## Instance methods

```
-[AWDMETRICSKCellularPowerLogNRSub6SINRHist hasTimestamp];
-[AWDMETRICSKCellularPowerLogNRSub6SINRHist setHasTimestamp:];
-[AWDMETRICSKCellularPowerLogNRSub6SINRHist setTimestamp:];
-[AWDMETRICSKCellularPowerLogNRSub6SINRHist writeTo:];
-[AWDMETRICSKCellularPowerLogNRSub6SINRHist mergeFrom:];
-[AWDMETRICSKCellularPowerLogNRSub6SINRHist timestamp];
-[AWDMETRICSKCellularPowerLogNRSub6SINRHist hash];
-[AWDMETRICSKCellularPowerLogNRSub6SINRHist copyTo:];
-[AWDMETRICSKCellularPowerLogNRSub6SINRHist description];
-[AWDMETRICSKCellularPowerLogNRSub6SINRHist readFrom:];
-[AWDMETRICSKCellularPowerLogNRSub6SINRHist copyWithZone:];
-[AWDMETRICSKCellularPowerLogNRSub6SINRHist isEqual:];
-[AWDMETRICSKCellularPowerLogNRSub6SINRHist dictionaryRepresentation];
-[AWDMETRICSKCellularPowerLogNRSub6SINRHist durationMs];
-[AWDMETRICSKCellularPowerLogNRSub6SINRHist hasDurationMs];
-[AWDMETRICSKCellularPowerLogNRSub6SINRHist setDurationMs:];
-[AWDMETRICSKCellularPowerLogNRSub6SINRHist setHasDurationMs:];
-[AWDMETRICSKCellularPowerLogNRSub6SINRHist bins];
-[AWDMETRICSKCellularPowerLogNRSub6SINRHist setBins:];
-[AWDMETRICSKCellularPowerLogNRSub6SINRHist isDataPreferred];
-[AWDMETRICSKCellularPowerLogNRSub6SINRHist addBin:];
-[AWDMETRICSKCellularPowerLogNRSub6SINRHist binAtIndex:];
-[AWDMETRICSKCellularPowerLogNRSub6SINRHist binsCount];
-[AWDMETRICSKCellularPowerLogNRSub6SINRHist clearBins];
-[AWDMETRICSKCellularPowerLogNRSub6SINRHist hasIsDataPreferred];
-[AWDMETRICSKCellularPowerLogNRSub6SINRHist hasSubsId];
-[AWDMETRICSKCellularPowerLogNRSub6SINRHist setHasIsDataPreferred:];
-[AWDMETRICSKCellularPowerLogNRSub6SINRHist setHasSubsId:];
-[AWDMETRICSKCellularPowerLogNRSub6SINRHist setIsDataPreferred:];
-[AWDMETRICSKCellularPowerLogNRSub6SINRHist setSubsId:];
-[AWDMETRICSKCellularPowerLogNRSub6SINRHist subsId];
```
