# `AWDMETRICSKCellularPowerLogGsmRrcStateChange`

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
-[AWDMETRICSKCellularPowerLogGsmRrcStateChange hasTimestamp];
-[AWDMETRICSKCellularPowerLogGsmRrcStateChange setHasTimestamp:];
-[AWDMETRICSKCellularPowerLogGsmRrcStateChange setTimestamp:];
-[AWDMETRICSKCellularPowerLogGsmRrcStateChange writeTo:];
-[AWDMETRICSKCellularPowerLogGsmRrcStateChange setState:];
-[AWDMETRICSKCellularPowerLogGsmRrcStateChange mergeFrom:];
-[AWDMETRICSKCellularPowerLogGsmRrcStateChange timestamp];
-[AWDMETRICSKCellularPowerLogGsmRrcStateChange stateAsString:];
-[AWDMETRICSKCellularPowerLogGsmRrcStateChange StringAsState:];
-[AWDMETRICSKCellularPowerLogGsmRrcStateChange hasState];
-[AWDMETRICSKCellularPowerLogGsmRrcStateChange hash];
-[AWDMETRICSKCellularPowerLogGsmRrcStateChange copyTo:];
-[AWDMETRICSKCellularPowerLogGsmRrcStateChange description];
-[AWDMETRICSKCellularPowerLogGsmRrcStateChange readFrom:];
-[AWDMETRICSKCellularPowerLogGsmRrcStateChange copyWithZone:];
-[AWDMETRICSKCellularPowerLogGsmRrcStateChange setHasState:];
-[AWDMETRICSKCellularPowerLogGsmRrcStateChange isEqual:];
-[AWDMETRICSKCellularPowerLogGsmRrcStateChange state];
-[AWDMETRICSKCellularPowerLogGsmRrcStateChange dictionaryRepresentation];
-[AWDMETRICSKCellularPowerLogGsmRrcStateChange cause];
-[AWDMETRICSKCellularPowerLogGsmRrcStateChange setCause:];
-[AWDMETRICSKCellularPowerLogGsmRrcStateChange StringAsCause:];
-[AWDMETRICSKCellularPowerLogGsmRrcStateChange StringAsPrevState:];
-[AWDMETRICSKCellularPowerLogGsmRrcStateChange causeAsString:];
-[AWDMETRICSKCellularPowerLogGsmRrcStateChange hasCause];
-[AWDMETRICSKCellularPowerLogGsmRrcStateChange hasPrevState];
-[AWDMETRICSKCellularPowerLogGsmRrcStateChange hasPrevStateDurMs];
-[AWDMETRICSKCellularPowerLogGsmRrcStateChange hasSubsId];
-[AWDMETRICSKCellularPowerLogGsmRrcStateChange prevState];
-[AWDMETRICSKCellularPowerLogGsmRrcStateChange prevStateAsString:];
-[AWDMETRICSKCellularPowerLogGsmRrcStateChange prevStateDurMs];
-[AWDMETRICSKCellularPowerLogGsmRrcStateChange setHasCause:];
-[AWDMETRICSKCellularPowerLogGsmRrcStateChange setHasPrevState:];
-[AWDMETRICSKCellularPowerLogGsmRrcStateChange setHasPrevStateDurMs:];
-[AWDMETRICSKCellularPowerLogGsmRrcStateChange setHasSubsId:];
-[AWDMETRICSKCellularPowerLogGsmRrcStateChange setPrevState:];
-[AWDMETRICSKCellularPowerLogGsmRrcStateChange setPrevStateDurMs:];
-[AWDMETRICSKCellularPowerLogGsmRrcStateChange setSubsId:];
-[AWDMETRICSKCellularPowerLogGsmRrcStateChange subsId];
```
