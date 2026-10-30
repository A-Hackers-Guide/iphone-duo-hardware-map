# `BWInferenceDepthScalingProvider`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWInferenceProvider`, `BWInferenceCacheable`, `BWInferenceExecutable`, `BWInferenceSubmittable`, `BWInferencePropagatable`
- 21 instance variables, 22 properties, 30 instance methods, 1 class methods

## Instance variables

```
@"NSString" _customInferenceIdentifier;
@"BWInferenceVideoRequirement" _inputRequirement;
@"NSArray" _outputRequirements;
^{opaqueCMFormatDescription=} _outputFormatDescription;
@"FigMetalContext" _metalContext;
i _requestedRotation;
i _processingMode;
B _GPUDepthConversionSupported;
B _inputIsFloatFormat;
@"NSDictionary" _pipelineStates;
I _outputFormat;
@"NSNumber" _NANValue;
@"NSNumber" _clampMin;
@"NSNumber" _clampMax;
B _flipX;
i _rotationDegrees;
B _allowUpsampling;
Q _concurrencyWidth;
B _propagateResultsToInferenceDictionary;
@"MTLTextureDescriptor" _srcdesc;
@"MTLTextureDescriptor" _dstdesc;
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
+[BWInferenceDepthScalingProvider initialize];
```

## Instance methods

```
-[BWInferenceDepthScalingProvider cacheable];
-[BWInferenceDepthScalingProvider prepareForExecution];
-[BWInferenceDepthScalingProvider submitForSampleBuffer:usingStorage:withSubmissionTime:workQueue:completionHandler:];
-[BWInferenceDepthScalingProvider extractable];
-[BWInferenceDepthScalingProvider executeOnSampleBuffer:usingStorage:withExecutionTime:completionHandler:];
-[BWInferenceDepthScalingProvider outputVideoRequirements];
-[BWInferenceDepthScalingProvider prewarmUsingLimitedMemory:];
-[BWInferenceDepthScalingProvider allowsAsyncPropagation];
-[BWInferenceDepthScalingProvider dealloc];
-[BWInferenceDepthScalingProvider reconcileWithPlaceholderProvider:];
-[BWInferenceDepthScalingProvider setCustomInferenceIdentifier:];
-[BWInferenceDepthScalingProvider cloneVideoRequirements];
-[BWInferenceDepthScalingProvider allowedPixelBufferCompressionDirection];
-[BWInferenceDepthScalingProvider executionTarget];
-[BWInferenceDepthScalingProvider preventionReasons];
-[BWInferenceDepthScalingProvider type];
-[BWInferenceDepthScalingProvider executable];
-[BWInferenceDepthScalingProvider bindVideoInputFromAttachedMediaUsingKey:preparedByAttachedMediaKey:withVideoFormatProvider:];
-[BWInferenceDepthScalingProvider outputMetadataRequirements];
-[BWInferenceDepthScalingProvider newStorage];
-[BWInferenceDepthScalingProvider propagatable];
-[BWInferenceDepthScalingProvider submittable];
-[BWInferenceDepthScalingProvider sharedResourcePreparator];
-[BWInferenceDepthScalingProvider prepareForSubmissionWithWorkQueue:];
-[BWInferenceDepthScalingProvider propagateInferenceResultsToInferenceDictionary:usingStorage:inputSampleBuffer:propagationSampleBuffer:];
-[BWInferenceDepthScalingProvider customInferenceIdentifier];
-[BWInferenceDepthScalingProvider inputMetadataRequirements];
-[BWInferenceDepthScalingProvider inputVideoRequirements];
-[BWInferenceDepthScalingProvider prewarmingSharedResourceType];
-[BWInferenceDepthScalingProvider initWithInputRequirement:outputRequirements:configuration:];
```
