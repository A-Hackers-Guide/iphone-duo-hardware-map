# `BWMattingInferenceProvider`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWInferenceProvider`, `BWInferenceCacheable`, `BWInferenceExecutable`, `BWInferencePropagatable`, `BWMattingInferenceBinding`
- 13 instance variables, 28 properties, 42 instance methods, 1 class methods

## Instance variables

```
@"NSString" _customInferenceIdentifier;
@"BWInferenceVideoRequirement" _primaryFormatInputVideoRequirement;
@"BWInferenceVideoRequirement" _segmentationInputVideoRequirement;
@"BWInferenceVideoRequirement" _depthInputVideoRequirement;
@"BWInferenceVideoRequirement" _disparityInputVideoRequirement;
@"NSMutableArray" _inputVideoRequirements;
@"BWInferenceVideoRequirement" _segmentationOutputVideoRequirement;
@"BWInferenceVideoRequirement" _refinedDepthOutputVideoRequirement;
@"NSMutableArray" _outputVideoRequirements;
@"NSDictionary" _tuningParameters;
@"NSDictionary" _sdofRenderingTuningParameters;
@"FigMatting" _mattingProcessor;
@"<MTLCommandQueue>" _metalCommandQueue;
```

## Properties

```
@property (T@"BWInferenceVideoRequirement",&,N) primaryFormatInputVideoRequirement;
@property (T@"BWInferenceVideoRequirement",&,N) segmentationInputVideoRequirement;
@property (T@"BWInferenceVideoRequirement",&,N) depthInputVideoRequirement;
@property (T@"BWInferenceVideoRequirement",&,N,V_disparityInputVideoRequirement) disparityInputVideoRequirement;
@property (T@"BWInferenceVideoRequirement",&,N) segmentationOutputVideoRequirement;
@property (T@"BWInferenceVideoRequirement",&,N) refinedDepthOutputVideoRequirement;
@property (Ti,R,N) executionTarget;
@property (T@"NSSet",R,C,N) preventionReasons;
@property (T@"NSArray",R,N,V_inputVideoRequirements) inputVideoRequirements;
@property (T@"NSArray",R,N,V_outputVideoRequirements) outputVideoRequirements;
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
+[BWMattingInferenceProvider initialize];
```

## Instance methods

```
-[BWMattingInferenceProvider cacheable];
-[BWMattingInferenceProvider prepareForExecution];
-[BWMattingInferenceProvider primaryFormatInputVideoRequirement];
-[BWMattingInferenceProvider extractable];
-[BWMattingInferenceProvider segmentationInputVideoRequirement];
-[BWMattingInferenceProvider executeOnSampleBuffer:usingStorage:withExecutionTime:completionHandler:];
-[BWMattingInferenceProvider bindMattingOutput:fromAttachedMediaUsingKey:preparedByAttachedMediaKey:withVideoFormatProvider:];
-[BWMattingInferenceProvider outputVideoRequirements];
-[BWMattingInferenceProvider prewarmUsingLimitedMemory:];
-[BWMattingInferenceProvider setSegmentationInputVideoRequirement:];
-[BWMattingInferenceProvider segmentationOutputVideoRequirement];
-[BWMattingInferenceProvider allowsAsyncPropagation];
-[BWMattingInferenceProvider dealloc];
-[BWMattingInferenceProvider setDepthInputVideoRequirement:];
-[BWMattingInferenceProvider reconcileWithPlaceholderProvider:];
-[BWMattingInferenceProvider refinedDepthOutputVideoRequirement];
-[BWMattingInferenceProvider initWithConfiguration:];
-[BWMattingInferenceProvider setCustomInferenceIdentifier:];
-[BWMattingInferenceProvider cloneVideoRequirements];
-[BWMattingInferenceProvider disparityInputVideoRequirement];
-[BWMattingInferenceProvider allowedPixelBufferCompressionDirection];
-[BWMattingInferenceProvider setDisparityInputVideoRequirement:];
-[BWMattingInferenceProvider executionTarget];
-[BWMattingInferenceProvider preventionReasons];
-[BWMattingInferenceProvider type];
-[BWMattingInferenceProvider setRefinedDepthOutputVideoRequirement:];
-[BWMattingInferenceProvider setSegmentationOutputVideoRequirement:];
-[BWMattingInferenceProvider executable];
-[BWMattingInferenceProvider depthInputVideoRequirement];
-[BWMattingInferenceProvider setPrimaryFormatInputVideoRequirement:];
-[BWMattingInferenceProvider outputMetadataRequirements];
-[BWMattingInferenceProvider newStorage];
-[BWMattingInferenceProvider propagatable];
-[BWMattingInferenceProvider submittable];
-[BWMattingInferenceProvider bindMattingInput:fromAttachedMediaUsingKey:preparedByAttachedMediaKey:withVideoFormatProvider:];
-[BWMattingInferenceProvider sharedResourcePreparator];
-[BWMattingInferenceProvider bindMattingInput:fromAttachedMediaUsingKey:withVideoFormat:];
-[BWMattingInferenceProvider propagateInferenceResultsToInferenceDictionary:usingStorage:inputSampleBuffer:propagationSampleBuffer:];
-[BWMattingInferenceProvider customInferenceIdentifier];
-[BWMattingInferenceProvider inputMetadataRequirements];
-[BWMattingInferenceProvider inputVideoRequirements];
-[BWMattingInferenceProvider prewarmingSharedResourceType];
```
