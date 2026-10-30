# `BWVideoDepthInferenceConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWInferenceConfiguration`
- 31 instance variables, 25 properties, 36 instance methods, 2 class methods

## Instance variables

```
i _videoDepthAlgorithm;
{?="width"i"height"i} _outputDimensions;
Q _concurrencyWidth;
I _temporalDepthInputPixelFormat;
@"<MTLEvent>" _backpressureEvent;
i _videoDepthLayout;
f _networkBias;
@"NSDictionary" _cameraInfoByPortType;
@"ADEspressoStereoV2InferenceDescriptor" _stereoV2inferenceDescriptor;
@"ADEspressoMonocularVideoInferenceDescriptor" _monocularVideoInferenceDescriptor;
@"ADMonocularVideoPipeline" _monocularVideoPipeline;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _monocularPipelineLock;
f _monocularDepthScaleFactor;
i _networkWidth;
i _networkHeight;
B _isFrontFacingCamera;
@"BWVideoFormat" _disparityMultiplierFormat;
@"NSString" _sensorIDString;
B _requiresAppleDepthPostProcessing;
B _requiresCroppingOfDepthBuffer;
B _usePrimaryPreviewSourceAttachedMediaForInference;
B _requiresVerticalFlipOfDepthBuffer;
B _sourceIsNuri;
B _colorInputRotationChangesWithAspectRatio;
I _outputPixelFormat;
I _featuresPixelFormat;
I _colorFeaturesPixelFormat;
{?="width"i"height"i} _inputDimensions;
@"NSString" _portType;
{?="width"i"height"i} _featuresDimensions;
{?="width"i"height"i} _colorFeaturesDimensions;
```

## Properties

```
@property (Ti,R,N,V_videoDepthAlgorithm) videoDepthAlgorithm;
@property (T{?=ii},R,N,V_outputDimensions) outputDimensions;
@property (TI,R,N,V_outputPixelFormat) outputPixelFormat;
@property (T{?=ii},R,N,V_inputDimensions) inputDimensions;
@property (T{?=ii},R,N,V_featuresDimensions) featuresDimensions;
@property (T@"NSString",R,N,V_portType) portType;
@property (TQ,R,N,V_concurrencyWidth) concurrencyWidth;
@property (TI,R,N,V_temporalDepthInputPixelFormat) temporalDepthInputPixelFormat;
@property (TI,R,N,V_featuresPixelFormat) featuresPixelFormat;
@property (T@"<MTLEvent>",R,N,V_backpressureEvent) backpressureEvent;
@property (Ti,R,N,V_videoDepthLayout) videoDepthLayout;
@property (TB,N,V_requiresAppleDepthPostProcessing) requiresAppleDepthPostProcessing;
@property (TB,R,N,V_requiresCroppingOfDepthBuffer) requiresCroppingOfDepthBuffer;
@property (TB,R,N,V_requiresVerticalFlipOfDepthBuffer) requiresVerticalFlipOfDepthBuffer;
@property (TB,N,V_sourceIsNuri) sourceIsNuri;
@property (Tf,R,N,V_networkBias) networkBias;
@property (TB,N,V_colorInputRotationChangesWithAspectRatio) colorInputRotationChangesWithAspectRatio;
@property (T@"NSDictionary",R,N,V_cameraInfoByPortType) cameraInfoByPortType;
@property (TB,N,V_usePrimaryPreviewSourceAttachedMediaForInference) usePrimaryPreviewSourceAttachedMediaForInference;
@property (T@"ADEspressoStereoV2InferenceDescriptor",R,N,V_stereoV2inferenceDescriptor) stereoV2inferenceDescriptor;
@property (T@"ADEspressoMonocularVideoInferenceDescriptor",R,N,V_monocularVideoInferenceDescriptor) monocularVideoInferenceDescriptor;
@property (T@"BWVideoFormat",R,N,V_disparityMultiplierFormat) disparityMultiplierFormat;
@property (T{?=ii},R,N,V_colorFeaturesDimensions) colorFeaturesDimensions;
@property (TI,R,N,V_colorFeaturesPixelFormat) colorFeaturesPixelFormat;
@property (T@"NSString",R,N,V_sensorIDString) sensorIDString;
```

## Class methods

```
+[BWVideoDepthInferenceConfiguration pceDisparityColorInferenceDescriptorForVideoDepthLayout:inputSource:];
+[BWVideoDepthInferenceConfiguration prewarmMonocularVideoPipelineForNetworkDimensions:height:isFrontFacingCamera:];
```

## Instance methods

```
-[BWVideoDepthInferenceConfiguration sensorIDString];
-[BWVideoDepthInferenceConfiguration setRequiresAppleDepthPostProcessing:];
-[BWVideoDepthInferenceConfiguration cameraInfoByPortType];
-[BWVideoDepthInferenceConfiguration portType];
-[BWVideoDepthInferenceConfiguration videoDepthLayout];
-[BWVideoDepthInferenceConfiguration getMonocularDepthScaleFactorForCinematic:];
-[BWVideoDepthInferenceConfiguration dealloc];
-[BWVideoDepthInferenceConfiguration setUsePrimaryPreviewSourceAttachedMediaForInference:];
-[BWVideoDepthInferenceConfiguration concurrencyWidth];
-[BWVideoDepthInferenceConfiguration temporalDepthInputPixelFormat];
-[BWVideoDepthInferenceConfiguration outputDimensions];
-[BWVideoDepthInferenceConfiguration inputDimensions];
-[BWVideoDepthInferenceConfiguration colorFeaturesDimensions];
-[BWVideoDepthInferenceConfiguration stereoV2inferenceDescriptor];
-[BWVideoDepthInferenceConfiguration monocularVideoInferenceDescriptor];
-[BWVideoDepthInferenceConfiguration setColorInputRotationChangesWithAspectRatio:];
-[BWVideoDepthInferenceConfiguration requiresVerticalFlipOfDepthBuffer];
-[BWVideoDepthInferenceConfiguration featuresDimensions];
-[BWVideoDepthInferenceConfiguration colorInputRotationChangesWithAspectRatio];
-[BWVideoDepthInferenceConfiguration initWithConcurrencyWidth:videoDepthLayout:networkInputDimensions:captureDevice:overrideOutputDimensions:backpressureEvent:];
-[BWVideoDepthInferenceConfiguration colorFeaturesPixelFormat];
-[BWVideoDepthInferenceConfiguration sourceIsNuri];
-[BWVideoDepthInferenceConfiguration disparityMultiplierFormat];
-[BWVideoDepthInferenceConfiguration videoDepthAlgorithm];
-[BWVideoDepthInferenceConfiguration loadMonocularVideoPipeline];
-[BWVideoDepthInferenceConfiguration requiresCroppingOfDepthBuffer];
-[BWVideoDepthInferenceConfiguration networkBias];
-[BWVideoDepthInferenceConfiguration initWithConcurrencyWidth:videoDepthLayout:networkInputDimensions:captureDevice:requiresCroppingOfDepthBuffer:requiresVerticalFlipOfDepthBuffer:backpressureEvent:];
-[BWVideoDepthInferenceConfiguration initWithConcurrencyWidth:videoDepthLayout:networkInputDimensions:captureDevice:backpressureEvent:];
-[BWVideoDepthInferenceConfiguration featuresPixelFormat];
-[BWVideoDepthInferenceConfiguration requiresAppleDepthPostProcessing];
-[BWVideoDepthInferenceConfiguration usePrimaryPreviewSourceAttachedMediaForInference];
-[BWVideoDepthInferenceConfiguration getMonocularDepthScaleFactor:inputImageIsRotated:inferenceCropRect:];
-[BWVideoDepthInferenceConfiguration backpressureEvent];
-[BWVideoDepthInferenceConfiguration outputPixelFormat];
-[BWVideoDepthInferenceConfiguration setSourceIsNuri:];
```
