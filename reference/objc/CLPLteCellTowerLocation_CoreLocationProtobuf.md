# `CLPLteCellTowerLocation`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 35 instance variables, 62 properties, 131 instance methods, 1 class methods

## Instance variables

```
d _cellLatitude;
d _cellLongitude;
@"NSString" _appBundleId;
i _bandInfo;
i _bandwidth;
i _ci;
I _csgId;
I _csgIndication;
I _deploymentType;
I _downlinkBandwidth;
i _ecn0;
I _latency;
@"CLPLocation" _location;
I _maxThroughput;
i _mcc;
i _mnc;
@"CLPCellNeighborsGroup" _neighborGroup;
@"NSMutableArray" _neighbors;
@"NSString" _npnCsgIdEf;
@"NSString" _npnNwIdEf;
@"NSString" _operatorName;
i _pid;
I _pmax;
i _rscp;
i _rssi;
i _serverHash;
@"NSString" _serviceProviderName;
i _tac;
i _timingAdvance;
i _uarfcn;
B _hasWifiFallback;
B _isLimitedService;
B _isStalled;
B _uniqueCount;
{?="cellLatitude"b1"cellLongitude"b1"bandInfo"b1"bandwidth"b1"csgId"b1"csgIndication"b1"deploymentType"b1"downlinkBandwidth"b1"ecn0"b1"latency"b1"maxThroughput"b1"pid"b1"pmax"b1"rscp"b1"rssi"b1"serverHash"b1"timingAdvance"b1"uarfcn"b1"hasWifiFallback"b1"isLimitedService"b1"isStalled"b1"uniqueCount"b1} _has;
```

## Properties

```
@property (Ti,N,V_mcc) mcc;
@property (Ti,N,V_mnc) mnc;
@property (Ti,N,V_tac) tac;
@property (Ti,N,V_ci) ci;
@property (TB,N) hasUarfcn;
@property (Ti,N,V_uarfcn) uarfcn;
@property (TB,N) hasPid;
@property (Ti,N,V_pid) pid;
@property (TB,N) hasBandInfo;
@property (Ti,N,V_bandInfo) bandInfo;
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
@property (TB,N) hasDeploymentType;
@property (TI,N,V_deploymentType) deploymentType;
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
@property (TB,N) hasCsgIndication;
@property (TI,N,V_csgIndication) csgIndication;
@property (TB,N) hasCsgId;
@property (TI,N,V_csgId) csgId;
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
+[CLPLteCellTowerLocation neighborType];
```

## Instance methods

```
-[CLPLteCellTowerLocation tac];
-[CLPLteCellTowerLocation rssi];
-[CLPLteCellTowerLocation rscp];
-[CLPLteCellTowerLocation ci];
-[CLPLteCellTowerLocation hasCsgId];
-[CLPLteCellTowerLocation pmax];
-[CLPLteCellTowerLocation setLatency:];
-[CLPLteCellTowerLocation hasPid];
-[CLPLteCellTowerLocation appBundleId];
-[CLPLteCellTowerLocation bandInfo];
-[CLPLteCellTowerLocation clearNeighbors];
-[CLPLteCellTowerLocation setIsLimitedService:];
-[CLPLteCellTowerLocation setPid:];
-[CLPLteCellTowerLocation latency];
-[CLPLteCellTowerLocation setOperatorName:];
-[CLPLteCellTowerLocation hasMaxThroughput];
-[CLPLteCellTowerLocation writeTo:];
-[CLPLteCellTowerLocation hasHasWifiFallback];
-[CLPLteCellTowerLocation hasNpnNwIdEf];
-[CLPLteCellTowerLocation setHasCsgId:];
-[CLPLteCellTowerLocation setHasPid:];
-[CLPLteCellTowerLocation isStalled];
-[CLPLteCellTowerLocation setNeighbors:];
-[CLPLteCellTowerLocation setDownlinkBandwidth:];
-[CLPLteCellTowerLocation neighborGroup];
-[CLPLteCellTowerLocation setCsgIndication:];
-[CLPLteCellTowerLocation hasDownlinkBandwidth];
-[CLPLteCellTowerLocation setAppBundleId:];
-[CLPLteCellTowerLocation serviceProviderName];
-[CLPLteCellTowerLocation setHasTimingAdvance:];
-[CLPLteCellTowerLocation hasEcn0];
-[CLPLteCellTowerLocation setHasDownlinkBandwidth:];
-[CLPLteCellTowerLocation hasUniqueCount];
-[CLPLteCellTowerLocation location];
-[CLPLteCellTowerLocation setNeighborGroup:];
-[CLPLteCellTowerLocation mergeFrom:];
-[CLPLteCellTowerLocation hasIsLimitedService];
-[CLPLteCellTowerLocation hasLatency];
-[CLPLteCellTowerLocation hasCellLatitude];
-[CLPLteCellTowerLocation hasAppBundleId];
-[CLPLteCellTowerLocation setServerHash:];
-[CLPLteCellTowerLocation setRssi:];
-[CLPLteCellTowerLocation hasBandwidth];
-[CLPLteCellTowerLocation hasNeighborGroup];
-[CLPLteCellTowerLocation neighborsCount];
-[CLPLteCellTowerLocation hasOperatorName];
-[CLPLteCellTowerLocation setNpnCsgIdEf:];
-[CLPLteCellTowerLocation operatorName];
-[CLPLteCellTowerLocation setHasRscp:];
-[CLPLteCellTowerLocation timingAdvance];
-[CLPLteCellTowerLocation setMaxThroughput:];
-[CLPLteCellTowerLocation hasNpnCsgIdEf];
-[CLPLteCellTowerLocation hasWifiFallback];
-[CLPLteCellTowerLocation isLimitedService];
-[CLPLteCellTowerLocation setHasCsgIndication:];
-[CLPLteCellTowerLocation setHasBandInfo:];
-[CLPLteCellTowerLocation setServiceProviderName:];
-[CLPLteCellTowerLocation serverHash];
-[CLPLteCellTowerLocation setUniqueCount:];
-[CLPLteCellTowerLocation npnCsgIdEf];
-[CLPLteCellTowerLocation setDeploymentType:];
-[CLPLteCellTowerLocation setHasHasWifiFallback:];
-[CLPLteCellTowerLocation setHasMaxThroughput:];
-[CLPLteCellTowerLocation setHasServerHash:];
-[CLPLteCellTowerLocation setHasLatency:];
-[CLPLteCellTowerLocation setTac:];
-[CLPLteCellTowerLocation pid];
-[CLPLteCellTowerLocation downlinkBandwidth];
-[CLPLteCellTowerLocation mnc];
-[CLPLteCellTowerLocation csgId];
-[CLPLteCellTowerLocation hasRscp];
-[CLPLteCellTowerLocation hasServerHash];
-[CLPLteCellTowerLocation hasUarfcn];
-[CLPLteCellTowerLocation setLocation:];
-[CLPLteCellTowerLocation setHasUarfcn:];
-[CLPLteCellTowerLocation hasTimingAdvance];
-[CLPLteCellTowerLocation uarfcn];
-[CLPLteCellTowerLocation setHasBandwidth:];
-[CLPLteCellTowerLocation hasPmax];
-[CLPLteCellTowerLocation npnNwIdEf];
-[CLPLteCellTowerLocation setHasPmax:];
-[CLPLteCellTowerLocation setPmax:];
-[CLPLteCellTowerLocation setCsgId:];
-[CLPLteCellTowerLocation hasRssi];
-[CLPLteCellTowerLocation setHasDeploymentType:];
-[CLPLteCellTowerLocation setBandwidth:];
-[CLPLteCellTowerLocation setHasIsLimitedService:];
-[CLPLteCellTowerLocation maxThroughput];
-[CLPLteCellTowerLocation hash];
-[CLPLteCellTowerLocation setBandInfo:];
-[CLPLteCellTowerLocation copyTo:];
-[CLPLteCellTowerLocation hasServiceProviderName];
-[CLPLteCellTowerLocation setHasCellLongitude:];
-[CLPLteCellTowerLocation description];
-[CLPLteCellTowerLocation neighborAtIndex:];
-[CLPLteCellTowerLocation setHasIsStalled:];
-[CLPLteCellTowerLocation hasDeploymentType];
-[CLPLteCellTowerLocation deploymentType];
-[CLPLteCellTowerLocation setMnc:];
-[CLPLteCellTowerLocation cellLatitude];
-[CLPLteCellTowerLocation hasCsgIndication];
-[CLPLteCellTowerLocation setRscp:];
-[CLPLteCellTowerLocation setHasRssi:];
-[CLPLteCellTowerLocation csgIndication];
-[CLPLteCellTowerLocation setCi:];
-[CLPLteCellTowerLocation mcc];
-[CLPLteCellTowerLocation bandwidth];
-[CLPLteCellTowerLocation setNpnNwIdEf:];
-[CLPLteCellTowerLocation setIsStalled:];
-[CLPLteCellTowerLocation uniqueCount];
-[CLPLteCellTowerLocation hasCellLongitude];
-[CLPLteCellTowerLocation readFrom:];
-[CLPLteCellTowerLocation hasIsStalled];
-[CLPLteCellTowerLocation copyWithZone:];
-[CLPLteCellTowerLocation setCellLatitude:];
-[CLPLteCellTowerLocation setUarfcn:];
-[CLPLteCellTowerLocation setHasWifiFallback:];
-[CLPLteCellTowerLocation setHasUniqueCount:];
-[CLPLteCellTowerLocation isEqual:];
-[CLPLteCellTowerLocation setHasCellLatitude:];
-[CLPLteCellTowerLocation neighbors];
-[CLPLteCellTowerLocation setEcn0:];
-[CLPLteCellTowerLocation setTimingAdvance:];
-[CLPLteCellTowerLocation cellLongitude];
-[CLPLteCellTowerLocation hasBandInfo];
-[CLPLteCellTowerLocation setMcc:];
-[CLPLteCellTowerLocation addNeighbor:];
-[CLPLteCellTowerLocation setCellLongitude:];
-[CLPLteCellTowerLocation dictionaryRepresentation];
-[CLPLteCellTowerLocation setHasEcn0:];
-[CLPLteCellTowerLocation ecn0];
```
