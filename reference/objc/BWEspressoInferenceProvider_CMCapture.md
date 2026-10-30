# `BWEspressoInferenceProvider`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWInferenceProvider`, `BWInferenceCacheable`, `BWInferenceExecutable`, `BWInferenceSubmittable`, `BWEspressoInferenceBinding`, `BWEspressoInferencePropagatable`
- 23 instance variables, 22 properties, 40 instance methods, 1 class methods

## Instance variables

```
@"NSString" _customInferenceIdentifier;
i _type;
i _executionTarget;
@"NSSet" _preventionReasons;
I _allowedCompressionDirection;
Q _concurrentSubmissionLimit;
@"NSURL" _networkURL;
@"NSString" _networkConfiguration;
@"NSString" _espressoNetworkVersion;
@"BWEspressoInferenceContext" _context;
^v _espressoPlan;
{?="plan"^v"network_index"i} _espressoNetwork;
i _espressoPriority;
@"NSMutableDictionary" _bindingNamesByRequirement;
@"NSMutableArray" _inputVideoRequirements;
@"NSMutableArray" _outputVideoRequirements;
@"NSMutableArray" _cloneVideoRequirements;
@"NSMutableArray" _inputMetadataRequirements;
@"NSMutableArray" _outputMetadataRequirements;
@"<BWInferencePropagatable>" _propagator;
@"<BWEspressoInferenceTensorMemoryProvider>" _tensorMemoryProvider;
B _updateMetadataWithCropRect;
@"NSMutableArray" _pixelBuffersLockedDuringExecution;
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
@property (T@"<BWEspressoInferenceTensorMemoryProvider>",&,N) tensorMemoryProvider;
```

## Class methods

```
+[BWEspressoInferenceProvider initialize];
```

## Instance methods

```
-[BWEspressoInferenceProvider cacheable];
-[BWEspressoInferenceProvider bindEspressoOutput:asAttachedMediaUsingKey:withVideoFormat:count:];
-[BWEspressoInferenceProvider prepareForExecution];
-[BWEspressoInferenceProvider bindEspressoInput:fromAttachedMediaUsingKey:withVideoFormat:];
-[BWEspressoInferenceProvider bindEspressoOutput:asAttachedMediaUsingKey:withVideoFormat:];
-[BWEspressoInferenceProvider submitForSampleBuffer:usingStorage:withSubmissionTime:workQueue:completionHandler:];
-[BWEspressoInferenceProvider bindEspressoInput:fromAttachedMediaUsingKey:withVideoFormat:count:];
-[BWEspressoInferenceProvider bindEspressoOutput:asMetadataUsingKey:];
-[BWEspressoInferenceProvider setPropagatable:];
-[BWEspressoInferenceProvider extractable];
-[BWEspressoInferenceProvider bindEspressoOutput:asConsolidatedMetadataUsingKeys:];
-[BWEspressoInferenceProvider executeOnSampleBuffer:usingStorage:withExecutionTime:completionHandler:];
-[BWEspressoInferenceProvider bindEspressoOutput:asMetadataUsingKeys:];
-[BWEspressoInferenceProvider tensorMemoryProvider];
-[BWEspressoInferenceProvider bindEspressoInput:fromMetadataUsingKeys:];
-[BWEspressoInferenceProvider setTensorMemoryProvider:];
-[BWEspressoInferenceProvider outputVideoRequirements];
-[BWEspressoInferenceProvider prewarmUsingLimitedMemory:];
-[BWEspressoInferenceProvider dealloc];
-[BWEspressoInferenceProvider reconcileWithPlaceholderProvider:];
-[BWEspressoInferenceProvider bindOutputByCloningInputRequirement:toAttachedMediaUsingKey:];
-[BWEspressoInferenceProvider setCustomInferenceIdentifier:];
-[BWEspressoInferenceProvider cloneVideoRequirements];
-[BWEspressoInferenceProvider allowedPixelBufferCompressionDirection];
-[BWEspressoInferenceProvider executionTarget];
-[BWEspressoInferenceProvider preventionReasons];
-[BWEspressoInferenceProvider initWithType:networkURL:networkConfiguration:context:executionTarget:schedulerPriority:preventionReasons:resourceProvider:allowedCompressionDirection:concurrentSubmissionLimit:updateMetadataWithCropRect:];
-[BWEspressoInferenceProvider type];
-[BWEspressoInferenceProvider executable];
-[BWEspressoInferenceProvider outputMetadataRequirements];
-[BWEspressoInferenceProvider newStorage];
-[BWEspressoInferenceProvider description];
-[BWEspressoInferenceProvider propagatable];
-[BWEspressoInferenceProvider submittable];
-[BWEspressoInferenceProvider sharedResourcePreparator];
-[BWEspressoInferenceProvider prepareForSubmissionWithWorkQueue:];
-[BWEspressoInferenceProvider customInferenceIdentifier];
-[BWEspressoInferenceProvider inputMetadataRequirements];
-[BWEspressoInferenceProvider inputVideoRequirements];
-[BWEspressoInferenceProvider prewarmingSharedResourceType];
```
