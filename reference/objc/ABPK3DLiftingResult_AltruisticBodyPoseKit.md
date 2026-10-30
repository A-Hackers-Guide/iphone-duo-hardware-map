# `ABPK3DLiftingResult`

- Image: [`/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit`](../userland/System__Library__PrivateFrameworks__AltruisticBodyPoseKit.framework__AltruisticBodyPoseKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 5 properties, 13 instance methods, 0 class methods

## Instance variables

```
{vector<float __attribute__((ext_vector_type(3))), std::allocator<float __attribute__((ext_vector_type(3)))>>="__begin_"^"__end_"^""{?="__cap_"^}} _jointsVector;
{vector<float __attribute__((ext_vector_type(3))), std::allocator<float __attribute__((ext_vector_type(3)))>>="__begin_"^"__end_"^""{?="__cap_"^}} _rawNetworkOutputJointsVector;
f _estimatedScale;
@"ABPK2DDetectionResult" _skeletonDetectionResult2D;
```

## Properties

```
@property (TQ,R,N) jointCount;
@property (T^,R,N) joints;
@property (T^,R,N) rawNetworkOutputJoints;
@property (T@"ABPK2DDetectionResult",R,N,V_skeletonDetectionResult2D) skeletonDetectionResult2D;
@property (Tf,N,V_estimatedScale) estimatedScale;
```

## Instance methods

```
-[ABPK3DLiftingResult init];
-[ABPK3DLiftingResult estimatedScale];
-[ABPK3DLiftingResult jointCount];
-[ABPK3DLiftingResult joints];
-[ABPK3DLiftingResult isJointTracked:];
-[ABPK3DLiftingResult createResultScaledByFactor:];
-[ABPK3DLiftingResult initWithJoints:numberOfJoints:];
-[ABPK3DLiftingResult initWithJoints:numberOfJoints:rawNetworkOutputs:referenceDetectionResult:];
-[ABPK3DLiftingResult initWithJoints:numberOfJoints:referenceDetectionResult:];
-[ABPK3DLiftingResult initWithJoints:rawNetworkOutputs:referenceDetectionResult:];
-[ABPK3DLiftingResult rawNetworkOutputJoints];
-[ABPK3DLiftingResult setEstimatedScale:];
-[ABPK3DLiftingResult skeletonDetectionResult2D];
```
