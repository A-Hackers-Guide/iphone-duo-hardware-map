# `KCellularLteRrcState`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 7 instance variables, 12 properties, 39 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
i _cause;
i _prevState;
I _prevStateDurMs;
i _state;
I _subsId;
{?="timestamp"b1"cause"b1"prevState"b1"prevStateDurMs"b1"state"b1"subsId"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasState;
@property (Ti,N,V_state) state;
@property (TB,N) hasPrevState;
@property (Ti,N,V_prevState) prevState;
@property (TB,N) hasPrevStateDurMs;
@property (TI,N,V_prevStateDurMs) prevStateDurMs;
@property (TB,N) hasCause;
@property (Ti,N,V_cause) cause;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
```

## Instance methods

```
-[KCellularLteRrcState hasTimestamp];
-[KCellularLteRrcState setHasTimestamp:];
-[KCellularLteRrcState setTimestamp:];
-[KCellularLteRrcState writeTo:];
-[KCellularLteRrcState setState:];
-[KCellularLteRrcState mergeFrom:];
-[KCellularLteRrcState timestamp];
-[KCellularLteRrcState stateAsString:];
-[KCellularLteRrcState StringAsState:];
-[KCellularLteRrcState hasState];
-[KCellularLteRrcState hash];
-[KCellularLteRrcState copyTo:];
-[KCellularLteRrcState description];
-[KCellularLteRrcState readFrom:];
-[KCellularLteRrcState copyWithZone:];
-[KCellularLteRrcState setHasState:];
-[KCellularLteRrcState isEqual:];
-[KCellularLteRrcState state];
-[KCellularLteRrcState dictionaryRepresentation];
-[KCellularLteRrcState cause];
-[KCellularLteRrcState setCause:];
-[KCellularLteRrcState StringAsCause:];
-[KCellularLteRrcState StringAsPrevState:];
-[KCellularLteRrcState causeAsString:];
-[KCellularLteRrcState hasCause];
-[KCellularLteRrcState hasPrevState];
-[KCellularLteRrcState hasPrevStateDurMs];
-[KCellularLteRrcState hasSubsId];
-[KCellularLteRrcState prevState];
-[KCellularLteRrcState prevStateAsString:];
-[KCellularLteRrcState prevStateDurMs];
-[KCellularLteRrcState setHasCause:];
-[KCellularLteRrcState setHasPrevState:];
-[KCellularLteRrcState setHasPrevStateDurMs:];
-[KCellularLteRrcState setHasSubsId:];
-[KCellularLteRrcState setPrevState:];
-[KCellularLteRrcState setPrevStateDurMs:];
-[KCellularLteRrcState setSubsId:];
-[KCellularLteRrcState subsId];
```
