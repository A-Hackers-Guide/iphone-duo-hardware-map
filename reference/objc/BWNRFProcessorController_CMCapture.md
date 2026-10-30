# `BWNRFProcessorController`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorController`
- Protocols: `BWNRFProcessorInputDelegate`, `NRFProcessorDelegate`
- 21 instance variables, 5 properties, 20 instance methods, 1 class methods

## Instance variables

```
@"BWNRFProcessorControllerConfiguration" _configuration;
@"NSSet" _supportedPortTypes;
@"FigStateMachine" _stateMachine;
@"<NRFProcessor>" _nrfProcessor;
@"NSString" _nrfProcessorClassName;
# _nrfUBFusionOutputClass;
# _nrfProgressiveBracketingStatisticsClass;
# _nrfProgressiveBracketingParametersClass;
@"NSDictionary" _adaptiveBracketingCaptureParametersByPortType;
# _nrfRawNightModeOutputFrameClass;
# _nrfDeepFusionOutputClass;
# _nrfCompletionStatusClass;
@"NSObject<OS_dispatch_queue>" _completionStatusQueue;
^{opaqueCMFormatDescription=} _outputFormatDescription;
^{opaqueCMFormatDescription=} _inferenceInputFormatDescription;
^{opaqueCMFormatDescription=} _demosaicedRawFormatDescription;
^{opaqueCMFormatDescription=} _linearOutputMIWBAppliedFormatDescription;
^{opaqueCMFormatDescription=} _gainMapFormatDescription;
@"NSMutableArray" _requestQueue;
@"BWNRFProcessorRequest" _currentRequest;
i _lastSelectedFusionMode;
```

## Properties

```
@property (Ti,R,N) progressiveLowLightFusionBatchSize;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWNRFProcessorController initialize];
```

## Instance methods

```
-[BWNRFProcessorController inputReceivedProcessedRawErrorRecoveryFrame:proxy:];
-[BWNRFProcessorController processorGetInferenceResults:];
-[BWNRFProcessorController inputReceivedAllFrames:];
-[BWNRFProcessorController processor:didSelectFusionMode:];
-[BWNRFProcessorController processor:didCompleteProcessingForSurfaceID:];
-[BWNRFProcessorController progressiveLowLightFusionBatchSize];
-[BWNRFProcessorController finishProcessingCurrentInputNow];
-[BWNRFProcessorController dealloc];
-[BWNRFProcessorController processor:outputReadyWithFrameType:outputPixelBuffer:outputMetadata:error:];
-[BWNRFProcessorController initWithConfiguration:];
-[BWNRFProcessorController type];
-[BWNRFProcessorController adaptiveBracketingParametersForDigitalFlashMode:frameStatistics:stationary:sphereOffsetEnabled:detectedObjects:];
-[BWNRFProcessorController metalImageBufferProcessor];
-[BWNRFProcessorController processor:didEnqueueProcessingForSurfaceID:];
-[BWNRFProcessorController cancelProcessing];
-[BWNRFProcessorController input:addFrame:isReferenceFrame:];
-[BWNRFProcessorController externalMemoryDescriptorForResolutionFlavors:];
-[BWNRFProcessorController processor:didSelectProgressiveFusionReferenceFrameIndex:];
-[BWNRFProcessorController adaptiveBracketingDigitalFlashTotalIntegrationTimesProviderForPortType:];
-[BWNRFProcessorController enqueueInputForProcessing:delegate:processErrorRecoveryFrame:processErrorRecoveryProxy:processHDRErrorRecovery:processOriginalImage:processLinearImage:processToneMapping:processInferenceInputImage:clientBracketSequenceNumber:processSemanticRendering:provideInferenceInputImageForProcessing:processSmartStyleRenderingInput:inferencesAvailable:];
```
