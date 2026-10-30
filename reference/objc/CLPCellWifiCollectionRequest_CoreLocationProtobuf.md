# `CLPCellWifiCollectionRequest`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBRequest`
- Protocols: `NSCopying`
- 9 instance variables, 9 properties, 61 instance methods, 8 class methods

## Instance variables

```
@"NSMutableArray" _cdmaCellTowerLocations;
@"NSMutableArray" _cellOutOfServiceInfos;
@"NSMutableArray" _cellTowerLocations;
@"NSMutableArray" _lteCellTowerLocations;
@"CLPMeta" _meta;
@"NSMutableArray" _nomapMacs;
@"NSMutableArray" _nrCellTowerLocations;
@"NSMutableArray" _scdmaCellTowerLocations;
@"NSMutableArray" _wifiAPLocations;
```

## Properties

```
@property (T@"CLPMeta",&,N,V_meta) meta;
@property (T@"NSMutableArray",&,N,V_cellTowerLocations) cellTowerLocations;
@property (T@"NSMutableArray",&,N,V_cdmaCellTowerLocations) cdmaCellTowerLocations;
@property (T@"NSMutableArray",&,N,V_lteCellTowerLocations) lteCellTowerLocations;
@property (T@"NSMutableArray",&,N,V_nrCellTowerLocations) nrCellTowerLocations;
@property (T@"NSMutableArray",&,N,V_wifiAPLocations) wifiAPLocations;
@property (T@"NSMutableArray",&,N,V_scdmaCellTowerLocations) scdmaCellTowerLocations;
@property (T@"NSMutableArray",&,N,V_cellOutOfServiceInfos) cellOutOfServiceInfos;
@property (T@"NSMutableArray",&,N,V_nomapMacs) nomapMacs;
```

## Class methods

```
+[CLPCellWifiCollectionRequest cdmaCellTowerLocationType];
+[CLPCellWifiCollectionRequest cellOutOfServiceInfoType];
+[CLPCellWifiCollectionRequest cellTowerLocationType];
+[CLPCellWifiCollectionRequest lteCellTowerLocationType];
+[CLPCellWifiCollectionRequest nomapMacsType];
+[CLPCellWifiCollectionRequest nrCellTowerLocationType];
+[CLPCellWifiCollectionRequest scdmaCellTowerLocationType];
+[CLPCellWifiCollectionRequest wifiAPLocationType];
```

## Instance methods

```
-[CLPCellWifiCollectionRequest writeTo:];
-[CLPCellWifiCollectionRequest responseClass];
-[CLPCellWifiCollectionRequest mergeFrom:];
-[CLPCellWifiCollectionRequest requestTypeCode];
-[CLPCellWifiCollectionRequest hash];
-[CLPCellWifiCollectionRequest copyTo:];
-[CLPCellWifiCollectionRequest description];
-[CLPCellWifiCollectionRequest readFrom:];
-[CLPCellWifiCollectionRequest copyWithZone:];
-[CLPCellWifiCollectionRequest isEqual:];
-[CLPCellWifiCollectionRequest dictionaryRepresentation];
-[CLPCellWifiCollectionRequest meta];
-[CLPCellWifiCollectionRequest setMeta:];
-[CLPCellWifiCollectionRequest wifiAPLocations];
-[CLPCellWifiCollectionRequest addCdmaCellTowerLocation:];
-[CLPCellWifiCollectionRequest addCellOutOfServiceInfo:];
-[CLPCellWifiCollectionRequest addCellTowerLocation:];
-[CLPCellWifiCollectionRequest addLteCellTowerLocation:];
-[CLPCellWifiCollectionRequest addNomapMacs:];
-[CLPCellWifiCollectionRequest addNrCellTowerLocation:];
-[CLPCellWifiCollectionRequest addScdmaCellTowerLocation:];
-[CLPCellWifiCollectionRequest addWifiAPLocation:];
-[CLPCellWifiCollectionRequest cdmaCellTowerLocationAtIndex:];
-[CLPCellWifiCollectionRequest cdmaCellTowerLocations];
-[CLPCellWifiCollectionRequest cdmaCellTowerLocationsCount];
-[CLPCellWifiCollectionRequest cellOutOfServiceInfoAtIndex:];
-[CLPCellWifiCollectionRequest cellOutOfServiceInfos];
-[CLPCellWifiCollectionRequest cellOutOfServiceInfosCount];
-[CLPCellWifiCollectionRequest cellTowerLocationAtIndex:];
-[CLPCellWifiCollectionRequest cellTowerLocations];
-[CLPCellWifiCollectionRequest cellTowerLocationsCount];
-[CLPCellWifiCollectionRequest clearCdmaCellTowerLocations];
-[CLPCellWifiCollectionRequest clearCellOutOfServiceInfos];
-[CLPCellWifiCollectionRequest clearCellTowerLocations];
-[CLPCellWifiCollectionRequest clearLteCellTowerLocations];
-[CLPCellWifiCollectionRequest clearNomapMacs];
-[CLPCellWifiCollectionRequest clearNrCellTowerLocations];
-[CLPCellWifiCollectionRequest clearScdmaCellTowerLocations];
-[CLPCellWifiCollectionRequest clearWifiAPLocations];
-[CLPCellWifiCollectionRequest lteCellTowerLocationAtIndex:];
-[CLPCellWifiCollectionRequest lteCellTowerLocations];
-[CLPCellWifiCollectionRequest lteCellTowerLocationsCount];
-[CLPCellWifiCollectionRequest nomapMacs];
-[CLPCellWifiCollectionRequest nomapMacsAtIndex:];
-[CLPCellWifiCollectionRequest nomapMacsCount];
-[CLPCellWifiCollectionRequest nrCellTowerLocationAtIndex:];
-[CLPCellWifiCollectionRequest nrCellTowerLocations];
-[CLPCellWifiCollectionRequest nrCellTowerLocationsCount];
-[CLPCellWifiCollectionRequest scdmaCellTowerLocationAtIndex:];
-[CLPCellWifiCollectionRequest scdmaCellTowerLocations];
-[CLPCellWifiCollectionRequest scdmaCellTowerLocationsCount];
-[CLPCellWifiCollectionRequest setCdmaCellTowerLocations:];
-[CLPCellWifiCollectionRequest setCellOutOfServiceInfos:];
-[CLPCellWifiCollectionRequest setCellTowerLocations:];
-[CLPCellWifiCollectionRequest setLteCellTowerLocations:];
-[CLPCellWifiCollectionRequest setNomapMacs:];
-[CLPCellWifiCollectionRequest setNrCellTowerLocations:];
-[CLPCellWifiCollectionRequest setScdmaCellTowerLocations:];
-[CLPCellWifiCollectionRequest setWifiAPLocations:];
-[CLPCellWifiCollectionRequest wifiAPLocationAtIndex:];
-[CLPCellWifiCollectionRequest wifiAPLocationsCount];
```
