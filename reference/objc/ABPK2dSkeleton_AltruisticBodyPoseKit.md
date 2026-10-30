# `ABPK2dSkeleton`

- Image: [`/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit`](../userland/System__Library__PrivateFrameworks__AltruisticBodyPoseKit.framework__AltruisticBodyPoseKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 10 properties, 22 instance methods, 0 class methods

## Instance variables

```
{vector<float __attribute__((ext_vector_type(2))), std::allocator<float __attribute__((ext_vector_type(2)))>>="__begin_"^"__end_"^""{?="__cap_"^}} _keypoints2d;
{vector<float __attribute__((ext_vector_type(2))), std::allocator<float __attribute__((ext_vector_type(2)))>>="__begin_"^"__end_"^""{?="__cap_"^}} _normalizedKeypoints2d;
{vector<float, std::allocator<float>>="__begin_"^f"__end_"^f""{?="__cap_"^f}} _confidences;
{vector<unsigned int, std::allocator<unsigned int>>="__begin_"^I"__end_"^I""{?="__cap_"^I}} _visibility;
B _hasMissingJoints;
q _skeletonType;
@"ABPKSkeletonDefinition" _skeletonDefinition;
q _imageType;
{CGSize="width"d"height"d} _imageRes;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _boundingBox;
```

## Properties

```
@property (Tq,R,N,V_skeletonType) skeletonType;
@property (T@"ABPKSkeletonDefinition",R,N,V_skeletonDefinition) skeletonDefinition;
@property (Tr^,R,N) keypoints2d;
@property (Tr^,R,N) normalizedKeypoints2d;
@property (Tr^f,R,N) confidences;
@property (Tr^I,R,N) visibility;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_boundingBox) boundingBox;
@property (T{CGSize=dd},R,N,V_imageRes) imageRes;
@property (Tq,R,N,V_imageType) imageType;
@property (TB,R,N) hasMissingJoints;
```

## Instance methods

```
-[ABPK2dSkeleton toDictionary];
-[ABPK2dSkeleton imageType];
-[ABPK2dSkeleton init];
-[ABPK2dSkeleton visibility];
-[ABPK2dSkeleton initWithType:];
-[ABPK2dSkeleton boundingBox];
-[ABPK2dSkeleton description];
-[ABPK2dSkeleton skeletonDefinition];
-[ABPK2dSkeleton confidences];
-[ABPK2dSkeleton computeBoundingBox];
-[ABPK2dSkeleton hasMissingJoints];
-[ABPK2dSkeleton imageRes];
-[ABPK2dSkeleton keypoints2d];
-[ABPK2dSkeleton normalizedKeypoints2d];
-[ABPK2dSkeleton overlaySkeletonOnImage:withResult:withColor:];
-[ABPK2dSkeleton printData];
-[ABPK2dSkeleton setHasMissingJoints:];
-[ABPK2dSkeleton setJointConfidences:];
-[ABPK2dSkeleton setJointVisibility:];
-[ABPK2dSkeleton setKeypoints2d:withImageRes:];
-[ABPK2dSkeleton setNormalizedKeypoints2d:withImageRes:];
-[ABPK2dSkeleton skeletonType];
```
