# `CLPProximityGPSTileEvent`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 3 instance variables, 4 properties, 17 instance methods, 0 class methods

## Instance variables

```
d _timestamp;
i _tileType;
{?="timestamp"b1"tileType"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (Td,N,V_timestamp) timestamp;
@property (TB,N) hasTileType;
@property (Ti,N,V_tileType) tileType;
```

## Instance methods

```
-[CLPProximityGPSTileEvent hasTimestamp];
-[CLPProximityGPSTileEvent setHasTimestamp:];
-[CLPProximityGPSTileEvent setTimestamp:];
-[CLPProximityGPSTileEvent writeTo:];
-[CLPProximityGPSTileEvent mergeFrom:];
-[CLPProximityGPSTileEvent timestamp];
-[CLPProximityGPSTileEvent hash];
-[CLPProximityGPSTileEvent copyTo:];
-[CLPProximityGPSTileEvent description];
-[CLPProximityGPSTileEvent readFrom:];
-[CLPProximityGPSTileEvent copyWithZone:];
-[CLPProximityGPSTileEvent isEqual:];
-[CLPProximityGPSTileEvent dictionaryRepresentation];
-[CLPProximityGPSTileEvent tileType];
-[CLPProximityGPSTileEvent setHasTileType:];
-[CLPProximityGPSTileEvent hasTileType];
-[CLPProximityGPSTileEvent setTileType:];
```
