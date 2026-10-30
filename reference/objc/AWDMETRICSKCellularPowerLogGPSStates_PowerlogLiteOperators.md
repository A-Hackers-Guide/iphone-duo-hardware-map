# `AWDMETRICSKCellularPowerLogGPSStates`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 6 instance variables, 9 properties, 33 instance methods, 1 class methods

## Instance variables

```
Q _timestamp;
@"NSMutableArray" _bins;
I _durationMs;
i _lastSdmState;
I _subsId;
{?="timestamp"b1"durationMs"b1"lastSdmState"b1"subsId"b1} _has;
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
@property (TB,N) hasLastSdmState;
@property (Ti,N,V_lastSdmState) lastSdmState;
```

## Class methods

```
+[AWDMETRICSKCellularPowerLogGPSStates binType];
```

## Instance methods

```
-[AWDMETRICSKCellularPowerLogGPSStates hasTimestamp];
-[AWDMETRICSKCellularPowerLogGPSStates setHasTimestamp:];
-[AWDMETRICSKCellularPowerLogGPSStates setTimestamp:];
-[AWDMETRICSKCellularPowerLogGPSStates writeTo:];
-[AWDMETRICSKCellularPowerLogGPSStates mergeFrom:];
-[AWDMETRICSKCellularPowerLogGPSStates timestamp];
-[AWDMETRICSKCellularPowerLogGPSStates hash];
-[AWDMETRICSKCellularPowerLogGPSStates copyTo:];
-[AWDMETRICSKCellularPowerLogGPSStates description];
-[AWDMETRICSKCellularPowerLogGPSStates readFrom:];
-[AWDMETRICSKCellularPowerLogGPSStates copyWithZone:];
-[AWDMETRICSKCellularPowerLogGPSStates isEqual:];
-[AWDMETRICSKCellularPowerLogGPSStates dictionaryRepresentation];
-[AWDMETRICSKCellularPowerLogGPSStates durationMs];
-[AWDMETRICSKCellularPowerLogGPSStates hasDurationMs];
-[AWDMETRICSKCellularPowerLogGPSStates setDurationMs:];
-[AWDMETRICSKCellularPowerLogGPSStates setHasDurationMs:];
-[AWDMETRICSKCellularPowerLogGPSStates bins];
-[AWDMETRICSKCellularPowerLogGPSStates setBins:];
-[AWDMETRICSKCellularPowerLogGPSStates StringAsLastSdmState:];
-[AWDMETRICSKCellularPowerLogGPSStates addBin:];
-[AWDMETRICSKCellularPowerLogGPSStates hasLastSdmState];
-[AWDMETRICSKCellularPowerLogGPSStates binAtIndex:];
-[AWDMETRICSKCellularPowerLogGPSStates binsCount];
-[AWDMETRICSKCellularPowerLogGPSStates clearBins];
-[AWDMETRICSKCellularPowerLogGPSStates hasSubsId];
-[AWDMETRICSKCellularPowerLogGPSStates lastSdmState];
-[AWDMETRICSKCellularPowerLogGPSStates lastSdmStateAsString:];
-[AWDMETRICSKCellularPowerLogGPSStates setHasLastSdmState:];
-[AWDMETRICSKCellularPowerLogGPSStates setHasSubsId:];
-[AWDMETRICSKCellularPowerLogGPSStates setLastSdmState:];
-[AWDMETRICSKCellularPowerLogGPSStates setSubsId:];
-[AWDMETRICSKCellularPowerLogGPSStates subsId];
```
