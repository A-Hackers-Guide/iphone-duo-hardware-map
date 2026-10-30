# `ABPK2DDetectionResult`

- Image: [`/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit`](../userland/System__Library__PrivateFrameworks__AltruisticBodyPoseKit.framework__AltruisticBodyPoseKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 6 instance variables, 7 properties, 16 instance methods, 1 class methods

## Instance variables

```
{vector<float __attribute__((ext_vector_type(2))), std::allocator<float __attribute__((ext_vector_type(2)))>>="__begin_"^"__end_"^""{?="__cap_"^}} _rawJoints;
{vector<float __attribute__((ext_vector_type(2))), std::allocator<float __attribute__((ext_vector_type(2)))>>="__begin_"^"__end_"^""{?="__cap_"^}} _rotatedJoints;
{vector<unsigned int, std::allocator<unsigned int>>="__begin_"^I"__end_"^I""{?="__cap_"^I}} _jointTrackingStates;
{CGSize="width"d"height"d} _imageResolution;
@"ABPK2D3DLiftingData" _liftingData;
q _rotation;
```

## Properties

```
@property (Tr^,R,N) joints;
@property (Tr^,R,N) rawJointsOutput;
@property (Tr^I,R,N) jointTrackingStates;
@property (TQ,R,N) jointCount;
@property (T{CGSize=dd},R,N,V_imageResolution) imageResolution;
@property (T@"ABPK2D3DLiftingData",R,N,V_liftingData) liftingData;
@property (Tq,R,N,V_rotation) rotation;
```

## Class methods

```
+[ABPK2DDetectionResult supportsSecureCoding];
```

## Instance methods

```
-[ABPK2DDetectionResult rotation];
-[ABPK2DDetectionResult encodeWithCoder:];
-[ABPK2DDetectionResult hash];
-[ABPK2DDetectionResult initWithCoder:];
-[ABPK2DDetectionResult isEqual:];
-[ABPK2DDetectionResult jointCount];
-[ABPK2DDetectionResult joints];
-[ABPK2DDetectionResult imageResolution];
-[ABPK2DDetectionResult rawJointsOutput];
-[ABPK2DDetectionResult alignSkeleton:rotationNeeded:];
-[ABPK2DDetectionResult initWithJoints:trackingStates:numberOfJoints:aligningPreviousSkeleton:rotation:];
-[ABPK2DDetectionResult initWithJoints:trackingStates:numberOfJoints:imageResolution:rotation:croppedRect:liftingData:];
-[ABPK2DDetectionResult initWithJoints:trackingStates:numberOfJoints:rotation:croppedRect:liftingData:];
-[ABPK2DDetectionResult jointTrackingStates];
-[ABPK2DDetectionResult liftingData];
-[ABPK2DDetectionResult trackedJointCount];
```
