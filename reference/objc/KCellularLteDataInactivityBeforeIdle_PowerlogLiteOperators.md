# `KCellularLteDataInactivityBeforeIdle`

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
-[KCellularLteDataInactivityBeforeIdle hasTimestamp];
-[KCellularLteDataInactivityBeforeIdle setHasTimestamp:];
-[KCellularLteDataInactivityBeforeIdle setTimestamp:];
-[KCellularLteDataInactivityBeforeIdle writeTo:];
-[KCellularLteDataInactivityBeforeIdle mergeFrom:];
-[KCellularLteDataInactivityBeforeIdle timestamp];
-[KCellularLteDataInactivityBeforeIdle hash];
-[KCellularLteDataInactivityBeforeIdle copyTo:];
-[KCellularLteDataInactivityBeforeIdle description];
-[KCellularLteDataInactivityBeforeIdle readFrom:];
-[KCellularLteDataInactivityBeforeIdle copyWithZone:];
-[KCellularLteDataInactivityBeforeIdle isEqual:];
-[KCellularLteDataInactivityBeforeIdle dictionaryRepresentation];
-[KCellularLteDataInactivityBeforeIdle dataInactivityDurMs];
-[KCellularLteDataInactivityBeforeIdle hasDataInactivityDurMs];
-[KCellularLteDataInactivityBeforeIdle hasSubsId];
-[KCellularLteDataInactivityBeforeIdle setDataInactivityDurMs:];
-[KCellularLteDataInactivityBeforeIdle setHasDataInactivityDurMs:];
-[KCellularLteDataInactivityBeforeIdle setHasSubsId:];
-[KCellularLteDataInactivityBeforeIdle setSubsId:];
-[KCellularLteDataInactivityBeforeIdle subsId];
```
