# `KCellularCdma1XRrState`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 7 instance variables, 12 properties, 35 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
I _currCpState;
i _currNormalizedState;
I _prevCpState;
I _prevStateDurMs;
I _subsId;
{?="timestamp"b1"currCpState"b1"currNormalizedState"b1"prevCpState"b1"prevStateDurMs"b1"subsId"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
@property (TB,N) hasPrevCpState;
@property (TI,N,V_prevCpState) prevCpState;
@property (TB,N) hasCurrCpState;
@property (TI,N,V_currCpState) currCpState;
@property (TB,N) hasPrevStateDurMs;
@property (TI,N,V_prevStateDurMs) prevStateDurMs;
@property (TB,N) hasCurrNormalizedState;
@property (Ti,N,V_currNormalizedState) currNormalizedState;
```

## Instance methods

```
-[KCellularCdma1XRrState hasTimestamp];
-[KCellularCdma1XRrState setHasTimestamp:];
-[KCellularCdma1XRrState setTimestamp:];
-[KCellularCdma1XRrState writeTo:];
-[KCellularCdma1XRrState mergeFrom:];
-[KCellularCdma1XRrState timestamp];
-[KCellularCdma1XRrState hash];
-[KCellularCdma1XRrState copyTo:];
-[KCellularCdma1XRrState description];
-[KCellularCdma1XRrState readFrom:];
-[KCellularCdma1XRrState copyWithZone:];
-[KCellularCdma1XRrState isEqual:];
-[KCellularCdma1XRrState dictionaryRepresentation];
-[KCellularCdma1XRrState hasPrevStateDurMs];
-[KCellularCdma1XRrState hasSubsId];
-[KCellularCdma1XRrState prevStateDurMs];
-[KCellularCdma1XRrState setHasPrevStateDurMs:];
-[KCellularCdma1XRrState setHasSubsId:];
-[KCellularCdma1XRrState setPrevStateDurMs:];
-[KCellularCdma1XRrState setSubsId:];
-[KCellularCdma1XRrState subsId];
-[KCellularCdma1XRrState StringAsCurrNormalizedState:];
-[KCellularCdma1XRrState setCurrCpState:];
-[KCellularCdma1XRrState setPrevCpState:];
-[KCellularCdma1XRrState currCpState];
-[KCellularCdma1XRrState currNormalizedState];
-[KCellularCdma1XRrState currNormalizedStateAsString:];
-[KCellularCdma1XRrState hasCurrCpState];
-[KCellularCdma1XRrState hasCurrNormalizedState];
-[KCellularCdma1XRrState hasPrevCpState];
-[KCellularCdma1XRrState prevCpState];
-[KCellularCdma1XRrState setCurrNormalizedState:];
-[KCellularCdma1XRrState setHasCurrCpState:];
-[KCellularCdma1XRrState setHasCurrNormalizedState:];
-[KCellularCdma1XRrState setHasPrevCpState:];
```
