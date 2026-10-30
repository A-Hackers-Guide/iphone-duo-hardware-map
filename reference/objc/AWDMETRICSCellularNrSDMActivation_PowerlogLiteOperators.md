# `AWDMETRICSCellularNrSDMActivation`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 16 instance variables, 30 properties, 85 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
i _currentRat;
i _deployment;
I _durationInPrevState;
i _fr;
i _newState;
i _prevRat;
i _prevTriggerCause;
i _saVerdict;
I _subsId;
i _triggerCause;
B _apNrRecomm;
B _apNrRecommConfFactor;
B _fr1MeasDisabled;
B _fr2MeasDisabled;
{?="timestamp"b1"currentRat"b1"deployment"b1"durationInPrevState"b1"fr"b1"newState"b1"prevRat"b1"prevTriggerCause"b1"saVerdict"b1"subsId"b1"triggerCause"b1"apNrRecomm"b1"apNrRecommConfFactor"b1"fr1MeasDisabled"b1"fr2MeasDisabled"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasDeployment;
@property (Ti,N,V_deployment) deployment;
@property (TB,N) hasFr1MeasDisabled;
@property (TB,N,V_fr1MeasDisabled) fr1MeasDisabled;
@property (TB,N) hasFr2MeasDisabled;
@property (TB,N,V_fr2MeasDisabled) fr2MeasDisabled;
@property (TB,N) hasTriggerCause;
@property (Ti,N,V_triggerCause) triggerCause;
@property (TB,N) hasPrevTriggerCause;
@property (Ti,N,V_prevTriggerCause) prevTriggerCause;
@property (TB,N) hasApNrRecomm;
@property (TB,N,V_apNrRecomm) apNrRecomm;
@property (TB,N) hasApNrRecommConfFactor;
@property (TB,N,V_apNrRecommConfFactor) apNrRecommConfFactor;
@property (TB,N) hasDurationInPrevState;
@property (TI,N,V_durationInPrevState) durationInPrevState;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
@property (TB,N) hasFr;
@property (Ti,N,V_fr) fr;
@property (TB,N) hasPrevRat;
@property (Ti,N,V_prevRat) prevRat;
@property (TB,N) hasCurrentRat;
@property (Ti,N,V_currentRat) currentRat;
@property (TB,N) hasNewState;
@property (Ti,N,V_newState) newState;
@property (TB,N) hasSaVerdict;
@property (Ti,N,V_saVerdict) saVerdict;
```

## Instance methods

```
-[AWDMETRICSCellularNrSDMActivation hasTimestamp];
-[AWDMETRICSCellularNrSDMActivation setHasTimestamp:];
-[AWDMETRICSCellularNrSDMActivation setTimestamp:];
-[AWDMETRICSCellularNrSDMActivation writeTo:];
-[AWDMETRICSCellularNrSDMActivation mergeFrom:];
-[AWDMETRICSCellularNrSDMActivation timestamp];
-[AWDMETRICSCellularNrSDMActivation hash];
-[AWDMETRICSCellularNrSDMActivation copyTo:];
-[AWDMETRICSCellularNrSDMActivation description];
-[AWDMETRICSCellularNrSDMActivation readFrom:];
-[AWDMETRICSCellularNrSDMActivation copyWithZone:];
-[AWDMETRICSCellularNrSDMActivation isEqual:];
-[AWDMETRICSCellularNrSDMActivation dictionaryRepresentation];
-[AWDMETRICSCellularNrSDMActivation deployment];
-[AWDMETRICSCellularNrSDMActivation newState];
-[AWDMETRICSCellularNrSDMActivation hasDeployment];
-[AWDMETRICSCellularNrSDMActivation setDeployment:];
-[AWDMETRICSCellularNrSDMActivation setHasDeployment:];
-[AWDMETRICSCellularNrSDMActivation hasNewState];
-[AWDMETRICSCellularNrSDMActivation setNewState:];
-[AWDMETRICSCellularNrSDMActivation StringAsDeployment:];
-[AWDMETRICSCellularNrSDMActivation StringAsFr:];
-[AWDMETRICSCellularNrSDMActivation StringAsPrevRat:];
-[AWDMETRICSCellularNrSDMActivation StringAsPrevTriggerCause:];
-[AWDMETRICSCellularNrSDMActivation StringAsSaVerdict:];
-[AWDMETRICSCellularNrSDMActivation fr1MeasDisabled];
-[AWDMETRICSCellularNrSDMActivation hasTriggerCause];
-[AWDMETRICSCellularNrSDMActivation StringAsCurrentRat:];
-[AWDMETRICSCellularNrSDMActivation StringAsNewState:];
-[AWDMETRICSCellularNrSDMActivation StringAsTriggerCause:];
-[AWDMETRICSCellularNrSDMActivation fr2MeasDisabled];
-[AWDMETRICSCellularNrSDMActivation prevRat];
-[AWDMETRICSCellularNrSDMActivation setHasNewState:];
-[AWDMETRICSCellularNrSDMActivation apNrRecomm];
-[AWDMETRICSCellularNrSDMActivation apNrRecommConfFactor];
-[AWDMETRICSCellularNrSDMActivation currentRat];
-[AWDMETRICSCellularNrSDMActivation currentRatAsString:];
-[AWDMETRICSCellularNrSDMActivation deploymentAsString:];
-[AWDMETRICSCellularNrSDMActivation durationInPrevState];
-[AWDMETRICSCellularNrSDMActivation fr];
-[AWDMETRICSCellularNrSDMActivation frAsString:];
-[AWDMETRICSCellularNrSDMActivation hasApNrRecomm];
-[AWDMETRICSCellularNrSDMActivation hasApNrRecommConfFactor];
-[AWDMETRICSCellularNrSDMActivation hasCurrentRat];
-[AWDMETRICSCellularNrSDMActivation hasDurationInPrevState];
-[AWDMETRICSCellularNrSDMActivation hasFr];
-[AWDMETRICSCellularNrSDMActivation hasFr1MeasDisabled];
-[AWDMETRICSCellularNrSDMActivation hasFr2MeasDisabled];
-[AWDMETRICSCellularNrSDMActivation hasPrevRat];
-[AWDMETRICSCellularNrSDMActivation hasPrevTriggerCause];
-[AWDMETRICSCellularNrSDMActivation hasSaVerdict];
-[AWDMETRICSCellularNrSDMActivation hasSubsId];
-[AWDMETRICSCellularNrSDMActivation newStateAsString:];
-[AWDMETRICSCellularNrSDMActivation prevRatAsString:];
-[AWDMETRICSCellularNrSDMActivation prevTriggerCause];
-[AWDMETRICSCellularNrSDMActivation prevTriggerCauseAsString:];
-[AWDMETRICSCellularNrSDMActivation saVerdict];
-[AWDMETRICSCellularNrSDMActivation saVerdictAsString:];
-[AWDMETRICSCellularNrSDMActivation setApNrRecomm:];
-[AWDMETRICSCellularNrSDMActivation setApNrRecommConfFactor:];
-[AWDMETRICSCellularNrSDMActivation setCurrentRat:];
-[AWDMETRICSCellularNrSDMActivation setDurationInPrevState:];
-[AWDMETRICSCellularNrSDMActivation setFr1MeasDisabled:];
-[AWDMETRICSCellularNrSDMActivation setFr2MeasDisabled:];
-[AWDMETRICSCellularNrSDMActivation setFr:];
-[AWDMETRICSCellularNrSDMActivation setHasApNrRecomm:];
-[AWDMETRICSCellularNrSDMActivation setHasApNrRecommConfFactor:];
-[AWDMETRICSCellularNrSDMActivation setHasCurrentRat:];
-[AWDMETRICSCellularNrSDMActivation setHasDurationInPrevState:];
-[AWDMETRICSCellularNrSDMActivation setHasFr1MeasDisabled:];
-[AWDMETRICSCellularNrSDMActivation setHasFr2MeasDisabled:];
-[AWDMETRICSCellularNrSDMActivation setHasFr:];
-[AWDMETRICSCellularNrSDMActivation setHasPrevRat:];
-[AWDMETRICSCellularNrSDMActivation setHasPrevTriggerCause:];
-[AWDMETRICSCellularNrSDMActivation setHasSaVerdict:];
-[AWDMETRICSCellularNrSDMActivation setHasSubsId:];
-[AWDMETRICSCellularNrSDMActivation setHasTriggerCause:];
-[AWDMETRICSCellularNrSDMActivation setPrevRat:];
-[AWDMETRICSCellularNrSDMActivation setPrevTriggerCause:];
-[AWDMETRICSCellularNrSDMActivation setSaVerdict:];
-[AWDMETRICSCellularNrSDMActivation setSubsId:];
-[AWDMETRICSCellularNrSDMActivation setTriggerCause:];
-[AWDMETRICSCellularNrSDMActivation subsId];
-[AWDMETRICSCellularNrSDMActivation triggerCause];
-[AWDMETRICSCellularNrSDMActivation triggerCauseAsString:];
```
