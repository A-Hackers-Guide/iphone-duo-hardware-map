# `KCellularWcdmaRrcConnectionState`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 6 instance variables, 10 properties, 35 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
i _establishmentCause;
i _releaseCause;
i _state;
I _subsId;
{?="timestamp"b1"establishmentCause"b1"releaseCause"b1"state"b1"subsId"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasState;
@property (Ti,N,V_state) state;
@property (TB,N) hasEstablishmentCause;
@property (Ti,N,V_establishmentCause) establishmentCause;
@property (TB,N) hasReleaseCause;
@property (Ti,N,V_releaseCause) releaseCause;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
```

## Instance methods

```
-[KCellularWcdmaRrcConnectionState hasTimestamp];
-[KCellularWcdmaRrcConnectionState setHasTimestamp:];
-[KCellularWcdmaRrcConnectionState setTimestamp:];
-[KCellularWcdmaRrcConnectionState writeTo:];
-[KCellularWcdmaRrcConnectionState setState:];
-[KCellularWcdmaRrcConnectionState mergeFrom:];
-[KCellularWcdmaRrcConnectionState timestamp];
-[KCellularWcdmaRrcConnectionState stateAsString:];
-[KCellularWcdmaRrcConnectionState StringAsState:];
-[KCellularWcdmaRrcConnectionState hasState];
-[KCellularWcdmaRrcConnectionState hash];
-[KCellularWcdmaRrcConnectionState copyTo:];
-[KCellularWcdmaRrcConnectionState description];
-[KCellularWcdmaRrcConnectionState readFrom:];
-[KCellularWcdmaRrcConnectionState copyWithZone:];
-[KCellularWcdmaRrcConnectionState setHasState:];
-[KCellularWcdmaRrcConnectionState isEqual:];
-[KCellularWcdmaRrcConnectionState state];
-[KCellularWcdmaRrcConnectionState dictionaryRepresentation];
-[KCellularWcdmaRrcConnectionState StringAsEstablishmentCause:];
-[KCellularWcdmaRrcConnectionState StringAsReleaseCause:];
-[KCellularWcdmaRrcConnectionState hasReleaseCause];
-[KCellularWcdmaRrcConnectionState establishmentCause];
-[KCellularWcdmaRrcConnectionState establishmentCauseAsString:];
-[KCellularWcdmaRrcConnectionState hasEstablishmentCause];
-[KCellularWcdmaRrcConnectionState hasSubsId];
-[KCellularWcdmaRrcConnectionState releaseCause];
-[KCellularWcdmaRrcConnectionState releaseCauseAsString:];
-[KCellularWcdmaRrcConnectionState setEstablishmentCause:];
-[KCellularWcdmaRrcConnectionState setHasEstablishmentCause:];
-[KCellularWcdmaRrcConnectionState setHasReleaseCause:];
-[KCellularWcdmaRrcConnectionState setHasSubsId:];
-[KCellularWcdmaRrcConnectionState setReleaseCause:];
-[KCellularWcdmaRrcConnectionState setSubsId:];
-[KCellularWcdmaRrcConnectionState subsId];
```
