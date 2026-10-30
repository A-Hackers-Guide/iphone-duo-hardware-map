# `AWDMETRICSKCellularPowerLogLteRrcStateChange`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 8 instance variables, 14 properties, 43 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
i _cause;
i _prevState;
I _prevStateDurMs;
i _state;
I _subsId;
B _isDataPreferred;
{?="timestamp"b1"cause"b1"prevState"b1"prevStateDurMs"b1"state"b1"subsId"b1"isDataPreferred"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
@property (TB,N) hasState;
@property (Ti,N,V_state) state;
@property (TB,N) hasPrevState;
@property (Ti,N,V_prevState) prevState;
@property (TB,N) hasPrevStateDurMs;
@property (TI,N,V_prevStateDurMs) prevStateDurMs;
@property (TB,N) hasCause;
@property (Ti,N,V_cause) cause;
@property (TB,N) hasIsDataPreferred;
@property (TB,N,V_isDataPreferred) isDataPreferred;
```

## Instance methods

```
-[AWDMETRICSKCellularPowerLogLteRrcStateChange hasTimestamp];
-[AWDMETRICSKCellularPowerLogLteRrcStateChange setHasTimestamp:];
-[AWDMETRICSKCellularPowerLogLteRrcStateChange setTimestamp:];
-[AWDMETRICSKCellularPowerLogLteRrcStateChange writeTo:];
-[AWDMETRICSKCellularPowerLogLteRrcStateChange setState:];
-[AWDMETRICSKCellularPowerLogLteRrcStateChange mergeFrom:];
-[AWDMETRICSKCellularPowerLogLteRrcStateChange timestamp];
-[AWDMETRICSKCellularPowerLogLteRrcStateChange stateAsString:];
-[AWDMETRICSKCellularPowerLogLteRrcStateChange StringAsState:];
-[AWDMETRICSKCellularPowerLogLteRrcStateChange hasState];
-[AWDMETRICSKCellularPowerLogLteRrcStateChange hash];
-[AWDMETRICSKCellularPowerLogLteRrcStateChange copyTo:];
-[AWDMETRICSKCellularPowerLogLteRrcStateChange description];
-[AWDMETRICSKCellularPowerLogLteRrcStateChange readFrom:];
-[AWDMETRICSKCellularPowerLogLteRrcStateChange copyWithZone:];
-[AWDMETRICSKCellularPowerLogLteRrcStateChange setHasState:];
-[AWDMETRICSKCellularPowerLogLteRrcStateChange isEqual:];
-[AWDMETRICSKCellularPowerLogLteRrcStateChange state];
-[AWDMETRICSKCellularPowerLogLteRrcStateChange dictionaryRepresentation];
-[AWDMETRICSKCellularPowerLogLteRrcStateChange cause];
-[AWDMETRICSKCellularPowerLogLteRrcStateChange setCause:];
-[AWDMETRICSKCellularPowerLogLteRrcStateChange isDataPreferred];
-[AWDMETRICSKCellularPowerLogLteRrcStateChange StringAsCause:];
-[AWDMETRICSKCellularPowerLogLteRrcStateChange StringAsPrevState:];
-[AWDMETRICSKCellularPowerLogLteRrcStateChange causeAsString:];
-[AWDMETRICSKCellularPowerLogLteRrcStateChange hasCause];
-[AWDMETRICSKCellularPowerLogLteRrcStateChange hasIsDataPreferred];
-[AWDMETRICSKCellularPowerLogLteRrcStateChange hasPrevState];
-[AWDMETRICSKCellularPowerLogLteRrcStateChange hasPrevStateDurMs];
-[AWDMETRICSKCellularPowerLogLteRrcStateChange hasSubsId];
-[AWDMETRICSKCellularPowerLogLteRrcStateChange prevState];
-[AWDMETRICSKCellularPowerLogLteRrcStateChange prevStateAsString:];
-[AWDMETRICSKCellularPowerLogLteRrcStateChange prevStateDurMs];
-[AWDMETRICSKCellularPowerLogLteRrcStateChange setHasCause:];
-[AWDMETRICSKCellularPowerLogLteRrcStateChange setHasIsDataPreferred:];
-[AWDMETRICSKCellularPowerLogLteRrcStateChange setHasPrevState:];
-[AWDMETRICSKCellularPowerLogLteRrcStateChange setHasPrevStateDurMs:];
-[AWDMETRICSKCellularPowerLogLteRrcStateChange setHasSubsId:];
-[AWDMETRICSKCellularPowerLogLteRrcStateChange setIsDataPreferred:];
-[AWDMETRICSKCellularPowerLogLteRrcStateChange setPrevState:];
-[AWDMETRICSKCellularPowerLogLteRrcStateChange setPrevStateDurMs:];
-[AWDMETRICSKCellularPowerLogLteRrcStateChange setSubsId:];
-[AWDMETRICSKCellularPowerLogLteRrcStateChange subsId];
```
