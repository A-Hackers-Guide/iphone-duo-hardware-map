# `FigCapturePreviewSinkPipelineConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 53 instance variables, 0 properties, 1 instance methods, 0 class methods

## Instance variables

```
@"NSString" _sinkID;
@"FigVideoCaptureConnectionConfiguration" _videoPreviewSinkConnectionConfiguration;
@"NSArray" _secondaryVideoPreviewSinkConnectionConfigurations;
@"FigVideoCaptureConnectionConfiguration" _videoThumbnailConnectionConfiguration;
@"FigDepthDataCaptureConnectionConfiguration" _depthDataConnectionConfiguration;
@"FigVideoCaptureConnectionConfiguration" _previewTimeMachineConnectionConfiguration;
@"FigVideoCaptureConnectionConfiguration" _sceneClassifierConnectionConfiguration;
@"FigVideoCaptureConnectionConfiguration" _sensitiveContentAnalyzerConnectionConfiguration;
@"FigMetadataObjectCaptureConnectionConfiguration" _metadataObjectConnectionConfiguration;
@"FigVideoCaptureConnectionConfiguration" _stillImageConnectionConfiguration;
{?="major"S"minor"S"patch"S} _sceneClassifierPipelineVersion;
i _sourceColorSpaceProperties;
B _sourcePixelFormatIsFullRange;
B _sourceIsBravoDevice;
B _clientIsCameraOrDerivative;
{?="val"[8I]} _clientAuditToken;
B _vitalityScoringEnabled;
B _remoteVideoPreview;
B _overCaptureEnabled;
B _singleCameraOverCaptureEnabled;
B _primaryCaptureRectModificationEnabled;
d _videoStabilizationOverscan;
B _trueVideoCaptureEnabled;
d _trueVideoCaptureAdditionalZoomFactor;
B _focusBlurMapForDepthFiltersEnabled;
B _smartCameraMotionDetectionEnabled;
B _generatesHistogram;
B _cinematicVideoEnabled;
B _depthInferenceForCinematicVideoEnabled;
B _cinematicVideoSDOFRenderingEnabled;
i _maxLossyCompressionLevel;
B _videoHDRImageStatisticsEnabled;
B _zoomPIPSingleStreamModeEnabled;
f _zoomPIPMinimumUIZoomFactor;
f _zoomPIPSlaveStreamingFrameRate;
B _preallocatePreviewStitcherOutputBufferPool;
B _previewStabilizationEnabled;
B _lowLatencyStabilizationEnabled;
B _pocketDetectionEnabled;
B _smartStyleRenderingEnabled;
B _smartStyleRenderedAttachmentEnabled;
B _parallelGraphRebuildEnabled;
B _ispFastSwitchEnabled;
B _rebuildingGraphForTrueVideoTransition;
B _sceneClassifierPipelineIsSharedWithLivePhotoVitalityScoring;
{BWLensSmudgeDetectionConfiguration="lensSmudgeDetectionEnabled"B"lensSmudgeDetectionInterval"{?="value"q"timescale"i"flags"I"epoch"q}} _lensSmudgeDetectionConfiguration;
@"NSString" _clientApplicationID;
B _personalPhotographerEnabled;
B _isSecondaryPreviewSink;
B _deferredPrepareEnabled;
B _coreMediaFaceTrackingEnabled;
i _smartStyleRenderingMethod;
@"FigVideoCaptureConnectionConfiguration" _previewSmartStyleCoefficientsTimeMachineConnectionConfiguration;
```

## Instance methods

```
-[FigCapturePreviewSinkPipelineConfiguration dealloc];
```
