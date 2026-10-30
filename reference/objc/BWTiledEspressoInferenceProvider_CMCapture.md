# `BWTiledEspressoInferenceProvider`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWInferenceProvider`, `BWInferenceSubmittable`, `BWInferencePropagatable`, `BWInferenceCacheable`
- 14 instance variables, 22 properties, 37 instance methods, 1 class methods

## Instance variables

```
@"NSString" _customInferenceIdentifier;
@"NSArray" _inputVideoRequirements;
@"NSArray" _outputVideoRequirements;
@"NSArray" _tileInputVideoRequirements;
@"NSArray" _tileInputBindingNames;
@"NSArray" _tileOutputVideoRequirements;
@"NSArray" _tileOutputBindingNames;
@"NSArray" _additionalVideoRequirements;
_maxTileCount;
@"BWEspressoInferenceProvider" _espressoProvider;
@"NSObject<OS_dispatch_queue>" _espressoWorkQueue;
@"BWTiledEspressoInferenceConfiguration" _configuration;
@"<BWInferenceResourceProvider>" _resourceProvider;
C _multipleBufferingLanes;
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
```

## Class methods

```
+[BWTiledEspressoInferenceProvider initialize];
```

## Instance methods

```
-[BWTiledEspressoInferenceProvider cacheable];
-[BWTiledEspressoInferenceProvider submitForSampleBuffer:usingStorage:withSubmissionTime:workQueue:completionHandler:];
-[BWTiledEspressoInferenceProvider extractable];
-[BWTiledEspressoInferenceProvider outputVideoRequirements];
-[BWTiledEspressoInferenceProvider prewarmUsingLimitedMemory:];
-[BWTiledEspressoInferenceProvider allowsAsyncPropagation];
-[BWTiledEspressoInferenceProvider dealloc];
-[BWTiledEspressoInferenceProvider reconcileWithPlaceholderProvider:];
-[BWTiledEspressoInferenceProvider setCustomInferenceIdentifier:];
-[BWTiledEspressoInferenceProvider cloneVideoRequirements];
-[BWTiledEspressoInferenceProvider allowedPixelBufferCompressionDirection];
-[BWTiledEspressoInferenceProvider executionTarget];
-[BWTiledEspressoInferenceProvider preventionReasons];
-[BWTiledEspressoInferenceProvider type];
-[BWTiledEspressoInferenceProvider executable];
-[BWTiledEspressoInferenceProvider purgeIntermediateResources];
-[BWTiledEspressoInferenceProvider outputMetadataRequirements];
-[BWTiledEspressoInferenceProvider newStorage];
-[BWTiledEspressoInferenceProvider propagatable];
-[BWTiledEspressoInferenceProvider submittable];
-[BWTiledEspressoInferenceProvider preProcessOutputBuffer:forMediaKey:];
-[BWTiledEspressoInferenceProvider sharedResourcePreparator];
-[BWTiledEspressoInferenceProvider prepareForSubmissionWithWorkQueue:];
-[BWTiledEspressoInferenceProvider propagateInferenceResultsToInferenceDictionary:usingStorage:inputSampleBuffer:propagationSampleBuffer:];
-[BWTiledEspressoInferenceProvider customInferenceIdentifier];
-[BWTiledEspressoInferenceProvider inputMetadataRequirements];
-[BWTiledEspressoInferenceProvider inputVideoRequirements];
-[BWTiledEspressoInferenceProvider propagateInferenceResultForOutputRequirement:storage:propagationSampleBuffer:];
-[BWTiledEspressoInferenceProvider prewarmingSharedResourceType];
-[BWTiledEspressoInferenceProvider createInputTiles:withInputs:atPosition:cmdBuffer:];
-[BWTiledEspressoInferenceProvider initWithConfiguration:inputVideoRequirements:outputVideoRequirements:resourceProvider:];
-[BWTiledEspressoInferenceProvider loadNetworkWithURL:configName:inferenceType:maxTileCount:inputFormatsByBindingName:outputFormatsByBindingName:additionalVideoRequirements:];
-[BWTiledEspressoInferenceProvider migrateInputVideoRequirements:outputVideoRequirements:];
-[BWTiledEspressoInferenceProvider outputRequirementsToProduceForInputSampleBuffer:];
-[BWTiledEspressoInferenceProvider submitForSampleBuffer:usingStorage:withSubmissionTime:workQueue:completionHandler:currentTileCount:];
-[BWTiledEspressoInferenceProvider updateMaxTileCount:];
-[BWTiledEspressoInferenceProvider writeOutputFor:to:fromNetworkOutputTiles:withAdditionalPixelBuffers:withInputTilePixelBuffers:withInputFullPixelBuffers:atPosition:cmdBuffer:];
```
