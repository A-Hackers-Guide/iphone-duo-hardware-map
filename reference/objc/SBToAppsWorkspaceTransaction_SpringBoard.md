# `SBToAppsWorkspaceTransaction`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBMainWorkspaceTransaction`
- Protocols: `SBSceneLayoutWorkspaceTransactionDelegate`, `FBSynchronizedTransactionDelegate`, `SBUIAnimationControllerObserver`
- 21 instance variables, 12 properties, 79 instance methods, 1 class methods

## Instance variables

```
@"NSMutableSet" _layoutTransitionCompletions;
@"UIApplicationSceneDeactivationAssertion" _resignActiveAssertion;
@? _layoutTransitionContinuation;
@"SBAppRepairTransaction" _appRepairTransaction;
@"SBUIAnimationController" _animationController;
@"SBSwitcherCoordinatedLayoutStateTransitionContext" _coordinatedLayoutStateTransitionContext;
@"SBApplicationController" _applicationController;
@"NSCountedSet" _completionDelayRequesters;
B _underLockScreenInForeground;
B _gestureInitiated;
Q _preactivationForegroundRunningApplicationCount;
B _toAndFromApplicationsDiffer;
B _retriedAfterVoluntaryExit;
B _applicationStateNeedsCapture;
B _dismissedOverlays;
B _shouldSerialDismissOverlays;
B _touchCancellationDisabled;
@"SBSceneLayoutWorkspaceTransaction" _layoutTransaction;
@"NSSet" _ancillaryLayoutTransactions;
@"NSSet" _ancillaryTransitionRequests;
@"SBFloatingDockBehaviorAssertion" _floatingDockBehaviorAssertion;
```

## Properties

```
@property (T@"SBFloatingDockBehaviorAssertion",&,N,V_floatingDockBehaviorAssertion) floatingDockBehaviorAssertion;
@property (T@"NSSet",R,N) toApplicationSceneEntities;
@property (T@"NSSet",R,N) fromApplicationSceneEntities;
@property (T@"SBSceneLayoutWorkspaceTransaction",R,N,V_layoutTransaction) layoutTransaction;
@property (T@"NSSet",R,N,V_ancillaryTransitionRequests) ancillaryTransitionRequests;
@property (T@"NSSet",R,N,V_ancillaryLayoutTransactions) ancillaryLayoutTransactions;
@property (T@"NSSet",R,N) allTransitionRequests;
@property (T@"NSSet",R,N) allLayoutTransactions;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBToAppsWorkspaceTransaction canInterruptTransaction:forTransitionRequest:];
```

## Instance methods

```
-[SBToAppsWorkspaceTransaction animationController];
-[SBToAppsWorkspaceTransaction _childTransactionDidComplete:];
-[SBToAppsWorkspaceTransaction _willBegin];
-[SBToAppsWorkspaceTransaction _canBeInterrupted];
-[SBToAppsWorkspaceTransaction _didComplete];
-[SBToAppsWorkspaceTransaction _willFailWithReason:];
-[SBToAppsWorkspaceTransaction _clearAnimation];
-[SBToAppsWorkspaceTransaction _animationDidRevealApplication];
-[SBToAppsWorkspaceTransaction _handleApplicationDidNotChange:];
-[SBToAppsWorkspaceTransaction synchronizedTransaction:willCommitSynchronizedTransactions:];
-[SBToAppsWorkspaceTransaction _beginTransition];
-[SBToAppsWorkspaceTransaction synchronizedTransaction:didCommitSynchronizedTransactions:];
-[SBToAppsWorkspaceTransaction _customizedDescriptionProperties];
-[SBToAppsWorkspaceTransaction _concurrentOverlayDismissalOptions];
-[SBToAppsWorkspaceTransaction setFloatingDockBehaviorAssertion:];
-[SBToAppsWorkspaceTransaction dealloc];
-[SBToAppsWorkspaceTransaction _endTransition];
-[SBToAppsWorkspaceTransaction _hasPostAnimationTasks];
-[SBToAppsWorkspaceTransaction _setupAnimation];
-[SBToAppsWorkspaceTransaction _serialOverlayPreDismissalOptions];
-[SBToAppsWorkspaceTransaction _transitionWasCancelled];
-[SBToAppsWorkspaceTransaction _shouldFailForChildTransaction:];
-[SBToAppsWorkspaceTransaction _logForInterruptAttemptReason:];
-[SBToAppsWorkspaceTransaction floatingDockBehaviorAssertion];
-[SBToAppsWorkspaceTransaction shouldAnimateOrientationChangeOnCompletion];
-[SBToAppsWorkspaceTransaction _handleApplicationUpdateScenesTransactionFailed:];
-[SBToAppsWorkspaceTransaction _willInterruptWithReason:];
-[SBToAppsWorkspaceTransaction fromApplicationSceneEntities];
-[SBToAppsWorkspaceTransaction _animationWillBegin:];
-[SBToAppsWorkspaceTransaction _performPostAnimationTasksWithCompletion:];
-[SBToAppsWorkspaceTransaction toApplicationSceneEntities];
-[SBToAppsWorkspaceTransaction animationControllerDidFinishAnimation:];
-[SBToAppsWorkspaceTransaction _performPreAnimationTasksWithCompletion:];
-[SBToAppsWorkspaceTransaction synchronizedTransactionReadyToCommit:];
-[SBToAppsWorkspaceTransaction initWithTransitionRequest:applicationController:];
-[SBToAppsWorkspaceTransaction shouldPerformToAppStateCleanupOnCompletion];
-[SBToAppsWorkspaceTransaction _shouldResignActiveForAnimation];
-[SBToAppsWorkspaceTransaction _didInterruptWithReason:];
-[SBToAppsWorkspaceTransaction _hasPreAnimationTasks];
-[SBToAppsWorkspaceTransaction _beginAnimation];
-[SBToAppsWorkspaceTransaction _transitionContext];
-[SBToAppsWorkspaceTransaction watchdogTimeout];
-[SBToAppsWorkspaceTransaction shouldWatchdog:];
-[SBToAppsWorkspaceTransaction _milestoneForLayoutTransaction:];
-[SBToAppsWorkspaceTransaction _acquireResignActiveAssertion];
-[SBToAppsWorkspaceTransaction _animationDidFinish];
-[SBToAppsWorkspaceTransaction _beginAnimationIfNecessary];
-[SBToAppsWorkspaceTransaction _captureApplicationState];
-[SBToAppsWorkspaceTransaction _checkForAnimationCompletion];
-[SBToAppsWorkspaceTransaction _completeCurrentTransition];
-[SBToAppsWorkspaceTransaction _configureAnimation];
-[SBToAppsWorkspaceTransaction _delayTransitionCompletionForRequester:];
-[SBToAppsWorkspaceTransaction _fireAndClearResultBlockIfNecessaryForFailure:];
-[SBToAppsWorkspaceTransaction _isGoingToHomeScreenForTransitionRequest:];
-[SBToAppsWorkspaceTransaction _noteAnimationFinished];
-[SBToAppsWorkspaceTransaction _relinquishResignActiveAssertion];
-[SBToAppsWorkspaceTransaction _setShouldSerialDismissOverlays:];
-[SBToAppsWorkspaceTransaction _shouldSerialDismissOverlays];
-[SBToAppsWorkspaceTransaction _stopDelayingTransitionCompletionForRequester:];
-[SBToAppsWorkspaceTransaction _synchronizeWithSceneUpdates];
-[SBToAppsWorkspaceTransaction activateApplications];
-[SBToAppsWorkspaceTransaction allLayoutTransactions];
-[SBToAppsWorkspaceTransaction allTransitionRequests];
-[SBToAppsWorkspaceTransaction ancillaryLayoutTransactions];
-[SBToAppsWorkspaceTransaction ancillaryTransitionRequests];
-[SBToAppsWorkspaceTransaction animationController:willBeginAnimation:];
-[SBToAppsWorkspaceTransaction animationControllerDidRevealApplication:];
-[SBToAppsWorkspaceTransaction createSceneEntityForHandle:];
-[SBToAppsWorkspaceTransaction isGoingToCoverSheet];
-[SBToAppsWorkspaceTransaction isGoingToLauncher];
-[SBToAppsWorkspaceTransaction isGoingToMainSwitcher];
-[SBToAppsWorkspaceTransaction layoutTransaction];
-[SBToAppsWorkspaceTransaction performToAppStateCleanup];
-[SBToAppsWorkspaceTransaction shouldPlaceOutgoingScenesUnderLockOnCompletion];
-[SBToAppsWorkspaceTransaction toAndFromAppsDiffer];
-[SBToAppsWorkspaceTransaction transaction:didEndLayoutTransitionWithContinuation:];
-[SBToAppsWorkspaceTransaction transaction:performTransitionWithCompletion:];
-[SBToAppsWorkspaceTransaction transaction:shouldKeepSceneForeground:withReason:];
-[SBToAppsWorkspaceTransaction transactionWillBeginLayoutTransition:];
```
