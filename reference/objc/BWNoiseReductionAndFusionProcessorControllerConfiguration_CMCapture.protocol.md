# `BWNoiseReductionAndFusionProcessorControllerConfiguration` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 19 properties, 38 instance methods, 0 class methods

## Properties

```
@property (T@"NSDictionary",&,N) sensorConfigurationsByPortType;
@property (TB,N) deferredCaptureSupportEnabled;
@property (TB,N) deferredPhotoProcessorEnabled;
@property (T@"<MTLCommandQueue>",&,N) metalCommandQueue;
@property (T@"BWVideoFormat",&,N) inputFormat;
@property (T@"BWVideoFormat",&,N) outputFormat;
@property (TB,N) unifiedBracketingFusionSupportEnabled;
@property (TB,N) lowLightFusionEnabled;
@property (TB,N) deepFusionEnabled;
@property (T@"BWVideoFormat",&,N) deepFusionInputFormat;
@property (TB,N) deepFusionWaitForProcessingToFinish;
@property (TB,N) depthDataDeliveryEnabled;
@property (TB,N) alwaysAllowModifyingInputBuffers;
@property (TI,N) figThreadPriority;
@property (Ti,N) greenGhostMitigationVersion;
@property (TB,N) demosaicedRawEnabled;
@property (TI,N) demosaicedRawPixelFormat;
@property (T@"NSDictionary",&,N) rawColorCalibrationsByPortType;
@property (Tf,N) gainMapMainImageDownscalingFactor;
```

## Instance methods

```
-[BWNoiseReductionAndFusionProcessorControllerConfiguration demosaicedRawPixelFormat];
-[BWNoiseReductionAndFusionProcessorControllerConfiguration deepFusionEnabled];
-[BWNoiseReductionAndFusionProcessorControllerConfiguration setGreenGhostMitigationVersion:];
-[BWNoiseReductionAndFusionProcessorControllerConfiguration gainMapMainImageDownscalingFactor];
-[BWNoiseReductionAndFusionProcessorControllerConfiguration setDemosaicedRawPixelFormat:];
-[BWNoiseReductionAndFusionProcessorControllerConfiguration setGainMapMainImageDownscalingFactor:];
-[BWNoiseReductionAndFusionProcessorControllerConfiguration greenGhostMitigationVersion];
-[BWNoiseReductionAndFusionProcessorControllerConfiguration setMetalCommandQueue:];
-[BWNoiseReductionAndFusionProcessorControllerConfiguration setDeferredCaptureSupportEnabled:];
-[BWNoiseReductionAndFusionProcessorControllerConfiguration setRawColorCalibrationsByPortType:];
-[BWNoiseReductionAndFusionProcessorControllerConfiguration setDeepFusionEnabled:];
-[BWNoiseReductionAndFusionProcessorControllerConfiguration setDemosaicedRawEnabled:];
-[BWNoiseReductionAndFusionProcessorControllerConfiguration metalCommandQueue];
-[BWNoiseReductionAndFusionProcessorControllerConfiguration setFigThreadPriority:];
-[BWNoiseReductionAndFusionProcessorControllerConfiguration setDeepFusionWaitForProcessingToFinish:];
-[BWNoiseReductionAndFusionProcessorControllerConfiguration deferredCaptureSupportEnabled];
-[BWNoiseReductionAndFusionProcessorControllerConfiguration deferredPhotoProcessorEnabled];
-[BWNoiseReductionAndFusionProcessorControllerConfiguration sensorConfigurationsByPortType];
-[BWNoiseReductionAndFusionProcessorControllerConfiguration rawColorCalibrationsByPortType];
-[BWNoiseReductionAndFusionProcessorControllerConfiguration setOutputFormat:];
-[BWNoiseReductionAndFusionProcessorControllerConfiguration lowLightFusionEnabled];
-[BWNoiseReductionAndFusionProcessorControllerConfiguration setDeferredPhotoProcessorEnabled:];
-[BWNoiseReductionAndFusionProcessorControllerConfiguration inputFormat];
-[BWNoiseReductionAndFusionProcessorControllerConfiguration demosaicedRawEnabled];
-[BWNoiseReductionAndFusionProcessorControllerConfiguration setInputFormat:];
-[BWNoiseReductionAndFusionProcessorControllerConfiguration alwaysAllowModifyingInputBuffers];
-[BWNoiseReductionAndFusionProcessorControllerConfiguration setDeepFusionInputFormat:];
-[BWNoiseReductionAndFusionProcessorControllerConfiguration setDepthDataDeliveryEnabled:];
-[BWNoiseReductionAndFusionProcessorControllerConfiguration setAlwaysAllowModifyingInputBuffers:];
-[BWNoiseReductionAndFusionProcessorControllerConfiguration setSensorConfigurationsByPortType:];
-[BWNoiseReductionAndFusionProcessorControllerConfiguration depthDataDeliveryEnabled];
-[BWNoiseReductionAndFusionProcessorControllerConfiguration deepFusionWaitForProcessingToFinish];
-[BWNoiseReductionAndFusionProcessorControllerConfiguration outputFormat];
-[BWNoiseReductionAndFusionProcessorControllerConfiguration setLowLightFusionEnabled:];
-[BWNoiseReductionAndFusionProcessorControllerConfiguration figThreadPriority];
-[BWNoiseReductionAndFusionProcessorControllerConfiguration deepFusionInputFormat];
-[BWNoiseReductionAndFusionProcessorControllerConfiguration setUnifiedBracketingFusionSupportEnabled:];
-[BWNoiseReductionAndFusionProcessorControllerConfiguration unifiedBracketingFusionSupportEnabled];
```
