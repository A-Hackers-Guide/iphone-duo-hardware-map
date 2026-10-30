# `FigCaptureBaseStillImageSinkPipelineConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 22 instance variables, 22 properties, 48 instance methods, 1 class methods

## Instance variables

```
B _allowsMultipleInflightCaptures;
B _clientIsCameraOrDerivative;
B _allowedToModifyInputBuffers;
B _inputIs10Bit;
i _horizontalSensorBinningFactor;
i _verticalSensorBinningFactor;
f _maxSupportedFrameRate;
i _motionAttachmentsSource;
i depthDataToRGBRotationAngle;
@"FigCaptureSinkConfiguration" _sinkConfiguration;
B _usesHighEncodingPriority;
I _outputPixelFormat;
i _outputColorSpaceProperties;
B _stillImageStabilizationSupported;
i _noiseReductionAndFusionScheme;
{?="width"i"height"i} _depthDataSourceDimensions;
{?="width"i"height"i} _depthDataTargetDimensions;
{?="width"i"height"i} _depthDataStillNetworkDimensions;
f _portraitEffectsMatteMainImageDownscalingFactor;
B _cinematicFramingWarpingRequired;
{?="width"i"height"i} _cinematicFramingWarpingOutputDimensions;
i _depthDataToRGBRotationAngle;
```

## Properties

```
@property (TB,N,V_allowsMultipleInflightCaptures) allowsMultipleInflightCaptures;
@property (TB,N,V_clientIsCameraOrDerivative) clientIsCameraOrDerivative;
@property (TB,N,V_allowedToModifyInputBuffers) allowedToModifyInputBuffers;
@property (TB,N,V_inputIs10Bit) inputIs10Bit;
@property (Ti,N,V_horizontalSensorBinningFactor) horizontalSensorBinningFactor;
@property (Ti,N,V_verticalSensorBinningFactor) verticalSensorBinningFactor;
@property (Tf,N,V_maxSupportedFrameRate) maxSupportedFrameRate;
@property (T{?=ii},N,V_depthDataSourceDimensions) depthDataSourceDimensions;
@property (Ti,N,V_motionAttachmentsSource) motionAttachmentsSource;
@property (Ti,N,V_depthDataToRGBRotationAngle) depthDataToRGBRotationAngle;
@property (T@"FigCaptureSinkConfiguration",&,N,V_sinkConfiguration) sinkConfiguration;
@property (T@"FigCaptureIrisSinkConfiguration",R,N) irisSinkConfiguration;
@property (TB,N,V_usesHighEncodingPriority) usesHighEncodingPriority;
@property (TI,N,V_outputPixelFormat) outputPixelFormat;
@property (Ti,N,V_outputColorSpaceProperties) outputColorSpaceProperties;
@property (TB,N,V_stillImageStabilizationSupported) stillImageStabilizationSupported;
@property (Ti,N,V_noiseReductionAndFusionScheme) noiseReductionAndFusionScheme;
@property (T{?=ii},N,V_depthDataTargetDimensions) depthDataTargetDimensions;
@property (T{?=ii},N,V_depthDataStillNetworkDimensions) depthDataStillNetworkDimensions;
@property (Tf,N,V_portraitEffectsMatteMainImageDownscalingFactor) portraitEffectsMatteMainImageDownscalingFactor;
@property (TB,N,V_cinematicFramingWarpingRequired) cinematicFramingWarpingRequired;
@property (T{?=ii},N,V_cinematicFramingWarpingOutputDimensions) cinematicFramingWarpingOutputDimensions;
```

## Class methods

```
+[FigCaptureBaseStillImageSinkPipelineConfiguration supportsSecureCoding];
```

## Instance methods

```
-[FigCaptureBaseStillImageSinkPipelineConfiguration verticalSensorBinningFactor];
-[FigCaptureBaseStillImageSinkPipelineConfiguration setHorizontalSensorBinningFactor:];
-[FigCaptureBaseStillImageSinkPipelineConfiguration usesHighEncodingPriority];
-[FigCaptureBaseStillImageSinkPipelineConfiguration horizontalSensorBinningFactor];
-[FigCaptureBaseStillImageSinkPipelineConfiguration setVerticalSensorBinningFactor:];
-[FigCaptureBaseStillImageSinkPipelineConfiguration setDepthDataToRGBRotationAngle:];
-[FigCaptureBaseStillImageSinkPipelineConfiguration depthDataToRGBRotationAngle];
-[FigCaptureBaseStillImageSinkPipelineConfiguration motionAttachmentsSource];
-[FigCaptureBaseStillImageSinkPipelineConfiguration setOutputColorSpaceProperties:];
-[FigCaptureBaseStillImageSinkPipelineConfiguration noiseReductionAndFusionScheme];
-[FigCaptureBaseStillImageSinkPipelineConfiguration clientIsCameraOrDerivative];
-[FigCaptureBaseStillImageSinkPipelineConfiguration setClientIsCameraOrDerivative:];
-[FigCaptureBaseStillImageSinkPipelineConfiguration setCinematicFramingWarpingRequired:];
-[FigCaptureBaseStillImageSinkPipelineConfiguration dealloc];
-[FigCaptureBaseStillImageSinkPipelineConfiguration setNoiseReductionAndFusionScheme:];
-[FigCaptureBaseStillImageSinkPipelineConfiguration setMotionAttachmentsSource:];
-[FigCaptureBaseStillImageSinkPipelineConfiguration setUsesHighEncodingPriority:];
-[FigCaptureBaseStillImageSinkPipelineConfiguration setOutputPixelFormat:];
-[FigCaptureBaseStillImageSinkPipelineConfiguration portraitEffectsMatteMainImageDownscalingFactor];
-[FigCaptureBaseStillImageSinkPipelineConfiguration encodeWithCoder:];
-[FigCaptureBaseStillImageSinkPipelineConfiguration cinematicFramingWarpingRequired];
-[FigCaptureBaseStillImageSinkPipelineConfiguration hash];
-[FigCaptureBaseStillImageSinkPipelineConfiguration stillImageStabilizationSupported];
-[FigCaptureBaseStillImageSinkPipelineConfiguration initWithCoder:];
-[FigCaptureBaseStillImageSinkPipelineConfiguration outputColorSpaceProperties];
-[FigCaptureBaseStillImageSinkPipelineConfiguration isEqual:];
-[FigCaptureBaseStillImageSinkPipelineConfiguration outputPixelFormat];
-[FigCaptureBaseStillImageSinkPipelineConfiguration maxSupportedFrameRate];
-[FigCaptureBaseStillImageSinkPipelineConfiguration setSinkConfiguration:];
-[FigCaptureBaseStillImageSinkPipelineConfiguration sinkConfiguration];
-[FigCaptureBaseStillImageSinkPipelineConfiguration depthDataStillNetworkDimensions];
-[FigCaptureBaseStillImageSinkPipelineConfiguration setAllowedToModifyInputBuffers:];
-[FigCaptureBaseStillImageSinkPipelineConfiguration allowedToModifyInputBuffers];
-[FigCaptureBaseStillImageSinkPipelineConfiguration allowsMultipleInflightCaptures];
-[FigCaptureBaseStillImageSinkPipelineConfiguration cinematicFramingWarpingOutputDimensions];
-[FigCaptureBaseStillImageSinkPipelineConfiguration depthDataSourceDimensions];
-[FigCaptureBaseStillImageSinkPipelineConfiguration depthDataTargetDimensions];
-[FigCaptureBaseStillImageSinkPipelineConfiguration inputIs10Bit];
-[FigCaptureBaseStillImageSinkPipelineConfiguration irisSinkConfiguration];
-[FigCaptureBaseStillImageSinkPipelineConfiguration setAllowsMultipleInflightCaptures:];
-[FigCaptureBaseStillImageSinkPipelineConfiguration setCinematicFramingWarpingOutputDimensions:];
-[FigCaptureBaseStillImageSinkPipelineConfiguration setDepthDataSourceDimensions:];
-[FigCaptureBaseStillImageSinkPipelineConfiguration setDepthDataStillNetworkDimensions:];
-[FigCaptureBaseStillImageSinkPipelineConfiguration setDepthDataTargetDimensions:];
-[FigCaptureBaseStillImageSinkPipelineConfiguration setInputIs10Bit:];
-[FigCaptureBaseStillImageSinkPipelineConfiguration setMaxSupportedFrameRate:];
-[FigCaptureBaseStillImageSinkPipelineConfiguration setPortraitEffectsMatteMainImageDownscalingFactor:];
-[FigCaptureBaseStillImageSinkPipelineConfiguration setStillImageStabilizationSupported:];
```
