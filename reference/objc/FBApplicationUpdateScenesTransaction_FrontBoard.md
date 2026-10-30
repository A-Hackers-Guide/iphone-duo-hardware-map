# `FBApplicationUpdateScenesTransaction`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSynchronizedTransactionGroup`
- Protocols: `FBApplicationProcessLaunchTransactionObserver`, `FBUpdateSceneTransactionObserver`
- 7 instance variables, 7 properties, 38 instance methods, 0 class methods

## Instance variables

```
@"FBSSceneClientIdentity" _clientIdentity;
@"FBApplicationProcessLaunchTransaction" _processLaunchTransaction;
B _hasScheduledProcessLaunch;
B _processLaunched;
B _waitsForSceneCommits;
@"NSMutableArray" _updateSceneTransactions;
@"NSMutableArray" _pendingUpdateTransactions;
```

## Properties

```
@property (T@"FBApplicationProcess",R,N) process;
@property (TB,N,V_waitsForSceneCommits) waitsForSceneCommits;
@property (T@"NSString",R,N) bundleID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FBApplicationUpdateScenesTransaction _childTransactionDidComplete:];
-[FBApplicationUpdateScenesTransaction _willBegin];
-[FBApplicationUpdateScenesTransaction _canBeInterrupted];
-[FBApplicationUpdateScenesTransaction _didComplete];
-[FBApplicationUpdateScenesTransaction _willFailWithReason:];
-[FBApplicationUpdateScenesTransaction transaction:willLaunchProcess:];
-[FBApplicationUpdateScenesTransaction _updateSceneWithIdentity:parameters:transitionContext:];
-[FBApplicationUpdateScenesTransaction initWithProcessIdentity:executionContextProvider:];
-[FBApplicationUpdateScenesTransaction updateSceneWithIdentity:parameters:transitionContext:];
-[FBApplicationUpdateScenesTransaction _customizedDescriptionProperties];
-[FBApplicationUpdateScenesTransaction removeObserver:];
-[FBApplicationUpdateScenesTransaction init];
-[FBApplicationUpdateScenesTransaction add:];
-[FBApplicationUpdateScenesTransaction _childTransactionDidFinishWork:];
-[FBApplicationUpdateScenesTransaction process];
-[FBApplicationUpdateScenesTransaction remove:];
-[FBApplicationUpdateScenesTransaction transaction:didLaunchProcess:];
-[FBApplicationUpdateScenesTransaction _noteWillCommitUpdateForScene:];
-[FBApplicationUpdateScenesTransaction addObserver:];
-[FBApplicationUpdateScenesTransaction _shouldFailForChildTransaction:];
-[FBApplicationUpdateScenesTransaction _executeProcessLaunchIfAppropriate];
-[FBApplicationUpdateScenesTransaction setWaitsForSceneCommits:];
-[FBApplicationUpdateScenesTransaction _willAddChildTransaction:];
-[FBApplicationUpdateScenesTransaction initWithClientIdentity:executionContextProvider:];
-[FBApplicationUpdateScenesTransaction updateSceneTransactionWillUpdateScene:];
-[FBApplicationUpdateScenesTransaction _didSatisfyMilestone:];
-[FBApplicationUpdateScenesTransaction _didRemoveChildTransaction:];
-[FBApplicationUpdateScenesTransaction updateSceneTransactionDidCreateScene:];
-[FBApplicationUpdateScenesTransaction _willInterruptWithReason:];
-[FBApplicationUpdateScenesTransaction updateSceneTransactionDidCommitUpdate:];
-[FBApplicationUpdateScenesTransaction bundleID];
-[FBApplicationUpdateScenesTransaction updateSceneTransactionWillCommitUpdate:];
-[FBApplicationUpdateScenesTransaction waitsForSceneCommits];
-[FBApplicationUpdateScenesTransaction _executeSceneUpdatesIfAppropriate];
-[FBApplicationUpdateScenesTransaction initWithApplicationBundleID:executionContextProvider:];
-[FBApplicationUpdateScenesTransaction _noteDidCommitUpdateForScene:];
-[FBApplicationUpdateScenesTransaction updateSceneWithIdentifier:parameters:transitionContext:];
-[FBApplicationUpdateScenesTransaction _isReadyToLaunch];
```
