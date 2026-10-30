# `CLPCellNeighborsGroup`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 5 instance variables, 5 properties, 39 instance methods, 5 class methods

## Instance variables

```
@"NSMutableArray" _cdmaNeighbors;
@"NSMutableArray" _gsmNeighbors;
@"NSMutableArray" _lteNeighbors;
@"NSMutableArray" _nrNeighbors;
@"NSMutableArray" _scdmaNeighbors;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V_gsmNeighbors) gsmNeighbors;
@property (T@"NSMutableArray",&,N,V_scdmaNeighbors) scdmaNeighbors;
@property (T@"NSMutableArray",&,N,V_cdmaNeighbors) cdmaNeighbors;
@property (T@"NSMutableArray",&,N,V_lteNeighbors) lteNeighbors;
@property (T@"NSMutableArray",&,N,V_nrNeighbors) nrNeighbors;
```

## Class methods

```
+[CLPCellNeighborsGroup nrNeighborsType];
+[CLPCellNeighborsGroup cdmaNeighborsType];
+[CLPCellNeighborsGroup gsmNeighborsType];
+[CLPCellNeighborsGroup lteNeighborsType];
+[CLPCellNeighborsGroup scdmaNeighborsType];
```

## Instance methods

```
-[CLPCellNeighborsGroup writeTo:];
-[CLPCellNeighborsGroup mergeFrom:];
-[CLPCellNeighborsGroup hash];
-[CLPCellNeighborsGroup copyTo:];
-[CLPCellNeighborsGroup description];
-[CLPCellNeighborsGroup readFrom:];
-[CLPCellNeighborsGroup copyWithZone:];
-[CLPCellNeighborsGroup isEqual:];
-[CLPCellNeighborsGroup dictionaryRepresentation];
-[CLPCellNeighborsGroup setNrNeighbors:];
-[CLPCellNeighborsGroup addNrNeighbors:];
-[CLPCellNeighborsGroup addCdmaNeighbors:];
-[CLPCellNeighborsGroup addGsmNeighbors:];
-[CLPCellNeighborsGroup addLteNeighbors:];
-[CLPCellNeighborsGroup addScdmaNeighbors:];
-[CLPCellNeighborsGroup cdmaNeighbors];
-[CLPCellNeighborsGroup cdmaNeighborsAtIndex:];
-[CLPCellNeighborsGroup cdmaNeighborsCount];
-[CLPCellNeighborsGroup clearCdmaNeighbors];
-[CLPCellNeighborsGroup clearGsmNeighbors];
-[CLPCellNeighborsGroup clearLteNeighbors];
-[CLPCellNeighborsGroup clearNrNeighbors];
-[CLPCellNeighborsGroup clearScdmaNeighbors];
-[CLPCellNeighborsGroup gsmNeighbors];
-[CLPCellNeighborsGroup gsmNeighborsAtIndex:];
-[CLPCellNeighborsGroup gsmNeighborsCount];
-[CLPCellNeighborsGroup lteNeighbors];
-[CLPCellNeighborsGroup lteNeighborsAtIndex:];
-[CLPCellNeighborsGroup lteNeighborsCount];
-[CLPCellNeighborsGroup nrNeighbors];
-[CLPCellNeighborsGroup nrNeighborsAtIndex:];
-[CLPCellNeighborsGroup nrNeighborsCount];
-[CLPCellNeighborsGroup scdmaNeighbors];
-[CLPCellNeighborsGroup scdmaNeighborsAtIndex:];
-[CLPCellNeighborsGroup scdmaNeighborsCount];
-[CLPCellNeighborsGroup setCdmaNeighbors:];
-[CLPCellNeighborsGroup setGsmNeighbors:];
-[CLPCellNeighborsGroup setLteNeighbors:];
-[CLPCellNeighborsGroup setScdmaNeighbors:];
```
