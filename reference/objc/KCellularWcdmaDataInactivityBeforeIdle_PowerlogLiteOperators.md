# `KCellularWcdmaDataInactivityBeforeIdle`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 4 instance variables, 6 properties, 21 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
I _dataInactivityDurMs;
I _subsId;
{?="timestamp"b1"dataInactivityDurMs"b1"subsId"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasDataInactivityDurMs;
@property (TI,N,V_dataInactivityDurMs) dataInactivityDurMs;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
```

## Instance methods

```
-[KCellularWcdmaDataInactivityBeforeIdle hasTimestamp];
-[KCellularWcdmaDataInactivityBeforeIdle setHasTimestamp:];
-[KCellularWcdmaDataInactivityBeforeIdle setTimestamp:];
-[KCellularWcdmaDataInactivityBeforeIdle writeTo:];
-[KCellularWcdmaDataInactivityBeforeIdle mergeFrom:];
-[KCellularWcdmaDataInactivityBeforeIdle timestamp];
-[KCellularWcdmaDataInactivityBeforeIdle hash];
-[KCellularWcdmaDataInactivityBeforeIdle copyTo:];
-[KCellularWcdmaDataInactivityBeforeIdle description];
-[KCellularWcdmaDataInactivityBeforeIdle readFrom:];
-[KCellularWcdmaDataInactivityBeforeIdle copyWithZone:];
-[KCellularWcdmaDataInactivityBeforeIdle isEqual:];
-[KCellularWcdmaDataInactivityBeforeIdle dictionaryRepresentation];
-[KCellularWcdmaDataInactivityBeforeIdle dataInactivityDurMs];
-[KCellularWcdmaDataInactivityBeforeIdle hasDataInactivityDurMs];
-[KCellularWcdmaDataInactivityBeforeIdle hasSubsId];
-[KCellularWcdmaDataInactivityBeforeIdle setDataInactivityDurMs:];
-[KCellularWcdmaDataInactivityBeforeIdle setHasDataInactivityDurMs:];
-[KCellularWcdmaDataInactivityBeforeIdle setHasSubsId:];
-[KCellularWcdmaDataInactivityBeforeIdle setSubsId:];
-[KCellularWcdmaDataInactivityBeforeIdle subsId];
```
