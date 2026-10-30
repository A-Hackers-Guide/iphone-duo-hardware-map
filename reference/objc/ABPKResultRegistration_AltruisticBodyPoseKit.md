# `ABPKResultRegistration`

- Image: [`/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit`](../userland/System__Library__PrivateFrameworks__AltruisticBodyPoseKit.framework__AltruisticBodyPoseKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 16 instance methods, 0 class methods

## Instance variables

```
B _success;
^ _joints2d;
^ _joints3dWrtBody;
^ _joints3dWrtCamera;
_distortion;
{CGSize="width"d"height"d} _imageSize;
{?="columns"[3]} _intrinsics;
{?="columns"[4]} _cameraFromBodyPose;
```

## Properties

```
@property (TB,N,V_success) success;
@property (T^,N,V_joints2d) joints2d;
@property (T^,N,V_joints3dWrtBody) joints3dWrtBody;
@property (T^,N,V_joints3dWrtCamera) joints3dWrtCamera;
@property (T{?=[3]},N,V_intrinsics) intrinsics;
@property (T,N,V_distortion) distortion;
@property (T{CGSize=dd},N,V_imageSize) imageSize;
@property (T{?=[4]},N,V_cameraFromBodyPose) cameraFromBodyPose;
```

## Instance methods

```
-[ABPKResultRegistration imageSize];
-[ABPKResultRegistration setSuccess:];
-[ABPKResultRegistration success];
-[ABPKResultRegistration setImageSize:];
-[ABPKResultRegistration intrinsics];
-[ABPKResultRegistration distortion];
-[ABPKResultRegistration setIntrinsics:];
-[ABPKResultRegistration joints3dWrtBody];
-[ABPKResultRegistration cameraFromBodyPose];
-[ABPKResultRegistration joints2d];
-[ABPKResultRegistration joints3dWrtCamera];
-[ABPKResultRegistration setCameraFromBodyPose:];
-[ABPKResultRegistration setDistortion:];
-[ABPKResultRegistration setJoints2d:];
-[ABPKResultRegistration setJoints3dWrtBody:];
-[ABPKResultRegistration setJoints3dWrtCamera:];
```
