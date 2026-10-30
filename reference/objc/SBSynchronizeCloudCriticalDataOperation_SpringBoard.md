# `SBSynchronizeCloudCriticalDataOperation`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 1 properties, 17 instance methods, 0 class methods

## Instance variables

```
B _needsSync;
@"SBBootDefaults" _queue_bootDefaults;
@"NSOperationQueue" _operationQueue;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSObject<OS_dispatch_group>" _queue_operationGroup;
Q _queue_operationCount;
B _queue_isComplete;
d _queue_cloudSyncStartTime;
```

## Properties

```
@property (TB,R,D,N,GisComplete) complete;
```

## Instance methods

```
-[SBSynchronizeCloudCriticalDataOperation isComplete];
-[SBSynchronizeCloudCriticalDataOperation init];
-[SBSynchronizeCloudCriticalDataOperation _startOperations];
-[SBSynchronizeCloudCriticalDataOperation _addOperation:shouldBlock:];
-[SBSynchronizeCloudCriticalDataOperation _addOperations];
-[SBSynchronizeCloudCriticalDataOperation _fetchDomains:fromIndex:queue:completion:];
-[SBSynchronizeCloudCriticalDataOperation _pendingOperationCount];
-[SBSynchronizeCloudCriticalDataOperation _queue_addOperation:shouldBlock:];
-[SBSynchronizeCloudCriticalDataOperation _queue_addOperations];
-[SBSynchronizeCloudCriticalDataOperation _queue_fetchCloudAccountOperation];
-[SBSynchronizeCloudCriticalDataOperation _queue_fetchCloudDefaultsOperation];
-[SBSynchronizeCloudCriticalDataOperation _queue_fetchMDMProfilesOperation];
-[SBSynchronizeCloudCriticalDataOperation _queue_isComplete];
-[SBSynchronizeCloudCriticalDataOperation _queue_migrateSoundPreferencesOperation];
-[SBSynchronizeCloudCriticalDataOperation initWithDefaults:userManager:];
-[SBSynchronizeCloudCriticalDataOperation startSynchronize];
-[SBSynchronizeCloudCriticalDataOperation waitForSynchronizeToCompleteWithTimeout:];
```
