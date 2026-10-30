# `ABPKDepthBasedScaleEstimation`

- Image: [`/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit`](../userland/System__Library__PrivateFrameworks__AltruisticBodyPoseKit.framework__AltruisticBodyPoseKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 4 instance methods, 0 class methods

## Instance variables

```
d _last_detection_timestamp;
{array<float, 2UL>="__elems_"[2f]} _depth_scaler_num_den;
Q _depth_scaler_observation_count;
```

## Instance methods

```
-[ABPKDepthBasedScaleEstimation resetState];
-[ABPKDepthBasedScaleEstimation init];
-[ABPKDepthBasedScaleEstimation estimateScaleFromDepthData:depthConfidenceData:timestamp:imageResolution:imageIntrinsics:cameraFromBodyPose:liftingResult:];
-[ABPKDepthBasedScaleEstimation estimateScaleFromJasperCloud:cameraFromBodyPose:liftingResult:];
```
