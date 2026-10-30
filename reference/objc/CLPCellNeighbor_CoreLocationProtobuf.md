# `CLPCellNeighbor`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 6 instance variables, 10 properties, 29 instance methods, 0 class methods

## Instance variables

```
i _ecn0;
i _psc;
i _rscp;
i _rssi;
i _uarfcn;
{?="ecn0"b1"psc"b1"rscp"b1"rssi"b1"uarfcn"b1} _has;
```

## Properties

```
@property (TB,N) hasUarfcn;
@property (Ti,N,V_uarfcn) uarfcn;
@property (TB,N) hasPsc;
@property (Ti,N,V_psc) psc;
@property (TB,N) hasRssi;
@property (Ti,N,V_rssi) rssi;
@property (TB,N) hasEcn0;
@property (Ti,N,V_ecn0) ecn0;
@property (TB,N) hasRscp;
@property (Ti,N,V_rscp) rscp;
```

## Instance methods

```
-[CLPCellNeighbor rssi];
-[CLPCellNeighbor rscp];
-[CLPCellNeighbor writeTo:];
-[CLPCellNeighbor hasEcn0];
-[CLPCellNeighbor mergeFrom:];
-[CLPCellNeighbor setRssi:];
-[CLPCellNeighbor setHasRscp:];
-[CLPCellNeighbor hasRscp];
-[CLPCellNeighbor hasUarfcn];
-[CLPCellNeighbor setHasUarfcn:];
-[CLPCellNeighbor uarfcn];
-[CLPCellNeighbor hasRssi];
-[CLPCellNeighbor hash];
-[CLPCellNeighbor copyTo:];
-[CLPCellNeighbor description];
-[CLPCellNeighbor setRscp:];
-[CLPCellNeighbor setHasRssi:];
-[CLPCellNeighbor readFrom:];
-[CLPCellNeighbor copyWithZone:];
-[CLPCellNeighbor setUarfcn:];
-[CLPCellNeighbor isEqual:];
-[CLPCellNeighbor setEcn0:];
-[CLPCellNeighbor dictionaryRepresentation];
-[CLPCellNeighbor setHasEcn0:];
-[CLPCellNeighbor ecn0];
-[CLPCellNeighbor setPsc:];
-[CLPCellNeighbor psc];
-[CLPCellNeighbor hasPsc];
-[CLPCellNeighbor setHasPsc:];
```
