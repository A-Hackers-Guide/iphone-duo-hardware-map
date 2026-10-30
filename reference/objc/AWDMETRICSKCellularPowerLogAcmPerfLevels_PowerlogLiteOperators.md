# `AWDMETRICSKCellularPowerLogAcmPerfLevels`

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
+[AWDMETRICSKCellularPowerLogAcmPerfLevels binType];
```

## Instance methods

```
-[AWDMETRICSKCellularPowerLogAcmPerfLevels hasTimestamp];
-[AWDMETRICSKCellularPowerLogAcmPerfLevels setHasTimestamp:];
-[AWDMETRICSKCellularPowerLogAcmPerfLevels setTimestamp:];
-[AWDMETRICSKCellularPowerLogAcmPerfLevels writeTo:];
-[AWDMETRICSKCellularPowerLogAcmPerfLevels mergeFrom:];
-[AWDMETRICSKCellularPowerLogAcmPerfLevels timestamp];
-[AWDMETRICSKCellularPowerLogAcmPerfLevels hash];
-[AWDMETRICSKCellularPowerLogAcmPerfLevels copyTo:];
-[AWDMETRICSKCellularPowerLogAcmPerfLevels description];
-[AWDMETRICSKCellularPowerLogAcmPerfLevels readFrom:];
-[AWDMETRICSKCellularPowerLogAcmPerfLevels copyWithZone:];
-[AWDMETRICSKCellularPowerLogAcmPerfLevels isEqual:];
-[AWDMETRICSKCellularPowerLogAcmPerfLevels dictionaryRepresentation];
-[AWDMETRICSKCellularPowerLogAcmPerfLevels durationMs];
-[AWDMETRICSKCellularPowerLogAcmPerfLevels hasDurationMs];
-[AWDMETRICSKCellularPowerLogAcmPerfLevels setDurationMs:];
-[AWDMETRICSKCellularPowerLogAcmPerfLevels setHasDurationMs:];
-[AWDMETRICSKCellularPowerLogAcmPerfLevels bins];
-[AWDMETRICSKCellularPowerLogAcmPerfLevels setBins:];
-[AWDMETRICSKCellularPowerLogAcmPerfLevels StringAsLastSdmState:];
-[AWDMETRICSKCellularPowerLogAcmPerfLevels addBin:];
-[AWDMETRICSKCellularPowerLogAcmPerfLevels hasLastSdmState];
-[AWDMETRICSKCellularPowerLogAcmPerfLevels binAtIndex:];
-[AWDMETRICSKCellularPowerLogAcmPerfLevels binsCount];
-[AWDMETRICSKCellularPowerLogAcmPerfLevels clearBins];
-[AWDMETRICSKCellularPowerLogAcmPerfLevels hasSubsId];
-[AWDMETRICSKCellularPowerLogAcmPerfLevels lastSdmState];
-[AWDMETRICSKCellularPowerLogAcmPerfLevels lastSdmStateAsString:];
-[AWDMETRICSKCellularPowerLogAcmPerfLevels setHasLastSdmState:];
-[AWDMETRICSKCellularPowerLogAcmPerfLevels setHasSubsId:];
-[AWDMETRICSKCellularPowerLogAcmPerfLevels setLastSdmState:];
-[AWDMETRICSKCellularPowerLogAcmPerfLevels setSubsId:];
-[AWDMETRICSKCellularPowerLogAcmPerfLevels subsId];
```
