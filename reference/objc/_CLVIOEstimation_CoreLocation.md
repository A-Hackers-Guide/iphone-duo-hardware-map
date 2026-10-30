# `_CLVIOEstimation`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 10 instance variables, 10 properties, 26 instance methods, 1 class methods

## Instance variables

```
i _trackingState;
d _originTimestamp;
d _timestamp;
@"NSData" _inertialState;
@"NSData" _inertialCovariance;
{CGSize="width"d"height"d} _cameraImageResolution;
{?="stateLengthInBytes"Q"stateLength"C"orientationOffset"C"orientationLength"C"gyroBiasOffset"C"gyroBiasLength"C"velocityOffset"C"velocityLength"C"accelBiasOffset"C"accelBiasLength"C"positionOffset"C"positionLength"C} _inertialStateInfo;
{?="covarianceSizeInBytes"Q"covarianceSize"C"orientationCovOffset"C"orientationDof"C"gyroBiasCovOffset"C"gyroBiasDof"C"velocityCovOffset"C"velocityDof"C"accelBiasCovOffset"C"accelBiasDof"C"positionCovOffset"C"positionDof"C} _inertialCovarianceInfo;
{?="columns"[3]} _cameraIntrinsics;
{?="columns"[4]} _cameraPose;
```

## Properties

```
@property (Ti,N,V_trackingState) trackingState;
@property (Td,N,V_originTimestamp) originTimestamp;
@property (Td,N,V_timestamp) timestamp;
@property (T{?=QCCCCCCCCCCC},N,V_inertialStateInfo) inertialStateInfo;
@property (T@"NSData",C,N,V_inertialState) inertialState;
@property (T{?=QCCCCCCCCCCC},N,V_inertialCovarianceInfo) inertialCovarianceInfo;
@property (T@"NSData",C,N,V_inertialCovariance) inertialCovariance;
@property (T{?=[4]},N,V_cameraPose) cameraPose;
@property (T{?=[3]},N,V_cameraIntrinsics) cameraIntrinsics;
@property (T{CGSize=dd},N,V_cameraImageResolution) cameraImageResolution;
```

## Class methods

```
+[_CLVIOEstimation supportsSecureCoding];
```

## Instance methods

```
-[_CLVIOEstimation setTimestamp:];
-[_CLVIOEstimation dealloc];
-[_CLVIOEstimation timestamp];
-[_CLVIOEstimation encodeWithCoder:];
-[_CLVIOEstimation description];
-[_CLVIOEstimation initWithCoder:];
-[_CLVIOEstimation copyWithZone:];
-[_CLVIOEstimation trackingState];
-[_CLVIOEstimation cameraIntrinsics];
-[_CLVIOEstimation originTimestamp];
-[_CLVIOEstimation cameraImageResolution];
-[_CLVIOEstimation cameraPose];
-[_CLVIOEstimation descriptionWithMemberIndent:endIndent:];
-[_CLVIOEstimation inertialCovariance];
-[_CLVIOEstimation inertialCovarianceInfo];
-[_CLVIOEstimation inertialState];
-[_CLVIOEstimation inertialStateInfo];
-[_CLVIOEstimation setCameraImageResolution:];
-[_CLVIOEstimation setCameraIntrinsics:];
-[_CLVIOEstimation setCameraPose:];
-[_CLVIOEstimation setInertialCovariance:];
-[_CLVIOEstimation setInertialCovarianceInfo:];
-[_CLVIOEstimation setInertialState:];
-[_CLVIOEstimation setInertialStateInfo:];
-[_CLVIOEstimation setOriginTimestamp:];
-[_CLVIOEstimation setTrackingState:];
```
