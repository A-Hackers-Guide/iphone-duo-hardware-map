# `BWInferenceSchedulerGraphInputNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWInferenceExtractable`, `BWInferenceJobProvider`
- 2 instance variables, 12 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"NSString" _customInferenceIdentifier;
@"NSSet" _videoPropagatedToStorage;
```

## Properties

```
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

## Class methods

```
+[BWInferenceSchedulerGraphInputNode initialize];
```

## Instance methods

```
-[BWInferenceSchedulerGraphInputNode cacheable];
-[BWInferenceSchedulerGraphInputNode extractFromStorage:usingVideoRequirements:metadataRequirements:toSampleBuffer:];
-[BWInferenceSchedulerGraphInputNode extractable];
-[BWInferenceSchedulerGraphInputNode dealloc];
-[BWInferenceSchedulerGraphInputNode setCustomInferenceIdentifier:];
-[BWInferenceSchedulerGraphInputNode initWithVideoPropagatedToStorage:];
-[BWInferenceSchedulerGraphInputNode type];
-[BWInferenceSchedulerGraphInputNode executable];
-[BWInferenceSchedulerGraphInputNode newStorage];
-[BWInferenceSchedulerGraphInputNode description];
-[BWInferenceSchedulerGraphInputNode propagatable];
-[BWInferenceSchedulerGraphInputNode submittable];
-[BWInferenceSchedulerGraphInputNode sharedResourcePreparator];
-[BWInferenceSchedulerGraphInputNode customInferenceIdentifier];
-[BWInferenceSchedulerGraphInputNode extractFromSampleBuffer:usingVideoRequirements:metadataRequirements:toStorage:];
```
