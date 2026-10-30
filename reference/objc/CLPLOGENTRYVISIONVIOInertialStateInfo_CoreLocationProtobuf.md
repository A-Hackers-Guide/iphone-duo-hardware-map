# `CLPLOGENTRYVISIONVIOInertialStateInfo`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 13 instance variables, 24 properties, 57 instance methods, 0 class methods

## Instance variables

```
Q _stateLengthInBytes;
I _accelBiasLength;
I _accelBiasOffset;
I _gyroBiasLength;
I _gyroBiasOffset;
I _orientationLength;
I _orientationOffset;
I _positionLength;
I _positionOffset;
I _stateLength;
I _velocityLength;
I _velocityOffset;
{?="stateLengthInBytes"b1"accelBiasLength"b1"accelBiasOffset"b1"gyroBiasLength"b1"gyroBiasOffset"b1"orientationLength"b1"orientationOffset"b1"positionLength"b1"positionOffset"b1"stateLength"b1"velocityLength"b1"velocityOffset"b1} _has;
```

## Properties

```
@property (TB,N) hasStateLengthInBytes;
@property (TQ,N,V_stateLengthInBytes) stateLengthInBytes;
@property (TB,N) hasStateLength;
@property (TI,N,V_stateLength) stateLength;
@property (TB,N) hasOrientationOffset;
@property (TI,N,V_orientationOffset) orientationOffset;
@property (TB,N) hasOrientationLength;
@property (TI,N,V_orientationLength) orientationLength;
@property (TB,N) hasGyroBiasOffset;
@property (TI,N,V_gyroBiasOffset) gyroBiasOffset;
@property (TB,N) hasGyroBiasLength;
@property (TI,N,V_gyroBiasLength) gyroBiasLength;
@property (TB,N) hasVelocityOffset;
@property (TI,N,V_velocityOffset) velocityOffset;
@property (TB,N) hasVelocityLength;
@property (TI,N,V_velocityLength) velocityLength;
@property (TB,N) hasAccelBiasOffset;
@property (TI,N,V_accelBiasOffset) accelBiasOffset;
@property (TB,N) hasAccelBiasLength;
@property (TI,N,V_accelBiasLength) accelBiasLength;
@property (TB,N) hasPositionOffset;
@property (TI,N,V_positionOffset) positionOffset;
@property (TB,N) hasPositionLength;
@property (TI,N,V_positionLength) positionLength;
```

## Instance methods

```
-[CLPLOGENTRYVISIONVIOInertialStateInfo writeTo:];
-[CLPLOGENTRYVISIONVIOInertialStateInfo mergeFrom:];
-[CLPLOGENTRYVISIONVIOInertialStateInfo setPositionOffset:];
-[CLPLOGENTRYVISIONVIOInertialStateInfo hash];
-[CLPLOGENTRYVISIONVIOInertialStateInfo copyTo:];
-[CLPLOGENTRYVISIONVIOInertialStateInfo description];
-[CLPLOGENTRYVISIONVIOInertialStateInfo readFrom:];
-[CLPLOGENTRYVISIONVIOInertialStateInfo copyWithZone:];
-[CLPLOGENTRYVISIONVIOInertialStateInfo isEqual:];
-[CLPLOGENTRYVISIONVIOInertialStateInfo dictionaryRepresentation];
-[CLPLOGENTRYVISIONVIOInertialStateInfo positionOffset];
-[CLPLOGENTRYVISIONVIOInertialStateInfo orientationOffset];
-[CLPLOGENTRYVISIONVIOInertialStateInfo setOrientationOffset:];
-[CLPLOGENTRYVISIONVIOInertialStateInfo stateLength];
-[CLPLOGENTRYVISIONVIOInertialStateInfo accelBiasOffset];
-[CLPLOGENTRYVISIONVIOInertialStateInfo accelBiasLength];
-[CLPLOGENTRYVISIONVIOInertialStateInfo setStateLength:];
-[CLPLOGENTRYVISIONVIOInertialStateInfo gyroBiasLength];
-[CLPLOGENTRYVISIONVIOInertialStateInfo gyroBiasOffset];
-[CLPLOGENTRYVISIONVIOInertialStateInfo hasAccelBiasLength];
-[CLPLOGENTRYVISIONVIOInertialStateInfo hasAccelBiasOffset];
-[CLPLOGENTRYVISIONVIOInertialStateInfo hasGyroBiasLength];
-[CLPLOGENTRYVISIONVIOInertialStateInfo hasGyroBiasOffset];
-[CLPLOGENTRYVISIONVIOInertialStateInfo hasOrientationLength];
-[CLPLOGENTRYVISIONVIOInertialStateInfo hasOrientationOffset];
-[CLPLOGENTRYVISIONVIOInertialStateInfo hasPositionLength];
-[CLPLOGENTRYVISIONVIOInertialStateInfo hasPositionOffset];
-[CLPLOGENTRYVISIONVIOInertialStateInfo hasStateLength];
-[CLPLOGENTRYVISIONVIOInertialStateInfo hasStateLengthInBytes];
-[CLPLOGENTRYVISIONVIOInertialStateInfo hasVelocityLength];
-[CLPLOGENTRYVISIONVIOInertialStateInfo hasVelocityOffset];
-[CLPLOGENTRYVISIONVIOInertialStateInfo orientationLength];
-[CLPLOGENTRYVISIONVIOInertialStateInfo positionLength];
-[CLPLOGENTRYVISIONVIOInertialStateInfo setAccelBiasLength:];
-[CLPLOGENTRYVISIONVIOInertialStateInfo setAccelBiasOffset:];
-[CLPLOGENTRYVISIONVIOInertialStateInfo setGyroBiasLength:];
-[CLPLOGENTRYVISIONVIOInertialStateInfo setGyroBiasOffset:];
-[CLPLOGENTRYVISIONVIOInertialStateInfo setHasAccelBiasLength:];
-[CLPLOGENTRYVISIONVIOInertialStateInfo setHasAccelBiasOffset:];
-[CLPLOGENTRYVISIONVIOInertialStateInfo setHasGyroBiasLength:];
-[CLPLOGENTRYVISIONVIOInertialStateInfo setHasGyroBiasOffset:];
-[CLPLOGENTRYVISIONVIOInertialStateInfo setHasOrientationLength:];
-[CLPLOGENTRYVISIONVIOInertialStateInfo setHasOrientationOffset:];
-[CLPLOGENTRYVISIONVIOInertialStateInfo setHasPositionLength:];
-[CLPLOGENTRYVISIONVIOInertialStateInfo setHasPositionOffset:];
-[CLPLOGENTRYVISIONVIOInertialStateInfo setHasStateLength:];
-[CLPLOGENTRYVISIONVIOInertialStateInfo setHasStateLengthInBytes:];
-[CLPLOGENTRYVISIONVIOInertialStateInfo setHasVelocityLength:];
-[CLPLOGENTRYVISIONVIOInertialStateInfo setHasVelocityOffset:];
-[CLPLOGENTRYVISIONVIOInertialStateInfo setOrientationLength:];
-[CLPLOGENTRYVISIONVIOInertialStateInfo setPositionLength:];
-[CLPLOGENTRYVISIONVIOInertialStateInfo setStateLengthInBytes:];
-[CLPLOGENTRYVISIONVIOInertialStateInfo setVelocityLength:];
-[CLPLOGENTRYVISIONVIOInertialStateInfo setVelocityOffset:];
-[CLPLOGENTRYVISIONVIOInertialStateInfo stateLengthInBytes];
-[CLPLOGENTRYVISIONVIOInertialStateInfo velocityLength];
-[CLPLOGENTRYVISIONVIOInertialStateInfo velocityOffset];
```
