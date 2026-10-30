# `CLPCdmaCellTower`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 6 instance variables, 10 properties, 29 instance methods, 0 class methods

## Instance variables

```
i _bsid;
i _mcc;
i _mnc;
i _nid;
i _sid;
{?="bsid"b1"mcc"b1"mnc"b1"nid"b1"sid"b1} _has;
```

## Properties

```
@property (TB,N) hasMcc;
@property (Ti,N,V_mcc) mcc;
@property (TB,N) hasMnc;
@property (Ti,N,V_mnc) mnc;
@property (TB,N) hasSid;
@property (Ti,N,V_sid) sid;
@property (TB,N) hasNid;
@property (Ti,N,V_nid) nid;
@property (TB,N) hasBsid;
@property (Ti,N,V_bsid) bsid;
```

## Instance methods

```
-[CLPCdmaCellTower writeTo:];
-[CLPCdmaCellTower mergeFrom:];
-[CLPCdmaCellTower mnc];
-[CLPCdmaCellTower hash];
-[CLPCdmaCellTower copyTo:];
-[CLPCdmaCellTower description];
-[CLPCdmaCellTower setMnc:];
-[CLPCdmaCellTower mcc];
-[CLPCdmaCellTower readFrom:];
-[CLPCdmaCellTower copyWithZone:];
-[CLPCdmaCellTower isEqual:];
-[CLPCdmaCellTower setMcc:];
-[CLPCdmaCellTower dictionaryRepresentation];
-[CLPCdmaCellTower setSid:];
-[CLPCdmaCellTower sid];
-[CLPCdmaCellTower hasBsid];
-[CLPCdmaCellTower nid];
-[CLPCdmaCellTower setNid:];
-[CLPCdmaCellTower bsid];
-[CLPCdmaCellTower hasMcc];
-[CLPCdmaCellTower hasMnc];
-[CLPCdmaCellTower hasNid];
-[CLPCdmaCellTower hasSid];
-[CLPCdmaCellTower setBsid:];
-[CLPCdmaCellTower setHasBsid:];
-[CLPCdmaCellTower setHasMcc:];
-[CLPCdmaCellTower setHasMnc:];
-[CLPCdmaCellTower setHasNid:];
-[CLPCdmaCellTower setHasSid:];
```
