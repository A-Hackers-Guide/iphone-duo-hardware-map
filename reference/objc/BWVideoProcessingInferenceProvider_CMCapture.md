# `BWVideoProcessingInferenceProvider`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWInferenceProvider`, `BWInferenceCacheable`, `BWInferenceSubmittable`, `BWInferenceExecutable`, `BWInferencePropagatable`
- 11 instance variables, 22 properties, 31 instance methods, 1 class methods

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
Q _analysisType;
@"VCPCaptureAnalysisSession" _vcpSession;
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
+[BWVideoProcessingInferenceProvider initialize];
```

## Instance methods

```
-[BWVideoProcessingInferenceProvider cacheable];
-[BWVideoProcessingInferenceProvider prepareForExecution];
-[BWVideoProcessingInferenceProvider submitForSampleBuffer:usingStorage:withSubmissionTime:workQueue:completionHandler:];
-[BWVideoProcessingInferenceProvider extractable];
-[BWVideoProcessingInferenceProvider executeOnSampleBuffer:usingStorage:withExecutionTime:completionHandler:];
-[BWVideoProcessingInferenceProvider outputVideoRequirements];
-[BWVideoProcessingInferenceProvider prewarmUsingLimitedMemory:];
-[BWVideoProcessingInferenceProvider allowsAsyncPropagation];
-[BWVideoProcessingInferenceProvider dealloc];
-[BWVideoProcessingInferenceProvider reconcileWithPlaceholderProvider:];
-[BWVideoProcessingInferenceProvider setCustomInferenceIdentifier:];
-[BWVideoProcessingInferenceProvider cloneVideoRequirements];
-[BWVideoProcessingInferenceProvider allowedPixelBufferCompressionDirection];
-[BWVideoProcessingInferenceProvider executionTarget];
-[BWVideoProcessingInferenceProvider preventionReasons];
-[BWVideoProcessingInferenceProvider type];
-[BWVideoProcessingInferenceProvider executable];
-[BWVideoProcessingInferenceProvider bindVideoInputFromAttachedMediaUsingKey:preparedByAttachedMediaKey:withVideoFormatProvider:];
-[BWVideoProcessingInferenceProvider outputMetadataRequirements];
-[BWVideoProcessingInferenceProvider newStorage];
-[BWVideoProcessingInferenceProvider propagatable];
-[BWVideoProcessingInferenceProvider submittable];
-[BWVideoProcessingInferenceProvider sharedResourcePreparator];
-[BWVideoProcessingInferenceProvider prepareForSubmissionWithWorkQueue:];
-[BWVideoProcessingInferenceProvider bindOutputMetadataKeys:];
-[BWVideoProcessingInferenceProvider propagateInferenceResultsToInferenceDictionary:usingStorage:inputSampleBuffer:propagationSampleBuffer:];
-[BWVideoProcessingInferenceProvider customInferenceIdentifier];
-[BWVideoProcessingInferenceProvider inputMetadataRequirements];
-[BWVideoProcessingInferenceProvider inputVideoRequirements];
-[BWVideoProcessingInferenceProvider prewarmingSharedResourceType];
-[BWVideoProcessingInferenceProvider initWithType:analysisType:executionTarget:schedulerPriority:preventionReasons:resourceProvider:];
```
