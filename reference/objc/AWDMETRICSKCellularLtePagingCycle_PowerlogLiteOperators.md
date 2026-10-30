# `AWDMETRICSKCellularLtePagingCycle`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 7 instance variables, 12 properties, 33 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
I _earfcn;
I _nbMs;
I _pagingCycleMs;
I _phyCellId;
I _subsId;
{?="timestamp"b1"earfcn"b1"nbMs"b1"pagingCycleMs"b1"phyCellId"b1"subsId"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasEarfcn;
@property (TI,N,V_earfcn) earfcn;
@property (TB,N) hasNbMs;
@property (TI,N,V_nbMs) nbMs;
@property (TB,N) hasPagingCycleMs;
@property (TI,N,V_pagingCycleMs) pagingCycleMs;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
@property (TB,N) hasPhyCellId;
@property (TI,N,V_phyCellId) phyCellId;
```

## Instance methods

```
-[AWDMETRICSKCellularLtePagingCycle hasTimestamp];
-[AWDMETRICSKCellularLtePagingCycle setHasTimestamp:];
-[AWDMETRICSKCellularLtePagingCycle setTimestamp:];
-[AWDMETRICSKCellularLtePagingCycle writeTo:];
-[AWDMETRICSKCellularLtePagingCycle mergeFrom:];
-[AWDMETRICSKCellularLtePagingCycle timestamp];
-[AWDMETRICSKCellularLtePagingCycle hash];
-[AWDMETRICSKCellularLtePagingCycle copyTo:];
-[AWDMETRICSKCellularLtePagingCycle description];
-[AWDMETRICSKCellularLtePagingCycle readFrom:];
-[AWDMETRICSKCellularLtePagingCycle copyWithZone:];
-[AWDMETRICSKCellularLtePagingCycle isEqual:];
-[AWDMETRICSKCellularLtePagingCycle dictionaryRepresentation];
-[AWDMETRICSKCellularLtePagingCycle hasNbMs];
-[AWDMETRICSKCellularLtePagingCycle earfcn];
-[AWDMETRICSKCellularLtePagingCycle hasEarfcn];
-[AWDMETRICSKCellularLtePagingCycle hasPagingCycleMs];
-[AWDMETRICSKCellularLtePagingCycle hasPhyCellId];
-[AWDMETRICSKCellularLtePagingCycle hasSubsId];
-[AWDMETRICSKCellularLtePagingCycle nbMs];
-[AWDMETRICSKCellularLtePagingCycle pagingCycleMs];
-[AWDMETRICSKCellularLtePagingCycle phyCellId];
-[AWDMETRICSKCellularLtePagingCycle setEarfcn:];
-[AWDMETRICSKCellularLtePagingCycle setHasEarfcn:];
-[AWDMETRICSKCellularLtePagingCycle setHasNbMs:];
-[AWDMETRICSKCellularLtePagingCycle setHasPagingCycleMs:];
-[AWDMETRICSKCellularLtePagingCycle setHasPhyCellId:];
-[AWDMETRICSKCellularLtePagingCycle setHasSubsId:];
-[AWDMETRICSKCellularLtePagingCycle setNbMs:];
-[AWDMETRICSKCellularLtePagingCycle setPagingCycleMs:];
-[AWDMETRICSKCellularLtePagingCycle setPhyCellId:];
-[AWDMETRICSKCellularLtePagingCycle setSubsId:];
-[AWDMETRICSKCellularLtePagingCycle subsId];
```
