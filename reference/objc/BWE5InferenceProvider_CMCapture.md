# `BWE5InferenceProvider`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWInferenceProvider`, `BWInferenceCacheable`, `BWInferenceExecutable`, `BWInferenceSubmittable`, `BWInferenceSharedResourcePreparatory`, `BWEspressoInferenceBinding`, `BWEspressoInferencePropagatable`, `BWInferenceSharedResourcePrewarmer`
- 31 instance variables, 25 properties, 53 instance methods, 1 class methods

## Instance variables

```
@"NSString" _customInferenceIdentifier;
@"NSURL" _networkURL;
@"NSString" _networkConfiguration;
i _executionTarget;
@"NSSet" _preventionReasons;
I _allowedCompressionDirection;
i _anePriority;
@"<BWInferencePropagatable>" _propagator;
@"<BWEspressoInferenceTensorMemoryProvider>" _tensorMemoryProvider;
B _updateMetadataWithCropRect;
@"NSMutableDictionary" _bindingNamesByRequirement;
@"NSMutableArray" _inputVideoRequirements;
@"NSMutableArray" _outputVideoRequirements;
@"NSMutableArray" _cloneVideoRequirements;
@"NSMutableArray" _inputMetadataRequirements;
@"NSMutableArray" _outputMetadataRequirements;
^{e5rt_execution_stream_operation=} _operation;
B _portraitOrientationSupportEnabled;
^{OpaqueVTPixelRotationSession=} _rotationSession;
^{e5rt_execution_stream=} _stream;
i _sharedResourceType;
@"<BWInferenceSharedResourcePreparatory>" _sharedResourcePreparatory;
B _submissionsUsingLowLatencySynchronizationEnabled;
@"<MTLSharedEventSPI>" _mtlSharedEvent;
AQ _mtlSharedEventValue;
^{e5rt_async_event=} _dependencyE5RTEvent;
^{e5rt_async_event=} _completionE5RTEvent;
d _tileE5RTInferenceStartTime;
I _anefProcedureVariantHintOverride;
I _anefIntermediateBufferSizeMultiplierHint;
i _type;
```

## Properties

```
@property (TB,N,V_portraitOrientationSupportEnabled) portraitOrientationSupportEnabled;
@property (TI,N,V_anefIntermediateBufferSizeMultiplierHint) anefIntermediateBufferSizeMultiplierHint;
@property (Ti,R,N,V_executionTarget) executionTarget;
@property (T@"NSSet",R,C,N,V_preventionReasons) preventionReasons;
@property (T@"NSArray",R,N,V_inputVideoRequirements) inputVideoRequirements;
@property (T@"NSArray",R,N,V_outputVideoRequirements) outputVideoRequirements;
@property (T@"NSArray",R,N,V_cloneVideoRequirements) cloneVideoRequirements;
@property (T@"NSArray",R,N,V_inputMetadataRequirements) inputMetadataRequirements;
@property (T@"NSArray",R,N,V_outputMetadataRequirements) outputMetadataRequirements;
@property (TI,R,N,V_allowedCompressionDirection) allowedPixelBufferCompressionDirection;
@property (Ti,R,N) prewarmingSharedResourceType;
@property (T@"NSString",&,N) customInferenceIdentifier;
@property (Ti,R,N,V_type) type;
@property (T@"<BWInferenceCacheable>",R,N) cacheable;
@property (T@"<BWInferenceExecutable>",R,N) executable;
@property (T@"<BWInferenceSubmittable>",R,N) submittable;
@property (T@"<BWInferenceSharedResourcePreparatory>",R,N) sharedResourcePreparator;
@property (T@"<BWInferenceExtractable>",R,N) extractable;
@property (T@"<BWInferencePropagatable>",R,N) propagatable;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Ti,R,N) sharedResourceType;
@property (T@"<BWEspressoInferenceTensorMemoryProvider>",&,N,V_tensorMemoryProvider) tensorMemoryProvider;
```

## Class methods

```
+[BWE5InferenceProvider initialize];
```

## Instance methods

```
-[BWE5InferenceProvider prepareForSubmissionWithWorkQueue:sharedANEMemoryProvider:];
-[BWE5InferenceProvider prepareForExecutionWithSharedANEMemoryProvider:];
-[BWE5InferenceProvider cacheable];
-[BWE5InferenceProvider bindEspressoOutput:asAttachedMediaUsingKey:withVideoFormat:count:];
-[BWE5InferenceProvider prepareForExecution];
-[BWE5InferenceProvider bindEspressoInput:fromAttachedMediaUsingKey:withVideoFormat:];
-[BWE5InferenceProvider bindEspressoOutput:asAttachedMediaUsingKey:withVideoFormat:];
-[BWE5InferenceProvider submitForSampleBuffer:usingStorage:withSubmissionTime:workQueue:completionHandler:];
-[BWE5InferenceProvider bindEspressoInput:fromAttachedMediaUsingKey:withVideoFormat:count:];
-[BWE5InferenceProvider bindEspressoOutput:asMetadataUsingKey:];
-[BWE5InferenceProvider setPropagatable:];
-[BWE5InferenceProvider extractable];
-[BWE5InferenceProvider bindEspressoOutput:asConsolidatedMetadataUsingKeys:];
-[BWE5InferenceProvider executeOnSampleBuffer:usingStorage:withExecutionTime:completionHandler:];
-[BWE5InferenceProvider bindEspressoOutput:asMetadataUsingKeys:];
-[BWE5InferenceProvider tensorMemoryProvider];
-[BWE5InferenceProvider bindEspressoInput:fromMetadataUsingKeys:];
-[BWE5InferenceProvider setTensorMemoryProvider:];
-[BWE5InferenceProvider resetBindingsAndExecutionWithStorage:];
-[BWE5InferenceProvider outputVideoRequirements];
-[BWE5InferenceProvider initWithType:networkURL:networkConfiguration:context:executionTarget:schedulerPriority:preventionReasons:resourceProvider:allowedCompressionDirection:updateMetadataWithCropRect:anefProcedureVariantHintOverride:];
-[BWE5InferenceProvider prewarmUsingLimitedMemory:];
-[BWE5InferenceProvider portraitOrientationSupportEnabled];
-[BWE5InferenceProvider configureANEToWaitForCompletionOfCommandBuffer:];
-[BWE5InferenceProvider dealloc];
-[BWE5InferenceProvider reconcileWithPlaceholderProvider:];
-[BWE5InferenceProvider bindOutputByCloningInputRequirement:toAttachedMediaUsingKey:];
-[BWE5InferenceProvider sharedResourceType];
-[BWE5InferenceProvider setCustomInferenceIdentifier:];
-[BWE5InferenceProvider cloneVideoRequirements];
-[BWE5InferenceProvider allowedPixelBufferCompressionDirection];
-[BWE5InferenceProvider executionTarget];
-[BWE5InferenceProvider preventionReasons];
-[BWE5InferenceProvider anefIntermediateBufferSizeMultiplierHint];
-[BWE5InferenceProvider type];
-[BWE5InferenceProvider executable];
-[BWE5InferenceProvider prewarmUsingLimitedMemory:sharedE5ANEMemoryProvider:];
-[BWE5InferenceProvider outputMetadataRequirements];
-[BWE5InferenceProvider ensureBindingsAndEncodeOperationForExecutionWithStorage:];
-[BWE5InferenceProvider newStorage];
-[BWE5InferenceProvider description];
-[BWE5InferenceProvider propagatable];
-[BWE5InferenceProvider submittable];
-[BWE5InferenceProvider setPortraitOrientationSupportEnabled:];
-[BWE5InferenceProvider sharedResourcePreparator];
-[BWE5InferenceProvider setAnefIntermediateBufferSizeMultiplierHint:];
-[BWE5InferenceProvider prepareForSubmissionWithWorkQueue:];
-[BWE5InferenceProvider setupForSubmissionsUsingLowLatencySynchronizationWithMetalDevice:];
-[BWE5InferenceProvider customInferenceIdentifier];
-[BWE5InferenceProvider inputMetadataRequirements];
-[BWE5InferenceProvider inputVideoRequirements];
-[BWE5InferenceProvider configureCommandBufferToWaitForANECompletion:];
-[BWE5InferenceProvider prewarmingSharedResourceType];
```
