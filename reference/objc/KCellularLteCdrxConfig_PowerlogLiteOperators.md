# `KCellularLteCdrxConfig`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 13 instance variables, 24 properties, 59 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
I _cdrxConfigStatus;
I _cellStatus;
I _drxInactivityMs;
I _drxRetxTimerMs;
I _drxShortCycleNum;
I _longDrxCycleMs;
I _onDurationMs;
i _rrcState;
I _shortDrxCycleMs;
I _subsId;
I _transmissionMode;
{?="timestamp"b1"cdrxConfigStatus"b1"cellStatus"b1"drxInactivityMs"b1"drxRetxTimerMs"b1"drxShortCycleNum"b1"longDrxCycleMs"b1"onDurationMs"b1"rrcState"b1"shortDrxCycleMs"b1"subsId"b1"transmissionMode"b1} _has;
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
-[KCellularLteCdrxConfig hasTimestamp];
-[KCellularLteCdrxConfig setHasTimestamp:];
-[KCellularLteCdrxConfig setTimestamp:];
-[KCellularLteCdrxConfig writeTo:];
-[KCellularLteCdrxConfig mergeFrom:];
-[KCellularLteCdrxConfig timestamp];
-[KCellularLteCdrxConfig transmissionMode];
-[KCellularLteCdrxConfig hash];
-[KCellularLteCdrxConfig copyTo:];
-[KCellularLteCdrxConfig description];
-[KCellularLteCdrxConfig readFrom:];
-[KCellularLteCdrxConfig copyWithZone:];
-[KCellularLteCdrxConfig isEqual:];
-[KCellularLteCdrxConfig setTransmissionMode:];
-[KCellularLteCdrxConfig dictionaryRepresentation];
-[KCellularLteCdrxConfig setHasRrcState:];
-[KCellularLteCdrxConfig hasRrcState];
-[KCellularLteCdrxConfig rrcState];
-[KCellularLteCdrxConfig StringAsRrcState:];
-[KCellularLteCdrxConfig drxInactivityMs];
-[KCellularLteCdrxConfig hasOnDurationMs];
-[KCellularLteCdrxConfig shortDrxCycleMs];
-[KCellularLteCdrxConfig cdrxConfigStatus];
-[KCellularLteCdrxConfig cellStatus];
-[KCellularLteCdrxConfig drxRetxTimerMs];
-[KCellularLteCdrxConfig drxShortCycleNum];
-[KCellularLteCdrxConfig hasCdrxConfigStatus];
-[KCellularLteCdrxConfig hasCellStatus];
-[KCellularLteCdrxConfig hasDrxInactivityMs];
-[KCellularLteCdrxConfig hasDrxRetxTimerMs];
-[KCellularLteCdrxConfig hasDrxShortCycleNum];
-[KCellularLteCdrxConfig hasLongDrxCycleMs];
-[KCellularLteCdrxConfig hasShortDrxCycleMs];
-[KCellularLteCdrxConfig hasSubsId];
-[KCellularLteCdrxConfig hasTransmissionMode];
-[KCellularLteCdrxConfig longDrxCycleMs];
-[KCellularLteCdrxConfig onDurationMs];
-[KCellularLteCdrxConfig rrcStateAsString:];
-[KCellularLteCdrxConfig setCdrxConfigStatus:];
-[KCellularLteCdrxConfig setCellStatus:];
-[KCellularLteCdrxConfig setDrxInactivityMs:];
-[KCellularLteCdrxConfig setDrxRetxTimerMs:];
-[KCellularLteCdrxConfig setDrxShortCycleNum:];
-[KCellularLteCdrxConfig setHasCdrxConfigStatus:];
-[KCellularLteCdrxConfig setHasCellStatus:];
-[KCellularLteCdrxConfig setHasDrxInactivityMs:];
-[KCellularLteCdrxConfig setHasDrxRetxTimerMs:];
-[KCellularLteCdrxConfig setHasDrxShortCycleNum:];
-[KCellularLteCdrxConfig setHasLongDrxCycleMs:];
-[KCellularLteCdrxConfig setHasOnDurationMs:];
-[KCellularLteCdrxConfig setHasShortDrxCycleMs:];
-[KCellularLteCdrxConfig setHasSubsId:];
-[KCellularLteCdrxConfig setHasTransmissionMode:];
-[KCellularLteCdrxConfig setLongDrxCycleMs:];
-[KCellularLteCdrxConfig setOnDurationMs:];
-[KCellularLteCdrxConfig setRrcState:];
-[KCellularLteCdrxConfig setShortDrxCycleMs:];
-[KCellularLteCdrxConfig setSubsId:];
-[KCellularLteCdrxConfig subsId];
```
