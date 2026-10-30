# `BWPhotonicEngineNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- Protocols: `BWNRFProcessorControllerDelegate`, `BWInferenceEngineControllerDelegate`, `BWDeepFusionProcessorControllerDelegate`, `BWDeferredCaptureControllerDelegate`, `BWAdaptiveBracketingController`, `BWDeferredProcessorControllerDelegate`, `BWStereoDisparityProcessorControllerDelegate`, `BWJasperColorStillsExecutorControllerDelegate`, `BWJasperDisparityProcessorControllerDelegate`, `BWLearnedNRProcessorControllerDelegate`, `BWSoftISPProcessorControllerDelegate`, `BWSWFRProcessorControllerDelegate`, `BWSmartStyleRenderingProcessorControllerDelegate`, `BWColorConstancyProcessorControllerDelegate`, `BWRedEyeReductionControllerDelegate`, `BWStillImageProcessingCoordinatorDelegate`, `BWStillImageProcessingSupportProvider`, `BWStillImageFilterStatusDelegate`, `BWDynamicAspectRatioChangeSource`, `BWDynamicPipelineDimensionsChangeSource`
- 70 instance variables, 9 properties, 58 instance methods, 1 class methods

## Instance variables

```
B _resourcesReleased;
@"BWFigVideoCaptureDevice" _device;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _dynamicPipelineChangeStateLock;
i _activeAspectRatio;
{?="width"i"height"i} _activePipelineDimensions;
@"BWPhotonicEngineNodeConfiguration" _nodeConfiguration;
@"NSSet" _supportedPortTypes;
@"BWNodeInput" _sensorRawInput;
@"NSString" _previousCaptureRequestIdentifier;
q _currentSettingsID;
@"NSString" _currentCaptureRequestIdentifier;
@"BWStillImageSettings" _currentStillImageSettings;
@"BWPhotonicEngineNodeResourceCoordinator" _resourceCoordinator;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _resourceLock;
@"BWPhotonicEngineNodeSampleBufferAndInputQueue" _sampleBufferAndInputQueue;
@"NSMutableDictionary" _softISPRemainingInputsByPortType;
@"NSMutableDictionary" _softISPNumberOfInflightInputsByPortType;
@"NSMutableDictionary" _softISPRemainingDisparitySbufsByCaptureFrameFlagsByPortType;
@"BWSharpnessScoreReferenceFrameSelector" _ultraHighResolutionSharpnessScoreReferenceFrameSelector;
@"NSMutableDictionary" _sensorRawErrorRecoveryFrameByPortType;
@"NSMutableDictionary" _sensorRawProvenanceFrameByCaptureFrameFlags;
^{opaqueCMFormatDescription=} _provenanceFormatDescription;
B _setupForBeginMomentProcessing;
@"NSMutableDictionary" _stashedSoftISPResultsByPortType;
@"NSMutableDictionary" _stashedSensorRawFramesByPortType;
@"NSMutableDictionary" _stashedAWBMetadataByPortType;
@"NSMutableDictionary" _nrfProcessorInputsByPortType;
@"NSMutableDictionary" _emittedOrEnqueuedReferenceFrameIDByPortType;
@"NSMutableDictionary" _stillImageFusionModeByCaptureRequestIdentifier;
@"NSMutableDictionary" _learnedNRInputByPortType;
@"NSMutableDictionary" _learnedNRSIFRSbufByPortType;
@"NSMutableDictionary" _deepFusionProcessorInputByPortType;
@"NSDictionary" _deepFusionEnhancedResolutionCanProcessDebugInfo;
@"NSMutableDictionary" _inferenceControllerInputByPortType;
@"NSMutableDictionary" _textureStylesInferenceControllerInputByPortType;
@"NSMutableDictionary" _pendingTextureStyleBaseLookPeopleDataByPortType;
^{opaqueCMFormatDescription=} _inferenceInputFormatDescription;
^{OpaqueVTPixelTransferSession=} _inferenceInputPixelTransferSession;
@"NSMutableDictionary" _swfrProcessorControllerInputByPortType;
@"NSMutableDictionary" _swfrRawRedEyeReductionAuxImageByPortType;
@"NSMutableDictionary" _colorConstancyProcessorControllerInputByPortType;
@"NSMutableDictionary" _redEyeReductionInputByPortType;
@"NSMutableDictionary" _intelligentDistortionCorrectionProcessorInputByPortType;
@"NSMutableDictionary" _remainingIntelligentDistortionCorrectionProcessorInputsByPortType;
I _lowResPersonSegmentationMaskWidth;
I _lowResPersonSegmentationMaskHeight;
@"NSMutableDictionary" _deepZoomProcessorInputByPortType;
@"NSMutableDictionary" _scalerProcessorControllerInputsByPortType;
@"BWStereoDisparityProcessorInput" _stereoDisparityProcessorInput;
i _stereoDisparityRemainingProcessorInputs;
@"NSMutableDictionary" _clientBracketEmittedOrEnqueuedReferenceFrameIDByPortTypeAndSequenceNumber;
@"NSMutableDictionary" _stereoDisparityClientBracketProcessorInputsBySequenceNumber;
@"NSMutableDictionary" _smartStyleRenderingInputByPortType;
@"BWNodeInput" _pointCloudInput;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _pointCloudLock;
B _discardPointClouds;
Q _pointCloudsLoggingCounter;
@"NSMutableDictionary" _jasperColorStillsExecutorInputByPortType;
@"NSMutableDictionary" _jasperDisparityProcessorInputByPortType;
@"BWDeferredCaptureControllerInput" _deferredCaptureControllerInput;
^{opaqueCMSampleBuffer=} _deferredCaptureProxyOrErrorRecoverySbuf;
@"NSMutableDictionary" _deferredStereoPhotoCaptureSecondarySbufsByFusionMode;
@"NSMutableDictionary" _deferredProcessorInputByPortType;
@"NSMutableDictionary" _stereoPhotoSensorRawFrameByPortType;
^{opaqueCMSampleBuffer=} _stereoPhotoStashedDeepZoomTransferSbuf;
i _dcOutputBufferCount;
i _demosaicedRawOutputBufferCount;
^{opaqueCMFormatDescription=} _sushiRawFormatDescription;
^{opaqueCMFormatDescription=} _gainMapFormatDescription;
@"<BWStillImageProcessingCoordinator>" _processingCoordinator;
```

## Properties

```
@property (T@"BWNodeInput",R,N) sensorRawInput;
@property (T@"BWNodeInput",R,N) pointCloudInput;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSDictionary",R,N) learnedFusionModeByPortType;
@property (Ti) activeAspectRatio;
@property (T{?=ii}) activePipelineDimensions;
```

## Class methods

```
+[BWPhotonicEngineNode initialize];
```

## Instance methods

```
-[BWPhotonicEngineNode prepareForCurrentConfigurationToBecomeLive];
-[BWPhotonicEngineNode preparedOutputPixelBufferPoolForAttachedMediaKey:format:];
-[BWPhotonicEngineNode processorController:didFinishProcessingInput:err:];
-[BWPhotonicEngineNode sharePhotoEncoderControllerForPiecemealEncoding:];
-[BWPhotonicEngineNode processorController:didFinishProcessingInferenceBuffer:metadata:inferenceAttachedMediaKey:processorInput:err:];
-[BWPhotonicEngineNode processingCoordinator:didEncounterError:stillImageSettings:description:];
-[BWPhotonicEngineNode processorController:didFinishProcessingSampleBuffer:type:processorInput:err:];
-[BWPhotonicEngineNode processorController:didFinishProcessingInferenceAttachedMediaMetadata:processorInput:];
-[BWPhotonicEngineNode activePipelineDimensions];
-[BWPhotonicEngineNode renderSampleBuffer:forInput:];
-[BWPhotonicEngineNode processorController:didSelectVitalityMode:forProcessorInput:];
-[BWPhotonicEngineNode processorController:newOutputPixelBufferForProcessorInput:type:];
-[BWPhotonicEngineNode processorController:newOutputPixelBufferForProcessorInput:type:dimensions:];
-[BWPhotonicEngineNode processorController:willProcessRedEyeReductionForProcessorInput:];
-[BWPhotonicEngineNode processorController:didFinishProcessingBuffer:metadata:type:captureFrameFlags:processorInput:err:];
-[BWPhotonicEngineNode processorControllerWillProcessInferences:];
-[BWPhotonicEngineNode processorController:didSelectNewReferenceFrameWithPTS:transform:processorInput:];
-[BWPhotonicEngineNode dealloc];
-[BWPhotonicEngineNode processorController:newInferencesForProcessorInput:];
-[BWPhotonicEngineNode processorController:newOutputPixelBufferForProcessorInput:type:attachedMediaKey:];
-[BWPhotonicEngineNode initWithNodeConfiguration:captureDevice:];
-[BWPhotonicEngineNode pointCloudInput];
-[BWPhotonicEngineNode stopAdaptiveBracketingForSettings:withGroup:];
-[BWPhotonicEngineNode processingOnBeginMomentSupportedForCaptureSettings:];
-[BWPhotonicEngineNode setActivePipelineDimensions:];
-[BWPhotonicEngineNode processorController:outputPixelBufferDimensionsForProcessorInput:type:attachedMediaKey:pixelFormat:dimensions:];
-[BWPhotonicEngineNode processingCoordinator:didFinishProcessingSampleBuffer:description:];
-[BWPhotonicEngineNode processorController:processRawErrorRecoveryFrameForProcessorInput:processErrorRecoveryProxy:failureMetadata:];
-[BWPhotonicEngineNode processorController:willAddSampleBuffer:processorInput:];
-[BWPhotonicEngineNode processorController:newInferencesForProcessorInput:inferenceInputBufferType:];
-[BWPhotonicEngineNode handleStillImagePrewarmWithSettings:resourceConfig:forInput:];
-[BWPhotonicEngineNode activeAspectRatio];
-[BWPhotonicEngineNode processorController:willAddBuffer:metadata:bufferType:processorInput:];
-[BWPhotonicEngineNode captureType:supportedForPortType:];
-[BWPhotonicEngineNode demosaicedRawSupportedForCaptureType:];
-[BWPhotonicEngineNode processorController:didDetermineProvenanceFrame:processorInput:err:];
-[BWPhotonicEngineNode didSelectFormat:forOutput:];
-[BWPhotonicEngineNode processorController:didSelectLowLightReferenceFrame:processorInput:];
-[BWPhotonicEngineNode processorController:didFinishProcessingInference:inferenceAttachmentKey:processorInput:err:];
-[BWPhotonicEngineNode adaptiveBracketingParametersForDigitalFlashMode:frameStatistics:stationary:sphereOffsetEnabled:detectedObjects:];
-[BWPhotonicEngineNode captureType:supportedForPortType:highResolutionFlavor:zoomBasedQSub:];
-[BWPhotonicEngineNode filterNodeDidReceiveStandardResolutionDeepFusionBuffer:error:];
-[BWPhotonicEngineNode didReachEndOfDataForConfigurationID:input:];
-[BWPhotonicEngineNode processorController:didSelectFusionMode:processorInput:];
-[BWPhotonicEngineNode adaptiveBracketingDigitalFlashTotalIntegrationTimesProviderForPortType:wait:];
-[BWPhotonicEngineNode processorController:newOutputPixelBufferForProcessorInput:type:attachedMediaKey:pixelFormat:dimensions:dimensionAlignment:];
-[BWPhotonicEngineNode setActiveAspectRatio:];
-[BWPhotonicEngineNode processorController:didDetermineReferenceFrame:processorInput:err:];
-[BWPhotonicEngineNode nodeSubType];
-[BWPhotonicEngineNode sensorRawInput];
-[BWPhotonicEngineNode processorController:newOutputPixelBufferForProcessorInput:type:attachedMediaKey:pixelFormat:dimensions:];
-[BWPhotonicEngineNode didSelectFormat:forInput:];
-[BWPhotonicEngineNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWPhotonicEngineNode idcSupportedForCaptureType:captureFlags:portType:];
-[BWPhotonicEngineNode processingCoordinatorComplete:];
-[BWPhotonicEngineNode handleNodeError:forInput:];
-[BWPhotonicEngineNode learnedFusionModeByPortType];
-[BWPhotonicEngineNode nodeType];
```
