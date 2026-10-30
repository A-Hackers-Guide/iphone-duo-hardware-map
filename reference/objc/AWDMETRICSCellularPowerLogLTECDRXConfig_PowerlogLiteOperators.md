# `AWDMETRICSCellularPowerLogLTECDRXConfig`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 12 instance variables, 22 properties, 53 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
I _cycleStartOffset;
I _drxInactivity;
I _drxRetxTimer;
I _drxShortCycleNum;
I _longDrxCycle;
I _onDuration;
I _shortDrxCycle;
I _subsId;
B _cdrxEnable;
B _shortDrxCycleEnable;
{?="timestamp"b1"cycleStartOffset"b1"drxInactivity"b1"drxRetxTimer"b1"drxShortCycleNum"b1"longDrxCycle"b1"onDuration"b1"shortDrxCycle"b1"subsId"b1"cdrxEnable"b1"shortDrxCycleEnable"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasOnDuration;
@property (TI,N,V_onDuration) onDuration;
@property (TB,N) hasDrxInactivity;
@property (TI,N,V_drxInactivity) drxInactivity;
@property (TB,N) hasDrxRetxTimer;
@property (TI,N,V_drxRetxTimer) drxRetxTimer;
@property (TB,N) hasLongDrxCycle;
@property (TI,N,V_longDrxCycle) longDrxCycle;
@property (TB,N) hasCycleStartOffset;
@property (TI,N,V_cycleStartOffset) cycleStartOffset;
@property (TB,N) hasShortDrxCycleEnable;
@property (TB,N,V_shortDrxCycleEnable) shortDrxCycleEnable;
@property (TB,N) hasShortDrxCycle;
@property (TI,N,V_shortDrxCycle) shortDrxCycle;
@property (TB,N) hasDrxShortCycleNum;
@property (TI,N,V_drxShortCycleNum) drxShortCycleNum;
@property (TB,N) hasCdrxEnable;
@property (TB,N,V_cdrxEnable) cdrxEnable;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
```

## Instance methods

```
-[AWDMETRICSCellularPowerLogLTECDRXConfig hasTimestamp];
-[AWDMETRICSCellularPowerLogLTECDRXConfig setHasTimestamp:];
-[AWDMETRICSCellularPowerLogLTECDRXConfig setTimestamp:];
-[AWDMETRICSCellularPowerLogLTECDRXConfig writeTo:];
-[AWDMETRICSCellularPowerLogLTECDRXConfig mergeFrom:];
-[AWDMETRICSCellularPowerLogLTECDRXConfig timestamp];
-[AWDMETRICSCellularPowerLogLTECDRXConfig hash];
-[AWDMETRICSCellularPowerLogLTECDRXConfig copyTo:];
-[AWDMETRICSCellularPowerLogLTECDRXConfig description];
-[AWDMETRICSCellularPowerLogLTECDRXConfig readFrom:];
-[AWDMETRICSCellularPowerLogLTECDRXConfig copyWithZone:];
-[AWDMETRICSCellularPowerLogLTECDRXConfig isEqual:];
-[AWDMETRICSCellularPowerLogLTECDRXConfig dictionaryRepresentation];
-[AWDMETRICSCellularPowerLogLTECDRXConfig hasLongDrxCycle];
-[AWDMETRICSCellularPowerLogLTECDRXConfig hasDrxRetxTimer];
-[AWDMETRICSCellularPowerLogLTECDRXConfig cdrxEnable];
-[AWDMETRICSCellularPowerLogLTECDRXConfig cycleStartOffset];
-[AWDMETRICSCellularPowerLogLTECDRXConfig drxInactivity];
-[AWDMETRICSCellularPowerLogLTECDRXConfig drxRetxTimer];
-[AWDMETRICSCellularPowerLogLTECDRXConfig drxShortCycleNum];
-[AWDMETRICSCellularPowerLogLTECDRXConfig hasCdrxEnable];
-[AWDMETRICSCellularPowerLogLTECDRXConfig hasCycleStartOffset];
-[AWDMETRICSCellularPowerLogLTECDRXConfig hasDrxInactivity];
-[AWDMETRICSCellularPowerLogLTECDRXConfig hasDrxShortCycleNum];
-[AWDMETRICSCellularPowerLogLTECDRXConfig hasOnDuration];
-[AWDMETRICSCellularPowerLogLTECDRXConfig hasShortDrxCycle];
-[AWDMETRICSCellularPowerLogLTECDRXConfig hasShortDrxCycleEnable];
-[AWDMETRICSCellularPowerLogLTECDRXConfig hasSubsId];
-[AWDMETRICSCellularPowerLogLTECDRXConfig longDrxCycle];
-[AWDMETRICSCellularPowerLogLTECDRXConfig onDuration];
-[AWDMETRICSCellularPowerLogLTECDRXConfig setCdrxEnable:];
-[AWDMETRICSCellularPowerLogLTECDRXConfig setCycleStartOffset:];
-[AWDMETRICSCellularPowerLogLTECDRXConfig setDrxInactivity:];
-[AWDMETRICSCellularPowerLogLTECDRXConfig setDrxRetxTimer:];
-[AWDMETRICSCellularPowerLogLTECDRXConfig setDrxShortCycleNum:];
-[AWDMETRICSCellularPowerLogLTECDRXConfig setHasCdrxEnable:];
-[AWDMETRICSCellularPowerLogLTECDRXConfig setHasCycleStartOffset:];
-[AWDMETRICSCellularPowerLogLTECDRXConfig setHasDrxInactivity:];
-[AWDMETRICSCellularPowerLogLTECDRXConfig setHasDrxRetxTimer:];
-[AWDMETRICSCellularPowerLogLTECDRXConfig setHasDrxShortCycleNum:];
-[AWDMETRICSCellularPowerLogLTECDRXConfig setHasLongDrxCycle:];
-[AWDMETRICSCellularPowerLogLTECDRXConfig setHasOnDuration:];
-[AWDMETRICSCellularPowerLogLTECDRXConfig setHasShortDrxCycle:];
-[AWDMETRICSCellularPowerLogLTECDRXConfig setHasShortDrxCycleEnable:];
-[AWDMETRICSCellularPowerLogLTECDRXConfig setHasSubsId:];
-[AWDMETRICSCellularPowerLogLTECDRXConfig setLongDrxCycle:];
-[AWDMETRICSCellularPowerLogLTECDRXConfig setOnDuration:];
-[AWDMETRICSCellularPowerLogLTECDRXConfig setShortDrxCycle:];
-[AWDMETRICSCellularPowerLogLTECDRXConfig setShortDrxCycleEnable:];
-[AWDMETRICSCellularPowerLogLTECDRXConfig setSubsId:];
-[AWDMETRICSCellularPowerLogLTECDRXConfig shortDrxCycle];
-[AWDMETRICSCellularPowerLogLTECDRXConfig shortDrxCycleEnable];
-[AWDMETRICSCellularPowerLogLTECDRXConfig subsId];
```
