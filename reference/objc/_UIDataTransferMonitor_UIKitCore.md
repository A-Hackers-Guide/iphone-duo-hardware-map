# `_UIDataTransferMonitor`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSItemProviderDataTransferDelegate`, `NSProgressReporting`
- 13 instance variables, 10 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _transferQueue_requestsBySourceItemUUID;
@"NSMutableSet" _transferQueue_requestsInProgress;
B _transferQueue_suppressEventsUntilRequested;
B _transferQueue_shouldSendBeganCallback;
B _transferQueue_hasSentBeganCallback;
B _transferQueue_hasSentFinishedCallback;
B _transferQueue_shouldSendFinishedCallback;
@"NSProgress" _transferQueue_masterProgress;
@"NSMutableArray" _transferQueue_childProgresses;
@"NSMutableSet" _transferQueue_allEncounteredItemUUIDs;
@"<_UIDataTransferMonitorDelegate>" _delegate;
@"NSArray" _outstandingRequests;
Q _outstandingItemsCount;
```

## Properties

```
@property (T@"<_UIDataTransferMonitorDelegate>",W,N,V_delegate) delegate;
@property (T@"NSArray",R,C,N,V_outstandingRequests) outstandingRequests;
@property (TQ,R,N,V_outstandingItemsCount) outstandingItemsCount;
@property (TQ,R,D,N) totalItemsCount;
@property (TB,D,N) suppressEventsUntilRequested;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSProgress",R) progress;
```

## Instance methods

```
-[_UIDataTransferMonitor outstandingRequests];
-[_UIDataTransferMonitor observeValueForKeyPath:ofObject:change:context:];
-[_UIDataTransferMonitor init];
-[_UIDataTransferMonitor dealloc];
-[_UIDataTransferMonitor progress];
-[_UIDataTransferMonitor setDelegate:];
-[_UIDataTransferMonitor delegate];
-[_UIDataTransferMonitor itemProvider:beganDataTransferTransactionUUID:progress:];
-[_UIDataTransferMonitor itemProvider:finishedDataTransferTransactionUUID:];
-[_UIDataTransferMonitor totalItemsCount];
-[_UIDataTransferMonitor _transferQueue_recomputeMasterProgress];
-[_UIDataTransferMonitor _transferQueue_scheduleBeganCallback];
-[_UIDataTransferMonitor _transferQueue_scheduleFinishedCallback];
-[_UIDataTransferMonitor _transferQueue_sendBeganCallback];
-[_UIDataTransferMonitor _transferQueue_sendFinishedCallback];
-[_UIDataTransferMonitor cancelOutstandingRequests];
-[_UIDataTransferMonitor outstandingItemsCount];
-[_UIDataTransferMonitor sendDelegateEventsIfNeeded];
-[_UIDataTransferMonitor setSuppressEventsUntilRequested:];
-[_UIDataTransferMonitor suppressEventsUntilRequested];
```
