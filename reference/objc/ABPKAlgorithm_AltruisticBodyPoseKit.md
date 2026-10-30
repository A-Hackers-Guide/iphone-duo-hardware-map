# `ABPKAlgorithm`

- Image: [`/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit`](../userland/System__Library__PrivateFrameworks__AltruisticBodyPoseKit.framework__AltruisticBodyPoseKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 0 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"ABPKAlgorithmParams" _algParams;
q _exitPoint;
@"ABPK2DPoseEstimation" _poseEstimation2D;
@"ABPK2DDetectionPostprocess" _postprocess2d;
@"ABPK3DLifting" _liftingAlgorithm;
@"ABPKCameraRegistration" _bodyRegistration;
@"ABPKDepthBasedScaleEstimation" _scaleEstimation;
@"ABPKRetargeting" _retargeting;
f _previousValidScale;
```

## Instance methods

```
-[ABPKAlgorithm initWithParams:];
-[ABPKAlgorithm _endABPKRunWithInputSignpostWithTimestamp:];
-[ABPKAlgorithm _endInitABPKSignpost];
-[ABPKAlgorithm _endRetargettingSignpostWithTimestamp:];
-[ABPKAlgorithm _endScaleEstimationSignpostWithTimestamp:];
-[ABPKAlgorithm _startABPKRunWithInputSignpostWithTimestamp:];
-[ABPKAlgorithm _startInitABPKSignpost];
-[ABPKAlgorithm _startRetargettingSignpostWithTimestamp:];
-[ABPKAlgorithm _startScaleEstimationSignpostWithTimestamp:];
-[ABPKAlgorithm runWithInput:andGetOutput:];
-[ABPKAlgorithm setExitPoint:];
```
