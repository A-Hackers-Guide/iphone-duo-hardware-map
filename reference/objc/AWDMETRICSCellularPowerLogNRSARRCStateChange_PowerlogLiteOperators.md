# `AWDMETRICSCellularPowerLogNRSARRCStateChange`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 8 instance variables, 14 properties, 45 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
i _cause;
i _fr;
i _prevState;
I _prevStateDurMs;
i _state;
I _subsId;
{?="timestamp"b1"cause"b1"fr"b1"prevState"b1"prevStateDurMs"b1"state"b1"subsId"b1} _has;
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
@property (TB,N) hasFr;
@property (Ti,N,V_fr) fr;
```

## Instance methods

```
-[AWDMETRICSCellularPowerLogNRSARRCStateChange hasTimestamp];
-[AWDMETRICSCellularPowerLogNRSARRCStateChange setHasTimestamp:];
-[AWDMETRICSCellularPowerLogNRSARRCStateChange setTimestamp:];
-[AWDMETRICSCellularPowerLogNRSARRCStateChange writeTo:];
-[AWDMETRICSCellularPowerLogNRSARRCStateChange setState:];
-[AWDMETRICSCellularPowerLogNRSARRCStateChange mergeFrom:];
-[AWDMETRICSCellularPowerLogNRSARRCStateChange timestamp];
-[AWDMETRICSCellularPowerLogNRSARRCStateChange stateAsString:];
-[AWDMETRICSCellularPowerLogNRSARRCStateChange StringAsState:];
-[AWDMETRICSCellularPowerLogNRSARRCStateChange hasState];
-[AWDMETRICSCellularPowerLogNRSARRCStateChange hash];
-[AWDMETRICSCellularPowerLogNRSARRCStateChange copyTo:];
-[AWDMETRICSCellularPowerLogNRSARRCStateChange description];
-[AWDMETRICSCellularPowerLogNRSARRCStateChange readFrom:];
-[AWDMETRICSCellularPowerLogNRSARRCStateChange copyWithZone:];
-[AWDMETRICSCellularPowerLogNRSARRCStateChange setHasState:];
-[AWDMETRICSCellularPowerLogNRSARRCStateChange isEqual:];
-[AWDMETRICSCellularPowerLogNRSARRCStateChange state];
-[AWDMETRICSCellularPowerLogNRSARRCStateChange dictionaryRepresentation];
-[AWDMETRICSCellularPowerLogNRSARRCStateChange cause];
-[AWDMETRICSCellularPowerLogNRSARRCStateChange setCause:];
-[AWDMETRICSCellularPowerLogNRSARRCStateChange StringAsFr:];
-[AWDMETRICSCellularPowerLogNRSARRCStateChange StringAsCause:];
-[AWDMETRICSCellularPowerLogNRSARRCStateChange StringAsPrevState:];
-[AWDMETRICSCellularPowerLogNRSARRCStateChange causeAsString:];
-[AWDMETRICSCellularPowerLogNRSARRCStateChange fr];
-[AWDMETRICSCellularPowerLogNRSARRCStateChange frAsString:];
-[AWDMETRICSCellularPowerLogNRSARRCStateChange hasCause];
-[AWDMETRICSCellularPowerLogNRSARRCStateChange hasFr];
-[AWDMETRICSCellularPowerLogNRSARRCStateChange hasPrevState];
-[AWDMETRICSCellularPowerLogNRSARRCStateChange hasPrevStateDurMs];
-[AWDMETRICSCellularPowerLogNRSARRCStateChange hasSubsId];
-[AWDMETRICSCellularPowerLogNRSARRCStateChange prevState];
-[AWDMETRICSCellularPowerLogNRSARRCStateChange prevStateAsString:];
-[AWDMETRICSCellularPowerLogNRSARRCStateChange prevStateDurMs];
-[AWDMETRICSCellularPowerLogNRSARRCStateChange setFr:];
-[AWDMETRICSCellularPowerLogNRSARRCStateChange setHasCause:];
-[AWDMETRICSCellularPowerLogNRSARRCStateChange setHasFr:];
-[AWDMETRICSCellularPowerLogNRSARRCStateChange setHasPrevState:];
-[AWDMETRICSCellularPowerLogNRSARRCStateChange setHasPrevStateDurMs:];
-[AWDMETRICSCellularPowerLogNRSARRCStateChange setHasSubsId:];
-[AWDMETRICSCellularPowerLogNRSARRCStateChange setPrevState:];
-[AWDMETRICSCellularPowerLogNRSARRCStateChange setPrevStateDurMs:];
-[AWDMETRICSCellularPowerLogNRSARRCStateChange setSubsId:];
-[AWDMETRICSCellularPowerLogNRSARRCStateChange subsId];
```
