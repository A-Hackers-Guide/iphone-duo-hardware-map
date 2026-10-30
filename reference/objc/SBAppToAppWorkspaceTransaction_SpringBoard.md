# `SBAppToAppWorkspaceTransaction`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBToAppsWorkspaceTransaction`
- 6 instance variables, 1 properties, 29 instance methods, 0 class methods

## Instance variables

```
@"SBAutoPIPWorkspaceTransaction" _autoPIPTransaction;
@"SBUIAnimationController" _animation;
Q _autoPIPTransitionOrder;
@"NSObject<OS_dispatch_group>" _pipDuringSwitchTransitionTasksGroup;
@"BSTransaction" _pendingPunchoutTransaction;
B _preventWhitePointAdaptationStrengthUpdateOnComplete;
```

## Properties

```
@property (TB,N,V_preventWhitePointAdaptationStrengthUpdateOnComplete) preventWhitePointAdaptationStrengthUpdateOnComplete;
```

## Instance methods

```
-[SBAppToAppWorkspaceTransaction canInterruptForTransitionRequest:];
-[SBAppToAppWorkspaceTransaction _canBeInterrupted];
-[SBAppToAppWorkspaceTransaction _didComplete];
-[SBAppToAppWorkspaceTransaction _begin];
-[SBAppToAppWorkspaceTransaction _clearAnimation];
-[SBAppToAppWorkspaceTransaction _animationDidRevealApplication];
-[SBAppToAppWorkspaceTransaction _handleApplicationDidNotChange:];
-[SBAppToAppWorkspaceTransaction debugDescription];
-[SBAppToAppWorkspaceTransaction _beginTransition];
-[SBAppToAppWorkspaceTransaction _concurrentOverlayDismissalOptions];
-[SBAppToAppWorkspaceTransaction dealloc];
-[SBAppToAppWorkspaceTransaction _hasPostAnimationTasks];
-[SBAppToAppWorkspaceTransaction _setupAnimation];
-[SBAppToAppWorkspaceTransaction _serialOverlayPreDismissalOptions];
-[SBAppToAppWorkspaceTransaction _cleanUpAfterAnimation];
-[SBAppToAppWorkspaceTransaction _transitionWasCancelled];
-[SBAppToAppWorkspaceTransaction _setupAnimationFrom:to:];
-[SBAppToAppWorkspaceTransaction preventWhitePointAdaptationStrengthUpdateOnComplete];
-[SBAppToAppWorkspaceTransaction shouldAnimateOrientationChangeOnCompletion];
-[SBAppToAppWorkspaceTransaction _handleApplicationUpdateScenesTransactionFailed:];
-[SBAppToAppWorkspaceTransaction _animationWillBegin:];
-[SBAppToAppWorkspaceTransaction _performPostAnimationTasksWithCompletion:];
-[SBAppToAppWorkspaceTransaction setPreventWhitePointAdaptationStrengthUpdateOnComplete:];
-[SBAppToAppWorkspaceTransaction initWithTransitionRequest:];
-[SBAppToAppWorkspaceTransaction _performPreAnimationTasksWithCompletion:];
-[SBAppToAppWorkspaceTransaction initWithTransitionRequest:applicationController:];
-[SBAppToAppWorkspaceTransaction shouldPerformToAppStateCleanupOnCompletion];
-[SBAppToAppWorkspaceTransaction _shouldResignActiveForAnimation];
-[SBAppToAppWorkspaceTransaction _hasPreAnimationTasks];
```
