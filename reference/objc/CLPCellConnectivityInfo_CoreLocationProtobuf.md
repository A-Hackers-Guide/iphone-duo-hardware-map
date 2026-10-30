# `CLPCellConnectivityInfo`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 8 instance variables, 14 properties, 34 instance methods, 0 class methods

## Instance variables

```
d _timestamp;
@"CLPCdmaCellTower" _cdma;
i _connectionStatus;
@"CLPGsmCellTower" _gsm;
@"CLPLteCellTower" _lte;
@"CLPNrCellTower" _nr;
@"CLPScdmaCellTower" _scdma;
{?="timestamp"b1"connectionStatus"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (Td,N,V_timestamp) timestamp;
@property (TB,N) hasConnectionStatus;
@property (Ti,N,V_connectionStatus) connectionStatus;
@property (TB,R,N) hasGsm;
@property (T@"CLPGsmCellTower",&,N,V_gsm) gsm;
@property (TB,R,N) hasCdma;
@property (T@"CLPCdmaCellTower",&,N,V_cdma) cdma;
@property (TB,R,N) hasScdma;
@property (T@"CLPScdmaCellTower",&,N,V_scdma) scdma;
@property (TB,R,N) hasLte;
@property (T@"CLPLteCellTower",&,N,V_lte) lte;
@property (TB,R,N) hasNr;
@property (T@"CLPNrCellTower",&,N,V_nr) nr;
```

## Instance methods

```
-[CLPCellConnectivityInfo hasTimestamp];
-[CLPCellConnectivityInfo setHasTimestamp:];
-[CLPCellConnectivityInfo setTimestamp:];
-[CLPCellConnectivityInfo writeTo:];
-[CLPCellConnectivityInfo setConnectionStatus:];
-[CLPCellConnectivityInfo mergeFrom:];
-[CLPCellConnectivityInfo timestamp];
-[CLPCellConnectivityInfo hash];
-[CLPCellConnectivityInfo copyTo:];
-[CLPCellConnectivityInfo description];
-[CLPCellConnectivityInfo readFrom:];
-[CLPCellConnectivityInfo copyWithZone:];
-[CLPCellConnectivityInfo isEqual:];
-[CLPCellConnectivityInfo connectionStatus];
-[CLPCellConnectivityInfo dictionaryRepresentation];
-[CLPCellConnectivityInfo StringAsConnectionStatus:];
-[CLPCellConnectivityInfo hasCdma];
-[CLPCellConnectivityInfo lte];
-[CLPCellConnectivityInfo setGsm:];
-[CLPCellConnectivityInfo gsm];
-[CLPCellConnectivityInfo setLte:];
-[CLPCellConnectivityInfo cdma];
-[CLPCellConnectivityInfo connectionStatusAsString:];
-[CLPCellConnectivityInfo hasConnectionStatus];
-[CLPCellConnectivityInfo hasGsm];
-[CLPCellConnectivityInfo hasLte];
-[CLPCellConnectivityInfo hasNr];
-[CLPCellConnectivityInfo hasScdma];
-[CLPCellConnectivityInfo nr];
-[CLPCellConnectivityInfo scdma];
-[CLPCellConnectivityInfo setCdma:];
-[CLPCellConnectivityInfo setHasConnectionStatus:];
-[CLPCellConnectivityInfo setNr:];
-[CLPCellConnectivityInfo setScdma:];
```
