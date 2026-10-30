# `BWOpticalFlowInferenceProvider`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWInferenceProvider`, `BWInferenceCacheable`, `BWInferenceSubmittable`, `BWInferencePropagatable`
- 10 instance variables, 22 properties, 28 instance methods, 1 class methods

## Instance variables

```
@"NSString" _customInferenceIdentifier;
@"BWInferenceVideoRequirement" _inputRequirement;
@"BWInferenceVideoRequirement" _outputRequirement;
@"NSMutableArray" _cloneVideoRequirements;
@"PTDisparityPostProcessing" _disparityPostProcessor;
@"BWMetalInferenceContext" _metalInferenceContext;
@"MTLTextureDescriptor" _colorOutputDescriptor;
@"MTLTextureDescriptor" _colorInputDescriptor;
@"NSString" _portType;
Q _concurrencyWidth;
```

## Properties

```
@property (Ti,R,N) executionTarget;
@property (T@"NSSet",R,C,N) preventionReasons;
@property (T@"NSArray",R,N) inputVideoRequirements;
@property (T@"NSArray",R,N) outputVideoRequirements;
@property (T@"NSArray",R,N,V_cloneVideoRequirements) cloneVideoRequirements;
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
+[BWOpticalFlowInferenceProvider initialize];
```

## Instance methods

```
-[BWOpticalFlowInferenceProvider cacheable];
-[BWOpticalFlowInferenceProvider submitForSampleBuffer:usingStorage:withSubmissionTime:workQueue:completionHandler:];
-[BWOpticalFlowInferenceProvider extractable];
-[BWOpticalFlowInferenceProvider outputVideoRequirements];
-[BWOpticalFlowInferenceProvider prewarmUsingLimitedMemory:];
-[BWOpticalFlowInferenceProvider allowsAsyncPropagation];
-[BWOpticalFlowInferenceProvider dealloc];
-[BWOpticalFlowInferenceProvider reconcileWithPlaceholderProvider:];
-[BWOpticalFlowInferenceProvider bindOutputByCloningInputRequirement:toAttachedMediaUsingKey:];
-[BWOpticalFlowInferenceProvider setCustomInferenceIdentifier:];
-[BWOpticalFlowInferenceProvider cloneVideoRequirements];
-[BWOpticalFlowInferenceProvider allowedPixelBufferCompressionDirection];
-[BWOpticalFlowInferenceProvider executionTarget];
-[BWOpticalFlowInferenceProvider preventionReasons];
-[BWOpticalFlowInferenceProvider type];
-[BWOpticalFlowInferenceProvider executable];
-[BWOpticalFlowInferenceProvider outputMetadataRequirements];
-[BWOpticalFlowInferenceProvider newStorage];
-[BWOpticalFlowInferenceProvider propagatable];
-[BWOpticalFlowInferenceProvider submittable];
-[BWOpticalFlowInferenceProvider sharedResourcePreparator];
-[BWOpticalFlowInferenceProvider prepareForSubmissionWithWorkQueue:];
-[BWOpticalFlowInferenceProvider propagateInferenceResultsToInferenceDictionary:usingStorage:inputSampleBuffer:propagationSampleBuffer:];
-[BWOpticalFlowInferenceProvider customInferenceIdentifier];
-[BWOpticalFlowInferenceProvider inputMetadataRequirements];
-[BWOpticalFlowInferenceProvider inputVideoRequirements];
-[BWOpticalFlowInferenceProvider prewarmingSharedResourceType];
-[BWOpticalFlowInferenceProvider initWithInputRequirement:outputRequirement:portType:resourceProvider:configuration:];
```
