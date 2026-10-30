# `CLPInertialOdometry`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 13 instance variables, 24 properties, 60 instance methods, 0 class methods

## Instance variables

```
d _deltaPositionX;
d _deltaPositionY;
d _deltaPositionZ;
d _deltaVelocityX;
d _deltaVelocityY;
d _deltaVelocityZ;
d _timestamp;
i _displacingState;
@"CLPQuaternion" _orientation;
f _rotationArbitraryToTrueNorthRad;
i _source;
B _wasReinitialized;
{?="deltaPositionX"b1"deltaPositionY"b1"deltaPositionZ"b1"deltaVelocityX"b1"deltaVelocityY"b1"deltaVelocityZ"b1"timestamp"b1"displacingState"b1"rotationArbitraryToTrueNorthRad"b1"source"b1"wasReinitialized"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (Td,N,V_timestamp) timestamp;
@property (TB,N) hasDeltaPositionX;
@property (Td,N,V_deltaPositionX) deltaPositionX;
@property (TB,N) hasDeltaPositionY;
@property (Td,N,V_deltaPositionY) deltaPositionY;
@property (TB,N) hasDeltaPositionZ;
@property (Td,N,V_deltaPositionZ) deltaPositionZ;
@property (TB,N) hasDeltaVelocityX;
@property (Td,N,V_deltaVelocityX) deltaVelocityX;
@property (TB,N) hasDeltaVelocityY;
@property (Td,N,V_deltaVelocityY) deltaVelocityY;
@property (TB,N) hasDeltaVelocityZ;
@property (Td,N,V_deltaVelocityZ) deltaVelocityZ;
@property (TB,R,N) hasOrientation;
@property (T@"CLPQuaternion",&,N,V_orientation) orientation;
@property (TB,N) hasDisplacingState;
@property (Ti,N,V_displacingState) displacingState;
@property (TB,N) hasRotationArbitraryToTrueNorthRad;
@property (Tf,N,V_rotationArbitraryToTrueNorthRad) rotationArbitraryToTrueNorthRad;
@property (TB,N) hasWasReinitialized;
@property (TB,N,V_wasReinitialized) wasReinitialized;
@property (TB,N) hasSource;
@property (Ti,N,V_source) source;
```

## Instance methods

```
-[CLPInertialOdometry setDeltaPositionY:];
-[CLPInertialOdometry setDeltaPositionZ:];
-[CLPInertialOdometry deltaPositionY];
-[CLPInertialOdometry setOrientation:];
-[CLPInertialOdometry deltaPositionX];
-[CLPInertialOdometry deltaPositionZ];
-[CLPInertialOdometry setDeltaPositionX:];
-[CLPInertialOdometry hasTimestamp];
-[CLPInertialOdometry setHasTimestamp:];
-[CLPInertialOdometry setTimestamp:];
-[CLPInertialOdometry writeTo:];
-[CLPInertialOdometry sourceAsString:];
-[CLPInertialOdometry mergeFrom:];
-[CLPInertialOdometry deltaVelocityZ];
-[CLPInertialOdometry orientation];
-[CLPInertialOdometry timestamp];
-[CLPInertialOdometry hasSource];
-[CLPInertialOdometry hasOrientation];
-[CLPInertialOdometry deltaVelocityX];
-[CLPInertialOdometry setSource:];
-[CLPInertialOdometry StringAsSource:];
-[CLPInertialOdometry deltaVelocityY];
-[CLPInertialOdometry hash];
-[CLPInertialOdometry copyTo:];
-[CLPInertialOdometry description];
-[CLPInertialOdometry setHasSource:];
-[CLPInertialOdometry readFrom:];
-[CLPInertialOdometry copyWithZone:];
-[CLPInertialOdometry isEqual:];
-[CLPInertialOdometry source];
-[CLPInertialOdometry dictionaryRepresentation];
-[CLPInertialOdometry StringAsDisplacingState:];
-[CLPInertialOdometry displacingState];
-[CLPInertialOdometry rotationArbitraryToTrueNorthRad];
-[CLPInertialOdometry displacingStateAsString:];
-[CLPInertialOdometry hasDeltaPositionX];
-[CLPInertialOdometry hasDeltaPositionY];
-[CLPInertialOdometry hasDeltaPositionZ];
-[CLPInertialOdometry hasDeltaVelocityX];
-[CLPInertialOdometry hasDeltaVelocityY];
-[CLPInertialOdometry hasDeltaVelocityZ];
-[CLPInertialOdometry hasDisplacingState];
-[CLPInertialOdometry hasRotationArbitraryToTrueNorthRad];
-[CLPInertialOdometry hasWasReinitialized];
-[CLPInertialOdometry setDeltaVelocityX:];
-[CLPInertialOdometry setDeltaVelocityY:];
-[CLPInertialOdometry setDeltaVelocityZ:];
-[CLPInertialOdometry setDisplacingState:];
-[CLPInertialOdometry setHasDeltaPositionX:];
-[CLPInertialOdometry setHasDeltaPositionY:];
-[CLPInertialOdometry setHasDeltaPositionZ:];
-[CLPInertialOdometry setHasDeltaVelocityX:];
-[CLPInertialOdometry setHasDeltaVelocityY:];
-[CLPInertialOdometry setHasDeltaVelocityZ:];
-[CLPInertialOdometry setHasDisplacingState:];
-[CLPInertialOdometry setHasRotationArbitraryToTrueNorthRad:];
-[CLPInertialOdometry setHasWasReinitialized:];
-[CLPInertialOdometry setRotationArbitraryToTrueNorthRad:];
-[CLPInertialOdometry setWasReinitialized:];
-[CLPInertialOdometry wasReinitialized];
```
