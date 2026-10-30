# `AWDMETRICSKCellularPowerLogCpuPerfLevels`

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
+[AWDMETRICSKCellularPowerLogCpuPerfLevels binType];
```

## Instance methods

```
-[AWDMETRICSKCellularPowerLogCpuPerfLevels hasTimestamp];
-[AWDMETRICSKCellularPowerLogCpuPerfLevels setHasTimestamp:];
-[AWDMETRICSKCellularPowerLogCpuPerfLevels setTimestamp:];
-[AWDMETRICSKCellularPowerLogCpuPerfLevels writeTo:];
-[AWDMETRICSKCellularPowerLogCpuPerfLevels mergeFrom:];
-[AWDMETRICSKCellularPowerLogCpuPerfLevels timestamp];
-[AWDMETRICSKCellularPowerLogCpuPerfLevels hash];
-[AWDMETRICSKCellularPowerLogCpuPerfLevels copyTo:];
-[AWDMETRICSKCellularPowerLogCpuPerfLevels description];
-[AWDMETRICSKCellularPowerLogCpuPerfLevels readFrom:];
-[AWDMETRICSKCellularPowerLogCpuPerfLevels copyWithZone:];
-[AWDMETRICSKCellularPowerLogCpuPerfLevels isEqual:];
-[AWDMETRICSKCellularPowerLogCpuPerfLevels dictionaryRepresentation];
-[AWDMETRICSKCellularPowerLogCpuPerfLevels durationMs];
-[AWDMETRICSKCellularPowerLogCpuPerfLevels hasDurationMs];
-[AWDMETRICSKCellularPowerLogCpuPerfLevels setDurationMs:];
-[AWDMETRICSKCellularPowerLogCpuPerfLevels setHasDurationMs:];
-[AWDMETRICSKCellularPowerLogCpuPerfLevels bins];
-[AWDMETRICSKCellularPowerLogCpuPerfLevels setBins:];
-[AWDMETRICSKCellularPowerLogCpuPerfLevels StringAsLastSdmState:];
-[AWDMETRICSKCellularPowerLogCpuPerfLevels addBin:];
-[AWDMETRICSKCellularPowerLogCpuPerfLevels hasLastSdmState];
-[AWDMETRICSKCellularPowerLogCpuPerfLevels binAtIndex:];
-[AWDMETRICSKCellularPowerLogCpuPerfLevels binsCount];
-[AWDMETRICSKCellularPowerLogCpuPerfLevels clearBins];
-[AWDMETRICSKCellularPowerLogCpuPerfLevels hasSubsId];
-[AWDMETRICSKCellularPowerLogCpuPerfLevels lastSdmState];
-[AWDMETRICSKCellularPowerLogCpuPerfLevels lastSdmStateAsString:];
-[AWDMETRICSKCellularPowerLogCpuPerfLevels setHasLastSdmState:];
-[AWDMETRICSKCellularPowerLogCpuPerfLevels setHasSubsId:];
-[AWDMETRICSKCellularPowerLogCpuPerfLevels setLastSdmState:];
-[AWDMETRICSKCellularPowerLogCpuPerfLevels setSubsId:];
-[AWDMETRICSKCellularPowerLogCpuPerfLevels subsId];
```
