# `AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 21 instance variables, 40 properties, 123 instance methods, 0 class methods

## Instance variables

```
i _axibr;
i _deployment;
i _dmdc0;
i _dmdc1;
i _dmdc2;
I _durationMs;
i _gala;
I _mcgAggregatedBw;
i _mcgDlCcActivated;
i _mcgDlCcConfigured;
i _mcgUlCcActivated;
i _mcgUlCcConfigured;
i _rflc;
I _scgAggregatedBw;
i _scgDlCcActivated;
i _scgDlCcConfigured;
i _scgUlCcActivated;
i _scgUlCcConfigured;
i _tdp;
i _uplink;
{?="axibr"b1"deployment"b1"dmdc0"b1"dmdc1"b1"dmdc2"b1"durationMs"b1"gala"b1"mcgAggregatedBw"b1"mcgDlCcActivated"b1"mcgDlCcConfigured"b1"mcgUlCcActivated"b1"mcgUlCcConfigured"b1"rflc"b1"scgAggregatedBw"b1"scgDlCcActivated"b1"scgDlCcConfigured"b1"scgUlCcActivated"b1"scgUlCcConfigured"b1"tdp"b1"uplink"b1} _has;
```

## Properties

```
@property (TB,N) hasTdp;
@property (Ti,N,V_tdp) tdp;
@property (TB,N) hasDmdc0;
@property (Ti,N,V_dmdc0) dmdc0;
@property (TB,N) hasDmdc1;
@property (Ti,N,V_dmdc1) dmdc1;
@property (TB,N) hasDmdc2;
@property (Ti,N,V_dmdc2) dmdc2;
@property (TB,N) hasGala;
@property (Ti,N,V_gala) gala;
@property (TB,N) hasUplink;
@property (Ti,N,V_uplink) uplink;
@property (TB,N) hasAxibr;
@property (Ti,N,V_axibr) axibr;
@property (TB,N) hasRflc;
@property (Ti,N,V_rflc) rflc;
@property (TB,N) hasMcgAggregatedBw;
@property (TI,N,V_mcgAggregatedBw) mcgAggregatedBw;
@property (TB,N) hasMcgDlCcConfigured;
@property (Ti,N,V_mcgDlCcConfigured) mcgDlCcConfigured;
@property (TB,N) hasMcgDlCcActivated;
@property (Ti,N,V_mcgDlCcActivated) mcgDlCcActivated;
@property (TB,N) hasMcgUlCcConfigured;
@property (Ti,N,V_mcgUlCcConfigured) mcgUlCcConfigured;
@property (TB,N) hasMcgUlCcActivated;
@property (Ti,N,V_mcgUlCcActivated) mcgUlCcActivated;
@property (TB,N) hasScgAggregatedBw;
@property (TI,N,V_scgAggregatedBw) scgAggregatedBw;
@property (TB,N) hasScgDlCcConfigured;
@property (Ti,N,V_scgDlCcConfigured) scgDlCcConfigured;
@property (TB,N) hasScgDlCcActivated;
@property (Ti,N,V_scgDlCcActivated) scgDlCcActivated;
@property (TB,N) hasScgUlCcConfigured;
@property (Ti,N,V_scgUlCcConfigured) scgUlCcConfigured;
@property (TB,N) hasScgUlCcActivated;
@property (Ti,N,V_scgUlCcActivated) scgUlCcActivated;
@property (TB,N) hasDurationMs;
@property (TI,N,V_durationMs) durationMs;
@property (TB,N) hasDeployment;
@property (Ti,N,V_deployment) deployment;
```

## Instance methods

```
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels writeTo:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels mergeFrom:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels hash];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels copyTo:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels description];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels readFrom:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels copyWithZone:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels isEqual:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels dictionaryRepresentation];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels deployment];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels durationMs];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels hasDurationMs];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels setDurationMs:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels setHasDurationMs:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels hasDeployment];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels setDeployment:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels setHasDeployment:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels StringAsAxibr:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels StringAsDeployment:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels StringAsDmdc0:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels StringAsDmdc2:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels StringAsGala:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels StringAsMcgDlCcActivated:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels StringAsMcgUlCcConfigured:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels StringAsScgDlCcActivated:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels StringAsScgUlCcActivated:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels StringAsTdp:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels hasGala];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels uplinkAsString:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels StringAsUplink:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels StringAsDmdc1:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels StringAsMcgDlCcConfigured:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels StringAsMcgUlCcActivated:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels StringAsRflc:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels StringAsScgDlCcConfigured:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels StringAsScgUlCcConfigured:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels hasRflc];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels mcgAggregatedBw];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels scgAggregatedBw];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels setTdp:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels tdp];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels axibr];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels axibrAsString:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels deploymentAsString:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels dmdc0];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels dmdc0AsString:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels dmdc1];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels dmdc1AsString:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels dmdc2];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels dmdc2AsString:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels gala];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels galaAsString:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels hasAxibr];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels hasDmdc0];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels hasDmdc1];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels hasDmdc2];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels hasMcgAggregatedBw];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels hasMcgDlCcActivated];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels hasMcgDlCcConfigured];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels hasMcgUlCcActivated];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels hasMcgUlCcConfigured];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels hasScgAggregatedBw];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels hasScgDlCcActivated];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels hasScgDlCcConfigured];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels hasScgUlCcActivated];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels hasScgUlCcConfigured];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels hasTdp];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels hasUplink];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels mcgDlCcActivated];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels mcgDlCcActivatedAsString:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels mcgDlCcConfigured];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels mcgDlCcConfiguredAsString:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels mcgUlCcActivated];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels mcgUlCcActivatedAsString:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels mcgUlCcConfigured];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels mcgUlCcConfiguredAsString:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels rflc];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels rflcAsString:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels scgDlCcActivated];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels scgDlCcActivatedAsString:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels scgDlCcConfigured];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels scgDlCcConfiguredAsString:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels scgUlCcActivated];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels scgUlCcActivatedAsString:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels scgUlCcConfigured];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels scgUlCcConfiguredAsString:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels setAxibr:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels setDmdc0:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels setDmdc1:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels setDmdc2:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels setGala:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels setHasAxibr:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels setHasDmdc0:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels setHasDmdc1:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels setHasDmdc2:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels setHasGala:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels setHasMcgAggregatedBw:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels setHasMcgDlCcActivated:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels setHasMcgDlCcConfigured:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels setHasMcgUlCcActivated:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels setHasMcgUlCcConfigured:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels setHasRflc:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels setHasScgAggregatedBw:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels setHasScgDlCcActivated:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels setHasScgDlCcConfigured:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels setHasScgUlCcActivated:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels setHasScgUlCcConfigured:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels setHasTdp:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels setHasUplink:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels setMcgAggregatedBw:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels setMcgDlCcActivated:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels setMcgDlCcConfigured:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels setMcgUlCcActivated:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels setMcgUlCcConfigured:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels setRflc:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels setScgAggregatedBw:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels setScgDlCcActivated:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels setScgDlCcConfigured:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels setScgUlCcActivated:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels setScgUlCcConfigured:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels setUplink:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels tdpAsString:];
-[AWDMETRICSKCellularAcmSleepStatsAcmCaSleepLevels uplink];
```
