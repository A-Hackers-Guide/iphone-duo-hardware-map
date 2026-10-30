# `AWDMETRICSBwpStats`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 4 instance variables, 6 properties, 23 instance methods, 0 class methods

## Instance variables

```
i _bandwidth;
I _duration;
I _scsSpacing;
{?="bandwidth"b1"duration"b1"scsSpacing"b1} _has;
```

## Properties

```
@property (TB,N) hasScsSpacing;
@property (TI,N,V_scsSpacing) scsSpacing;
@property (TB,N) hasDuration;
@property (TI,N,V_duration) duration;
@property (TB,N) hasBandwidth;
@property (Ti,N,V_bandwidth) bandwidth;
```

## Instance methods

```
-[AWDMETRICSBwpStats writeTo:];
-[AWDMETRICSBwpStats mergeFrom:];
-[AWDMETRICSBwpStats hasDuration];
-[AWDMETRICSBwpStats hasBandwidth];
-[AWDMETRICSBwpStats duration];
-[AWDMETRICSBwpStats setHasDuration:];
-[AWDMETRICSBwpStats setHasBandwidth:];
-[AWDMETRICSBwpStats setBandwidth:];
-[AWDMETRICSBwpStats hash];
-[AWDMETRICSBwpStats copyTo:];
-[AWDMETRICSBwpStats description];
-[AWDMETRICSBwpStats bandwidth];
-[AWDMETRICSBwpStats setDuration:];
-[AWDMETRICSBwpStats readFrom:];
-[AWDMETRICSBwpStats copyWithZone:];
-[AWDMETRICSBwpStats isEqual:];
-[AWDMETRICSBwpStats dictionaryRepresentation];
-[AWDMETRICSBwpStats StringAsBandwidth:];
-[AWDMETRICSBwpStats bandwidthAsString:];
-[AWDMETRICSBwpStats hasScsSpacing];
-[AWDMETRICSBwpStats scsSpacing];
-[AWDMETRICSBwpStats setHasScsSpacing:];
-[AWDMETRICSBwpStats setScsSpacing:];
```
