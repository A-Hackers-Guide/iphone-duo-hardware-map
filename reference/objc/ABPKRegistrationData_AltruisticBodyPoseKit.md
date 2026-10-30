# `ABPKRegistrationData`

- Image: [`/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit`](../userland/System__Library__PrivateFrameworks__AltruisticBodyPoseKit.framework__AltruisticBodyPoseKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 9 instance methods, 0 class methods

## Instance variables

```
{vector<float __attribute__((ext_vector_type(2))), std::allocator<float __attribute__((ext_vector_type(2)))>>="__begin_"^"__end_"^""{?="__cap_"^}} _imagePointsVector;
{vector<float __attribute__((ext_vector_type(3))), std::allocator<float __attribute__((ext_vector_type(3)))>>="__begin_"^"__end_"^""{?="__cap_"^}} _jointsLifted3DVector;
B _registrationValid;
Q _imagePointsCount;
Q _jointsLifted3DCount;
{CGSize="width"d"height"d} _imageDimensions;
{?="columns"[3]} _cameraIntrinsics;
{?="columns"[4]} _cameraFromBodyPose;
```

## Properties

```
@property (Tr^,R,N) imagePoints;
@property (TQ,R,N,V_imagePointsCount) imagePointsCount;
@property (Tr^,R,N) jointsLifted3D;
@property (TQ,R,N,V_jointsLifted3DCount) jointsLifted3DCount;
@property (T{?=[3]},R,N,V_cameraIntrinsics) cameraIntrinsics;
@property (T{CGSize=dd},R,N,V_imageDimensions) imageDimensions;
@property (T{?=[4]},R,N,V_cameraFromBodyPose) cameraFromBodyPose;
@property (TB,R,N,V_registrationValid) registrationValid;
```

## Instance methods

```
-[ABPKRegistrationData imageDimensions];
-[ABPKRegistrationData cameraIntrinsics];
-[ABPKRegistrationData cameraFromBodyPose];
-[ABPKRegistrationData imagePoints];
-[ABPKRegistrationData imagePointsCount];
-[ABPKRegistrationData initWithImagePoints:imagePointsCount:jointsLifted3D:jointsLifted3DCount:cameraIntrinsics:imageDimensions:cameraFromBodyPose:registrationValid:];
-[ABPKRegistrationData jointsLifted3D];
-[ABPKRegistrationData jointsLifted3DCount];
-[ABPKRegistrationData registrationValid];
```
