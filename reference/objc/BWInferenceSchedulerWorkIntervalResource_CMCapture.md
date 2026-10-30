# `BWInferenceSchedulerWorkIntervalResource`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 2 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_workloop>" _submissionWorkloop;
@"NSObject<OS_dispatch_workloop>" _completionWorkloop;
@"NSObject<OS_dispatch_queue>" _metalSubmissionQueue;
@"NSObject<OS_dispatch_queue>" _metalCompletionQueue;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_metalSubmissionQueue) metalSubmissionQueue;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_metalCompletionQueue) metalCompletionQueue;
```

## Instance methods

```
-[BWInferenceSchedulerWorkIntervalResource metalSubmissionQueue];
-[BWInferenceSchedulerWorkIntervalResource dealloc];
-[BWInferenceSchedulerWorkIntervalResource metalCompletionQueue];
-[BWInferenceSchedulerWorkIntervalResource initWithWorkGroup:];
```
