# `AWDMETRICSKCellularPowerLogPowerEstimatorComponentPowerStats`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 7 instance variables, 12 properties, 35 instance methods, 0 class methods

## Instance variables

```
I _activeDurationMs;
I _avgActivePowerMw;
I _avgPowerMw;
i _component;
I _cumulatedEnergyMj;
I _peakPowerMw;
{?="activeDurationMs"b1"avgActivePowerMw"b1"avgPowerMw"b1"component"b1"cumulatedEnergyMj"b1"peakPowerMw"b1} _has;
```

## Properties

```
@property (TB,N) hasComponent;
@property (Ti,N,V_component) component;
@property (TB,N) hasAvgPowerMw;
@property (TI,N,V_avgPowerMw) avgPowerMw;
@property (TB,N) hasAvgActivePowerMw;
@property (TI,N,V_avgActivePowerMw) avgActivePowerMw;
@property (TB,N) hasPeakPowerMw;
@property (TI,N,V_peakPowerMw) peakPowerMw;
@property (TB,N) hasCumulatedEnergyMj;
@property (TI,N,V_cumulatedEnergyMj) cumulatedEnergyMj;
@property (TB,N) hasActiveDurationMs;
@property (TI,N,V_activeDurationMs) activeDurationMs;
```

## Instance methods

```
-[AWDMETRICSKCellularPowerLogPowerEstimatorComponentPowerStats writeTo:];
-[AWDMETRICSKCellularPowerLogPowerEstimatorComponentPowerStats mergeFrom:];
-[AWDMETRICSKCellularPowerLogPowerEstimatorComponentPowerStats component];
-[AWDMETRICSKCellularPowerLogPowerEstimatorComponentPowerStats hash];
-[AWDMETRICSKCellularPowerLogPowerEstimatorComponentPowerStats copyTo:];
-[AWDMETRICSKCellularPowerLogPowerEstimatorComponentPowerStats description];
-[AWDMETRICSKCellularPowerLogPowerEstimatorComponentPowerStats readFrom:];
-[AWDMETRICSKCellularPowerLogPowerEstimatorComponentPowerStats copyWithZone:];
-[AWDMETRICSKCellularPowerLogPowerEstimatorComponentPowerStats isEqual:];
-[AWDMETRICSKCellularPowerLogPowerEstimatorComponentPowerStats dictionaryRepresentation];
-[AWDMETRICSKCellularPowerLogPowerEstimatorComponentPowerStats setComponent:];
-[AWDMETRICSKCellularPowerLogPowerEstimatorComponentPowerStats hasComponent];
-[AWDMETRICSKCellularPowerLogPowerEstimatorComponentPowerStats setHasComponent:];
-[AWDMETRICSKCellularPowerLogPowerEstimatorComponentPowerStats setPeakPowerMw:];
-[AWDMETRICSKCellularPowerLogPowerEstimatorComponentPowerStats StringAsComponent:];
-[AWDMETRICSKCellularPowerLogPowerEstimatorComponentPowerStats activeDurationMs];
-[AWDMETRICSKCellularPowerLogPowerEstimatorComponentPowerStats avgActivePowerMw];
-[AWDMETRICSKCellularPowerLogPowerEstimatorComponentPowerStats avgPowerMw];
-[AWDMETRICSKCellularPowerLogPowerEstimatorComponentPowerStats componentAsString:];
-[AWDMETRICSKCellularPowerLogPowerEstimatorComponentPowerStats cumulatedEnergyMj];
-[AWDMETRICSKCellularPowerLogPowerEstimatorComponentPowerStats hasActiveDurationMs];
-[AWDMETRICSKCellularPowerLogPowerEstimatorComponentPowerStats hasAvgActivePowerMw];
-[AWDMETRICSKCellularPowerLogPowerEstimatorComponentPowerStats hasAvgPowerMw];
-[AWDMETRICSKCellularPowerLogPowerEstimatorComponentPowerStats hasCumulatedEnergyMj];
-[AWDMETRICSKCellularPowerLogPowerEstimatorComponentPowerStats hasPeakPowerMw];
-[AWDMETRICSKCellularPowerLogPowerEstimatorComponentPowerStats peakPowerMw];
-[AWDMETRICSKCellularPowerLogPowerEstimatorComponentPowerStats setActiveDurationMs:];
-[AWDMETRICSKCellularPowerLogPowerEstimatorComponentPowerStats setAvgActivePowerMw:];
-[AWDMETRICSKCellularPowerLogPowerEstimatorComponentPowerStats setAvgPowerMw:];
-[AWDMETRICSKCellularPowerLogPowerEstimatorComponentPowerStats setCumulatedEnergyMj:];
-[AWDMETRICSKCellularPowerLogPowerEstimatorComponentPowerStats setHasActiveDurationMs:];
-[AWDMETRICSKCellularPowerLogPowerEstimatorComponentPowerStats setHasAvgActivePowerMw:];
-[AWDMETRICSKCellularPowerLogPowerEstimatorComponentPowerStats setHasAvgPowerMw:];
-[AWDMETRICSKCellularPowerLogPowerEstimatorComponentPowerStats setHasCumulatedEnergyMj:];
-[AWDMETRICSKCellularPowerLogPowerEstimatorComponentPowerStats setHasPeakPowerMw:];
```
