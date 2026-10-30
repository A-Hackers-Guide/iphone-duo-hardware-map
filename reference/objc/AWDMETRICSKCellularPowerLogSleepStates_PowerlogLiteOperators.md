# `AWDMETRICSKCellularPowerLogSleepStates`

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
@property (TB,N) hasDurationMs;
@property (TI,N,V_durationMs) durationMs;
@property (T@"NSMutableArray",&,N,V_bins) bins;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
@property (TB,N) hasIsDataPreferred;
@property (TB,N,V_isDataPreferred) isDataPreferred;
```

## Class methods

```
+[AWDMETRICSKCellularPowerLogSleepStates binType];
```

## Instance methods

```
-[AWDMETRICSKCellularPowerLogSleepStates hasTimestamp];
-[AWDMETRICSKCellularPowerLogSleepStates setHasTimestamp:];
-[AWDMETRICSKCellularPowerLogSleepStates setTimestamp:];
-[AWDMETRICSKCellularPowerLogSleepStates writeTo:];
-[AWDMETRICSKCellularPowerLogSleepStates mergeFrom:];
-[AWDMETRICSKCellularPowerLogSleepStates timestamp];
-[AWDMETRICSKCellularPowerLogSleepStates hash];
-[AWDMETRICSKCellularPowerLogSleepStates copyTo:];
-[AWDMETRICSKCellularPowerLogSleepStates description];
-[AWDMETRICSKCellularPowerLogSleepStates readFrom:];
-[AWDMETRICSKCellularPowerLogSleepStates copyWithZone:];
-[AWDMETRICSKCellularPowerLogSleepStates isEqual:];
-[AWDMETRICSKCellularPowerLogSleepStates dictionaryRepresentation];
-[AWDMETRICSKCellularPowerLogSleepStates durationMs];
-[AWDMETRICSKCellularPowerLogSleepStates hasDurationMs];
-[AWDMETRICSKCellularPowerLogSleepStates setDurationMs:];
-[AWDMETRICSKCellularPowerLogSleepStates setHasDurationMs:];
-[AWDMETRICSKCellularPowerLogSleepStates bins];
-[AWDMETRICSKCellularPowerLogSleepStates setBins:];
-[AWDMETRICSKCellularPowerLogSleepStates isDataPreferred];
-[AWDMETRICSKCellularPowerLogSleepStates addBin:];
-[AWDMETRICSKCellularPowerLogSleepStates binAtIndex:];
-[AWDMETRICSKCellularPowerLogSleepStates binsCount];
-[AWDMETRICSKCellularPowerLogSleepStates clearBins];
-[AWDMETRICSKCellularPowerLogSleepStates hasIsDataPreferred];
-[AWDMETRICSKCellularPowerLogSleepStates hasSubsId];
-[AWDMETRICSKCellularPowerLogSleepStates setHasIsDataPreferred:];
-[AWDMETRICSKCellularPowerLogSleepStates setHasSubsId:];
-[AWDMETRICSKCellularPowerLogSleepStates setIsDataPreferred:];
-[AWDMETRICSKCellularPowerLogSleepStates setSubsId:];
-[AWDMETRICSKCellularPowerLogSleepStates subsId];
```
