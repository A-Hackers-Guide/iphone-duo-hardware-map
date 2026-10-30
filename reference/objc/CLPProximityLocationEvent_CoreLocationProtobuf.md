# `CLPProximityLocationEvent`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 5 instance variables, 8 properties, 25 instance methods, 0 class methods

## Instance variables

```
d _latitude;
d _longitude;
d _timestamp;
f _horizontalAccuracy;
{?="latitude"b1"longitude"b1"timestamp"b1"horizontalAccuracy"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (Td,N,V_timestamp) timestamp;
@property (TB,N) hasLatitude;
@property (Td,N,V_latitude) latitude;
@property (TB,N) hasLongitude;
@property (Td,N,V_longitude) longitude;
@property (TB,N) hasHorizontalAccuracy;
@property (Tf,N,V_horizontalAccuracy) horizontalAccuracy;
```

## Instance methods

```
-[CLPProximityLocationEvent hasTimestamp];
-[CLPProximityLocationEvent setHasTimestamp:];
-[CLPProximityLocationEvent setTimestamp:];
-[CLPProximityLocationEvent writeTo:];
-[CLPProximityLocationEvent setLatitude:];
-[CLPProximityLocationEvent latitude];
-[CLPProximityLocationEvent mergeFrom:];
-[CLPProximityLocationEvent longitude];
-[CLPProximityLocationEvent setLongitude:];
-[CLPProximityLocationEvent timestamp];
-[CLPProximityLocationEvent horizontalAccuracy];
-[CLPProximityLocationEvent setHorizontalAccuracy:];
-[CLPProximityLocationEvent hash];
-[CLPProximityLocationEvent copyTo:];
-[CLPProximityLocationEvent description];
-[CLPProximityLocationEvent readFrom:];
-[CLPProximityLocationEvent copyWithZone:];
-[CLPProximityLocationEvent isEqual:];
-[CLPProximityLocationEvent dictionaryRepresentation];
-[CLPProximityLocationEvent setHasLatitude:];
-[CLPProximityLocationEvent hasLatitude];
-[CLPProximityLocationEvent hasLongitude];
-[CLPProximityLocationEvent setHasLongitude:];
-[CLPProximityLocationEvent hasHorizontalAccuracy];
-[CLPProximityLocationEvent setHasHorizontalAccuracy:];
```
