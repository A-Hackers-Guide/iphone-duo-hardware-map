# `KCellularTdsRrcState`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 6 instance variables, 10 properties, 33 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
i _newRrcState;
I _prevStateDurMs;
i _rrcState;
I _subsId;
{?="timestamp"b1"newRrcState"b1"prevStateDurMs"b1"rrcState"b1"subsId"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasRrcState;
@property (Ti,N,V_rrcState) rrcState;
@property (TB,N) hasNewRrcState;
@property (Ti,N,V_newRrcState) newRrcState;
@property (TB,N) hasPrevStateDurMs;
@property (TI,N,V_prevStateDurMs) prevStateDurMs;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
```

## Instance methods

```
-[KCellularTdsRrcState hasTimestamp];
-[KCellularTdsRrcState setHasTimestamp:];
-[KCellularTdsRrcState setTimestamp:];
-[KCellularTdsRrcState writeTo:];
-[KCellularTdsRrcState mergeFrom:];
-[KCellularTdsRrcState timestamp];
-[KCellularTdsRrcState hash];
-[KCellularTdsRrcState copyTo:];
-[KCellularTdsRrcState description];
-[KCellularTdsRrcState readFrom:];
-[KCellularTdsRrcState copyWithZone:];
-[KCellularTdsRrcState isEqual:];
-[KCellularTdsRrcState dictionaryRepresentation];
-[KCellularTdsRrcState setHasRrcState:];
-[KCellularTdsRrcState hasRrcState];
-[KCellularTdsRrcState rrcState];
-[KCellularTdsRrcState StringAsRrcState:];
-[KCellularTdsRrcState hasPrevStateDurMs];
-[KCellularTdsRrcState hasSubsId];
-[KCellularTdsRrcState prevStateDurMs];
-[KCellularTdsRrcState rrcStateAsString:];
-[KCellularTdsRrcState setHasPrevStateDurMs:];
-[KCellularTdsRrcState setHasSubsId:];
-[KCellularTdsRrcState setPrevStateDurMs:];
-[KCellularTdsRrcState setRrcState:];
-[KCellularTdsRrcState setSubsId:];
-[KCellularTdsRrcState subsId];
-[KCellularTdsRrcState StringAsNewRrcState:];
-[KCellularTdsRrcState setNewRrcState:];
-[KCellularTdsRrcState hasNewRrcState];
-[KCellularTdsRrcState newRrcState];
-[KCellularTdsRrcState newRrcStateAsString:];
-[KCellularTdsRrcState setHasNewRrcState:];
```
