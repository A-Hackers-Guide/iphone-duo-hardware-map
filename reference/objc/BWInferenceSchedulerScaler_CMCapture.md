# `BWInferenceSchedulerScaler`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWInferenceJobProvider`, `BWInferenceCacheable`, `BWInferenceExecutable`, `BWInferenceSubmittable`, `BWInferencePropagatable`, `BWInferenceJobProvider`, `BWInferencePreventable`
- 5 instance variables, 16 properties, 26 instance methods, 0 class methods

## Instance variables

```
@"NSString" _customInferenceIdentifier;
@"BWInferenceVideoRequirement" _inputRequirement;
@"NSArray" _outputRequirements;
@"<BWInferenceProvider>" _provider;
B _allowsAsyncPropagation;
```

## Properties

```
@property (T@"NSArray",R,N) inputVideoRequirements;
@property (T@"NSArray",R,N,V_outputRequirements) outputRequirements;
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
@property (TB,R,N,V_allowsAsyncPropagation) allowsAsyncPropagation;
@property (TB,R,N) mustExecuteWhenAllowed;
```

## Instance methods

```
-[BWInferenceSchedulerScaler cacheable];
-[BWInferenceSchedulerScaler prepareForExecution];
-[BWInferenceSchedulerScaler submitForSampleBuffer:usingStorage:withSubmissionTime:workQueue:completionHandler:];
-[BWInferenceSchedulerScaler extractable];
-[BWInferenceSchedulerScaler executeOnSampleBuffer:usingStorage:withExecutionTime:completionHandler:];
-[BWInferenceSchedulerScaler allowsAsyncPropagation];
-[BWInferenceSchedulerScaler initWithInputRequirement:derivedFromRequirement:outputRequirements:scalerConfiguration:];
-[BWInferenceSchedulerScaler dealloc];
-[BWInferenceSchedulerScaler reconcileWithPlaceholderProvider:];
-[BWInferenceSchedulerScaler outputRequirements];
-[BWInferenceSchedulerScaler setCustomInferenceIdentifier:];
-[BWInferenceSchedulerScaler type];
-[BWInferenceSchedulerScaler executable];
-[BWInferenceSchedulerScaler newStorage];
-[BWInferenceSchedulerScaler description];
-[BWInferenceSchedulerScaler mustExecuteWhenAllowed];
-[BWInferenceSchedulerScaler propagatable];
-[BWInferenceSchedulerScaler preventionReasonWithSampleBuffer:executionTime:];
-[BWInferenceSchedulerScaler submittable];
-[BWInferenceSchedulerScaler sharedResourcePreparator];
-[BWInferenceSchedulerScaler prepareForSubmissionWithWorkQueue:];
-[BWInferenceSchedulerScaler copyWithZone:];
-[BWInferenceSchedulerScaler propagateInferenceResultsToInferenceDictionary:usingStorage:inputSampleBuffer:propagationSampleBuffer:];
-[BWInferenceSchedulerScaler customInferenceIdentifier];
-[BWInferenceSchedulerScaler inputVideoRequirements];
-[BWInferenceSchedulerScaler _newProviderForWithScalerConfiguration:inputDerivedFromRequirement:];
```
