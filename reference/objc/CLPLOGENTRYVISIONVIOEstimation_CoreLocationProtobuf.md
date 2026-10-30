# `CLPLOGENTRYVISIONVIOEstimation`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 11 instance variables, 20 properties, 42 instance methods, 0 class methods

## Instance variables

```
@"CLPLOGENTRYVISIONCGSize" _cameraImageResolution;
@"CLPLOGENTRYVISIONSimdFloatMxN" _cameraIntrinsics;
@"CLPLOGENTRYVISIONSimdFloatMxN" _cameraPose;
@"NSData" _inertialCovariance;
@"CLPLOGENTRYVISIONVIOInertialCovarianceInfo" _inertialCovarianceInfo;
@"NSData" _inertialState;
@"CLPLOGENTRYVISIONVIOInertialStateInfo" _inertialStateInfo;
@"CLPLOGENTRYVISIONTimeStamp" _originTimestamp;
@"CLPLOGENTRYVISIONTimeStamp" _timestamp;
i _trackingState;
{?="trackingState"b1} _has;
```

## Properties

```
@property (TB,N) hasTrackingState;
@property (Ti,N,V_trackingState) trackingState;
@property (TB,R,N) hasOriginTimestamp;
@property (T@"CLPLOGENTRYVISIONTimeStamp",&,N,V_originTimestamp) originTimestamp;
@property (TB,R,N) hasTimestamp;
@property (T@"CLPLOGENTRYVISIONTimeStamp",&,N,V_timestamp) timestamp;
@property (TB,R,N) hasInertialStateInfo;
@property (T@"CLPLOGENTRYVISIONVIOInertialStateInfo",&,N,V_inertialStateInfo) inertialStateInfo;
@property (TB,R,N) hasInertialState;
@property (T@"NSData",&,N,V_inertialState) inertialState;
@property (TB,R,N) hasInertialCovarianceInfo;
@property (T@"CLPLOGENTRYVISIONVIOInertialCovarianceInfo",&,N,V_inertialCovarianceInfo) inertialCovarianceInfo;
@property (TB,R,N) hasInertialCovariance;
@property (T@"NSData",&,N,V_inertialCovariance) inertialCovariance;
@property (TB,R,N) hasCameraPose;
@property (T@"CLPLOGENTRYVISIONSimdFloatMxN",&,N,V_cameraPose) cameraPose;
@property (TB,R,N) hasCameraIntrinsics;
@property (T@"CLPLOGENTRYVISIONSimdFloatMxN",&,N,V_cameraIntrinsics) cameraIntrinsics;
@property (TB,R,N) hasCameraImageResolution;
@property (T@"CLPLOGENTRYVISIONCGSize",&,N,V_cameraImageResolution) cameraImageResolution;
```

## Instance methods

```
-[CLPLOGENTRYVISIONVIOEstimation hasTimestamp];
-[CLPLOGENTRYVISIONVIOEstimation setTimestamp:];
-[CLPLOGENTRYVISIONVIOEstimation writeTo:];
-[CLPLOGENTRYVISIONVIOEstimation mergeFrom:];
-[CLPLOGENTRYVISIONVIOEstimation timestamp];
-[CLPLOGENTRYVISIONVIOEstimation hash];
-[CLPLOGENTRYVISIONVIOEstimation copyTo:];
-[CLPLOGENTRYVISIONVIOEstimation description];
-[CLPLOGENTRYVISIONVIOEstimation readFrom:];
-[CLPLOGENTRYVISIONVIOEstimation copyWithZone:];
-[CLPLOGENTRYVISIONVIOEstimation isEqual:];
-[CLPLOGENTRYVISIONVIOEstimation dictionaryRepresentation];
-[CLPLOGENTRYVISIONVIOEstimation trackingState];
-[CLPLOGENTRYVISIONVIOEstimation cameraIntrinsics];
-[CLPLOGENTRYVISIONVIOEstimation originTimestamp];
-[CLPLOGENTRYVISIONVIOEstimation cameraImageResolution];
-[CLPLOGENTRYVISIONVIOEstimation cameraPose];
-[CLPLOGENTRYVISIONVIOEstimation inertialCovariance];
-[CLPLOGENTRYVISIONVIOEstimation inertialCovarianceInfo];
-[CLPLOGENTRYVISIONVIOEstimation inertialState];
-[CLPLOGENTRYVISIONVIOEstimation inertialStateInfo];
-[CLPLOGENTRYVISIONVIOEstimation setCameraImageResolution:];
-[CLPLOGENTRYVISIONVIOEstimation setCameraIntrinsics:];
-[CLPLOGENTRYVISIONVIOEstimation setCameraPose:];
-[CLPLOGENTRYVISIONVIOEstimation setInertialCovariance:];
-[CLPLOGENTRYVISIONVIOEstimation setInertialCovarianceInfo:];
-[CLPLOGENTRYVISIONVIOEstimation setInertialState:];
-[CLPLOGENTRYVISIONVIOEstimation setInertialStateInfo:];
-[CLPLOGENTRYVISIONVIOEstimation setOriginTimestamp:];
-[CLPLOGENTRYVISIONVIOEstimation setTrackingState:];
-[CLPLOGENTRYVISIONVIOEstimation StringAsTrackingState:];
-[CLPLOGENTRYVISIONVIOEstimation hasCameraImageResolution];
-[CLPLOGENTRYVISIONVIOEstimation hasCameraIntrinsics];
-[CLPLOGENTRYVISIONVIOEstimation hasCameraPose];
-[CLPLOGENTRYVISIONVIOEstimation hasInertialCovariance];
-[CLPLOGENTRYVISIONVIOEstimation hasInertialCovarianceInfo];
-[CLPLOGENTRYVISIONVIOEstimation hasInertialState];
-[CLPLOGENTRYVISIONVIOEstimation hasInertialStateInfo];
-[CLPLOGENTRYVISIONVIOEstimation hasOriginTimestamp];
-[CLPLOGENTRYVISIONVIOEstimation hasTrackingState];
-[CLPLOGENTRYVISIONVIOEstimation setHasTrackingState:];
-[CLPLOGENTRYVISIONVIOEstimation trackingStateAsString:];
```
