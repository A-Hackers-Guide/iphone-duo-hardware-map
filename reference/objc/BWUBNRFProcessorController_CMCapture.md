# `BWUBNRFProcessorController`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorController`
- Protocols: `BWUBNRFProcessorInputDelegate`, `NRFProcessorDelegate`, `BWNoiseReductionAndFusionProcessorController`
- 21 instance variables, 5 properties, 19 instance methods, 1 class methods

## Instance variables

```
@"BWUBNRFProcessorControllerConfiguration" _configuration;
@"NSSet" _supportedPortTypes;
@"FigStateMachine" _stateMachine;
@"<NRFProcessor>" _nrfProcessor;
@"NSString" _nrfProcessorClassName;
@"NRFPrepareDescriptor" _prepareDescriptor;
@"NRFPrepareDescriptor" _ubPrepareDescriptor;
# _nrfUBFusionOutputClass;
# _nrfProgressiveBracketingStatisticsClass;
# _nrfProgressiveBracketingParametersClass;
@"NSDictionary" _adaptiveBracketingCaptureParametersByPortType;
# _nrfDeepFusionOutputClass;
@"NRFPrepareDescriptor" _deepFusionPrepareDescriptor;
# _nrfCompletionStatusClass;
@"NSObject<OS_dispatch_queue>" _completionStatusQueue;
^{opaqueCMFormatDescription=} _outputFormatDescription;
^{opaqueCMFormatDescription=} _inferenceInputFormatDescription;
^{opaqueCMFormatDescription=} _demosaicedRawFormatDescription;
^{opaqueCMFormatDescription=} _gainMapFormatDescription;
@"NSMutableArray" _requestQueue;
@"BWUBNRFProcessorRequest" _currentRequest;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Ti,R,N) progressiveLowLightFusionBatchSize;
```

## Class methods

```
+[BWUBNRFProcessorController initialize];
```

## Instance methods

```
-[BWUBNRFProcessorController processorGetInferenceResults:];
-[BWUBNRFProcessorController inputReceivedAllFrames:];
-[BWUBNRFProcessorController processor:didSelectFusionMode:];
-[BWUBNRFProcessorController processor:didCompleteProcessingForSurfaceID:];
-[BWUBNRFProcessorController progressiveLowLightFusionBatchSize];
-[BWUBNRFProcessorController finishProcessingCurrentInputNow];
-[BWUBNRFProcessorController dealloc];
-[BWUBNRFProcessorController processor:outputReadyWithFrameType:outputPixelBuffer:outputMetadata:error:];
-[BWUBNRFProcessorController initWithConfiguration:];
-[BWUBNRFProcessorController type];
-[BWUBNRFProcessorController adaptiveBracketingParametersForDigitalFlashMode:frameStatistics:stationary:sphereOffsetEnabled:detectedObjects:];
-[BWUBNRFProcessorController metalImageBufferProcessor];
-[BWUBNRFProcessorController processor:didEnqueueProcessingForSurfaceID:];
-[BWUBNRFProcessorController cancelProcessing];
-[BWUBNRFProcessorController input:addFrame:isReferenceFrame:];
-[BWUBNRFProcessorController externalMemoryDescriptorForResolutionFlavors:];
-[BWUBNRFProcessorController processor:didSelectProgressiveFusionReferenceFrameIndex:];
-[BWUBNRFProcessorController adaptiveBracketingDigitalFlashTotalIntegrationTimesProviderForPortType:];
-[BWUBNRFProcessorController enqueueInputForProcessing:delegate:processErrorRecoveryFrame:processOriginalImage:clientBracketSequenceNumber:processSemanticRendering:provideInferenceInputImageForProcessing:inferencesAvailable:];
```
