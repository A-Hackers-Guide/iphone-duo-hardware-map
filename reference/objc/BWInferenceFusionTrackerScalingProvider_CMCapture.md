# `BWInferenceFusionTrackerScalingProvider`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWInferenceProvider`, `BWInferenceCacheable`, `BWInferenceExecutable`, `BWInferenceSubmittable`, `BWInferencePreventable`, `BWInferencePropagatable`
- 10 instance variables, 23 properties, 31 instance methods, 0 class methods

## Instance variables

```
@"NSString" _customInferenceIdentifier;
@"BWInferenceVideoRequirement" _inputRequirement;
@"BWInferenceVideoRequirement" _orderBufferRequirement;
@"BWInferenceVideoRequirement" _outputRequirement;
^{opaqueCMFormatDescription=} _outputFormatDescription;
@"NSMutableArray" _outputMetadataRequirements;
q _operation;
@"FTMSRScaler" _scaler;
@"BWMetalInferenceContext" _metalInferenceContext;
@"BWInferenceFusionTrackerMeanPixelCalculator" _meanPixelCalculator;
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
@property (TB,R,N) mustExecuteWhenAllowed;
@property (TB,R,N) allowsAsyncPropagation;
```

## Instance methods

```
-[BWInferenceFusionTrackerScalingProvider cacheable];
-[BWInferenceFusionTrackerScalingProvider prepareForExecution];
-[BWInferenceFusionTrackerScalingProvider submitForSampleBuffer:usingStorage:withSubmissionTime:workQueue:completionHandler:];
-[BWInferenceFusionTrackerScalingProvider extractable];
-[BWInferenceFusionTrackerScalingProvider executeOnSampleBuffer:usingStorage:withExecutionTime:completionHandler:];
-[BWInferenceFusionTrackerScalingProvider outputVideoRequirements];
-[BWInferenceFusionTrackerScalingProvider prewarmUsingLimitedMemory:];
-[BWInferenceFusionTrackerScalingProvider allowsAsyncPropagation];
-[BWInferenceFusionTrackerScalingProvider dealloc];
-[BWInferenceFusionTrackerScalingProvider reconcileWithPlaceholderProvider:];
-[BWInferenceFusionTrackerScalingProvider setCustomInferenceIdentifier:];
-[BWInferenceFusionTrackerScalingProvider cloneVideoRequirements];
-[BWInferenceFusionTrackerScalingProvider allowedPixelBufferCompressionDirection];
-[BWInferenceFusionTrackerScalingProvider executionTarget];
-[BWInferenceFusionTrackerScalingProvider preventionReasons];
-[BWInferenceFusionTrackerScalingProvider type];
-[BWInferenceFusionTrackerScalingProvider executable];
-[BWInferenceFusionTrackerScalingProvider outputMetadataRequirements];
-[BWInferenceFusionTrackerScalingProvider newStorage];
-[BWInferenceFusionTrackerScalingProvider description];
-[BWInferenceFusionTrackerScalingProvider mustExecuteWhenAllowed];
-[BWInferenceFusionTrackerScalingProvider propagatable];
-[BWInferenceFusionTrackerScalingProvider preventionReasonWithSampleBuffer:executionTime:];
-[BWInferenceFusionTrackerScalingProvider submittable];
-[BWInferenceFusionTrackerScalingProvider sharedResourcePreparator];
-[BWInferenceFusionTrackerScalingProvider prepareForSubmissionWithWorkQueue:];
-[BWInferenceFusionTrackerScalingProvider propagateInferenceResultsToInferenceDictionary:usingStorage:inputSampleBuffer:propagationSampleBuffer:];
-[BWInferenceFusionTrackerScalingProvider customInferenceIdentifier];
-[BWInferenceFusionTrackerScalingProvider inputMetadataRequirements];
-[BWInferenceFusionTrackerScalingProvider inputVideoRequirements];
-[BWInferenceFusionTrackerScalingProvider prewarmingSharedResourceType];
```
