# `CLPNRCellNeighbor`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 12 instance variables, 22 properties, 53 instance methods, 0 class methods

## Instance variables

```
I _bandwidth;
I _bwpSupport;
i _ecn0;
I _maxThroughput;
I _neighborType;
i _nrarfcn;
i _pid;
i _rscp;
i _rssi;
I _saOrNsaNeighbor;
I _scs;
{?="bandwidth"b1"bwpSupport"b1"ecn0"b1"maxThroughput"b1"neighborType"b1"nrarfcn"b1"pid"b1"rscp"b1"rssi"b1"saOrNsaNeighbor"b1"scs"b1} _has;
```

## Properties

```
@property (TB,N) hasNrarfcn;
@property (Ti,N,V_nrarfcn) nrarfcn;
@property (TB,N) hasPid;
@property (Ti,N,V_pid) pid;
@property (TB,N) hasRssi;
@property (Ti,N,V_rssi) rssi;
@property (TB,N) hasEcn0;
@property (Ti,N,V_ecn0) ecn0;
@property (TB,N) hasRscp;
@property (Ti,N,V_rscp) rscp;
@property (TB,N) hasScs;
@property (TI,N,V_scs) scs;
@property (TB,N) hasSaOrNsaNeighbor;
@property (TI,N,V_saOrNsaNeighbor) saOrNsaNeighbor;
@property (TB,N) hasBandwidth;
@property (TI,N,V_bandwidth) bandwidth;
@property (TB,N) hasNeighborType;
@property (TI,N,V_neighborType) neighborType;
@property (TB,N) hasMaxThroughput;
@property (TI,N,V_maxThroughput) maxThroughput;
@property (TB,N) hasBwpSupport;
@property (TI,N,V_bwpSupport) bwpSupport;
```

## Instance methods

```
-[CLPNRCellNeighbor rssi];
-[CLPNRCellNeighbor rscp];
-[CLPNRCellNeighbor hasPid];
-[CLPNRCellNeighbor setPid:];
-[CLPNRCellNeighbor hasMaxThroughput];
-[CLPNRCellNeighbor writeTo:];
-[CLPNRCellNeighbor setHasPid:];
-[CLPNRCellNeighbor hasEcn0];
-[CLPNRCellNeighbor mergeFrom:];
-[CLPNRCellNeighbor setRssi:];
-[CLPNRCellNeighbor hasBandwidth];
-[CLPNRCellNeighbor setHasRscp:];
-[CLPNRCellNeighbor setMaxThroughput:];
-[CLPNRCellNeighbor setHasMaxThroughput:];
-[CLPNRCellNeighbor pid];
-[CLPNRCellNeighbor hasRscp];
-[CLPNRCellNeighbor setHasBandwidth:];
-[CLPNRCellNeighbor hasRssi];
-[CLPNRCellNeighbor setBandwidth:];
-[CLPNRCellNeighbor maxThroughput];
-[CLPNRCellNeighbor hash];
-[CLPNRCellNeighbor copyTo:];
-[CLPNRCellNeighbor description];
-[CLPNRCellNeighbor setRscp:];
-[CLPNRCellNeighbor setHasRssi:];
-[CLPNRCellNeighbor bandwidth];
-[CLPNRCellNeighbor readFrom:];
-[CLPNRCellNeighbor copyWithZone:];
-[CLPNRCellNeighbor isEqual:];
-[CLPNRCellNeighbor setEcn0:];
-[CLPNRCellNeighbor dictionaryRepresentation];
-[CLPNRCellNeighbor setHasEcn0:];
-[CLPNRCellNeighbor ecn0];
-[CLPNRCellNeighbor hasNeighborType];
-[CLPNRCellNeighbor saOrNsaNeighbor];
-[CLPNRCellNeighbor scs];
-[CLPNRCellNeighbor setScs:];
-[CLPNRCellNeighbor nrarfcn];
-[CLPNRCellNeighbor bwpSupport];
-[CLPNRCellNeighbor hasBwpSupport];
-[CLPNRCellNeighbor hasNrarfcn];
-[CLPNRCellNeighbor hasSaOrNsaNeighbor];
-[CLPNRCellNeighbor hasScs];
-[CLPNRCellNeighbor neighborType];
-[CLPNRCellNeighbor setBwpSupport:];
-[CLPNRCellNeighbor setHasBwpSupport:];
-[CLPNRCellNeighbor setHasNeighborType:];
-[CLPNRCellNeighbor setHasNrarfcn:];
-[CLPNRCellNeighbor setHasSaOrNsaNeighbor:];
-[CLPNRCellNeighbor setHasScs:];
-[CLPNRCellNeighbor setNeighborType:];
-[CLPNRCellNeighbor setNrarfcn:];
-[CLPNRCellNeighbor setSaOrNsaNeighbor:];
```
