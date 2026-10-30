# `AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 8 instance variables, 14 properties, 47 instance methods, 0 class methods

## Instance variables

```
i _ap;
i _bbChipset;
I _durationMs;
I _durationUlpnMs;
i _mode;
i _nonPsPrefSim;
i _psPrefSim;
{?="ap"b1"bbChipset"b1"durationMs"b1"durationUlpnMs"b1"mode"b1"nonPsPrefSim"b1"psPrefSim"b1} _has;
```

## Properties

```
@property (TB,N) hasAp;
@property (Ti,N,V_ap) ap;
@property (TB,N) hasPsPrefSim;
@property (Ti,N,V_psPrefSim) psPrefSim;
@property (TB,N) hasNonPsPrefSim;
@property (Ti,N,V_nonPsPrefSim) nonPsPrefSim;
@property (TB,N) hasBbChipset;
@property (Ti,N,V_bbChipset) bbChipset;
@property (TB,N) hasDurationMs;
@property (TI,N,V_durationMs) durationMs;
@property (TB,N) hasDurationUlpnMs;
@property (TI,N,V_durationUlpnMs) durationUlpnMs;
@property (TB,N) hasMode;
@property (Ti,N,V_mode) mode;
```

## Instance methods

```
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState StringAsMode:];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState setHasMode:];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState hasMode];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState writeTo:];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState mergeFrom:];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState setMode:];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState mode];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState hash];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState copyTo:];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState description];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState readFrom:];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState modeAsString:];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState copyWithZone:];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState isEqual:];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState dictionaryRepresentation];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState durationMs];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState hasDurationMs];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState setDurationMs:];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState setHasDurationMs:];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState hasNonPsPrefSim];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState StringAsAp:];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState StringAsBbChipset:];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState StringAsNonPsPrefSim:];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState StringAsPsPrefSim:];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState ap];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState apAsString:];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState bbChipset];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState bbChipsetAsString:];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState durationUlpnMs];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState hasAp];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState hasBbChipset];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState hasDurationUlpnMs];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState hasPsPrefSim];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState nonPsPrefSim];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState nonPsPrefSimAsString:];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState psPrefSim];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState psPrefSimAsString:];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState setAp:];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState setBbChipset:];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState setDurationUlpnMs:];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState setHasAp:];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState setHasBbChipset:];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState setHasDurationUlpnMs:];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState setHasNonPsPrefSim:];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState setHasPsPrefSim:];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState setNonPsPrefSim:];
-[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState setPsPrefSim:];
```
