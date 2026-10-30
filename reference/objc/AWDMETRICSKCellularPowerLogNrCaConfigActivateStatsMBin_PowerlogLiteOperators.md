# `AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 10 instance variables, 18 properties, 53 instance methods, 0 class methods

## Instance variables

```
i _ccActivated;
i _ccConfigured;
i _direction;
I _duration;
i _freqRange;
I _scheduledScellCount;
B _areScellsScheduled;
B _isEndc;
B _isSpcellScheduled;
{?="ccActivated"b1"ccConfigured"b1"direction"b1"duration"b1"freqRange"b1"scheduledScellCount"b1"areScellsScheduled"b1"isEndc"b1"isSpcellScheduled"b1} _has;
```

## Properties

```
@property (TB,N) hasCcConfigured;
@property (Ti,N,V_ccConfigured) ccConfigured;
@property (TB,N) hasCcActivated;
@property (Ti,N,V_ccActivated) ccActivated;
@property (TB,N) hasDuration;
@property (TI,N,V_duration) duration;
@property (TB,N) hasDirection;
@property (Ti,N,V_direction) direction;
@property (TB,N) hasIsEndc;
@property (TB,N,V_isEndc) isEndc;
@property (TB,N) hasFreqRange;
@property (Ti,N,V_freqRange) freqRange;
@property (TB,N) hasIsSpcellScheduled;
@property (TB,N,V_isSpcellScheduled) isSpcellScheduled;
@property (TB,N) hasAreScellsScheduled;
@property (TB,N,V_areScellsScheduled) areScellsScheduled;
@property (TB,N) hasScheduledScellCount;
@property (TI,N,V_scheduledScellCount) scheduledScellCount;
```

## Instance methods

```
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin writeTo:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin mergeFrom:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin hasDuration];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin setDirection:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin duration];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin setHasDuration:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin direction];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin hash];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin copyTo:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin description];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin setDuration:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin readFrom:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin copyWithZone:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin isEqual:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin dictionaryRepresentation];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin hasDirection];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin StringAsDirection:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin directionAsString:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin setHasDirection:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin StringAsCcActivated:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin StringAsCcConfigured:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin StringAsFreqRange:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin hasCcConfigured];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin setCcActivated:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin areScellsScheduled];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin ccActivated];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin ccActivatedAsString:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin ccConfigured];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin ccConfiguredAsString:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin freqRange];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin freqRangeAsString:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin hasAreScellsScheduled];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin hasCcActivated];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin hasFreqRange];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin hasIsEndc];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin hasIsSpcellScheduled];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin hasScheduledScellCount];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin isEndc];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin isSpcellScheduled];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin scheduledScellCount];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin setAreScellsScheduled:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin setCcConfigured:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin setFreqRange:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin setHasAreScellsScheduled:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin setHasCcActivated:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin setHasCcConfigured:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin setHasFreqRange:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin setHasIsEndc:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin setHasIsSpcellScheduled:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin setHasScheduledScellCount:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin setIsEndc:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin setIsSpcellScheduled:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin setScheduledScellCount:];
```
