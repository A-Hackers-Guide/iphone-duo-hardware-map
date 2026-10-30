# `AWDMETRICSKCellularPowerLogSubsysSleepStates`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 6 instance variables, 9 properties, 33 instance methods, 1 class methods

## Instance variables

```
Q _durationMs;
Q _timestamp;
@"NSMutableArray" _bins;
i _lastSdmState;
I _subsId;
{?="durationMs"b1"timestamp"b1"lastSdmState"b1"subsId"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (T@"NSMutableArray",&,N,V_bins) bins;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
@property (TB,N) hasDurationMs;
@property (TQ,N,V_durationMs) durationMs;
@property (TB,N) hasLastSdmState;
@property (Ti,N,V_lastSdmState) lastSdmState;
```

## Class methods

```
+[AWDMETRICSKCellularPowerLogSubsysSleepStates binType];
```

## Instance methods

```
-[AWDMETRICSKCellularPowerLogSubsysSleepStates hasTimestamp];
-[AWDMETRICSKCellularPowerLogSubsysSleepStates setHasTimestamp:];
-[AWDMETRICSKCellularPowerLogSubsysSleepStates setTimestamp:];
-[AWDMETRICSKCellularPowerLogSubsysSleepStates writeTo:];
-[AWDMETRICSKCellularPowerLogSubsysSleepStates mergeFrom:];
-[AWDMETRICSKCellularPowerLogSubsysSleepStates timestamp];
-[AWDMETRICSKCellularPowerLogSubsysSleepStates hash];
-[AWDMETRICSKCellularPowerLogSubsysSleepStates copyTo:];
-[AWDMETRICSKCellularPowerLogSubsysSleepStates description];
-[AWDMETRICSKCellularPowerLogSubsysSleepStates readFrom:];
-[AWDMETRICSKCellularPowerLogSubsysSleepStates copyWithZone:];
-[AWDMETRICSKCellularPowerLogSubsysSleepStates isEqual:];
-[AWDMETRICSKCellularPowerLogSubsysSleepStates dictionaryRepresentation];
-[AWDMETRICSKCellularPowerLogSubsysSleepStates durationMs];
-[AWDMETRICSKCellularPowerLogSubsysSleepStates hasDurationMs];
-[AWDMETRICSKCellularPowerLogSubsysSleepStates setDurationMs:];
-[AWDMETRICSKCellularPowerLogSubsysSleepStates setHasDurationMs:];
-[AWDMETRICSKCellularPowerLogSubsysSleepStates bins];
-[AWDMETRICSKCellularPowerLogSubsysSleepStates setBins:];
-[AWDMETRICSKCellularPowerLogSubsysSleepStates StringAsLastSdmState:];
-[AWDMETRICSKCellularPowerLogSubsysSleepStates addBin:];
-[AWDMETRICSKCellularPowerLogSubsysSleepStates hasLastSdmState];
-[AWDMETRICSKCellularPowerLogSubsysSleepStates binAtIndex:];
-[AWDMETRICSKCellularPowerLogSubsysSleepStates binsCount];
-[AWDMETRICSKCellularPowerLogSubsysSleepStates clearBins];
-[AWDMETRICSKCellularPowerLogSubsysSleepStates hasSubsId];
-[AWDMETRICSKCellularPowerLogSubsysSleepStates lastSdmState];
-[AWDMETRICSKCellularPowerLogSubsysSleepStates lastSdmStateAsString:];
-[AWDMETRICSKCellularPowerLogSubsysSleepStates setHasLastSdmState:];
-[AWDMETRICSKCellularPowerLogSubsysSleepStates setHasSubsId:];
-[AWDMETRICSKCellularPowerLogSubsysSleepStates setLastSdmState:];
-[AWDMETRICSKCellularPowerLogSubsysSleepStates setSubsId:];
-[AWDMETRICSKCellularPowerLogSubsysSleepStates subsId];
```
