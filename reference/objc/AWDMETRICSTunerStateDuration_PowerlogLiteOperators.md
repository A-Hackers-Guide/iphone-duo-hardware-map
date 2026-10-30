# `AWDMETRICSTunerStateDuration`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 8 instance variables, 14 properties, 43 instance methods, 0 class methods

## Instance variables

```
I _duration;
I _ftQualInd;
I _port;
i _rat;
i _scenarioDecision;
i _txBand;
I _workMode;
{?="duration"b1"ftQualInd"b1"port"b1"rat"b1"scenarioDecision"b1"txBand"b1"workMode"b1} _has;
```

## Properties

```
@property (TB,N) hasRat;
@property (Ti,N,V_rat) rat;
@property (TB,N) hasTxBand;
@property (Ti,N,V_txBand) txBand;
@property (TB,N) hasPort;
@property (TI,N,V_port) port;
@property (TB,N) hasScenarioDecision;
@property (Ti,N,V_scenarioDecision) scenarioDecision;
@property (TB,N) hasDuration;
@property (TI,N,V_duration) duration;
@property (TB,N) hasWorkMode;
@property (TI,N,V_workMode) workMode;
@property (TB,N) hasFtQualInd;
@property (TI,N,V_ftQualInd) ftQualInd;
```

## Instance methods

```
-[AWDMETRICSTunerStateDuration setPort:];
-[AWDMETRICSTunerStateDuration writeTo:];
-[AWDMETRICSTunerStateDuration mergeFrom:];
-[AWDMETRICSTunerStateDuration hasDuration];
-[AWDMETRICSTunerStateDuration rat];
-[AWDMETRICSTunerStateDuration duration];
-[AWDMETRICSTunerStateDuration setHasDuration:];
-[AWDMETRICSTunerStateDuration port];
-[AWDMETRICSTunerStateDuration hash];
-[AWDMETRICSTunerStateDuration copyTo:];
-[AWDMETRICSTunerStateDuration description];
-[AWDMETRICSTunerStateDuration setDuration:];
-[AWDMETRICSTunerStateDuration readFrom:];
-[AWDMETRICSTunerStateDuration copyWithZone:];
-[AWDMETRICSTunerStateDuration isEqual:];
-[AWDMETRICSTunerStateDuration dictionaryRepresentation];
-[AWDMETRICSTunerStateDuration setRat:];
-[AWDMETRICSTunerStateDuration hasPort];
-[AWDMETRICSTunerStateDuration hasRat];
-[AWDMETRICSTunerStateDuration setHasPort:];
-[AWDMETRICSTunerStateDuration setHasRat:];
-[AWDMETRICSTunerStateDuration StringAsTxBand:];
-[AWDMETRICSTunerStateDuration StringAsRat:];
-[AWDMETRICSTunerStateDuration setHasWorkMode:];
-[AWDMETRICSTunerStateDuration StringAsScenarioDecision:];
-[AWDMETRICSTunerStateDuration txBandAsString:];
-[AWDMETRICSTunerStateDuration ftQualInd];
-[AWDMETRICSTunerStateDuration hasFtQualInd];
-[AWDMETRICSTunerStateDuration hasScenarioDecision];
-[AWDMETRICSTunerStateDuration hasTxBand];
-[AWDMETRICSTunerStateDuration hasWorkMode];
-[AWDMETRICSTunerStateDuration ratAsString:];
-[AWDMETRICSTunerStateDuration scenarioDecision];
-[AWDMETRICSTunerStateDuration scenarioDecisionAsString:];
-[AWDMETRICSTunerStateDuration setFtQualInd:];
-[AWDMETRICSTunerStateDuration setHasFtQualInd:];
-[AWDMETRICSTunerStateDuration setHasScenarioDecision:];
-[AWDMETRICSTunerStateDuration setHasTxBand:];
-[AWDMETRICSTunerStateDuration setScenarioDecision:];
-[AWDMETRICSTunerStateDuration setTxBand:];
-[AWDMETRICSTunerStateDuration setWorkMode:];
-[AWDMETRICSTunerStateDuration txBand];
-[AWDMETRICSTunerStateDuration workMode];
```
