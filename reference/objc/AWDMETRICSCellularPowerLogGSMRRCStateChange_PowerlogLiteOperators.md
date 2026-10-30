# `AWDMETRICSCellularPowerLogGSMRRCStateChange`

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
-[AWDMETRICSCellularPowerLogGSMRRCStateChange hasTimestamp];
-[AWDMETRICSCellularPowerLogGSMRRCStateChange setHasTimestamp:];
-[AWDMETRICSCellularPowerLogGSMRRCStateChange setTimestamp:];
-[AWDMETRICSCellularPowerLogGSMRRCStateChange writeTo:];
-[AWDMETRICSCellularPowerLogGSMRRCStateChange setState:];
-[AWDMETRICSCellularPowerLogGSMRRCStateChange mergeFrom:];
-[AWDMETRICSCellularPowerLogGSMRRCStateChange timestamp];
-[AWDMETRICSCellularPowerLogGSMRRCStateChange stateAsString:];
-[AWDMETRICSCellularPowerLogGSMRRCStateChange StringAsState:];
-[AWDMETRICSCellularPowerLogGSMRRCStateChange hasState];
-[AWDMETRICSCellularPowerLogGSMRRCStateChange hash];
-[AWDMETRICSCellularPowerLogGSMRRCStateChange copyTo:];
-[AWDMETRICSCellularPowerLogGSMRRCStateChange description];
-[AWDMETRICSCellularPowerLogGSMRRCStateChange readFrom:];
-[AWDMETRICSCellularPowerLogGSMRRCStateChange copyWithZone:];
-[AWDMETRICSCellularPowerLogGSMRRCStateChange setHasState:];
-[AWDMETRICSCellularPowerLogGSMRRCStateChange isEqual:];
-[AWDMETRICSCellularPowerLogGSMRRCStateChange state];
-[AWDMETRICSCellularPowerLogGSMRRCStateChange dictionaryRepresentation];
-[AWDMETRICSCellularPowerLogGSMRRCStateChange cause];
-[AWDMETRICSCellularPowerLogGSMRRCStateChange setCause:];
-[AWDMETRICSCellularPowerLogGSMRRCStateChange StringAsCause:];
-[AWDMETRICSCellularPowerLogGSMRRCStateChange StringAsPrevState:];
-[AWDMETRICSCellularPowerLogGSMRRCStateChange causeAsString:];
-[AWDMETRICSCellularPowerLogGSMRRCStateChange hasCause];
-[AWDMETRICSCellularPowerLogGSMRRCStateChange hasPrevState];
-[AWDMETRICSCellularPowerLogGSMRRCStateChange hasPrevStateDurMs];
-[AWDMETRICSCellularPowerLogGSMRRCStateChange hasSubsId];
-[AWDMETRICSCellularPowerLogGSMRRCStateChange prevState];
-[AWDMETRICSCellularPowerLogGSMRRCStateChange prevStateAsString:];
-[AWDMETRICSCellularPowerLogGSMRRCStateChange prevStateDurMs];
-[AWDMETRICSCellularPowerLogGSMRRCStateChange setHasCause:];
-[AWDMETRICSCellularPowerLogGSMRRCStateChange setHasPrevState:];
-[AWDMETRICSCellularPowerLogGSMRRCStateChange setHasPrevStateDurMs:];
-[AWDMETRICSCellularPowerLogGSMRRCStateChange setHasSubsId:];
-[AWDMETRICSCellularPowerLogGSMRRCStateChange setPrevState:];
-[AWDMETRICSCellularPowerLogGSMRRCStateChange setPrevStateDurMs:];
-[AWDMETRICSCellularPowerLogGSMRRCStateChange setSubsId:];
-[AWDMETRICSCellularPowerLogGSMRRCStateChange subsId];
```
