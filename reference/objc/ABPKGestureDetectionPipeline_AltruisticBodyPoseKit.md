# `ABPKGestureDetectionPipeline`

- Image: [`/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit`](../userland/System__Library__PrivateFrameworks__AltruisticBodyPoseKit.framework__AltruisticBodyPoseKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 0 properties, 21 instance methods, 0 class methods

## Instance variables

```
I _fps;
@"ABPK2DDetectionConfiguration" _config2D;
@"ABPK2DPoseEstimation" _poseEstimation2D;
@"NSMutableDictionary" _joints2DBufferDict;
@"NSMutableArray" _previousGestureDetectionResult;
Q _lastTrackingId;
I _maxPreviousPoses;
I _raisingMaxPreviousPoses;
I _wavingMinPeriodicFrames;
I _wavingAngleChangeLastFrames;
```

## Instance methods

```
-[ABPKGestureDetectionPipeline init];
-[ABPKGestureDetectionPipeline initWithFrequency:];
-[ABPKGestureDetectionPipeline _endGestureDetection2DDetectionMLSignpostWithTimestamp:];
-[ABPKGestureDetectionPipeline _endGestureDetection2DDetectionPostProcessingSignpostWithTimestamp:];
-[ABPKGestureDetectionPipeline _endGestureDetectionAlgorithmSignpostWithTimestamp:];
-[ABPKGestureDetectionPipeline _endGestureDetectionImagePreProcessingSignpostWithTimestamp:];
-[ABPKGestureDetectionPipeline _endGestureDetectionPersonTrackingSignpostWithTimestamp:];
-[ABPKGestureDetectionPipeline _endGestureDetectionRunWithInputSignpostWithTimestamp:];
-[ABPKGestureDetectionPipeline _endInitABPKSignpost];
-[ABPKGestureDetectionPipeline _startGestureDetection2DDetectionMLSignpostWithTimestamp:];
-[ABPKGestureDetectionPipeline _startGestureDetection2DDetectionPostProcessingSignpostWithTimestamp:];
-[ABPKGestureDetectionPipeline _startGestureDetectionAlgorithmSignpostWithTimestamp:];
-[ABPKGestureDetectionPipeline _startGestureDetectionImagePreProcessingSignpostWithTimestamp:];
-[ABPKGestureDetectionPipeline _startGestureDetectionPersonTrackingSignpostWithTimestamp:];
-[ABPKGestureDetectionPipeline _startGestureDetectionRunWithInputSignpostWithTimestamp:];
-[ABPKGestureDetectionPipeline _startInitABPKSignpost];
-[ABPKGestureDetectionPipeline extractDataForJointIdx:fromPoseTimeArray:];
-[ABPKGestureDetectionPipeline overlayResult:OnImage:andGenerateOverlayImage:];
-[ABPKGestureDetectionPipeline runGestureDetection:withTrackingId:andResult:];
-[ABPKGestureDetectionPipeline runPoseEstimationWithInput:abpkDeviceOrientation:atTimeStamp:andOutput:];
-[ABPKGestureDetectionPipeline runWithInput:abpkDeviceOrientation:atTimeStamp:andOutput:];
```
