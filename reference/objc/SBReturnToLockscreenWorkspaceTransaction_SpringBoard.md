# `SBReturnToLockscreenWorkspaceTransaction`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBActivateAppUnderLockScreenWorkspaceTransaction`
- 3 instance variables, 0 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"SBApplicationSceneEntity" _fromAppSceneEntity;
B _workspaceAlreadyResumed;
B _animatedAppDeactivation;
```

## Instance methods

```
-[SBReturnToLockscreenWorkspaceTransaction _didComplete];
-[SBReturnToLockscreenWorkspaceTransaction debugDescription];
-[SBReturnToLockscreenWorkspaceTransaction _setupAnimation];
-[SBReturnToLockscreenWorkspaceTransaction _serialOverlayPreDismissalOptions];
-[SBReturnToLockscreenWorkspaceTransaction _animationWillBegin:];
-[SBReturnToLockscreenWorkspaceTransaction _animationDidFinish];
-[SBReturnToLockscreenWorkspaceTransaction initWithTransitionRequest:lockScreenEnvironment:applicationController:];
```
