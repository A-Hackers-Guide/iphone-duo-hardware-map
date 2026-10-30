# `BWVideoProcessingImageEmbeddingInferenceProvider`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWInferenceProvider`, `BWInferenceCacheable`, `BWInferenceExecutable`, `BWInferencePropagatable`
- 10 instance variables, 22 properties, 29 instance methods, 1 class methods

## Instance variables

```
@"NSString" _customInferenceIdentifier;
i _type;
i _executionTarget;
@"NSSet" _preventionReasons;
@"NSMutableArray" _inputVideoRequirements;
@"NSMutableArray" _outputVideoRequirements;
@"NSMutableArray" _cloneVideoRequirements;
@"NSMutableArray" _inputMetadataRequirements;
@"NSMutableArray" _outputMetadataRequirements;
@"VCPImageEmbeddingRequest" _imageEmbeddingRequest;
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
@property (TI,R,N) allowedPixelBufferCompressionDirection;
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
@property (TB,R,N) allowsAsyncPropagation;
```

## Class methods

```
+[BWVideoProcessingImageEmbeddingInferenceProvider initialize];
```

## Instance methods

```
-[BWVideoProcessingImageEmbeddingInferenceProvider cacheable];
-[BWVideoProcessingImageEmbeddingInferenceProvider prepareForExecution];
-[BWVideoProcessingImageEmbeddingInferenceProvider extractable];
-[BWVideoProcessingImageEmbeddingInferenceProvider executeOnSampleBuffer:usingStorage:withExecutionTime:completionHandler:];
-[BWVideoProcessingImageEmbeddingInferenceProvider outputVideoRequirements];
-[BWVideoProcessingImageEmbeddingInferenceProvider prewarmUsingLimitedMemory:];
-[BWVideoProcessingImageEmbeddingInferenceProvider allowsAsyncPropagation];
-[BWVideoProcessingImageEmbeddingInferenceProvider dealloc];
-[BWVideoProcessingImageEmbeddingInferenceProvider reconcileWithPlaceholderProvider:];
-[BWVideoProcessingImageEmbeddingInferenceProvider setCustomInferenceIdentifier:];
-[BWVideoProcessingImageEmbeddingInferenceProvider cloneVideoRequirements];
-[BWVideoProcessingImageEmbeddingInferenceProvider allowedPixelBufferCompressionDirection];
-[BWVideoProcessingImageEmbeddingInferenceProvider executionTarget];
-[BWVideoProcessingImageEmbeddingInferenceProvider preventionReasons];
-[BWVideoProcessingImageEmbeddingInferenceProvider type];
-[BWVideoProcessingImageEmbeddingInferenceProvider executable];
-[BWVideoProcessingImageEmbeddingInferenceProvider outputMetadataRequirements];
-[BWVideoProcessingImageEmbeddingInferenceProvider newStorage];
-[BWVideoProcessingImageEmbeddingInferenceProvider propagatable];
-[BWVideoProcessingImageEmbeddingInferenceProvider submittable];
-[BWVideoProcessingImageEmbeddingInferenceProvider sharedResourcePreparator];
-[BWVideoProcessingImageEmbeddingInferenceProvider bindOutputMetadataKeys:];
-[BWVideoProcessingImageEmbeddingInferenceProvider propagateInferenceResultsToInferenceDictionary:usingStorage:inputSampleBuffer:propagationSampleBuffer:];
-[BWVideoProcessingImageEmbeddingInferenceProvider customInferenceIdentifier];
-[BWVideoProcessingImageEmbeddingInferenceProvider inputMetadataRequirements];
-[BWVideoProcessingImageEmbeddingInferenceProvider inputVideoRequirements];
-[BWVideoProcessingImageEmbeddingInferenceProvider prewarmingSharedResourceType];
-[BWVideoProcessingImageEmbeddingInferenceProvider bindVideoInput:fromAttachedMediaUsingKey:withVideoFormat:];
-[BWVideoProcessingImageEmbeddingInferenceProvider initWithType:executionTarget:schedulerPriority:preventionReasons:resourceProvider:];
```
