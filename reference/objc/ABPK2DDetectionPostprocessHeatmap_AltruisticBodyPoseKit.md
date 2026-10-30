# `ABPK2DDetectionPostprocessHeatmap`

- Image: [`/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit`](../userland/System__Library__PrivateFrameworks__AltruisticBodyPoseKit.framework__AltruisticBodyPoseKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ABPK2DDetectionPostprocess`
- 12 instance variables, 0 properties, 22 instance methods, 0 class methods

## Instance variables

```
Q _numberOfInputJoints;
Q _numberOfOutputJoints;
B _saveKeypoints;
B _humansDetected;
@"ABPKImagePreProcessingParams" _imagePreProcessingParams;
@"ABPK2DExtrapolationFiltering" _extrapolationFiltering;
B _abpkPersonIDTrackerSupportedOnDevice;
@"ABPKPersonIDTracker" _abpkPersonIDTracker;
@"NSMutableArray" _trackedBodies;
q _abpkPersonTrackerFPS;
f _timeLastABPKTrackerRun;
f _timeLastABPKTrackerRunThreshold;
```

## Instance methods

```
-[ABPK2DDetectionPostprocessHeatmap rawTrackedHuman];
-[ABPK2DDetectionPostprocessHeatmap _endExtract2DSkeletonSignpostWithTimestamp:];
-[ABPK2DDetectionPostprocessHeatmap _endExtractHumanSignpostWithTimestamp:];
-[ABPK2DDetectionPostprocessHeatmap _endExtrapolationSignpostWithTimestamp:];
-[ABPK2DDetectionPostprocessHeatmap _endMaxFilterSignpostWithTimestamp:];
-[ABPK2DDetectionPostprocessHeatmap _startExtract2DSkeletonSignpostWithTimestamp:];
-[ABPK2DDetectionPostprocessHeatmap _startExtractHumanSignpostWithTimestamp:];
-[ABPK2DDetectionPostprocessHeatmap _startExtrapolationSignpostWithTimestamp:];
-[ABPK2DDetectionPostprocessHeatmap _startMaxFilterSignpostWithTimestamp:];
-[ABPK2DDetectionPostprocessHeatmap extract2DSkeletonfromBuffers:withImagePreProcessingParams:atTimestamp:previousSkeleton3D:];
-[ABPK2DDetectionPostprocessHeatmap get2DDetectionResultforRotation:croppedRect:];
-[ABPK2DDetectionPostprocessHeatmap getAligned3DSkeleton];
-[ABPK2DDetectionPostprocessHeatmap getRaw2DDetectionResultforRotation:croppedRect:];
-[ABPK2DDetectionPostprocessHeatmap getRawTrackedHumanForLiftingSkeleton:];
-[ABPK2DDetectionPostprocessHeatmap getRawTrackedHumanSkeleton:];
-[ABPK2DDetectionPostprocessHeatmap getRawTrackedHumanSkeletonVector:];
-[ABPK2DDetectionPostprocessHeatmap getTrackedHumanForLiftingSkeleton:];
-[ABPK2DDetectionPostprocessHeatmap getTrackedHumanSkeleton:];
-[ABPK2DDetectionPostprocessHeatmap initWithInputJoints:andOutputJoints:use3DSkeletonForExtrapolation:shouldPush3DSupportSkeleton:withExtrapolationTime:];
-[ABPK2DDetectionPostprocessHeatmap rawTrackedHumanVector];
-[ABPK2DDetectionPostprocessHeatmap trackedHuman];
-[ABPK2DDetectionPostprocessHeatmap trackedHumanForLifting];
```
