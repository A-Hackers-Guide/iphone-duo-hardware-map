# `BWDisparityPostProcessingInferenceProvider`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWInferenceProvider`, `BWInferenceCacheable`, `BWInferenceSubmittable`, `BWInferencePropagatable`
- 20 instance variables, 22 properties, 27 instance methods, 1 class methods

## Instance variables

```
@"NSString" _customInferenceIdentifier;
@"BWInferenceVideoRequirement" _displacementInputRequirement;
@"BWInferenceVideoRequirement" _disparityInputRequirement;
@"BWInferenceVideoRequirement" _disparityOutputRequirement;
@"BWInferenceVideoRequirement" _stateInputRequirement;
@"BWInferenceVideoRequirement" _stateOutputRequirement;
@"PTDisparityPostProcessing" _disparityPostProcessor;
@"BWMetalInferenceContext" _metalInferenceContext;
@"MTLTextureDescriptor" _disparityInputDescriptor;
@"MTLTextureDescriptor" _disparityOutputDescriptor;
@"MTLTextureDescriptor" _displacementDescriptor;
@"MTLTextureDescriptor" _stateInDescriptor;
@"MTLTextureDescriptor" _stateOutDescriptor;
^{opaqueCMFormatDescription=} _outputFormatDescription;
@"NSString" _portType;
Q _concurrencyWidth;
B _appliesValidBufferRectPadding;
@"<MTLComputePipelineState>" _depthPaddingPipelineState;
@"BWPixelBufferPool" _unpaddedDisparityPool;
@"MTLTextureDescriptor" _unpaddedDisparityDescriptor;
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
+[BWDisparityPostProcessingInferenceProvider initialize];
```

## Instance methods

```
-[BWDisparityPostProcessingInferenceProvider cacheable];
-[BWDisparityPostProcessingInferenceProvider submitForSampleBuffer:usingStorage:withSubmissionTime:workQueue:completionHandler:];
-[BWDisparityPostProcessingInferenceProvider extractable];
-[BWDisparityPostProcessingInferenceProvider outputVideoRequirements];
-[BWDisparityPostProcessingInferenceProvider prewarmUsingLimitedMemory:];
-[BWDisparityPostProcessingInferenceProvider allowsAsyncPropagation];
-[BWDisparityPostProcessingInferenceProvider dealloc];
-[BWDisparityPostProcessingInferenceProvider reconcileWithPlaceholderProvider:];
-[BWDisparityPostProcessingInferenceProvider setCustomInferenceIdentifier:];
-[BWDisparityPostProcessingInferenceProvider cloneVideoRequirements];
-[BWDisparityPostProcessingInferenceProvider allowedPixelBufferCompressionDirection];
-[BWDisparityPostProcessingInferenceProvider executionTarget];
-[BWDisparityPostProcessingInferenceProvider preventionReasons];
-[BWDisparityPostProcessingInferenceProvider type];
-[BWDisparityPostProcessingInferenceProvider executable];
-[BWDisparityPostProcessingInferenceProvider outputMetadataRequirements];
-[BWDisparityPostProcessingInferenceProvider newStorage];
-[BWDisparityPostProcessingInferenceProvider propagatable];
-[BWDisparityPostProcessingInferenceProvider submittable];
-[BWDisparityPostProcessingInferenceProvider sharedResourcePreparator];
-[BWDisparityPostProcessingInferenceProvider prepareForSubmissionWithWorkQueue:];
-[BWDisparityPostProcessingInferenceProvider propagateInferenceResultsToInferenceDictionary:usingStorage:inputSampleBuffer:propagationSampleBuffer:];
-[BWDisparityPostProcessingInferenceProvider customInferenceIdentifier];
-[BWDisparityPostProcessingInferenceProvider initWithDisparityInputRequirement:displacementInputRequirement:stateInputRequirement:stateOutputRequirement:disparityOutputRequirement:resourceProvider:configuration:];
-[BWDisparityPostProcessingInferenceProvider inputMetadataRequirements];
-[BWDisparityPostProcessingInferenceProvider inputVideoRequirements];
-[BWDisparityPostProcessingInferenceProvider prewarmingSharedResourceType];
```
