# `AWDMETRICSKCellularPowerLogSocPerfLevels`

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
+[AWDMETRICSKCellularPowerLogSocPerfLevels binType];
```

## Instance methods

```
-[AWDMETRICSKCellularPowerLogSocPerfLevels hasTimestamp];
-[AWDMETRICSKCellularPowerLogSocPerfLevels setHasTimestamp:];
-[AWDMETRICSKCellularPowerLogSocPerfLevels setTimestamp:];
-[AWDMETRICSKCellularPowerLogSocPerfLevels writeTo:];
-[AWDMETRICSKCellularPowerLogSocPerfLevels mergeFrom:];
-[AWDMETRICSKCellularPowerLogSocPerfLevels timestamp];
-[AWDMETRICSKCellularPowerLogSocPerfLevels hash];
-[AWDMETRICSKCellularPowerLogSocPerfLevels copyTo:];
-[AWDMETRICSKCellularPowerLogSocPerfLevels description];
-[AWDMETRICSKCellularPowerLogSocPerfLevels readFrom:];
-[AWDMETRICSKCellularPowerLogSocPerfLevels copyWithZone:];
-[AWDMETRICSKCellularPowerLogSocPerfLevels isEqual:];
-[AWDMETRICSKCellularPowerLogSocPerfLevels dictionaryRepresentation];
-[AWDMETRICSKCellularPowerLogSocPerfLevels durationMs];
-[AWDMETRICSKCellularPowerLogSocPerfLevels hasDurationMs];
-[AWDMETRICSKCellularPowerLogSocPerfLevels setDurationMs:];
-[AWDMETRICSKCellularPowerLogSocPerfLevels setHasDurationMs:];
-[AWDMETRICSKCellularPowerLogSocPerfLevels bins];
-[AWDMETRICSKCellularPowerLogSocPerfLevels setBins:];
-[AWDMETRICSKCellularPowerLogSocPerfLevels StringAsLastSdmState:];
-[AWDMETRICSKCellularPowerLogSocPerfLevels addBin:];
-[AWDMETRICSKCellularPowerLogSocPerfLevels hasLastSdmState];
-[AWDMETRICSKCellularPowerLogSocPerfLevels binAtIndex:];
-[AWDMETRICSKCellularPowerLogSocPerfLevels binsCount];
-[AWDMETRICSKCellularPowerLogSocPerfLevels clearBins];
-[AWDMETRICSKCellularPowerLogSocPerfLevels hasSubsId];
-[AWDMETRICSKCellularPowerLogSocPerfLevels lastSdmState];
-[AWDMETRICSKCellularPowerLogSocPerfLevels lastSdmStateAsString:];
-[AWDMETRICSKCellularPowerLogSocPerfLevels setHasLastSdmState:];
-[AWDMETRICSKCellularPowerLogSocPerfLevels setHasSubsId:];
-[AWDMETRICSKCellularPowerLogSocPerfLevels setLastSdmState:];
-[AWDMETRICSKCellularPowerLogSocPerfLevels setSubsId:];
-[AWDMETRICSKCellularPowerLogSocPerfLevels subsId];
```
