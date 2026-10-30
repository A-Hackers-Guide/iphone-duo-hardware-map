# `AWDMETRICSKCellularPowerLogGSMRABMode`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 8 instance variables, 13 properties, 38 instance methods, 1 class methods

## Instance variables

```
Q _timestamp;
@"NSMutableArray" _bins;
I _durationMs;
I _numSubs;
@"NSData" _plmn;
I _subsId;
B _isDataPreferred;
{?="timestamp"b1"durationMs"b1"numSubs"b1"subsId"b1"isDataPreferred"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (T@"NSMutableArray",&,N,V_bins) bins;
@property (TB,N) hasDurationMs;
@property (TI,N,V_durationMs) durationMs;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
@property (TB,N) hasNumSubs;
@property (TI,N,V_numSubs) numSubs;
@property (TB,N) hasIsDataPreferred;
@property (TB,N,V_isDataPreferred) isDataPreferred;
@property (TB,R,N) hasPlmn;
@property (T@"NSData",&,N,V_plmn) plmn;
```

## Class methods

```
+[AWDMETRICSKCellularPowerLogGSMRABMode binType];
```

## Instance methods

```
-[AWDMETRICSKCellularPowerLogGSMRABMode hasTimestamp];
-[AWDMETRICSKCellularPowerLogGSMRABMode setHasTimestamp:];
-[AWDMETRICSKCellularPowerLogGSMRABMode setTimestamp:];
-[AWDMETRICSKCellularPowerLogGSMRABMode writeTo:];
-[AWDMETRICSKCellularPowerLogGSMRABMode mergeFrom:];
-[AWDMETRICSKCellularPowerLogGSMRABMode timestamp];
-[AWDMETRICSKCellularPowerLogGSMRABMode setPlmn:];
-[AWDMETRICSKCellularPowerLogGSMRABMode hash];
-[AWDMETRICSKCellularPowerLogGSMRABMode copyTo:];
-[AWDMETRICSKCellularPowerLogGSMRABMode description];
-[AWDMETRICSKCellularPowerLogGSMRABMode readFrom:];
-[AWDMETRICSKCellularPowerLogGSMRABMode copyWithZone:];
-[AWDMETRICSKCellularPowerLogGSMRABMode isEqual:];
-[AWDMETRICSKCellularPowerLogGSMRABMode plmn];
-[AWDMETRICSKCellularPowerLogGSMRABMode dictionaryRepresentation];
-[AWDMETRICSKCellularPowerLogGSMRABMode durationMs];
-[AWDMETRICSKCellularPowerLogGSMRABMode hasDurationMs];
-[AWDMETRICSKCellularPowerLogGSMRABMode setDurationMs:];
-[AWDMETRICSKCellularPowerLogGSMRABMode setHasDurationMs:];
-[AWDMETRICSKCellularPowerLogGSMRABMode bins];
-[AWDMETRICSKCellularPowerLogGSMRABMode setBins:];
-[AWDMETRICSKCellularPowerLogGSMRABMode hasPlmn];
-[AWDMETRICSKCellularPowerLogGSMRABMode isDataPreferred];
-[AWDMETRICSKCellularPowerLogGSMRABMode numSubs];
-[AWDMETRICSKCellularPowerLogGSMRABMode addBin:];
-[AWDMETRICSKCellularPowerLogGSMRABMode binAtIndex:];
-[AWDMETRICSKCellularPowerLogGSMRABMode binsCount];
-[AWDMETRICSKCellularPowerLogGSMRABMode clearBins];
-[AWDMETRICSKCellularPowerLogGSMRABMode hasIsDataPreferred];
-[AWDMETRICSKCellularPowerLogGSMRABMode hasNumSubs];
-[AWDMETRICSKCellularPowerLogGSMRABMode hasSubsId];
-[AWDMETRICSKCellularPowerLogGSMRABMode setHasIsDataPreferred:];
-[AWDMETRICSKCellularPowerLogGSMRABMode setHasNumSubs:];
-[AWDMETRICSKCellularPowerLogGSMRABMode setHasSubsId:];
-[AWDMETRICSKCellularPowerLogGSMRABMode setIsDataPreferred:];
-[AWDMETRICSKCellularPowerLogGSMRABMode setNumSubs:];
-[AWDMETRICSKCellularPowerLogGSMRABMode setSubsId:];
-[AWDMETRICSKCellularPowerLogGSMRABMode subsId];
```
