# `MLE5ExecutionStream`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 7 properties, 28 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _operations;
@"<MLE5ExecutionStreamOperationPool>" _operationPool;
^{e5rt_execution_stream=} _streamHandle;
q _state;
@"NSObject<OS_dispatch_queue>" _resetQueue;
@"NSObject<OS_dispatch_source>" _resetTimer;
```

## Properties

```
@property (T@"NSArray",C,N,V_operations) operations;
@property (T^{e5rt_execution_stream=},N,V_streamHandle) streamHandle;
@property (T@"<MLE5ExecutionStreamOperationPool>",&,N,V_operationPool) operationPool;
@property (Tq,N,V_state) state;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_resetQueue) resetQueue;
@property (T@"NSObject<OS_dispatch_source>",&,N,V_resetTimer) resetTimer;
@property (TQ,R,N) streamId;
```

## Instance methods

```
-[MLE5ExecutionStream streamId];
-[MLE5ExecutionStream _reset];
-[MLE5ExecutionStream _setANEExecutionPriorityWithOptions:];
-[MLE5ExecutionStream cancelPendingReset];
-[MLE5ExecutionStream setState:];
-[MLE5ExecutionStream prepareAsyncSubmissionForInputFeatures:options:error:];
-[MLE5ExecutionStream init];
-[MLE5ExecutionStream resetAfterLingering:];
-[MLE5ExecutionStream dealloc];
-[MLE5ExecutionStream _executeStream:error:];
-[MLE5ExecutionStream _reusableForInputFeatures:options:];
-[MLE5ExecutionStream setStreamHandle:];
-[MLE5ExecutionStream resetQueue];
-[MLE5ExecutionStream setResetTimer:];
-[MLE5ExecutionStream operations];
-[MLE5ExecutionStream executeForInputFeatures:options:error:];
-[MLE5ExecutionStream submitWithCompletionHandler:];
-[MLE5ExecutionStream setOperationPool:];
-[MLE5ExecutionStream resetTimer];
-[MLE5ExecutionStream operationPool];
-[MLE5ExecutionStream reusableForSyncPredictionForInputFeatures:options:];
-[MLE5ExecutionStream reusableForAsyncSubmissionForInputFeatures:options:];
-[MLE5ExecutionStream serializeInferenceFrameDataForOptions:error:];
-[MLE5ExecutionStream setupOperationForInputFeatures:operationPool:error:];
-[MLE5ExecutionStream streamHandle];
-[MLE5ExecutionStream setOperations:];
-[MLE5ExecutionStream state];
-[MLE5ExecutionStream _prepareForInputFeatures:options:error:];
```
