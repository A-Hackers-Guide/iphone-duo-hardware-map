# `AWDMETRICSCellularPowerLog1xEVDORRCStateChange`

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
-[AWDMETRICSCellularPowerLog1xEVDORRCStateChange hasTimestamp];
-[AWDMETRICSCellularPowerLog1xEVDORRCStateChange setHasTimestamp:];
-[AWDMETRICSCellularPowerLog1xEVDORRCStateChange setTimestamp:];
-[AWDMETRICSCellularPowerLog1xEVDORRCStateChange writeTo:];
-[AWDMETRICSCellularPowerLog1xEVDORRCStateChange setState:];
-[AWDMETRICSCellularPowerLog1xEVDORRCStateChange mergeFrom:];
-[AWDMETRICSCellularPowerLog1xEVDORRCStateChange timestamp];
-[AWDMETRICSCellularPowerLog1xEVDORRCStateChange stateAsString:];
-[AWDMETRICSCellularPowerLog1xEVDORRCStateChange StringAsState:];
-[AWDMETRICSCellularPowerLog1xEVDORRCStateChange hasState];
-[AWDMETRICSCellularPowerLog1xEVDORRCStateChange hash];
-[AWDMETRICSCellularPowerLog1xEVDORRCStateChange copyTo:];
-[AWDMETRICSCellularPowerLog1xEVDORRCStateChange description];
-[AWDMETRICSCellularPowerLog1xEVDORRCStateChange readFrom:];
-[AWDMETRICSCellularPowerLog1xEVDORRCStateChange copyWithZone:];
-[AWDMETRICSCellularPowerLog1xEVDORRCStateChange setHasState:];
-[AWDMETRICSCellularPowerLog1xEVDORRCStateChange isEqual:];
-[AWDMETRICSCellularPowerLog1xEVDORRCStateChange state];
-[AWDMETRICSCellularPowerLog1xEVDORRCStateChange dictionaryRepresentation];
-[AWDMETRICSCellularPowerLog1xEVDORRCStateChange cause];
-[AWDMETRICSCellularPowerLog1xEVDORRCStateChange setCause:];
-[AWDMETRICSCellularPowerLog1xEVDORRCStateChange StringAsCause:];
-[AWDMETRICSCellularPowerLog1xEVDORRCStateChange StringAsPrevState:];
-[AWDMETRICSCellularPowerLog1xEVDORRCStateChange causeAsString:];
-[AWDMETRICSCellularPowerLog1xEVDORRCStateChange hasCause];
-[AWDMETRICSCellularPowerLog1xEVDORRCStateChange hasPrevState];
-[AWDMETRICSCellularPowerLog1xEVDORRCStateChange hasPrevStateDurMs];
-[AWDMETRICSCellularPowerLog1xEVDORRCStateChange hasSubsId];
-[AWDMETRICSCellularPowerLog1xEVDORRCStateChange prevState];
-[AWDMETRICSCellularPowerLog1xEVDORRCStateChange prevStateAsString:];
-[AWDMETRICSCellularPowerLog1xEVDORRCStateChange prevStateDurMs];
-[AWDMETRICSCellularPowerLog1xEVDORRCStateChange setHasCause:];
-[AWDMETRICSCellularPowerLog1xEVDORRCStateChange setHasPrevState:];
-[AWDMETRICSCellularPowerLog1xEVDORRCStateChange setHasPrevStateDurMs:];
-[AWDMETRICSCellularPowerLog1xEVDORRCStateChange setHasSubsId:];
-[AWDMETRICSCellularPowerLog1xEVDORRCStateChange setPrevState:];
-[AWDMETRICSCellularPowerLog1xEVDORRCStateChange setPrevStateDurMs:];
-[AWDMETRICSCellularPowerLog1xEVDORRCStateChange setSubsId:];
-[AWDMETRICSCellularPowerLog1xEVDORRCStateChange subsId];
```
