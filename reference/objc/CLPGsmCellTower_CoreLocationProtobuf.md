# `CLPGsmCellTower`

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
-[CLPGsmCellTower lac];
-[CLPGsmCellTower ci];
-[CLPGsmCellTower setLac:];
-[CLPGsmCellTower writeTo:];
-[CLPGsmCellTower mergeFrom:];
-[CLPGsmCellTower mnc];
-[CLPGsmCellTower hash];
-[CLPGsmCellTower copyTo:];
-[CLPGsmCellTower description];
-[CLPGsmCellTower setMnc:];
-[CLPGsmCellTower setCi:];
-[CLPGsmCellTower mcc];
-[CLPGsmCellTower readFrom:];
-[CLPGsmCellTower copyWithZone:];
-[CLPGsmCellTower isEqual:];
-[CLPGsmCellTower setMcc:];
-[CLPGsmCellTower dictionaryRepresentation];
-[CLPGsmCellTower hasCi];
-[CLPGsmCellTower hasLac];
-[CLPGsmCellTower hasMcc];
-[CLPGsmCellTower hasMnc];
-[CLPGsmCellTower setHasCi:];
-[CLPGsmCellTower setHasLac:];
-[CLPGsmCellTower setHasMcc:];
-[CLPGsmCellTower setHasMnc:];
```
