# `ABPKResultRetargeting`

- Image: [`/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit`](../userland/System__Library__PrivateFrameworks__AltruisticBodyPoseKit.framework__AltruisticBodyPoseKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 8 instance methods, 0 class methods

## Instance variables

```
{vector<simd_float4x4, std::allocator<simd_float4x4>>="__begin_"^{?}"__end_"^{?}""{?="__cap_"^{?}}} _modelTransforms;
{vector<ABPKSRT, std::allocator<ABPKSRT>>="__begin_"^{ABPKSRT}"__end_"^{ABPKSRT}""{?="__cap_"^{ABPKSRT}}} _localTransformsSRT;
{vector<simd_float4x4, std::allocator<simd_float4x4>>="__begin_"^{?}"__end_"^{?}""{?="__cap_"^{?}}} _localTransforms;
@"ABPK3DLiftingResult" _liftingResult;
f _estimatedScale;
@"NSUUID" _identifier;
```

## Properties

```
@property (TQ,R,N) jointTransformCount;
@property (Tr^{?=[4]},R,N) jointModelTransforms;
@property (Tr^{?=[4]},R,N) jointLocalTransforms;
@property (Tr^{ABPKSRT={?=}},R,N) localJointTransformsSRT;
@property (Tf,N,V_estimatedScale) estimatedScale;
@property (T@"NSUUID",R,N,V_identifier) identifier;
```

## Instance methods

```
-[ABPKResultRetargeting identifier];
-[ABPKResultRetargeting estimatedScale];
-[ABPKResultRetargeting jointTransformCount];
-[ABPKResultRetargeting localJointTransformsSRT];
-[ABPKResultRetargeting initWithModelJointTransforms:localJointTransformsSRT:numberOfTransforms:liftedSkeletonData:identifier:];
-[ABPKResultRetargeting jointLocalTransforms];
-[ABPKResultRetargeting jointModelTransforms];
-[ABPKResultRetargeting setEstimatedScale:];
```
