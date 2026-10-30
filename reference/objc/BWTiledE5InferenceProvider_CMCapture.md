# `BWTiledE5InferenceProvider`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWInferenceProvider`, `BWInferenceSubmittable`, `BWInferencePropagatable`, `BWInferenceCacheable`, `BWInferenceSharedResourcePreparatory`, `BWInferenceSharedResourcePrewarmer`
- 16 instance variables, 23 properties, 41 instance methods, 1 class methods

## Instance variables

```
@"NSString" _customInferenceIdentifier;
@"BWTiledEspressoInferenceConfiguration" _configuration;
@"<BWInferenceResourceProvider>" _resourceProvider;
@"NSMutableArray" _commandQueues;
@"NSArray" _inputVideoRequirements;
@"NSArray" _outputVideoRequirements;
@"NSMutableDictionary" _tileInputBindingNamesByLane;
@"NSMutableDictionary" _tileOutputBindingNamesByLane;
@"NSMutableDictionary" _tileInputVideoRequirementsByLane;
@"NSMutableDictionary" _tileOutputVideoRequirementsByLane;
@"NSArray" _additionalVideoRequirements;
_maxTileCount;
@"NSMutableArray" _espressoProviders;
i _bufferingLaneCount;
i _sharedResourceType;
@"<BWInferenceSharedResourcePreparatory>" _sharedResourcePreparatory;
```

## Properties

```
@property (Ti,R,N) executionTarget;
@property (T@"NSSet",R,C,N) preventionReasons;
@property (T@"NSArray",R,N) inputVideoRequirements;
@property (T@"NSArray",R,N) outputVideoRequirements;
@property (T@"NSArray",R,N) cloneVideoRequirements;
@property (T@"NSArray",R,N) inputMetadataRequirements;
@property (T@"NSArray",R,N) outputMetadataRequirements;
@property (TI,R,N) allowedPixelBufferCompressionDirection;
@property (Ti,R,N) prewarmingSharedResourceType;
@property (T@"NSString",&,N) customInferenceIdentifier;
@property (Ti,R,N) type;
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
@property (TB,R,N) allowsAsyncPropagation;
@property (Ti,R,N) sharedResourceType;
```

## Class methods

```
+[BWTiledE5InferenceProvider initialize];
```

## Instance methods

```
-[BWTiledE5InferenceProvider prepareForSubmissionWithWorkQueue:sharedANEMemoryProvider:];
-[BWTiledE5InferenceProvider prepareForExecutionWithSharedANEMemoryProvider:];
-[BWTiledE5InferenceProvider cacheable];
-[BWTiledE5InferenceProvider submitForSampleBuffer:usingStorage:withSubmissionTime:workQueue:completionHandler:];
-[BWTiledE5InferenceProvider createInputTiles:withInputs:tileInputInfo:tileOutputInfo:];
-[BWTiledE5InferenceProvider writeOutputFor:to:fromNetworkOutputTiles:withAdditionalPixelBuffers:withInputTilePixelBuffers:withInputFullPixelBuffers:tileInputInfo:tileOutputInfo:];
-[BWTiledE5InferenceProvider extractable];
-[BWTiledE5InferenceProvider outputVideoRequirements];
-[BWTiledE5InferenceProvider prewarmUsingLimitedMemory:];
-[BWTiledE5InferenceProvider allowsAsyncPropagation];
-[BWTiledE5InferenceProvider dealloc];
-[BWTiledE5InferenceProvider reconcileWithPlaceholderProvider:];
-[BWTiledE5InferenceProvider sharedResourceType];
-[BWTiledE5InferenceProvider setCustomInferenceIdentifier:];
-[BWTiledE5InferenceProvider cloneVideoRequirements];
-[BWTiledE5InferenceProvider allowedPixelBufferCompressionDirection];
-[BWTiledE5InferenceProvider executionTarget];
-[BWTiledE5InferenceProvider preventionReasons];
-[BWTiledE5InferenceProvider type];
-[BWTiledE5InferenceProvider executable];
-[BWTiledE5InferenceProvider prewarmUsingLimitedMemory:sharedE5ANEMemoryProvider:];
-[BWTiledE5InferenceProvider purgeIntermediateResources];
-[BWTiledE5InferenceProvider outputMetadataRequirements];
-[BWTiledE5InferenceProvider newStorage];
-[BWTiledE5InferenceProvider propagatable];
-[BWTiledE5InferenceProvider submittable];
-[BWTiledE5InferenceProvider preProcessOutputBuffer:forMediaKey:];
-[BWTiledE5InferenceProvider sharedResourcePreparator];
-[BWTiledE5InferenceProvider prepareForSubmissionWithWorkQueue:];
-[BWTiledE5InferenceProvider propagateInferenceResultsToInferenceDictionary:usingStorage:inputSampleBuffer:propagationSampleBuffer:];
-[BWTiledE5InferenceProvider customInferenceIdentifier];
-[BWTiledE5InferenceProvider inputMetadataRequirements];
-[BWTiledE5InferenceProvider inputVideoRequirements];
-[BWTiledE5InferenceProvider propagateInferenceResultForOutputRequirement:storage:propagationSampleBuffer:];
-[BWTiledE5InferenceProvider prewarmingSharedResourceType];
-[BWTiledE5InferenceProvider initWithConfiguration:inputVideoRequirements:outputVideoRequirements:resourceProvider:];
-[BWTiledE5InferenceProvider migrateInputVideoRequirements:outputVideoRequirements:];
-[BWTiledE5InferenceProvider outputRequirementsToProduceForInputSampleBuffer:];
-[BWTiledE5InferenceProvider setupNetworkWithURL:configName:inferenceType:maxTileCount:inputFormatsByBindingName:outputFormatsByBindingName:additionalVideoRequirements:];
-[BWTiledE5InferenceProvider submitForSampleBuffer:usingStorage:withSubmissionTime:workQueue:completionHandler:currentTileCount:];
-[BWTiledE5InferenceProvider updateMaxTileCount:];
```
