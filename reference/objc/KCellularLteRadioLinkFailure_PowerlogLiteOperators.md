# `KCellularLteRadioLinkFailure`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 8 instance variables, 14 properties, 41 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
I _band;
I _coexPolicy;
i _failCause;
I _hstState;
i _rrcState;
I _subsId;
{?="timestamp"b1"band"b1"coexPolicy"b1"failCause"b1"hstState"b1"rrcState"b1"subsId"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasFailCause;
@property (Ti,N,V_failCause) failCause;
@property (TB,N) hasBand;
@property (TI,N,V_band) band;
@property (TB,N) hasCoexPolicy;
@property (TI,N,V_coexPolicy) coexPolicy;
@property (TB,N) hasRrcState;
@property (Ti,N,V_rrcState) rrcState;
@property (TB,N) hasHstState;
@property (TI,N,V_hstState) hstState;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
```

## Instance methods

```
-[KCellularLteRadioLinkFailure hasTimestamp];
-[KCellularLteRadioLinkFailure setHasTimestamp:];
-[KCellularLteRadioLinkFailure setTimestamp:];
-[KCellularLteRadioLinkFailure writeTo:];
-[KCellularLteRadioLinkFailure mergeFrom:];
-[KCellularLteRadioLinkFailure timestamp];
-[KCellularLteRadioLinkFailure band];
-[KCellularLteRadioLinkFailure setBand:];
-[KCellularLteRadioLinkFailure hash];
-[KCellularLteRadioLinkFailure copyTo:];
-[KCellularLteRadioLinkFailure description];
-[KCellularLteRadioLinkFailure readFrom:];
-[KCellularLteRadioLinkFailure copyWithZone:];
-[KCellularLteRadioLinkFailure isEqual:];
-[KCellularLteRadioLinkFailure dictionaryRepresentation];
-[KCellularLteRadioLinkFailure setHasRrcState:];
-[KCellularLteRadioLinkFailure hasRrcState];
-[KCellularLteRadioLinkFailure rrcState];
-[KCellularLteRadioLinkFailure hasBand];
-[KCellularLteRadioLinkFailure setHasBand:];
-[KCellularLteRadioLinkFailure StringAsRrcState:];
-[KCellularLteRadioLinkFailure hasSubsId];
-[KCellularLteRadioLinkFailure rrcStateAsString:];
-[KCellularLteRadioLinkFailure setHasSubsId:];
-[KCellularLteRadioLinkFailure setRrcState:];
-[KCellularLteRadioLinkFailure setSubsId:];
-[KCellularLteRadioLinkFailure subsId];
-[KCellularLteRadioLinkFailure setHasHstState:];
-[KCellularLteRadioLinkFailure StringAsFailCause:];
-[KCellularLteRadioLinkFailure coexPolicy];
-[KCellularLteRadioLinkFailure failCause];
-[KCellularLteRadioLinkFailure failCauseAsString:];
-[KCellularLteRadioLinkFailure hasCoexPolicy];
-[KCellularLteRadioLinkFailure hasFailCause];
-[KCellularLteRadioLinkFailure hasHstState];
-[KCellularLteRadioLinkFailure hstState];
-[KCellularLteRadioLinkFailure setCoexPolicy:];
-[KCellularLteRadioLinkFailure setFailCause:];
-[KCellularLteRadioLinkFailure setHasCoexPolicy:];
-[KCellularLteRadioLinkFailure setHasFailCause:];
-[KCellularLteRadioLinkFailure setHstState:];
```
