# `AWDMETRICSKCellularPowerLogXOShutdown`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 8 instance variables, 13 properties, 41 instance methods, 1 class methods

## Instance variables

```
Q _timestamp;
@"NSMutableArray" _bins;
I _duration;
I _durationMs;
i _lastSdmState;
I _shutdownCount;
I _totalNon0States;
{?="timestamp"b1"duration"b1"durationMs"b1"lastSdmState"b1"shutdownCount"b1"totalNon0States"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (T@"NSMutableArray",&,N,V_bins) bins;
@property (TB,N) hasDurationMs;
@property (TI,N,V_durationMs) durationMs;
@property (TB,N) hasDuration;
@property (TI,N,V_duration) duration;
@property (TB,N) hasShutdownCount;
@property (TI,N,V_shutdownCount) shutdownCount;
@property (TB,N) hasTotalNon0States;
@property (TI,N,V_totalNon0States) totalNon0States;
@property (TB,N) hasLastSdmState;
@property (Ti,N,V_lastSdmState) lastSdmState;
```

## Class methods

```
+[AWDMETRICSKCellularPowerLogXOShutdown binType];
```

## Instance methods

```
-[AWDMETRICSKCellularPowerLogXOShutdown hasTimestamp];
-[AWDMETRICSKCellularPowerLogXOShutdown setHasTimestamp:];
-[AWDMETRICSKCellularPowerLogXOShutdown setTimestamp:];
-[AWDMETRICSKCellularPowerLogXOShutdown writeTo:];
-[AWDMETRICSKCellularPowerLogXOShutdown mergeFrom:];
-[AWDMETRICSKCellularPowerLogXOShutdown hasDuration];
-[AWDMETRICSKCellularPowerLogXOShutdown timestamp];
-[AWDMETRICSKCellularPowerLogXOShutdown duration];
-[AWDMETRICSKCellularPowerLogXOShutdown setHasDuration:];
-[AWDMETRICSKCellularPowerLogXOShutdown hash];
-[AWDMETRICSKCellularPowerLogXOShutdown copyTo:];
-[AWDMETRICSKCellularPowerLogXOShutdown description];
-[AWDMETRICSKCellularPowerLogXOShutdown setDuration:];
-[AWDMETRICSKCellularPowerLogXOShutdown readFrom:];
-[AWDMETRICSKCellularPowerLogXOShutdown copyWithZone:];
-[AWDMETRICSKCellularPowerLogXOShutdown isEqual:];
-[AWDMETRICSKCellularPowerLogXOShutdown dictionaryRepresentation];
-[AWDMETRICSKCellularPowerLogXOShutdown durationMs];
-[AWDMETRICSKCellularPowerLogXOShutdown hasDurationMs];
-[AWDMETRICSKCellularPowerLogXOShutdown setDurationMs:];
-[AWDMETRICSKCellularPowerLogXOShutdown setHasDurationMs:];
-[AWDMETRICSKCellularPowerLogXOShutdown bins];
-[AWDMETRICSKCellularPowerLogXOShutdown setBins:];
-[AWDMETRICSKCellularPowerLogXOShutdown totalNon0States];
-[AWDMETRICSKCellularPowerLogXOShutdown StringAsLastSdmState:];
-[AWDMETRICSKCellularPowerLogXOShutdown addBin:];
-[AWDMETRICSKCellularPowerLogXOShutdown hasLastSdmState];
-[AWDMETRICSKCellularPowerLogXOShutdown binAtIndex:];
-[AWDMETRICSKCellularPowerLogXOShutdown binsCount];
-[AWDMETRICSKCellularPowerLogXOShutdown clearBins];
-[AWDMETRICSKCellularPowerLogXOShutdown hasShutdownCount];
-[AWDMETRICSKCellularPowerLogXOShutdown hasTotalNon0States];
-[AWDMETRICSKCellularPowerLogXOShutdown lastSdmState];
-[AWDMETRICSKCellularPowerLogXOShutdown lastSdmStateAsString:];
-[AWDMETRICSKCellularPowerLogXOShutdown setHasLastSdmState:];
-[AWDMETRICSKCellularPowerLogXOShutdown setHasShutdownCount:];
-[AWDMETRICSKCellularPowerLogXOShutdown setHasTotalNon0States:];
-[AWDMETRICSKCellularPowerLogXOShutdown setLastSdmState:];
-[AWDMETRICSKCellularPowerLogXOShutdown setShutdownCount:];
-[AWDMETRICSKCellularPowerLogXOShutdown setTotalNon0States:];
-[AWDMETRICSKCellularPowerLogXOShutdown shutdownCount];
```
