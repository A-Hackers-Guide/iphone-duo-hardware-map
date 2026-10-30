# `BWInferenceScheduler`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 4 properties, 13 instance methods, 1 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _connectionsLock;
@"NSMapTable" _connectionsByIdentifier;
@"NSObject<OS_dispatch_workloop>" _inferenceWorkloop;
@"NSObject<OS_dispatch_workloop>" _scalingWorkloop;
@"NSObject<OS_dispatch_workloop>" _submissionWorkloop;
@"NSObject<OS_dispatch_workloop>" _completionWorkloop;
@"NSObject<OS_dispatch_queue>" _metalSubmissionQueue;
@"NSObject<OS_dispatch_queue>" _metalCompletionQueue;
@"NSObject<OS_dispatch_queue>" _transientInferenceQueue;
@"BWInferenceSharedE5ANEMemoryProvider" _sharedE5ANEMemoryProvider;
@"NSMutableArray" _workIntervalResources;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_metalSubmissionQueue) metalSubmissionQueue;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_metalCompletionQueue) metalCompletionQueue;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_transientInferenceQueue) transientInferenceQueue;
@property (T@"BWInferenceSharedE5ANEMemoryProvider",&,V_sharedE5ANEMemoryProvider) sharedE5ANEMemoryProvider;
```

## Class methods

```
+[BWInferenceScheduler initialize];
```

## Instance methods

```
-[BWInferenceScheduler metalCompletionQueueForWorkIntervalIndex:];
-[BWInferenceScheduler metalSubmissionQueue];
-[BWInferenceScheduler init];
-[BWInferenceScheduler prepareForInferenceRequirements:dependencyProviderSource:formatProvider:pixelBufferPoolProvider:connection:backPressureDrivenPipelining:engineReconfigured:processingConfiguration:postProcessors:schedulerPriority:engineDescription:];
-[BWInferenceScheduler dealloc];
-[BWInferenceScheduler transientInferenceQueue];
-[BWInferenceScheduler metalCompletionQueue];
-[BWInferenceScheduler performInferencesForConnection:usingInputSampleBuffer:attachingResultsToSampleBuffer:skippingInferencesWithTypes:];
-[BWInferenceScheduler metalSubmissionQueueForWorkIntervalIndex:];
-[BWInferenceScheduler sharedE5ANEMemoryProvider];
-[BWInferenceScheduler registerInferenceConnectionWithEngineDescription:];
-[BWInferenceScheduler setSharedE5ANEMemoryProvider:];
-[BWInferenceScheduler unregisterInferenceConnection:];
```
