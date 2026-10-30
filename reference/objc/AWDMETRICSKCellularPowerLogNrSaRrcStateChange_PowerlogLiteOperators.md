# `AWDMETRICSKCellularPowerLogNrSaRrcStateChange`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 10 instance variables, 18 properties, 55 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
I _band;
i _cause;
i _deployment;
i _fr;
i _prevState;
I _prevStateDurMs;
i _state;
I _subsId;
{?="timestamp"b1"band"b1"cause"b1"deployment"b1"fr"b1"prevState"b1"prevStateDurMs"b1"state"b1"subsId"b1} _has;
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
@property (TB,N) hasBand;
@property (TI,N,V_band) band;
@property (TB,N) hasDeployment;
@property (Ti,N,V_deployment) deployment;
```

## Instance methods

```
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange hasTimestamp];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange setHasTimestamp:];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange setTimestamp:];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange writeTo:];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange setState:];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange mergeFrom:];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange timestamp];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange band];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange stateAsString:];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange StringAsState:];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange hasState];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange setBand:];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange hash];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange copyTo:];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange description];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange readFrom:];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange copyWithZone:];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange setHasState:];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange isEqual:];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange state];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange dictionaryRepresentation];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange deployment];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange hasBand];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange setHasBand:];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange hasDeployment];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange setDeployment:];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange setHasDeployment:];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange cause];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange setCause:];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange StringAsDeployment:];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange StringAsFr:];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange StringAsCause:];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange StringAsPrevState:];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange causeAsString:];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange deploymentAsString:];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange fr];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange frAsString:];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange hasCause];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange hasFr];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange hasPrevState];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange hasPrevStateDurMs];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange hasSubsId];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange prevState];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange prevStateAsString:];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange prevStateDurMs];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange setFr:];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange setHasCause:];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange setHasFr:];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange setHasPrevState:];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange setHasPrevStateDurMs:];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange setHasSubsId:];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange setPrevState:];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange setPrevStateDurMs:];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange setSubsId:];
-[AWDMETRICSKCellularPowerLogNrSaRrcStateChange subsId];
```
