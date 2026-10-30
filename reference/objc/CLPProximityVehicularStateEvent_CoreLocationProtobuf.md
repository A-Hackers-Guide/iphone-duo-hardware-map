# `CLPProximityVehicularStateEvent`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 3 instance variables, 4 properties, 17 instance methods, 0 class methods

## Instance variables

```
d _timestamp;
B _isVehicular;
{?="timestamp"b1"isVehicular"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (Td,N,V_timestamp) timestamp;
@property (TB,N) hasIsVehicular;
@property (TB,N,V_isVehicular) isVehicular;
```

## Instance methods

```
-[CLPProximityVehicularStateEvent hasTimestamp];
-[CLPProximityVehicularStateEvent setHasTimestamp:];
-[CLPProximityVehicularStateEvent setTimestamp:];
-[CLPProximityVehicularStateEvent writeTo:];
-[CLPProximityVehicularStateEvent mergeFrom:];
-[CLPProximityVehicularStateEvent timestamp];
-[CLPProximityVehicularStateEvent hash];
-[CLPProximityVehicularStateEvent copyTo:];
-[CLPProximityVehicularStateEvent description];
-[CLPProximityVehicularStateEvent readFrom:];
-[CLPProximityVehicularStateEvent copyWithZone:];
-[CLPProximityVehicularStateEvent isEqual:];
-[CLPProximityVehicularStateEvent dictionaryRepresentation];
-[CLPProximityVehicularStateEvent setIsVehicular:];
-[CLPProximityVehicularStateEvent hasIsVehicular];
-[CLPProximityVehicularStateEvent isVehicular];
-[CLPProximityVehicularStateEvent setHasIsVehicular:];
```
