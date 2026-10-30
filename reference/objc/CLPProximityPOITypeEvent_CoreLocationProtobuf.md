# `CLPProximityPOITypeEvent`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 3 instance variables, 4 properties, 17 instance methods, 0 class methods

## Instance variables

```
d _timestamp;
i _poiType;
{?="timestamp"b1"poiType"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (Td,N,V_timestamp) timestamp;
@property (TB,N) hasPoiType;
@property (Ti,N,V_poiType) poiType;
```

## Instance methods

```
-[CLPProximityPOITypeEvent hasTimestamp];
-[CLPProximityPOITypeEvent setHasTimestamp:];
-[CLPProximityPOITypeEvent setTimestamp:];
-[CLPProximityPOITypeEvent writeTo:];
-[CLPProximityPOITypeEvent mergeFrom:];
-[CLPProximityPOITypeEvent timestamp];
-[CLPProximityPOITypeEvent hash];
-[CLPProximityPOITypeEvent copyTo:];
-[CLPProximityPOITypeEvent description];
-[CLPProximityPOITypeEvent readFrom:];
-[CLPProximityPOITypeEvent copyWithZone:];
-[CLPProximityPOITypeEvent isEqual:];
-[CLPProximityPOITypeEvent dictionaryRepresentation];
-[CLPProximityPOITypeEvent poiType];
-[CLPProximityPOITypeEvent hasPoiType];
-[CLPProximityPOITypeEvent setHasPoiType:];
-[CLPProximityPOITypeEvent setPoiType:];
```
