# `CLPScdmaCellTower`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 5 instance variables, 8 properties, 25 instance methods, 0 class methods

## Instance variables

```
i _ci;
i _lac;
i _mcc;
i _mnc;
{?="ci"b1"lac"b1"mcc"b1"mnc"b1} _has;
```

## Properties

```
@property (TB,N) hasMcc;
@property (Ti,N,V_mcc) mcc;
@property (TB,N) hasMnc;
@property (Ti,N,V_mnc) mnc;
@property (TB,N) hasLac;
@property (Ti,N,V_lac) lac;
@property (TB,N) hasCi;
@property (Ti,N,V_ci) ci;
```

## Instance methods

```
-[CLPScdmaCellTower lac];
-[CLPScdmaCellTower ci];
-[CLPScdmaCellTower setLac:];
-[CLPScdmaCellTower writeTo:];
-[CLPScdmaCellTower mergeFrom:];
-[CLPScdmaCellTower mnc];
-[CLPScdmaCellTower hash];
-[CLPScdmaCellTower copyTo:];
-[CLPScdmaCellTower description];
-[CLPScdmaCellTower setMnc:];
-[CLPScdmaCellTower setCi:];
-[CLPScdmaCellTower mcc];
-[CLPScdmaCellTower readFrom:];
-[CLPScdmaCellTower copyWithZone:];
-[CLPScdmaCellTower isEqual:];
-[CLPScdmaCellTower setMcc:];
-[CLPScdmaCellTower dictionaryRepresentation];
-[CLPScdmaCellTower hasCi];
-[CLPScdmaCellTower hasLac];
-[CLPScdmaCellTower hasMcc];
-[CLPScdmaCellTower hasMnc];
-[CLPScdmaCellTower setHasCi:];
-[CLPScdmaCellTower setHasLac:];
-[CLPScdmaCellTower setHasMcc:];
-[CLPScdmaCellTower setHasMnc:];
```
