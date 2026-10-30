# `FBProcessManager`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBProcessDelegate`, `FBWorkspaceDomainConnectionDelegate`
- 23 instance variables, 6 properties, 44 instance methods, 3 class methods

## Instance variables

```
@"FBWorkspaceEventDispatcher" _eventDispatcher;
@"FBSceneManager" _lock_legacySceneManager;
@"FBProcess" _currentProcess;
@"FBLocalSynchronousSceneClientProvider" _lock_syncLocalSceneClientProvider;
@"NSObject<OS_dispatch_queue>" _bootstrapQueue;
@"NSObject<OS_dispatch_queue>" _callOutQueue;
@"RBSProcessMonitor" _processMonitor;
@"<BSInvalidatable>" _stateCaptureAssertion;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _bootstrapLock;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _bootstrapPredicatesLock;
@"NSMutableSet" _bootstrap_pendingProcesses;
@"NSMutableSet" _bootstrap_bootstrappingProcesses;
@"NSMutableSet" _bootstrap_processPredicates;
@"<FBProcessWatchdogProviding>" _noDirectAccess_defaultWatchdogPolicy;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSMutableDictionary" _lock_processesByPID;
@"NSMutableDictionary" _lock_processesByVersionedPID;
@"NSMutableDictionary" _lock_processesByIdentity;
@"NSHashTable" _lock_observers;
@"RBSAssertion" _lock_assertion;
B _lock_initializationComplete;
B _lock_invalidated;
B _bootstrapLock_invalidated;
```

## Properties

```
@property (T@"<FBProcessWatchdogProviding>",&,V_noDirectAccess_defaultWatchdogPolicy) defaultWatchdogPolicy;
@property (T@"FBApplicationProcess",R,N) systemApplicationProcess;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBProcessManager sharedInstance];
+[FBProcessManager sharedInstanceIfExists];
+[FBProcessManager _sharedInstanceCreateIfNeeded:];
```

## Instance methods

```
-[FBProcessManager eventDispatcher];
-[FBProcessManager currentProcess];
-[FBProcessManager watchdogPolicyForProcess:eventContext:];
-[FBProcessManager registerProcessForHandle:];
-[FBProcessManager allProcesses];
-[FBProcessManager _notifyObserversUsingBlock:completion:];
-[FBProcessManager _noteShellInitializationComplete];
-[FBProcessManager syncLocalSceneClientProvider];
-[FBProcessManager defaultWatchdogPolicy];
-[FBProcessManager _removeProcess:];
-[FBProcessManager domain:didReceiveConnection:];
-[FBProcessManager processesForBundleIdentifier:];
-[FBProcessManager removeObserver:];
-[FBProcessManager init];
-[FBProcessManager noteProcessDidLaunch:];
-[FBProcessManager _createProcessFutureWithExecutionContext:error:];
-[FBProcessManager add:];
-[FBProcessManager _bootstrap_consumeLock_addProcess:];
-[FBProcessManager systemApplicationProcess];
-[FBProcessManager remove:];
-[FBProcessManager incomingWorkspaceEndpoint];
-[FBProcessManager dealloc];
-[FBProcessManager applicationProcessForPID:];
-[FBProcessManager processForVersionedPID:];
-[FBProcessManager _bootstrapProcessWithHandle:synchronously:error:];
-[FBProcessManager registerProcessForAuditToken:];
-[FBProcessManager _createProcessFutureForProcessHandle:error:];
-[FBProcessManager _registerProcessForMonitorableProcessHandle:error:];
-[FBProcessManager addObserver:];
-[FBProcessManager legacySceneManagerCreatingIfNecessary:];
-[FBProcessManager processForIdentity:];
-[FBProcessManager noteProcessAssertionStateDidChange:];
-[FBProcessManager _bootstrap_consumeLock_addProcess:synchronously:];
-[FBProcessManager _createProcessWithExecutionContext:error:];
-[FBProcessManager launchProcessWithContext:];
-[FBProcessManager _bootstrapProcessWithExecutionContext:synchronously:error:];
-[FBProcessManager description];
-[FBProcessManager applicationProcessesForBundleIdentifier:];
-[FBProcessManager allApplicationProcesses];
-[FBProcessManager _bestProcessForOpenApplicationIdentifier:];
-[FBProcessManager noteProcessDidExit:];
-[FBProcessManager _reallyRegisterProcessForHandle:];
-[FBProcessManager processForPID:];
-[FBProcessManager setDefaultWatchdogPolicy:];
```
