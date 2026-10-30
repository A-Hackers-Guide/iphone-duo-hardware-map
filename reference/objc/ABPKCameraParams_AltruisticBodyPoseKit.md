# `ABPKCameraParams`

- Image: [`/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit`](../userland/System__Library__PrivateFrameworks__AltruisticBodyPoseKit.framework__AltruisticBodyPoseKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 20 instance methods, 0 class methods

## Instance variables

```
B _isImageRectified;
q _deviceType;
q _deviceOrientation;
_distortion;
{CGSize="width"d"height"d} _inputRes;
{?="columns"[3]} _intrinsics;
{?="columns"[4]} _extrinsics;
```

## Properties

```
@property (T{?=[3]},V_intrinsics) intrinsics;
@property (T{?=[4]},V_extrinsics) extrinsics;
@property (T,V_distortion) distortion;
@property (T{CGSize=dd},V_inputRes) inputRes;
@property (Tq,V_deviceType) deviceType;
@property (TB,V_isImageRectified) isImageRectified;
@property (Tq,V_deviceOrientation) deviceOrientation;
```

## Instance methods

```
-[ABPKCameraParams setDeviceType:];
-[ABPKCameraParams setDeviceOrientation:];
-[ABPKCameraParams deviceOrientation];
-[ABPKCameraParams initWithDictionary:];
-[ABPKCameraParams deviceType];
-[ABPKCameraParams initWithIntrinsics:andExtrinsics:andDistortion:andInputResolution:];
-[ABPKCameraParams inputRes];
-[ABPKCameraParams intrinsics];
-[ABPKCameraParams toDict];
-[ABPKCameraParams distortion];
-[ABPKCameraParams setIntrinsics:];
-[ABPKCameraParams checkAndSetApproximateIntrinsics];
-[ABPKCameraParams extrinsics];
-[ABPKCameraParams initWithIntrinsics:andExtrinsics:andDistortion:];
-[ABPKCameraParams isImageRectified];
-[ABPKCameraParams isMatrixIdentity:];
-[ABPKCameraParams setDistortion:];
-[ABPKCameraParams setExtrinsics:];
-[ABPKCameraParams setInputRes:];
-[ABPKCameraParams setIsImageRectified:];
```
