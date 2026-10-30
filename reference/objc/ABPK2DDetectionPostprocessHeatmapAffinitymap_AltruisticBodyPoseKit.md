# `ABPK2DDetectionPostprocessHeatmapAffinitymap`

- Image: [`/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit`](../userland/System__Library__PrivateFrameworks__AltruisticBodyPoseKit.framework__AltruisticBodyPoseKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ABPK2DDetectionPostprocess`
- 6 instance variables, 0 properties, 22 instance methods, 0 class methods

## Instance variables

```
Q _numberOfInputJoints;
Q _numberOfOutputJoints;
@"ABPK2DDetectionPostprocessGPU" _postprocessorGPU;
@"ABPKImagePreProcessingParams" _imagePreProcessingParams;
@"ABPK2DExtrapolationFiltering" _extrapolationFiltering;
B _humansDetected;
```

## Instance methods

```
-[ABPK2DDetectionPostprocessHeatmapAffinitymap rawTrackedHuman];
-[ABPK2DDetectionPostprocessHeatmapAffinitymap _endExtract2DSkeletonSignpostWithTimestamp:];
-[ABPK2DDetectionPostprocessHeatmapAffinitymap _endExtractHumanSignpostWithTimestamp:];
-[ABPK2DDetectionPostprocessHeatmapAffinitymap _endExtrapolationSignpostWithTimestamp:];
-[ABPK2DDetectionPostprocessHeatmapAffinitymap _endMaxFilterSignpostWithTimestamp:];
-[ABPK2DDetectionPostprocessHeatmapAffinitymap _startExtract2DSkeletonSignpostWithTimestamp:];
-[ABPK2DDetectionPostprocessHeatmapAffinitymap _startExtractHumanSignpostWithTimestamp:];
-[ABPK2DDetectionPostprocessHeatmapAffinitymap _startExtrapolationSignpostWithTimestamp:];
-[ABPK2DDetectionPostprocessHeatmapAffinitymap _startMaxFilterSignpostWithTimestamp:];
-[ABPK2DDetectionPostprocessHeatmapAffinitymap extract2DSkeletonfromBuffers:withImagePreProcessingParams:atTimestamp:previousSkeleton3D:];
-[ABPK2DDetectionPostprocessHeatmapAffinitymap get2DDetectionResultforRotation:croppedRect:];
-[ABPK2DDetectionPostprocessHeatmapAffinitymap getAligned3DSkeleton];
-[ABPK2DDetectionPostprocessHeatmapAffinitymap getRaw2DDetectionResultforRotation:croppedRect:];
-[ABPK2DDetectionPostprocessHeatmapAffinitymap getRawTrackedHumanForLiftingSkeleton:];
-[ABPK2DDetectionPostprocessHeatmapAffinitymap getRawTrackedHumanSkeleton:];
-[ABPK2DDetectionPostprocessHeatmapAffinitymap getRawTrackedHumanSkeletonVector:];
-[ABPK2DDetectionPostprocessHeatmapAffinitymap getTrackedHumanForLiftingSkeleton:];
-[ABPK2DDetectionPostprocessHeatmapAffinitymap getTrackedHumanSkeleton:];
-[ABPK2DDetectionPostprocessHeatmapAffinitymap initWithInputJoints:andOutputJoints:use3DSkeletonForExtrapolation:shouldPush3DSupportSkeleton:withExtrapolationTime:];
-[ABPK2DDetectionPostprocessHeatmapAffinitymap rawTrackedHumanVector];
-[ABPK2DDetectionPostprocessHeatmapAffinitymap trackedHuman];
-[ABPK2DDetectionPostprocessHeatmapAffinitymap trackedHumanForLifting];
```
