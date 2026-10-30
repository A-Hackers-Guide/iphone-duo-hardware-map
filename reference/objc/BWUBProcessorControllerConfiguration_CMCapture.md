# `BWUBProcessorControllerConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorControllerConfiguration`
- Protocols: `BWNoiseReductionAndFusionProcessorControllerConfiguration`
- 15 instance variables, 23 properties, 31 instance methods, 0 class methods

## Instance variables

```
@"BWVideoFormat" _inputFormat;
@"BWVideoFormat" _outputFormat;
B _unifiedBracketingFusionSupportEnabled;
B _lowLightFusionEnabled;
B _deepFusionEnabled;
@"BWVideoFormat" _deepFusionInputFormat;
B _deepFusionWaitForProcessingToFinish;
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
-[BWUBProcessorControllerConfiguration demosaicedRawPixelFormat];
-[BWUBProcessorControllerConfiguration deepFusionEnabled];
-[BWUBProcessorControllerConfiguration setGreenGhostMitigationVersion:];
-[BWUBProcessorControllerConfiguration gainMapMainImageDownscalingFactor];
-[BWUBProcessorControllerConfiguration setDemosaicedRawPixelFormat:];
-[BWUBProcessorControllerConfiguration setGainMapMainImageDownscalingFactor:];
-[BWUBProcessorControllerConfiguration greenGhostMitigationVersion];
-[BWUBProcessorControllerConfiguration setRawColorCalibrationsByPortType:];
-[BWUBProcessorControllerConfiguration setDeepFusionEnabled:];
-[BWUBProcessorControllerConfiguration setDemosaicedRawEnabled:];
-[BWUBProcessorControllerConfiguration setFigThreadPriority:];
-[BWUBProcessorControllerConfiguration setDeepFusionWaitForProcessingToFinish:];
-[BWUBProcessorControllerConfiguration rawColorCalibrationsByPortType];
-[BWUBProcessorControllerConfiguration setOutputFormat:];
-[BWUBProcessorControllerConfiguration lowLightFusionEnabled];
-[BWUBProcessorControllerConfiguration inputFormat];
-[BWUBProcessorControllerConfiguration dealloc];
-[BWUBProcessorControllerConfiguration demosaicedRawEnabled];
-[BWUBProcessorControllerConfiguration setInputFormat:];
-[BWUBProcessorControllerConfiguration alwaysAllowModifyingInputBuffers];
-[BWUBProcessorControllerConfiguration setDeepFusionInputFormat:];
-[BWUBProcessorControllerConfiguration setDepthDataDeliveryEnabled:];
-[BWUBProcessorControllerConfiguration setAlwaysAllowModifyingInputBuffers:];
-[BWUBProcessorControllerConfiguration depthDataDeliveryEnabled];
-[BWUBProcessorControllerConfiguration deepFusionWaitForProcessingToFinish];
-[BWUBProcessorControllerConfiguration outputFormat];
-[BWUBProcessorControllerConfiguration setLowLightFusionEnabled:];
-[BWUBProcessorControllerConfiguration figThreadPriority];
-[BWUBProcessorControllerConfiguration deepFusionInputFormat];
-[BWUBProcessorControllerConfiguration setUnifiedBracketingFusionSupportEnabled:];
-[BWUBProcessorControllerConfiguration unifiedBracketingFusionSupportEnabled];
```
