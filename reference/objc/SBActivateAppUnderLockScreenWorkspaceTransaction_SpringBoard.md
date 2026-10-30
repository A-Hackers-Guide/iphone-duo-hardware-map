# `SBActivateAppUnderLockScreenWorkspaceTransaction`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBToAppsWorkspaceTransaction`
- 2 instance variables, 0 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"<SBLockScreenEnvironment>" _lockScreenEnvironment;
@"SBDisableActiveInterfaceOrientationChangeAssertion" _disableActiveOrientationChangeAssertion;
```

## Instance methods

```
-[SBActivateAppUnderLockScreenWorkspaceTransaction _didComplete];
-[SBActivateAppUnderLockScreenWorkspaceTransaction _begin];
-[SBActivateAppUnderLockScreenWorkspaceTransaction dealloc];
-[SBActivateAppUnderLockScreenWorkspaceTransaction shouldPerformToAppStateCleanupOnCompletion];
-[SBActivateAppUnderLockScreenWorkspaceTransaction _activateLockScreen];
-[SBActivateAppUnderLockScreenWorkspaceTransaction _lockScreenDidActivate];
-[SBActivateAppUnderLockScreenWorkspaceTransaction _setupAndActivate];
-[SBActivateAppUnderLockScreenWorkspaceTransaction initWithTransitionRequest:lockScreenEnvironment:applicationController:];
-[SBActivateAppUnderLockScreenWorkspaceTransaction shouldPlaceOutgoingScenesUnderLockOnCompletion];
```
