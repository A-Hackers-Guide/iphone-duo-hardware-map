# `KCellularWcdmaCpcStat`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 7 instance variables, 12 properties, 33 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
I _energy;
I _rxOnDurationMs;
I _rxTxOffDurationMs;
I _subsId;
I _totalDurationMs;
{?="timestamp"b1"energy"b1"rxOnDurationMs"b1"rxTxOffDurationMs"b1"subsId"b1"totalDurationMs"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasTotalDurationMs;
@property (TI,N,V_totalDurationMs) totalDurationMs;
@property (TB,N) hasRxTxOffDurationMs;
@property (TI,N,V_rxTxOffDurationMs) rxTxOffDurationMs;
@property (TB,N) hasRxOnDurationMs;
@property (TI,N,V_rxOnDurationMs) rxOnDurationMs;
@property (TB,N) hasEnergy;
@property (TI,N,V_energy) energy;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
```

## Instance methods

```
-[KCellularWcdmaCpcStat hasTimestamp];
-[KCellularWcdmaCpcStat setHasTimestamp:];
-[KCellularWcdmaCpcStat setTimestamp:];
-[KCellularWcdmaCpcStat writeTo:];
-[KCellularWcdmaCpcStat mergeFrom:];
-[KCellularWcdmaCpcStat timestamp];
-[KCellularWcdmaCpcStat energy];
-[KCellularWcdmaCpcStat totalDurationMs];
-[KCellularWcdmaCpcStat hash];
-[KCellularWcdmaCpcStat copyTo:];
-[KCellularWcdmaCpcStat description];
-[KCellularWcdmaCpcStat readFrom:];
-[KCellularWcdmaCpcStat copyWithZone:];
-[KCellularWcdmaCpcStat isEqual:];
-[KCellularWcdmaCpcStat dictionaryRepresentation];
-[KCellularWcdmaCpcStat setEnergy:];
-[KCellularWcdmaCpcStat hasEnergy];
-[KCellularWcdmaCpcStat hasSubsId];
-[KCellularWcdmaCpcStat hasTotalDurationMs];
-[KCellularWcdmaCpcStat setHasSubsId:];
-[KCellularWcdmaCpcStat setHasTotalDurationMs:];
-[KCellularWcdmaCpcStat setSubsId:];
-[KCellularWcdmaCpcStat setTotalDurationMs:];
-[KCellularWcdmaCpcStat subsId];
-[KCellularWcdmaCpcStat hasRxOnDurationMs];
-[KCellularWcdmaCpcStat hasRxTxOffDurationMs];
-[KCellularWcdmaCpcStat rxOnDurationMs];
-[KCellularWcdmaCpcStat rxTxOffDurationMs];
-[KCellularWcdmaCpcStat setHasEnergy:];
-[KCellularWcdmaCpcStat setHasRxOnDurationMs:];
-[KCellularWcdmaCpcStat setHasRxTxOffDurationMs:];
-[KCellularWcdmaCpcStat setRxOnDurationMs:];
-[KCellularWcdmaCpcStat setRxTxOffDurationMs:];
```
