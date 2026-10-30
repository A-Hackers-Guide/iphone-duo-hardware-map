# `FBApplicationProcessLaunchTransaction`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBTransaction`
- 7 instance variables, 3 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"FBProcessManager" _processManager;
@"RBSProcessIdentity" _identity;
@"FBProcess" _process;
@? _executionContextProvider;
@"FBWaitForProcessDeathTransaction" _deathTransaction;
@"FBProcessExecutionContext" _executionContext;
@"BSAtomicSignal" _interruptedOrComplete;
```

## Properties

```
@property (T@"FBProcess",R,N,V_process) process;
@property (TB,R,N) failedLaunch;
@property (TB,R,N) exited;
```

## Instance methods

```
-[FBApplicationProcessLaunchTransaction exited];
-[FBApplicationProcessLaunchTransaction _childTransactionDidComplete:];
-[FBApplicationProcessLaunchTransaction _canBeInterrupted];
-[FBApplicationProcessLaunchTransaction _didComplete];
-[FBApplicationProcessLaunchTransaction _begin];
-[FBApplicationProcessLaunchTransaction _willFailWithReason:];
-[FBApplicationProcessLaunchTransaction initWithProcessIdentity:executionContextProvider:];
-[FBApplicationProcessLaunchTransaction failedLaunch];
-[FBApplicationProcessLaunchTransaction _customizedDescriptionProperties];
-[FBApplicationProcessLaunchTransaction removeObserver:];
-[FBApplicationProcessLaunchTransaction init];
-[FBApplicationProcessLaunchTransaction add:];
-[FBApplicationProcessLaunchTransaction process];
-[FBApplicationProcessLaunchTransaction remove:];
-[FBApplicationProcessLaunchTransaction addObserver:];
-[FBApplicationProcessLaunchTransaction _shouldFailForChildTransaction:];
-[FBApplicationProcessLaunchTransaction _queue_finishProcessLaunch:];
-[FBApplicationProcessLaunchTransaction _willComplete];
-[FBApplicationProcessLaunchTransaction _willInterruptWithReason:];
-[FBApplicationProcessLaunchTransaction initWithApplicationProcess:];
-[FBApplicationProcessLaunchTransaction initWithApplicationBundleID:executionContextProvider:];
-[FBApplicationProcessLaunchTransaction _queue_launchProcess:];
-[FBApplicationProcessLaunchTransaction _queue_noteExited];
-[FBApplicationProcessLaunchTransaction _queue_processWillLaunch:];
```
