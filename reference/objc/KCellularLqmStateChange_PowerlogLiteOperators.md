# `KCellularLqmStateChange`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 17 instance variables, 32 properties, 77 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
i _hiPowerEvent;
i _hiPowerExitReason;
I _lqmState;
i _lteRsrp;
i _lteRsrq;
i _lteRssi;
i _lteRssnr;
I _prevLqmState;
I _prevStateDurationSec;
I _prevSysMode;
i _sysMode;
i _wcdmaEcio;
i _wcdmaRscp;
B _isScreenOn;
B _prevIsScreenOn;
{?="timestamp"b1"hiPowerEvent"b1"hiPowerExitReason"b1"lqmState"b1"lteRsrp"b1"lteRsrq"b1"lteRssi"b1"lteRssnr"b1"prevLqmState"b1"prevStateDurationSec"b1"prevSysMode"b1"sysMode"b1"wcdmaEcio"b1"wcdmaRscp"b1"isScreenOn"b1"prevIsScreenOn"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasPrevStateDurationSec;
@property (TI,N,V_prevStateDurationSec) prevStateDurationSec;
@property (TB,N) hasLqmState;
@property (TI,N,V_lqmState) lqmState;
@property (TB,N) hasSysMode;
@property (Ti,N,V_sysMode) sysMode;
@property (TB,N) hasIsScreenOn;
@property (TB,N,V_isScreenOn) isScreenOn;
@property (TB,N) hasPrevLqmState;
@property (TI,N,V_prevLqmState) prevLqmState;
@property (TB,N) hasPrevSysMode;
@property (TI,N,V_prevSysMode) prevSysMode;
@property (TB,N) hasPrevIsScreenOn;
@property (TB,N,V_prevIsScreenOn) prevIsScreenOn;
@property (TB,N) hasHiPowerEvent;
@property (Ti,N,V_hiPowerEvent) hiPowerEvent;
@property (TB,N) hasHiPowerExitReason;
@property (Ti,N,V_hiPowerExitReason) hiPowerExitReason;
@property (TB,N) hasWcdmaEcio;
@property (Ti,N,V_wcdmaEcio) wcdmaEcio;
@property (TB,N) hasWcdmaRscp;
@property (Ti,N,V_wcdmaRscp) wcdmaRscp;
@property (TB,N) hasLteRssi;
@property (Ti,N,V_lteRssi) lteRssi;
@property (TB,N) hasLteRsrp;
@property (Ti,N,V_lteRsrp) lteRsrp;
@property (TB,N) hasLteRsrq;
@property (Ti,N,V_lteRsrq) lteRsrq;
@property (TB,N) hasLteRssnr;
@property (Ti,N,V_lteRssnr) lteRssnr;
```

## Instance methods

```
-[KCellularLqmStateChange isScreenOn];
-[KCellularLqmStateChange hasTimestamp];
-[KCellularLqmStateChange setHasTimestamp:];
-[KCellularLqmStateChange setTimestamp:];
-[KCellularLqmStateChange writeTo:];
-[KCellularLqmStateChange mergeFrom:];
-[KCellularLqmStateChange timestamp];
-[KCellularLqmStateChange hash];
-[KCellularLqmStateChange copyTo:];
-[KCellularLqmStateChange description];
-[KCellularLqmStateChange readFrom:];
-[KCellularLqmStateChange copyWithZone:];
-[KCellularLqmStateChange isEqual:];
-[KCellularLqmStateChange dictionaryRepresentation];
-[KCellularLqmStateChange StringAsHiPowerEvent:];
-[KCellularLqmStateChange hasPrevLqmState];
-[KCellularLqmStateChange lteRsrq];
-[KCellularLqmStateChange setHasLqmState:];
-[KCellularLqmStateChange setPrevSysMode:];
-[KCellularLqmStateChange sysMode];
-[KCellularLqmStateChange StringAsHiPowerExitReason:];
-[KCellularLqmStateChange hasHiPowerEvent];
-[KCellularLqmStateChange lteRsrp];
-[KCellularLqmStateChange lteRssi];
-[KCellularLqmStateChange setHasLteRssnr:];
-[KCellularLqmStateChange hasHiPowerExitReason];
-[KCellularLqmStateChange hasIsScreenOn];
-[KCellularLqmStateChange hasLqmState];
-[KCellularLqmStateChange hasLteRsrp];
-[KCellularLqmStateChange hasLteRsrq];
-[KCellularLqmStateChange hasLteRssi];
-[KCellularLqmStateChange hasLteRssnr];
-[KCellularLqmStateChange hasPrevIsScreenOn];
-[KCellularLqmStateChange hasPrevStateDurationSec];
-[KCellularLqmStateChange hasPrevSysMode];
-[KCellularLqmStateChange hasSysMode];
-[KCellularLqmStateChange hasWcdmaEcio];
-[KCellularLqmStateChange hasWcdmaRscp];
-[KCellularLqmStateChange hiPowerEvent];
-[KCellularLqmStateChange hiPowerEventAsString:];
-[KCellularLqmStateChange hiPowerExitReason];
-[KCellularLqmStateChange hiPowerExitReasonAsString:];
-[KCellularLqmStateChange lqmState];
-[KCellularLqmStateChange lteRssnr];
-[KCellularLqmStateChange prevIsScreenOn];
-[KCellularLqmStateChange prevLqmState];
-[KCellularLqmStateChange prevStateDurationSec];
-[KCellularLqmStateChange prevSysMode];
-[KCellularLqmStateChange setHasHiPowerEvent:];
-[KCellularLqmStateChange setHasHiPowerExitReason:];
-[KCellularLqmStateChange setHasIsScreenOn:];
-[KCellularLqmStateChange setHasLteRsrp:];
-[KCellularLqmStateChange setHasLteRsrq:];
-[KCellularLqmStateChange setHasLteRssi:];
-[KCellularLqmStateChange setHasPrevIsScreenOn:];
-[KCellularLqmStateChange setHasPrevLqmState:];
-[KCellularLqmStateChange setHasPrevStateDurationSec:];
-[KCellularLqmStateChange setHasPrevSysMode:];
-[KCellularLqmStateChange setHasSysMode:];
-[KCellularLqmStateChange setHasWcdmaEcio:];
-[KCellularLqmStateChange setHasWcdmaRscp:];
-[KCellularLqmStateChange setHiPowerEvent:];
-[KCellularLqmStateChange setHiPowerExitReason:];
-[KCellularLqmStateChange setIsScreenOn:];
-[KCellularLqmStateChange setLqmState:];
-[KCellularLqmStateChange setLteRsrp:];
-[KCellularLqmStateChange setLteRsrq:];
-[KCellularLqmStateChange setLteRssi:];
-[KCellularLqmStateChange setLteRssnr:];
-[KCellularLqmStateChange setPrevIsScreenOn:];
-[KCellularLqmStateChange setPrevLqmState:];
-[KCellularLqmStateChange setPrevStateDurationSec:];
-[KCellularLqmStateChange setSysMode:];
-[KCellularLqmStateChange setWcdmaEcio:];
-[KCellularLqmStateChange setWcdmaRscp:];
-[KCellularLqmStateChange wcdmaEcio];
-[KCellularLqmStateChange wcdmaRscp];
```
