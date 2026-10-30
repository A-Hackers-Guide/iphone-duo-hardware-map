# `CLPCdmaCellTowerLocation`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 30 instance variables, 51 properties, 113 instance methods, 1 class methods

## Instance variables

```
{?="list"^i"count"Q"size"Q} _derivedMccs;
d _bsLatitude;
d _bsLongitude;
d _sectorLatitude;
d _sectorLongitude;
@"NSString" _appBundleId;
i _bandclass;
i _bsid;
i _celltype;
i _channel;
i _dayLightSavings;
i _ecn0;
@"CLPLocation" _location;
i _ltmOffset;
i _mcc;
i _mnc;
@"CLPCellNeighborsGroup" _neighborGroup;
@"NSMutableArray" _neighbors;
i _nid;
@"NSString" _operatorName;
i _pnoffset;
i _rat;
i _rscp;
@"NSString" _sectorid;
i _serverHash;
@"NSString" _serviceProviderName;
i _sid;
i _zoneid;
B _isLimitedService;
{?="bsLatitude"b1"bsLongitude"b1"sectorLatitude"b1"sectorLongitude"b1"bandclass"b1"celltype"b1"channel"b1"dayLightSavings"b1"ecn0"b1"ltmOffset"b1"pnoffset"b1"rat"b1"rscp"b1"serverHash"b1"zoneid"b1"isLimitedService"b1} _has;
```

## Properties

```
@property (Ti,N,V_mcc) mcc;
@property (Ti,N,V_mnc) mnc;
@property (Ti,N,V_sid) sid;
@property (Ti,N,V_nid) nid;
@property (Ti,N,V_bsid) bsid;
@property (TB,N) hasBsLatitude;
@property (Td,N,V_bsLatitude) bsLatitude;
@property (TB,N) hasBsLongitude;
@property (Td,N,V_bsLongitude) bsLongitude;
@property (TB,N) hasZoneid;
@property (Ti,N,V_zoneid) zoneid;
@property (TB,R,N) hasSectorid;
@property (T@"NSString",&,N,V_sectorid) sectorid;
@property (TB,N) hasSectorLatitude;
@property (Td,N,V_sectorLatitude) sectorLatitude;
@property (TB,N) hasSectorLongitude;
@property (Td,N,V_sectorLongitude) sectorLongitude;
@property (TB,N) hasBandclass;
@property (Ti,N,V_bandclass) bandclass;
@property (TB,N) hasRat;
@property (Ti,N,V_rat) rat;
@property (TB,N) hasCelltype;
@property (Ti,N,V_celltype) celltype;
@property (TB,N) hasPnoffset;
@property (Ti,N,V_pnoffset) pnoffset;
@property (TB,N) hasChannel;
@property (Ti,N,V_channel) channel;
@property (T@"CLPLocation",&,N,V_location) location;
@property (TB,R,N) hasAppBundleId;
@property (T@"NSString",&,N,V_appBundleId) appBundleId;
@property (TB,N) hasServerHash;
@property (Ti,N,V_serverHash) serverHash;
@property (TB,R,N) hasOperatorName;
@property (T@"NSString",&,N,V_operatorName) operatorName;
@property (TB,N) hasLtmOffset;
@property (Ti,N,V_ltmOffset) ltmOffset;
@property (TB,N) hasDayLightSavings;
@property (Ti,N,V_dayLightSavings) dayLightSavings;
@property (TQ,R,N) derivedMccsCount;
@property (T^i,R,N) derivedMccs;
@property (TB,N) hasEcn0;
@property (Ti,N,V_ecn0) ecn0;
@property (TB,N) hasRscp;
@property (Ti,N,V_rscp) rscp;
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
+[CLPCdmaCellTowerLocation neighborType];
```

## Instance methods

```
-[CLPCdmaCellTowerLocation rscp];
-[CLPCdmaCellTowerLocation setChannel:];
-[CLPCdmaCellTowerLocation channel];
-[CLPCdmaCellTowerLocation appBundleId];
-[CLPCdmaCellTowerLocation clearNeighbors];
-[CLPCdmaCellTowerLocation setIsLimitedService:];
-[CLPCdmaCellTowerLocation setOperatorName:];
-[CLPCdmaCellTowerLocation writeTo:];
-[CLPCdmaCellTowerLocation setNeighbors:];
-[CLPCdmaCellTowerLocation neighborGroup];
-[CLPCdmaCellTowerLocation setAppBundleId:];
-[CLPCdmaCellTowerLocation hasChannel];
-[CLPCdmaCellTowerLocation serviceProviderName];
-[CLPCdmaCellTowerLocation hasEcn0];
-[CLPCdmaCellTowerLocation location];
-[CLPCdmaCellTowerLocation setNeighborGroup:];
-[CLPCdmaCellTowerLocation mergeFrom:];
-[CLPCdmaCellTowerLocation hasIsLimitedService];
-[CLPCdmaCellTowerLocation setHasChannel:];
-[CLPCdmaCellTowerLocation hasAppBundleId];
-[CLPCdmaCellTowerLocation dealloc];
-[CLPCdmaCellTowerLocation setServerHash:];
-[CLPCdmaCellTowerLocation hasNeighborGroup];
-[CLPCdmaCellTowerLocation neighborsCount];
-[CLPCdmaCellTowerLocation hasOperatorName];
-[CLPCdmaCellTowerLocation operatorName];
-[CLPCdmaCellTowerLocation setHasRscp:];
-[CLPCdmaCellTowerLocation isLimitedService];
-[CLPCdmaCellTowerLocation setServiceProviderName:];
-[CLPCdmaCellTowerLocation serverHash];
-[CLPCdmaCellTowerLocation rat];
-[CLPCdmaCellTowerLocation setHasServerHash:];
-[CLPCdmaCellTowerLocation mnc];
-[CLPCdmaCellTowerLocation hasRscp];
-[CLPCdmaCellTowerLocation hasServerHash];
-[CLPCdmaCellTowerLocation setLocation:];
-[CLPCdmaCellTowerLocation setHasIsLimitedService:];
-[CLPCdmaCellTowerLocation hash];
-[CLPCdmaCellTowerLocation copyTo:];
-[CLPCdmaCellTowerLocation hasServiceProviderName];
-[CLPCdmaCellTowerLocation description];
-[CLPCdmaCellTowerLocation neighborAtIndex:];
-[CLPCdmaCellTowerLocation setMnc:];
-[CLPCdmaCellTowerLocation setRscp:];
-[CLPCdmaCellTowerLocation mcc];
-[CLPCdmaCellTowerLocation readFrom:];
-[CLPCdmaCellTowerLocation copyWithZone:];
-[CLPCdmaCellTowerLocation isEqual:];
-[CLPCdmaCellTowerLocation neighbors];
-[CLPCdmaCellTowerLocation setEcn0:];
-[CLPCdmaCellTowerLocation setMcc:];
-[CLPCdmaCellTowerLocation addNeighbor:];
-[CLPCdmaCellTowerLocation dictionaryRepresentation];
-[CLPCdmaCellTowerLocation setHasEcn0:];
-[CLPCdmaCellTowerLocation ecn0];
-[CLPCdmaCellTowerLocation setRat:];
-[CLPCdmaCellTowerLocation setSid:];
-[CLPCdmaCellTowerLocation sid];
-[CLPCdmaCellTowerLocation hasRat];
-[CLPCdmaCellTowerLocation setHasRat:];
-[CLPCdmaCellTowerLocation dayLightSavings];
-[CLPCdmaCellTowerLocation nid];
-[CLPCdmaCellTowerLocation sectorLongitude];
-[CLPCdmaCellTowerLocation setBsLongitude:];
-[CLPCdmaCellTowerLocation setHasCelltype:];
-[CLPCdmaCellTowerLocation setHasPnoffset:];
-[CLPCdmaCellTowerLocation setNid:];
-[CLPCdmaCellTowerLocation addDerivedMcc:];
-[CLPCdmaCellTowerLocation bandclass];
-[CLPCdmaCellTowerLocation bsLatitude];
-[CLPCdmaCellTowerLocation bsLongitude];
-[CLPCdmaCellTowerLocation bsid];
-[CLPCdmaCellTowerLocation celltype];
-[CLPCdmaCellTowerLocation clearDerivedMccs];
-[CLPCdmaCellTowerLocation derivedMccAtIndex:];
-[CLPCdmaCellTowerLocation derivedMccs];
-[CLPCdmaCellTowerLocation derivedMccsCount];
-[CLPCdmaCellTowerLocation hasBandclass];
-[CLPCdmaCellTowerLocation hasBsLatitude];
-[CLPCdmaCellTowerLocation hasBsLongitude];
-[CLPCdmaCellTowerLocation hasCelltype];
-[CLPCdmaCellTowerLocation hasDayLightSavings];
-[CLPCdmaCellTowerLocation hasLtmOffset];
-[CLPCdmaCellTowerLocation hasPnoffset];
-[CLPCdmaCellTowerLocation hasSectorLatitude];
-[CLPCdmaCellTowerLocation hasSectorLongitude];
-[CLPCdmaCellTowerLocation hasSectorid];
-[CLPCdmaCellTowerLocation hasZoneid];
-[CLPCdmaCellTowerLocation ltmOffset];
-[CLPCdmaCellTowerLocation pnoffset];
-[CLPCdmaCellTowerLocation sectorLatitude];
-[CLPCdmaCellTowerLocation sectorid];
-[CLPCdmaCellTowerLocation setBandclass:];
-[CLPCdmaCellTowerLocation setBsLatitude:];
-[CLPCdmaCellTowerLocation setBsid:];
-[CLPCdmaCellTowerLocation setCelltype:];
-[CLPCdmaCellTowerLocation setDayLightSavings:];
-[CLPCdmaCellTowerLocation setDerivedMccs:count:];
-[CLPCdmaCellTowerLocation setHasBandclass:];
-[CLPCdmaCellTowerLocation setHasBsLatitude:];
-[CLPCdmaCellTowerLocation setHasBsLongitude:];
-[CLPCdmaCellTowerLocation setHasDayLightSavings:];
-[CLPCdmaCellTowerLocation setHasLtmOffset:];
-[CLPCdmaCellTowerLocation setHasSectorLatitude:];
-[CLPCdmaCellTowerLocation setHasSectorLongitude:];
-[CLPCdmaCellTowerLocation setHasZoneid:];
-[CLPCdmaCellTowerLocation setLtmOffset:];
-[CLPCdmaCellTowerLocation setPnoffset:];
-[CLPCdmaCellTowerLocation setSectorLatitude:];
-[CLPCdmaCellTowerLocation setSectorLongitude:];
-[CLPCdmaCellTowerLocation setSectorid:];
-[CLPCdmaCellTowerLocation setZoneid:];
-[CLPCdmaCellTowerLocation zoneid];
```
