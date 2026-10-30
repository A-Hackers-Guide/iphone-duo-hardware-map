# `SBCoverSheetToAppsWorkspaceTransaction`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBToAppsWorkspaceTransaction`
- 5 instance variables, 2 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"SBDismissOverlaysAnimationController" _dismissOverlaysAnimationController;
@"SBTransientOverlayDismissAllWorkspaceTransaction" _transientOverlayTransaction;
@"SBAutoPIPWorkspaceTransaction" _autoPIPTransaction;
B _preservesBanners;
B _forSecureAppTransition;
```

## Properties

```
@property (TB,N,V_preservesBanners) preservesBanners;
@property (TB,R,N,V_forSecureAppTransition) forSecureAppTransition;
```

## Instance methods

```
-[SBCoverSheetToAppsWorkspaceTransaction canInterruptForTransitionRequest:];
-[SBCoverSheetToAppsWorkspaceTransaction setPreservesBanners:];
-[SBCoverSheetToAppsWorkspaceTransaction _didComplete];
-[SBCoverSheetToAppsWorkspaceTransaction _begin];
-[SBCoverSheetToAppsWorkspaceTransaction dealloc];
-[SBCoverSheetToAppsWorkspaceTransaction _setupAnimation];
-[SBCoverSheetToAppsWorkspaceTransaction forSecureAppTransition];
-[SBCoverSheetToAppsWorkspaceTransaction _dismissOverlaysIfNeeded];
-[SBCoverSheetToAppsWorkspaceTransaction _logForInterruptAttemptReason:];
-[SBCoverSheetToAppsWorkspaceTransaction _dismissOverlaysOptions];
-[SBCoverSheetToAppsWorkspaceTransaction _autoPIPIfNeeded];
-[SBCoverSheetToAppsWorkspaceTransaction initWithTransitionRequest:forSecureAppTransition:applicationController:];
-[SBCoverSheetToAppsWorkspaceTransaction initWithTransitionRequest:applicationController:];
-[SBCoverSheetToAppsWorkspaceTransaction preservesBanners];
```
