# `FigCapturePhotonicEngineSinkPipeline`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FigCaptureSinkPipeline`
- Protocols: `FigCaptureStillImageSinkPipeline`
- 13 instance variables, 11 properties, 12 instance methods, 2 class methods

## Instance variables

```
I _pipelineStagePriority;
I _inferencePriority;
@"BWStillImageCoordinatorNode" _stillImageCoordinatorNode;
@"BWCompressedShotBufferNode" _compressedShotBufferNode;
@"BWStillImageSampleBufferSinkNode" _stillImageSinkNode;
@"BWStillImageBravoDisparityNode" _stillImageDisparityNode;
@"BWDepthConverterNode" _stillImageDepthConverterNode;
@"BWPortraitHDRStagingNode" _portraitHDRStagingNode;
B _isPrimaryStillImagePipeline;
@"BWMultiCamClientCompositingNode" _multiCamClientCompositingNode;
@"BWNodeOutput" _outputForSecondaryStillImagePipeline;
@"<BWDynamicAspectRatioChangeSource>" _dynamicAspectRatioChangeSource;
@"<BWDynamicPipelineDimensionsChangeSource>" _dynamicPipelineDimensionChangeSource;
```

## Properties

```
@property (T{?=ii},R,N) activePipelineDimensions;
@property (T@"NSArray",R,N) nodes;
@property (T@"NSString",R,N) sinkID;
@property (T@"BWStillImageCoordinatorNode",R,N) stillImageCoordinatorNode;
@property (T@"BWCompressedShotBufferNode",R,N) compressedShotBufferNode;
@property (T@"BWStillImageSampleBufferSinkNode",R,N) stillImageSinkNode;
@property (T@"BWPortraitHDRStagingNode",R,N) portraitHDRStagingNode;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FigCapturePhotonicEngineSinkPipeline initialize];
+[FigCapturePhotonicEngineSinkPipeline pipelineBaseName];
```

## Instance methods

```
-[FigCapturePhotonicEngineSinkPipeline activePipelineDimensions];
-[FigCapturePhotonicEngineSinkPipeline dealloc];
-[FigCapturePhotonicEngineSinkPipeline compressedShotBufferNode];
-[FigCapturePhotonicEngineSinkPipeline connectToSecondaryMultiCameraClientCompositingPipeline:];
-[FigCapturePhotonicEngineSinkPipeline enablePrepareTimeAllocationsForDeferredPrepare];
-[FigCapturePhotonicEngineSinkPipeline initWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:isPrimaryStillImagePipeline:graph:name:];
-[FigCapturePhotonicEngineSinkPipeline liveReconfigureForAspectRatio:];
-[FigCapturePhotonicEngineSinkPipeline liveReconfigureForPipelineDimensions:];
-[FigCapturePhotonicEngineSinkPipeline liveReconfigureForSmartCropWarperFormatDimensions:];
-[FigCapturePhotonicEngineSinkPipeline portraitHDRStagingNode];
-[FigCapturePhotonicEngineSinkPipeline stillImageCoordinatorNode];
-[FigCapturePhotonicEngineSinkPipeline stillImageSinkNode];
```
