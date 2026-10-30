# `AWDMETRICSKCellularPowerLogProtocolStateHist`

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
+[AWDMETRICSKCellularPowerLogProtocolStateHist binType];
```

## Instance methods

```
-[AWDMETRICSKCellularPowerLogProtocolStateHist hasTimestamp];
-[AWDMETRICSKCellularPowerLogProtocolStateHist setHasTimestamp:];
-[AWDMETRICSKCellularPowerLogProtocolStateHist setTimestamp:];
-[AWDMETRICSKCellularPowerLogProtocolStateHist writeTo:];
-[AWDMETRICSKCellularPowerLogProtocolStateHist mergeFrom:];
-[AWDMETRICSKCellularPowerLogProtocolStateHist timestamp];
-[AWDMETRICSKCellularPowerLogProtocolStateHist hash];
-[AWDMETRICSKCellularPowerLogProtocolStateHist copyTo:];
-[AWDMETRICSKCellularPowerLogProtocolStateHist description];
-[AWDMETRICSKCellularPowerLogProtocolStateHist readFrom:];
-[AWDMETRICSKCellularPowerLogProtocolStateHist copyWithZone:];
-[AWDMETRICSKCellularPowerLogProtocolStateHist isEqual:];
-[AWDMETRICSKCellularPowerLogProtocolStateHist dictionaryRepresentation];
-[AWDMETRICSKCellularPowerLogProtocolStateHist durationMs];
-[AWDMETRICSKCellularPowerLogProtocolStateHist hasDurationMs];
-[AWDMETRICSKCellularPowerLogProtocolStateHist setDurationMs:];
-[AWDMETRICSKCellularPowerLogProtocolStateHist setHasDurationMs:];
-[AWDMETRICSKCellularPowerLogProtocolStateHist bins];
-[AWDMETRICSKCellularPowerLogProtocolStateHist setBins:];
-[AWDMETRICSKCellularPowerLogProtocolStateHist isDataPreferred];
-[AWDMETRICSKCellularPowerLogProtocolStateHist StringAsLastSdmState:];
-[AWDMETRICSKCellularPowerLogProtocolStateHist addBin:];
-[AWDMETRICSKCellularPowerLogProtocolStateHist hasLastSdmState];
-[AWDMETRICSKCellularPowerLogProtocolStateHist binAtIndex:];
-[AWDMETRICSKCellularPowerLogProtocolStateHist binsCount];
-[AWDMETRICSKCellularPowerLogProtocolStateHist clearBins];
-[AWDMETRICSKCellularPowerLogProtocolStateHist hasIsDataPreferred];
-[AWDMETRICSKCellularPowerLogProtocolStateHist hasSubsId];
-[AWDMETRICSKCellularPowerLogProtocolStateHist lastSdmState];
-[AWDMETRICSKCellularPowerLogProtocolStateHist lastSdmStateAsString:];
-[AWDMETRICSKCellularPowerLogProtocolStateHist setHasIsDataPreferred:];
-[AWDMETRICSKCellularPowerLogProtocolStateHist setHasLastSdmState:];
-[AWDMETRICSKCellularPowerLogProtocolStateHist setHasSubsId:];
-[AWDMETRICSKCellularPowerLogProtocolStateHist setIsDataPreferred:];
-[AWDMETRICSKCellularPowerLogProtocolStateHist setLastSdmState:];
-[AWDMETRICSKCellularPowerLogProtocolStateHist setSubsId:];
-[AWDMETRICSKCellularPowerLogProtocolStateHist subsId];
```
