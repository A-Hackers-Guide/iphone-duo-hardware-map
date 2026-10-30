# `SBSceneLayoutWorkspaceTransaction`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWorkspaceTransaction`
- Protocols: `FBSynchronizedTransactionGroupDelegate`, `SBApplicationSceneUpdateTransactionObserver`, `FBSynchronizedTransaction`
- 25 instance variables, 12 properties, 49 instance methods, 0 class methods

## Instance variables

```
@"<SBSceneLayoutWorkspaceTransactionDelegate>" _delegate;
Q _options;
@"<BSInvalidatable>" _displayLayoutTransitionAssertion;
@"NSString" _preferredDisplayLayoutTransitionReason;
B _isTransitioning;
B _transitionFailed;
B _delegateTransitionComplete;
B _performSceneUpdates;
B _waitForSceneUpdates;
B _waitingForSynchronizedCommit;
@"SBSceneLayoutSynchronizeTransitionTransaction" _synchronizePrepareTransitionTransaction;
@"SBSceneLayoutSynchronizeTransitionTransaction" _synchronizeSendActivationResultTransaction;
@"SBSceneLayoutSynchronizeTransitionTransaction" _synchronizeBeginTransitionTransaction;
@"SBWorkspaceApplicationSceneTransitionContext" _transitionContext;
@"FBSynchronizedTransactionGroup" _sceneUpdateTransactionGroup;
@"SBSceneBackgroundedStatusAssertion" _scenesBackgroundedStatusAssertion;
@"NSMutableSet" _updateTransactions;
@"NSMutableSet" _toAppSceneEntities;
@"NSMutableSet" _fromAppSceneEntities;
@"NSMutableSet" _foregroundingAppSceneEntities;
@"NSMutableSet" _backgroundingAppSceneEntities;
@"NSMutableSet" _scenesToBackground;
@"SBWorkspaceTransitionRequest" _interruptingTransitionRequest;
@"SBApplicationController" _applicationController;
@"<FBSynchronizedTransactionDelegate>" _synchronizationDelegate;
```

## Properties

```
@property (T@"<SBSceneLayoutWorkspaceTransactionDelegate>",W,N,V_delegate) delegate;
@property (TQ,N,V_options) options;
@property (TB,R,N,GisTransitioning,V_isTransitioning) transitioning;
@property (T@"SBWorkspaceApplicationSceneTransitionContext",R,N,V_transitionContext) transitionContext;
@property (T@"NSSet",R,N,V_updateTransactions) sceneUpdateTransactions;
@property (T@"NSSet",R,N) toApplicationSceneEntities;
@property (T@"NSSet",R,N) fromApplicationSceneEntities;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<FBSynchronizedTransactionDelegate>",W,N,V_synchronizationDelegate) synchronizationDelegate;
```

## Instance methods

```
-[SBSceneLayoutWorkspaceTransaction _childTransactionDidComplete:];
-[SBSceneLayoutWorkspaceTransaction canInterruptForTransitionRequest:];
-[SBSceneLayoutWorkspaceTransaction sceneManager];
-[SBSceneLayoutWorkspaceTransaction isReadyForSynchronizedCommit];
-[SBSceneLayoutWorkspaceTransaction performSynchronizedCommit];
-[SBSceneLayoutWorkspaceTransaction _overrideInterfaceOrientationForOrientationMismatch:];
-[SBSceneLayoutWorkspaceTransaction sceneUpdateTransactions];
-[SBSceneLayoutWorkspaceTransaction _willBegin];
-[SBSceneLayoutWorkspaceTransaction _canBeInterrupted];
-[SBSceneLayoutWorkspaceTransaction _didComplete];
-[SBSceneLayoutWorkspaceTransaction _begin];
-[SBSceneLayoutWorkspaceTransaction setSynchronizationDelegate:];
-[SBSceneLayoutWorkspaceTransaction _willFailWithReason:];
-[SBSceneLayoutWorkspaceTransaction transaction:willLaunchProcess:];
-[SBSceneLayoutWorkspaceTransaction setOptions:];
-[SBSceneLayoutWorkspaceTransaction _defaultDisplayLayoutTransitionReason];
-[SBSceneLayoutWorkspaceTransaction synchronizedTransaction:willCommitSynchronizedTransactions:];
-[SBSceneLayoutWorkspaceTransaction synchronizedTransaction:didCommitSynchronizedTransactions:];
-[SBSceneLayoutWorkspaceTransaction synchronizationDelegate];
-[SBSceneLayoutWorkspaceTransaction transitionContext];
-[SBSceneLayoutWorkspaceTransaction transaction:didCommitSceneUpdate:];
-[SBSceneLayoutWorkspaceTransaction isTransitioning];
-[SBSceneLayoutWorkspaceTransaction _updateKeyboardContextMaskStyles:];
-[SBSceneLayoutWorkspaceTransaction _runningOnManagedDisplay];
-[SBSceneLayoutWorkspaceTransaction dealloc];
-[SBSceneLayoutWorkspaceTransaction _performTransition];
-[SBSceneLayoutWorkspaceTransaction _completeTransition];
-[SBSceneLayoutWorkspaceTransaction _evaluateTransitionCompletion];
-[SBSceneLayoutWorkspaceTransaction _updateScenesForTransitionCompletion];
-[SBSceneLayoutWorkspaceTransaction setDelegate:];
-[SBSceneLayoutWorkspaceTransaction _sceneEntities:hasEntityRepresentingSceneID:];
-[SBSceneLayoutWorkspaceTransaction synchronizedTransactionGroup:shouldFailForSynchronizedTransaction:];
-[SBSceneLayoutWorkspaceTransaction _collectSceneIDsOfExternallyHostedApps];
-[SBSceneLayoutWorkspaceTransaction _shouldKeepSceneForSceneHandleForeground:];
-[SBSceneLayoutWorkspaceTransaction _prepareLayoutTransition];
-[SBSceneLayoutWorkspaceTransaction _updatePreferredDisplayLayoutTransitionReason:];
-[SBSceneLayoutWorkspaceTransaction delegate];
-[SBSceneLayoutWorkspaceTransaction _prepareScenesForSceneUpdates];
-[SBSceneLayoutWorkspaceTransaction _willInterruptWithReason:];
-[SBSceneLayoutWorkspaceTransaction fromApplicationSceneEntities];
-[SBSceneLayoutWorkspaceTransaction _currentFlexibleWindowingAutoLayoutSpace];
-[SBSceneLayoutWorkspaceTransaction options];
-[SBSceneLayoutWorkspaceTransaction _beginLayoutTransition];
-[SBSceneLayoutWorkspaceTransaction _captureAppsForTransition];
-[SBSceneLayoutWorkspaceTransaction _sendActivationResultWithError:];
-[SBSceneLayoutWorkspaceTransaction toApplicationSceneEntities];
-[SBSceneLayoutWorkspaceTransaction initWithTransitionRequest:delegate:applicationController:];
-[SBSceneLayoutWorkspaceTransaction synchronizedTransactionReadyToCommit:];
-[SBSceneLayoutWorkspaceTransaction _prepareScenesForTransition];
```
