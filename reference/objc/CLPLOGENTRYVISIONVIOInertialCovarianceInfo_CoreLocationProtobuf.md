# `CLPLOGENTRYVISIONVIOInertialCovarianceInfo`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 13 instance variables, 24 properties, 57 instance methods, 0 class methods

## Instance variables

```
Q _covarianceSizeInBytes;
I _accelBiasCovOffset;
I _accelBiasDof;
I _covarianceSize;
I _gyroBiasCovOffset;
I _gyroBiasDof;
I _orientationCovOffset;
I _orientationDof;
I _positionCovOffset;
I _positionDof;
I _velocityCovOffset;
I _velocityDof;
{?="covarianceSizeInBytes"b1"accelBiasCovOffset"b1"accelBiasDof"b1"covarianceSize"b1"gyroBiasCovOffset"b1"gyroBiasDof"b1"orientationCovOffset"b1"orientationDof"b1"positionCovOffset"b1"positionDof"b1"velocityCovOffset"b1"velocityDof"b1} _has;
```

## Properties

```
@property (TB,N) hasCovarianceSizeInBytes;
@property (TQ,N,V_covarianceSizeInBytes) covarianceSizeInBytes;
@property (TB,N) hasCovarianceSize;
@property (TI,N,V_covarianceSize) covarianceSize;
@property (TB,N) hasOrientationCovOffset;
@property (TI,N,V_orientationCovOffset) orientationCovOffset;
@property (TB,N) hasOrientationDof;
@property (TI,N,V_orientationDof) orientationDof;
@property (TB,N) hasGyroBiasCovOffset;
@property (TI,N,V_gyroBiasCovOffset) gyroBiasCovOffset;
@property (TB,N) hasGyroBiasDof;
@property (TI,N,V_gyroBiasDof) gyroBiasDof;
@property (TB,N) hasVelocityCovOffset;
@property (TI,N,V_velocityCovOffset) velocityCovOffset;
@property (TB,N) hasVelocityDof;
@property (TI,N,V_velocityDof) velocityDof;
@property (TB,N) hasAccelBiasCovOffset;
@property (TI,N,V_accelBiasCovOffset) accelBiasCovOffset;
@property (TB,N) hasAccelBiasDof;
@property (TI,N,V_accelBiasDof) accelBiasDof;
@property (TB,N) hasPositionCovOffset;
@property (TI,N,V_positionCovOffset) positionCovOffset;
@property (TB,N) hasPositionDof;
@property (TI,N,V_positionDof) positionDof;
```

## Instance methods

```
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo writeTo:];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo mergeFrom:];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo hash];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo copyTo:];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo description];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo readFrom:];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo copyWithZone:];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo isEqual:];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo dictionaryRepresentation];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo hasAccelBiasDof];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo setPositionDof:];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo setVelocityDof:];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo setGyroBiasDof:];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo accelBiasCovOffset];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo accelBiasDof];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo covarianceSize];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo covarianceSizeInBytes];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo gyroBiasCovOffset];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo gyroBiasDof];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo hasAccelBiasCovOffset];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo hasCovarianceSize];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo hasCovarianceSizeInBytes];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo hasGyroBiasCovOffset];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo hasGyroBiasDof];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo hasOrientationCovOffset];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo hasOrientationDof];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo hasPositionCovOffset];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo hasPositionDof];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo hasVelocityCovOffset];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo hasVelocityDof];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo orientationCovOffset];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo orientationDof];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo positionCovOffset];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo positionDof];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo setAccelBiasCovOffset:];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo setAccelBiasDof:];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo setCovarianceSize:];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo setCovarianceSizeInBytes:];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo setGyroBiasCovOffset:];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo setHasAccelBiasCovOffset:];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo setHasAccelBiasDof:];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo setHasCovarianceSize:];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo setHasCovarianceSizeInBytes:];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo setHasGyroBiasCovOffset:];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo setHasGyroBiasDof:];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo setHasOrientationCovOffset:];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo setHasOrientationDof:];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo setHasPositionCovOffset:];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo setHasPositionDof:];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo setHasVelocityCovOffset:];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo setHasVelocityDof:];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo setOrientationCovOffset:];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo setOrientationDof:];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo setPositionCovOffset:];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo setVelocityCovOffset:];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo velocityCovOffset];
-[CLPLOGENTRYVISIONVIOInertialCovarianceInfo velocityDof];
```
