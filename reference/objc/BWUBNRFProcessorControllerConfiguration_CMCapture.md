# `BWUBNRFProcessorControllerConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorControllerConfiguration`
- Protocols: `BWNoiseReductionAndFusionProcessorControllerConfiguration`
- 19 instance variables, 25 properties, 35 instance methods, 0 class methods

## Instance variables

```
@"BWVideoFormat" _inputFormat;
@"BWVideoFormat" _outputFormat;
@"NSDictionary" _dimensionsByResolutionFlavor;
B _cmiResourceEnabled;
B _unifiedBracketingFusionSupportEnabled;
B _lowLightFusionEnabled;
i _semanticRenderingVersion;
B _deepFusionEnabled;
@"BWVideoFormat" _deepFusionInputFormat;
B _deepFusionWaitForProcessingToFinish;
I _learnedNRMode;
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
@property (Ti,N,V_semanticRenderingVersion) semanticRenderingVersion;
@property (TI,N,V_learnedNRMode) learnedNRMode;
@property (T@"NSDictionary",&,N) sensorConfigurationsByPortType;
@property (TB,N) deferredCaptureSupportEnabled;
@property (TB,N) deferredPhotoProcessorEnabled;
@property (T@"<MTLCommandQueue>",&,N) metalCommandQueue;
@property (T@"BWVideoFormat",&,N,V_inputFormat) inputFormat;
@property (T@"BWVideoFormat",&,N,V_outputFormat) outputFormat;
@property (TB,N,V_unifiedBracketingFusionSupportEnabled) unifiedBracketingFusionSupportEnabled;
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
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BWUBNRFProcessorControllerConfiguration demosaicedRawPixelFormat];
-[BWUBNRFProcessorControllerConfiguration deepFusionEnabled];
-[BWUBNRFProcessorControllerConfiguration setLearnedNRMode:];
-[BWUBNRFProcessorControllerConfiguration setGreenGhostMitigationVersion:];
-[BWUBNRFProcessorControllerConfiguration gainMapMainImageDownscalingFactor];
-[BWUBNRFProcessorControllerConfiguration setDemosaicedRawPixelFormat:];
-[BWUBNRFProcessorControllerConfiguration setGainMapMainImageDownscalingFactor:];
-[BWUBNRFProcessorControllerConfiguration learnedNRMode];
-[BWUBNRFProcessorControllerConfiguration greenGhostMitigationVersion];
-[BWUBNRFProcessorControllerConfiguration setRawColorCalibrationsByPortType:];
-[BWUBNRFProcessorControllerConfiguration setDeepFusionEnabled:];
-[BWUBNRFProcessorControllerConfiguration setDemosaicedRawEnabled:];
-[BWUBNRFProcessorControllerConfiguration semanticRenderingVersion];
-[BWUBNRFProcessorControllerConfiguration setFigThreadPriority:];
-[BWUBNRFProcessorControllerConfiguration setDeepFusionWaitForProcessingToFinish:];
-[BWUBNRFProcessorControllerConfiguration setSemanticRenderingVersion:];
-[BWUBNRFProcessorControllerConfiguration rawColorCalibrationsByPortType];
-[BWUBNRFProcessorControllerConfiguration setOutputFormat:];
-[BWUBNRFProcessorControllerConfiguration lowLightFusionEnabled];
-[BWUBNRFProcessorControllerConfiguration inputFormat];
-[BWUBNRFProcessorControllerConfiguration dealloc];
-[BWUBNRFProcessorControllerConfiguration demosaicedRawEnabled];
-[BWUBNRFProcessorControllerConfiguration setInputFormat:];
-[BWUBNRFProcessorControllerConfiguration alwaysAllowModifyingInputBuffers];
-[BWUBNRFProcessorControllerConfiguration setDeepFusionInputFormat:];
-[BWUBNRFProcessorControllerConfiguration setDepthDataDeliveryEnabled:];
-[BWUBNRFProcessorControllerConfiguration setAlwaysAllowModifyingInputBuffers:];
-[BWUBNRFProcessorControllerConfiguration depthDataDeliveryEnabled];
-[BWUBNRFProcessorControllerConfiguration deepFusionWaitForProcessingToFinish];
-[BWUBNRFProcessorControllerConfiguration outputFormat];
-[BWUBNRFProcessorControllerConfiguration setLowLightFusionEnabled:];
-[BWUBNRFProcessorControllerConfiguration figThreadPriority];
-[BWUBNRFProcessorControllerConfiguration deepFusionInputFormat];
-[BWUBNRFProcessorControllerConfiguration setUnifiedBracketingFusionSupportEnabled:];
-[BWUBNRFProcessorControllerConfiguration unifiedBracketingFusionSupportEnabled];
```
