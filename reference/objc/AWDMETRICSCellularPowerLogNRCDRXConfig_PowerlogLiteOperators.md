# `AWDMETRICSCellularPowerLogNRCDRXConfig`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 18 instance variables, 34 properties, 79 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
I _drxSlotOffset;
i _fr;
I _harqRttTimerDl;
I _harqRttTimerUl;
I _inactivityTimerMs;
I _longCycle;
I _longCycleOffset;
I _onDurationTimerFraction;
I _onDurationTimerMs;
I _retransmissionTimerDl;
I _retransmissionTimerUl;
I _shortCycle;
I _shortCycleTimer;
I _subsId;
B _cdrxEnable;
B _shortCycleEnable;
{?="timestamp"b1"drxSlotOffset"b1"fr"b1"harqRttTimerDl"b1"harqRttTimerUl"b1"inactivityTimerMs"b1"longCycle"b1"longCycleOffset"b1"onDurationTimerFraction"b1"onDurationTimerMs"b1"retransmissionTimerDl"b1"retransmissionTimerUl"b1"shortCycle"b1"shortCycleTimer"b1"subsId"b1"cdrxEnable"b1"shortCycleEnable"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasCdrxEnable;
@property (TB,N,V_cdrxEnable) cdrxEnable;
@property (TB,N) hasHarqRttTimerDl;
@property (TI,N,V_harqRttTimerDl) harqRttTimerDl;
@property (TB,N) hasHarqRttTimerUl;
@property (TI,N,V_harqRttTimerUl) harqRttTimerUl;
@property (TB,N) hasDrxSlotOffset;
@property (TI,N,V_drxSlotOffset) drxSlotOffset;
@property (TB,N) hasShortCycleEnable;
@property (TB,N,V_shortCycleEnable) shortCycleEnable;
@property (TB,N) hasRetransmissionTimerDl;
@property (TI,N,V_retransmissionTimerDl) retransmissionTimerDl;
@property (TB,N) hasRetransmissionTimerUl;
@property (TI,N,V_retransmissionTimerUl) retransmissionTimerUl;
@property (TB,N) hasOnDurationTimerFraction;
@property (TI,N,V_onDurationTimerFraction) onDurationTimerFraction;
@property (TB,N) hasOnDurationTimerMs;
@property (TI,N,V_onDurationTimerMs) onDurationTimerMs;
@property (TB,N) hasInactivityTimerMs;
@property (TI,N,V_inactivityTimerMs) inactivityTimerMs;
@property (TB,N) hasLongCycle;
@property (TI,N,V_longCycle) longCycle;
@property (TB,N) hasLongCycleOffset;
@property (TI,N,V_longCycleOffset) longCycleOffset;
@property (TB,N) hasShortCycle;
@property (TI,N,V_shortCycle) shortCycle;
@property (TB,N) hasShortCycleTimer;
@property (TI,N,V_shortCycleTimer) shortCycleTimer;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
@property (TB,N) hasFr;
@property (Ti,N,V_fr) fr;
```

## Instance methods

```
-[AWDMETRICSCellularPowerLogNRCDRXConfig hasTimestamp];
-[AWDMETRICSCellularPowerLogNRCDRXConfig setHasTimestamp:];
-[AWDMETRICSCellularPowerLogNRCDRXConfig setTimestamp:];
-[AWDMETRICSCellularPowerLogNRCDRXConfig writeTo:];
-[AWDMETRICSCellularPowerLogNRCDRXConfig mergeFrom:];
-[AWDMETRICSCellularPowerLogNRCDRXConfig timestamp];
-[AWDMETRICSCellularPowerLogNRCDRXConfig hash];
-[AWDMETRICSCellularPowerLogNRCDRXConfig copyTo:];
-[AWDMETRICSCellularPowerLogNRCDRXConfig description];
-[AWDMETRICSCellularPowerLogNRCDRXConfig readFrom:];
-[AWDMETRICSCellularPowerLogNRCDRXConfig copyWithZone:];
-[AWDMETRICSCellularPowerLogNRCDRXConfig isEqual:];
-[AWDMETRICSCellularPowerLogNRCDRXConfig dictionaryRepresentation];
-[AWDMETRICSCellularPowerLogNRCDRXConfig StringAsFr:];
-[AWDMETRICSCellularPowerLogNRCDRXConfig longCycleOffset];
-[AWDMETRICSCellularPowerLogNRCDRXConfig shortCycleTimer];
-[AWDMETRICSCellularPowerLogNRCDRXConfig cdrxEnable];
-[AWDMETRICSCellularPowerLogNRCDRXConfig drxSlotOffset];
-[AWDMETRICSCellularPowerLogNRCDRXConfig fr];
-[AWDMETRICSCellularPowerLogNRCDRXConfig frAsString:];
-[AWDMETRICSCellularPowerLogNRCDRXConfig harqRttTimerDl];
-[AWDMETRICSCellularPowerLogNRCDRXConfig harqRttTimerUl];
-[AWDMETRICSCellularPowerLogNRCDRXConfig hasCdrxEnable];
-[AWDMETRICSCellularPowerLogNRCDRXConfig hasDrxSlotOffset];
-[AWDMETRICSCellularPowerLogNRCDRXConfig hasFr];
-[AWDMETRICSCellularPowerLogNRCDRXConfig hasHarqRttTimerDl];
-[AWDMETRICSCellularPowerLogNRCDRXConfig hasHarqRttTimerUl];
-[AWDMETRICSCellularPowerLogNRCDRXConfig hasInactivityTimerMs];
-[AWDMETRICSCellularPowerLogNRCDRXConfig hasLongCycle];
-[AWDMETRICSCellularPowerLogNRCDRXConfig hasLongCycleOffset];
-[AWDMETRICSCellularPowerLogNRCDRXConfig hasOnDurationTimerFraction];
-[AWDMETRICSCellularPowerLogNRCDRXConfig hasOnDurationTimerMs];
-[AWDMETRICSCellularPowerLogNRCDRXConfig hasRetransmissionTimerDl];
-[AWDMETRICSCellularPowerLogNRCDRXConfig hasRetransmissionTimerUl];
-[AWDMETRICSCellularPowerLogNRCDRXConfig hasShortCycle];
-[AWDMETRICSCellularPowerLogNRCDRXConfig hasShortCycleEnable];
-[AWDMETRICSCellularPowerLogNRCDRXConfig hasShortCycleTimer];
-[AWDMETRICSCellularPowerLogNRCDRXConfig hasSubsId];
-[AWDMETRICSCellularPowerLogNRCDRXConfig inactivityTimerMs];
-[AWDMETRICSCellularPowerLogNRCDRXConfig longCycle];
-[AWDMETRICSCellularPowerLogNRCDRXConfig onDurationTimerFraction];
-[AWDMETRICSCellularPowerLogNRCDRXConfig onDurationTimerMs];
-[AWDMETRICSCellularPowerLogNRCDRXConfig retransmissionTimerDl];
-[AWDMETRICSCellularPowerLogNRCDRXConfig retransmissionTimerUl];
-[AWDMETRICSCellularPowerLogNRCDRXConfig setCdrxEnable:];
-[AWDMETRICSCellularPowerLogNRCDRXConfig setDrxSlotOffset:];
-[AWDMETRICSCellularPowerLogNRCDRXConfig setFr:];
-[AWDMETRICSCellularPowerLogNRCDRXConfig setHarqRttTimerDl:];
-[AWDMETRICSCellularPowerLogNRCDRXConfig setHarqRttTimerUl:];
-[AWDMETRICSCellularPowerLogNRCDRXConfig setHasCdrxEnable:];
-[AWDMETRICSCellularPowerLogNRCDRXConfig setHasDrxSlotOffset:];
-[AWDMETRICSCellularPowerLogNRCDRXConfig setHasFr:];
-[AWDMETRICSCellularPowerLogNRCDRXConfig setHasHarqRttTimerDl:];
-[AWDMETRICSCellularPowerLogNRCDRXConfig setHasHarqRttTimerUl:];
-[AWDMETRICSCellularPowerLogNRCDRXConfig setHasInactivityTimerMs:];
-[AWDMETRICSCellularPowerLogNRCDRXConfig setHasLongCycle:];
-[AWDMETRICSCellularPowerLogNRCDRXConfig setHasLongCycleOffset:];
-[AWDMETRICSCellularPowerLogNRCDRXConfig setHasOnDurationTimerFraction:];
-[AWDMETRICSCellularPowerLogNRCDRXConfig setHasOnDurationTimerMs:];
-[AWDMETRICSCellularPowerLogNRCDRXConfig setHasRetransmissionTimerDl:];
-[AWDMETRICSCellularPowerLogNRCDRXConfig setHasRetransmissionTimerUl:];
-[AWDMETRICSCellularPowerLogNRCDRXConfig setHasShortCycle:];
-[AWDMETRICSCellularPowerLogNRCDRXConfig setHasShortCycleEnable:];
-[AWDMETRICSCellularPowerLogNRCDRXConfig setHasShortCycleTimer:];
-[AWDMETRICSCellularPowerLogNRCDRXConfig setHasSubsId:];
-[AWDMETRICSCellularPowerLogNRCDRXConfig setInactivityTimerMs:];
-[AWDMETRICSCellularPowerLogNRCDRXConfig setLongCycle:];
-[AWDMETRICSCellularPowerLogNRCDRXConfig setLongCycleOffset:];
-[AWDMETRICSCellularPowerLogNRCDRXConfig setOnDurationTimerFraction:];
-[AWDMETRICSCellularPowerLogNRCDRXConfig setOnDurationTimerMs:];
-[AWDMETRICSCellularPowerLogNRCDRXConfig setRetransmissionTimerDl:];
-[AWDMETRICSCellularPowerLogNRCDRXConfig setRetransmissionTimerUl:];
-[AWDMETRICSCellularPowerLogNRCDRXConfig setShortCycle:];
-[AWDMETRICSCellularPowerLogNRCDRXConfig setShortCycleEnable:];
-[AWDMETRICSCellularPowerLogNRCDRXConfig setShortCycleTimer:];
-[AWDMETRICSCellularPowerLogNRCDRXConfig setSubsId:];
-[AWDMETRICSCellularPowerLogNRCDRXConfig shortCycle];
-[AWDMETRICSCellularPowerLogNRCDRXConfig shortCycleEnable];
-[AWDMETRICSCellularPowerLogNRCDRXConfig subsId];
```
