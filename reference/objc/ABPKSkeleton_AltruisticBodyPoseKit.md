# `ABPKSkeleton`

- Image: [`/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit`](../userland/System__Library__PrivateFrameworks__AltruisticBodyPoseKit.framework__AltruisticBodyPoseKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 27 instance methods, 0 class methods

## Instance variables

```
{vector<ABPKTransform, std::allocator<ABPKTransform>>="__begin_"^{ABPKTransform}"__end_"^{ABPKTransform}""{?="__cap_"^{ABPKTransform}}} _localPoses;
{vector<simd_float4x4, std::allocator<simd_float4x4>>="__begin_"^{?}"__end_"^{?}""{?="__cap_"^{?}}} _modelPoses;
f _estimatedScale;
q _skeletonType;
@"ABPKSkeletonDefinition" _skeletonDefinition;
{?="columns"[4]} _cameraRootTransform;
{?="columns"[4]} _renderingCameraRootTransform;
{?="columns"[4]} _deviceRootTransform;
```

## Properties

```
@property (Tq,R,N,V_skeletonType) skeletonType;
@property (T@"ABPKSkeletonDefinition",R,N,V_skeletonDefinition) skeletonDefinition;
@property (Tr^{ABPKTransform={?=}},R,N) localPoses;
@property (Tf,N,V_estimatedScale) estimatedScale;
@property (Tr^{?=[4]},R,N) modelPoses;
@property (T{?=[4]},N,V_cameraRootTransform) cameraRootTransform;
@property (T{?=[4]},N,V_renderingCameraRootTransform) renderingCameraRootTransform;
@property (T{?=[4]},N,V_deviceRootTransform) deviceRootTransform;
```

## Instance methods

```
-[ABPKSkeleton toDictionary];
-[ABPKSkeleton init];
-[ABPKSkeleton initWithType:];
-[ABPKSkeleton description];
-[ABPKSkeleton cameraRootTransform];
-[ABPKSkeleton computeHeight];
-[ABPKSkeleton estimatedScale];
-[ABPKSkeleton localPoses];
-[ABPKSkeleton modelPoses];
-[ABPKSkeleton renderingCameraRootTransform];
-[ABPKSkeleton skeletonDefinition];
-[ABPKSkeleton deviceRootTransform];
-[ABPKSkeleton getGlobalJointDataForSkeletonWithPosition:withOrientation:];
-[ABPKSkeleton getLocalJointDataForSkeletonWithPosition:withOrientation:];
-[ABPKSkeleton scaleTransform:withScale:];
-[ABPKSkeleton setCameraRootTransform:];
-[ABPKSkeleton setDeviceRootTransform:];
-[ABPKSkeleton setEstimatedScale:];
-[ABPKSkeleton setLocalPoses:andUpdateModelPoses:];
-[ABPKSkeleton setModelPoses:andUpdateLocalPoses:];
-[ABPKSkeleton setModelPosesFromDict:andUpdateLocalPoses:];
-[ABPKSkeleton setRenderingCameraRootTransform:];
-[ABPKSkeleton skeletonType];
-[ABPKSkeleton transformModelPoses:andUpdateLocalPoses:];
-[ABPKSkeleton updateJointPosesAndRootTransformUsingDepthEstimatedScale];
-[ABPKSkeleton updateLocalPosesFromModelPoses];
-[ABPKSkeleton updateModelPosesFromLocalPoses];
```
