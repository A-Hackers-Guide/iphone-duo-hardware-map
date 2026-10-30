# `ULBGSystemTaskManager`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"BGSystemTaskScheduler" _scheduler;
@"NSObject<OS_dispatch_queue>" _internalQueue;
```

## Properties

```
@property (T@"BGSystemTaskScheduler",&,N,V_scheduler) scheduler;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_internalQueue) internalQueue;
```

## Instance methods

```
-[ULBGSystemTaskManager init];
-[ULBGSystemTaskManager setScheduler:];
-[ULBGSystemTaskManager scheduler];
-[ULBGSystemTaskManager setInternalQueue:];
-[ULBGSystemTaskManager internalQueue];
-[ULBGSystemTaskManager deregisterAndCancelTaskWithIdentifier:];
-[ULBGSystemTaskManager registerAndSubmitTaskWithRequest:usingQueue:launchCondition:launchHandler:];
```
