# `BWDisparityFilteringInferenceProvider`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWInferenceProvider`, `BWInferenceCacheable`, `BWInferenceSubmittable`, `BWInferencePropagatable`
- 16 instance variables, 22 properties, 27 instance methods, 1 class methods

## Instance variables

```
@"NSString" _customInferenceIdentifier;
@"BWInferenceVideoRequirement" _disparityInputRequirement;
@"BWInferenceVideoRequirement" _outputRequirement;
@"ADPCEDisparityColorPipeline" _stereoPipeline;
^{opaqueCMFormatDescription=} _outputFormatDescription;
@"BWMetalInferenceContext" _metalInferenceContext;
@"<MTLComputePipelineState>" _cropPipelineState;
@"MTLTextureDescriptor" _disparityInputDescriptor;
@"MTLTextureDescriptor" _disparityOutputDescriptor;
q _requestedRotation;
Q _inputSource;
Q _concurrencyWidth;
B _isPreProcessing;
@"<MTLTexture>" _disparitySourceTextureCroppedUpscaledAndMirrored;
B _requiresCroppingOfDepthBuffer;
B _requiresVerticalFlipOfDepthBuffer;
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
+[BWDisparityFilteringInferenceProvider initialize];
```

## Instance methods

```
-[BWDisparityFilteringInferenceProvider cacheable];
-[BWDisparityFilteringInferenceProvider submitForSampleBuffer:usingStorage:withSubmissionTime:workQueue:completionHandler:];
-[BWDisparityFilteringInferenceProvider extractable];
-[BWDisparityFilteringInferenceProvider initWithDisparityInputRequirement:disparityOutputRequirement:resourceProvider:configuration:isPreprocessing:];
-[BWDisparityFilteringInferenceProvider outputVideoRequirements];
-[BWDisparityFilteringInferenceProvider prewarmUsingLimitedMemory:];
-[BWDisparityFilteringInferenceProvider allowsAsyncPropagation];
-[BWDisparityFilteringInferenceProvider dealloc];
-[BWDisparityFilteringInferenceProvider reconcileWithPlaceholderProvider:];
-[BWDisparityFilteringInferenceProvider setCustomInferenceIdentifier:];
-[BWDisparityFilteringInferenceProvider cloneVideoRequirements];
-[BWDisparityFilteringInferenceProvider allowedPixelBufferCompressionDirection];
-[BWDisparityFilteringInferenceProvider executionTarget];
-[BWDisparityFilteringInferenceProvider preventionReasons];
-[BWDisparityFilteringInferenceProvider type];
-[BWDisparityFilteringInferenceProvider executable];
-[BWDisparityFilteringInferenceProvider outputMetadataRequirements];
-[BWDisparityFilteringInferenceProvider newStorage];
-[BWDisparityFilteringInferenceProvider propagatable];
-[BWDisparityFilteringInferenceProvider submittable];
-[BWDisparityFilteringInferenceProvider sharedResourcePreparator];
-[BWDisparityFilteringInferenceProvider prepareForSubmissionWithWorkQueue:];
-[BWDisparityFilteringInferenceProvider propagateInferenceResultsToInferenceDictionary:usingStorage:inputSampleBuffer:propagationSampleBuffer:];
-[BWDisparityFilteringInferenceProvider customInferenceIdentifier];
-[BWDisparityFilteringInferenceProvider inputMetadataRequirements];
-[BWDisparityFilteringInferenceProvider inputVideoRequirements];
-[BWDisparityFilteringInferenceProvider prewarmingSharedResourceType];
```
