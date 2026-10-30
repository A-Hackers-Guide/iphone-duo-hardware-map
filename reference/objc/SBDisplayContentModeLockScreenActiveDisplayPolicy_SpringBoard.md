# `SBDisplayContentModeLockScreenActiveDisplayPolicy`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBDisplayContentModeTransitionObserver`, `SBLockScreenActiveDisplayPolicyProviding`
- 6 instance variables, 6 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"SBDisplayContentModeCoordinator" _displayContentModeCoordinator;
@"NSObject<OS_dispatch_queue>" _calloutQueue;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSHashTable" _lock_observers;
@"NSHashTable" _lock_lockScreenManagers;
@"SBLockScreenManager" _lock_activeDisplayLockScreenManager;
```

## Properties

```
@property (T@"SBLockScreenManager",W,N,S_setActiveDisplayLockScreenManager:,V_lock_activeDisplayLockScreenManager) activeDisplayLockScreenManager;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"SBLockScreenManager",W,N) overrideActiveLockScreenManager;
```

## Instance methods

```
-[SBDisplayContentModeLockScreenActiveDisplayPolicy setOverrideActiveLockScreenManager:];
-[SBDisplayContentModeLockScreenActiveDisplayPolicy removeObserver:];
-[SBDisplayContentModeLockScreenActiveDisplayPolicy initWithDisplayContentModeCoordinator:];
-[SBDisplayContentModeLockScreenActiveDisplayPolicy displayContentModeCoordinator:handleDisplayContentModeTransition:];
-[SBDisplayContentModeLockScreenActiveDisplayPolicy displayContentModeCoordinator:handleSwapTransitionFromPrimaryWindowScene:toPrimaryWindowScene:withContinuationLockProvider:];
-[SBDisplayContentModeLockScreenActiveDisplayPolicy addObserver:];
-[SBDisplayContentModeLockScreenActiveDisplayPolicy activeDisplayLockScreenManager];
-[SBDisplayContentModeLockScreenActiveDisplayPolicy removeLockScreenManager:];
-[SBDisplayContentModeLockScreenActiveDisplayPolicy addLockScreenManager:];
-[SBDisplayContentModeLockScreenActiveDisplayPolicy overrideActiveLockScreenManager];
-[SBDisplayContentModeLockScreenActiveDisplayPolicy _isAnyWindowSceneUILockedForTransitionContext:];
-[SBDisplayContentModeLockScreenActiveDisplayPolicy _setActiveDisplayLockScreenManager:];
-[SBDisplayContentModeLockScreenActiveDisplayPolicy _updateActiveDisplayLockScreenManager];
-[SBDisplayContentModeLockScreenActiveDisplayPolicy _updateActiveDisplayLockScreenManagerWithPrimaryWindowScene:];
```
