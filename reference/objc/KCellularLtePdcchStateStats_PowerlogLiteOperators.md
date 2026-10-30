# `KCellularLtePdcchStateStats`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 9 instance variables, 16 properties, 52 instance methods, 0 class methods

## Instance variables

```
{?="list"^I"count"Q"size"Q} _pccPdcchStates;
{?="list"^I"count"Q"size"Q} _scc0PdcchStates;
{?="list"^I"count"Q"size"Q} _scc1PdcchStates;
{?="list"^I"count"Q"size"Q} _scc2PdcchStates;
{?="list"^I"count"Q"size"Q} _scc3PdcchStates;
Q _timestamp;
I _durationMs;
I _subsId;
{?="timestamp"b1"durationMs"b1"subsId"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TQ,R,N) pccPdcchStatesCount;
@property (T^I,R,N) pccPdcchStates;
@property (TQ,R,N) scc0PdcchStatesCount;
@property (T^I,R,N) scc0PdcchStates;
@property (TQ,R,N) scc1PdcchStatesCount;
@property (T^I,R,N) scc1PdcchStates;
@property (TB,N) hasDurationMs;
@property (TI,N,V_durationMs) durationMs;
@property (TQ,R,N) scc2PdcchStatesCount;
@property (T^I,R,N) scc2PdcchStates;
@property (TQ,R,N) scc3PdcchStatesCount;
@property (T^I,R,N) scc3PdcchStates;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
```

## Instance methods

```
-[KCellularLtePdcchStateStats hasTimestamp];
-[KCellularLtePdcchStateStats setHasTimestamp:];
-[KCellularLtePdcchStateStats setTimestamp:];
-[KCellularLtePdcchStateStats writeTo:];
-[KCellularLtePdcchStateStats mergeFrom:];
-[KCellularLtePdcchStateStats dealloc];
-[KCellularLtePdcchStateStats timestamp];
-[KCellularLtePdcchStateStats hash];
-[KCellularLtePdcchStateStats copyTo:];
-[KCellularLtePdcchStateStats description];
-[KCellularLtePdcchStateStats readFrom:];
-[KCellularLtePdcchStateStats copyWithZone:];
-[KCellularLtePdcchStateStats isEqual:];
-[KCellularLtePdcchStateStats dictionaryRepresentation];
-[KCellularLtePdcchStateStats durationMs];
-[KCellularLtePdcchStateStats hasDurationMs];
-[KCellularLtePdcchStateStats setDurationMs:];
-[KCellularLtePdcchStateStats setHasDurationMs:];
-[KCellularLtePdcchStateStats hasSubsId];
-[KCellularLtePdcchStateStats setHasSubsId:];
-[KCellularLtePdcchStateStats setSubsId:];
-[KCellularLtePdcchStateStats subsId];
-[KCellularLtePdcchStateStats scc0PdcchStates];
-[KCellularLtePdcchStateStats scc2PdcchStates];
-[KCellularLtePdcchStateStats scc1PdcchStates];
-[KCellularLtePdcchStateStats scc3PdcchStates];
-[KCellularLtePdcchStateStats addPccPdcchState:];
-[KCellularLtePdcchStateStats addScc0PdcchState:];
-[KCellularLtePdcchStateStats addScc1PdcchState:];
-[KCellularLtePdcchStateStats addScc2PdcchState:];
-[KCellularLtePdcchStateStats addScc3PdcchState:];
-[KCellularLtePdcchStateStats clearPccPdcchStates];
-[KCellularLtePdcchStateStats clearScc0PdcchStates];
-[KCellularLtePdcchStateStats clearScc1PdcchStates];
-[KCellularLtePdcchStateStats clearScc2PdcchStates];
-[KCellularLtePdcchStateStats clearScc3PdcchStates];
-[KCellularLtePdcchStateStats pccPdcchStateAtIndex:];
-[KCellularLtePdcchStateStats pccPdcchStates];
-[KCellularLtePdcchStateStats pccPdcchStatesCount];
-[KCellularLtePdcchStateStats scc0PdcchStateAtIndex:];
-[KCellularLtePdcchStateStats scc0PdcchStatesCount];
-[KCellularLtePdcchStateStats scc1PdcchStateAtIndex:];
-[KCellularLtePdcchStateStats scc1PdcchStatesCount];
-[KCellularLtePdcchStateStats scc2PdcchStateAtIndex:];
-[KCellularLtePdcchStateStats scc2PdcchStatesCount];
-[KCellularLtePdcchStateStats scc3PdcchStateAtIndex:];
-[KCellularLtePdcchStateStats scc3PdcchStatesCount];
-[KCellularLtePdcchStateStats setPccPdcchStates:count:];
-[KCellularLtePdcchStateStats setScc0PdcchStates:count:];
-[KCellularLtePdcchStateStats setScc1PdcchStates:count:];
-[KCellularLtePdcchStateStats setScc2PdcchStates:count:];
-[KCellularLtePdcchStateStats setScc3PdcchStates:count:];
```
