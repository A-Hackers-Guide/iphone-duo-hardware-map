# `AWDMETRICSKCellularPowerLogDcsPerfStates`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 5 instance variables, 7 properties, 29 instance methods, 1 class methods

## Instance variables

```
Q _durationMs;
Q _timestamp;
@"NSMutableArray" _bins;
i _lastSdmState;
{?="durationMs"b1"timestamp"b1"lastSdmState"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (T@"NSMutableArray",&,N,V_bins) bins;
@property (TB,N) hasDurationMs;
@property (TQ,N,V_durationMs) durationMs;
@property (TB,N) hasLastSdmState;
@property (Ti,N,V_lastSdmState) lastSdmState;
```

## Class methods

```
+[AWDMETRICSKCellularPowerLogDcsPerfStates binType];
```

## Instance methods

```
-[AWDMETRICSKCellularPowerLogDcsPerfStates hasTimestamp];
-[AWDMETRICSKCellularPowerLogDcsPerfStates setHasTimestamp:];
-[AWDMETRICSKCellularPowerLogDcsPerfStates setTimestamp:];
-[AWDMETRICSKCellularPowerLogDcsPerfStates writeTo:];
-[AWDMETRICSKCellularPowerLogDcsPerfStates mergeFrom:];
-[AWDMETRICSKCellularPowerLogDcsPerfStates timestamp];
-[AWDMETRICSKCellularPowerLogDcsPerfStates hash];
-[AWDMETRICSKCellularPowerLogDcsPerfStates copyTo:];
-[AWDMETRICSKCellularPowerLogDcsPerfStates description];
-[AWDMETRICSKCellularPowerLogDcsPerfStates readFrom:];
-[AWDMETRICSKCellularPowerLogDcsPerfStates copyWithZone:];
-[AWDMETRICSKCellularPowerLogDcsPerfStates isEqual:];
-[AWDMETRICSKCellularPowerLogDcsPerfStates dictionaryRepresentation];
-[AWDMETRICSKCellularPowerLogDcsPerfStates durationMs];
-[AWDMETRICSKCellularPowerLogDcsPerfStates hasDurationMs];
-[AWDMETRICSKCellularPowerLogDcsPerfStates setDurationMs:];
-[AWDMETRICSKCellularPowerLogDcsPerfStates setHasDurationMs:];
-[AWDMETRICSKCellularPowerLogDcsPerfStates bins];
-[AWDMETRICSKCellularPowerLogDcsPerfStates setBins:];
-[AWDMETRICSKCellularPowerLogDcsPerfStates StringAsLastSdmState:];
-[AWDMETRICSKCellularPowerLogDcsPerfStates addBin:];
-[AWDMETRICSKCellularPowerLogDcsPerfStates hasLastSdmState];
-[AWDMETRICSKCellularPowerLogDcsPerfStates binAtIndex:];
-[AWDMETRICSKCellularPowerLogDcsPerfStates binsCount];
-[AWDMETRICSKCellularPowerLogDcsPerfStates clearBins];
-[AWDMETRICSKCellularPowerLogDcsPerfStates lastSdmState];
-[AWDMETRICSKCellularPowerLogDcsPerfStates lastSdmStateAsString:];
-[AWDMETRICSKCellularPowerLogDcsPerfStates setHasLastSdmState:];
-[AWDMETRICSKCellularPowerLogDcsPerfStates setLastSdmState:];
```
