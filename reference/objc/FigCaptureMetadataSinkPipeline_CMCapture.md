# `FigCaptureMetadataSinkPipeline`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FigCaptureRemoteQueueSinkPipeline`
- 14 instance variables, 0 properties, 1 instance methods, 1 class methods

## Instance variables

```
@"BWMetadataDetectorGatingNode" _metadataGatingNode;
@"BWMRCNode" _mrcNode;
B _mrcSuspended;
B _mrcConnectionDisabled;
@"BWSceneClassifierSinkNode" _sceneClassifierSinkNode;
@"BWNodeOutput" _sceneClassifierPipelineUpstreamOutput;
@"BWNodeOutput" _smartCameraInferenceOutput;
@"BWPreviewHistogramNode" _previewHistogramNode;
@"BWFaceTrackingNode" _faceTrackingNode;
@"BWFaceDetectionNode" _faceDetectionNode;
@"BWFocusSegmentationMaskConverterNode" _focusSegmentationMaskConverterNode;
@"NSString" _sourceID;
i _sourceDeviceType;
@"BWFunnelNode" _metadataFunnelNode;
```

## Class methods

```
+[FigCaptureMetadataSinkPipeline initialize];
```

## Instance methods

```
-[FigCaptureMetadataSinkPipeline dealloc];
```
