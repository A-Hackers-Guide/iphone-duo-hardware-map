# `KCellularCdmaEvdoRrState`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 7 instance variables, 12 properties, 35 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
I _currAtState;
i _currNormalizedState;
I _prevAtState;
I _prevStateDurMs;
I _subsId;
{?="timestamp"b1"currAtState"b1"currNormalizedState"b1"prevAtState"b1"prevStateDurMs"b1"subsId"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
@property (TB,N) hasPrevAtState;
@property (TI,N,V_prevAtState) prevAtState;
@property (TB,N) hasCurrAtState;
@property (TI,N,V_currAtState) currAtState;
@property (TB,N) hasPrevStateDurMs;
@property (TI,N,V_prevStateDurMs) prevStateDurMs;
@property (TB,N) hasCurrNormalizedState;
@property (Ti,N,V_currNormalizedState) currNormalizedState;
```

## Instance methods

```
-[KCellularCdmaEvdoRrState hasTimestamp];
-[KCellularCdmaEvdoRrState setHasTimestamp:];
-[KCellularCdmaEvdoRrState setTimestamp:];
-[KCellularCdmaEvdoRrState writeTo:];
-[KCellularCdmaEvdoRrState mergeFrom:];
-[KCellularCdmaEvdoRrState timestamp];
-[KCellularCdmaEvdoRrState hash];
-[KCellularCdmaEvdoRrState copyTo:];
-[KCellularCdmaEvdoRrState description];
-[KCellularCdmaEvdoRrState readFrom:];
-[KCellularCdmaEvdoRrState copyWithZone:];
-[KCellularCdmaEvdoRrState isEqual:];
-[KCellularCdmaEvdoRrState dictionaryRepresentation];
-[KCellularCdmaEvdoRrState hasPrevStateDurMs];
-[KCellularCdmaEvdoRrState hasSubsId];
-[KCellularCdmaEvdoRrState prevStateDurMs];
-[KCellularCdmaEvdoRrState setHasPrevStateDurMs:];
-[KCellularCdmaEvdoRrState setHasSubsId:];
-[KCellularCdmaEvdoRrState setPrevStateDurMs:];
-[KCellularCdmaEvdoRrState setSubsId:];
-[KCellularCdmaEvdoRrState subsId];
-[KCellularCdmaEvdoRrState StringAsCurrNormalizedState:];
-[KCellularCdmaEvdoRrState setPrevAtState:];
-[KCellularCdmaEvdoRrState setCurrAtState:];
-[KCellularCdmaEvdoRrState currAtState];
-[KCellularCdmaEvdoRrState currNormalizedState];
-[KCellularCdmaEvdoRrState currNormalizedStateAsString:];
-[KCellularCdmaEvdoRrState hasCurrAtState];
-[KCellularCdmaEvdoRrState hasCurrNormalizedState];
-[KCellularCdmaEvdoRrState hasPrevAtState];
-[KCellularCdmaEvdoRrState prevAtState];
-[KCellularCdmaEvdoRrState setCurrNormalizedState:];
-[KCellularCdmaEvdoRrState setHasCurrAtState:];
-[KCellularCdmaEvdoRrState setHasCurrNormalizedState:];
-[KCellularCdmaEvdoRrState setHasPrevAtState:];
```
