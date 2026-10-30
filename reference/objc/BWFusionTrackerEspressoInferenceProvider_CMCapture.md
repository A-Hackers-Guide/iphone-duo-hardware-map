# `BWFusionTrackerEspressoInferenceProvider`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWEspressoInferenceProvider`
- Protocols: `BWInferencePreventable`
- 1 instance variables, 14 properties, 5 instance methods, 0 class methods

## Instance variables

```
q _operation;
```

## Properties

```
@property (Tq,V_operation) operation;
@property (TB,R,N) mustExecuteWhenAllowed;
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
```

## Instance methods

```
-[BWFusionTrackerEspressoInferenceProvider setOperation:];
-[BWFusionTrackerEspressoInferenceProvider submitForSampleBuffer:usingStorage:withSubmissionTime:workQueue:completionHandler:];
-[BWFusionTrackerEspressoInferenceProvider operation];
-[BWFusionTrackerEspressoInferenceProvider mustExecuteWhenAllowed];
-[BWFusionTrackerEspressoInferenceProvider preventionReasonWithSampleBuffer:executionTime:];
```
