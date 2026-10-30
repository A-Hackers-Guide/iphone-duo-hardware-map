# `SBLockScreenAutoUnlockAggregateRule`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBAutoUnlockComposableRule`
- 2 instance variables, 2 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"SBFUserAuthenticationController" _userAuthenticationController;
@"SBSyncController" _syncController;
```

## Properties

```
@property (T@"SBFUserAuthenticationController",R,N,V_userAuthenticationController) userAuthenticationController;
@property (T@"SBSyncController",R,N,V_syncController) syncController;
```

## Instance methods

```
-[SBLockScreenAutoUnlockAggregateRule syncController];
-[SBLockScreenAutoUnlockAggregateRule shouldAutoUnlockForSource:];
-[SBLockScreenAutoUnlockAggregateRule initWithUserAuthenticationController:syncController:];
-[SBLockScreenAutoUnlockAggregateRule userAuthenticationController];
```
