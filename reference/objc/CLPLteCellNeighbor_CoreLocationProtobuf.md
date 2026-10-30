# `CLPLteCellNeighbor`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 9 instance variables, 16 properties, 41 instance methods, 0 class methods

## Instance variables

```
I _bandwidth;
i _ecn0;
I _maxThroughput;
I _neighborType;
i _pid;
i _rscp;
i _rssi;
i _uarfcn;
{?="bandwidth"b1"ecn0"b1"maxThroughput"b1"neighborType"b1"pid"b1"rscp"b1"rssi"b1"uarfcn"b1} _has;
```

## Properties

```
@property (TB,N) hasUarfcn;
@property (Ti,N,V_uarfcn) uarfcn;
@property (TB,N) hasPid;
@property (Ti,N,V_pid) pid;
@property (TB,N) hasRssi;
@property (Ti,N,V_rssi) rssi;
@property (TB,N) hasEcn0;
@property (Ti,N,V_ecn0) ecn0;
@property (TB,N) hasRscp;
@property (Ti,N,V_rscp) rscp;
@property (TB,N) hasBandwidth;
@property (TI,N,V_bandwidth) bandwidth;
@property (TB,N) hasNeighborType;
@property (TI,N,V_neighborType) neighborType;
@property (TB,N) hasMaxThroughput;
@property (TI,N,V_maxThroughput) maxThroughput;
```

## Instance methods

```
-[CLPLteCellNeighbor rssi];
-[CLPLteCellNeighbor rscp];
-[CLPLteCellNeighbor hasPid];
-[CLPLteCellNeighbor setPid:];
-[CLPLteCellNeighbor hasMaxThroughput];
-[CLPLteCellNeighbor writeTo:];
-[CLPLteCellNeighbor setHasPid:];
-[CLPLteCellNeighbor hasEcn0];
-[CLPLteCellNeighbor mergeFrom:];
-[CLPLteCellNeighbor setRssi:];
-[CLPLteCellNeighbor hasBandwidth];
-[CLPLteCellNeighbor setHasRscp:];
-[CLPLteCellNeighbor setMaxThroughput:];
-[CLPLteCellNeighbor setHasMaxThroughput:];
-[CLPLteCellNeighbor pid];
-[CLPLteCellNeighbor hasRscp];
-[CLPLteCellNeighbor hasUarfcn];
-[CLPLteCellNeighbor setHasUarfcn:];
-[CLPLteCellNeighbor uarfcn];
-[CLPLteCellNeighbor setHasBandwidth:];
-[CLPLteCellNeighbor hasRssi];
-[CLPLteCellNeighbor setBandwidth:];
-[CLPLteCellNeighbor maxThroughput];
-[CLPLteCellNeighbor hash];
-[CLPLteCellNeighbor copyTo:];
-[CLPLteCellNeighbor description];
-[CLPLteCellNeighbor setRscp:];
-[CLPLteCellNeighbor setHasRssi:];
-[CLPLteCellNeighbor bandwidth];
-[CLPLteCellNeighbor readFrom:];
-[CLPLteCellNeighbor copyWithZone:];
-[CLPLteCellNeighbor setUarfcn:];
-[CLPLteCellNeighbor isEqual:];
-[CLPLteCellNeighbor setEcn0:];
-[CLPLteCellNeighbor dictionaryRepresentation];
-[CLPLteCellNeighbor setHasEcn0:];
-[CLPLteCellNeighbor ecn0];
-[CLPLteCellNeighbor hasNeighborType];
-[CLPLteCellNeighbor neighborType];
-[CLPLteCellNeighbor setHasNeighborType:];
-[CLPLteCellNeighbor setNeighborType:];
```
