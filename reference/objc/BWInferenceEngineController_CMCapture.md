# `BWInferenceEngineController`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorController`
- Protocols: `BWInferenceEngineControllerInputDelegate`, `BWInferenceFormatProvider`
- 10 instance variables, 6 properties, 24 instance methods, 9 class methods

## Instance variables

```
@"NSString" _contextName;
B _inferenceEnginePrepared;
B _inferenceEnginePreparedToReconfigure;
@"BWInferenceEngine" _inferenceEngine;
@"BWVideoFormat" _inputFormat;
@"NSDictionary" _inferenceOutputFormatByAttachedMediaKey;
B _appliesFinalCropRect;
B _producesHighQualityInferencesFromZoomRegionWithLargeDigitalZoom;
@"NSMutableDictionary" _pixelTransferSessionByMediaKey;
@"NSMutableDictionary" _outputFormatDescriptionByAttachedMediaKey;
```

## Properties

```
@property (T@"NSArray",R,N) providedAttachedMediaKeys;
@property (TB,R,N) inferenceEnginePrepared;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWInferenceEngineController faceObservationsFromSbuf:];
+[BWInferenceEngineController inferenceMaskFromSbuf:attachedMediaKey:];
+[BWInferenceEngineController inferenceMaskSbufFromSbuf:attachedMediaKey:];
+[BWInferenceEngineController lowResPersonInstanceBoundingBoxesFromSbuf:];
+[BWInferenceEngineController lowResPersonInstanceConfidencesFromSbuf:];
+[BWInferenceEngineController lowResPersonInstanceMasksFromSbuf:];
+[BWInferenceEngineController skinToneClassificationsFromSbuf:];
+[BWInferenceEngineController smartCameraClassificationsFromSbuf:];
+[BWInferenceEngineController usesCustomProcessingFlow];
```

## Instance methods

```
-[BWInferenceEngineController _suppressedInferenceTypesForInput:];
-[BWInferenceEngineController _ensurePixelTransferSessionForAttachedMediaKey:];
-[BWInferenceEngineController outputFormatForAttachedMediaKey:];
-[BWInferenceEngineController intermediateResourceTrackingAllowedForAttachedMediaKey:];
-[BWInferenceEngineController inputVideoFormatForAttachedMediaKey:];
-[BWInferenceEngineController process];
-[BWInferenceEngineController dealloc];
-[BWInferenceEngineController _replaceAttachedSampleBuffer:attachedMediaKey:primarySampleBuffer:aspectRatio:];
-[BWInferenceEngineController reset];
-[BWInferenceEngineController providedAttachedMediaKeys];
-[BWInferenceEngineController _unzoomAndBlackenBordersOnAttachedMediaSampleBuffer:inputSbuf:attachedMediaKey:finalCropRect:];
-[BWInferenceEngineController inputInferenceVideoFormatForAttachedMediaKey:];
-[BWInferenceEngineController outputVideoFormatForAttachedMediaKey:];
-[BWInferenceEngineController inputReceivedNewData:];
-[BWInferenceEngineController inputFormatForAttachedMediaKey:];
-[BWInferenceEngineController prepareWithPixelBufferPoolProvider:];
-[BWInferenceEngineController reconfigure];
-[BWInferenceEngineController prepare];
-[BWInferenceEngineController prepareForReconfigurationWithInputDimensions:];
-[BWInferenceEngineController requestForInput:delegate:errOut:];
-[BWInferenceEngineController prepareForReconfigurationWithInputAspectRatio:];
-[BWInferenceEngineController _addTextureStylesPostProcessorWithInstanceMaskInferenceType:validBufferRectAppliedToVisionFaceLandmarks:finalCropRectAppliedToFaceAndInstanceSegmentationMasks:finalCropRectAppliedToPersonSemanticMasks:];
-[BWInferenceEngineController inferenceEnginePrepared];
-[BWInferenceEngineController initWithConfiguration:contextName:];
```
