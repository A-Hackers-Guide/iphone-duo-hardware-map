# `BWDeferredCaptureControllerInput`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorControllerInput`
- 13 instance variables, 4 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"BWDeferredCaptureControllerConfiguration" _configuration;
@"BWStillImageSettings" _settings;
@"BWDeferredCaptureContainer" _captureContainer;
i _compressionProfile;
B _proxyBufferReady;
B _depthDataGenerationFailed;
B _skipInferences;
@"NSNumber" _canProcessDeepFusionEnhancedResolution;
^{opaqueCMSampleBuffer=} _stashedEVZero;
^{opaqueCMSampleBuffer=} _stashedEVMinus;
^{opaqueCMSampleBuffer=} _stashedErrorRecovery;
@"NSNumber" _proxyGenerationUsedEVMinus;
@"NSNumber" _proxyGenerationUsedEVZero;
```

## Properties

```
@property (T@"BWDeferredCaptureContainer",R,N,V_captureContainer) captureContainer;
@property (Ti,R,N,V_compressionProfile) compressionProfile;
@property (TB,R,N,V_skipInferences) skipInferences;
@property (T@"BWDeferredPipelineParameters",R,N) pipelineParameters;
```

## Instance methods

```
-[BWDeferredCaptureControllerInput dealloc];
-[BWDeferredCaptureControllerInput pipelineParameters];
-[BWDeferredCaptureControllerInput initWithSettings:configuration:sourceNodePixelBufferAttributes:];
-[BWDeferredCaptureControllerInput _addDictionary:tag:];
-[BWDeferredCaptureControllerInput _addInference:inferenceAttachmentKey:portType:];
-[BWDeferredCaptureControllerInput _addInferenceBuffer:metadata:inferenceAttachedMediaKey:portType:];
-[BWDeferredCaptureControllerInput addBuffer:bufferType:captureFrameFlags:metadata:portType:];
-[BWDeferredCaptureControllerInput addDictionary:tag:];
-[BWDeferredCaptureControllerInput addPhotoDescriptor:];
-[BWDeferredCaptureControllerInput addSensorRawSampleBuffer:];
-[BWDeferredCaptureControllerInput canProcessDeepFusionEnhancedResolution:skipInferences:];
-[BWDeferredCaptureControllerInput captureContainer];
-[BWDeferredCaptureControllerInput compressionProfile];
-[BWDeferredCaptureControllerInput depthDataGenerationFailed];
-[BWDeferredCaptureControllerInput encounteredProcessingError:];
-[BWDeferredCaptureControllerInput proxyReadyWithFPNREnabled:];
-[BWDeferredCaptureControllerInput setLearnedNRProxyGenerationUsedEVZero:usedEVMinus:];
-[BWDeferredCaptureControllerInput setProxyGenerationUsedEVMinus:];
-[BWDeferredCaptureControllerInput skipInferences];
```
