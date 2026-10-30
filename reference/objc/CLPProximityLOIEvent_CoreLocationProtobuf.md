# `CLPProximityLOIEvent`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 3 instance variables, 4 properties, 17 instance methods, 0 class methods

## Instance variables

```
d _timestamp;
i _loiId;
{?="timestamp"b1"loiId"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (Td,N,V_timestamp) timestamp;
@property (TB,N) hasLoiId;
@property (Ti,N,V_loiId) loiId;
```

## Instance methods

```
-[CLPProximityLOIEvent hasTimestamp];
-[CLPProximityLOIEvent setHasTimestamp:];
-[CLPProximityLOIEvent setTimestamp:];
-[CLPProximityLOIEvent writeTo:];
-[CLPProximityLOIEvent mergeFrom:];
-[CLPProximityLOIEvent timestamp];
-[CLPProximityLOIEvent hash];
-[CLPProximityLOIEvent copyTo:];
-[CLPProximityLOIEvent description];
-[CLPProximityLOIEvent readFrom:];
-[CLPProximityLOIEvent copyWithZone:];
-[CLPProximityLOIEvent isEqual:];
-[CLPProximityLOIEvent dictionaryRepresentation];
-[CLPProximityLOIEvent loiId];
-[CLPProximityLOIEvent setLoiId:];
-[CLPProximityLOIEvent hasLoiId];
-[CLPProximityLOIEvent setHasLoiId:];
```
