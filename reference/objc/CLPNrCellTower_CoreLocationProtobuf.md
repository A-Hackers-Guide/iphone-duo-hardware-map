# `CLPNrCellTower`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 5 instance variables, 8 properties, 25 instance methods, 0 class methods

## Instance variables

```
q _ci;
i _mcc;
i _mnc;
i _tac;
{?="ci"b1"mcc"b1"mnc"b1"tac"b1} _has;
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
```

## Instance methods

```
-[CLPNrCellTower tac];
-[CLPNrCellTower ci];
-[CLPNrCellTower writeTo:];
-[CLPNrCellTower mergeFrom:];
-[CLPNrCellTower setTac:];
-[CLPNrCellTower mnc];
-[CLPNrCellTower hash];
-[CLPNrCellTower copyTo:];
-[CLPNrCellTower description];
-[CLPNrCellTower setMnc:];
-[CLPNrCellTower setCi:];
-[CLPNrCellTower mcc];
-[CLPNrCellTower readFrom:];
-[CLPNrCellTower copyWithZone:];
-[CLPNrCellTower isEqual:];
-[CLPNrCellTower setMcc:];
-[CLPNrCellTower dictionaryRepresentation];
-[CLPNrCellTower hasCi];
-[CLPNrCellTower hasMcc];
-[CLPNrCellTower hasMnc];
-[CLPNrCellTower hasTac];
-[CLPNrCellTower setHasCi:];
-[CLPNrCellTower setHasMcc:];
-[CLPNrCellTower setHasMnc:];
-[CLPNrCellTower setHasTac:];
```
