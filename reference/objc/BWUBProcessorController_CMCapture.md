# `BWUBProcessorController`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorController`
- Protocols: `BWUBProcessorInputDelegate`, `UBProcessorDelegate`, `BWNoiseReductionAndFusionProcessorController`
- 15 instance variables, 5 properties, 16 instance methods, 2 class methods

## Instance variables

```
@"BWUBProcessorControllerConfiguration" _configuration;
@"NSSet" _supportedPortTypes;
@"FigStateMachine" _stateMachine;
@"UBProcessor" _ubProcessor;
@"UBPrepareDescriptor" _prepareDescriptor;
# _ubFusionOutputClass;
# _ubProgressiveBracketingStatisticsClass;
# _ubProgressiveBracketingParametersClass;
@"NSDictionary" _adaptiveBracketingCaptureParametersByPortType;
# _ubDeepFusionOutputClass;
@"UBPrepareDescriptor" _deepFusionPrepareDescriptor;
^{opaqueCMFormatDescription=} _outputFormatDescription;
^{opaqueCMFormatDescription=} _inferenceInputFormatDescription;
@"NSMutableArray" _requestQueue;
@"BWUBProcessorRequest" _currentRequest;
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
+[BWUBProcessorController initialize];
+[BWUBProcessorController lazilyAllocatesDeepFusionOutputBuffers];
```

## Instance methods

```
-[BWUBProcessorController processorGetInferenceResults:];
-[BWUBProcessorController inputReceivedAllFrames:];
-[BWUBProcessorController processor:didSelectFusionMode:];
-[BWUBProcessorController processor:didCompleteProcessingForSurfaceID:];
-[BWUBProcessorController progressiveLowLightFusionBatchSize];
-[BWUBProcessorController finishProcessingCurrentInputNow];
-[BWUBProcessorController dealloc];
-[BWUBProcessorController processor:outputReadyWithFrameType:outputPixelBuffer:outputMetadata:error:];
-[BWUBProcessorController initWithConfiguration:];
-[BWUBProcessorController type];
-[BWUBProcessorController adaptiveBracketingParametersForDigitalFlashMode:frameStatistics:stationary:sphereOffsetEnabled:detectedObjects:];
-[BWUBProcessorController processor:didEnqueueProcessingForSurfaceID:];
-[BWUBProcessorController cancelProcessing];
-[BWUBProcessorController input:addFrame:isReferenceFrame:];
-[BWUBProcessorController adaptiveBracketingDigitalFlashTotalIntegrationTimesProviderForPortType:];
-[BWUBProcessorController enqueueInputForProcessing:delegate:processErrorRecoveryFrame:processOriginalImage:clientBracketSequenceNumber:processSemanticRendering:provideInferenceInputImageForProcessing:inferencesAvailable:];
```
