# `CLPCellTowerLocation`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 22 instance variables, 35 properties, 79 instance methods, 1 class methods

## Instance variables

```
@"NSString" _appBundleId;
i _arfcn;
i _ci;
i _ecn0;
i _lac;
@"CLPLocation" _location;
i _mcc;
i _mnc;
@"CLPCellNeighborsGroup" _neighborGroup;
@"NSMutableArray" _neighbors;
@"NSString" _operatorName;
i _psc;
i _rat;
i _rscp;
i _rssi;
i _serverHash;
@"NSString" _serviceProviderName;
i _transmit;
B _hasWifiFallback;
B _isLimitedService;
B _uniqueCount;
{?="arfcn"b1"ecn0"b1"psc"b1"rat"b1"rscp"b1"serverHash"b1"transmit"b1"hasWifiFallback"b1"isLimitedService"b1"uniqueCount"b1} _has;
```

## Properties

```
@property (Ti,N,V_mcc) mcc;
@property (Ti,N,V_mnc) mnc;
@property (Ti,N,V_lac) lac;
@property (Ti,N,V_ci) ci;
@property (Ti,N,V_rssi) rssi;
@property (TB,N) hasArfcn;
@property (Ti,N,V_arfcn) arfcn;
@property (TB,N) hasPsc;
@property (Ti,N,V_psc) psc;
@property (T@"CLPLocation",&,N,V_location) location;
@property (TB,R,N) hasAppBundleId;
@property (T@"NSString",&,N,V_appBundleId) appBundleId;
@property (TB,N) hasServerHash;
@property (Ti,N,V_serverHash) serverHash;
@property (TB,N) hasTransmit;
@property (Ti,N,V_transmit) transmit;
@property (TB,R,N) hasOperatorName;
@property (T@"NSString",&,N,V_operatorName) operatorName;
@property (TB,N) hasEcn0;
@property (Ti,N,V_ecn0) ecn0;
@property (TB,N) hasRscp;
@property (Ti,N,V_rscp) rscp;
@property (TB,N) hasRat;
@property (Ti,N,V_rat) rat;
@property (T@"NSMutableArray",&,N,V_neighbors) neighbors;
@property (TB,R,N) hasNeighborGroup;
@property (T@"CLPCellNeighborsGroup",&,N,V_neighborGroup) neighborGroup;
@property (TB,N) hasIsLimitedService;
@property (TB,N,V_isLimitedService) isLimitedService;
@property (TB,R,N) hasServiceProviderName;
@property (T@"NSString",&,N,V_serviceProviderName) serviceProviderName;
@property (TB,N) hasUniqueCount;
@property (TB,N,V_uniqueCount) uniqueCount;
@property (TB,N) hasHasWifiFallback;
@property (TB,N,V_hasWifiFallback) hasWifiFallback;
```

## Class methods

```
+[CLPCellTowerLocation neighborType];
```

## Instance methods

```
-[CLPCellTowerLocation lac];
-[CLPCellTowerLocation rssi];
-[CLPCellTowerLocation rscp];
-[CLPCellTowerLocation ci];
-[CLPCellTowerLocation appBundleId];
-[CLPCellTowerLocation clearNeighbors];
-[CLPCellTowerLocation setIsLimitedService:];
-[CLPCellTowerLocation setLac:];
-[CLPCellTowerLocation setOperatorName:];
-[CLPCellTowerLocation writeTo:];
-[CLPCellTowerLocation hasHasWifiFallback];
-[CLPCellTowerLocation setNeighbors:];
-[CLPCellTowerLocation neighborGroup];
-[CLPCellTowerLocation setAppBundleId:];
-[CLPCellTowerLocation serviceProviderName];
-[CLPCellTowerLocation hasEcn0];
-[CLPCellTowerLocation hasUniqueCount];
-[CLPCellTowerLocation location];
-[CLPCellTowerLocation setNeighborGroup:];
-[CLPCellTowerLocation mergeFrom:];
-[CLPCellTowerLocation hasIsLimitedService];
-[CLPCellTowerLocation hasAppBundleId];
-[CLPCellTowerLocation setServerHash:];
-[CLPCellTowerLocation setRssi:];
-[CLPCellTowerLocation hasNeighborGroup];
-[CLPCellTowerLocation neighborsCount];
-[CLPCellTowerLocation hasOperatorName];
-[CLPCellTowerLocation operatorName];
-[CLPCellTowerLocation setHasRscp:];
-[CLPCellTowerLocation hasWifiFallback];
-[CLPCellTowerLocation isLimitedService];
-[CLPCellTowerLocation setServiceProviderName:];
-[CLPCellTowerLocation serverHash];
-[CLPCellTowerLocation setUniqueCount:];
-[CLPCellTowerLocation rat];
-[CLPCellTowerLocation setHasHasWifiFallback:];
-[CLPCellTowerLocation setHasServerHash:];
-[CLPCellTowerLocation mnc];
-[CLPCellTowerLocation hasRscp];
-[CLPCellTowerLocation hasServerHash];
-[CLPCellTowerLocation setLocation:];
-[CLPCellTowerLocation setHasIsLimitedService:];
-[CLPCellTowerLocation hash];
-[CLPCellTowerLocation copyTo:];
-[CLPCellTowerLocation hasServiceProviderName];
-[CLPCellTowerLocation description];
-[CLPCellTowerLocation neighborAtIndex:];
-[CLPCellTowerLocation setMnc:];
-[CLPCellTowerLocation setRscp:];
-[CLPCellTowerLocation setCi:];
-[CLPCellTowerLocation mcc];
-[CLPCellTowerLocation uniqueCount];
-[CLPCellTowerLocation readFrom:];
-[CLPCellTowerLocation copyWithZone:];
-[CLPCellTowerLocation setHasWifiFallback:];
-[CLPCellTowerLocation setHasUniqueCount:];
-[CLPCellTowerLocation isEqual:];
-[CLPCellTowerLocation neighbors];
-[CLPCellTowerLocation setEcn0:];
-[CLPCellTowerLocation setMcc:];
-[CLPCellTowerLocation addNeighbor:];
-[CLPCellTowerLocation dictionaryRepresentation];
-[CLPCellTowerLocation setHasEcn0:];
-[CLPCellTowerLocation ecn0];
-[CLPCellTowerLocation setRat:];
-[CLPCellTowerLocation hasRat];
-[CLPCellTowerLocation setHasRat:];
-[CLPCellTowerLocation setPsc:];
-[CLPCellTowerLocation psc];
-[CLPCellTowerLocation setHasTransmit:];
-[CLPCellTowerLocation arfcn];
-[CLPCellTowerLocation hasArfcn];
-[CLPCellTowerLocation hasPsc];
-[CLPCellTowerLocation hasTransmit];
-[CLPCellTowerLocation setArfcn:];
-[CLPCellTowerLocation setHasArfcn:];
-[CLPCellTowerLocation setHasPsc:];
-[CLPCellTowerLocation setTransmit:];
-[CLPCellTowerLocation transmit];
```
