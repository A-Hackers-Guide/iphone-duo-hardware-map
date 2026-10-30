# `AWDMETRICSKCellularPowerLogSleepStatesMBin`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 7 instance variables, 12 properties, 41 instance methods, 0 class methods

## Instance variables

```
I _count;
i _deployment;
I _durationMs;
i _rat;
i _rrcState;
i _socSleepState;
{?="count"b1"deployment"b1"durationMs"b1"rat"b1"rrcState"b1"socSleepState"b1} _has;
```

## Properties

```
@property (TB,N) hasRat;
@property (Ti,N,V_rat) rat;
@property (TB,N) hasRrcState;
@property (Ti,N,V_rrcState) rrcState;
@property (TB,N) hasDeployment;
@property (Ti,N,V_deployment) deployment;
@property (TB,N) hasSocSleepState;
@property (Ti,N,V_socSleepState) socSleepState;
@property (TB,N) hasDurationMs;
@property (TI,N,V_durationMs) durationMs;
@property (TB,N) hasCount;
@property (TI,N,V_count) count;
```

## Instance methods

```
-[AWDMETRICSKCellularPowerLogSleepStatesMBin writeTo:];
-[AWDMETRICSKCellularPowerLogSleepStatesMBin setCount:];
-[AWDMETRICSKCellularPowerLogSleepStatesMBin mergeFrom:];
-[AWDMETRICSKCellularPowerLogSleepStatesMBin count];
-[AWDMETRICSKCellularPowerLogSleepStatesMBin rat];
-[AWDMETRICSKCellularPowerLogSleepStatesMBin hash];
-[AWDMETRICSKCellularPowerLogSleepStatesMBin copyTo:];
-[AWDMETRICSKCellularPowerLogSleepStatesMBin description];
-[AWDMETRICSKCellularPowerLogSleepStatesMBin readFrom:];
-[AWDMETRICSKCellularPowerLogSleepStatesMBin copyWithZone:];
-[AWDMETRICSKCellularPowerLogSleepStatesMBin isEqual:];
-[AWDMETRICSKCellularPowerLogSleepStatesMBin dictionaryRepresentation];
-[AWDMETRICSKCellularPowerLogSleepStatesMBin setHasRrcState:];
-[AWDMETRICSKCellularPowerLogSleepStatesMBin deployment];
-[AWDMETRICSKCellularPowerLogSleepStatesMBin hasCount];
-[AWDMETRICSKCellularPowerLogSleepStatesMBin hasRrcState];
-[AWDMETRICSKCellularPowerLogSleepStatesMBin rrcState];
-[AWDMETRICSKCellularPowerLogSleepStatesMBin setHasCount:];
-[AWDMETRICSKCellularPowerLogSleepStatesMBin durationMs];
-[AWDMETRICSKCellularPowerLogSleepStatesMBin hasDurationMs];
-[AWDMETRICSKCellularPowerLogSleepStatesMBin setDurationMs:];
-[AWDMETRICSKCellularPowerLogSleepStatesMBin setHasDurationMs:];
-[AWDMETRICSKCellularPowerLogSleepStatesMBin setRat:];
-[AWDMETRICSKCellularPowerLogSleepStatesMBin hasDeployment];
-[AWDMETRICSKCellularPowerLogSleepStatesMBin hasRat];
-[AWDMETRICSKCellularPowerLogSleepStatesMBin setDeployment:];
-[AWDMETRICSKCellularPowerLogSleepStatesMBin setHasDeployment:];
-[AWDMETRICSKCellularPowerLogSleepStatesMBin setHasRat:];
-[AWDMETRICSKCellularPowerLogSleepStatesMBin StringAsDeployment:];
-[AWDMETRICSKCellularPowerLogSleepStatesMBin StringAsRat:];
-[AWDMETRICSKCellularPowerLogSleepStatesMBin StringAsRrcState:];
-[AWDMETRICSKCellularPowerLogSleepStatesMBin StringAsSocSleepState:];
-[AWDMETRICSKCellularPowerLogSleepStatesMBin deploymentAsString:];
-[AWDMETRICSKCellularPowerLogSleepStatesMBin hasSocSleepState];
-[AWDMETRICSKCellularPowerLogSleepStatesMBin ratAsString:];
-[AWDMETRICSKCellularPowerLogSleepStatesMBin rrcStateAsString:];
-[AWDMETRICSKCellularPowerLogSleepStatesMBin setHasSocSleepState:];
-[AWDMETRICSKCellularPowerLogSleepStatesMBin setRrcState:];
-[AWDMETRICSKCellularPowerLogSleepStatesMBin setSocSleepState:];
-[AWDMETRICSKCellularPowerLogSleepStatesMBin socSleepState];
-[AWDMETRICSKCellularPowerLogSleepStatesMBin socSleepStateAsString:];
```
