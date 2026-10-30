# `ABPKPoseEstimationPipeline`

- Image: [`/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit`](../userland/System__Library__PrivateFrameworks__AltruisticBodyPoseKit.framework__AltruisticBodyPoseKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 25 instance variables, 0 properties, 21 instance methods, 0 class methods

## Instance variables

```
q _exitPoint;
^{__CVBuffer=} _mlImage;
@"NSString" _saveDirectory;
@"ABPK2DDetectionConfiguration" _config2D;
B _deviceANEVersionPriorOrEqualToH12;
B _useLSTM3D;
@"ABPK2DPoseEstimation" _poseEstimation2D;
@"ABPK2DDetectionPostprocess" _postprocess2d;
@"ABPK3DLifting" _liftingAlgorithm;
@"ABPK3DLiftingSequence" _liftingAlgorithmSequence;
@"ABPK3DLiftingLSTM" _liftingAlgorithmLSTM;
@"ABPKCameraRegistration" _bodyRegistration;
@"ABPKDepthBasedScaleEstimation" _scaleEstimation;
@"ABPKRetargeting" _retargeting;
@"ABPK2dSkeleton" _rawDetection2dSkeleton;
@"ABPK2dSkeleton" _detection2dSkeleton;
@"NSMutableArray" _rawDetection2dSkeletonArray;
@"ABPKSkeleton" _liftingSkeleton;
@"ABPK2dSkeleton" _registered2dSkeleton;
@"ABPKSkeleton" _retargetedSkeleton;
f _previousValidScale;
{CGSize="width"d"height"d} _inputResolution;
@"ABPKImagePreProcessing" _imagePreprocessor;
@"ABPKImagePreProcessingParams" _imagePreProcessingParams;
i _consistent2DSkeletonMissing;
```

## Instance methods

```
-[ABPKPoseEstimationPipeline init];
-[ABPKPoseEstimationPipeline dealloc];
-[ABPKPoseEstimationPipeline runABPKAlgorithmWithInputData:andGetOutput:];
-[ABPKPoseEstimationPipeline _endExecuteAlgorithmSignpost];
-[ABPKPoseEstimationPipeline _endImagePreprocessingSignpost];
-[ABPKPoseEstimationPipeline _endInitABPKOutputSignpost];
-[ABPKPoseEstimationPipeline _endInitABPKSignpost];
-[ABPKPoseEstimationPipeline _endRetargettingSignpostWithTimestamp:];
-[ABPKPoseEstimationPipeline _endScaleEstimationSignpostWithTimestamp:];
-[ABPKPoseEstimationPipeline _startExecuteAlgorithmSignpost];
-[ABPKPoseEstimationPipeline _startImagePreprocessingSignpost];
-[ABPKPoseEstimationPipeline _startInitABPKOutputSignpost];
-[ABPKPoseEstimationPipeline _startInitABPKSignpost];
-[ABPKPoseEstimationPipeline _startRetargettingSignpostWithTimestamp:];
-[ABPKPoseEstimationPipeline _startScaleEstimationSignpostWithTimestamp:];
-[ABPKPoseEstimationPipeline computeRootTransforms:withCameraExtrinsics:withVioPose:withVioPoseValidity:];
-[ABPKPoseEstimationPipeline initAlgorithmModules];
-[ABPKPoseEstimationPipeline initializeOutput];
-[ABPKPoseEstimationPipeline runABPKPoseEstimationWithInputData:andGetOutput:];
-[ABPKPoseEstimationPipeline saveInputData:andOutputData:ToDir:withFileNamePrefix:];
-[ABPKPoseEstimationPipeline setExitPoint:];
```
