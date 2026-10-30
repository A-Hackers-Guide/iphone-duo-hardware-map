# `ABPK2DExtrapolationFiltering`

- Image: [`/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit`](../userland/System__Library__PrivateFrameworks__AltruisticBodyPoseKit.framework__AltruisticBodyPoseKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 1 properties, 10 instance methods, 0 class methods

## Instance variables

```
{SkeletonJointFilter<float>="m_values"{vector<float, std::allocator<float>>="__begin_"^f"__end_"^f""{?="__cap_"^f}}"m_speed"{vector<float, std::allocator<float>>="__begin_"^f"__end_"^f""{?="__cap_"^f}}"m_timestamps"{vector<double, std::allocator<double>>="__begin_"^d"__end_"^d""{?="__cap_"^d}}"m_smoothing"f"m_lowest_threshold"f"m_low_threshold"f"m_high_threshold"f"m_highest_threshold"f"m_temporal_smoothing"f"m_prediction_factor"f"m_min_smoothing"f"m_up_slope"f"m_down_slope"f"m_temporal_slope"f} _extrapolationFilter2D;
d _extrapolationTime;
{SkeletonJointFilter<float>="m_values"{vector<float, std::allocator<float>>="__begin_"^f"__end_"^f""{?="__cap_"^f}}"m_speed"{vector<float, std::allocator<float>>="__begin_"^f"__end_"^f""{?="__cap_"^f}}"m_timestamps"{vector<double, std::allocator<double>>="__begin_"^d"__end_"^d""{?="__cap_"^d}}"m_smoothing"f"m_lowest_threshold"f"m_low_threshold"f"m_high_threshold"f"m_highest_threshold"f"m_temporal_smoothing"f"m_prediction_factor"f"m_min_smoothing"f"m_up_slope"f"m_down_slope"f"m_temporal_slope"f} _extrapolationFilter2DForLiftingData;
{Human="keypoints"{vector<float __attribute__((ext_vector_type(2))), std::allocator<float __attribute__((ext_vector_type(2)))>>="__begin_"^"__end_"^""{?="__cap_"^}}"_jointsTrackingState"{vector<unsigned int, std::allocator<unsigned int>>="__begin_"^I"__end_"^I""{?="__cap_"^I}}"_confidence"{vector<float, std::allocator<float>>="__begin_"^f"__end_"^f""{?="__cap_"^f}}"_jointVector"{optional<std::vector<float __attribute__((ext_vector_type(2)))>>=""(?="__null_state_"c"__val_"{vector<float __attribute__((ext_vector_type(2))), std::allocator<float __attribute__((ext_vector_type(2)))>>="__begin_"^"__end_"^""{?="__cap_"^}})"__engaged_"B}"_trackedJointsCount"Q"_area"{optional<float>=""(?="__null_state_"c"__val_"f)"__engaged_"B}} _trackedHuman;
{Human="keypoints"{vector<float __attribute__((ext_vector_type(2))), std::allocator<float __attribute__((ext_vector_type(2)))>>="__begin_"^"__end_"^""{?="__cap_"^}}"_jointsTrackingState"{vector<unsigned int, std::allocator<unsigned int>>="__begin_"^I"__end_"^I""{?="__cap_"^I}}"_confidence"{vector<float, std::allocator<float>>="__begin_"^f"__end_"^f""{?="__cap_"^f}}"_jointVector"{optional<std::vector<float __attribute__((ext_vector_type(2)))>>=""(?="__null_state_"c"__val_"{vector<float __attribute__((ext_vector_type(2))), std::allocator<float __attribute__((ext_vector_type(2)))>>="__begin_"^"__end_"^""{?="__cap_"^}})"__engaged_"B}"_trackedJointsCount"Q"_area"{optional<float>=""(?="__null_state_"c"__val_"f)"__engaged_"B}} _rawTrackedHuman;
B _shouldPush3DSupportSkeleton;
B _use3DSupportSkeletonForExtrapolation;
{vector<abpk::Human, std::allocator<abpk::Human>>="__begin_"^{Human}"__end_"^{Human}""{?="__cap_"^{Human}}} _rawTrackedHumanVector;
{Human="keypoints"{vector<float __attribute__((ext_vector_type(2))), std::allocator<float __attribute__((ext_vector_type(2)))>>="__begin_"^"__end_"^""{?="__cap_"^}}"_jointsTrackingState"{vector<unsigned int, std::allocator<unsigned int>>="__begin_"^I"__end_"^I""{?="__cap_"^I}}"_confidence"{vector<float, std::allocator<float>>="__begin_"^f"__end_"^f""{?="__cap_"^f}}"_jointVector"{optional<std::vector<float __attribute__((ext_vector_type(2)))>>=""(?="__null_state_"c"__val_"{vector<float __attribute__((ext_vector_type(2))), std::allocator<float __attribute__((ext_vector_type(2)))>>="__begin_"^"__end_"^""{?="__cap_"^}})"__engaged_"B}"_trackedJointsCount"Q"_area"{optional<float>=""(?="__null_state_"c"__val_"f)"__engaged_"B}} _trackedHumanForLifting;
{__wrap_iter<const abpk::Human *>="__i_"^{Human}} _iteratorToTrackedInstance;
Q _lastANSTTrackedInstanceId;
d _lastANSTTrackedInstanceIdTime;
@"ABPK2DDetectionResult" _aligned3DSkeleton;
```

## Properties

```
@property (T@"ABPK2DDetectionResult",R,N,V_aligned3DSkeleton) aligned3DSkeleton;
```

## Instance methods

```
-[ABPK2DExtrapolationFiltering rawTrackedHuman];
-[ABPK2DExtrapolationFiltering _getTrackedHumanForHumans:atTimestamp:withImageResolution:];
-[ABPK2DExtrapolationFiltering _getTrackedHumanForHumans:atTimestamp:withImageResolution:withPersonTracker:];
-[ABPK2DExtrapolationFiltering aligned3DSkeleton];
-[ABPK2DExtrapolationFiltering initWithUse3DSkeletonForExtrapolation:shouldPush3DSupportSkeleton:withExtrapolationTime:];
-[ABPK2DExtrapolationFiltering performExtrapolationOnHumans:withImageResolution:atTimestamp:rotationNeeded:previousSkeleton3D:];
-[ABPK2DExtrapolationFiltering performExtrapolationOnHumans:withImageResolution:atTimestamp:rotationNeeded:previousSkeleton3D:personTracker:];
-[ABPK2DExtrapolationFiltering rawTrackedHumanVector];
-[ABPK2DExtrapolationFiltering trackedHuman];
-[ABPK2DExtrapolationFiltering trackedHumanForLifting];
```
