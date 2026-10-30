# `FigCapturePreviewSinkPipeline`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FigCaptureSinkPipeline`
- 46 instance variables, 32 properties, 61 instance methods, 1 class methods

## Instance variables

```
@"BWPixelTransferNode" _scalerNode;
@"BWImageQueueSinkNode" _imageQueueSinkNode;
@"BWSceneClassifierSinkNode" _sceneClassifierSinkNode;
@"BWStreamingFilterNode" _filterNode;
@"BWPreviewTimeMachineSinkNode" _timeMachineSinkNode;
@"BWVideoPIPOverlayNode" _zoomPIPOverlayNode;
@"BWAssistiveOverlayNode" _assistiveOverlayNode;
@"BWNodeOutput" _sceneClassifierPipelineUpstreamOutput;
@"BWInferenceNode" _personSegmentationAndDepthNode;
@"BWInferenceNode" _semanticStylePersonSegmentationNode;
@"BWInferenceNode" _portraitOnlyPersonSegmentationNode;
@"BWPreviewStabilizationNode" _previewStabilizationNode;
@"BWPocketDetectionNode" _pocketDetectionNode;
@"BWFaceTrackingNode" _faceTrackingNode;
@"BWPreviewStitcherNode" _previewStitcher;
@"BWOverCaptureSmartStyleApplyNode" _smartStylePreviewApplyNode;
@"BWSmartCropNode" _lowLatencyStabilizationNode;
@"<BWPersonalPhotographerDelegate>" _personalPhotographerDelegate;
@"BWNodeOutput" _sensitiveContentAnalyzerSinkOutput;
@"BWNodeOutput" _metadataSinkOutput;
@"BWNodeOutput" _videoThumbnailSinkOutput;
@"BWNodeOutput" _depthDataSinkOutput;
@"BWNodeOutput" _secondaryPreviewSinkOutput;
@"NSDictionary" _imageQueueUpdatedPayloadToBeSentAfterCommitConfiguration;
{FigCaptureVideoTransform="mirrored"B"rotationDegrees"i"dimensions"{?="width"i"height"i}} _outputTransform;
{FigCaptureVideoTransform="mirrored"B"rotationDegrees"i"dimensions"{?="width"i"height"i}} _videoThumbnailSinkOutputTransform;
@"NSString" _sourceID;
i _sourceDeviceType;
B _cinematicVideoEnabled;
B _overCaptureEnabled;
B _singleCameraOverCaptureEnabled;
d _videoStabilizationOverscan;
d _trueVideoTransitionPercentComplete;
q _primaryCaptureRectUniqueID;
B _applyPreviewShiftToMomentCapture;
B _isSecondaryPreviewSinkPipeline;
B _filterNodeIsPostStitcher;
B _smartStyleRenderingEnabled;
@"BWVideoDepthNode" _videoDepthNode;
@"BWInferenceNode" _opticalFlowInferenceNode;
{?="width"i"height"i} _rotatedSourceDimensions;
i _previewRotationDegrees;
i _omahaAdditionalPreviewRotationDegrees;
@"NSObject<OS_dispatch_queue>" _metalCompletionQueue;
@"NSObject<OS_dispatch_queue>" _metalSubmissionQueue;
B _depthFilterRenderingEnabled;
```

## Properties

```
@property (T@"<BWMRCSceneObserver>",N) mrcSceneObserver;
@property (T@"<BWSemanticStyleSceneObserver>",N) semanticStyleSceneObserver;
@property (T@"NSString",R,N,V_sourceID) sourceID;
@property (Ti,R,N,V_sourceDeviceType) sourceDeviceType;
@property (T@"BWImageQueueSinkNode",R,N,V_imageQueueSinkNode) imageQueueSinkNode;
@property (T@"BWPreviewStitcherNode",R,N,V_previewStitcher) previewStitcherNode;
@property (T@"BWPreviewStabilizationNode",R,N,V_previewStabilizationNode) previewStabilizationNode;
@property (T@"BWStreamingFilterNode",R,N,V_filterNode) filterNode;
@property (T@"BWPixelTransferNode",R,N,V_scalerNode) scalerNode;
@property (T@"BWPreviewTimeMachineSinkNode",R,N,V_timeMachineSinkNode) timeMachineSinkNode;
@property (T@"<BWPersonalPhotographerDelegate>",R,N,V_personalPhotographerDelegate) personalPhotographerDelegate;
@property (T@"BWNodeOutput",R,N,V_sensitiveContentAnalyzerSinkOutput) sensitiveContentAnalyzerSinkOutput;
@property (T@"BWNodeOutput",R,N,V_metadataSinkOutput) metadataSinkOutput;
@property (T@"BWNodeOutput",R,N,V_videoThumbnailSinkOutput) videoThumbnailSinkOutput;
@property (T@"BWNodeOutput",R,N,V_depthDataSinkOutput) depthDataSinkOutput;
@property (T@"BWNodeOutput",R,N,V_secondaryPreviewSinkOutput) secondaryPreviewSinkOutput;
@property (TB,R,N,V_isSecondaryPreviewSinkPipeline) isSecondaryPreviewSinkPipeline;
@property (T@"NSDictionary",R,N,V_imageQueueUpdatedPayloadToBeSentAfterCommitConfiguration) imageQueueUpdatedPayloadToBeSentAfterCommitConfiguration;
@property (TB,R,N,V_depthFilterRenderingEnabled) depthFilterRenderingEnabled;
@property (T{FigCaptureVideoTransform=Bi{?=ii}},R,N,V_outputTransform) outputTransform;
@property (T{FigCaptureVideoTransform=Bi{?=ii}},R,N,V_videoThumbnailSinkOutputTransform) videoThumbnailSinkOutputTransform;
@property (TB,N) discardsImageQueueSampleData;
@property (TB,N) sceneClassifierSuspended;
@property (T@"NSArray",&,N) filters;
@property (Tf,N) simulatedAperture;
@property (Tf,N) portraitLightingEffectStrength;
@property (T@"FigCaptureSemanticStyle",&,N) semanticStyle;
@property (Td,R) primaryCaptureRectAspectRatio;
@property (T{CGPoint=dd},R) primaryCaptureRectCenter;
@property (Tq,R) primaryCaptureRectUniqueID;
@property (TB) displaysWidestCameraOnly;
@property (Ti,N,V_previewRotationDegrees) previewRotationDegrees;
```

## Class methods

```
+[FigCapturePreviewSinkPipeline initialize];
```

## Instance methods

```
-[FigCapturePreviewSinkPipeline updateClientAuditToken:];
-[FigCapturePreviewSinkPipeline setSceneClassifierSuspended:];
-[FigCapturePreviewSinkPipeline sceneClassifierSuspended];
-[FigCapturePreviewSinkPipeline semanticStyleSceneObserver];
-[FigCapturePreviewSinkPipeline primaryCaptureRectUniqueID];
-[FigCapturePreviewSinkPipeline primaryCaptureRectCenter];
-[FigCapturePreviewSinkPipeline setSemanticStyle:];
-[FigCapturePreviewSinkPipeline primaryCaptureRectAspectRatio];
-[FigCapturePreviewSinkPipeline portraitLightingEffectStrength];
-[FigCapturePreviewSinkPipeline setPreviewRotationDegrees:];
-[FigCapturePreviewSinkPipeline dealloc];
-[FigCapturePreviewSinkPipeline prepareForRenderingWithPreparedPixelBufferPool];
-[FigCapturePreviewSinkPipeline setFilters:];
-[FigCapturePreviewSinkPipeline setFocusPeakingOverlayState:];
-[FigCapturePreviewSinkPipeline filters];
-[FigCapturePreviewSinkPipeline setSimulatedAperture:];
-[FigCapturePreviewSinkPipeline setSemanticStyleSet:fencePortSendRight:];
-[FigCapturePreviewSinkPipeline sourceID];
-[FigCapturePreviewSinkPipeline sourceDeviceType];
-[FigCapturePreviewSinkPipeline setSubstrateState:];
-[FigCapturePreviewSinkPipeline semanticStyle];
-[FigCapturePreviewSinkPipeline setSemanticStyle:animated:];
-[FigCapturePreviewSinkPipeline setSemanticStyleSceneObserver:];
-[FigCapturePreviewSinkPipeline previewRotationDegrees];
-[FigCapturePreviewSinkPipeline mrcSceneObserver];
-[FigCapturePreviewSinkPipeline setPortraitLightingEffectStrength:];
-[FigCapturePreviewSinkPipeline simulatedAperture];
-[FigCapturePreviewSinkPipeline setPreviewTapRegistered:];
-[FigCapturePreviewSinkPipeline setExposureClippingOverlayState:];
-[FigCapturePreviewSinkPipeline setSemanticStyleRenderingSuspended:animated:];
-[FigCapturePreviewSinkPipeline setMrcSceneObserver:];
-[FigCapturePreviewSinkPipeline setDisplaysWidestCameraOnly:];
-[FigCapturePreviewSinkPipeline displaysWidestCameraOnly];
-[FigCapturePreviewSinkPipeline personalPhotographerDelegate];
-[FigCapturePreviewSinkPipeline scalerNode];
-[FigCapturePreviewSinkPipeline outputTransform];
-[FigCapturePreviewSinkPipeline depthDataSinkOutput];
-[FigCapturePreviewSinkPipeline depthFilterRenderingEnabled];
-[FigCapturePreviewSinkPipeline discardsImageQueueSampleData];
-[FigCapturePreviewSinkPipeline filterNode];
-[FigCapturePreviewSinkPipeline imageQueueSinkNode];
-[FigCapturePreviewSinkPipeline imageQueueUpdatedPayloadToBeSentAfterCommitConfiguration];
-[FigCapturePreviewSinkPipeline initForSecondaryPreviewSinkWithConfiguration:upstreamPreviewOutput:upstreamTransform:sourcingFromPreviewStitcher:imageQueueSinkNode:graph:name:captureDevice:previewTapDelegate:];
-[FigCapturePreviewSinkPipeline initWithConfiguration:sourcePreviewOutput:sourceSensorRawPreviewOutput:sourceHueMapPreviewOutput:imageQueueSinkNode:graph:name:inferenceScheduler:captureDevice:previewTapDelegate:zoomPIPOverlayDelegate:personalPhotographerCaptureDelegate:sourceStillImageOutputsByPortType:];
-[FigCapturePreviewSinkPipeline isSecondaryPreviewSinkPipeline];
-[FigCapturePreviewSinkPipeline liveReconfigureForOutputDimensions:];
-[FigCapturePreviewSinkPipeline liveReconfigureForRotationDegrees:cameraExtrinsicMatrix:];
-[FigCapturePreviewSinkPipeline loadInferenceNetworksForHVS];
-[FigCapturePreviewSinkPipeline metadataSinkOutput];
-[FigCapturePreviewSinkPipeline previewStabilizationNode];
-[FigCapturePreviewSinkPipeline previewStitcherNode];
-[FigCapturePreviewSinkPipeline secondaryPreviewSinkOutput];
-[FigCapturePreviewSinkPipeline sensitiveContentAnalyzerSinkOutput];
-[FigCapturePreviewSinkPipeline setDiscardsImageQueueSampleData:];
-[FigCapturePreviewSinkPipeline setPrimaryCaptureRectAspectRatio:center:trueVideoTransitionPercentComplete:smartFramingTransitionPercentComplete:smartFramingTransitionTargetFieldOfView:fencePortSendRight:uniqueID:];
-[FigCapturePreviewSinkPipeline setStoppingForClientBackgrounded:];
-[FigCapturePreviewSinkPipeline setStoppingForModeSwitch:parallelGraphRebuildEnabled:ispFastSwitchEnabled:smartStyleRenderingEnabledInTrueVideoGraph:];
-[FigCapturePreviewSinkPipeline setVideoStabilizationOverscanCropEnabled:momentMovieRecordingEnabled:];
-[FigCapturePreviewSinkPipeline timeMachineSinkNode];
-[FigCapturePreviewSinkPipeline videoThumbnailSinkOutput];
-[FigCapturePreviewSinkPipeline videoThumbnailSinkOutputTransform];
```
