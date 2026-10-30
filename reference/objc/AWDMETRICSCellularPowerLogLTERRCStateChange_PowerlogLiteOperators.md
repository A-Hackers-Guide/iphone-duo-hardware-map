# `AWDMETRICSCellularPowerLogLTERRCStateChange`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 7 instance variables, 12 properties, 39 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
i _cause;
i _prevState;
I _prevStateDurMs;
i _state;
I _subsId;
{?="timestamp"b1"cause"b1"prevState"b1"prevStateDurMs"b1"state"b1"subsId"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasState;
@property (Ti,N,V_state) state;
@property (TB,N) hasPrevState;
@property (Ti,N,V_prevState) prevState;
@property (TB,N) hasPrevStateDurMs;
@property (TI,N,V_prevStateDurMs) prevStateDurMs;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
@property (TB,N) hasCause;
@property (Ti,N,V_cause) cause;
```

## Instance methods

```
-[AWDMETRICSCellularPowerLogLTERRCStateChange hasTimestamp];
-[AWDMETRICSCellularPowerLogLTERRCStateChange setHasTimestamp:];
-[AWDMETRICSCellularPowerLogLTERRCStateChange setTimestamp:];
-[AWDMETRICSCellularPowerLogLTERRCStateChange writeTo:];
-[AWDMETRICSCellularPowerLogLTERRCStateChange setState:];
-[AWDMETRICSCellularPowerLogLTERRCStateChange mergeFrom:];
-[AWDMETRICSCellularPowerLogLTERRCStateChange timestamp];
-[AWDMETRICSCellularPowerLogLTERRCStateChange stateAsString:];
-[AWDMETRICSCellularPowerLogLTERRCStateChange StringAsState:];
-[AWDMETRICSCellularPowerLogLTERRCStateChange hasState];
-[AWDMETRICSCellularPowerLogLTERRCStateChange hash];
-[AWDMETRICSCellularPowerLogLTERRCStateChange copyTo:];
-[AWDMETRICSCellularPowerLogLTERRCStateChange description];
-[AWDMETRICSCellularPowerLogLTERRCStateChange readFrom:];
-[AWDMETRICSCellularPowerLogLTERRCStateChange copyWithZone:];
-[AWDMETRICSCellularPowerLogLTERRCStateChange setHasState:];
-[AWDMETRICSCellularPowerLogLTERRCStateChange isEqual:];
-[AWDMETRICSCellularPowerLogLTERRCStateChange state];
-[AWDMETRICSCellularPowerLogLTERRCStateChange dictionaryRepresentation];
-[AWDMETRICSCellularPowerLogLTERRCStateChange cause];
-[AWDMETRICSCellularPowerLogLTERRCStateChange setCause:];
-[AWDMETRICSCellularPowerLogLTERRCStateChange StringAsCause:];
-[AWDMETRICSCellularPowerLogLTERRCStateChange StringAsPrevState:];
-[AWDMETRICSCellularPowerLogLTERRCStateChange causeAsString:];
-[AWDMETRICSCellularPowerLogLTERRCStateChange hasCause];
-[AWDMETRICSCellularPowerLogLTERRCStateChange hasPrevState];
-[AWDMETRICSCellularPowerLogLTERRCStateChange hasPrevStateDurMs];
-[AWDMETRICSCellularPowerLogLTERRCStateChange hasSubsId];
-[AWDMETRICSCellularPowerLogLTERRCStateChange prevState];
-[AWDMETRICSCellularPowerLogLTERRCStateChange prevStateAsString:];
-[AWDMETRICSCellularPowerLogLTERRCStateChange prevStateDurMs];
-[AWDMETRICSCellularPowerLogLTERRCStateChange setHasCause:];
-[AWDMETRICSCellularPowerLogLTERRCStateChange setHasPrevState:];
-[AWDMETRICSCellularPowerLogLTERRCStateChange setHasPrevStateDurMs:];
-[AWDMETRICSCellularPowerLogLTERRCStateChange setHasSubsId:];
-[AWDMETRICSCellularPowerLogLTERRCStateChange setPrevState:];
-[AWDMETRICSCellularPowerLogLTERRCStateChange setPrevStateDurMs:];
-[AWDMETRICSCellularPowerLogLTERRCStateChange setSubsId:];
-[AWDMETRICSCellularPowerLogLTERRCStateChange subsId];
```
