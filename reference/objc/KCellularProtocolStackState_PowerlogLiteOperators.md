# `KCellularProtocolStackState`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 6 instance variables, 10 properties, 33 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
i _currState;
i _prevState;
I _prevStateDurMs;
I _subsId;
{?="timestamp"b1"currState"b1"prevState"b1"prevStateDurMs"b1"subsId"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
@property (TB,N) hasPrevState;
@property (Ti,N,V_prevState) prevState;
@property (TB,N) hasCurrState;
@property (Ti,N,V_currState) currState;
@property (TB,N) hasPrevStateDurMs;
@property (TI,N,V_prevStateDurMs) prevStateDurMs;
```

## Instance methods

```
-[KCellularProtocolStackState hasTimestamp];
-[KCellularProtocolStackState setHasTimestamp:];
-[KCellularProtocolStackState setTimestamp:];
-[KCellularProtocolStackState writeTo:];
-[KCellularProtocolStackState mergeFrom:];
-[KCellularProtocolStackState timestamp];
-[KCellularProtocolStackState hash];
-[KCellularProtocolStackState copyTo:];
-[KCellularProtocolStackState description];
-[KCellularProtocolStackState readFrom:];
-[KCellularProtocolStackState copyWithZone:];
-[KCellularProtocolStackState isEqual:];
-[KCellularProtocolStackState dictionaryRepresentation];
-[KCellularProtocolStackState StringAsPrevState:];
-[KCellularProtocolStackState hasPrevState];
-[KCellularProtocolStackState hasPrevStateDurMs];
-[KCellularProtocolStackState hasSubsId];
-[KCellularProtocolStackState prevState];
-[KCellularProtocolStackState prevStateAsString:];
-[KCellularProtocolStackState prevStateDurMs];
-[KCellularProtocolStackState setHasPrevState:];
-[KCellularProtocolStackState setHasPrevStateDurMs:];
-[KCellularProtocolStackState setHasSubsId:];
-[KCellularProtocolStackState setPrevState:];
-[KCellularProtocolStackState setPrevStateDurMs:];
-[KCellularProtocolStackState setSubsId:];
-[KCellularProtocolStackState subsId];
-[KCellularProtocolStackState StringAsCurrState:];
-[KCellularProtocolStackState currState];
-[KCellularProtocolStackState currStateAsString:];
-[KCellularProtocolStackState hasCurrState];
-[KCellularProtocolStackState setCurrState:];
-[KCellularProtocolStackState setHasCurrState:];
```
