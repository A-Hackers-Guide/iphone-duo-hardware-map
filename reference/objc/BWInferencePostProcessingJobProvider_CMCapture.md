# `BWInferencePostProcessingJobProvider`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWInferenceJobProvider`, `BWInferencePostProcessable`
- 5 instance variables, 16 properties, 22 instance methods, 1 class methods

## Instance variables

```
@"NSString" _customInferenceIdentifier;
@"<BWInferencePostProcessor>" _postProcessor;
@"NSMutableDictionary" _multipleDependencyCountByInferenceType;
@"NSMutableSet" _completedDependencies;
B _allDependenciesCompleted;
```

## Properties

```
@property (T@"<BWInferencePostProcessor>",R,N,V_postProcessor) postProcessor;
@property (T@"NSMutableSet",R,N,V_completedDependencies) completedDependencies;
@property (TB,R,N,V_allDependenciesCompleted) allDependenciesCompleted;
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
@property (TB,R,N) requiresReprepareDuringReconfiguration;
```

## Class methods

```
+[BWInferencePostProcessingJobProvider initialize];
```

## Instance methods

```
-[BWInferencePostProcessingJobProvider cacheable];
-[BWInferencePostProcessingJobProvider extractable];
-[BWInferencePostProcessingJobProvider prepareForPostProcessing];
-[BWInferencePostProcessingJobProvider postProcessor];
-[BWInferencePostProcessingJobProvider dealloc];
-[BWInferencePostProcessingJobProvider initWithPostProcessor:];
-[BWInferencePostProcessingJobProvider completedDependencies];
-[BWInferencePostProcessingJobProvider setCustomInferenceIdentifier:];
-[BWInferencePostProcessingJobProvider type];
-[BWInferencePostProcessingJobProvider executable];
-[BWInferencePostProcessingJobProvider newStorage];
-[BWInferencePostProcessingJobProvider description];
-[BWInferencePostProcessingJobProvider propagatable];
-[BWInferencePostProcessingJobProvider markDependencyCompletedForInferenceType:];
-[BWInferencePostProcessingJobProvider resetDependencyManagement];
-[BWInferencePostProcessingJobProvider submittable];
-[BWInferencePostProcessingJobProvider recordIndirectDependenciesForInferenceType:dependencyCount:];
-[BWInferencePostProcessingJobProvider allDependenciesCompleted];
-[BWInferencePostProcessingJobProvider sharedResourcePreparator];
-[BWInferencePostProcessingJobProvider postProcessOnAttachingSampleBuffer:completionHandler:];
-[BWInferencePostProcessingJobProvider requiresReprepareDuringReconfiguration];
-[BWInferencePostProcessingJobProvider customInferenceIdentifier];
```
