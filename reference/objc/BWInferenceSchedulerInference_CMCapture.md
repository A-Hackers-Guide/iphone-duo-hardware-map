# `BWInferenceSchedulerInference`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWInferenceJobProvider`, `BWInferenceCacheable`, `BWInferenceExecutable`, `BWInferenceSubmittable`, `BWInferenceSharedResourcePreparatory`, `BWInferencePreventable`
- 9 instance variables, 20 properties, 29 instance methods, 1 class methods

## Instance variables

```
Q _identifier;
@"<BWInferencePreventable>" _preventable;
@"<BWInferenceProvider>" _provider;
i _inferenceType;
I _priority;
f _maximumFramesPerSecond;
Ad _previousExecutionTimeInSeconds;
B _mustExecuteWhenAllowed;
B _propagatesFrameRatePrevention;
```

## Properties

```
@property (T@"<BWInferenceProvider>",R,N,V_provider) provider;
@property (TQ,R,N,V_identifier) identifier;
@property (Ti,R,N,V_inferenceType) inferenceType;
@property (TI,R,N,V_priority) priority;
@property (Tf,R,N,V_maximumFramesPerSecond) maximumFramesPerSecond;
@property (T{?=qiIq},R,N) previousExecutionTime;
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
@property (Ti,R,N) sharedResourceType;
@property (TB,R,N) mustExecuteWhenAllowed;
```

## Class methods

```
+[BWInferenceSchedulerInference initialize];
```

## Instance methods

```
-[BWInferenceSchedulerInference prepareForSubmissionWithWorkQueue:sharedANEMemoryProvider:];
-[BWInferenceSchedulerInference prepareForExecutionWithSharedANEMemoryProvider:];
-[BWInferenceSchedulerInference cacheable];
-[BWInferenceSchedulerInference prepareForExecution];
-[BWInferenceSchedulerInference priority];
-[BWInferenceSchedulerInference submitForSampleBuffer:usingStorage:withSubmissionTime:workQueue:completionHandler:];
-[BWInferenceSchedulerInference extractable];
-[BWInferenceSchedulerInference executeOnSampleBuffer:usingStorage:withExecutionTime:completionHandler:];
-[BWInferenceSchedulerInference identifier];
-[BWInferenceSchedulerInference dealloc];
-[BWInferenceSchedulerInference reconcileWithPlaceholderProvider:];
-[BWInferenceSchedulerInference provider];
-[BWInferenceSchedulerInference sharedResourceType];
-[BWInferenceSchedulerInference previousExecutionTime];
-[BWInferenceSchedulerInference setCustomInferenceIdentifier:];
-[BWInferenceSchedulerInference type];
-[BWInferenceSchedulerInference executable];
-[BWInferenceSchedulerInference maximumFramesPerSecond];
-[BWInferenceSchedulerInference initWithInferenceRequirement:];
-[BWInferenceSchedulerInference newStorage];
-[BWInferenceSchedulerInference description];
-[BWInferenceSchedulerInference mustExecuteWhenAllowed];
-[BWInferenceSchedulerInference propagatable];
-[BWInferenceSchedulerInference preventionReasonWithSampleBuffer:executionTime:];
-[BWInferenceSchedulerInference submittable];
-[BWInferenceSchedulerInference sharedResourcePreparator];
-[BWInferenceSchedulerInference prepareForSubmissionWithWorkQueue:];
-[BWInferenceSchedulerInference inferenceType];
-[BWInferenceSchedulerInference customInferenceIdentifier];
```
