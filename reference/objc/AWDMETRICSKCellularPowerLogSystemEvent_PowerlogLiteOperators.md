# `AWDMETRICSKCellularPowerLogSystemEvent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 9 instance variables, 16 properties, 49 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
i _mode;
i _prevMode;
i _prevRat;
I _prevStateDurationMs;
i _rat;
I _subsId;
B _oosPlmnSearchTimerActive;
{?="timestamp"b1"mode"b1"prevMode"b1"prevRat"b1"prevStateDurationMs"b1"rat"b1"subsId"b1"oosPlmnSearchTimerActive"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
@property (TB,N) hasOosPlmnSearchTimerActive;
@property (TB,N,V_oosPlmnSearchTimerActive) oosPlmnSearchTimerActive;
@property (TB,N) hasMode;
@property (Ti,N,V_mode) mode;
@property (TB,N) hasRat;
@property (Ti,N,V_rat) rat;
@property (TB,N) hasPrevMode;
@property (Ti,N,V_prevMode) prevMode;
@property (TB,N) hasPrevRat;
@property (Ti,N,V_prevRat) prevRat;
@property (TB,N) hasPrevStateDurationMs;
@property (TI,N,V_prevStateDurationMs) prevStateDurationMs;
```

## Instance methods

```
-[AWDMETRICSKCellularPowerLogSystemEvent StringAsMode:];
-[AWDMETRICSKCellularPowerLogSystemEvent setHasMode:];
-[AWDMETRICSKCellularPowerLogSystemEvent hasTimestamp];
-[AWDMETRICSKCellularPowerLogSystemEvent hasMode];
-[AWDMETRICSKCellularPowerLogSystemEvent setHasTimestamp:];
-[AWDMETRICSKCellularPowerLogSystemEvent setTimestamp:];
-[AWDMETRICSKCellularPowerLogSystemEvent writeTo:];
-[AWDMETRICSKCellularPowerLogSystemEvent mergeFrom:];
-[AWDMETRICSKCellularPowerLogSystemEvent timestamp];
-[AWDMETRICSKCellularPowerLogSystemEvent setMode:];
-[AWDMETRICSKCellularPowerLogSystemEvent rat];
-[AWDMETRICSKCellularPowerLogSystemEvent mode];
-[AWDMETRICSKCellularPowerLogSystemEvent hash];
-[AWDMETRICSKCellularPowerLogSystemEvent copyTo:];
-[AWDMETRICSKCellularPowerLogSystemEvent description];
-[AWDMETRICSKCellularPowerLogSystemEvent readFrom:];
-[AWDMETRICSKCellularPowerLogSystemEvent modeAsString:];
-[AWDMETRICSKCellularPowerLogSystemEvent copyWithZone:];
-[AWDMETRICSKCellularPowerLogSystemEvent isEqual:];
-[AWDMETRICSKCellularPowerLogSystemEvent dictionaryRepresentation];
-[AWDMETRICSKCellularPowerLogSystemEvent setRat:];
-[AWDMETRICSKCellularPowerLogSystemEvent hasRat];
-[AWDMETRICSKCellularPowerLogSystemEvent setHasRat:];
-[AWDMETRICSKCellularPowerLogSystemEvent StringAsPrevRat:];
-[AWDMETRICSKCellularPowerLogSystemEvent StringAsRat:];
-[AWDMETRICSKCellularPowerLogSystemEvent setHasOosPlmnSearchTimerActive:];
-[AWDMETRICSKCellularPowerLogSystemEvent StringAsPrevMode:];
-[AWDMETRICSKCellularPowerLogSystemEvent prevRat];
-[AWDMETRICSKCellularPowerLogSystemEvent setHasPrevMode:];
-[AWDMETRICSKCellularPowerLogSystemEvent hasOosPlmnSearchTimerActive];
-[AWDMETRICSKCellularPowerLogSystemEvent hasPrevMode];
-[AWDMETRICSKCellularPowerLogSystemEvent hasPrevRat];
-[AWDMETRICSKCellularPowerLogSystemEvent hasPrevStateDurationMs];
-[AWDMETRICSKCellularPowerLogSystemEvent hasSubsId];
-[AWDMETRICSKCellularPowerLogSystemEvent oosPlmnSearchTimerActive];
-[AWDMETRICSKCellularPowerLogSystemEvent prevMode];
-[AWDMETRICSKCellularPowerLogSystemEvent prevModeAsString:];
-[AWDMETRICSKCellularPowerLogSystemEvent prevRatAsString:];
-[AWDMETRICSKCellularPowerLogSystemEvent prevStateDurationMs];
-[AWDMETRICSKCellularPowerLogSystemEvent ratAsString:];
-[AWDMETRICSKCellularPowerLogSystemEvent setHasPrevRat:];
-[AWDMETRICSKCellularPowerLogSystemEvent setHasPrevStateDurationMs:];
-[AWDMETRICSKCellularPowerLogSystemEvent setHasSubsId:];
-[AWDMETRICSKCellularPowerLogSystemEvent setOosPlmnSearchTimerActive:];
-[AWDMETRICSKCellularPowerLogSystemEvent setPrevMode:];
-[AWDMETRICSKCellularPowerLogSystemEvent setPrevRat:];
-[AWDMETRICSKCellularPowerLogSystemEvent setPrevStateDurationMs:];
-[AWDMETRICSKCellularPowerLogSystemEvent setSubsId:];
-[AWDMETRICSKCellularPowerLogSystemEvent subsId];
```
