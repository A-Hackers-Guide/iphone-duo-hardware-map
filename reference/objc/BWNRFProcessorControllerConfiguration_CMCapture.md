# `BWNRFProcessorControllerConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorControllerConfiguration`
- 30 instance variables, 30 properties, 61 instance methods, 0 class methods

## Instance variables

```
@"BWVideoFormat" _inputFormat;
@"BWVideoFormat" _outputFormat;
@"NSDictionary" _dimensionsByResolutionFlavor;
@"NSDictionary" _dimensionsByResolutionFlavorByPortType;
B _cmiResourceEnabled;
B _quadraSupportEnabled;
B _unifiedBracketingFusionEnabled;
B _lowLightFusionEnabled;
i _semanticRenderingVersion;
B _rawNightModeEnabled;
@"BWVideoFormat" _rawNightModeInputFormat;
B _deepFusionEnabled;
@"BWVideoFormat" _deepFusionInputFormat;
B _deepFusionWaitForProcessingToFinish;
I _learnedFusionMode;
@"BWVideoFormat" _learnedFusionInputFormat;
B _adaptiveFusionEnabled;
@"BWVideoFormat" _adaptiveFusionInputFormat;
B _swfrEnabled;
B _learnedNRUsingNRFEnabled;
I _learnedNRMode;
@"BWVideoFormat" _learnedNRInputFormat;
B _depthDataDeliveryEnabled;
B _alwaysAllowModifyingInputBuffers;
I _figThreadPriority;
i _greenGhostMitigationVersion;
B _demosaicedRawEnabled;
I _demosaicedRawPixelFormat;
@"NSDictionary" _rawColorCalibrationsByPortType;
f _gainMapMainImageDownscalingFactor;
```

## Properties

```
@property (T@"BWVideoFormat",&,N,V_inputFormat) inputFormat;
@property (T@"BWVideoFormat",&,N,V_outputFormat) outputFormat;
@property (TB,N,V_quadraSupportEnabled) quadraSupportEnabled;
@property (TB,N,V_unifiedBracketingFusionEnabled) unifiedBracketingFusionEnabled;
@property (TB,N,V_lowLightFusionEnabled) lowLightFusionEnabled;
@property (TB,N,V_deepFusionEnabled) deepFusionEnabled;
@property (T@"BWVideoFormat",&,N,V_deepFusionInputFormat) deepFusionInputFormat;
@property (TB,N,V_deepFusionWaitForProcessingToFinish) deepFusionWaitForProcessingToFinish;
@property (TB,N,V_depthDataDeliveryEnabled) depthDataDeliveryEnabled;
@property (TB,N,V_alwaysAllowModifyingInputBuffers) alwaysAllowModifyingInputBuffers;
@property (TI,N,V_figThreadPriority) figThreadPriority;
@property (Ti,N,V_greenGhostMitigationVersion) greenGhostMitigationVersion;
@property (TB,N,V_demosaicedRawEnabled) demosaicedRawEnabled;
@property (TI,N,V_demosaicedRawPixelFormat) demosaicedRawPixelFormat;
@property (T@"NSDictionary",&,N,V_rawColorCalibrationsByPortType) rawColorCalibrationsByPortType;
@property (Tf,N,V_gainMapMainImageDownscalingFactor) gainMapMainImageDownscalingFactor;
@property (Ti,N,V_semanticRenderingVersion) semanticRenderingVersion;
@property (TB,N,V_swfrEnabled) swfrEnabled;
@property (TB,N,V_learnedNRUsingNRFEnabled) learnedNRUsingNRFEnabled;
@property (TI,N,V_learnedNRMode) learnedNRMode;
@property (T@"BWVideoFormat",&,N,V_learnedNRInputFormat) learnedNRInputFormat;
@property (TB,N,V_rawNightModeEnabled) rawNightModeEnabled;
@property (T@"BWVideoFormat",&,N,V_rawNightModeInputFormat) rawNightModeInputFormat;
@property (TI,N,V_learnedFusionMode) learnedFusionMode;
@property (T@"BWVideoFormat",&,N,V_learnedFusionInputFormat) learnedFusionInputFormat;
@property (TB,N,V_adaptiveFusionEnabled) adaptiveFusionEnabled;
@property (T@"BWVideoFormat",&,N,V_adaptiveFusionInputFormat) adaptiveFusionInputFormat;
@property (TB,N,V_cmiResourceEnabled) cmiResourceEnabled;
@property (T@"NSDictionary",&,N,V_dimensionsByResolutionFlavor) dimensionsByResolutionFlavor;
@property (T@"NSDictionary",&,N,V_dimensionsByResolutionFlavorByPortType) dimensionsByResolutionFlavorByPortType;
```

## Instance methods

```
-[BWNRFProcessorControllerConfiguration demosaicedRawPixelFormat];
-[BWNRFProcessorControllerConfiguration deepFusionEnabled];
-[BWNRFProcessorControllerConfiguration setLearnedNRMode:];
-[BWNRFProcessorControllerConfiguration setGreenGhostMitigationVersion:];
-[BWNRFProcessorControllerConfiguration gainMapMainImageDownscalingFactor];
-[BWNRFProcessorControllerConfiguration setDimensionsByResolutionFlavorByPortType:];
-[BWNRFProcessorControllerConfiguration setDemosaicedRawPixelFormat:];
-[BWNRFProcessorControllerConfiguration setGainMapMainImageDownscalingFactor:];
-[BWNRFProcessorControllerConfiguration learnedNRMode];
-[BWNRFProcessorControllerConfiguration greenGhostMitigationVersion];
-[BWNRFProcessorControllerConfiguration swfrEnabled];
-[BWNRFProcessorControllerConfiguration setRawNightModeEnabled:];
-[BWNRFProcessorControllerConfiguration setCmiResourceEnabled:];
-[BWNRFProcessorControllerConfiguration setRawColorCalibrationsByPortType:];
-[BWNRFProcessorControllerConfiguration setDeepFusionEnabled:];
-[BWNRFProcessorControllerConfiguration setDemosaicedRawEnabled:];
-[BWNRFProcessorControllerConfiguration semanticRenderingVersion];
-[BWNRFProcessorControllerConfiguration setFigThreadPriority:];
-[BWNRFProcessorControllerConfiguration setDeepFusionWaitForProcessingToFinish:];
-[BWNRFProcessorControllerConfiguration setSemanticRenderingVersion:];
-[BWNRFProcessorControllerConfiguration rawColorCalibrationsByPortType];
-[BWNRFProcessorControllerConfiguration setOutputFormat:];
-[BWNRFProcessorControllerConfiguration unifiedBracketingFusionEnabled];
-[BWNRFProcessorControllerConfiguration dimensionsByResolutionFlavorByPortType];
-[BWNRFProcessorControllerConfiguration lowLightFusionEnabled];
-[BWNRFProcessorControllerConfiguration adaptiveFusionInputFormat];
-[BWNRFProcessorControllerConfiguration setRawNightModeInputFormat:];
-[BWNRFProcessorControllerConfiguration inputFormat];
-[BWNRFProcessorControllerConfiguration dealloc];
-[BWNRFProcessorControllerConfiguration learnedFusionMode];
-[BWNRFProcessorControllerConfiguration setSwfrEnabled:];
-[BWNRFProcessorControllerConfiguration demosaicedRawEnabled];
-[BWNRFProcessorControllerConfiguration rawNightModeEnabled];
-[BWNRFProcessorControllerConfiguration setAdaptiveFusionInputFormat:];
-[BWNRFProcessorControllerConfiguration setAdaptiveFusionEnabled:];
-[BWNRFProcessorControllerConfiguration setInputFormat:];
-[BWNRFProcessorControllerConfiguration setUnifiedBracketingFusionEnabled:];
-[BWNRFProcessorControllerConfiguration setLearnedFusionMode:];
-[BWNRFProcessorControllerConfiguration setQuadraSupportEnabled:];
-[BWNRFProcessorControllerConfiguration setLearnedNRInputFormat:];
-[BWNRFProcessorControllerConfiguration learnedNRInputFormat];
-[BWNRFProcessorControllerConfiguration setDimensionsByResolutionFlavor:];
-[BWNRFProcessorControllerConfiguration setLearnedFusionInputFormat:];
-[BWNRFProcessorControllerConfiguration learnedNRUsingNRFEnabled];
-[BWNRFProcessorControllerConfiguration quadraSupportEnabled];
-[BWNRFProcessorControllerConfiguration alwaysAllowModifyingInputBuffers];
-[BWNRFProcessorControllerConfiguration adaptiveFusionEnabled];
-[BWNRFProcessorControllerConfiguration setDeepFusionInputFormat:];
-[BWNRFProcessorControllerConfiguration setDepthDataDeliveryEnabled:];
-[BWNRFProcessorControllerConfiguration setAlwaysAllowModifyingInputBuffers:];
-[BWNRFProcessorControllerConfiguration depthDataDeliveryEnabled];
-[BWNRFProcessorControllerConfiguration rawNightModeInputFormat];
-[BWNRFProcessorControllerConfiguration deepFusionWaitForProcessingToFinish];
-[BWNRFProcessorControllerConfiguration outputFormat];
-[BWNRFProcessorControllerConfiguration learnedFusionInputFormat];
-[BWNRFProcessorControllerConfiguration setLowLightFusionEnabled:];
-[BWNRFProcessorControllerConfiguration figThreadPriority];
-[BWNRFProcessorControllerConfiguration deepFusionInputFormat];
-[BWNRFProcessorControllerConfiguration cmiResourceEnabled];
-[BWNRFProcessorControllerConfiguration dimensionsByResolutionFlavor];
-[BWNRFProcessorControllerConfiguration setLearnedNRUsingNRFEnabled:];
```
