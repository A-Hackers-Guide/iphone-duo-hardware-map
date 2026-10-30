# `AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 15 instance variables, 28 properties, 65 instance methods, 0 class methods

## Instance variables

```
I _drxSlotOffset;
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
B _cdrxEnable;
B _shortCycleEnable;
{?="drxSlotOffset"b1"harqRttTimerDl"b1"harqRttTimerUl"b1"inactivityTimerMs"b1"longCycle"b1"longCycleOffset"b1"onDurationTimerFraction"b1"onDurationTimerMs"b1"retransmissionTimerDl"b1"retransmissionTimerUl"b1"shortCycle"b1"shortCycleTimer"b1"cdrxEnable"b1"shortCycleEnable"b1} _has;
```

## Properties

```
@property (TB,N) hasCdrxEnable;
@property (TB,N,V_cdrxEnable) cdrxEnable;
@property (TB,N) hasHarqRttTimerDl;
@property (TI,N,V_harqRttTimerDl) harqRttTimerDl;
@property (TB,N) hasHarqRttTimerUl;
@property (TI,N,V_harqRttTimerUl) harqRttTimerUl;
@property (TB,N) hasDrxSlotOffset;
@property (TI,N,V_drxSlotOffset) drxSlotOffset;
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
@property (TB,N) hasShortCycleEnable;
@property (TB,N,V_shortCycleEnable) shortCycleEnable;
@property (TB,N) hasShortCycle;
@property (TI,N,V_shortCycle) shortCycle;
@property (TB,N) hasShortCycleTimer;
@property (TI,N,V_shortCycleTimer) shortCycleTimer;
```

## Instance methods

```
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup writeTo:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup mergeFrom:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup hash];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup copyTo:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup description];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup readFrom:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup copyWithZone:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup isEqual:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup dictionaryRepresentation];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup longCycleOffset];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup shortCycleTimer];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup cdrxEnable];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup drxSlotOffset];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup harqRttTimerDl];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup harqRttTimerUl];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup hasCdrxEnable];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup hasDrxSlotOffset];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup hasHarqRttTimerDl];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup hasHarqRttTimerUl];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup hasInactivityTimerMs];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup hasLongCycle];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup hasLongCycleOffset];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup hasOnDurationTimerFraction];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup hasOnDurationTimerMs];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup hasRetransmissionTimerDl];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup hasRetransmissionTimerUl];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup hasShortCycle];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup hasShortCycleEnable];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup hasShortCycleTimer];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup inactivityTimerMs];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup longCycle];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup onDurationTimerFraction];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup onDurationTimerMs];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup retransmissionTimerDl];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup retransmissionTimerUl];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup setCdrxEnable:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup setDrxSlotOffset:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup setHarqRttTimerDl:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup setHarqRttTimerUl:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup setHasCdrxEnable:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup setHasDrxSlotOffset:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup setHasHarqRttTimerDl:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup setHasHarqRttTimerUl:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup setHasInactivityTimerMs:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup setHasLongCycle:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup setHasLongCycleOffset:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup setHasOnDurationTimerFraction:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup setHasOnDurationTimerMs:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup setHasRetransmissionTimerDl:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup setHasRetransmissionTimerUl:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup setHasShortCycle:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup setHasShortCycleEnable:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup setHasShortCycleTimer:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup setInactivityTimerMs:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup setLongCycle:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup setLongCycleOffset:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup setOnDurationTimerFraction:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup setOnDurationTimerMs:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup setRetransmissionTimerDl:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup setRetransmissionTimerUl:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup setShortCycle:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup setShortCycleEnable:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup setShortCycleTimer:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup shortCycle];
-[AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup shortCycleEnable];
```
