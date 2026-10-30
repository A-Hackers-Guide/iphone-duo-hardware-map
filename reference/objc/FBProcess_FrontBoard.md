# `FBProcess`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBProcessBootstrapping`, `FBSProcessInternal`, `RBSProcessMatching`, `FBSProcess`
- 56 instance variables, 32 properties, 87 instance methods, 3 class methods

## Instance variables

```
@"FBProcessManager" _processManager;
i _pid;
q _versionedPID;
@"RBSProcessIdentity" _identity;
@"BSProcessHandle" _handle;
@"RBSProcessHandle" _rbsHandle;
@"NSString" _bundleIdentifier;
@"NSString" _executablePath;
@"BSAuditToken" _auditToken;
@"FBWorkspace" _workspace;
@"FBProcessExecutionContext" _executionContext;
@"NSString" _identityDescription;
@"NSString" _handleDescription;
{os_unfair_recursive_lock_s="ourl_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}"ourl_count"I} _lock;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _observerLock;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _bootstrapLock;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _watchdogProviderLock;
@"NSString" _description;
@"NSError" _bootstrapError;
@"NSMutableSet" _observerLock_observers;
@"RBSAssertion" _lock_gracefulExitAssertion;
@"NSMutableArray" _lock_launchCompletionBlocks;
@"NSMutableArray" _lock_bootstrapBlocks;
@"FBSApplicationInfo" _lock_applicationInfo;
@"FBProcessState" _lock_state;
@"RBSProcessState" _lock_rbsState;
C _lock_sceneState;
@"FBProcessCPUStatistics" _lock_watchdogCPUStatistics;
@"FBSProcessTerminationRequest" _lock_terminationRequest;
@"FBProcessWatchdogEventContext" _lock_terminationWatchdogContext;
q _terminationReason;
@"NSMutableArray" _lock_terminateRequestCompletionBlocks;
@"BSAbsoluteMachTimer" _lock_exitTimer;
@"<FBProcessWatchdogProviding>" _watchdogProvider;
@"FBProcessWatchdog" _lock_watchdog;
@"FBSProcessWatchdogPolicy" _sceneCreateWatchdogPolicy;
@"FBSProcessExecutionProvision" _lock_latestViolatedProvision;
B _lock_pendingExit;
B _lock_invalidated;
B _lock_attemptedBootstrap;
B _lock_waitForDebugger;
B _lock_updatingState;
B _lock_didExit;
B _lock_launchFinalized;
B _lock_launchSuccess;
B _lock_attemptedGracefulTermination;
q _lock_executableLivesOnSystemPartition;
q _lock_platformBinary;
B _calloutQueue_sentWillExit;
B _calloutQueue_sentDidExit;
B _calloutQueue_sentAppWillLaunch;
B _calloutQueue_sentAppDidLaunch;
@"<FBProcessDelegate>" _lock_delegate;
@"FBProcessExitContext" _lock_exitContext;
d _execTime;
@"RBSTarget" _target;
```

## Properties

```
@property (TB,R,N) executableLivesOnSystemPartition;
@property (TB,R,N,GisPlatformBinary) platformBinary;
@property (Td,R,N,V_execTime) execTime;
@property (T@"RBSTarget",R,N,V_target) target;
@property (T@"RBSProcessHandle",R,N,V_rbsHandle) rbsHandle;
@property (T@"BSAuditToken",R,N,V_auditToken) auditToken;
@property (T@"<FBProcessDelegate>",R,W,N,V_lock_delegate) delegate;
@property (T{?=I},R,N) workspaceState;
@property (TB,R,N) allowsTerminatingOnWatchdogViolations;
@property (T@"FBWorkspace",R,N,V_workspace) workspace;
@property (T@"BSProcessHandle",R,N,V_handle) handle;
@property (T@"RBSProcessIdentity",R,N,V_identity) identity;
@property (T@"FBSApplicationInfo",R,N,V_lock_applicationInfo) applicationInfo;
@property (T@"NSString",R,C,N,V_bundleIdentifier) bundleIdentifier;
@property (T@"NSString",R,C,N,V_executablePath) executablePath;
@property (T@"FBProcessExecutionContext",R,C,N,V_executionContext) executionContext;
@property (T@"FBProcessExitContext",R,N,V_lock_exitContext) exitContext;
@property (T@"FBProcessState",R,C,N) state;
@property (Ti,R,N,V_pid) pid;
@property (Tq,R,N,V_versionedPID) versionedPID;
@property (TB,R,N,GisRunning) running;
@property (TB,R,N,GisForeground) foreground;
@property (TB,R,N,GisBeingDebugged) beingDebugged;
@property (TB,R,N,GisCurrentProcess) currentProcess;
@property (TB,R,N,GisFinishedLaunching) finishedLaunching;
@property (TB,R,N,GisPendingExit) pendingExit;
@property (T@"NSString",R,C,N) name;
@property (T@"BSMachPortTaskNameRight",R,&,N) taskNameRight;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBProcess calloutQueue];
+[FBProcess _currentProcess];
+[FBProcess userInitiatedWorkloop];
```

## Instance methods

```
-[FBProcess matchesProcess:];
-[FBProcess isRunning];
-[FBProcess processPredicate];
-[FBProcess workspace];
-[FBProcess hasEntitlement:];
-[FBProcess valueForEntitlement:];
-[FBProcess isBeingDebugged];
-[FBProcess debugDescription];
-[FBProcess taskState];
-[FBProcess succinctDescriptionBuilder];
-[FBProcess removeObserver:];
-[FBProcess setWatchdogProvider:];
-[FBProcess init];
-[FBProcess visibility];
-[FBProcess isPlatformBinary];
-[FBProcess add:];
-[FBProcess remove:];
-[FBProcess dealloc];
-[FBProcess bundleIdentifier];
-[FBProcess versionedPID];
-[FBProcess descriptionWithMultilinePrefix:];
-[FBProcess isForeground];
-[FBProcess _observers];
-[FBProcess _createBootstrapContext];
-[FBProcess succinctDescription];
-[FBProcess addObserver:];
-[FBProcess invalidate];
-[FBProcess pid];
-[FBProcess executionContext];
-[FBProcess handle];
-[FBProcess delegate];
-[FBProcess _finishInit];
-[FBProcess identity];
-[FBProcess description];
-[FBProcess auditToken];
-[FBProcess target];
-[FBProcess isApplicationProcess];
-[FBProcess executablePath];
-[FBProcess name];
-[FBProcess _bootstrapDidComplete];
-[FBProcess state];
-[FBProcess descriptionBuilderWithMultilinePrefix:];
-[FBProcess execTime];
-[FBProcess finishedLaunching];
-[FBProcess taskNameRight];
-[FBProcess _terminateWithRequest:forWatchdog:];
-[FBProcess _watchdog:shouldTerminateWithDeclineReason:];
-[FBProcess _watchdog:terminationRequestForError:];
-[FBProcess rbsHandle];
-[FBProcess _configureIntrinsicsFromHandle:];
-[FBProcess applicationInfo];
-[FBProcess _bootstrapAndExec];
-[FBProcess _configureBundleInfo];
-[FBProcess _executeBlockAfterBootstrap:];
-[FBProcess _executeBlockAfterLaunchCompletes:];
-[FBProcess _executeBlockAsCurrentProcess:];
-[FBProcess _initWithProcessManager:identity:handle:executionContext:];
-[FBProcess _killForReason:andReport:withDescription:completion:];
-[FBProcess _launchDidComplete:finalizeBlock:];
-[FBProcess _lock_consumeLock_executeTerminationRequest];
-[FBProcess _lock_consumeLock_performGracefulKill];
-[FBProcess _newWatchdogForContext:completion:];
-[FBProcess _noteAssertionStateDidChange];
-[FBProcess _notePendingExitForReason:];
-[FBProcess _noteStateDidUpdate:];
-[FBProcess _processDidExitWithContext:];
-[FBProcess _rebuildState];
-[FBProcess _rebuildState:];
-[FBProcess _setSceneLifecycleState:];
-[FBProcess _shouldWatchdogWithDeclineReason:];
-[FBProcess _startWatchdogTimerForContext:];
-[FBProcess _terminateWithRequest:completion:];
-[FBProcess _updateStateWithBlock:];
-[FBProcess _watchdogProvider];
-[FBProcess _watchdogReportType];
-[FBProcess allowsTerminatingOnWatchdogViolations];
-[FBProcess bootstrapLock:];
-[FBProcess bootstrapWithDelegate:];
-[FBProcess executableLivesOnSystemPartition];
-[FBProcess exitContext];
-[FBProcess isCurrentProcess];
-[FBProcess isExtensionProcess];
-[FBProcess isFinishedLaunching];
-[FBProcess isPendingExit];
-[FBProcess isSystemApplicationProcess];
-[FBProcess noteProcessPublished];
-[FBProcess workspaceState];
```
