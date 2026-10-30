# `ABPK2DPoseEstimation`

- Image: [`/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit`](../userland/System__Library__PrivateFrameworks__AltruisticBodyPoseKit.framework__AltruisticBodyPoseKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"ABPK2DDetectionConfiguration" _config2D;
@"ABPK2DDetection" _detection2dAlgorithm;
@"ABPK2DDetectionPostprocess" _postprocess2d;
```

## Instance methods

```
-[ABPK2DPoseEstimation getRawTrackedHumanForLiftingSkeleton:];
-[ABPK2DPoseEstimation getRawTrackedHumanSkeleton:];
-[ABPK2DPoseEstimation getRawTrackedHumanSkeletonVector:];
-[ABPK2DPoseEstimation getTrackedHumanForLiftingSkeleton:];
-[ABPK2DPoseEstimation getTrackedHumanSkeleton:];
-[ABPK2DPoseEstimation initWith2DDetectionConfig:use3DSkeletonForExtrapolation:shouldPush3DSupportSkeleton:];
-[ABPK2DPoseEstimation runWithMLImageData:rotationOfResultTensor:];
```
