# `BWDeepFusionProcessorController`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorController`
- Protocols: `BWDeepFusionProcessorInputDelegate`, `IBPDeepFusionProcessorDelegate`
- 15 instance variables, 4 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"BWDeepFusionProcessorControllerConfiguration" _configuration;
@"NSSet" _supportedPortTypes;
@"FigStateMachine" _stateMachine;
i _processorVersion;
@"<IBPDeepFusionProcessor>" _deepFusionProcessor;
# _deepFusionOutputClass;
^{opaqueCMFormatDescription=} _outputFormatDescription;
^{opaqueCMFormatDescription=} _quadraForEnhancedResolutionOutputFormatDescription;
^{opaqueCMFormatDescription=} _inferenceInputFormatDescription;
^{opaqueCMFormatDescription=} _demosaicedRawFormatDescription;
^{opaqueCMFormatDescription=} _smartStyleStillLinearImageFormatDescription;
^{opaqueCMFormatDescription=} _inferenceAttachedMediaFormatDescription;
^{opaqueCMFormatDescription=} _gainMapFormatDescription;
@"NSMutableArray" _requestQueue;
@"BWDeepFusionProcessorRequest" _currentRequest;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWDeepFusionProcessorController initialize];
```

## Instance methods

```
-[BWDeepFusionProcessorController processor:didSelectFusionMode:];
-[BWDeepFusionProcessorController dealloc];
-[BWDeepFusionProcessorController initWithConfiguration:];
-[BWDeepFusionProcessorController type];
-[BWDeepFusionProcessorController metalImageBufferProcessor];
-[BWDeepFusionProcessorController cancelProcessing];
-[BWDeepFusionProcessorController addInferencesForInput:];
-[BWDeepFusionProcessorController beginProcessingCachedBuffersForInput:];
-[BWDeepFusionProcessorController enqueueInputForProcessing:delegate:];
-[BWDeepFusionProcessorController externalMemoryDescriptor];
-[BWDeepFusionProcessorController input:addInputBuffer:];
-[BWDeepFusionProcessorController processor:outputReadyWithBufferType:outputPixelBuffer:outputMetadata:error:];
-[BWDeepFusionProcessorController processorGetInferenceResults:inferenceInputBufferType:];
```
