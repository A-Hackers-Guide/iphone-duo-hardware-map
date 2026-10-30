# `SBFluidSwitcherGestureWorkspaceTransaction`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSystemGestureWorkspaceTransaction`
- Protocols: `SBUIAnimationControllerObserver`, `SBSceneLayoutWorkspaceTransactionDelegate`, `SBWorkspaceApplicationSceneTransitionContextDelegate`, `SBViewMorphAnimatorObserver`
- 30 instance variables, 24 properties, 96 instance methods, 0 class methods

## Instance variables

```
B _calledBeginWithGesture;
B _hasActiveLayoutStateTransitionCoordinatorTransition;
B _hasCompletedFirstCACommitSinceTransactionBeganForPPT;
q _numberOfAppLayoutsTraveledWithArcSwipe;
d _digitizerSurfaceHeightForLastGestureEvent;
B _isPointerTouch;
Q _hidEventSenderID;
@"NSMutableSet" _sceneIdentifiersWithSceneUpdateTransactionsInProgress;
@"NSMutableDictionary" _pendingSceneUpdateTransactionsBySceneIdentifier;
B _hasLoggedDiagnosticMessage;
B _shouldCancelGestureUponInterruption;
B _hasCompletedAtLeastOneGesture;
@"SBSwitcherController" _switcherController;
@"SBFluidSwitcherViewController" _switcherViewController;
@"SBUISwitcherAnimationController" _animationController;
@"SBSceneLayoutWorkspaceTransaction" _layoutTransaction;
@"<SBFluidSwitcherGestureWorkspaceTransactionDelegate>" _delegate;
@"SBApplicationController" _applicationController;
@"UIApplicationSceneDeactivationAssertion" _backgroundingScenesDeactivationAssertion;
@"NSMapTable" _originalLayoutStatesBySwitcherController;
@"NSMapTable" _activeLayoutStatesBySwitcherController;
@"SBMainWorkspaceTransaction" _finalRootTransaction;
@"NSMutableSet" _ancillaryLayoutTransactions;
@"NSMutableSet" _layoutTransitionCompletions;
@"SBAutoPIPWorkspaceTransaction" _autoPIPWorkspaceTransaction;
@"NSTimer" _activateScenesTimer;
@"SBTransientOverlayViewController" _switcherTransitioningTransientOverlayViewController;
@"NSCountedSet" _completionDeferralReasons;
@"NSUUID" _gestureID;
@"SBAppLayout" _selectedAppLayout;
```

## Properties

```
@property (T@"SBFluidSwitcherViewController",W,N,V_switcherViewController) switcherViewController;
@property (T@"<SBFluidSwitcherGestureWorkspaceTransactionDelegate>",W,N,V_delegate) delegate;
@property (T@"SBApplicationController",&,N,V_applicationController) applicationController;
@property (T@"UIApplicationSceneDeactivationAssertion",&,N,V_backgroundingScenesDeactivationAssertion) backgroundingScenesDeactivationAssertion;
@property (T@"NSMapTable",&,N,V_originalLayoutStatesBySwitcherController) originalLayoutStatesBySwitcherController;
@property (T@"NSMapTable",&,N,V_activeLayoutStatesBySwitcherController) activeLayoutStatesBySwitcherController;
@property (T@"SBMainWorkspaceTransaction",&,N,V_finalRootTransaction) finalRootTransaction;
@property (T@"SBSceneLayoutWorkspaceTransaction",&,N,V_layoutTransaction) layoutTransaction;
@property (T@"NSMutableSet",&,N,V_ancillaryLayoutTransactions) ancillaryLayoutTransactions;
@property (T@"NSMutableSet",&,N,V_layoutTransitionCompletions) layoutTransitionCompletions;
@property (T@"SBAutoPIPWorkspaceTransaction",&,N,V_autoPIPWorkspaceTransaction) autoPIPWorkspaceTransaction;
@property (T@"NSTimer",&,N,V_activateScenesTimer) activateScenesTimer;
@property (T@"SBTransientOverlayViewController",&,N,V_switcherTransitioningTransientOverlayViewController) switcherTransitioningTransientOverlayViewController;
@property (T@"NSCountedSet",&,N,V_completionDeferralReasons) completionDeferralReasons;
@property (TB,R,N,V_hasCompletedAtLeastOneGesture) hasCompletedAtLeastOneGesture;
@property (T@"NSUUID",R,N,V_gestureID) gestureID;
@property (T@"SBAppLayout",&,N,V_selectedAppLayout) selectedAppLayout;
@property (T@"SBSwitcherController",R,W,N,V_switcherController) switcherController;
@property (T@"SBUISwitcherAnimationController",&,N,V_animationController) animationController;
@property (TB,N,V_shouldCancelGestureUponInterruption) shouldCancelGestureUponInterruption;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFluidSwitcherGestureWorkspaceTransaction animationController];
-[SBFluidSwitcherGestureWorkspaceTransaction switcherController];
-[SBFluidSwitcherGestureWorkspaceTransaction _childTransactionDidComplete:];
-[SBFluidSwitcherGestureWorkspaceTransaction canInterruptForTransitionRequest:];
-[SBFluidSwitcherGestureWorkspaceTransaction _canBeInterrupted];
-[SBFluidSwitcherGestureWorkspaceTransaction _didComplete];
-[SBFluidSwitcherGestureWorkspaceTransaction _begin];
-[SBFluidSwitcherGestureWorkspaceTransaction applicationController];
-[SBFluidSwitcherGestureWorkspaceTransaction transactionDidComplete:];
-[SBFluidSwitcherGestureWorkspaceTransaction _gestureType];
-[SBFluidSwitcherGestureWorkspaceTransaction setApplicationController:];
-[SBFluidSwitcherGestureWorkspaceTransaction dealloc];
-[SBFluidSwitcherGestureWorkspaceTransaction selectedAppLayout];
-[SBFluidSwitcherGestureWorkspaceTransaction applicationTransitionContext:frameForApplicationSceneEntity:];
-[SBFluidSwitcherGestureWorkspaceTransaction layoutStateForApplicationTransitionContext:];
-[SBFluidSwitcherGestureWorkspaceTransaction setDelegate:];
-[SBFluidSwitcherGestureWorkspaceTransaction previousLayoutStateForApplicationTransitionContext:];
-[SBFluidSwitcherGestureWorkspaceTransaction _finishWithGesture:];
-[SBFluidSwitcherGestureWorkspaceTransaction delegate];
-[SBFluidSwitcherGestureWorkspaceTransaction _willInterruptWithReason:];
-[SBFluidSwitcherGestureWorkspaceTransaction _shouldThrottleSceneUpdateTransactionsForSceneHandle:];
-[SBFluidSwitcherGestureWorkspaceTransaction switcherViewController];
-[SBFluidSwitcherGestureWorkspaceTransaction _beginWithGesture:];
-[SBFluidSwitcherGestureWorkspaceTransaction setAnimationController:];
-[SBFluidSwitcherGestureWorkspaceTransaction setSwitcherViewController:];
-[SBFluidSwitcherGestureWorkspaceTransaction _didInterruptWithReason:];
-[SBFluidSwitcherGestureWorkspaceTransaction _shouldComplete];
-[SBFluidSwitcherGestureWorkspaceTransaction setAncillaryLayoutTransactions:];
-[SBFluidSwitcherGestureWorkspaceTransaction setAutoPIPWorkspaceTransaction:];
-[SBFluidSwitcherGestureWorkspaceTransaction setLayoutTransitionCompletions:];
-[SBFluidSwitcherGestureWorkspaceTransaction _currentGestureEventForGesture:];
-[SBFluidSwitcherGestureWorkspaceTransaction _acquireBackgroundingScenesDeactivationAssertionForTransitionRequest:];
-[SBFluidSwitcherGestureWorkspaceTransaction _addChildWorkspaceTransaction:];
-[SBFluidSwitcherGestureWorkspaceTransaction _addWaitForSceneLayoutTransitionTransaction:forLeafAnimationControllers:];
-[SBFluidSwitcherGestureWorkspaceTransaction _beginDeferringCompletionForReason:];
-[SBFluidSwitcherGestureWorkspaceTransaction _copiedTransitionRequestFromTransitionRequest:];
-[SBFluidSwitcherGestureWorkspaceTransaction _createWorkspaceTransientOverlayForAppLayout:];
-[SBFluidSwitcherGestureWorkspaceTransaction _endDeferringCompletionForReason:];
-[SBFluidSwitcherGestureWorkspaceTransaction _failRunningLayoutStateTransition];
-[SBFluidSwitcherGestureWorkspaceTransaction _finishWithCompletionType:];
-[SBFluidSwitcherGestureWorkspaceTransaction _isDeferringCompletionForAnyReason];
-[SBFluidSwitcherGestureWorkspaceTransaction _isDeferringCompletionForReason:];
-[SBFluidSwitcherGestureWorkspaceTransaction _runSceneLayoutTransactionForTransitionRequest:updateScenes:];
-[SBFluidSwitcherGestureWorkspaceTransaction _safeAreasChangingFromSettings:toSettings:];
-[SBFluidSwitcherGestureWorkspaceTransaction _sceneHandleIsInLiveResize:];
-[SBFluidSwitcherGestureWorkspaceTransaction _sceneUpdateTransactionIsForLiveResize:];
-[SBFluidSwitcherGestureWorkspaceTransaction _startSceneUpdateTransaction:forSceneIdentifier:];
-[SBFluidSwitcherGestureWorkspaceTransaction _switcherControllerForWorkspaceTransitionRequest:];
-[SBFluidSwitcherGestureWorkspaceTransaction _switcherGestureDidUpdate:];
-[SBFluidSwitcherGestureWorkspaceTransaction _transitionRequestForApplicationTransitionContext:eventLabel:];
-[SBFluidSwitcherGestureWorkspaceTransaction _updateDigitizerSurfaceDimensions];
-[SBFluidSwitcherGestureWorkspaceTransaction _updateHomeScreenIfNecessaryForWorkspaceTransitionRequest:switcherController:];
-[SBFluidSwitcherGestureWorkspaceTransaction _updatePPTsForAnimationEndedWithFinalLayoutState:];
-[SBFluidSwitcherGestureWorkspaceTransaction _updatePPTsForGestureEnded];
-[SBFluidSwitcherGestureWorkspaceTransaction _updatePPTsForGestureTransactionBegan];
-[SBFluidSwitcherGestureWorkspaceTransaction _updateWithGesture:];
-[SBFluidSwitcherGestureWorkspaceTransaction _willBeginWithGesture:];
-[SBFluidSwitcherGestureWorkspaceTransaction _windowSceneForWorkspaceTransitionRequest:];
-[SBFluidSwitcherGestureWorkspaceTransaction _workspaceTransitionRequestForSwitcherTransitionRequest:fromGestureManager:withEventLabel:];
-[SBFluidSwitcherGestureWorkspaceTransaction activateScenesTimer];
-[SBFluidSwitcherGestureWorkspaceTransaction activeLayoutStatesBySwitcherController];
-[SBFluidSwitcherGestureWorkspaceTransaction ancillaryLayoutTransactions];
-[SBFluidSwitcherGestureWorkspaceTransaction autoPIPWorkspaceTransaction];
-[SBFluidSwitcherGestureWorkspaceTransaction backgroundingScenesDeactivationAssertion];
-[SBFluidSwitcherGestureWorkspaceTransaction completionDeferralReasons];
-[SBFluidSwitcherGestureWorkspaceTransaction createSceneEntityForHandle:];
-[SBFluidSwitcherGestureWorkspaceTransaction didEndAllAnimations];
-[SBFluidSwitcherGestureWorkspaceTransaction finalRootTransaction];
-[SBFluidSwitcherGestureWorkspaceTransaction gestureID];
-[SBFluidSwitcherGestureWorkspaceTransaction handleTransitionRequestForGestureComplete:fromGestureManager:];
-[SBFluidSwitcherGestureWorkspaceTransaction handleTransitionRequestForGestureUpdate:fromGestureManager:];
-[SBFluidSwitcherGestureWorkspaceTransaction hasCompletedAtLeastOneGesture];
-[SBFluidSwitcherGestureWorkspaceTransaction initWithTransitionRequest:switcherController:delegate:applicationController:];
-[SBFluidSwitcherGestureWorkspaceTransaction interceptTransitionRequest:];
-[SBFluidSwitcherGestureWorkspaceTransaction isLiveResize];
-[SBFluidSwitcherGestureWorkspaceTransaction layoutTransaction];
-[SBFluidSwitcherGestureWorkspaceTransaction layoutTransitionCompletions];
-[SBFluidSwitcherGestureWorkspaceTransaction originalLayoutStatesBySwitcherController];
-[SBFluidSwitcherGestureWorkspaceTransaction setActivateScenesTimer:];
-[SBFluidSwitcherGestureWorkspaceTransaction setActiveLayoutStatesBySwitcherController:];
-[SBFluidSwitcherGestureWorkspaceTransaction setBackgroundingScenesDeactivationAssertion:];
-[SBFluidSwitcherGestureWorkspaceTransaction setCompletionDeferralReasons:];
-[SBFluidSwitcherGestureWorkspaceTransaction setFinalRootTransaction:];
-[SBFluidSwitcherGestureWorkspaceTransaction setLayoutTransaction:];
-[SBFluidSwitcherGestureWorkspaceTransaction setOriginalLayoutStatesBySwitcherController:];
-[SBFluidSwitcherGestureWorkspaceTransaction setSelectedAppLayout:];
-[SBFluidSwitcherGestureWorkspaceTransaction setShouldCancelGestureUponInterruption:];
-[SBFluidSwitcherGestureWorkspaceTransaction setSwitcherTransitioningTransientOverlayViewController:];
-[SBFluidSwitcherGestureWorkspaceTransaction shouldCancelGestureUponInterruption];
-[SBFluidSwitcherGestureWorkspaceTransaction shouldSuppressMedusaKeyboardDuringGesture];
-[SBFluidSwitcherGestureWorkspaceTransaction switcherTransitioningTransientOverlayViewController];
-[SBFluidSwitcherGestureWorkspaceTransaction systemGestureStateChanged:];
-[SBFluidSwitcherGestureWorkspaceTransaction transaction:didEndLayoutTransitionWithContinuation:];
-[SBFluidSwitcherGestureWorkspaceTransaction transaction:performTransitionWithCompletion:];
-[SBFluidSwitcherGestureWorkspaceTransaction transaction:shouldKeepSceneForeground:withReason:];
-[SBFluidSwitcherGestureWorkspaceTransaction transactionWillBeginLayoutTransition:];
```
