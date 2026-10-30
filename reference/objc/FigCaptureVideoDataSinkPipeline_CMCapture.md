# `FigCaptureVideoDataSinkPipeline`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FigCaptureRemoteQueueSinkPipeline`
- 15 instance variables, 0 properties, 2 instance methods, 1 class methods

## Instance variables

```
@"BWFigVideoCaptureDevice" _captureDevice;
@"FigCaptureVISPipeline" _visPipeline;
@"BWPipelineStage" _visPipelineStage;
@"BWStreamingFilterNode" _filterNode;
@"BWPixelTransferNode" _videoDataConverterRotatorNode;
@"BWPixelTransferNode" _videoDataCopierNode;
@"BWSmartCropNode" _lowLatencyStabilizationNode;
@"BWNodeOutput" _faceTrackingVideoCaptureOutput;
@"BWNodeOutput" _offlineVISMotionDataCaptureOutput;
@"NSString" _sourceID;
i _sourceDeviceType;
B _optimizedForPreview;
@"BWBackgroundBlurNode" _backgroundBlurNode;
B _cinematicVideoMetadataCaptureEnabled;
B _countedAsStreamingVideoDataOutputConsumer;
```

## Class methods

```
+[FigCaptureVideoDataSinkPipeline initialize];
```

## Instance methods

```
-[FigCaptureVideoDataSinkPipeline dealloc];
-[FigCaptureVideoDataSinkPipeline setDiscardsSampleData:];
```
