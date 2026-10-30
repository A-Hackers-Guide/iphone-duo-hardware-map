# `FigCaptureCameraSourcePipelineConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 113 instance variables, 0 properties, 1 instance methods, 0 class methods

## Instance variables

```
i _motionAttachmentsSource;
@"NSArray" _videoStabilizationTypes;
B _actionCameraEnabled;
i _multiCamClientCompositingPrimaryCameraVideoStabilizationStrength;
i _depthType;
f _maxContinuousZoomFactorForDepthDataDelivery;
{?="width"i"height"i} _depthDimensionsOverride;
B _strictDepthModePreferred;
I _RGBIRStereoFusionMinDepthThresholdMM;
I _RGBIRStereoFusionMaxDepthThresholdMM;
I _RGBIRStereoFusionFixedDepthThresholdMM;
I _RGBIRStereoFusionFixedDepthValueMM;
B _RGBIRStereoFusionEnabled;
{?="value"q"timescale"i"flags"I"epoch"q} _maxExposureDurationClientOverride;
{?="value"q"timescale"i"flags"I"epoch"q} _maxExposureDurationFrameworkOverride;
B _forceCNRDisabled;
B _coreMediaFaceTrackingEnabled;
B _ispFaceTrackingEnabled;
B _stillImageGeometricDistortionCorrectionEnabled;
B _videoCaptureGeometricDistortionCorrectionEnabled;
B _previewGeometricDistortionCorrectionEnabled;
B _stillImageGeometricDistortionCorrectionExpansionCoversOverscan;
B _stillImageLocalHistogramClippingDataMetadataEnabled;
B _offlineVISEnabled;
B _zeroShutterLagEnabled;
B _configureForZeroShutterLagSupport;
B _configureForSIFRStillImageCaptureIfAvailable;
B _softISPEnabled;
B _sensorRawStillImageOutputsEnabledIfAvailable;
B _sensorRawOutputsEnabled;
B _enableStillImageSensorOverscanIfAvailable;
f _overCapturePercentage;
B _configureForSpatialOverCaptureSupport;
B _configureForDigitalFlashSupport;
B _configureForSoftISPSupport;
B _configureForDepthDataDeliverySupport;
B _configureForStereoPhotoCaptureSupport;
B _clockSynchronizationEnabled;
B _depthConversionEnabled;
B _midFrameSynchronizationEnabled;
i _stillImageFocusPixelDataRetainedBufferCount;
i _stillImageSashimiRawRetainedBufferCount;
i _stillImageSensorInterfaceRawRetainedBufferCount;
i _stillImageOutputRetainedBufferCountOverride;
B _stillImageOutputSushiRawAttachmentOptionEnabled;
B _streamingForegroundSegmentationEnabled;
B _streamingCameraCalibrationDataDeliveryEnabled;
i _autoImageControlMode;
@"FigCaptureSourceConfiguration" _cameraConfiguration;
@"NSArray" _connectionConfigurations;
@"FigVideoCaptureConnectionConfiguration" _videoPreviewSinkConnectionConfiguration;
@"NSArray" _previewDerivedConnectionConfigurations;
@"NSArray" _videoCaptureConnectionConfigurations;
@"FigVideoCaptureConnectionConfiguration" _stillImageConnectionConfiguration;
@"FigDepthDataCaptureConnectionConfiguration" _depthDataConnectionConfiguration;
@"NSArray" _visionDataConnectionConfigurations;
@"NSArray" _metadataObjectConnectionConfigurations;
@"NSArray" _movieFileDetectedObjectMetadataConnectionConfigurations;
@"NSArray" _pointCloudDataConnectionConfigurations;
@"NSArray" _secureVideoConnectionConfigurations;
B _clientIsCameraOrDerivative;
B _deferredTimeOfFlightNodePrepareEnabled;
B _videoHDRImageStatisticsEnabled;
f _additionalVISOverscanWhenRecording;
B _videoSTFMetadataEnabled;
i _previewMaxLossyCompressionLevel;
i _videoDataMaxLossyCompressionLevel;
i _movieFileMaxLossyCompressionLevel;
i _stillImageMaxLossyCompressionLevel;
B _depthOutputEnabled;
B _lumaHistogramsEnabled;
B _continuityCameraIsWired;
i _continuityCameraClientDeviceClass;
B _clientIsVOIP;
B _zoomPIPSingleStreamModeEnabled;
f _zoomPIPMinimumUIZoomFactor;
f _zoomPIPSlaveStreamingFrameRate;
@"NSString" _preferredMasterPortType;
i _timewarpMode;
B _smartStyleLearningEnabled;
B _smartStyleReversibilityEnabled;
B _smartStyleHardwareApplyEnabled;
@"FigCaptureSmartStyle" _smartStyle;
@"FigCaptureTextureStyle" _textureStyle;
B _rebuildingGraphForTrueVideoTransition;
f _trueVideoTransitionPreviousPhotoGraphZoomFactor;
i _targetFrameRateWhenNotRecording;
B _preLTMThumbnailEnabled;
B _postLTMThumbnailEnabled;
B _postColorProcessingThumbnailEnabled;
B _weightSegmentMapEnabled;
B _smartFramingEnabled;
B _lowLatencyStabilizationEnabledInSourcePipeline;
B _clientIsAttachedInfraredMetadataSession;
B _lowLightVideoNoiseReductionEnabled;
B _cinematicVideoCaptureEnabled;
B _stereoVideoCaptureEnabled;
B _clientSetsUserInitiatedCaptureRequestTime;
B _graphContainsMultipleVideoSources;
B _structuredLightAFAssistEnabled;
B _textureStyleEnabled;
B _temporalNoiseReductionStrengthHighEnabled;
B _audioMixWithOthersEnabled;
B _previewStabilizationEnabled;
B _cinematicVideoMetadataDeliveryEnabled;
B _visualIntelligenceCameraEnabled;
I _weightSegmentMapNumberOfSegments;
I _weightSegmentMapSmoothingSigma;
i _textureStyleRenderingVersion;
{?="width"i"height"i} _styleEngineCoefficientsDimensions;
{?="width"i"height"i} _ltmThumbnailOutputDimensions;
{?="width"i"height"i} _weightSegmentMapOutputDimensions;
{?="width"i"height"i} _captureDimensionsForFSDNetSecondary;
```

## Instance methods

```
-[FigCaptureCameraSourcePipelineConfiguration dealloc];
```
