# `CLPSCdmaCellTowerLocation`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 20 instance variables, 31 properties, 71 instance methods, 1 class methods

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
B _isLimitedService;
{?="arfcn"b1"ecn0"b1"psc"b1"rat"b1"rscp"b1"serverHash"b1"transmit"b1"isLimitedService"b1} _has;
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
```

## Class methods

```
+[CLPSCdmaCellTowerLocation neighborType];
```

## Instance methods

```
-[CLPSCdmaCellTowerLocation lac];
-[CLPSCdmaCellTowerLocation rssi];
-[CLPSCdmaCellTowerLocation rscp];
-[CLPSCdmaCellTowerLocation ci];
-[CLPSCdmaCellTowerLocation appBundleId];
-[CLPSCdmaCellTowerLocation clearNeighbors];
-[CLPSCdmaCellTowerLocation setIsLimitedService:];
-[CLPSCdmaCellTowerLocation setLac:];
-[CLPSCdmaCellTowerLocation setOperatorName:];
-[CLPSCdmaCellTowerLocation writeTo:];
-[CLPSCdmaCellTowerLocation setNeighbors:];
-[CLPSCdmaCellTowerLocation neighborGroup];
-[CLPSCdmaCellTowerLocation setAppBundleId:];
-[CLPSCdmaCellTowerLocation serviceProviderName];
-[CLPSCdmaCellTowerLocation hasEcn0];
-[CLPSCdmaCellTowerLocation location];
-[CLPSCdmaCellTowerLocation setNeighborGroup:];
-[CLPSCdmaCellTowerLocation mergeFrom:];
-[CLPSCdmaCellTowerLocation hasIsLimitedService];
-[CLPSCdmaCellTowerLocation hasAppBundleId];
-[CLPSCdmaCellTowerLocation setServerHash:];
-[CLPSCdmaCellTowerLocation setRssi:];
-[CLPSCdmaCellTowerLocation hasNeighborGroup];
-[CLPSCdmaCellTowerLocation neighborsCount];
-[CLPSCdmaCellTowerLocation hasOperatorName];
-[CLPSCdmaCellTowerLocation operatorName];
-[CLPSCdmaCellTowerLocation setHasRscp:];
-[CLPSCdmaCellTowerLocation isLimitedService];
-[CLPSCdmaCellTowerLocation setServiceProviderName:];
-[CLPSCdmaCellTowerLocation serverHash];
-[CLPSCdmaCellTowerLocation rat];
-[CLPSCdmaCellTowerLocation setHasServerHash:];
-[CLPSCdmaCellTowerLocation mnc];
-[CLPSCdmaCellTowerLocation hasRscp];
-[CLPSCdmaCellTowerLocation hasServerHash];
-[CLPSCdmaCellTowerLocation setLocation:];
-[CLPSCdmaCellTowerLocation setHasIsLimitedService:];
-[CLPSCdmaCellTowerLocation hash];
-[CLPSCdmaCellTowerLocation copyTo:];
-[CLPSCdmaCellTowerLocation hasServiceProviderName];
-[CLPSCdmaCellTowerLocation description];
-[CLPSCdmaCellTowerLocation neighborAtIndex:];
-[CLPSCdmaCellTowerLocation setMnc:];
-[CLPSCdmaCellTowerLocation setRscp:];
-[CLPSCdmaCellTowerLocation setCi:];
-[CLPSCdmaCellTowerLocation mcc];
-[CLPSCdmaCellTowerLocation readFrom:];
-[CLPSCdmaCellTowerLocation copyWithZone:];
-[CLPSCdmaCellTowerLocation isEqual:];
-[CLPSCdmaCellTowerLocation neighbors];
-[CLPSCdmaCellTowerLocation setEcn0:];
-[CLPSCdmaCellTowerLocation setMcc:];
-[CLPSCdmaCellTowerLocation addNeighbor:];
-[CLPSCdmaCellTowerLocation dictionaryRepresentation];
-[CLPSCdmaCellTowerLocation setHasEcn0:];
-[CLPSCdmaCellTowerLocation ecn0];
-[CLPSCdmaCellTowerLocation setRat:];
-[CLPSCdmaCellTowerLocation hasRat];
-[CLPSCdmaCellTowerLocation setHasRat:];
-[CLPSCdmaCellTowerLocation setPsc:];
-[CLPSCdmaCellTowerLocation psc];
-[CLPSCdmaCellTowerLocation setHasTransmit:];
-[CLPSCdmaCellTowerLocation arfcn];
-[CLPSCdmaCellTowerLocation hasArfcn];
-[CLPSCdmaCellTowerLocation hasPsc];
-[CLPSCdmaCellTowerLocation hasTransmit];
-[CLPSCdmaCellTowerLocation setArfcn:];
-[CLPSCdmaCellTowerLocation setHasArfcn:];
-[CLPSCdmaCellTowerLocation setHasPsc:];
-[CLPSCdmaCellTowerLocation setTransmit:];
-[CLPSCdmaCellTowerLocation transmit];
```
