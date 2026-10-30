# `AWDMETRICSKCellularPowerLogNRSub6RSRPHist`

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
+[AWDMETRICSKCellularPowerLogNRSub6RSRPHist binType];
```

## Instance methods

```
-[AWDMETRICSKCellularPowerLogNRSub6RSRPHist hasTimestamp];
-[AWDMETRICSKCellularPowerLogNRSub6RSRPHist setHasTimestamp:];
-[AWDMETRICSKCellularPowerLogNRSub6RSRPHist setTimestamp:];
-[AWDMETRICSKCellularPowerLogNRSub6RSRPHist writeTo:];
-[AWDMETRICSKCellularPowerLogNRSub6RSRPHist mergeFrom:];
-[AWDMETRICSKCellularPowerLogNRSub6RSRPHist timestamp];
-[AWDMETRICSKCellularPowerLogNRSub6RSRPHist hash];
-[AWDMETRICSKCellularPowerLogNRSub6RSRPHist copyTo:];
-[AWDMETRICSKCellularPowerLogNRSub6RSRPHist description];
-[AWDMETRICSKCellularPowerLogNRSub6RSRPHist readFrom:];
-[AWDMETRICSKCellularPowerLogNRSub6RSRPHist copyWithZone:];
-[AWDMETRICSKCellularPowerLogNRSub6RSRPHist isEqual:];
-[AWDMETRICSKCellularPowerLogNRSub6RSRPHist dictionaryRepresentation];
-[AWDMETRICSKCellularPowerLogNRSub6RSRPHist durationMs];
-[AWDMETRICSKCellularPowerLogNRSub6RSRPHist hasDurationMs];
-[AWDMETRICSKCellularPowerLogNRSub6RSRPHist setDurationMs:];
-[AWDMETRICSKCellularPowerLogNRSub6RSRPHist setHasDurationMs:];
-[AWDMETRICSKCellularPowerLogNRSub6RSRPHist bins];
-[AWDMETRICSKCellularPowerLogNRSub6RSRPHist setBins:];
-[AWDMETRICSKCellularPowerLogNRSub6RSRPHist isDataPreferred];
-[AWDMETRICSKCellularPowerLogNRSub6RSRPHist addBin:];
-[AWDMETRICSKCellularPowerLogNRSub6RSRPHist binAtIndex:];
-[AWDMETRICSKCellularPowerLogNRSub6RSRPHist binsCount];
-[AWDMETRICSKCellularPowerLogNRSub6RSRPHist clearBins];
-[AWDMETRICSKCellularPowerLogNRSub6RSRPHist hasIsDataPreferred];
-[AWDMETRICSKCellularPowerLogNRSub6RSRPHist hasSubsId];
-[AWDMETRICSKCellularPowerLogNRSub6RSRPHist setHasIsDataPreferred:];
-[AWDMETRICSKCellularPowerLogNRSub6RSRPHist setHasSubsId:];
-[AWDMETRICSKCellularPowerLogNRSub6RSRPHist setIsDataPreferred:];
-[AWDMETRICSKCellularPowerLogNRSub6RSRPHist setSubsId:];
-[AWDMETRICSKCellularPowerLogNRSub6RSRPHist subsId];
```
