# `BWUBNodeConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageNodeConfiguration`
- 46 instance variables, 0 properties, 1 instance methods, 0 class methods

## Instance variables

```
i _stillImageFusionScheme;
@"NSDictionary" _sensorConfigurationsByPortType;
@"NSArray" _sensorConfigurations;
@"BWSensorConfiguration" _jasperSensorConfiguration;
B _alwaysAllowModifyingInputBuffers;
B _inputIs10Bit;
i _retainedBufferCount;
i _outputBufferCount;
i _minimumOutputBufferCount;
i _maxNumberOfBurstCapturesAllowedInFlight;
B _outputPoolBackPressureEnabled;
@"<BWStillImageProcessingStatusDelegate>" _referenceFrameSelectionDelegate;
B _unifiedBracketingFusionSupportEnabled;
B _digitalFlashSupportEnabled;
B _deepFusionSyntheticsInNRSupportEnabled;
B _deepFusionWaitForPreprocessingToFinish;
B _deepFusionSupportEnabled;
i _maxDeepFusionOutputCount;
I _learnedNRMode;
i _deepZoomVersion;
f _gainMapMainImageDownscalingFactor;
f _inferenceMainImageDownscalingFactor;
@"NSDictionary" _providedInferenceAttachedMediaByMode;
B _redEyeReductionEnabled;
i _semanticRenderingVersion;
i _semanticDevelopmentVersion;
i _personSemanticsVersion;
B _semanticStyleRenderingEnabled;
{?="width"i"height"i} _outputDimensions;
@"NSArray" _portTypesWithGeometricDistortionCorrectionEnabled;
{?="width"i"height"i} _geometricDistortionCorrectionExpandedImageDimensions;
@"NSArray" _portTypesWithIntelligentDistortionCorrectionEnabled;
i _intelligentDistortionCorrectionVersion;
B _intelligentDistortionCorrectionAppliesFinalDimensions;
i _horizontalSensorBinningFactor;
i _verticalSensorBinningFactor;
i _greenGhostMitigationVersion;
B _depthDataDeliveryEnabled;
@"NSArray" _portTypesWithDepthSegmentationPortraitParameters;
{?="width"i"height"i} _disparityOutputDimensions;
B _shouldComputeDisparityWhenCalibrationFails;
B _demosaicedRawEnabled;
I _demosaicedRawPixelFormat;
@"NSDictionary" _rawColorCalibrationsByPortType;
@"NSDictionary" _rawLensShadingCorrectionCoefficientsByPortType;
B _generateLiDARDepth;
```

## Instance methods

```
-[BWUBNodeConfiguration dealloc];
```
