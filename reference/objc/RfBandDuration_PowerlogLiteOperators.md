# `RfBandDuration`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 7 instance variables, 12 properties, 43 instance methods, 0 class methods

## Instance variables

```
I _durationMs;
i _eutraRfBand;
i _geraRfBand;
i _rat;
i _utraFddRfBand;
i _utraTddRfBand;
{?="durationMs"b1"eutraRfBand"b1"geraRfBand"b1"rat"b1"utraFddRfBand"b1"utraTddRfBand"b1} _has;
```

## Properties

```
@property (TB,N) hasRat;
@property (Ti,N,V_rat) rat;
@property (TB,N) hasGeraRfBand;
@property (Ti,N,V_geraRfBand) geraRfBand;
@property (TB,N) hasUtraFddRfBand;
@property (Ti,N,V_utraFddRfBand) utraFddRfBand;
@property (TB,N) hasUtraTddRfBand;
@property (Ti,N,V_utraTddRfBand) utraTddRfBand;
@property (TB,N) hasEutraRfBand;
@property (Ti,N,V_eutraRfBand) eutraRfBand;
@property (TB,N) hasDurationMs;
@property (TI,N,V_durationMs) durationMs;
```

## Instance methods

```
-[RfBandDuration writeTo:];
-[RfBandDuration mergeFrom:];
-[RfBandDuration rat];
-[RfBandDuration hash];
-[RfBandDuration copyTo:];
-[RfBandDuration description];
-[RfBandDuration readFrom:];
-[RfBandDuration copyWithZone:];
-[RfBandDuration isEqual:];
-[RfBandDuration dictionaryRepresentation];
-[RfBandDuration durationMs];
-[RfBandDuration hasDurationMs];
-[RfBandDuration setDurationMs:];
-[RfBandDuration setHasDurationMs:];
-[RfBandDuration setRat:];
-[RfBandDuration hasRat];
-[RfBandDuration setHasRat:];
-[RfBandDuration StringAsRat:];
-[RfBandDuration ratAsString:];
-[RfBandDuration StringAsUtraFddRfBand:];
-[RfBandDuration StringAsEutraRfBand:];
-[RfBandDuration StringAsGeraRfBand:];
-[RfBandDuration StringAsUtraTddRfBand:];
-[RfBandDuration setEutraRfBand:];
-[RfBandDuration eutraRfBand];
-[RfBandDuration eutraRfBandAsString:];
-[RfBandDuration geraRfBand];
-[RfBandDuration geraRfBandAsString:];
-[RfBandDuration hasEutraRfBand];
-[RfBandDuration hasGeraRfBand];
-[RfBandDuration hasUtraFddRfBand];
-[RfBandDuration hasUtraTddRfBand];
-[RfBandDuration setGeraRfBand:];
-[RfBandDuration setHasEutraRfBand:];
-[RfBandDuration setHasGeraRfBand:];
-[RfBandDuration setHasUtraFddRfBand:];
-[RfBandDuration setHasUtraTddRfBand:];
-[RfBandDuration setUtraFddRfBand:];
-[RfBandDuration setUtraTddRfBand:];
-[RfBandDuration utraFddRfBand];
-[RfBandDuration utraFddRfBandAsString:];
-[RfBandDuration utraTddRfBand];
-[RfBandDuration utraTddRfBandAsString:];
```
