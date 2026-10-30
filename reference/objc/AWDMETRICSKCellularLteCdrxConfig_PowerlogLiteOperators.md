# `AWDMETRICSKCellularLteCdrxConfig`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 15 instance variables, 28 properties, 67 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
I _cdrxConfigStatus;
I _cellStatus;
I _drxInactivityMs;
I _drxRetxTimerMs;
I _drxShortCycleNum;
I _longDrxCycleMs;
I _longDrxCycleStartOffsetMs;
I _onDurationMs;
i _rrcState;
I _shortDrxCycleMs;
I _subsId;
I _transmissionMode;
B _shortDrxCycleEnable;
{?="timestamp"b1"cdrxConfigStatus"b1"cellStatus"b1"drxInactivityMs"b1"drxRetxTimerMs"b1"drxShortCycleNum"b1"longDrxCycleMs"b1"longDrxCycleStartOffsetMs"b1"onDurationMs"b1"rrcState"b1"shortDrxCycleMs"b1"subsId"b1"transmissionMode"b1"shortDrxCycleEnable"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasCellStatus;
@property (TI,N,V_cellStatus) cellStatus;
@property (TB,N) hasOnDurationMs;
@property (TI,N,V_onDurationMs) onDurationMs;
@property (TB,N) hasDrxInactivityMs;
@property (TI,N,V_drxInactivityMs) drxInactivityMs;
@property (TB,N) hasDrxRetxTimerMs;
@property (TI,N,V_drxRetxTimerMs) drxRetxTimerMs;
@property (TB,N) hasLongDrxCycleMs;
@property (TI,N,V_longDrxCycleMs) longDrxCycleMs;
@property (TB,N) hasLongDrxCycleStartOffsetMs;
@property (TI,N,V_longDrxCycleStartOffsetMs) longDrxCycleStartOffsetMs;
@property (TB,N) hasShortDrxCycleEnable;
@property (TB,N,V_shortDrxCycleEnable) shortDrxCycleEnable;
@property (TB,N) hasShortDrxCycleMs;
@property (TI,N,V_shortDrxCycleMs) shortDrxCycleMs;
@property (TB,N) hasDrxShortCycleNum;
@property (TI,N,V_drxShortCycleNum) drxShortCycleNum;
@property (TB,N) hasRrcState;
@property (Ti,N,V_rrcState) rrcState;
@property (TB,N) hasCdrxConfigStatus;
@property (TI,N,V_cdrxConfigStatus) cdrxConfigStatus;
@property (TB,N) hasTransmissionMode;
@property (TI,N,V_transmissionMode) transmissionMode;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
```

## Instance methods

```
-[AWDMETRICSKCellularLteCdrxConfig hasTimestamp];
-[AWDMETRICSKCellularLteCdrxConfig setHasTimestamp:];
-[AWDMETRICSKCellularLteCdrxConfig setTimestamp:];
-[AWDMETRICSKCellularLteCdrxConfig writeTo:];
-[AWDMETRICSKCellularLteCdrxConfig mergeFrom:];
-[AWDMETRICSKCellularLteCdrxConfig timestamp];
-[AWDMETRICSKCellularLteCdrxConfig transmissionMode];
-[AWDMETRICSKCellularLteCdrxConfig hash];
-[AWDMETRICSKCellularLteCdrxConfig copyTo:];
-[AWDMETRICSKCellularLteCdrxConfig description];
-[AWDMETRICSKCellularLteCdrxConfig readFrom:];
-[AWDMETRICSKCellularLteCdrxConfig copyWithZone:];
-[AWDMETRICSKCellularLteCdrxConfig isEqual:];
-[AWDMETRICSKCellularLteCdrxConfig setTransmissionMode:];
-[AWDMETRICSKCellularLteCdrxConfig dictionaryRepresentation];
-[AWDMETRICSKCellularLteCdrxConfig setHasRrcState:];
-[AWDMETRICSKCellularLteCdrxConfig hasRrcState];
-[AWDMETRICSKCellularLteCdrxConfig rrcState];
-[AWDMETRICSKCellularLteCdrxConfig StringAsRrcState:];
-[AWDMETRICSKCellularLteCdrxConfig drxInactivityMs];
-[AWDMETRICSKCellularLteCdrxConfig hasOnDurationMs];
-[AWDMETRICSKCellularLteCdrxConfig shortDrxCycleMs];
-[AWDMETRICSKCellularLteCdrxConfig cdrxConfigStatus];
-[AWDMETRICSKCellularLteCdrxConfig cellStatus];
-[AWDMETRICSKCellularLteCdrxConfig drxRetxTimerMs];
-[AWDMETRICSKCellularLteCdrxConfig drxShortCycleNum];
-[AWDMETRICSKCellularLteCdrxConfig hasCdrxConfigStatus];
-[AWDMETRICSKCellularLteCdrxConfig hasCellStatus];
-[AWDMETRICSKCellularLteCdrxConfig hasDrxInactivityMs];
-[AWDMETRICSKCellularLteCdrxConfig hasDrxRetxTimerMs];
-[AWDMETRICSKCellularLteCdrxConfig hasDrxShortCycleNum];
-[AWDMETRICSKCellularLteCdrxConfig hasLongDrxCycleMs];
-[AWDMETRICSKCellularLteCdrxConfig hasLongDrxCycleStartOffsetMs];
-[AWDMETRICSKCellularLteCdrxConfig hasShortDrxCycleEnable];
-[AWDMETRICSKCellularLteCdrxConfig hasShortDrxCycleMs];
-[AWDMETRICSKCellularLteCdrxConfig hasSubsId];
-[AWDMETRICSKCellularLteCdrxConfig hasTransmissionMode];
-[AWDMETRICSKCellularLteCdrxConfig longDrxCycleMs];
-[AWDMETRICSKCellularLteCdrxConfig longDrxCycleStartOffsetMs];
-[AWDMETRICSKCellularLteCdrxConfig onDurationMs];
-[AWDMETRICSKCellularLteCdrxConfig rrcStateAsString:];
-[AWDMETRICSKCellularLteCdrxConfig setCdrxConfigStatus:];
-[AWDMETRICSKCellularLteCdrxConfig setCellStatus:];
-[AWDMETRICSKCellularLteCdrxConfig setDrxInactivityMs:];
-[AWDMETRICSKCellularLteCdrxConfig setDrxRetxTimerMs:];
-[AWDMETRICSKCellularLteCdrxConfig setDrxShortCycleNum:];
-[AWDMETRICSKCellularLteCdrxConfig setHasCdrxConfigStatus:];
-[AWDMETRICSKCellularLteCdrxConfig setHasCellStatus:];
-[AWDMETRICSKCellularLteCdrxConfig setHasDrxInactivityMs:];
-[AWDMETRICSKCellularLteCdrxConfig setHasDrxRetxTimerMs:];
-[AWDMETRICSKCellularLteCdrxConfig setHasDrxShortCycleNum:];
-[AWDMETRICSKCellularLteCdrxConfig setHasLongDrxCycleMs:];
-[AWDMETRICSKCellularLteCdrxConfig setHasLongDrxCycleStartOffsetMs:];
-[AWDMETRICSKCellularLteCdrxConfig setHasOnDurationMs:];
-[AWDMETRICSKCellularLteCdrxConfig setHasShortDrxCycleEnable:];
-[AWDMETRICSKCellularLteCdrxConfig setHasShortDrxCycleMs:];
-[AWDMETRICSKCellularLteCdrxConfig setHasSubsId:];
-[AWDMETRICSKCellularLteCdrxConfig setHasTransmissionMode:];
-[AWDMETRICSKCellularLteCdrxConfig setLongDrxCycleMs:];
-[AWDMETRICSKCellularLteCdrxConfig setLongDrxCycleStartOffsetMs:];
-[AWDMETRICSKCellularLteCdrxConfig setOnDurationMs:];
-[AWDMETRICSKCellularLteCdrxConfig setRrcState:];
-[AWDMETRICSKCellularLteCdrxConfig setShortDrxCycleEnable:];
-[AWDMETRICSKCellularLteCdrxConfig setShortDrxCycleMs:];
-[AWDMETRICSKCellularLteCdrxConfig setSubsId:];
-[AWDMETRICSKCellularLteCdrxConfig shortDrxCycleEnable];
-[AWDMETRICSKCellularLteCdrxConfig subsId];
```
