# `FBSceneSynchronizer`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 4 properties, 6 instance methods, 3 class methods

## Instance variables

```
@"NSString" _identifier;
@"BSServiceDispatchQueue" _workspaceQueue;
@"BSServiceCompoundQueue" _serviceQueue;
@"FBWorkspaceEventDispatcher" _dispatcher;
@"RBSProcessHandle" _lock_process;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _lock_waitingForConnect;
```

## Properties

```
@property (T@"BSServiceDispatchQueue",R,N,V_workspaceQueue) machQueue;
@property (T@"BSServiceQueue",R,N) callOutQueue;
@property (T@"BSServiceQueue",R,N,V_serviceQueue) serviceQueue;
@property (T@"RBSProcessHandle",R,N) processHandle;
```

## Class methods

```
+[FBSceneSynchronizer detachedSynchronizerWithIdentifier:];
+[FBSceneSynchronizer synchronizerForViewServiceWithProcessIdentifier:];
+[FBSceneSynchronizer synchronizerWithAuditToken:];
```

## Instance methods

```
-[FBSceneSynchronizer callOutQueue];
-[FBSceneSynchronizer machQueue];
-[FBSceneSynchronizer performAsyncOnSendingQueue:];
-[FBSceneSynchronizer serviceQueue];
-[FBSceneSynchronizer processHandle];
-[FBSceneSynchronizer description];
```
