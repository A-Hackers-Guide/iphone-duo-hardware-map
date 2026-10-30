# `BWBackPressureNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 11 instance variables, 3 properties, 20 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_semaphore>" _semaphore;
I _numberOfInputs;
@"NSMutableArray" _receivedPresentationTimestampByInput;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _presentationTimestampLock;
q _initialSemaphoreValue;
@"BWLimitedGMErrorLogger" _limitedGMErrorLogger;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _stateLock;
i _numEODMessagesReceived;
B _receivedFirstFrame;
@"<BWNodeBackPressureSource>" _backPressureSourceNode;
@"NSObject<OS_dispatch_queue>" _semaphoreSignalQueue;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_semaphore>",R,N,V_semaphore) semaphore;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_semaphoreSignalQueue) semaphoreSignalQueue;
@property (T@"<BWNodeBackPressureSource>",N,V_backPressureSourceNode) backPressureSourceNode;
```

## Class methods

```
+[BWBackPressureNode initialize];
```

## Instance methods

```
-[BWBackPressureNode prepareForCurrentConfigurationToBecomeLive];
-[BWBackPressureNode renderSampleBuffer:forInput:];
-[BWBackPressureNode setSemaphoreSignalQueue:];
-[BWBackPressureNode semaphore];
-[BWBackPressureNode init];
-[BWBackPressureNode dealloc];
-[BWBackPressureNode semaphoreSignalQueue];
-[BWBackPressureNode hasNonLiveConfigurationChanges];
-[BWBackPressureNode setInitialSemaphoreValue:];
-[BWBackPressureNode setBackPressureSourceNode:];
-[BWBackPressureNode _setSemaphore:];
-[BWBackPressureNode handleDroppedSample:forInput:];
-[BWBackPressureNode didReachEndOfDataForConfigurationID:input:];
-[BWBackPressureNode initWithNumberOfInputsAndOutputs:initialSemaphoreValue:];
-[BWBackPressureNode _handleUpdatedPresentationTimestamp:forIndex:];
-[BWBackPressureNode nodeSubType];
-[BWBackPressureNode didSelectFormat:forInput:];
-[BWBackPressureNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWBackPressureNode backPressureSourceNode];
-[BWBackPressureNode nodeType];
```
