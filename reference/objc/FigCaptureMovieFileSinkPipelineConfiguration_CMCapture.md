# `FigCaptureMovieFileSinkPipelineConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 46 instance variables, 0 properties, 1 instance methods, 0 class methods

## Instance variables

```
@"FigCaptureSourceConfiguration" _primaryCameraConfiguration;
@"FigVideoCaptureConnectionConfiguration" _primaryVideoConnectionConfiguration;
@"NSArray" _videoConnectionConfigurations;
@"FigAudioCaptureConnectionConfiguration" _audioConnectionConfiguration;
@"FigMetadataItemCaptureConnectionConfiguration" _cameraDebugInfoMetadataConnectionConfiguration;
@"NSArray" _detectedObjectMetadataConnectionConfigurations;
@"FigDepthDataCaptureConnectionConfiguration" _depthDataConnectionConfiguration;
{?="width"i"height"i} _depthOutputDimensions;
@"FigVideoCaptureConnectionConfiguration" _stillImageConnectionConfiguration;
@"FigVideoCaptureConnectionConfiguration" _sceneClassifierConnectionConfiguration;
{FigCaptureVideoTransform="mirrored"B"rotationDegrees"i"dimensions"{?="width"i"height"i}} _videoSourceCaptureTransform;
@"NSDictionary" _visConfigurationsByConnectionID;
B _boxedMetadataPostVISEnabled;
{?="major"S"minor"S"patch"S} _smartCameraPipelineVersion;
B _offlineVISEnabled;
@"NSArray" _portTypesWithGeometricDistortionCorrectionInVISEnabled;
B _vitalityScoringEnabled;
B _captureDeviceHasOverCaptureEnabled;
B _overCaptureEnabled;
B _frameReconstructionEnabled;
B _semanticStyleRenderingEnabled;
B _P3ToBT2020ConversionEnabled;
i _maxLossyCompressionLevel;
B _videoSTFEnabled;
B _videoGreenGhostMitigationEnabled;
B _ispFastSwitchEnabled;
B _trueVideoCaptureEnabled;
B _cinematicVideoMetadataEnabled;
B _cinematicAudioEnabled;
@"NSString" _clientApplicationID;
q _maximumAllowedInFlightCompressedBytes;
B _lightSourceMaskAndKeypointDescriptorDataEnabled;
{BWLensSmudgeDetectionConfiguration="lensSmudgeDetectionEnabled"B"lensSmudgeDetectionInterval"{?="value"q"timescale"i"flags"I"epoch"q}} _lensSmudgeDetectionConfiguration;
B _lowLatencyStabilizationEnabled;
B _proResRawCaptureEnabled;
B _lowLightVideoNoiseReductionEnabled;
B _personalPhotographerEnabled;
B _depthDataDeliveryEnabled;
B _lowResImageUsedByVideoEncoderEnabled;
B _smartStyleRenderingEnabled;
B _smartStyleReversibilityEnabled;
B _textureStyleEnabled;
B _videoGreenGhostOfflineMetadataEnabled;
B _videoGreenGhostOfflineLightSourceMaskEnabled;
f _personalPhotographerTypicalCaptureLatencyInSeconds;
i _smartStyleRenderingMethod;
```

## Instance methods

```
-[FigCaptureMovieFileSinkPipelineConfiguration dealloc];
```
