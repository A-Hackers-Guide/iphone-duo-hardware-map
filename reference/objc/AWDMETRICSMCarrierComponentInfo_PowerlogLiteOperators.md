# `AWDMETRICSMCarrierComponentInfo`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 6 instance variables, 10 properties, 33 instance methods, 0 class methods

## Instance variables

```
I _band;
I _bandwidth;
i _duplex;
I _earfcn;
i _type;
{?="band"b1"bandwidth"b1"duplex"b1"earfcn"b1"type"b1} _has;
```

## Properties

```
@property (TB,N) hasBand;
@property (TI,N,V_band) band;
@property (TB,N) hasBandwidth;
@property (TI,N,V_bandwidth) bandwidth;
@property (TB,N) hasEarfcn;
@property (TI,N,V_earfcn) earfcn;
@property (TB,N) hasType;
@property (Ti,N,V_type) type;
@property (TB,N) hasDuplex;
@property (Ti,N,V_duplex) duplex;
```

## Instance methods

```
-[AWDMETRICSMCarrierComponentInfo writeTo:];
-[AWDMETRICSMCarrierComponentInfo typeAsString:];
-[AWDMETRICSMCarrierComponentInfo setHasType:];
-[AWDMETRICSMCarrierComponentInfo mergeFrom:];
-[AWDMETRICSMCarrierComponentInfo hasBandwidth];
-[AWDMETRICSMCarrierComponentInfo band];
-[AWDMETRICSMCarrierComponentInfo hasType];
-[AWDMETRICSMCarrierComponentInfo StringAsType:];
-[AWDMETRICSMCarrierComponentInfo setType:];
-[AWDMETRICSMCarrierComponentInfo type];
-[AWDMETRICSMCarrierComponentInfo setHasBandwidth:];
-[AWDMETRICSMCarrierComponentInfo setBand:];
-[AWDMETRICSMCarrierComponentInfo setBandwidth:];
-[AWDMETRICSMCarrierComponentInfo hash];
-[AWDMETRICSMCarrierComponentInfo copyTo:];
-[AWDMETRICSMCarrierComponentInfo description];
-[AWDMETRICSMCarrierComponentInfo bandwidth];
-[AWDMETRICSMCarrierComponentInfo readFrom:];
-[AWDMETRICSMCarrierComponentInfo copyWithZone:];
-[AWDMETRICSMCarrierComponentInfo isEqual:];
-[AWDMETRICSMCarrierComponentInfo dictionaryRepresentation];
-[AWDMETRICSMCarrierComponentInfo hasBand];
-[AWDMETRICSMCarrierComponentInfo setHasBand:];
-[AWDMETRICSMCarrierComponentInfo duplex];
-[AWDMETRICSMCarrierComponentInfo setDuplex:];
-[AWDMETRICSMCarrierComponentInfo StringAsDuplex:];
-[AWDMETRICSMCarrierComponentInfo duplexAsString:];
-[AWDMETRICSMCarrierComponentInfo earfcn];
-[AWDMETRICSMCarrierComponentInfo hasDuplex];
-[AWDMETRICSMCarrierComponentInfo hasEarfcn];
-[AWDMETRICSMCarrierComponentInfo setEarfcn:];
-[AWDMETRICSMCarrierComponentInfo setHasDuplex:];
-[AWDMETRICSMCarrierComponentInfo setHasEarfcn:];
```
