# `ABPKCameraRegistration`

- Image: [`/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit`](../userland/System__Library__PrivateFrameworks__AltruisticBodyPoseKit.framework__AltruisticBodyPoseKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 0 properties, 5 instance methods, 0 class methods

## Instance variables

```
d _tot_avg_err;
{BodyRegistration="m_last_result"{BodyRegistrationInfo="status"i"camera_from_body"{CameraPoseInfo="camera_matrix"{Matrix<double, 3U, 3U, false>="m_data"[9d]}"transform"{SE3GroupStorage<double, cva::Matrix<double, 4, 4>>="m_data"[16d]}"pose"{?="columns"[4]}}"correspondences"{Correspondences2d3d="image_points"{vector<cva::Matrix<double, 2, 1>, std::allocator<cva::Matrix<double, 2, 1>>>="__begin_"^v"__end_"^v""{?="__cap_"^v}}"model_points"{vector<cva::Matrix<double, 3, 1>, std::allocator<cva::Matrix<double, 3, 1>>>="__begin_"^v"__end_"^v""{?="__cap_"^v}}}}} _body_registration;
@"ABPKResultRegistration" _regResult;
{vector<float __attribute__((ext_vector_type(2))), std::allocator<float __attribute__((ext_vector_type(2)))>>="__begin_"^"__end_"^""{?="__cap_"^}} _imagePoints;
{vector<float __attribute__((ext_vector_type(3))), std::allocator<float __attribute__((ext_vector_type(3)))>>="__begin_"^"__end_"^""{?="__cap_"^}} _v3d_body;
{vector<float __attribute__((ext_vector_type(3))), std::allocator<float __attribute__((ext_vector_type(3)))>>="__begin_"^"__end_"^""{?="__cap_"^}} _v3d_cam;
```

## Instance methods

```
-[ABPKCameraRegistration init];
-[ABPKCameraRegistration _endRunCameraRegistrationSignpost];
-[ABPKCameraRegistration _startRunCameraRegistrationSignpost];
-[ABPKCameraRegistration estimateCameraPoseFromMatchingwithImageIntrinsics:imageResolution:joints2d:jointsLifted3D:jointsLifted3DCount:];
-[ABPKCameraRegistration runCameraRegistrationWithImageIntrinsics:imageResolution:liftingResult:];
```
