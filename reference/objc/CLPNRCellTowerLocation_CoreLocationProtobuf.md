# `CLPNRCellTowerLocation`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 35 instance variables, 67 properties, 140 instance methods, 1 class methods

## Instance variables

```
d _cellLatitude;
d _cellLongitude;
q _ci;
@"NSString" _appBundleId;
i _bandInfo;
i _bandwidth;
I _bwpSupport;
I _downlinkBandwidth;
i _ecn0;
I _gscn;
I _latency;
@"CLPLocation" _location;
I _maxThroughput;
i _mcc;
i _mnc;
@"CLPCellNeighborsGroup" _neighborGroup;
@"NSMutableArray" _neighbors;
@"NSString" _npnCsgIdEf;
@"NSString" _npnNwIdEf;
i _nrarfcn;
@"NSString" _operatorName;
i _pid;
I _pmax;
i _rscp;
i _rssi;
I _scs;
i _serverHash;
@"NSString" _serviceProviderName;
i _tac;
i _timingAdvance;
B _hasWifiFallback;
B _isLimitedService;
B _isStalled;
B _uniqueCount;
{?="cellLatitude"b1"cellLongitude"b1"ci"b1"bandInfo"b1"bandwidth"b1"bwpSupport"b1"downlinkBandwidth"b1"ecn0"b1"gscn"b1"latency"b1"maxThroughput"b1"mcc"b1"mnc"b1"nrarfcn"b1"pid"b1"pmax"b1"rscp"b1"rssi"b1"scs"b1"serverHash"b1"tac"b1"timingAdvance"b1"hasWifiFallback"b1"isLimitedService"b1"isStalled"b1"uniqueCount"b1} _has;
```

## Properties

```
@property (TB,N) hasMcc;
@property (Ti,N,V_mcc) mcc;
@property (TB,N) hasMnc;
@property (Ti,N,V_mnc) mnc;
@property (TB,N) hasTac;
@property (Ti,N,V_tac) tac;
@property (TB,N) hasCi;
@property (Tq,N,V_ci) ci;
@property (TB,N) hasNrarfcn;
@property (Ti,N,V_nrarfcn) nrarfcn;
@property (TB,N) hasPid;
@property (Ti,N,V_pid) pid;
@property (TB,N) hasBandInfo;
@property (Ti,N,V_bandInfo) bandInfo;
@property (TB,R,N) hasLocation;
@property (T@"CLPLocation",&,N,V_location) location;
@property (TB,R,N) hasAppBundleId;
@property (T@"NSString",&,N,V_appBundleId) appBundleId;
@property (TB,R,N) hasOperatorName;
@property (T@"NSString",&,N,V_operatorName) operatorName;
@property (TB,N) hasCellLatitude;
@property (Td,N,V_cellLatitude) cellLatitude;
@property (TB,N) hasCellLongitude;
@property (Td,N,V_cellLongitude) cellLongitude;
@property (TB,N) hasServerHash;
@property (Ti,N,V_serverHash) serverHash;
@property (TB,N) hasEcn0;
@property (Ti,N,V_ecn0) ecn0;
@property (TB,N) hasRscp;
@property (Ti,N,V_rscp) rscp;
@property (TB,N) hasRssi;
@property (Ti,N,V_rssi) rssi;
@property (T@"NSMutableArray",&,N,V_neighbors) neighbors;
@property (TB,R,N) hasNeighborGroup;
@property (T@"CLPCellNeighborsGroup",&,N,V_neighborGroup) neighborGroup;
@property (TB,N) hasBandwidth;
@property (Ti,N,V_bandwidth) bandwidth;
@property (TB,N) hasIsLimitedService;
@property (TB,N,V_isLimitedService) isLimitedService;
@property (TB,R,N) hasServiceProviderName;
@property (T@"NSString",&,N,V_serviceProviderName) serviceProviderName;
@property (TB,N) hasScs;
@property (TI,N,V_scs) scs;
@property (TB,N) hasGscn;
@property (TI,N,V_gscn) gscn;
@property (TB,N) hasDownlinkBandwidth;
@property (TI,N,V_downlinkBandwidth) downlinkBandwidth;
@property (TB,N) hasIsStalled;
@property (TB,N,V_isStalled) isStalled;
@property (TB,N) hasLatency;
@property (TI,N,V_latency) latency;
@property (TB,N) hasPmax;
@property (TI,N,V_pmax) pmax;
@property (TB,N) hasMaxThroughput;
@property (TI,N,V_maxThroughput) maxThroughput;
@property (TB,N) hasBwpSupport;
@property (TI,N,V_bwpSupport) bwpSupport;
@property (TB,N) hasTimingAdvance;
@property (Ti,N,V_timingAdvance) timingAdvance;
@property (TB,N) hasUniqueCount;
@property (TB,N,V_uniqueCount) uniqueCount;
@property (TB,N) hasHasWifiFallback;
@property (TB,N,V_hasWifiFallback) hasWifiFallback;
@property (TB,R,N) hasNpnNwIdEf;
@property (T@"NSString",&,N,V_npnNwIdEf) npnNwIdEf;
@property (TB,R,N) hasNpnCsgIdEf;
@property (T@"NSString",&,N,V_npnCsgIdEf) npnCsgIdEf;
```

## Class methods

```
+[CLPNRCellTowerLocation neighborType];
```

## Instance methods

```
-[CLPNRCellTowerLocation tac];
-[CLPNRCellTowerLocation rssi];
-[CLPNRCellTowerLocation rscp];
-[CLPNRCellTowerLocation ci];
-[CLPNRCellTowerLocation pmax];
-[CLPNRCellTowerLocation setLatency:];
-[CLPNRCellTowerLocation hasPid];
-[CLPNRCellTowerLocation appBundleId];
-[CLPNRCellTowerLocation bandInfo];
-[CLPNRCellTowerLocation clearNeighbors];
-[CLPNRCellTowerLocation setIsLimitedService:];
-[CLPNRCellTowerLocation setPid:];
-[CLPNRCellTowerLocation latency];
-[CLPNRCellTowerLocation setOperatorName:];
-[CLPNRCellTowerLocation hasMaxThroughput];
-[CLPNRCellTowerLocation writeTo:];
-[CLPNRCellTowerLocation hasHasWifiFallback];
-[CLPNRCellTowerLocation hasNpnNwIdEf];
-[CLPNRCellTowerLocation setHasPid:];
-[CLPNRCellTowerLocation isStalled];
-[CLPNRCellTowerLocation setNeighbors:];
-[CLPNRCellTowerLocation setDownlinkBandwidth:];
-[CLPNRCellTowerLocation neighborGroup];
-[CLPNRCellTowerLocation hasDownlinkBandwidth];
-[CLPNRCellTowerLocation setAppBundleId:];
-[CLPNRCellTowerLocation serviceProviderName];
-[CLPNRCellTowerLocation setHasTimingAdvance:];
-[CLPNRCellTowerLocation hasLocation];
-[CLPNRCellTowerLocation hasEcn0];
-[CLPNRCellTowerLocation setHasDownlinkBandwidth:];
-[CLPNRCellTowerLocation hasUniqueCount];
-[CLPNRCellTowerLocation location];
-[CLPNRCellTowerLocation setNeighborGroup:];
-[CLPNRCellTowerLocation mergeFrom:];
-[CLPNRCellTowerLocation hasIsLimitedService];
-[CLPNRCellTowerLocation hasLatency];
-[CLPNRCellTowerLocation hasCellLatitude];
-[CLPNRCellTowerLocation hasAppBundleId];
-[CLPNRCellTowerLocation setServerHash:];
-[CLPNRCellTowerLocation setRssi:];
-[CLPNRCellTowerLocation hasBandwidth];
-[CLPNRCellTowerLocation hasNeighborGroup];
-[CLPNRCellTowerLocation neighborsCount];
-[CLPNRCellTowerLocation hasOperatorName];
-[CLPNRCellTowerLocation setNpnCsgIdEf:];
-[CLPNRCellTowerLocation operatorName];
-[CLPNRCellTowerLocation setHasRscp:];
-[CLPNRCellTowerLocation timingAdvance];
-[CLPNRCellTowerLocation setMaxThroughput:];
-[CLPNRCellTowerLocation hasNpnCsgIdEf];
-[CLPNRCellTowerLocation hasWifiFallback];
-[CLPNRCellTowerLocation isLimitedService];
-[CLPNRCellTowerLocation setHasBandInfo:];
-[CLPNRCellTowerLocation setServiceProviderName:];
-[CLPNRCellTowerLocation serverHash];
-[CLPNRCellTowerLocation setUniqueCount:];
-[CLPNRCellTowerLocation npnCsgIdEf];
-[CLPNRCellTowerLocation setHasHasWifiFallback:];
-[CLPNRCellTowerLocation setHasMaxThroughput:];
-[CLPNRCellTowerLocation setHasServerHash:];
-[CLPNRCellTowerLocation setHasLatency:];
-[CLPNRCellTowerLocation setTac:];
-[CLPNRCellTowerLocation pid];
-[CLPNRCellTowerLocation downlinkBandwidth];
-[CLPNRCellTowerLocation mnc];
-[CLPNRCellTowerLocation hasRscp];
-[CLPNRCellTowerLocation hasServerHash];
-[CLPNRCellTowerLocation setLocation:];
-[CLPNRCellTowerLocation hasTimingAdvance];
-[CLPNRCellTowerLocation setHasBandwidth:];
-[CLPNRCellTowerLocation hasPmax];
-[CLPNRCellTowerLocation npnNwIdEf];
-[CLPNRCellTowerLocation setHasPmax:];
-[CLPNRCellTowerLocation setPmax:];
-[CLPNRCellTowerLocation hasRssi];
-[CLPNRCellTowerLocation setBandwidth:];
-[CLPNRCellTowerLocation setHasIsLimitedService:];
-[CLPNRCellTowerLocation maxThroughput];
-[CLPNRCellTowerLocation hash];
-[CLPNRCellTowerLocation setBandInfo:];
-[CLPNRCellTowerLocation copyTo:];
-[CLPNRCellTowerLocation hasServiceProviderName];
-[CLPNRCellTowerLocation setHasCellLongitude:];
-[CLPNRCellTowerLocation description];
-[CLPNRCellTowerLocation neighborAtIndex:];
-[CLPNRCellTowerLocation setHasIsStalled:];
-[CLPNRCellTowerLocation setMnc:];
-[CLPNRCellTowerLocation cellLatitude];
-[CLPNRCellTowerLocation setRscp:];
-[CLPNRCellTowerLocation setHasRssi:];
-[CLPNRCellTowerLocation setCi:];
-[CLPNRCellTowerLocation mcc];
-[CLPNRCellTowerLocation bandwidth];
-[CLPNRCellTowerLocation setNpnNwIdEf:];
-[CLPNRCellTowerLocation setIsStalled:];
-[CLPNRCellTowerLocation uniqueCount];
-[CLPNRCellTowerLocation hasCellLongitude];
-[CLPNRCellTowerLocation readFrom:];
-[CLPNRCellTowerLocation hasIsStalled];
-[CLPNRCellTowerLocation copyWithZone:];
-[CLPNRCellTowerLocation setCellLatitude:];
-[CLPNRCellTowerLocation setHasWifiFallback:];
-[CLPNRCellTowerLocation setHasUniqueCount:];
-[CLPNRCellTowerLocation isEqual:];
-[CLPNRCellTowerLocation setHasCellLatitude:];
-[CLPNRCellTowerLocation neighbors];
-[CLPNRCellTowerLocation setEcn0:];
-[CLPNRCellTowerLocation setTimingAdvance:];
-[CLPNRCellTowerLocation cellLongitude];
-[CLPNRCellTowerLocation hasBandInfo];
-[CLPNRCellTowerLocation setMcc:];
-[CLPNRCellTowerLocation addNeighbor:];
-[CLPNRCellTowerLocation setCellLongitude:];
-[CLPNRCellTowerLocation dictionaryRepresentation];
-[CLPNRCellTowerLocation setHasEcn0:];
-[CLPNRCellTowerLocation ecn0];
-[CLPNRCellTowerLocation hasGscn];
-[CLPNRCellTowerLocation scs];
-[CLPNRCellTowerLocation setScs:];
-[CLPNRCellTowerLocation nrarfcn];
-[CLPNRCellTowerLocation bwpSupport];
-[CLPNRCellTowerLocation gscn];
-[CLPNRCellTowerLocation hasBwpSupport];
-[CLPNRCellTowerLocation hasCi];
-[CLPNRCellTowerLocation hasMcc];
-[CLPNRCellTowerLocation hasMnc];
-[CLPNRCellTowerLocation hasNrarfcn];
-[CLPNRCellTowerLocation hasScs];
-[CLPNRCellTowerLocation hasTac];
-[CLPNRCellTowerLocation setBwpSupport:];
-[CLPNRCellTowerLocation setGscn:];
-[CLPNRCellTowerLocation setHasBwpSupport:];
-[CLPNRCellTowerLocation setHasCi:];
-[CLPNRCellTowerLocation setHasGscn:];
-[CLPNRCellTowerLocation setHasMcc:];
-[CLPNRCellTowerLocation setHasMnc:];
-[CLPNRCellTowerLocation setHasNrarfcn:];
-[CLPNRCellTowerLocation setHasScs:];
-[CLPNRCellTowerLocation setHasTac:];
-[CLPNRCellTowerLocation setNrarfcn:];
```
