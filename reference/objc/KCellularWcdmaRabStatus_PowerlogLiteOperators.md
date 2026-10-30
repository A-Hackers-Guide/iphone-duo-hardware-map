# `KCellularWcdmaRabStatus`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 6 instance variables, 10 properties, 29 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
I _hsRabCount;
I _r99RabCount;
I _subsId;
I _totalRabCount;
{?="timestamp"b1"hsRabCount"b1"r99RabCount"b1"subsId"b1"totalRabCount"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasTotalRabCount;
@property (TI,N,V_totalRabCount) totalRabCount;
@property (TB,N) hasR99RabCount;
@property (TI,N,V_r99RabCount) r99RabCount;
@property (TB,N) hasHsRabCount;
@property (TI,N,V_hsRabCount) hsRabCount;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
```

## Instance methods

```
-[KCellularWcdmaRabStatus hasTimestamp];
-[KCellularWcdmaRabStatus setHasTimestamp:];
-[KCellularWcdmaRabStatus setTimestamp:];
-[KCellularWcdmaRabStatus writeTo:];
-[KCellularWcdmaRabStatus mergeFrom:];
-[KCellularWcdmaRabStatus timestamp];
-[KCellularWcdmaRabStatus hash];
-[KCellularWcdmaRabStatus copyTo:];
-[KCellularWcdmaRabStatus description];
-[KCellularWcdmaRabStatus readFrom:];
-[KCellularWcdmaRabStatus copyWithZone:];
-[KCellularWcdmaRabStatus isEqual:];
-[KCellularWcdmaRabStatus dictionaryRepresentation];
-[KCellularWcdmaRabStatus hasSubsId];
-[KCellularWcdmaRabStatus setHasSubsId:];
-[KCellularWcdmaRabStatus setSubsId:];
-[KCellularWcdmaRabStatus subsId];
-[KCellularWcdmaRabStatus setR99RabCount:];
-[KCellularWcdmaRabStatus hasHsRabCount];
-[KCellularWcdmaRabStatus hasR99RabCount];
-[KCellularWcdmaRabStatus hasTotalRabCount];
-[KCellularWcdmaRabStatus hsRabCount];
-[KCellularWcdmaRabStatus r99RabCount];
-[KCellularWcdmaRabStatus setHasHsRabCount:];
-[KCellularWcdmaRabStatus setHasR99RabCount:];
-[KCellularWcdmaRabStatus setHasTotalRabCount:];
-[KCellularWcdmaRabStatus setHsRabCount:];
-[KCellularWcdmaRabStatus setTotalRabCount:];
-[KCellularWcdmaRabStatus totalRabCount];
```
