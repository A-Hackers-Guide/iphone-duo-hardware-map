# `FigCaptureVideoDataSinkPipelineConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 43 instance variables, 0 properties, 1 instance methods, 0 class methods

## Instance variables

```
{FigCaptureVideoTransform="mirrored"B"rotationDegrees"i"dimensions"{?="width"i"height"i}} _sourceVideoTransform;
B _sourceHasAppliedAllZoom;
i _videoStabilizationType;
i _motionAttachmentsSource;
B _faceTrackingEnabled;
B _offlineVISMotionDataEnabled;
@"NSArray" _portTypesWithGeometricDistortionCorrectionInVISEnabled;
B _P3ToBT2020ConversionEnabled;
i _sourceNodeColorSpaceProperties;
i _maxLossyCompressionLevel;
B _forcePixelTransfer;
B _videoSTFEnabled;
@"FigCaptureSourceConfiguration" _sourceConfiguration;
i _sourceDeviceType;
{?="width"i"height"i} _visOutputDimensions;
@"FigVideoCaptureConnectionConfiguration" _videoDataConnectionConfiguration;
{?="val"[8I]} _clientAuditToken;
B _previewStabilizationEnabled;
B _lowLatencyStabilizationEnabled;
B _pocketDetectionEnabled;
B _cinematicFramingSupported;
B _cinematicFramingEnabled;
i _centerStageFramingMode;
B _deskCamEnabled;
B _subjectSelectionEnabled;
B _gazeSelectionEnabled;
i _overheadCameraMode;
B _temporalFilterEnabled;
B _temporalFilterLowLightBandingMitigationEnabled;
@"NSDictionary" _temporalFilterConfigurationsByPortType;
B _cinematicVideoCaptureEnabled;
f _simulatedAperture;
@"NSString" _clientApplicationID;
B _cinematicVideoMetadataCaptureEnabled;
B _depthInferenceForCinematicVideoEnabled;
B _ringLightEnabled;
B _smartStyleRenderingEnabled;
B _manualCinematicFramingEnabled;
i _smartStyleRenderingMethod;
f _manualFramingZoomFactor;
f _manualFramingPanningAngleX;
f _manualFramingPanningAngleY;
{?="width"i"height"i} _visGeneratedTransformsOutputDimensionsOverride;
```

## Instance methods

```
-[FigCaptureVideoDataSinkPipelineConfiguration dealloc];
```
