# `AWDMETRICSKCellularPowerLogWcdmaRrcStateChange`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 9 instance variables, 16 properties, 49 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
i _connState;
i _establishmentCause;
i _prevConnState;
I _prevDurMs;
i _releaseCause;
I _subsId;
B _isDataPreferred;
{?="timestamp"b1"connState"b1"establishmentCause"b1"prevConnState"b1"prevDurMs"b1"releaseCause"b1"subsId"b1"isDataPreferred"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
@property (TB,N) hasConnState;
@property (Ti,N,V_connState) connState;
@property (TB,N) hasPrevConnState;
@property (Ti,N,V_prevConnState) prevConnState;
@property (TB,N) hasPrevDurMs;
@property (TI,N,V_prevDurMs) prevDurMs;
@property (TB,N) hasEstablishmentCause;
@property (Ti,N,V_establishmentCause) establishmentCause;
@property (TB,N) hasReleaseCause;
@property (Ti,N,V_releaseCause) releaseCause;
@property (TB,N) hasIsDataPreferred;
@property (TB,N,V_isDataPreferred) isDataPreferred;
```

## Instance methods

```
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange hasTimestamp];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange setHasTimestamp:];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange setTimestamp:];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange writeTo:];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange mergeFrom:];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange timestamp];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange hash];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange copyTo:];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange description];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange readFrom:];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange copyWithZone:];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange isEqual:];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange dictionaryRepresentation];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange StringAsConnState:];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange StringAsEstablishmentCause:];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange StringAsPrevConnState:];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange StringAsReleaseCause:];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange hasReleaseCause];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange isDataPreferred];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange connState];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange connStateAsString:];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange establishmentCause];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange establishmentCauseAsString:];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange hasConnState];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange hasEstablishmentCause];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange hasIsDataPreferred];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange hasPrevConnState];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange hasPrevDurMs];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange hasSubsId];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange prevConnState];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange prevConnStateAsString:];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange prevDurMs];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange releaseCause];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange releaseCauseAsString:];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange setConnState:];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange setEstablishmentCause:];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange setHasConnState:];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange setHasEstablishmentCause:];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange setHasIsDataPreferred:];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange setHasPrevConnState:];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange setHasPrevDurMs:];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange setHasReleaseCause:];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange setHasSubsId:];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange setIsDataPreferred:];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange setPrevConnState:];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange setPrevDurMs:];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange setReleaseCause:];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange setSubsId:];
-[AWDMETRICSKCellularPowerLogWcdmaRrcStateChange subsId];
```
