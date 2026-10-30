# `BWUBNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- Protocols: `BWNoiseReductionAndFusionProcessorDelegate`, `BWInferenceEngineControllerDelegate`, `BWDeepFusionProcessorControllerDelegate`, `BWDeferredCaptureControllerDelegate`, `BWAdaptiveBracketingController`, `BWDeferredProcessorControllerDelegate`, `BWStereoDisparityProcessorControllerDelegate`, `BWJasperColorStillsExecutorControllerDelegate`, `BWJasperDisparityProcessorControllerDelegate`, `BWLearnedNRProcessorControllerDelegate`, `BWRedEyeReductionControllerDelegate`, `BWStillImageProcessingSupportProvider`
- 71 instance variables, 6 properties, 44 instance methods, 1 class methods

## Instance variables

```
B _resourcesReleased;
@"BWFigVideoCaptureDevice" _device;
@"BWUBNodeConfiguration" _nodeConfiguration;
@"NSSet" _supportedPortTypes;
@"NSString" _previousCaptureRequestIdentifier;
q _currentSettingsID;
@"NSString" _currentCaptureRequestIdentifier;
@"BWStillImageProcessorCoordinator" _processorCoordinator;
@"NSObject<OS_dispatch_queue>" _processorCoordinatorWorkerQueue;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _processorCoordinatorLock;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _resourceLock;
@"NSObject<OS_dispatch_queue>" _emitQueue;
B _useSharedExternalMemoryResourceForProcessorControllers;
B _sharedExternalMemoryResourceForProcessorControllersSetUp;
@"CMIExternalMemoryResource" _sharedExternalMemoryResource;
@"BWPixelBufferPool" _noiseReductionAndFusionProcessorOutputIntermediatePool;
Q _nrProcessorControllerType;
@"<BWNoiseReductionAndFusionProcessorControllerConfiguration>" _nrProcessorControllerConfiguration;
@"NSMutableDictionary" _nrProcessorInputsByPortType;
@"NSMutableDictionary" _emittedOrEnqueuedReferenceFrameIDByPortType;
@"NSMutableDictionary" _nrfusionModeByCaptureRequestIdentifier;
@"BWLearnedNRProcessorControllerConfiguration" _learnedNRProcessorControllerConfiguration;
@"NSMutableDictionary" _learnedNRInputByPortType;
@"BWDeepFusionProcessorControllerConfiguration" _deepFusionProcessorControllerConfiguration;
@"NSMutableDictionary" _deepFusionProcessorInputByPortType;
@"NSObject<OS_dispatch_queue>" _deepFusionProcessorControllerQueue;
@"BWPixelBufferPool" _syntheticIntermediatesPool;
@"BWPixelBufferPool" _fusionMapPool;
@"BWInferenceEngineControllerConfiguration" _inferenceControllerConfiguration;
@"NSMutableDictionary" _inferenceControllerInputByPortType;
@"NSObject<OS_dispatch_queue>" _inferenceControllerQueue;
@"NSObject<OS_dispatch_group>" _inferenceControllerGroup;
@"BWPixelBufferPool" _intermediateInferenceInputPool;
@"NSDictionary" _inferenceOutputPoolsByAttachedMediaKey;
@"BWStillImageInferences" _inferences;
^{opaqueCMSampleBuffer=} _inferenceOutputSampleBuffer;
^{opaqueCMFormatDescription=} _inferenceInputFormatDescription;
^{OpaqueVTPixelTransferSession=} _inferenceInputPixelTransferSession;
^{opaqueCMFormatDescription=} _inferenceAttachedMediaFormatDescription;
@"NSDictionary" _providedInferenceAttachedMediaModesByAttachedMediaKey;
@"BWStillImageProcessorControllerConfiguration" _redEyeReductionConfiguration;
@"NSMutableDictionary" _redEyeReductionInputByPortType;
@"BWIntelligentDistortionCorrectionProcessorControllerConfiguration" _intelligentDistortionCorrectionControllerConfiguration;
@"NSMutableDictionary" _intelligentDistortionCorrectionProcessorInputByPortType;
@"NSMutableDictionary" _remainingIntelligentDistortionCorrectionProcessorInputsByPortType;
I _lowResPersonSegmentationMaskWidth;
I _lowResPersonSegmentationMaskHeight;
@"BWDeepZoomProcessorControllerConfiguration" _deepZoomProcessorControllerConfiguration;
@"NSMutableDictionary" _deepZoomProcessorInputByPortType;
@"BWStereoDisparityProcessorControllerConfiguration" _stereoDisparityProcessorControllerConfiguration;
@"BWStereoDisparityProcessorInput" _stereoDisparityProcessorInput;
i _stereoDisparityRemainingProcessorInputs;
@"NSObject<OS_dispatch_queue>" _stereoDisparityProcessorControllerQueue;
@"NSMutableDictionary" _clientBracketEmittedOrEnqueuedReferenceFrameIDByPortTypeAndSequenceNumber;
@"NSMutableDictionary" _stereoDisparityClientBracketProcessorInputsBySequenceNumber;
@"BWNodeInput" _pointCloudInput;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _pointCloudLock;
B _discardPointClouds;
@"BWJasperColorStillsExecutorControllerConfiguration" _jasperColorStillsExecutorConfiguration;
@"NSMutableDictionary" _jasperColorStillsExecutorInputByPortType;
@"BWJasperDisparityProcessorControllerConfiguration" _jasperDisparityProcessorControllerConfiguration;
@"NSMutableDictionary" _jasperDisparityProcessorInputByPortType;
@"BWDeferredCaptureControllerConfiguration" _deferredCaptureControllerConfiguration;
@"BWDeferredCaptureControllerInput" _deferredCaptureControllerInput;
^{opaqueCMSampleBuffer=} _deferredCaptureProxyOrErrorRecoverySbuf;
@"NSObject<OS_dispatch_queue>" _deferredProcessorControllerQueue;
@"BWDeferredProcessorControllerConfiguration" _deferredProcessorControllerConfiguration;
@"NSMutableDictionary" _deferredProcessorInputByPortType;
i _dcOutputBufferCount;
i _demosaicedRawOutputBufferCount;
^{opaqueCMFormatDescription=} _sushiRawFormatDescription;
```

## Properties

```
@property (T@"BWNodeInput",R,N) pointCloudInput;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSDictionary",R,N) learnedFusionModeByPortType;
```

## Class methods

```
+[BWUBNode initialize];
```

## Instance methods

```
-[BWUBNode prepareForCurrentConfigurationToBecomeLive];
-[BWUBNode preparedOutputPixelBufferPoolForAttachedMediaKey:format:];
-[BWUBNode processorController:didFinishProcessingInput:err:];
-[BWUBNode processorController:didFinishProcessingInferenceBuffer:metadata:inferenceAttachedMediaKey:processorInput:err:];
-[BWUBNode processorController:didFinishProcessingSampleBuffer:type:processorInput:err:];
-[BWUBNode processorController:didFinishProcessingInferenceAttachedMediaMetadata:processorInput:];
-[BWUBNode renderSampleBuffer:forInput:];
-[BWUBNode processorController:newOutputPixelBufferForProcessorInput:type:];
-[BWUBNode processorController:newOutputPixelBufferForProcessorInput:type:dimensions:];
-[BWUBNode processorController:willProcessRedEyeReductionForProcessorInput:];
-[BWUBNode processorController:didFinishProcessingBuffer:metadata:type:captureFrameFlags:processorInput:err:];
-[BWUBNode processorControllerWillProcessInferences:];
-[BWUBNode processorController:didSelectNewReferenceFrameWithPTS:transform:processorInput:];
-[BWUBNode dealloc];
-[BWUBNode processorController:newInferencesForProcessorInput:];
-[BWUBNode processorController:newOutputPixelBufferForProcessorInput:type:attachedMediaKey:];
-[BWUBNode initWithNodeConfiguration:captureDevice:];
-[BWUBNode pointCloudInput];
-[BWUBNode stopAdaptiveBracketingForSettings:withGroup:];
-[BWUBNode processingOnBeginMomentSupportedForCaptureSettings:];
-[BWUBNode processorController:newInferencesForProcessorInput:inferenceInputBufferType:];
-[BWUBNode handleStillImagePrewarmWithSettings:resourceConfig:forInput:];
-[BWUBNode processorController:willAddBuffer:metadata:bufferType:processorInput:];
-[BWUBNode captureType:supportedForPortType:];
-[BWUBNode demosaicedRawSupportedForCaptureType:];
-[BWUBNode processorController:didDetermineProvenanceFrame:processorInput:err:];
-[BWUBNode didSelectFormat:forOutput:];
-[BWUBNode processorController:didSelectLowLightReferenceFrame:processorInput:];
-[BWUBNode processorController:didFinishProcessingInference:inferenceAttachmentKey:processorInput:err:];
-[BWUBNode adaptiveBracketingParametersForDigitalFlashMode:frameStatistics:stationary:sphereOffsetEnabled:detectedObjects:];
-[BWUBNode captureType:supportedForPortType:highResolutionFlavor:zoomBasedQSub:];
-[BWUBNode didSelectFormat:forInput:forAttachedMediaKey:];
-[BWUBNode processorController:didSelectFusionMode:processorInput:];
-[BWUBNode adaptiveBracketingDigitalFlashTotalIntegrationTimesProviderForPortType:wait:];
-[BWUBNode processorController:didDetermineReferenceFrame:processorInput:err:];
-[BWUBNode nodeSubType];
-[BWUBNode didSelectFormat:forInput:];
-[BWUBNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWUBNode idcSupportedForCaptureType:captureFlags:portType:];
-[BWUBNode handleNodeError:forInput:];
-[BWUBNode learnedFusionModeByPortType];
-[BWUBNode nodeType];
-[BWUBNode didReachEndOfDataForInput:];
-[BWUBNode processorCoordinator];
```
