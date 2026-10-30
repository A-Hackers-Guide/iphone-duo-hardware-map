# `BWInferenceJobProvider` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 8 properties, 10 instance methods, 0 class methods

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
```

## Instance methods

```
-[BWInferenceJobProvider cacheable];
-[BWInferenceJobProvider extractable];
-[BWInferenceJobProvider setCustomInferenceIdentifier:];
-[BWInferenceJobProvider type];
-[BWInferenceJobProvider executable];
-[BWInferenceJobProvider newStorage];
-[BWInferenceJobProvider propagatable];
-[BWInferenceJobProvider submittable];
-[BWInferenceJobProvider sharedResourcePreparator];
-[BWInferenceJobProvider customInferenceIdentifier];
```
