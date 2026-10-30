# `AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 12 instance variables, 22 properties, 67 instance methods, 0 class methods

## Instance variables

```
I _appliedDrxdMs;
i _bandGroup;
i _caIndex;
i _cellGroup;
i _deployment;
I _durationMs;
I _mcgCcNum;
i _mcgState;
i _rat;
i _rxDivState;
B _isEndc;
{?="appliedDrxdMs"b1"bandGroup"b1"caIndex"b1"cellGroup"b1"deployment"b1"durationMs"b1"mcgCcNum"b1"mcgState"b1"rat"b1"rxDivState"b1"isEndc"b1} _has;
```

## Properties

```
@property (TB,N) hasIsEndc;
@property (TB,N,V_isEndc) isEndc;
@property (TB,N) hasMcgState;
@property (Ti,N,V_mcgState) mcgState;
@property (TB,N) hasRat;
@property (Ti,N,V_rat) rat;
@property (TB,N) hasMcgCcNum;
@property (TI,N,V_mcgCcNum) mcgCcNum;
@property (TB,N) hasCaIndex;
@property (Ti,N,V_caIndex) caIndex;
@property (TB,N) hasRxDivState;
@property (Ti,N,V_rxDivState) rxDivState;
@property (TB,N) hasBandGroup;
@property (Ti,N,V_bandGroup) bandGroup;
@property (TB,N) hasDeployment;
@property (Ti,N,V_deployment) deployment;
@property (TB,N) hasCellGroup;
@property (Ti,N,V_cellGroup) cellGroup;
@property (TB,N) hasDurationMs;
@property (TI,N,V_durationMs) durationMs;
@property (TB,N) hasAppliedDrxdMs;
@property (TI,N,V_appliedDrxdMs) appliedDrxdMs;
```

## Instance methods

```
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin writeTo:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin mergeFrom:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin rat];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin hash];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin copyTo:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin description];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin readFrom:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin copyWithZone:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin isEqual:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin dictionaryRepresentation];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin deployment];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin durationMs];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin hasDurationMs];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin setDurationMs:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin setHasDurationMs:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin setRat:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin hasDeployment];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin hasRat];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin setDeployment:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin setHasDeployment:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin setHasRat:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin StringAsDeployment:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin StringAsMcgState:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin StringAsRat:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin caIndex];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin setHasMcgState:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin StringAsBandGroup:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin StringAsCaIndex:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin StringAsCellGroup:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin StringAsRxDivState:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin setHasMcgCcNum:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin appliedDrxdMs];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin bandGroup];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin bandGroupAsString:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin caIndexAsString:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin cellGroup];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin cellGroupAsString:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin deploymentAsString:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin hasAppliedDrxdMs];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin hasBandGroup];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin hasCaIndex];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin hasCellGroup];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin hasIsEndc];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin hasMcgCcNum];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin hasMcgState];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin hasRxDivState];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin isEndc];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin mcgCcNum];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin mcgState];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin mcgStateAsString:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin ratAsString:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin rxDivState];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin rxDivStateAsString:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin setAppliedDrxdMs:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin setBandGroup:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin setCaIndex:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin setCellGroup:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin setHasAppliedDrxdMs:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin setHasBandGroup:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin setHasCaIndex:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin setHasCellGroup:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin setHasIsEndc:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin setHasRxDivState:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin setIsEndc:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin setMcgCcNum:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin setMcgState:];
-[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin setRxDivState:];
```
