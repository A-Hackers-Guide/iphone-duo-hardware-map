# `CLPIndoorCMPedometer`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 8 instance variables, 14 properties, 37 instance methods, 0 class methods

## Instance variables

```
d _firstStepTime;
d _timestamp;
f _activeTime;
f _distance;
i _floorsAscended;
i _floorsDescended;
i _numberOfSteps;
{?="firstStepTime"b1"timestamp"b1"activeTime"b1"distance"b1"floorsAscended"b1"floorsDescended"b1"numberOfSteps"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (Td,N,V_timestamp) timestamp;
@property (TB,N) hasDistance;
@property (Tf,N,V_distance) distance;
@property (TB,N) hasNumberOfSteps;
@property (Ti,N,V_numberOfSteps) numberOfSteps;
@property (TB,N) hasFloorsAscended;
@property (Ti,N,V_floorsAscended) floorsAscended;
@property (TB,N) hasFloorsDescended;
@property (Ti,N,V_floorsDescended) floorsDescended;
@property (TB,N) hasFirstStepTime;
@property (Td,N,V_firstStepTime) firstStepTime;
@property (TB,N) hasActiveTime;
@property (Tf,N,V_activeTime) activeTime;
```

## Instance methods

```
-[CLPIndoorCMPedometer hasTimestamp];
-[CLPIndoorCMPedometer setHasTimestamp:];
-[CLPIndoorCMPedometer distance];
-[CLPIndoorCMPedometer setTimestamp:];
-[CLPIndoorCMPedometer writeTo:];
-[CLPIndoorCMPedometer setDistance:];
-[CLPIndoorCMPedometer mergeFrom:];
-[CLPIndoorCMPedometer timestamp];
-[CLPIndoorCMPedometer setNumberOfSteps:];
-[CLPIndoorCMPedometer numberOfSteps];
-[CLPIndoorCMPedometer setHasDistance:];
-[CLPIndoorCMPedometer hash];
-[CLPIndoorCMPedometer copyTo:];
-[CLPIndoorCMPedometer description];
-[CLPIndoorCMPedometer hasDistance];
-[CLPIndoorCMPedometer readFrom:];
-[CLPIndoorCMPedometer copyWithZone:];
-[CLPIndoorCMPedometer isEqual:];
-[CLPIndoorCMPedometer dictionaryRepresentation];
-[CLPIndoorCMPedometer floorsDescended];
-[CLPIndoorCMPedometer activeTime];
-[CLPIndoorCMPedometer firstStepTime];
-[CLPIndoorCMPedometer floorsAscended];
-[CLPIndoorCMPedometer hasActiveTime];
-[CLPIndoorCMPedometer hasFirstStepTime];
-[CLPIndoorCMPedometer hasFloorsAscended];
-[CLPIndoorCMPedometer hasFloorsDescended];
-[CLPIndoorCMPedometer hasNumberOfSteps];
-[CLPIndoorCMPedometer setActiveTime:];
-[CLPIndoorCMPedometer setFirstStepTime:];
-[CLPIndoorCMPedometer setFloorsAscended:];
-[CLPIndoorCMPedometer setFloorsDescended:];
-[CLPIndoorCMPedometer setHasActiveTime:];
-[CLPIndoorCMPedometer setHasFirstStepTime:];
-[CLPIndoorCMPedometer setHasFloorsAscended:];
-[CLPIndoorCMPedometer setHasFloorsDescended:];
-[CLPIndoorCMPedometer setHasNumberOfSteps:];
```
