# `BWE5MultipleLayoutInferenceProvider`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWInferenceProvider`, `BWInferenceCacheable`, `BWInferenceExecutable`, `BWEspressoInferenceBinding`, `BWEspressoInferencePropagatable`, `BWInferenceSharedResourcePreparatory`, `BWInferenceSharedResourcePrewarmer`
- 23 instance variables, 23 properties, 42 instance methods, 1 class methods

## Instance variables

```
@"NSString" _customInferenceIdentifier;
@"NSURL" _networkURL;
@"NSMutableDictionary" _networkConfigurationsByLayout;
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
[2^{e5rt_execution_stream_operation}] _operationsByNetworkLayout;
I _defaultLayout;
^{OpaqueVTPixelRotationSession=} _rotationSession;
^{e5rt_execution_stream=} _stream;
i _sharedResourceType;
@"<BWInferenceSharedResourcePreparatory>" _sharedResourcePreparatory;
i _type;
```

## Properties

```
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
@property (T@"<BWEspressoInferenceTensorMemoryProvider>",&,N,V_tensorMemoryProvider) tensorMemoryProvider;
@property (Ti,R,N) sharedResourceType;
```

## Class methods

```
+[BWE5MultipleLayoutInferenceProvider initialize];
```

## Instance methods

```
-[BWE5MultipleLayoutInferenceProvider prepareForSubmissionWithWorkQueue:sharedANEMemoryProvider:];
-[BWE5MultipleLayoutInferenceProvider prepareForExecutionWithSharedANEMemoryProvider:];
-[BWE5MultipleLayoutInferenceProvider cacheable];
-[BWE5MultipleLayoutInferenceProvider bindEspressoOutput:asAttachedMediaUsingKey:withVideoFormat:count:];
-[BWE5MultipleLayoutInferenceProvider prepareForExecution];
-[BWE5MultipleLayoutInferenceProvider bindEspressoInput:fromAttachedMediaUsingKey:withVideoFormat:];
-[BWE5MultipleLayoutInferenceProvider bindEspressoOutput:asAttachedMediaUsingKey:withVideoFormat:];
-[BWE5MultipleLayoutInferenceProvider bindEspressoInput:fromAttachedMediaUsingKey:withVideoFormat:count:];
-[BWE5MultipleLayoutInferenceProvider bindEspressoOutput:asMetadataUsingKey:];
-[BWE5MultipleLayoutInferenceProvider setPropagatable:];
-[BWE5MultipleLayoutInferenceProvider extractable];
-[BWE5MultipleLayoutInferenceProvider bindEspressoOutput:asConsolidatedMetadataUsingKeys:];
-[BWE5MultipleLayoutInferenceProvider executeOnSampleBuffer:usingStorage:withExecutionTime:completionHandler:];
-[BWE5MultipleLayoutInferenceProvider bindEspressoOutput:asMetadataUsingKeys:];
-[BWE5MultipleLayoutInferenceProvider tensorMemoryProvider];
-[BWE5MultipleLayoutInferenceProvider bindEspressoInput:fromMetadataUsingKeys:];
-[BWE5MultipleLayoutInferenceProvider setTensorMemoryProvider:];
-[BWE5MultipleLayoutInferenceProvider outputVideoRequirements];
-[BWE5MultipleLayoutInferenceProvider prewarmUsingLimitedMemory:];
-[BWE5MultipleLayoutInferenceProvider dealloc];
-[BWE5MultipleLayoutInferenceProvider reconcileWithPlaceholderProvider:];
-[BWE5MultipleLayoutInferenceProvider bindOutputByCloningInputRequirement:toAttachedMediaUsingKey:];
-[BWE5MultipleLayoutInferenceProvider sharedResourceType];
-[BWE5MultipleLayoutInferenceProvider setCustomInferenceIdentifier:];
-[BWE5MultipleLayoutInferenceProvider cloneVideoRequirements];
-[BWE5MultipleLayoutInferenceProvider allowedPixelBufferCompressionDirection];
-[BWE5MultipleLayoutInferenceProvider executionTarget];
-[BWE5MultipleLayoutInferenceProvider preventionReasons];
-[BWE5MultipleLayoutInferenceProvider type];
-[BWE5MultipleLayoutInferenceProvider executable];
-[BWE5MultipleLayoutInferenceProvider prewarmUsingLimitedMemory:sharedE5ANEMemoryProvider:];
-[BWE5MultipleLayoutInferenceProvider outputMetadataRequirements];
-[BWE5MultipleLayoutInferenceProvider newStorage];
-[BWE5MultipleLayoutInferenceProvider description];
-[BWE5MultipleLayoutInferenceProvider propagatable];
-[BWE5MultipleLayoutInferenceProvider submittable];
-[BWE5MultipleLayoutInferenceProvider sharedResourcePreparator];
-[BWE5MultipleLayoutInferenceProvider customInferenceIdentifier];
-[BWE5MultipleLayoutInferenceProvider inputMetadataRequirements];
-[BWE5MultipleLayoutInferenceProvider inputVideoRequirements];
-[BWE5MultipleLayoutInferenceProvider prewarmingSharedResourceType];
-[BWE5MultipleLayoutInferenceProvider initWithType:networkURL:networkConfigurationsByLayout:defaultLayout:executionTarget:schedulerPriority:preventionReasons:allowedCompressionDirection:updateMetadataWithCropRect:];
```
