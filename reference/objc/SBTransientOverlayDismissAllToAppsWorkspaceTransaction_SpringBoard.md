# `SBTransientOverlayDismissAllToAppsWorkspaceTransaction`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBToAppsWorkspaceTransaction`
- 5 instance variables, 0 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _switcherTransitioningTransientOverlayViewControllers;
@"SBAutoPIPWorkspaceTransaction" _autoPIPTransaction;
@"<BSInvalidatable>" _pipWindowLevelOverrideAssertionInvalidatable;
B _isUsingSwitcherAnimation;
B _beganDismissingTransientOverlays;
```

## Instance methods

```
-[SBTransientOverlayDismissAllToAppsWorkspaceTransaction canInterruptForTransitionRequest:];
-[SBTransientOverlayDismissAllToAppsWorkspaceTransaction _canBeInterrupted];
-[SBTransientOverlayDismissAllToAppsWorkspaceTransaction _didComplete];
-[SBTransientOverlayDismissAllToAppsWorkspaceTransaction _begin];
-[SBTransientOverlayDismissAllToAppsWorkspaceTransaction _concurrentOverlayDismissalOptions];
-[SBTransientOverlayDismissAllToAppsWorkspaceTransaction dealloc];
-[SBTransientOverlayDismissAllToAppsWorkspaceTransaction _setupAnimation];
-[SBTransientOverlayDismissAllToAppsWorkspaceTransaction _serialOverlayPreDismissalOptions];
-[SBTransientOverlayDismissAllToAppsWorkspaceTransaction _logForInterruptAttemptReason:];
-[SBTransientOverlayDismissAllToAppsWorkspaceTransaction _shouldAnimateTransition];
-[SBTransientOverlayDismissAllToAppsWorkspaceTransaction _shouldUseSwitcherDismissalAnimationForTransientOverlayViewController:];
-[SBTransientOverlayDismissAllToAppsWorkspaceTransaction _handleDismissOverlaysCompletion];
-[SBTransientOverlayDismissAllToAppsWorkspaceTransaction _performDismissal];
-[SBTransientOverlayDismissAllToAppsWorkspaceTransaction initWithTransitionRequest:applicationController:];
-[SBTransientOverlayDismissAllToAppsWorkspaceTransaction _shouldResignActiveForAnimation];
```
