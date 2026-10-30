# `ABPKMultiPerson2DTracking`

- Image: [`/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit`](../userland/System__Library__PrivateFrameworks__AltruisticBodyPoseKit.framework__AltruisticBodyPoseKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 0 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"ABPKPersonIDTracker" _abpkPersonIDTracker;
@"ABPK2DDetectionConfiguration" _config2D;
@"ABPK2DPoseEstimation" _poseEstimation2D;
@"NSMutableArray" _previousMultiPerson2DResult;
@"NSMutableArray" _trackedBodies;
Q _lastTrackingId;
```

## Instance methods

```
-[ABPKMultiPerson2DTracking init];
-[ABPKMultiPerson2DTracking _startMultiPerson2DTrackingPersonTrackingSignpostWithTimestamp:];
-[ABPKMultiPerson2DTracking _endInitABPKSignpost];
-[ABPKMultiPerson2DTracking _endMultiPerson2DTracking2DDetectionMLSignpostWithTimestamp:];
-[ABPKMultiPerson2DTracking _endMultiPerson2DTracking2DDetectionPostProcessingSignpostWithTimestamp:];
-[ABPKMultiPerson2DTracking _endMultiPerson2DTrackingImagePreProcessingSignpostWithTimestamp:];
-[ABPKMultiPerson2DTracking _endMultiPerson2DTrackingPersonTrackingSignpostWithTimestamp:];
-[ABPKMultiPerson2DTracking _endMultiPerson2DTrackingRunWithInputSignpostWithTimestamp:];
-[ABPKMultiPerson2DTracking _rotateBoundingBoxToPortrait:withImageRes:];
-[ABPKMultiPerson2DTracking _startInitABPKSignpost];
-[ABPKMultiPerson2DTracking _startMultiPerson2DTracking2DDetectionMLSignpostWithTimestamp:];
-[ABPKMultiPerson2DTracking _startMultiPerson2DTracking2DDetectionPostProcessingSignpostWithTimestamp:];
-[ABPKMultiPerson2DTracking _startMultiPerson2DTrackingImagePreProcessingSignpostWithTimestamp:];
-[ABPKMultiPerson2DTracking _startMultiPerson2DTrackingRunWithInputSignpostWithTimestamp:];
-[ABPKMultiPerson2DTracking overlayResult:OnImage:andGenerateOverlayImage:];
-[ABPKMultiPerson2DTracking overlayTrackedBodiesOnImage:andGenerateOverlayImage:];
-[ABPKMultiPerson2DTracking runPoseEstimationWithInput:abpkDeviceOrientation:atTimeStamp:andOutput:];
-[ABPKMultiPerson2DTracking runWithInput:abpkDeviceOrientation:atTimeStamp:andOutput:];
```
