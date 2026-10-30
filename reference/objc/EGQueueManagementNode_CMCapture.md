# `EGQueueManagementNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `EGNode`
- 4 instance variables, 0 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _allInputQueue;
B _allInputSync;
@"NSMutableDictionary" _queuesBySpecificInputName;
@"NSMutableDictionary" _syncBySpecificInputName;
```

## Class methods

```
+[EGQueueManagementNode initialize];
```

## Instance methods

```
-[EGQueueManagementNode dealloc];
-[EGQueueManagementNode handleAllInputAsyncOnQueue:];
-[EGQueueManagementNode handleAllInputSyncAndAssertQueue:];
-[EGQueueManagementNode queueManagedReceiveData:fromInput:];
-[EGQueueManagementNode queueManagedReceiveData:fromInputGroup:];
-[EGQueueManagementNode receiveData:fromInput:];
-[EGQueueManagementNode receiveData:fromInputGroup:];
-[EGQueueManagementNode specifyInput:handledAsyncOnQueue:];
-[EGQueueManagementNode specifyInput:handledSyncAndAssertQueue:];
```
