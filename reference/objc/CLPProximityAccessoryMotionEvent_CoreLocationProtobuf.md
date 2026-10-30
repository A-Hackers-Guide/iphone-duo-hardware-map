# `CLPProximityAccessoryMotionEvent`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 3 instance variables, 4 properties, 17 instance methods, 0 class methods

## Instance variables

```
d _timestamp;
i _motionState;
{?="timestamp"b1"motionState"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (Td,N,V_timestamp) timestamp;
@property (TB,N) hasMotionState;
@property (Ti,N,V_motionState) motionState;
```

## Instance methods

```
-[CLPProximityAccessoryMotionEvent motionState];
-[CLPProximityAccessoryMotionEvent hasTimestamp];
-[CLPProximityAccessoryMotionEvent setHasTimestamp:];
-[CLPProximityAccessoryMotionEvent setTimestamp:];
-[CLPProximityAccessoryMotionEvent writeTo:];
-[CLPProximityAccessoryMotionEvent setHasMotionState:];
-[CLPProximityAccessoryMotionEvent mergeFrom:];
-[CLPProximityAccessoryMotionEvent timestamp];
-[CLPProximityAccessoryMotionEvent setMotionState:];
-[CLPProximityAccessoryMotionEvent hash];
-[CLPProximityAccessoryMotionEvent copyTo:];
-[CLPProximityAccessoryMotionEvent description];
-[CLPProximityAccessoryMotionEvent hasMotionState];
-[CLPProximityAccessoryMotionEvent readFrom:];
-[CLPProximityAccessoryMotionEvent copyWithZone:];
-[CLPProximityAccessoryMotionEvent isEqual:];
-[CLPProximityAccessoryMotionEvent dictionaryRepresentation];
```
