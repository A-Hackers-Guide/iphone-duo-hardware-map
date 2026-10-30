# `AWDMETRICSKCellularRfTunerHistTunerStateDuration`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 9 instance variables, 16 properties, 49 instance methods, 0 class methods

## Instance variables

```
i _deviceMode;
I _duration;
I _ftQualInd;
I _port;
i _rat;
i _scenarioDecision;
i _txBand;
I _workMode;
{?="deviceMode"b1"duration"b1"ftQualInd"b1"port"b1"rat"b1"scenarioDecision"b1"txBand"b1"workMode"b1} _has;
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
@property (TB,N) hasDeviceMode;
@property (Ti,N,V_deviceMode) deviceMode;
@property (TB,N) hasFtQualInd;
@property (TI,N,V_ftQualInd) ftQualInd;
```

## Instance methods

```
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration setPort:];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration writeTo:];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration mergeFrom:];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration hasDuration];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration rat];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration duration];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration setHasDuration:];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration port];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration hash];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration copyTo:];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration description];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration setDuration:];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration readFrom:];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration copyWithZone:];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration isEqual:];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration dictionaryRepresentation];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration setRat:];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration hasPort];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration hasRat];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration setHasPort:];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration setHasRat:];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration StringAsDeviceMode:];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration deviceMode];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration deviceModeAsString:];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration hasDeviceMode];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration setDeviceMode:];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration setHasDeviceMode:];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration StringAsTxBand:];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration StringAsRat:];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration setHasWorkMode:];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration StringAsScenarioDecision:];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration txBandAsString:];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration ftQualInd];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration hasFtQualInd];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration hasScenarioDecision];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration hasTxBand];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration hasWorkMode];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration ratAsString:];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration scenarioDecision];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration scenarioDecisionAsString:];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration setFtQualInd:];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration setHasFtQualInd:];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration setHasScenarioDecision:];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration setHasTxBand:];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration setScenarioDecision:];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration setTxBand:];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration setWorkMode:];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration txBand];
-[AWDMETRICSKCellularRfTunerHistTunerStateDuration workMode];
```
